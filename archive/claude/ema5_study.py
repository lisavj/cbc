#!/usr/bin/env python3
"""5m chart EMA length study (CBC v10.50 "Chart EMA fast / slow / 200") -- 10/31/2026 (weekly check; candidate 12 / 26 / 200).

Question: on MES / MGC 5m charts, do other chart EMA lengths (e.g. 5 / 12 / 120 = the 3m 9 / 20 / 200 time span) beat the
standard 9 / 20 / 200? And are CBC's bar-count gates (setup cooldown 10 bars, ER(12), range gate 24 bars) right on 5m candles,
where each bar is 5 minutes instead of 3?
Data: server archive MES_5 / MGC_5 (Databento rebuild + BarFeed), Jan 5 - Oct 30. Chart EMAs recomputed from the 5m closes
(fast / slow / 200 per combo); HTF = 25m (CBC default 5x) with BarFeed's 25m CBC and EMA9/20, or 15m rebuilt from the 5m
candles (CBC rule: 15m close above the prior 15m high = long, below the prior low = short) with 15m EMA9/20.
Engine: chop_sim (triggers HTF CBC Flip, LTF EMA20 Pierce on the slow chart EMA, HTF EMA9 / EMA20 Pierce, 1-bar late confirm,
ER chop rule 0.23 with breakout exception, VWAP bounce block, opening-range windows). 5m live settings: range gate, VWAP stretch
and MTF gate OFF (per-symbol lists only cover 3m / 2m). BASE exits (SL1 1.7 ATR min 5, TP1 1.7 ATR capped 6, 80 % at TP1, BE,
trail 1.7 ATR; SL cap MGC 7 / MES 8). Not modelled: "price past both EMA clouds" gate, CBC's 5-bar LTF late window.
~50 % exact match with live setups on 3m: compare variants, not totals. z = change / (SD x sqrt(setups changed));
robust = z >= 2 and better in all three thirds (Jan-Mar / Apr-Jun / Jul-Oct); promising = z >= 1 and better in all three.
Usage: python3 ema5_study.py   (needs chop_sim.py + stretch_study.py next to it)
"""
import sys, datetime as D, numpy as np, pandas as pd
import chop_sim as cs, stretch_study as ss

ss.FROM[5] = '2026-01-05'
COMBOS = [('A', 9, 20, 200, 'standard'), ('B', 5, 12, 120, '3m time span'), ('C', 5, 12, 200, 'fast/slow only'),
          ('D', 9, 20, 120, '200 only'), ('E', 7, 15, 150, 'midway'), ('F', 12, 26, 200, 'slower'),
          ('G', 10, 24, 200, 'around F'), ('H', 14, 30, 200, 'around F'), ('I', 16, 34, 200, 'around F'),
          ('J', 12, 26, 150, 'F + EMA 150'), ('K', 12, 26, 120, 'F + EMA 120'),
          ('L', 20, 40, 200, 'beyond I'), ('M', 24, 50, 200, 'beyond I'), ('N', 16, 34, 120, 'I + EMA 120')]


def ema(x, n):
    return pd.Series(x).ewm(span=n, adjust=False).mean().values


def htf15(B):
    """Rebuild a 15m HTF from the 5m candles: hk = 15m bucket (CME day from 18:00), h9 / h20 = 15m EMA (final value on the
    bucket's last bar), hc = 15m CBC (changes on the bar that closes the 15m candle), hf = +1 / -1 on that bar."""
    B = B.copy()
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // 15).astype(str)
    B['last'] = B.groupby('hk').t.transform('max')
    G = B.groupby('hk', sort=False).agg(h=('h', 'max'), l=('l', 'min'), c=('c', 'last'), t=('t', 'max'))
    G['e9'] = G.c.ewm(span=9, adjust=False).mean(); G['e20'] = G.c.ewm(span=20, adjust=False).mean()
    st = None; S = []; ph = pl = None
    for h, l, c in zip(G.h.values, G.l.values, G.c.values):
        if ph is not None:
            if st is None:
                st = c > ph
            elif st and c < pl:
                st = False
            elif (not st) and c > ph:
                st = True
        S.append(st); ph, pl = h, l
    G['st'] = S
    m = G.set_index('t')
    isl = B.t.values == B['last'].values
    hc = np.full(len(B), np.nan); hf = np.zeros(len(B)); cur = np.nan
    stv = m.st.to_dict()
    prev = None
    for i, t in enumerate(B.t.values):
        if isl[i]:
            s_ = stv.get(t)
            if s_ is not None:
                nv = 1.0 if s_ else 0.0
                if prev is not None and nv != prev:
                    hf[i] = 1 if nv == 1 else -1
                cur = nv; prev = nv
        hc[i] = cur
    # chop_sim reads hc as the state from this bar on; CBC state flips on the closing bar of the 15m candle
    B['hc'] = hc; B['hf'] = hf
    e9 = G.set_index('t').e9.to_dict(); e20 = G.set_index('t').e20.to_dict()
    lastt = B['last'].values
    B['h9'] = [e9.get(t, np.nan) for t in lastt]; B['h20'] = [e20.get(t, np.nan) for t in lastt]
    return B


