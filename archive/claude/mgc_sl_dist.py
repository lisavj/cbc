import sys, io, contextlib, numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import mgc_sl_study as M
rows = []
for lab, slm, cap in (('1.7 ATR, cap 7 (live)', 1.7, 7), ('1.5 ATR, no cap', 1.5, 1e9), ('1.7 ATR, no cap', 1.7, 1e9), ('2.0 ATR, no cap', 2.0, 1e9)):
    v = []; sds = []
    for (i, lg, stop) in M.ST:
        r, sd = M.sim(i, lg, stop, slm, 5, cap, 0.0, 'FLIP')
        if r is not None: v.append(r - M.c); sds.append(sd)
    v = np.array(v); sds = np.array(sds)
    rows.append((lab, v, sds))
out = ['MGC 3m, FLIP 0 % exit (v10.96), replay Jan 5 -> now, pts per trade after 0.22 cost (1 pt = $10 per micro).', '',
       '| SL1 | Trades | Win % | Breakeven-ish (|r| < 0.5) | Loss % | Net | Avg win | Avg loss | Max profit | Max loss | Avg stop | Largest stop |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
for lab, v, sds in rows:
    w = v[v > 0.5]; l = v[v < -0.5]
    out.append('| %s | %d | %.0f %% | %.0f %% | %.0f %% | %+.0f | %+.2f | %+.2f | %+.1f | %+.1f | %.1f | %.1f |' % (lab, len(v), 100 * (v > 0).mean(), 100 * (abs(v) <= .5).mean(), 100 * (v < -.5).mean(), v.sum(), w.mean(), l.mean(), v.max(), v.min(), sds.mean(), sds.max()))
out += ['', 'Distribution of trade results (percentiles, pts): 10 % of trades did worse than the P10 value, etc.', '',
        '| SL1 | P0 (min) | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 (max) |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
for lab, v, sds in rows:
    out.append('| %s | %s |' % (lab, ' | '.join('%+.1f' % np.percentile(v, p) for p in range(0, 101, 10))))
out += ['', 'Share of total profit by decile of trades (sorted worst -> best, each = 10 % of trades), pts:', '',
        '| SL1 | D1 (worst) | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 (best) |', '|---|---|---|---|---|---|---|---|---|---|---|']
for lab, v, sds in rows:
    sv = np.sort(v); parts = np.array_split(sv, 10)
    out.append('| %s | %s |' % (lab, ' | '.join('%+.0f' % p.sum() for p in parts)))
out += ['', 'Trades by result band (pts):', '', '| SL1 | <= -10 | -10..-7 | -7..-5 | -5..-2 | -2..-0.5 | about 0 (+-0.5) | 0.5..5 | 5..10 | 10..20 | 20..40 | > 40 |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
bands = [(-1e9, -10), (-10, -7), (-7, -5), (-5, -2), (-2, -.5), (-.5, .5), (.5, 5), (5, 10), (10, 20), (20, 40), (40, 1e9)]
for lab, v, sds in rows:
    out.append('| %s | %s |' % (lab, ' | '.join('%.0f %%' % (100 * ((v > a) & (v <= b)).mean()) for a, b in bands)))
open('mgc_sl_dist.md', 'w').write('\n'.join(out)); print('\n'.join(out))
