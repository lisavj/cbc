#!/usr/bin/env python3
"""CBC "▌⑤ Alerts" parameter sweep (scheduled weekdays 17:05 ET).

Replays five alert types from the BarFeed bars under different ⑤ Alerts settings, validates the replay against
the stored Alert Feed alerts at the CURRENT settings, and scores every fired alert with two outcome rules.

Alert logic (approximated from CBC v10.41 + ESLib/ESLib2):
  HTF dir         = confirmed HTF CBC (bar field hc; hf = +1/-1 on the LTF bar where it flips). HTF = 5 x chart tf
                    (3m chart -> 15m, 2m chart -> 10m); HTF candles are rebuilt from the LTF bars.
  flip-away gate  = latched at each HTF flip: long flip with close > HTF EMA20 (short: close < HTF EMA20).
  session gate    = Asia 18:00-22:30, London 03:00-07:45, NY 09:30-17:00 ET (alert_session_ok). Cooldown /
                    throttle state still advances outside the sessions (same as Pine).
  LTF EMA20 Pierce  : range touches e20, previous bar's did not, bar - last_fire > cooldown, pullback-only
                    (long: low[1] > e20[1]; short: high[1] < e20[1]), HTF dir + flip-away.
                    Direction = f_pierce_word: close on the wrong side of e20 -> "Option 2: Reverse" (opposite).
  HTF EMA9/20 Pierce: same on h9 / h20 (own state per line), bar - last > 3 (current), flip-away gate.
  HTF Pullback - Structure Confirmed: close enters the HTF EMA9/20 band (was outside last bar), HTF dir,
                    HTF swing structure HH+HL (long) / LH+LL (short) from pivots N=1 on the rebuilt HTF candles,
                    HTF bars since the flip <= window, flip-away gate.
  In FVG of HTF Flip Candle: 3-candle FVG (candle before the flip candle / candle after), live once the candle
                    after closes; fires when the bar trades inside the gap (intrabar alert), bar - last >= gap,
                    LTF bars since the flip <= max.
  VWAP Bounce     : LTF CBC flip (close > high[1] / close < low[1] state), |close - VWAP| <= 3 pts, and the
                    distance from close to the nearest of PP/R1-3/S1-3 (standard formula rebuilt from pp/r1/s1)
                    and the active session's opening-range high/low >= min distance (0 = no gate).
Outcomes (entry = alert candle close, direction from the alert):
  (a) exit at the close of the first candle with an opposite HTF CBC flip, the candle ending 17:00 ET, or 2 h.
  (b) 1.3 ATR(14) stop / 2.0 ATR target, first hit (both in one candle = stop); unresolved -> close at 17:00 ET.
Usage: python3 alert_param_sweep.py [prev_report.md] > alert_param_report.md
"""
import gzip, json, re, sys, time, urllib.request, datetime as D
from zoneinfo import ZoneInfo

BASE = 'https://tv-webhook-dashboard.onrender.com'
TZ = ZoneInfo('America/New_York')
CASES = [('MES', 3), ('MGC', 3), ('MNQ', 3), ('MES', 2), ('MGC', 2)]
PROX = 3.0          # prox_approach_dist default
VB_AUTO = {'MES': 6, 'MGC': 6, 'MNQ': 60}
VB_GRID = {'MES': [0, 2, 4, 6, 8, 10], 'MGC': [0, 2, 4, 6, 8, 10], 'MNQ': [0, 20, 40, 60, 80]}
TYPES = {'ltf': '• LTF EMA20 Pierce', 'h9': '• HTF EMA9 Pierce', 'h20': '• HTF EMA20 Pierce',
         'pb': '• HTF Pullback Entry - Structure Confirmed', 'fvg': '• In FVG of HTF Flip Candle', 'vb': '• VWAP Bounce'}


def get(url, tries=2):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=200) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(60)


def raw(x):
    return x['raw'] if isinstance(x['raw'], str) else json.dumps(x['raw'])


def et(ms):
    return D.datetime.fromtimestamp(ms / 1000, TZ)