def run(s, cd=10, erk=12, r5=None, ok_thr=.23, no_ltf=False):
    """chop_sim Case.run with the bar-count gates as parameters. cd = setup cooldown (bars), erk = ER length (bars) for the chop
    rule and the trigger ER minimums, r5 = (bars, ATR width) range gate or None (off, = 5m live)."""
    q = ss.QB[s.sym]
    rg = None
    if r5:
        n, x = r5
        hh = pd.Series(s.H).rolling(n).max().values; ll = pd.Series(s.L).rolling(n).min().values
        rg = (hh, ll, x)
    res = []; last = -999; lastlg = None; op = None
    for d in s.cands:
        if d['VB'] or (no_ltf and d['trig'] == 'ltf20'):
            continue
        e = d['er'][erk]
        if d['trig'] != 'flip' and e < d['erm']:
            continue
        if not cs.cur_rule(d, thr=ok_thr, flip_thr=ok_thr, k=erk):
            continue
        i = d['i']
        if rg:
            hh, ll, x = rg; w = hh[i] - ll[i]
            if w > 0 and w / s.atr[i] < x:
                pos = (s.C[i] - ll[i]) / w
                if (pos if d['lg'] else 1 - pos) >= .8:
                    continue
        live = op is not None and i <= op['j']
        if res and res[-1]['i'] == i:
            continue
        if live and d['lg'] == op['lg']:
            continue
        if not (i - last >= cd or d['trig'] == 'flip' or (lastlg is not None and d['lg'] != lastlg)):
            continue
        if live:
            r, j, why = s.sim1(op['i'], op['lg'], q, i); op.update(res=r, j=j, why=why)
        r, j, why = s.sim1(i, d['lg'], q, -1); op = dict(d, res=r, why=why, j=j); res.append(op); last = i; lastlg = d['lg']
    return res


def stats(res, s):
    v = [r['res'] for r in res]
    w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
    return dict(n=len(v), net=sum(v), wr=100 * w / (w + l) if w + l else 0, avg=np.mean(v) if v else 0, th=ss.thirds(res, s.month, 3), sd=float(np.std(v)) if v else 1)


def cmp(base, bres, res, s):
    b, x = stats(bres, s), stats(res, s)
    ch = len({(r['i'], r['lg']) for r in bres} ^ {(r['i'], r['lg']) for r in res}) or 1
    z = (x['net'] - b['net']) / ((b['sd'] or 1) * np.sqrt(ch))
    dth = [p - q for p, q in zip(x['th'], b['th'])]
    b3 = all(d > 0 for d in dth)
    v = 'baseline' if res is bres else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if x['net'] < b['net'] else 'noise'
    return x, z, dth, v


def line(lbl, x, z, dth, v, base):
    return '| %s | %d | %.0f%% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (lbl, x['n'], x['wr'], x['net'], x['avg'], x['net'] - base['net'], z, *dth, v)


HDR = ['| Variant | Setups | Win % | Net | Avg | Δ vs standard | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Oct) | Verdict |', '|---|---|---|---|---|---|---|---|---|']


def by_trig(res):
    out = []
    for t, nm in (('flip', 'Flip'), ('ltf20', 'LTF20'), ('h9', 'HTF9'), ('h20', 'HTF20')):
        g = [r['res'] for r in res if r['trig'] == t]
        out.append('%s %d / %+.0f' % (nm, len(g), sum(g)))
    return ' · '.join(out)


