#!/usr/bin/env python3
"""CBC evening-session study: setups entered 18:00-20:30 ET in 15-minute buckets, per chart and trigger type.

Cases: MGC 3m, MES 3m (HTF 15m), MGC 2m, MES 2m (HTF 10m), MGC 5m, MES 5m (HTF 25m; base exits, no gates). Two sources:
  LIVE  real Trade Setup alerts matched to their Setup Ended results (Alert Feed, /alerts?from=2000-01-01).
  SIM   chop_sim.py replay (current CBC-style rules + exits, ~50 % exact match with real setups) on the BarFeed
        archive: 3m and 5m from 01/05, 2m from 06/01. The sim's quiet window ends 18:30 (CBC: 18:45) and it skips the
        forming Asia opening range 20:00-20:30 (same as CBC), so those buckets are empty / thin by design.
Bucket = entry candle OPEN time (ET). Thirds = the case's sim setups split into three equal time blocks.
A bucket/trigger cell is flagged "weak" when it has >= 10 sim setups and is negative in all three thirds, and
"strong" when >= 10 sim setups and positive in all three thirds.
Usage: python3 evening_study.py > evening_session_report_new.md   (needs chop_sim.py in the same folder)
"""
import gzip, json, re, sys, time, urllib.request, datetime as D, collections
from zoneinfo import ZoneInfo
import numpy as np, pandas as pd
import chop_sim as cs

BASE = 'https://tv-webhook-dashboard.onrender.com'
TZ = ZoneInfo('America/New_York')
CASES = [('MGC', 3), ('MES', 3), ('MGC', 2), ('MES', 2), ('MGC', 5), ('MES', 5)]
FROM = {3: '2026-01-05', 2: '2026-06-01', 5: '2026-01-05'}
# 5m charts (HTF 25m) are not listed in any CBC per-symbol/timeframe default -> base exits (SL1 1.7 ATR + min 5,
# TP1 1.7 ATR, 80 % at TP1, breakeven at TP1, trail 1.7 ATR) and no range / stretch / MTF gates.
for _s in ('MGC', 'MES'):
    cs.EXIT.setdefault((_s, 5), dict(sl=1.7, mn=5, tp=1.7, part=.8, be=True, ts=0, tr=1.7, cap={'MGC': 7, 'MES': 8}[_s]))
    cs.GATE.setdefault((_s, 5), dict(R5=0, X4=0, MTF=0))
# CBC v10.42 (10/27): MES 3m exits back to the base exits (MES 3m removed from the SL1 / min SL / TP1 / partial / BE lists).
cs.EXIT[('MES', 3)] = dict(sl=1.7, mn=5, tp=1.7, part=.8, be=True, ts=0, tr=1.7, cap=8)
B0, B1 = 18 * 60, 20 * 60 + 30
BUCKETS = list(range(B0, B1, 15))
TN = {'flip': 'HTF CBC Flip', 'ltf20': 'LTF EMA20 Pierce', 'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}


def get(url, tries=3):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=300) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(60)


def load_bars(sym, tf):
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    B = pd.DataFrame(get('%s/bars?sym=%s&days=400&from=%s' % (BASE, key, FROM[tf]))['bars'])
    B = B.sort_values('t').drop_duplicates('t').reset_index(drop=True)
    for c in B.columns:
        if c != 'fl':
            B[c] = pd.to_numeric(B[c], errors='coerce')
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // (5 * tf)).astype(str)
    B['last'] = B.groupby('hk').t.transform('max')
    B['hf'] = B['hf'].fillna(0)
    return B


def raw(x):
    return x['raw'] if isinstance(x['raw'], str) else json.dumps(x['raw'])


def live_setups(alerts, sym, tf):
    S, E = {}, {}
    for x in alerts:
        r = raw(x)
        if not r.startswith(sym) or not re.search(r'Chart: \S+\s+%dm' % tf, r):
            continue
        tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
        if not tm:
            continue
        mo, dd, hh, mi = map(int, tm.groups())
        t = D.datetime(int(x['receivedAt'][:4]), mo, dd, hh, mi, tzinfo=TZ)
        if '• Trade Setup:' in r:
            d = re.search(r'Trade Setup: (\w+)', r).group(1)
            en = float(re.search(r'\nEntry: ([\d.]+)', r).group(1))
            k = (t, d, en)
            if k not in S or len(r) > len(S[k]):
                S[k] = r
        elif '• Setup Ended:' in r:
            en = float(re.search(r'Setup Entry: ([\d.]+)', r).group(1))
            st = re.search(r'Started: (\d+):(\d+)', r)
            d = re.search(r'Setup Ended: (\w+)', r).group(1)
            m = re.search(r'Ended: ([^|\n]*?) \| Result: ([+-]?[\d.]+)', r)
            if st and m:
                E[(d, en, int(st.group(1)), int(st.group(2)))] = (m.group(1).strip(), float(m.group(2)))
    out = []
    for (t, d, en), r in sorted(S.items()):
        res = E.get((d, en, t.hour, t.minute))
        if not res:
            continue
        trg = re.search(r'Trigger: ([^\n]*)', r)
        trg = trg.group(1) if trg else ''
        k = 'flip' if 'HTF CBC Flip' in trg else 'mom' if 'Momentum' in trg else 'ltf20' if 'LTF EMA20' in trg else 'h9' if 'HTF EMA9' in trg else 'h20' if 'HTF EMA20' in trg else 'other'
        out.append(dict(t=t, om=(t.hour * 60 + t.minute - tf) % 1440, trig=k, res=res[1], why=res[0]))
    return out


