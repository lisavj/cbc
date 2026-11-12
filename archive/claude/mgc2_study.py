#!/usr/bin/env python3
"""MGC 2m improvement battery -- 11/02/2026 (11/08: range gate 24 bars / 20 % / 5 ATR now part of the live baseline, v10.77).
Replay Jun 1 -> now, live MGC 2m settings (ER 0.23 + breakout + range gate 5 ATR), base exits
(SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6, 80 % at TP1, BE, trail 1.7). One change at a time. Thirds Jun-Jul / Aug / Sep-Nov.
Not modelled: v10.77 "skip NON-flip setups while the HTF flip is a flop" (MGC 2m).
z = change / (SD x sqrt(setups changed)); for exit changes 'changed' = setups whose result changed."""
import numpy as np, chop_sim as cs, stretch_study as ss, filter_sweep as fs
s = cs.Case('MGC', 2, ss.load('MGC', 2)); fs.prep(s)
P0 = dict(er=.23, bo=3, r5=5, r5z=.2, x4=None, mtf=0, fl=None); q0 = dict(ss.QB['MGC']); keep = list(s.cands)
def run(P=P0, q=q0, skip=(), mtf=0, extra=None):
    s.cands = [d for d in keep if d['trig'] not in skip]
    ok = fs.make_ok(s, P)
    try: return s.run((lambda d: ok(d) and extra(d)) if extra else ok, q=q, gates=dict(R5=0, X4=0, MTF=mtf))
    finally: s.cands = keep
cur = run(); v0 = np.array([r['res'] for r in cur]); n0 = v0.sum(); sd = float(np.std(v0)); t0 = ss.thirds(cur, s.month, 2)
K0 = {(r['i'], r['lg']): r['res'] for r in cur}; te = s.T[-1] - 28 * 86400000; r40 = sum(r['res'] for r in cur if s.T[r['i']] >= te)
print('Current (incl. range gate 5 ATR): %d setups, net %+.0f pts ($%+.0f), thirds %+.0f / %+.0f / %+.0f\n' % (len(v0), n0, 10 * n0, *t0))
print('| Change | Setups | Net | Δ | z | Δ by third | Verdict | Last 4 wk Δ |'); print('|---|---|---|---|---|---|---|---|')
def row(nm, R):
    v = np.array([r['res'] for r in R]); n = v.sum(); K = {(r['i'], r['lg']): r['res'] for r in R}
    ch = sum(1 for k in set(K) | set(K0) if abs(K.get(k, 1e9) - K0.get(k, 1e9)) > 1e-9) or 1
    z = (n - n0) / (sd * np.sqrt(ch)); d = [a - b for a, b in zip(ss.thirds(R, s.month, 2), t0)]; b3 = all(x > 0 for x in d)
    vd = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if n < n0 else 'noise'
    print('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %+.1f |' % (nm, len(v), n, n - n0, z, *d, vd, sum(r['res'] for r in R if s.T[r['i']] >= te) - r40), flush=True)
for p in (.5, .6, .7, .9, 1.0): row('Close %d %% at TP1' % (p * 100), run(q=dict(q0, part=p)))
for x in (1.3, 1.5, 2.0): row('SL1 %.1f ATR' % x, run(q=dict(q0, sl=x)))
for x in (3, 4, 6): row('Min SL %d pts' % x, run(q=dict(q0, mn=x)))
for x in (6, 8, 10): row('Max SL cap %d pts' % x, run(q=dict(q0, cap=x)))
for x in (1.3, 2.0, 2.5): row('TP1 %.1f ATR' % x, run(q=dict(q0, tp=x)))
for x in (1.3, 2.0, 2.5): row('Trail %.1f ATR' % x, run(q=dict(q0, tr=x)))
row('No breakeven at TP1', run(q=dict(q0, be=False)))
for t, nm in (('flip', 'HTF CBC Flip'), ('ltf20', 'LTF EMA20 Pierce'), ('h9', 'HTF EMA9 Pierce'), ('h20', 'HTF EMA20 Pierce')): row('Trigger OFF: ' + nm, run(skip=(t,)))
row('Trigger OFF: HTF EMA9 + EMA20', run(skip=('h9', 'h20')))
row('Range gate OFF (pre-v10.77)', run(P=dict(P0, r5=None)))
for x in (4, 6): row('Range gate %d ATR (24 bars, 20 %%)' % x, run(P=dict(P0, r5=x)))
row('Range gate 4 ATR, zone 30 %', run(P=dict(P0, r5=4, r5z=.3)))
row('Range gate 5 ATR, zone 30 %', run(P=dict(P0, r5z=.3)))
for x in (3., 4., 6.): row('VWAP stretch %g ATR' % x, run(P=dict(P0, x4=x)))
row('1H MTF gate (skip against 60m CBC)', run(mtf=1))
for x in (3, 4): row('HTF flips >= %d in 8 block' % x, run(P=dict(P0, fl=x)))
row('Block 22:30-03:00 setups', run(extra=lambda d: not (s.hm[d['i']] >= 1350 or s.hm[d['i']] < 180)))
row('Block 07:45-09:30 setups', run(extra=lambda d: not (465 <= s.hm[d['i']] < 570)))
row('Block 16:00-18:00 setups', run(extra=lambda d: not (960 <= s.hm[d['i']] < 1080)))
row('NY session only (09:30-17:00)', run(extra=lambda d: 570 <= s.hm[d['i']] < 1020))