def study(sym):
    B0 = ss.load(sym, 5)
    L = ['## %s 5m (%d candles, %s to %s)' % (sym, len(B0), *[D.datetime.fromtimestamp(B0.t.iloc[k] / 1000).strftime('%m/%d') for k in (0, -1)]), '']
    cases = {}
    for htf in ('25m', '15m'):
        Bh = B0 if htf == '25m' else htf15(B0)
        for key, f, sl, l2, why in COMBOS:
            if htf == '15m' and key not in ('A', 'B'):
                continue
            B = Bh.copy(); C = B.c.values.astype(float)
            B['e9'] = ema(C, f); B['e20'] = ema(C, sl); B['e200'] = ema(C, l2)
            cases[(htf, key)] = cs.Case(sym, 5, B)
    if True:  # sanity: rebuilt 15m HTF vs nothing to compare; 25m rebuild check against BarFeed's own 25m CBC
        pass
    sA = cases[('25m', 'A')]; base_res = run(sA); base = stats(base_res, sA)
    L += ['**A. Chart EMA lengths (25m HTF = CBC default on 5m)**', ''] + HDR
    T = []
    for key, f, sl, l2, why in COMBOS:
        s = cases[('25m', key)]; res = run(s)
        x, z, dth, v = cmp(base, base_res, res, s) if key != 'A' else (base, 0.0, [0, 0, 0], 'baseline')
        L.append(line('%s %d / %d / %d (%s)' % (key, f, sl, l2, why), x, z, dth, v, base))
        T.append('%s: %s' % (key, by_trig(res)))
    res = run(sA, no_ltf=True); x, z, dth, v = cmp(base, base_res, res, sA)
    L.append(line('Reference: standard EMAs, LTF EMA20 Pierce trigger OFF', x, z, dth, v, base))
    L += ['', 'By trigger (setups / net): ' + '; '.join(T), '']
    L += ['**B. 15m HTF instead of 25m (⑪ HTF Timeframe = 15)** — compared with A (standard, 25m HTF)', ''] + HDR
    for key in ('A', 'B'):
        s = cases[('15m', key)]; res = run(s)
        x, z, dth, v = cmp(base, base_res, res, s)
        f, sl, l2 = [c for c in COMBOS if c[0] == key][0][1:4]
        L.append(line('15m HTF + %s %d / %d / %d' % (key, f, sl, l2), x, z, dth, v, base))
        T.append('15m %s: %s' % (key, by_trig(res)))
    L += ['', 'By trigger: ' + '; '.join(T[-2:]), '']
    # bar-count gates
    L += ['**C. Bar-count gates on 5m candles** (standard EMAs, 25m HTF). On 3m: cooldown 10 bars = 30 min, ER(12) = 36 min,'
          ' range gate 24 bars = 72 min. Time-matched on 5m: cooldown 6, ER(8) (40 min; ER(6) = 30 min), range 14 bars.', ''] + HDR
    G = [('Cooldown 6 bars (30 min)', dict(cd=6)), ('Cooldown 4 bars', dict(cd=4)), ('Cooldown 15 bars', dict(cd=15)),
         ('ER(8) (40 min)', dict(erk=8)), ('ER(6) (30 min)', dict(erk=6)), ('ER(16) (80 min)', dict(erk=16)),
         ('Cooldown 6 + ER(8) (all time-matched)', dict(cd=6, erk=8)),
         ('Range gate ON, 24 bars / 5 ATR (as 3m, = 120 min)', dict(r5=(24, 5))), ('Range gate ON, 14 bars / 5 ATR (72 min)', dict(r5=(14, 5))),
         ('Range gate ON, 14 bars / 4 ATR', dict(r5=(14, 4)))]
    for nm, kw in G:
        res = run(sA, **kw); x, z, dth, v = cmp(base, base_res, res, sA)
        L.append(line(nm, x, z, dth, v, base))
    # same gates on combo B
    sB = cases[('25m', 'B')]; resB = run(sB)
    L += ['', '**D. Bar-count gates with 5 / 12 / 120** (compared with A standard)', ''] + HDR
    for nm, kw in [('B 5 / 12 / 120, standard gates', {})] + [g for g in G if g[0].startswith(('Cooldown 6 +', 'ER(8)', 'Range gate ON, 14 bars / 5'))]:
        res = run(sB, **kw); x, z, dth, v = cmp(base, base_res, res, sB)
        L.append(line(nm, x, z, dth, v, base))
    L.append('')
    return L


