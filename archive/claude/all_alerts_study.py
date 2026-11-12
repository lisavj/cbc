#!/usr/bin/env python3
"""Every CBC alert type, scored -- 11/01/2026.

For each chart (MES / MGC / MNQ 3m, MES / MGC 2m, MES / MGC 5m) every directional alert section ("• <type>: LONG / SHORT /
Bullish / Bearish / Above / Below / Pass + / Pass - ...") stored in the Alert Feed is scored from the BarFeed bars with the
same two outcome rules as claude/alert_param_sweep.py:
  (a) entry = close of the alert candle, exit at the close of the first candle with an opposite HTF CBC flip, the candle
      ending 17:00 ET, or after 2 h;   (b) 1.3 ATR(14) stop / 2.0 ATR target (both in one candle = stop), else 17:00 ET.
Points per contract-point, before costs. ✱ = positive in both halves (by date) under both rules. Non-directional alerts
(Approaching / Crossing / Setup Ended / TP1 Partial / Shadow ...) are counted only.
Alert candle = the bar that closes at the alert's "Time:" (CBC alerts fire at the candle close).
Also: Trade Setups the setup engine would draw OUTSIDE CBC's alert sessions (Asia 18:00-22:30, London 03:00-07:45,
NY 09:30-17:00 ET) never reach the feed -- replay counts / results for 3m and 5m (chop_sim, live gates, base exits).
Usage: python3 all_alerts_study.py
"""
import re, json, gzip, time, urllib.request, collections, datetime as D
from zoneinfo import ZoneInfo
import numpy as np

BASE = 'https://tv-webhook-dashboard.onrender.com'
TZ = ZoneInfo('America/New_York')
CHARTS = [('MES', 3), ('MGC', 3), ('MNQ', 3), ('MES', 2), ('MGC', 2), ('MES', 5), ('MGC', 5)]
SKIP = re.compile(r'Approaching|Crossing|Setup Ended|TP1 Partial|Shadow Ended|Setup Confirmed|Bill Breaker')


def get(url):
    for k in range(4):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=300) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception:
            if k == 3:
                raise
            time.sleep(45)


def et(ms):
    return D.datetime.fromtimestamp(ms / 1000, TZ)


def direction(line):
    w = re.findall(r'LONG|SHORT|Bullish|Bearish|\bAbove\b|\bBelow\b|Pass \+|Pass -|FAIL|Fail', line)
    if not w:
        return 0
    x = w[-1] if 'LONG' in w or 'SHORT' in w else w[0]
    if 'LONG' in w or 'SHORT' in w:
        x = [y for y in w if y in ('LONG', 'SHORT')][-1]
    return 1 if x in ('LONG', 'Bullish', 'Above', 'Pass +') else -1 if x in ('SHORT', 'Bearish', 'Below', 'Pass -') else 0


def norm_type(line):
    t = line[2:].split(':')[0].strip()
    t = re.sub(r'\s*-\s*(Entry|Option 2).*$', '', t)
    t = re.sub(r'^CH\d+\s+', '', t)
    t = re.sub(r'\s*\(.*$', '', t)
    if t.startswith('Key Level Alert'):
        t = 'Key Level Alert'
    if t.startswith('High Confluence Setup'):
        t = 'High Confluence Setup'
    if t.startswith('HTF(') or t.startswith('HTF ('):
        t = re.sub(r'HTF\s*\(\d+\)', 'HTF', t)
    if t.startswith('LTF('):
        t = re.sub(r'LTF\(\d+\)', 'LTF', t)
    t = re.sub(r'\d+\)', '', t)
    return t.strip()


def prep(B):
    atr, a = [], None
    for i, b in enumerate(B):
        tr = max(b['h'], B[i - 1]['c']) - min(b['l'], B[i - 1]['c']) if i else b['h'] - b['l']
        a = tr if a is None else (a * 13 + tr) / 14
        atr.append(a)
    return atr


