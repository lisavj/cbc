#!/usr/bin/env python3
"""MES / MGC 3m stop / take-profit grid on the REAL CBC setups (Alert Feed alerts + BarFeed bars).

Fetches /alerts and /bars?sym=<SYM>&days=60 from the Render dashboard, rebuilds every <SYM> 3m setup that has a
"Setup Ended" result (setups whose Trade Setup alert is missing get SL1 = 1.3 ATR cap 8 and TP1 = 2 ATR cap 6),
replays it on the 3m bars and prints a markdown report:
  - validation: replay with each setup's own stop vs the actual results (win/loss agreement)
  - grid: 14 take-profit methods x stops (current, 8, 10, 12, 14, 16 pts); * = positive in both halves
  - robustness: uncapped ATR TP1 1.5 / 2.0 / 2.5 / 3.0 x 50 / 80 % partial; T = positive in all three thirds
  - tracked ATR block: TP1 1.75/2.0/2.25 ATR x 80/90/100 % closed x trail 1.0/1.3/1.7 ATR x stop 2.0/2.5/3.0 ATR
  - MGC stop floor: own SL1 with a minimum of 3/4/5/6 pts x 5 TP methods
Exit model: stop first if a candle touches both; after TP1 the rest trails 1.7 ATR from the close; exits on the
opposite 15m CBC flip (BarFeed hc) and at 16:00 ET.
MGC 'Current' row also applies the time stop (exit at the close of candle 10 if TP1 not hit and +0.5 ATR never reached).
Usage: python3 mes_sltp_grid.py [MES|MGC] [since MM/DD]   (default: MES, all stored alerts)
"""
import json, re, sys, statistics, urllib.request, datetime as D
from zoneinfo import ZoneInfo

BASE = 'https://tv-webhook-dashboard.onrender.com'
TZ = ZoneInfo('America/New_York')
SYM = 'MES'


def get(url):
    for _ in range(2):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # Render wake-up
            err = e
    raise err


def load(since=None):
    A = get(BASE + '/alerts')
    B = get(BASE + '/bars?sym=%s&days=60' % SYM)['bars']
    ix = {b['t']: i for i, b in enumerate(B)}
    atr, a = [], None
    for i, x in enumerate(B):
        tr = max(x['h'], B[i - 1]['c']) - min(x['l'], B[i - 1]['c']) if i else x['h'] - x['l']
        a = tr if a is None else (a * 13 + tr) / 14
        atr.append(a)
    yr = D.datetime.now(TZ).year
    S, E = {}, {}
    for x in A:
        r = x['raw'] if isinstance(x['raw'], str) else ''
        if not r.startswith(SYM) or not re.search(r'Chart: \S+\s+3m', r):
            continue
        tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
        if not tm:
            continue
        mo, dd, hh, mi = map(int, tm.groups())
        if '• Trade Setup:' in r:
            en = float(re.search(r'\nEntry: ([\d.]+)', r).group(1))
            S[(mo, dd, hh, mi, en)] = r
        elif '• Setup Ended:' in r:
            st = re.search(r'Started: (\d+):(\d+)', r)
            m = re.search(r'Result: ([+-]?[\d.]+)', r)
            if not st or not m:
                continue
            en = float(re.search(r'Setup Entry: ([\d.]+)', r).group(1))
            sh, sm = int(st.group(1)), int(st.group(2))
            day = D.date(yr, mo, dd) - (D.timedelta(days=1) if (sh, sm) > (hh, mi) else D.timedelta(0))
            E[(day.month, day.day, sh, sm, en)] = (re.search(r'Setup Ended: (\w+)', r).group(1), float(m.group(1)))
    T = []
    for k, (d, res) in E.items():
        mo, dd, hh, mi, en = k
        t = D.datetime(yr, mo, dd, hh, mi, tzinfo=TZ)
        if since and t < since:
            continue
        i = ix.get(int(t.timestamp() * 1000) - 180000)
        if i is None or i < 20:
            continue
        r = S.get(k, '')
        lg = d == 'LONG'
        s = 1 if lg else -1
        tp = re.search(r'\nTP1: ([\d.]+)', r)
        sl = re.search(r'\nSL1: ([\d.]+)', r)
        T.append(dict(t=t, i=i, lg=lg, en=en, act=res, has=bool(r),
                      tp1=float(tp.group(1)) if tp else en + s * min(2 * atr[i], 6),
                      sl1=float(sl.group(1)) if sl else en - s * min(1.3 * atr[i], 8)))
    T.sort(key=lambda x: x['t'])
    return B, atr, T