def live_part():
    """Live 5m Trade Setups (current CBC, chart EMAs 9 / 20) by trigger with their Setup Ended results: the trigger a slower slow
    EMA changes most is LTF EMA20 Pierce."""
    import json, re, collections, gzip, urllib.request
    try:
        A = ss.get(ss.BASE + '/alerts?from=2000-01-01')
    except Exception as e:
        return ['## Live 5m setups', '', 'could not load alerts: %r' % e, '']
    A = A if isinstance(A, list) else A.get('alerts', [])
    A.sort(key=lambda a: a.get('receivedAt', ''))
    ends = {}
    for a in A:
        r = a.get('raw', '')
        if 'Setup Ended:' not in r:
            continue
        ch = re.search(r'\nChart: (\S+) (\d+)m', r); se = re.search(r'Setup Entry: ([-\d.]+)', r); res = re.search(r'Result: ([-+\d.]+)', r)
        if ch and se and res:
            ends.setdefault((ch.group(1), ch.group(2), float(se.group(1))), []).append((a['receivedAt'], float(res.group(1))))
    G = collections.defaultdict(list)
    for a in A:
        r = a.get('raw', '')
        if 'Trade Setup:' not in r:
            continue
        ch = re.search(r'\nChart: (\S+) (\d+)m', r); t = re.search(r'\nTrigger: ([^\n(,]+)', r); en = re.search(r'\nEntry: ([-\d.]+)', r)
        if not (ch and t and en) or not ((ch.group(2) == '5' and ch.group(1).startswith(('MES', 'MGC'))) or (ch.group(2) in ('3', '2') and ch.group(1).startswith('MES'))):
            continue
        e = [x for x in ends.get((ch.group(1), ch.group(2), float(en.group(1))), []) if x[0] > a['receivedAt']]
        G[(ch.group(1)[:3] + ' ' + ch.group(2) + 'm', t.group(1).strip())].append(e[0][1] if e else None)
    L = ['## Live setups (alert store, current CBC chart EMAs 9 / 20 / 200) by trigger: MES / MGC 5m and MES 3m', '', '| Chart | Trigger | Setups | Ended | Win % | Net | Avg |', '|---|---|---|---|---|---|---|']
    for k in sorted(G):
        v = [x for x in G[k] if x is not None]; w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
        L.append('| %s | %s | %d | %d | %s | %+.1f | %s |' % (k[0], k[1], len(G[k]), len(v), '%d%%' % round(100 * w / (w + l)) if w + l else '–', sum(v), '%+.2f' % (sum(v) / len(v)) if v else '–'))
    return L + ['']


def study_mes3():
    """MES 3m (live settings: range gate 24 bars / 5 ATR on, VWAP stretch off, MTF off; HTF 15m) -- slow EMA 16 / 14 watch."""
    B0 = ss.load('MES', 3); C = B0.c.values.astype(float)
    def case(f, sl, l2):
        B = B0.copy(); B['e9'] = ema(C, f); B['e20'] = ema(C, sl); B['e200'] = ema(C, l2); return cs.Case('MES', 3, B)
    kw = dict(r5=(24, 5)); rec = []
    sA = case(9, 20, 200); bres = run(sA, **kw); base = stats(bres, sA)
    L = ['## MES 3m (%d candles) — watch: slow EMA 16 / 14 (range gate on, base exits)' % len(B0), '',
         'Only the SLOW length changes the replay (the fast EMA feeds only the cloud / "price past both EMA clouds" gate, not modelled).', ''] + HDR
    L.append(line('A3 9 / 20 / 200 (standard)', base, 0.0, [0, 0, 0], 'baseline', base) + ' ' + by_trig(bres))
    for key, f, sl, l2 in (('P3', 8, 18, 200), ('Q3', 7, 16, 200), ('R3', 6, 14, 200), ('S3', 5, 12, 200)):
        s = case(f, sl, l2); res = run(s, **kw); x, z, dth, v = cmp(base, bres, res, s)
        L.append(line('%s %d / %d / %d' % (key, f, sl, l2), x, z, dth, v, base) + ' ' + by_trig(res))
        t0 = sA.T[-1] - 28 * 86400000
        rec.append('%s %+.1f' % (key, sum(r['res'] for r in res if s.T[r['i']] >= t0) - sum(r['res'] for r in bres if sA.T[r['i']] >= t0)))
    L += ['', 'Last 4 weeks of the replay, Δ net vs standard (live-period check; the extra shallow pierces a faster slow EMA adds cannot be seen in the live alerts): ' + ' · '.join(rec)]
    return L + ['']