def outcome(B, atr, i, d, tf):
    b0 = B[i]; en = b0['c']; t_end0 = b0['t'] + tf * 60000
    day17 = et(b0['t']).replace(hour=17, minute=0, second=0, microsecond=0)
    if et(b0['t']).hour >= 17:
        day17 += D.timedelta(days=1)
    e17 = int(day17.timestamp() * 1000)
    ra = rb = None
    for j in range(i + 1, len(B)):
        b = B[j]; te = b['t'] + tf * 60000
        if b.get('hf') == -d or te >= e17 or te - t_end0 >= 2 * 3600000:
            ra = d * (b['c'] - en); break
    A = atr[i]; sl, tp = en - d * 1.3 * A, en + d * 2.0 * A
    for j in range(i + 1, len(B)):
        b = B[j]
        if (b['l'] <= sl) if d == 1 else (b['h'] >= sl):
            rb = -1.3 * A; break
        if (b['h'] >= tp) if d == 1 else (b['l'] <= tp):
            rb = 2.0 * A; break
        if b['t'] + tf * 60000 >= e17:
            rb = d * (b['c'] - en); break
    return ra, rb


def main():
    A = get(BASE + '/alerts?from=2000-01-01'); A = A if isinstance(A, list) else A.get('alerts', [])
    now = D.datetime.now(TZ)
    out = ['# Every CBC alert type, scored — %s' % now.strftime('%a %m/%d/%Y %H:%M ET'), '', __doc__.strip(), '',
           'Alert Feed: %d alerts, %s to %s.' % (len(A), min(a['receivedAt'] for a in A)[:10], max(a['receivedAt'] for a in A)[:10]), '']
    for sym, tf in CHARTS:
        key = sym if tf == 3 else '%s_%d' % (sym, tf)
        sec = collections.defaultdict(list)   # type -> [(close_ms, dir)]
        for a in A:
            r = a.get('raw', '')
            if not isinstance(r, str) or not r.startswith(sym):
                continue
            ch = re.search(r'\nChart: \S+\s+(\d+)m', r)
            if not ch or int(ch.group(1)) != tf:
                continue
            tm = re.search(r'\nTime: (\d+)/(\d+) (\d+):(\d+)', r)
            if not tm:
                continue
            mo, dd, hh, mi = map(int, tm.groups())
            t = D.datetime(int(a['receivedAt'][:4]), mo, dd, hh, mi, tzinfo=TZ)
            cms = int(t.timestamp() * 1000)
            for ln in r.split('\n'):
                if ln.startswith('• '):
                    sec[norm_type(ln)].append((cms, 0 if SKIP.search(ln) else direction(ln)))
        if not sec:
            out += ['## %s %dm' % (sym, tf), '', 'No alerts with "Chart: %s… %dm" in the feed.' % (sym, tf), '']
            continue
        t0 = min(c for v in sec.values() for c, _ in v)
        try:
            B = get('%s/bars?sym=%s&days=60&from=%s' % (BASE, key, et(t0 - 86400000).strftime('%Y-%m-%d')))['bars']
        except Exception as e:
            out += ['## %s %dm' % (sym, tf), '', 'bars error %r' % e, '']; continue
        B = [b for b in B if all(b.get(k) is not None for k in ('o', 'h', 'l', 'c')) and not b.get('live')]
        B.sort(key=lambda b: b['t'])
        idx = {b['t']: i for i, b in enumerate(B)}
        atr = prep(B)
        last = max(c for v in sec.values() for c, _ in v)
        mid = t0 + (last - t0) / 2
        days = len({et(c).date() for v in sec.values() for c, _ in v})
        out += ['## %s %dm — %s to %s (%d days with alerts)' % (sym, tf, et(t0).strftime('%m/%d'), et(last).strftime('%m/%d'), days), '',
                '| Alert type | Alerts | /day | Directional | (a) win % | (a) avg | (a) total | (b) win % | (b) avg | (b) total | ✱ |', '|---|---|---|---|---|---|---|---|---|---|---|']
        rows = []
        for typ, v in sec.items():
            res = []
            for cms, d in v:
                if not d:
                    continue
                i = idx.get(cms - tf * 60000)
                if i is None:
                    continue
                ra, rb = outcome(B, atr, i, d, tf)
                if ra is not None and rb is not None:
                    res.append((cms, ra, rb))
            nd = sum(1 for _, d in v if d)
            if res:
                a_ = [x[1] for x in res]; b_ = [x[2] for x in res]
                halves = all(sum(x[k] for x in res if (x[0] < mid) == h) > 0 for k in (1, 2) for h in (True, False))
                rows.append((sum(a_) + sum(b_), '| %s | %d | %.1f | %d | %.0f | %+.2f | %+.1f | %.0f | %+.2f | %+.1f | %s |' % (
                    typ, len(v), len(v) / max(1, days), len(res), 100 * np.mean([x > 0 for x in a_]), np.mean(a_), sum(a_),
                    100 * np.mean([x > 0 for x in b_]), np.mean(b_), sum(b_), '✱' if halves else '')))
            else:
                rows.append((-1e9, '| %s | %d | %.1f | %s | | | | | | | |' % (typ, len(v), len(v) / max(1, days), '0' if not nd else '%d (no bars)' % nd)))
        out += [r for _, r in sorted(rows, key=lambda x: -x[0])] + ['']
    # setups outside the alert sessions (replay)
    try:
        import chop_sim as cs, stretch_study as ss
        ss.FROM[5] = '2026-01-05'
        GT = {('MES', 3): dict(R5=1, X4=0, MTF=0), ('MGC', 3): dict(R5=1, X4=1, MTF=0), ('MES', 2): dict(R5=0, X4=0, MTF=1), ('MGC', 2): dict(R5=0, X4=0, MTF=0), ('MES', 5): dict(R5=0, X4=0, MTF=0), ('MGC', 5): dict(R5=0, X4=0, MTF=0)}
        out += ['## Trade Setups drawn outside the alert sessions (replay, Jan–Oct, live gates, base exits)', '',
                'CBC sends no alert outside Asia 18:00–22:30, London 03:00–07:45, NY 09:30–17:00 ET (⑤ Alerts session boxes). The chart still draws these setups.', '',
                '| Chart | Window | Setups | Win % | Net | Avg | Net by third (3m/5m: Jan–Mar / Apr–Jun / Jul–Oct; 2m: Jun–Jul / Aug / Sep–Oct) |', '|---|---|---|---|---|---|---|']
        for (sym, tf), G in GT.items():
            s = cs.Case(sym, tf, ss.load(sym, tf))
            res = s.run(lambda d: cs.cur_rule(d), q=ss.QB[sym], gates=G)
            def win(r):
                m = s.hm[r['i']]  # candle close minute
                if 18 * 60 <= m < 22 * 60 + 30 or 3 * 60 <= m < 7 * 60 + 45 or 9 * 60 + 30 <= m < 17 * 60:
                    return 'inside sessions'
                return '22:30–03:00' if (m >= 22 * 60 + 30 or m < 3 * 60) else '07:45–09:30' if m < 9 * 60 + 30 else 'other'
            g = collections.defaultdict(list); gr = collections.defaultdict(list)
            for r in res:
                g[win(r)].append(r['res']); gr[win(r)].append(r)
            for w in ('inside sessions', '22:30–03:00', '07:45–09:30', 'other'):
                v = g.get(w, [])
                if v:
                    th = ss.thirds(gr[w], s.month, 3 if tf != 2 else 2)
                    out.append('| %s %dm | %s | %d | %.0f%% | %+.0f | %+.2f | %+.0f / %+.0f / %+.0f |' % (sym, tf, w, len(v), 100 * np.mean([x > 0 for x in v]), sum(v), np.mean(v), *th))
    except Exception as e:
        out += ['session replay error: %r' % e]
    print('\n'.join(out))


if __name__ == '__main__':
    main()