def f(g):
    if not g:
        return '–'
    return '%d · %d%% · %+.1f' % (len(g), round(100 * sum(x['res'] > 0 for x in g) / len(g)), sum(x['res'] for x in g))


def lab(m):
    return '%d:%02d' % (m // 60, m % 60)


def main():
    now = D.datetime.now(TZ)
    alerts = get(BASE + '/alerts?from=2000-01-01')
    out = ['# Evening session 18:00–20:30 ET in 15-minute buckets — %s' % now.strftime('%a %m/%d/%Y %H:%M ET'), '', __doc__.strip(), '',
           'Cells: setups · win % · net pts. Thirds: net in each third of the sim period. ⚠ weak = ≥ 10 sim setups and negative in all thirds; ✓ strong = ≥ 10 and positive in all thirds.', '']
    flags = []
    for sym, tf in CASES:
        case = '%s %dm' % (sym, tf)
        L = live_setups(alerts, sym, tf)
        B = load_bars(sym, tf)
        s = cs.Case(sym, tf, B)
        res = s.run(cs.cur_rule)
        for r in res:
            r['om'] = (s.hm[r['i']] - tf) % 1440
        n = len(res)
        T = [res[:n // 3], res[n // 3:2 * n // 3], res[2 * n // 3:]]
        tid = [{id(r) for r in t} for t in T]
        inW = lambda r: B0 <= r['om'] < B1
        win, rest = [r for r in res if inW(r)], [r for r in res if not inW(r)]
        lw, lr = [r for r in L if inW(r)], [r for r in L if not inW(r)]
        out += ['## %s — sim %s → %s (%d setups), live %d setups since %s' % (case, s.date[0][:5], s.date[-1][:5], n, len(L), L[0]['t'].strftime('%m/%d') if L else '–'), '',
                'Whole window 18:00–20:30: sim %s (avg %+.2f) vs rest of day avg %+.2f · live %s vs rest %s' % (
                    f(win), (sum(r['res'] for r in win) / len(win)) if win else 0, (sum(r['res'] for r in rest) / len(rest)) if rest else 0, f(lw), f(lr)), '']
        hdr = '| Bucket (ET) | Sim all | Sim thirds | Live all | ' + ' | '.join('Sim %s' % TN[k] for k in TN) + ' |'
        out += [hdr, '|' + '---|' * (4 + len(TN))]
        for b in BUCKETS:
            g = [r for r in res if b <= r['om'] < b + 15]
            th = [sum(r['res'] for r in g if id(r) in tid[j]) for j in range(3)]
            mark = ''
            if len(g) >= 10 and all(x < 0 for x in th):
                mark = ' ⚠ weak'; flags.append('%s %s–%s all triggers: %s, thirds %s' % (case, lab(b), lab(b + 15), f(g), ' / '.join('%+.0f' % x for x in th)))
            elif len(g) >= 10 and all(x > 0 for x in th):
                mark = ' ✓ strong'
            cells = []
            for k in TN:
                gk = [r for r in g if r['trig'] == k]
                tk = [sum(r['res'] for r in gk if id(r) in tid[j]) for j in range(3)]
                m2 = ''
                if len(gk) >= 10 and all(x < 0 for x in tk):
                    m2 = ' ⚠'; flags.append('%s %s–%s %s: %s, thirds %s' % (case, lab(b), lab(b + 15), TN[k], f(gk), ' / '.join('%+.0f' % x for x in tk)))
                elif len(gk) >= 10 and all(x > 0 for x in tk):
                    m2 = ' ✓'
                cells.append(f(gk) + m2)
            lg = [r for r in L if b <= r['om'] < b + 15]
            out.append('| %s–%s | %s%s | %s | %s | %s |' % (lab(b), lab(b + 15), f(g), mark, ' / '.join('%+.0f' % x for x in th) if g else '–', f(lg), ' | '.join(cells)))
        # whole window by trigger
        out += ['', '**Whole window by trigger** (sim N · win · net, thirds | live)', '']
        for k in TN:
            g = [r for r in win if r['trig'] == k]
            th = [sum(r['res'] for r in g if id(r) in tid[j]) for j in range(3)]
            gl = [r for r in lw if r['trig'] == k]
            out.append('- %s: sim %s (%s) | live %s' % (TN[k], f(g), ' / '.join('%+.0f' % x for x in th), f(gl)))
        out.append('')
    out += ['## Flags (weak cells: ≥ 10 sim setups, negative in all thirds)', ''] + (['- ' + x for x in flags] if flags else ['- none'])
    print('\n'.join(out))


if __name__ == '__main__':
    main()