def in_sess(ms):
    t = et(ms)
    m = t.hour * 60 + t.minute
    return 18 * 60 <= m < 22 * 60 + 30 or 3 * 60 <= m < 7 * 60 + 45 or 9 * 60 + 30 <= m < 17 * 60


def stored_alerts(alerts, sym, tf):
    """{type: {bar_open_ms: dir}} for this symbol + chart timeframe."""
    out = {k: {} for k in TYPES}
    for x in alerts:
        r = raw(x)
        if not r.startswith(sym) or not re.search(r'Chart: \S+\s+%dm\b' % tf, r):
            continue
        tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
        if not tm:
            continue
        mo, dd, hh, mi = map(int, tm.groups())
        t = D.datetime(int(x['receivedAt'][:4]), mo, dd, hh, mi, tzinfo=TZ)
        ms = int(t.timestamp() * 1000)
        ms -= ms % (tf * 60000)
        for k, s in TYPES.items():
            m = re.search(re.escape(s) + r'[^\n]*', r)
            if m:
                ln = m.group(0)
                d = re.findall(r'(LONG|SHORT)', ln)
                out[k][ms] = (1 if d[-1] == 'LONG' else -1) if d else 0
    return out


def prep(B, tf):
    n = len(B)
    htf = tf * 5 * 60000
    # ATR(14) Wilder
    atr, a = [], None
    for i, b in enumerate(B):
        tr = max(b['h'], B[i - 1]['c']) - min(b['l'], B[i - 1]['c']) if i else b['h'] - b['l']
        a = tr if a is None else (a * 13 + tr) / 14
        atr.append(a)
    # LTF CBC
    cbc, st = [], False
    for i, b in enumerate(B):
        if i:
            if st and b['c'] < B[i - 1]['l']:
                st = False
            elif not st and b['c'] > B[i - 1]['h']:
                st = True
        cbc.append(st)
    # HTF candles rebuilt from LTF bars; hix[i] = index of HTF candle containing bar i
    H, hix = [], []
    for b in B:
        k = b['t'] - b['t'] % htf
        if not H or H[-1]['k'] != k:
            H.append(dict(k=k, h=b['h'], l=b['l']))
        else:
            H[-1]['h'] = max(H[-1]['h'], b['h']); H[-1]['l'] = min(H[-1]['l'], b['l'])
        hix.append(len(H) - 1)
    # HTF structure (pivot N=1), known once the candle after the pivot closes -> from the first LTF bar of the
    # HTF candle after that one
    hs_at = {}   # HTF candle index -> (hi_struct, lo_struct) valid from its first LTF bar
    hi_s = lo_s = None
    last_hi = last_lo = None
    for j in range(2, len(H)):
        p = H[j - 2:j + 1]
        if p[1]['h'] > p[0]['h'] and p[1]['h'] > p[2]['h']:   # ta.pivothigh: strictly greater (approx.)
            if last_hi is not None:
                hi_s = 'HH' if p[1]['h'] > last_hi else 'LH'
            last_hi = p[1]['h']
        if p[1]['l'] < p[0]['l'] and p[1]['l'] < p[2]['l']:
            if last_lo is not None:
                lo_s = 'LL' if p[1]['l'] < last_lo else 'HL'
            last_lo = p[1]['l']
        hs_at[j + 1] = (hi_s, lo_s)
    hstruct = [hs_at.get(hix[i], (None, None)) for i in range(n)]
    # if a later HTF candle had no update, carry forward
    cur = (None, None)
    for i in range(n):
        if hix[i] in hs_at:
            cur = hs_at[hix[i]]
        hstruct[i] = cur
    # HTF flip bookkeeping
    away, hbs, lbs = [False] * n, [99] * n, [9999] * n
    # setup-engine direction / flip gate (HTF EMA pierces): ats_hc_on -> the flip counts on the last chart candle
    # of the HTF candle; ats_tw_late -> after a toward flip, ok once a candle closes >= 1 pt beyond HTF EMA20 (away side)
    sdir, sok = [0] * n, [False] * n
    fvg = [None] * n
    ok, d0 = False, 0
    for i, b in enumerate(B):
        nb = B[i + 1] if i + 1 < n else None
        d = nb['hf'] if nb is not None and nb.get('hf') in (1, -1) else (1 if b['hc'] == 1 else -1)
        if d != d0:
            ok = b['c'] > b['h20'] if d == 1 else b['c'] < b['h20']
            d0 = d
        elif not ok and (b['c'] >= b['h20'] + 1 if d == 1 else b['c'] <= b['h20'] - 1):
            ok = True
        sdir[i], sok[i] = d, ok
    aw, fi, fv = False, None, None
    for i, b in enumerate(B):
        if b.get('hf') in (1, -1):
            aw = b['c'] > b['h20'] if b['hf'] == 1 else b['c'] < b['h20']
            fi = i
            fh = hix[i] - 1           # flip candle = last completed HTF candle
            fv = dict(bull=b['hf'] == 1, prev=H[fh - 1] if fh >= 1 else None, ready=hix[i] + 1, z=None)
        away[i] = aw
        if fi is not None:
            hbs[i] = hix[i] - hix[fi]
            lbs[i] = i - fi
            if fv and fv['z'] is None and fv['prev'] and hix[i] >= fv['ready']:
                nx = H[fv['ready'] - 1]
                pv = fv['prev']
                if fv['bull'] and nx['l'] > pv['h']:
                    fv['z'] = (pv['h'], nx['l'])
                elif not fv['bull'] and pv['l'] > nx['h']:
                    fv['z'] = (nx['h'], pv['l'])
                else:
                    fv['z'] = False
            if fv and fv['z']:
                fvg[i] = (fv['z'][0], fv['z'][1], 1 if fv['bull'] else -1)
    return dict(sdir=sdir, sok=sok, atr=atr, cbc=cbc, hstruct=hstruct, away=away, hbs=hbs, lbs=lbs, fvg=fvg)


