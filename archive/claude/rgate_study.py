#!/usr/bin/env python3
"""Range gate sweep (MES 3m / MGC 3m) -- 11/02/2026.
Range gate = block a new setup when the 24-bar range is under x ATR and the close is in the top 20 % (long) / bottom 20 % (short).
x = OFF, 3.0 ... 6.0 by 0.5, one change on top of each chart's live settings (filter_sweep.LIVE: ER 0.23 + breakout, MGC 3m VWAP stretch 4).
Bars Jan 5 - Nov 2, base exits (ss.QB). Also: what the current gate (5) blocks, by trigger.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all thirds (Jan-Mar / Apr-Jun / Jul-Nov); promising = z >= 1 and all three.
"""
import sys, collections, numpy as np, chop_sim as cs, stretch_study as ss, filter_sweep as fs
ss.FROM[3] = '2026-01-05'
out = [__doc__.strip(), '']
for sym in ('MES', 'MGC'):
    L0 = fs.LIVE[(sym, 3)]
    base = dict(er=.23, bo=3, r5=L0['r5'], r5z=.2, x4=L0['x4'], mtf=0, fl=None)
    s = cs.Case(sym, 3, ss.load(sym, 3)); fs.prep(s)
    cur = fs.run(s, base); v0 = [r['res'] for r in cur]; n0 = sum(v0); sd = float(np.std(v0)) or 1
    t0 = ss.thirds(cur, s.month, 3); C0 = {(r['i'], r['lg']) for r in cur}
    te = s.T[-1] - 28 * 86400000; r40 = sum(r['res'] for r in cur if s.T[r['i']] >= te)
    w = sum(x > 0 for x in v0); l = sum(x < 0 for x in v0)
    out += ['## %s 3m — current (range gate 5 ATR): %d setups, win %.0f%%, net %+.0f, thirds %+.0f / %+.0f / %+.0f' % (sym, len(v0), 100 * w / (w + l), n0, *t0), '',
            '| Range gate | Setups | Win % | Net | Δ vs 5 | z | Δ by third | Verdict | Last 4 wk Δ |', '|---|---|---|---|---|---|---|---|---|']
    for x in (None, 3, 3.5, 4, 4.5, 5, 5.5, 6):
        P = dict(base); P['r5'] = x
        R = cur if x == base['r5'] else fs.run(s, P); v = [r['res'] for r in R]; n = sum(v)
        ch = len(C0 ^ {(r['i'], r['lg']) for r in R}) or 1; z = (n - n0) / (sd * np.sqrt(ch))
        d = [a - b for a, b in zip(ss.thirds(R, s.month, 3), t0)]; b3 = all(y > 0 for y in d)
        vd = 'current' if x == base['r5'] else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if n < n0 else 'noise'
        w = sum(y > 0 for y in v); l = sum(y < 0 for y in v)
        r4 = sum(r['res'] for r in R if s.T[r['i']] >= te) - r40
        out.append('| %s | %d | %.0f%% | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %+.1f |' % ('OFF' if x is None else '%.1f ATR' % x, len(v), 100 * w / max(1, w + l), n, n - n0, z, *d, vd, r4))
    # what gate 5 removes: setups present with OFF but not with 5
    P = dict(base); P['r5'] = None; off = fs.run(s, P)
    gone = [r for r in off if (r['i'], r['lg']) not in C0]
    g = collections.defaultdict(list)
    for r in gone: g[r['trig']].append(r['res'])
    out += ['', 'Setups present with the gate OFF but not with 5 ATR (by trigger, their OFF-run result): ' +
            ', '.join('%s %d / %+.0f (win %.0f%%)' % (k, len(v), sum(v), 100 * np.mean([y > 0 for y in v])) for k, v in g.items()), '']
print('\n'.join(out))