def sim(B, atr, tr, d, tpm, part, trail, ts=None):
    """d = fixed stop pts (None = the setup's own SL1); tpm(tr, atr, stop) -> TP1 distance or None; part = share
    closed at TP1; trail = ATR multiple after TP1, None = no trail, 'all' = trail 1.7 ATR from entry."""
    i, lg, en = tr['i'], tr['lg'], tr['en']
    s = 1 if lg else -1
    sd = abs(en - tr['sl1']) if d is None else d
    sl = en - s * sd
    td = tpm(tr, atr[i], sd) if tpm else None
    if td is None and tpm == 'own':
        td = abs(tr['tp1'] - en)
    tp1 = None if td is None else en + s * td
    hit = False
    mfe = 0.0

    def fin(px):
        rem = (px - en) * s
        return part * td + (1 - part) * rem if hit else rem
    for j in range(i + 1, min(len(B), i + 500)):
        x = B[j]
        hi, lo, c = x['h'], x['l'], x['c']
        if (lo <= sl) if lg else (hi >= sl):
            return fin(sl)
        if tp1 is not None and not hit and ((hi >= tp1) if lg else (lo <= tp1)):
            hit = True
            if part >= 1:
                return td
        if ts and not hit:
            mfe = max(mfe, (hi - en) if lg else (en - lo))
            if j - i >= ts and mfe < 0.5 * atr[i]:
                return fin(c)
        if (hit and trail) or trail == 'all':
            m = 1.7 if trail == 'all' else trail
            ns = c - m * atr[j] if lg else c + m * atr[j]
            sl = max(sl, ns) if lg else min(sl, ns)
        hc, hp = x['hc'], B[j - 1]['hc']
        if hc is not None and hp is not None and hc != hp and ((lg and hc == 0) or (not lg and hc == 1)):
            return fin(c)
        t = D.datetime.fromtimestamp(x['t'] / 1000, TZ)
        if t.hour == 15 and t.minute >= 57:
            return fin(c)
    return 0.0


MES_METHODS = [
    ('Current: TP1 2 ATR cap 6, 80% + trail 1.7', lambda tr, a, sd: min(2 * a, 6), .8, 1.7),
    ('TP1 2 ATR no cap, 80% + trail', lambda tr, a, sd: 2 * a, .8, 1.7),
    ('TP1 6 pts, 50% + trail', lambda tr, a, sd: 6, .5, 1.7),
    ('TP1 8 pts, 80% + trail', lambda tr, a, sd: 8, .8, 1.7),
    ('TP1 10 pts, 80% + trail', lambda tr, a, sd: 10, .8, 1.7),
    ('TP 6 pts, 100%', lambda tr, a, sd: 6, 1.0, None),
    ('TP 8 pts, 100%', lambda tr, a, sd: 8, 1.0, None),
    ('TP 10 pts, 100%', lambda tr, a, sd: 10, 1.0, None),
    ('TP 12 pts, 100%', lambda tr, a, sd: 12, 1.0, None),
    ('TP 1R (= stop), 100%', lambda tr, a, sd: sd, 1.0, None),
    ('TP1 1R 50% + trail', lambda tr, a, sd: sd, .5, 1.7),
    ('TP 1.5R, 100%', lambda tr, a, sd: 1.5 * sd, 1.0, None),
    ('No TP: trail 1.7 ATR from entry', lambda tr, a, sd: None, 0, 'all'),
    ('No TP: hold to 15m flip / 16:00', lambda tr, a, sd: None, 0, None),
]
MES_STOPS = [None, 8, 10, 12, 14, 16]

