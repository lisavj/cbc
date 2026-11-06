import numpy as np, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
s = ls.LCase('MES', 3, B)
G = dict(R5=1, X4=0, MTF=0)
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
th = lambda res: [sum(r['res'] for r in res if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
def run(cap, tp=2.0):
    return s.run(lambda d: cs.cur_rule(d), q=dict(m.LIVE, tp=tp, tcap=cap), gates=G)
for tp in (2.0, 1.5):
    b = run(1e9, tp); bv = [r['res'] for r in b]; bn = sum(bv); sd = np.std(bv); bset = {(r['i'], r['lg']) for r in b}; bt = th(b); b4 = sum(r['res'] for r in b if s.T[r['i']] >= t4)
    print('\n### TP1 %.1f x ATR' % tp)
    print('| TP1 cap | Setups | Win %% | Net | Δ vs no cap | z | Δ by third | Last 4 wk Δ | Setups where cap binds |')
    print('|---|---|---|---|---|---|---|---|---|')
    for cap in (1e9, 20, 15, 12, 10, 8):
        r = run(cap, tp); v = [x['res'] for x in r]; net = sum(v)
        ch = len(bset ^ {(x['i'], x['lg']) for x in r}) or 1; z = (net - bn) / (sd * np.sqrt(ch))
        dth = [a - c for a, c in zip(th(r), bt)]
        bind = sum(tp * s.atr[x['i']] > cap for x in r)
        print('| %s | %d | %d%% | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.1f | %d (%.0f%%) |' % ('none (live)' if cap > 1e8 else '%d pts' % cap, len(v), round(100*sum(x>0 for x in v)/max(1,sum(x!=0 for x in v))), net, net-bn, 0 if cap>1e8 else z, *dth, sum(x['res'] for x in r if s.T[x['i']]>=t4)-b4, bind, 100*bind/len(r)))
a = s.atr[300:]; a = a[~np.isnan(a)]
print('\n3m ATR percentiles (pts): 50%% %.1f · 75%% %.1f · 90%% %.1f · 99%% %.1f · max %.1f' % (*np.percentile(a, [50, 75, 90, 99]), a.max()))
