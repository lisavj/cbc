import numpy as np, collections
import chop_sim as cs, late_study as ls, mes3_ema_grid as m
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
s = ls.LCase('MES', 3, B); e9 = m.ema(s.C, 9)
res = s.run(lambda d: cs.cur_rule(d), q=dict(m.LIVE, tp=2.0, part=1.0), gates=dict(R5=1, X4=0, MTF=0))
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
th = lambda r: 0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2
def cat(r):
    t = r['trig']
    if t == 'flip': return '1 HTF CBC Flip (bot)'
    if t == 'ltf20':
        if r.get('late'): return '4 LTF Pierce late confirm'
        b = (s.C[r['i']] > e9[r['i']]) if r['lg'] else (s.C[r['i']] < e9[r['i']])
        return '2 LTF Pierce beyond EMA9 (bot)' if b else '3 LTF Pierce not beyond EMA9'
    return ('5 HTF EMA9 Pierce' if t == 'h9' else '6 HTF EMA20 Pierce') + (' (late)' if r.get('late') else '')
W = {'0630-1300 + 1400-1430': lambda mm: 390 <= mm <= 780 or 840 <= mm <= 870,
     '0630-1300 + 1400-1545': lambda mm: 390 <= mm <= 780 or 840 <= mm < 945}
for wn, f in W.items():
    G = collections.defaultdict(list)
    for r in res:
        if f(s.hm[r['i']] % 1440): G[cat(r)].append(r)
    print('\n### %s (replay Jan 5 – Nov 5, bot exits)\n' % wn)
    print('| Trigger | Setups | Win % | Net | Avg | Thirds | +thirds |\n|---|---|---|---|---|---|---|')
    for k in sorted(G):
        v = [r['res'] for r in G[k]]; t = [sum(r['res'] for r in G[k] if th(r) == j) for j in range(3)]
        print('| %s | %d | %d%% | %+.0f | %+.2f | %+.0f / %+.0f / %+.0f | %d/3 |' % (k[2:], len(v), round(100*sum(x>0 for x in v)/max(1,sum(x!=0 for x in v))), sum(v), np.mean(v), *t, sum(x>0 for x in t)))