MGC_METHODS = [
    ('Current: TP1 2 ATR cap 6, 50% + trail 1.7 + time stop', lambda tr, a, sd: min(2 * a, 6), .5, 1.7, 10),
    ('TP1 2 ATR no cap, 50% + trail', lambda tr, a, sd: 2 * a, .5, 1.7),
    ('TP1 2 ATR cap 6, 80% + trail', lambda tr, a, sd: min(2 * a, 6), .8, 1.7),
    ('TP1 4 pts, 50% + trail', lambda tr, a, sd: 4, .5, 1.7),
    ('TP1 6 pts, 80% + trail', lambda tr, a, sd: 6, .8, 1.7),
    ('TP1 8 pts, 80% + trail', lambda tr, a, sd: 8, .8, 1.7),
    ('TP 4 pts, 100%', lambda tr, a, sd: 4, 1.0, None),
    ('TP 6 pts, 100%', lambda tr, a, sd: 6, 1.0, None),
    ('TP 8 pts, 100%', lambda tr, a, sd: 8, 1.0, None),
    ('TP 10 pts, 100%', lambda tr, a, sd: 10, 1.0, None),
    ('TP 1R (= stop), 100%', lambda tr, a, sd: sd, 1.0, None),
    ('TP1 1R 50% + trail', lambda tr, a, sd: sd, .5, 1.7),
    ('TP 1.5R, 100%', lambda tr, a, sd: 1.5 * sd, 1.0, None),
    ('No TP: trail 1.7 ATR from entry', lambda tr, a, sd: None, 0, 'all'),
    ('No TP: hold to 15m flip / 16:00', lambda tr, a, sd: None, 0, None),
]
MGC_STOPS = [None, 3, 4, 5, 6, 8, 10]
METHODS, STOPS = MES_METHODS, MES_STOPS


def report(since=None):
    B, atr, T = load(since)
    n = len(T)
    if n < 4:
        return '# %s 3m stop / TP grid' % SYM + '\n\nNot enough setups with results (%d).' % n
    h, t3 = n // 2, n // 3
    own = [sim(B, atr, t, None, lambda tr, a, sd: abs(tr['tp1'] - tr['en']), .5 if SYM == 'MGC' else .8, 1.7,
               10 if SYM == 'MGC' else None) for t in T]
    agree = sum((o > 0) == (t['act'] > 0) for o, t in zip(own, T))
    L = ['# %s 3m stop / take-profit grid -- %s' % (SYM, D.datetime.now(TZ).strftime('%a %m/%d/%Y %H:%M ET')), '',
         'Setups with results: **%d** (%s – %s), %d without a Trade Setup alert (levels estimated). Halves split at %s.' % (
             n, T[0]['t'].strftime('%m/%d'), T[-1]['t'].strftime('%m/%d'), sum(not t['has'] for t in T), T[h]['t'].strftime('%m/%d %H:%M')),
         'Actual result %+.1f pts · replay with own levels %+.1f · win/loss agreement %d/%d.' % (sum(t['act'] for t in T), sum(own), agree, n),
         'Median actual SL1 %.1f pts · median ATR %.2f · 2 ATR > 6 pts on %d%% of setups.' % (
             statistics.median(abs(t['en'] - t['sl1']) for t in T), statistics.median(atr[t['i']] for t in T),
             round(sum(2 * atr[t['i']] > 6 for t in T) / n * 100)), '',
         '## Net pts by take-profit method × stop (✱ = positive in both halves)', '',
         '| Method | ' + ' | '.join('current' if s is None else '%d pts' % s for s in STOPS) + ' |',
         '|---|' + '---|' * len(STOPS)]
    allr = []
    for name, f, part, tr, *ts in METHODS:
        cells = []
        for s in STOPS:
            R = [sim(B, atr, t, s, f, part, tr, *ts) for t in T]
            g = sum(r for r in R if r > 0)
            l = -sum(r for r in R if r < 0)
            both = sum(R[:h]) > 0 and sum(R[h:]) > 0
            thirds = all(sum(R[k * t3:(k + 1) * t3 if k < 2 else n]) > 0 for k in range(3))
            allr.append((sum(R), name, s, sum(R[:h]), sum(R[h:]), g / l if l else 9.9, sum(r > 0 for r in R) / n, min(R), thirds))
            cells.append('%+.1f%s' % (sum(R), ' ✱' if both else ''))
        L.append('| %s | %s |' % (name, ' | '.join(cells)))
    L += ['', '## Top 8', '', '| Method | Stop | Net | Halves | PF | Win % | Worst | All 3 thirds + |', '|---|---|---|---|---|---|---|---|']
    for r in sorted(allr, key=lambda x: -x[0])[:8]:
        L.append('| %s | %s | %+.1f | %+.1f / %+.1f | %.2f | %d%% | %.1f | %s |' % (r[1], 'current' if r[2] is None else r[2], r[0], r[3], r[4], r[5], round(r[6] * 100), r[7], 'yes' if r[8] else 'no'))
    L += ['', '## Robustness: uncapped ATR TP1 (+ trail 1.7) — net pts, ✱ both halves, T all thirds', '',
          '| TP1 | ' + ' | '.join('%d pts' % s for s in STOPS[1:]) + ' |', '|---|' + '---|' * (len(STOPS) - 1)]
    for m in (1.5, 2.0, 2.5, 3.0):
        for part in (.5, .8):
            cells = []
            for s in STOPS[1:]:
                R = [sim(B, atr, t, s, lambda tr, a, sd, m=m: m * a, part, 1.7) for t in T]
                cells.append('%+.1f%s%s' % (sum(R), ' ✱' if sum(R[:h]) > 0 and sum(R[h:]) > 0 else '',
                                            ' T' if all(sum(R[k * t3:(k + 1) * t3 if k < 2 else n]) > 0 for k in range(3)) else ''))
            L.append('| %.1f ATR, %d%% | %s |' % (m, part * 100, ' | '.join(cells)))
    if SYM == 'MES':
        L += atr_block(B, atr, T)
    if SYM == 'MGC':
        L += floor_block(B, atr, T)
    L += ['', 'Rule: only act on a combination that is positive in both halves AND all three thirds, with neighbours (±0.5 ATR, ±2 pts stop) also positive, on 60+ setups.']
    return '\n'.join(L)


