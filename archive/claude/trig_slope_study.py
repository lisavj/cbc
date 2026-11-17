"""Per-trigger results, current filters vs + "Block in chop: HTF EMA20 slope below 0.3 ATR" -- MES 3m and MGC 3m -- 11/14/2026.
Replay Jan 5 -> now, CBC engine setups, current filters (ER 0.23 + breakout 3, range gate 5 ATR, MGC VWAP stretch 4 ATR applied correctly),
live exits (MES 3m SL1 3 ATR min 5, TP1 1.75, 100 % at TP1; MGC 3m SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, FLIP 0 %). Net after costs
(MES 0.50, MGC 0.22). Trigger = the setup's first trigger. "Blocked" = setups in the current run that are absent with the slope filter
(the filter also lets some new setups in, because one setup at a time / cooldown). Thirds by date."""
import sys, numpy as np, pandas as pd, collections
import combo_study as cb, chop_sim as cs, late_study as ls
X = {'MES': dict(c=.5, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7), x4=None),
     'MGC': dict(c=.22, q=dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9), x4=4.0)}
NM = {'flip': 'HTF CBC Flip', 'ltf20': 'LTF EMA20 Pierce', 'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}
out = [__doc__, '']
for sym in ('MES', 'MGC'):
    x = X[sym]; B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B)
    C, H, L, A = s.C, s.H, s.L, s.atr; S = pd.Series
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    hh24, ll24 = S(H).rolling(24).max().values, S(L).rolling(24).min().values
    h20 = B.h20.values.astype(float); SLP = np.abs(h20 - np.roll(h20, 12)) / A
    def ok(d, slope):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
        if not cs.cur_rule(d): return False
        w = hh24[i] - ll24[i]
        if w > 0 and w / a < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        if x['x4'] and g * (C[i] - s.vw[i]) / a > x['x4']: return False
        if slope and SLP[i] < slope: return False
        return True
    RR = {sl: s.run(lambda d, sl=sl: ok(d, sl), q=x['q'], gates=dict(R5=0, X4=0, MTF=0)) for sl in (0, .3)}
    trigs = sorted({r['trig'] for R in RR.values() for r in R}, key=lambda t: list(NM).index(t) if t in NM else 9)
    def st(R):
        v = np.array([r['res'] - x['c'] for r in R]) if R else np.array([0.])
        th = [sum(r['res'] - x['c'] for r in R if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        l4 = sum(r['res'] - x['c'] for r in R if s.T[r['i']] >= t4)
        return len(R), v.sum() if R else 0, v.mean() if R else 0, (100 * (v > 0).mean()) if R else 0, th, l4
    keys1 = {(r['i'], r['lg']) for r in RR[.3]}
    rows = []
    for t in trigs + ['ALL']:
        sel = lambda R: [r for r in R if t == 'ALL' or r['trig'] == t]
        a = st(sel(RR[0])); b = st(sel(RR[.3])); bl = st([r for r in sel(RR[0]) if (r['i'], r['lg']) not in keys1])
        rows.append('| %s | %d / %+.0f / %+.2f / %.0f %% | %+.0f / %+.0f / %+.0f | %+.0f | %d / %+.0f / %+.2f / %.0f %% | %+.0f / %+.0f / %+.0f | %+.0f | %+.0f | %d / %+.0f / %+.2f |' % (
            '**ALL**' if t == 'ALL' else NM.get(t, t), *a[:4], *a[4], a[5], *b[:4], *b[4], b[5], b[1] - a[1], bl[0], bl[1], bl[2]))
    out += ['## %s 3m' % sym, '', '| Trigger | Current: n / net / avg / win | Current thirds | Current last 4 wk | Slope 0.3: n / net / avg / win | Slope thirds | Slope last 4 wk | Δ net | Blocked by slope: n / net / avg |',
            '|---|---|---|---|---|---|---|---|---|'] + rows + ['']
    print('done', sym, file=sys.stderr, flush=True)
open('trig_slope_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
