import numpy as np
import chop_sim as cs, late_study as ls, mes3_ema_grid as m
B = ls.load('MES', 3)
def go(nyw):
    ls.LCase.LATE = 1; ls.LCase.NYW = nyw; s = ls.LCase('MES', 3, B); e9 = m.ema(s.C, 9)
    res = s.run(lambda d: cs.cur_rule(d), q=dict(m.LIVE, tp=2.0, part=1.0), gates=dict(R5=1, X4=0, MTF=0))
    bot = lambda r: r['trig'] == 'flip' or (r['trig'] == 'ltf20' and not r.get('late') and ((s.C[r['i']] > e9[r['i']]) if r['lg'] else (s.C[r['i']] < e9[r['i']])))
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
    th = lambda r: 0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2
    return s, res, bot, th
for nyw in (30, 0):
    s, res, bot, th = go(nyw)
    for nm, f in (('all triggers', lambda r: True), ('bot set', bot)):
        L = [r for r in res if f(r)]
        om = lambda r: (s.hm[r['i']] - 3) % 1440
        slot = [r for r in L if 570 <= om(r) < 600]
        print('block %2d | %-12s | total %4d net %+5.0f | 9:30-10:00 setups %2d net %+6.1f avg %+.2f thirds %s | 9:30-9:45 %+.1f (%d) 9:45-10 %+.1f (%d)' % (
            nyw, nm, len(L), sum(r['res'] for r in L), len(slot), sum(r['res'] for r in slot), np.mean([r['res'] for r in slot]) if slot else 0,
            [round(sum(r['res'] for r in slot if th(r) == j)) for j in range(3)],
            sum(r['res'] for r in slot if om(r) < 585), sum(1 for r in slot if om(r) < 585), sum(r['res'] for r in slot if om(r) >= 585), sum(1 for r in slot if om(r) >= 585)))