FLOORS = (None, 3, 4, 5, 6)
FLOOR_METHODS = [
    ('Current: TP1 2 ATR cap 6, 50% + trail 1.7 + time stop', lambda tr, a, sd: min(2 * a, 6), .5, 1.7, 10),
    ('TP1 2 ATR no cap, 50% + trail', lambda tr, a, sd: 2 * a, .5, 1.7),
    ('TP1 2 ATR no cap, 80% + trail', lambda tr, a, sd: 2 * a, .8, 1.7),
    ('TP1 2.5 ATR no cap, 50% + trail', lambda tr, a, sd: 2.5 * a, .5, 1.7),
    ('No TP: trail 1.7 ATR from entry', lambda tr, a, sd: None, 0, 'all'),
]


def floor_block(B, atr, T):
    """MGC stop floor: each setup keeps its own SL1 unless it is tighter than the floor (stop = max(own, floor)).
    ✱ both halves, T all three thirds."""
    n = len(T)
    h, t3 = n // 2, n // 3
    L = ['', '## Stop floor: own SL1, minimum X pts — net pts, ✱ both halves, T all thirds', '',
         'Stop = max(setup\'s own SL1 distance, floor). "none" = own SL1 as-is. Neighbours = ±1 pt floor.', '',
         '| Method | ' + ' | '.join('none' if f is None else 'min %d pts' % f for f in FLOORS) + ' |',
         '|---|' + '---|' * len(FLOORS)]
    for name, f, part, trl, *ts in FLOOR_METHODS:
        cells = []
        for fl in FLOORS:
            R = [sim(B, atr, t, max(abs(t['en'] - t['sl1']), fl or 0), f, part, trl, *ts) for t in T]
            cells.append('%+.1f%s%s' % (sum(R), ' ✱' if sum(R[:h]) > 0 and sum(R[h:]) > 0 else '',
                                        ' T' if all(sum(R[k * t3:(k + 1) * t3 if k < 2 else n]) > 0 for k in range(3)) else ''))
        L.append('| %s | %s |' % (name, ' | '.join(cells)))
    return L


ATR_TP = (1.75, 2.0, 2.25)
ATR_PART = (.8, .9, 1.0)
ATR_TRAIL = (1.0, 1.3, 1.7)
ATR_STOP = (2.0, 2.5, 3.0)


