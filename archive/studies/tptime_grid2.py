#!/usr/bin/env python3
"""Time-based TP1 reduction, fine grid -- 11/06/2026. X = 12..45 min by 3, Y = 50..90 % by 5. Same engine / settings as
tptime_study.py (mode A modified TP limit, mode B close at the candle close). Cell = Δ net vs current exits; flags:
T = better in all three thirds, 4 = better in the last 4 weeks, R = T and all 4 neighbours (±3 min, ±5 %) also better overall."""
import sys, numpy as np, datetime as D, pickle
import chop_sim as cs, late_study as ls, mes3_ema_grid as m, tptime_study as tt
XS = list(range(12, 46, 3)); YS = [y / 100 for y in range(50, 91, 5)]
def main(sym):
    nm, s_, q, G = [c for c in tt.CH if c[1] == sym][0]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
    s = tt.TCase(sym, 3, B)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    th = lambda res: [sum(r['res'] for r in res if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
    def run(x, y, mode):
        tt.TCase.X, tt.TCase.Y, tt.TCase.MODE = x, y, mode
        r = s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
        return sum(t['res'] for t in r), th(r), sum(t['res'] for t in r if s.T[t['i']] >= t4)
    bn, bt, b4 = run(0, 0, 'A')
    res = {}
    for mode in ('A', 'B'):
        for x in XS:
            for y in YS:
                n, t, l4 = run(x, y, mode); res[(mode, x, y)] = (n - bn, [a - c for a, c in zip(t, bt)], l4 - b4)
    pickle.dump((bn, res), open('grid2_%s.pkl' % sym, 'wb'))
if __name__ == '__main__':
    main(sys.argv[1])