def dirn(b):
    return 1 if b['hc'] == 1 else -1


def rep_pierce(B, P, key, cool):
    """LTF EMA20 / HTF EMA9 / HTF EMA20 pierce. Returns {i: dir}."""
    out, last = {}, -10 ** 9
    for i in range(1, len(B)):
        b, p = B[i], B[i - 1]
        lv, lp = b.get(key), p.get(key)
        if lv is None or lp is None:
            continue
        s = b['l'] <= lv <= b['h']
        s1 = p['l'] <= lp <= p['h']
        eng = key != 'e20'
        if not (s and not s1 and i - last > cool and (P['sok'][i] if eng else P['away'][i])):
            continue
        d = P['sdir'][i] if eng else dirn(b)
        if d == 1 and p['l'] > lp or d == -1 and p['h'] < lp:
            last = i
            word = d if (d == 1 and b['c'] >= lv or d == -1 and b['c'] <= lv) else -d
            out[i] = word
    return out


def rep_pb(B, P, win):
    out = {}
    for i in range(1, len(B)):
        b, p = B[i], B[i - 1]
        bn = min(b['h9'], b['h20']) <= b['c'] <= max(b['h9'], b['h20'])
        bp = min(p['h9'], p['h20']) <= p['c'] <= max(p['h9'], p['h20'])
        if not (bn and not bp and P['away'][i] and P['hbs'][i] <= win):
            continue
        hs, ls = P['hstruct'][i]
        d = dirn(b)
        if d == 1 and hs == 'HH' and ls == 'HL' or d == -1 and hs == 'LH' and ls == 'LL':
            out[i] = d
    return out


def rep_fvg(B, P, gap, mx):
    out, last = {}, -10 ** 9
    for i, b in enumerate(B):
        z = P['fvg'][i]
        if not z or P['lbs'][i] > mx or i - last < gap:
            continue
        if b['l'] <= z[1] and b['h'] >= z[0]:
            last = i
            out[i] = z[2]
    return out


