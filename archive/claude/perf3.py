import numpy as np, datetime as D, combo_study as cb, chop_sim as cs, late_study as ls
COST = {'MES': .5, 'MGC': .22}
CFG = {'MES': [('Current exits', (0, 0.0), (None, 0.0, 0)), ('TP rule alone: TP1 -> 85 % after 18 min', (18, .85), (None, 0.0, 0)),
               ('SL rule alone: half SL1 if negative at 18 min', (0, 0.0), ('HALF', 0.0, 18)), ('Both rules', (18, .85), ('HALF', 0.0, 18))],
       'MGC': [('Current exits', (0, 0.0), (None, 0.0, 0)), ('TP rule alone: TP1 -> 65 % after 21 min', (21, .65), (None, 0.0, 0)),
               ('SL rule alone: cut if < 25 % of TP1 at 18 min', (0, 0.0), ('CUT', .25, 18)), ('Both rules', (21, .65), ('CUT', .25, 18))]}
def st(v):
    v = np.array(v); w = v[v > 0].sum(); l = -v[v < 0].sum(); eq = np.cumsum(v)
    dd = (np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max() if len(v) else 0
    return '%d | %+.0f | %+.2f | %d %% | %.2f | %.0f' % (len(v), v.sum(), v.mean() if len(v) else 0, round(100 * (v > 0).sum() / max(1, (v != 0).sum())), w / l if l else 0, dd)
for sym in ('MES', 'MGC'):
    nm, q, G = cb.CH[sym]; B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    f = lambda t: D.datetime.utcfromtimestamp(t / 1000).strftime('%m/%d')
    per = [('Third 1 (%s–%s)' % (f(T0), f(cuts[0])), lambda t: t < cuts[0]), ('Third 2 (%s–%s)' % (f(cuts[0]), f(cuts[1])), lambda t: cuts[0] <= t < cuts[1]),
           ('Third 3 (%s–%s)' % (f(cuts[1]), f(T1)), lambda t: t >= cuts[1]), ('Last 4 weeks (%s–%s)' % (f(t4), f(T1)), lambda t: t >= t4), ('Whole period', lambda t: True)]
    print('\n## %s\n' % nm)
    rows = {}
    for lab, tp, sl in CFG[sym]:
        cb.CCase.TX, cb.CCase.TY = tp; cb.CCase.ACT, cb.CCase.SY, cb.CCase.SX = sl
        rows[lab] = s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
    for pn, P in per:
        for kind in ('gross', 'after costs'):
            print('**%s — %s**\n\n| Exits | Trades | Net pts | Avg / trade | Win %% | Profit factor | Max drawdown |\n|---|---|---|---|---|---|---|' % (pn, kind))
            for lab in rows:
                v = [t['res'] - (0 if kind == 'gross' else COST[sym] + (.25 if sym == 'MES' else .1) * (t['why'] == 'cut')) for t in rows[lab] if P(s.T[t['i']])]
                print('| %s | %s |' % (lab, st(v)))
            print()
