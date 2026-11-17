"""MGC 5m: close % at TP1 x runner trail (replay Jan 5 -> now, chop_sim, base exits SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6, BE, no gates). Net after 0.32 pt cost per trade. Current MGC 5m = 80 % / trail 1.7. Thirds Jan-Mar / Apr-Jun / Jul-now."""
import numpy as np, chop_sim as cs, stretch_study as ss
ss.FROM[5] = '2026-01-05'
s = cs.Case('MGC', 5, ss.load('MGC', 5))
q0 = dict(ss.QB['MGC']); G = dict(R5=0, X4=0, MTF=0); COST = .32
te = s.T[-1] - 28 * 86400000
def run(part, tr):
    R = s.run(cs.cur_rule, q=dict(q0, part=part, tr=tr), gates=G)
    v = np.array([r['res'] - COST for r in R])
    return R, v.sum(), [x - COST * sum(1 for r in R if lo <= s.month[r['i']] <= hi) for x, (lo, hi) in zip(ss.thirds(R, s.month, 5), ((1, 3), (4, 6), (7, 12)))], sum(r['res'] - COST for r in R if s.T[r['i']] >= te), v
R0, n0, t0, l0, v0 = run(.8, 1.7); sd = v0.std()
K0 = {(r['i'], r['lg']): r['res'] for r in R0}
print(__doc__); print('Current 80 %% / trail 1.7: %d trades, net %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f\n' % (len(v0), n0, *t0, l0))
print('| Close at TP1 | Trail | Net | Δ | z | Δ by third | Δ last 4 wk | Verdict |'); print('|---|---|---|---|---|---|---|---|')
for p in (.8, .6, .5, .4):
    for tr in (1.7, 2.5, 3.5, 4.5):
        if (p, tr) == (.8, 1.7): continue
        R, n, t, l, v = run(p, tr)
        K = {(r['i'], r['lg']): r['res'] for r in R}; ch = sum(1 for k in set(K) | set(K0) if abs(K.get(k, 1e9) - K0.get(k, 1e9)) > 1e-9) or 1
        z = (n - n0) / (sd * np.sqrt(ch)); d = [a - b for a, b in zip(t, t0)]
        vd = 'robust' if z >= 2 and all(x > 0 for x in d) else 'promising' if z >= 1 and all(x > 0 for x in d) else 'worse' if n < n0 else 'noise'
        print('| %d %% | %.1f | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.1f | %s |' % (p * 100, tr, n, n - n0, z, *d, l - l0, vd), flush=True)