def rep_vb(B, P, sym, mind):
    out = {}
    for i in range(1, len(B)):
        b = B[i]
        if P['cbc'][i] == P['cbc'][i - 1] or b.get('vw') is None or abs(b['c'] - b['vw']) > PROX:
            continue
        pp, r1, s1 = b.get('pp'), b.get('r1'), b.get('s1')
        lv = []
        if pp is not None and r1 is not None and s1 is not None:
            H, L = 2 * pp - s1, 2 * pp - r1
            rg = H - L
            lv = [pp, r1, s1, pp + rg, pp - rg, H + 2 * (pp - L), L - 2 * (H - pp)]
        t = et(b['t'])
        m = t.hour * 60 + t.minute
        ses = 'ln' if 3 * 60 <= m < 9 * 60 + 30 else 'ny' if 9 * 60 + 30 <= m < 18 * 60 else 'as'
        lv += [b.get(ses + 'h'), b.get(ses + 'l')]
        dist = min((abs(b['c'] - x) for x in lv if x is not None), default=1e10)
        if dist >= mind:
            out[i] = 1 if P['cbc'][i] else -1
    return out


def outcome(B, P, i, d, tf):
    b0 = B[i]
    en = b0['c']
    t_end0 = b0['t'] + tf * 60000
    day17 = et(b0['t']).replace(hour=17, minute=0, second=0, microsecond=0)
    if et(b0['t']).hour >= 17:
        day17 += D.timedelta(days=1)
    e17 = int(day17.timestamp() * 1000)
    # (a)
    ra = None
    for j in range(i + 1, len(B)):
        b = B[j]
        te = b['t'] + tf * 60000
        if b.get('hf') == -d or te >= e17 or te - t_end0 >= 2 * 3600000:
            ra = d * (b['c'] - en); break
    # (b)
    A = P['atr'][i]
    sl, tp = en - d * 1.3 * A, en + d * 2.0 * A
    rb = None
    for j in range(i + 1, len(B)):
        b = B[j]
        hit_s = b['l'] <= sl if d == 1 else b['h'] >= sl
        hit_t = b['h'] >= tp if d == 1 else b['l'] <= tp
        if hit_s:
            rb = -1.3 * A; break
        if hit_t:
            rb = 2.0 * A; break
        if b['t'] + tf * 60000 >= e17:
            rb = d * (b['c'] - en); break
    return ra, rb


def stats(B, fires, P, tf, mid):
    """fires {i: dir}, session-filtered. Returns dict of metrics."""
    rows = []
    for i, d in sorted(fires.items()):
        ra, rb = outcome(B, P, i, d, tf)
        if ra is None or rb is None:
            continue
        rows.append((B[i]['t'], ra, rb))
    days = len({et(t).date() for t, _, _ in rows}) or 1
    nd = len({et(b['t']).date() for b in B if et(b['t']).weekday() < 5}) or 1

    def m(k):
        v = [r[k] for r in rows]
        if not v:
            return dict(w=0, avg=0, tot=0, pf=0, h1=0, h2=0)
        g = sum(x for x in v if x > 0); l = -sum(x for x in v if x < 0)
        h1 = sum(r[k] for r in rows if r[0] < mid); h2 = sum(r[k] for r in rows if r[0] >= mid)
        return dict(w=100 * sum(x > 0 for x in v) / len(v), avg=sum(v) / len(v), tot=sum(v), pf=(g / l if l else float('inf')), h1=h1, h2=h2)
    return dict(n=len(rows), pd=len(rows) / nd, a=m(1), b=m(2))


def validate(B, fires_all, stored, t0, t1, days):
    """Match replayed session alerts with stored alerts inside the stored-alert window (±1 bar)."""
    tset = {b['t']: i for i, b in enumerate(B)}
    if not stored:
        return None
    rep = {B[i]['t'] for i in fires_all if t0 <= B[i]['t'] <= t1 and et(B[i]['t']).date() in days}
    step = B[1]['t'] - B[0]['t']
    st = set(stored)
    hit_s = sum(1 for t in st if any(t + k * step in rep for k in (-1, 0, 1)))
    hit_r = sum(1 for t in rep if any(t + k * step in st for k in (-1, 0, 1)))
    return dict(ns=len(st), nr=len(rep), rec=hit_s / len(st) * 100, prec=(hit_r / len(rep) * 100) if rep else 0)


def fmt_pf(x):
    return '∞' if x == float('inf') else '%.2f' % x