def atr_block(B, atr, T):
    """Tracked block: TP1 x ATR x share closed x trail x stop (ATR multiples). 100% closed = no runner, so
    the trail does not apply and one value is shown. ✱ both halves, T all thirds, R = T and every neighbour
    (one step in any of the four settings) is positive."""
    n = len(T)
    h, t3 = n // 2, n // 3
    res = {}
    for sk in ATR_STOP:
        for m in ATR_TP:
            for p in ATR_PART:
                for tk in (ATR_TRAIL if p < 1 else (None,)):
                    R = [sim(B, atr, t, sk * atr[t['i']], lambda tr, a, sd, m=m: m * a, p, tk) for t in T]
                    res[(sk, m, p, tk)] = (sum(R), sum(R[:h]) > 0 and sum(R[h:]) > 0,
                                           all(sum(R[k * t3:(k + 1) * t3 if k < 2 else n]) > 0 for k in range(3)))

    def val(sk, m, p, tk):
        return res[(sk, m, p, None if p >= 1 else tk)]

    def nbrs(sk, m, p, tk):
        out = []
        for arr, idx in ((ATR_STOP, 0), (ATR_TP, 1), (ATR_PART, 2), (ATR_TRAIL, 3)):
            key = [sk, m, p, tk if tk is not None else ATR_TRAIL[0]]
            i = arr.index(key[idx])
            for j in (i - 1, i + 1):
                if 0 <= j < len(arr):
                    k2 = list(key)
                    k2[idx] = arr[j]
                    out.append(val(*k2))
        return out

    def robust(k):
        net, both, th = res[k]
        return th and net > 0 and all(x[0] > 0 for x in nbrs(*k))

    L = ['', '## Tracked: ATR-based exits (stop & TP1 in ATR, trail after TP1) — net pts', '',
         '✱ = both halves positive · T = all three thirds positive · R = T plus every one-step neighbour positive. '
         '100% closed = no runner (trail n/a).', '']
    for sk in ATR_STOP:
        L += ['**Stop %.1f ATR**' % sk, '',
              '| TP1 | ' + ' | '.join('80%%, trail %.1f' % x for x in ATR_TRAIL) + ' | ' +
              ' | '.join('90%%, trail %.1f' % x for x in ATR_TRAIL) + ' | 100% |', '|---|' + '---|' * 7]
        for m in ATR_TP:
            cells = []
            for p in ATR_PART:
                for tk in (ATR_TRAIL if p < 1 else (None,)):
                    k = (sk, m, p, tk)
                    net, both, th = res[k]
                    cells.append('%+.1f%s%s%s' % (net, ' ✱' if both else '', ' T' if th else '', ' R' if robust(k) else ''))
            L.append('| %.2f ATR | %s |' % (m, ' | '.join(cells)))
        L.append('')
    best = max(res.items(), key=lambda kv: kv[1][0])
    rob = sorted([k for k in res if robust(k)], key=lambda k: -res[k][0])

    def nm(k):
        sk, m, p, tk = k
        return 'stop %.1f ATR, TP1 %.2f ATR, %d%%%s' % (sk, m, p * 100, '' if tk is None else ', trail %.1f' % tk)
    L += ['Cells: %d · ✱ %d · T %d · R %d · positive %d.' % (len(res), sum(v[1] for v in res.values()),
                                                           sum(v[2] for v in res.values()), len(rob), sum(v[0] > 0 for v in res.values())),
          'Best: %s = %+.1f.' % (nm(best[0]), best[1][0]),
          'Robust (R) candidates: %s.' % ('; '.join('%s = %+.1f' % (nm(k), res[k][0]) for k in rob[:5]) if rob else 'none'),
          'Ready to change: %s (needs an R cell and 60+ setups; %d now).' % ('YES' if rob and n >= 60 else 'no', n)]
    return L


if __name__ == '__main__':
    since = None
    for arg in sys.argv[1:]:
        if arg.upper() in ('MES', 'MGC'):
            SYM = arg.upper()
            if SYM == 'MGC':
                METHODS, STOPS = MGC_METHODS, MGC_STOPS
        else:
            mo, dd = map(int, arg.split('/'))
            since = D.datetime(D.datetime.now(TZ).year, mo, dd, tzinfo=TZ)
    print(report(since))