def study_mes2():
    """MES 2m (live settings: 1H MTF gate + HTF flips >= 4 in 8; HTF 10m) -- slow EMA watch (16; neighbours 12 / 24 / 28)."""
    import filter_sweep as fs
    B0 = ss.load('MES', 2); C = B0.c.values.astype(float); L0 = fs.LIVE[('MES', 2)]
    P = dict(er=.23, bo=3, r5=L0['r5'], r5z=.2, x4=L0['x4'], mtf=L0['mtf'], fl=L0['fl'])
    def case(sl):
        B = B0.copy(); B['e20'] = ema(C, sl); s = cs.Case('MES', 2, B); fs.prep(s); return s
    sA = case(20); bres = fs.run(sA, P); v0 = [r['res'] for r in bres]; net0 = sum(v0); sd = float(np.std(v0)) or 1
    t0 = ss.thirds(bres, sA.month, 2); C0 = {(r['i'], r['lg']) for r in bres}
    L = ['## MES 2m (%d candles, Jun–Oct) — watch: slow EMA 16 (1H MTF gate + HTF flips >= 4, base exits)' % len(B0), '',
         'Only the SLOW length changes the replay. Thirds = Jun–Jul / Aug / Sep–Oct.', '',
         '| Variant | Setups | Net | Δ vs standard | z | Δ by third | Verdict | LTF EMA20 Pierce setups / net |', '|---|---|---|---|---|---|---|---|']
    lt = lambda R: '%d / %+.0f' % (sum(r['trig'] == 'ltf20' for r in R), sum(r['res'] for r in R if r['trig'] == 'ltf20'))
    L.append('| A2 9 / 20 / 200 (standard) | %d | %+.0f | +0 | +0.0 | +0 / +0 / +0 | baseline | %s |' % (len(v0), net0, lt(bres)))
    rec = []
    t_end = sA.T[-1] - 28 * 86400000
    for key, sl in (('T2', 12), ('U2', 16), ('V2', 24), ('W2', 28)):
        s = case(sl); res = fs.run(s, P); v = [r['res'] for r in res]; net = sum(v)
        ch = len(C0 ^ {(r['i'], r['lg']) for r in res}) or 1; z = (net - net0) / (sd * np.sqrt(ch))
        dth = [a - b for a, b in zip(ss.thirds(res, s.month, 2), t0)]; b3 = all(x > 0 for x in dth)
        vd = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < net0 else 'noise'
        L.append('| %s 9 / %d / 200 | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %s |' % (key, sl, len(v), net, net - net0, z, *dth, vd, lt(res)))
        rec.append('%s %+.1f' % (key, sum(r['res'] for r in res if s.T[r['i']] >= t_end) - sum(r['res'] for r in bres if sA.T[r['i']] >= t_end)))
    L += ['', 'Last 4 weeks of the replay, Δ net vs standard: ' + ' · '.join(rec), '']
    return L


def main():
    out = ['# 5m chart EMA length + bar-gate study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for sym in ('MES', 'MGC'):
        L = study(sym)
        out += L
        summ += ['%s 5m: %s' % (sym, l.split('|')[1].strip() + ' → Δ ' + l.split('|')[6].strip() + ', z ' + l.split('|')[7].strip() + ', thirds ' + l.split('|')[8].strip() + ' (' + l.split('|')[9].strip() + ')') for l in L if l.startswith('| ') and l.rstrip().endswith(('robust |', 'promising |'))]
    L = study_mes3(); out += L
    L2 = study_mes2(); out += L2
    summ += ['MES 2m: %s' % (l.split('|')[1].strip() + ' → Δ ' + l.split('|')[4].strip() + ', z ' + l.split('|')[5].strip() + ', thirds ' + l.split('|')[6].strip() + ' (' + l.split('|')[7].strip() + ')') for l in L2 if l.startswith('| ') and l.split('|')[7].strip() in ('robust', 'promising')]
    summ += ['MES 3m: %s' % (l.split('|')[1].strip() + ' → Δ ' + l.split('|')[6].strip() + ', z ' + l.split('|')[7].strip() + ', thirds ' + l.split('|')[8].strip() + ' (' + l.split('|')[9].strip() + ')') for l in L if l.startswith('| ') and l.split('|')[9].strip() in ('robust', 'promising')]
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    out += live_part()
    print('\n'.join(out))


if __name__ == '__main__':
    main()