def table(rows, cur):
    L = ['| Value | Alerts | /day | (a) win % | (a) avg | (a) total | (a) PF | (b) win % | (b) avg | (b) total | (b) PF | ✱ |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for v, s in rows:
        a, b = s['a'], s['b']
        both = '✱' if a['h1'] > 0 and a['h2'] > 0 and b['h1'] > 0 and b['h2'] > 0 else ''
        L.append('| %s%s | %d | %.1f | %.0f | %+.2f | %+.1f | %s | %.0f | %+.2f | %+.1f | %s | %s |' % (
            v, ' (current)' if v == cur else '', s['n'], s['pd'], a['w'], a['avg'], a['tot'], fmt_pf(a['pf']),
            b['w'], b['avg'], b['tot'], fmt_pf(b['pf']), both))
    return L


def verdict(rows, cur, valid_ok):
    """'worth considering' only with 30+ alerts, beats current in both halves on both rules, neighbours agree."""
    vals = [v for v, _ in rows]
    S = dict(rows)
    if cur not in S:
        return 'no change yet', None
    c = S[cur]
    score = lambda s: s['a']['tot'] + s['b']['tot']
    best = max(vals, key=lambda v: score(S[v]))
    if best == cur:
        return 'no change yet (current value is best)', best
    s = S[best]
    beats = all(s[k]['h1'] > c[k]['h1'] and s[k]['h2'] > c[k]['h2'] for k in ('a', 'b'))
    i = vals.index(best)
    nb = [vals[j] for j in (i - 1, i + 1) if 0 <= j < len(vals) and vals[j] != cur]
    agree = all(score(S[v]) > score(c) for v in nb) if nb else False
    if s['n'] >= 30 and beats and agree and valid_ok:
        return '**worth considering: %s**' % best, best
    why = []
    if s['n'] < 30: why.append('%d alerts' % s['n'])
    if not beats: why.append('not better in both halves')
    if not agree: why.append('neighbours disagree')
    if not valid_ok: why.append('replay unreliable')
    return 'no change yet (best %s: %s)' % (best, ', '.join(why)), best


def run(prev=None):
    alerts = get(BASE + '/alerts?from=2000-01-01')
    ts = [int(D.datetime.fromisoformat(x['receivedAt'].replace('Z', '+00:00')).timestamp() * 1000) for x in alerts]
    a0, a1 = min(ts), max(ts)
    now = D.datetime.now(TZ)
    L = ['# CBC alert parameter sweep -- %s' % now.strftime('%Y-%m-%d %H:%M ET'), '',
         'Alert Feed: %d alerts (%s to %s). Bars: BarFeed, last 60 days. Validation window = days with stored alerts.' % (
             len(alerts), et(a0).strftime('%m/%d'), et(a1).strftime('%m/%d')),
         'Outcome (a) = exit at first opposite HTF CBC flip / 17:00 ET / 2 h. (b) = 1.3 ATR stop / 2.0 ATR target (both in one candle = stop). '
         'Points per contract-point, before costs. ✱ = positive in both halves of the data under both rules. '
         'Validation: recall = stored alerts the replay reproduces (±1 bar), precision = replayed alerts that were stored. '
         'Unreliable = recall or precision < 70 %.', '',
         'Notes: "Option 2: Reverse" pierces are scored in the reversed direction (as the alert says). LTF cooldown 0 and 1 '
         'are identical (a pierce needs the previous candle not touching the line). HTF EMA pierces use the setup-engine '
         'direction (flip counts on the HTF candle close) and the away / toward-late (1 pt) gate. 2m charts use their own '
         '10m HTF fields from the BarFeed. Pullback-Structure replay rebuilds HTF swing pivots from the chart candles and '
         'does not reproduce the live alerts well (few stored alerts). In FVG alerts: none stored in the Alert Feed so far. '
         'Verdict rule: "worth considering" needs 30+ alerts, better than current in both halves under both rules, '
         'neighbouring values also better, and a reliable replay.', '']
    if prev:
        L += ['Since last run: ' + prev, '']
    summary = []
    for sym, tf in CASES:
        key = sym if tf == 3 else '%s_%d' % (sym, tf)
        stor = stored_alerts(alerts, sym, tf)
        if tf != 3 and not any(stor.values()):
            continue
        try:
            B = get('%s/bars?sym=%s&days=60&from=%s' % (BASE, key, (now - D.timedelta(days=62)).strftime('%Y-%m-%d')))['bars']
        except Exception as e:
            L += ['## %s %dm' % (sym, tf), '', 'bars error: %s' % e, '']; continue
        B = [b for b in B if all(b.get(k) is not None for k in ('o', 'h', 'l', 'c', 'e20', 'h9', 'h20', 'hc'))]
        P = prep(B, tf)
        mid = B[len(B) // 2]['t']
        sess = lambda f: {i: d for i, d in f.items() if in_sess(B[i]['t'])}
        L += ['## %s %dm (HTF %dm) -- %d bars %s to %s' % (sym, tf, tf * 5, len(B), et(B[0]['t']).strftime('%m/%d'), et(B[-1]['t']).strftime('%m/%d')), '']
        case_notes = []
        cdays = {et(t).date() for k in stor for t in stor[k]}

        def section(title, typ, grid, cur, fn, extra=''):
            fires = {v: sess(fn(v)) for v in grid}
            vs = [validate(B, fires[cur], {t: d for t, d in stor[k].items()}, a0, a1, cdays) for k in (typ if isinstance(typ, tuple) else (typ,))]
            vs = [v for v in vs if v]
            L.append('### %s' % title)
            L.append('')
            ok = True
            if not vs:
                L.append('Validation: no stored alerts of this type for this chart -- replay unchecked.')
                ok = False
            else:
                for v in vs:
                    bad = v['rec'] < 70 or v['prec'] < 70
                    ok = ok and not bad
                    L.append('Validation at current: stored %d, replayed %d, recall %.0f %%, precision %.0f %%%s' % (
                        v['ns'], v['nr'], v['rec'], v['prec'], ' -- **unreliable**' if bad else ''))
            if extra:
                L.append(extra)
            L.append('')
            rows = [(v, stats(B, fires[v], P, tf, mid)) for v in grid]
            L.extend(table(rows, cur))
            vd, best = verdict(rows, cur, ok)
            L.extend(['', 'Best value: %s · %s' % (best, vd), ''])
            cn = dict(rows)[cur]['n']
            case_notes.append((title, vd, cn, ok))

        section('LTF EMA20 Pierce: cooldown bars', 'ltf', [0, 1, 2, 3, 5, 8], 3, lambda v: rep_pierce(B, P, 'e20', v))
        section('HTF EMA9 Pierce: spacing (bars, fires when bar - last > value)', 'h9', [1, 3, 5], 3, lambda v: rep_pierce(B, P, 'h9', v),
                'No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.')
        section('HTF EMA20 Pierce: spacing (bars)', 'h20', [1, 3, 5], 3, lambda v: rep_pierce(B, P, 'h20', v),
                'No input in CBC (fixed once every 3 bars per line); 1 / 5 are what-if variants.')
        section('HTF Pullback Entry - Structure Confirmed: recent flip window (HTF bars)', 'pb', [1, 2, 3, 4, 6, 8], 4, lambda v: rep_pb(B, P, v))
        # FVG full grid
        grid = [(g, m) for g in (1, 2, 3, 5) for m in (10, 15, 20, 30, 40)]
        section('In FVG of HTF Flip Candle: (min gap bars, stop after N bars)', 'fvg', grid, (2, 20), lambda v: rep_fvg(B, P, v[0], v[1]))
        section('VWAP Bounce: min distance from major S/R (pts, 0 = no gate)', 'vb', VB_GRID[sym], VB_AUTO[sym], lambda v: rep_vb(B, P, sym, v),
                'Current = auto %s.' % VB_AUTO[sym])
        summary.append(('%s %dm' % (sym, tf), case_notes))
    return '\n'.join(L), summary


if __name__ == '__main__':
    prev = sys.argv[1] if len(sys.argv) > 1 else None
    rep, summ = run(prev)
    print(rep)
    print('\n<!-- SUMMARY')
    for c, notes in summ:
        print(c, ' | '.join('%s: %s (n=%d%s)' % (t.split(':')[0], v, n, '' if ok else ', unchecked/unreliable') for t, v, n, ok in notes))
    print('-->')
