"""MGC 3m range gate 4.0 combos -- 11/02/2026. Baseline = live (gate 5 / 24 bars / 20 % zone, VWAP stretch 4, ER 0.23 + breakout)."""
import numpy as np, pandas as pd, collections, chop_sim as cs, stretch_study as ss, filter_sweep as fs
ss.FROM[3]='2026-01-05'
s=cs.Case('MGC',3,ss.load('MGC',3)); fs.prep(s)
HH={n:(pd.Series(s.H).rolling(n).max().values,pd.Series(s.L).rolling(n).min().values) for n in (12,18,24,30,36,48)}
base=dict(er=.23,bo=3,r5=5,r5z=.2,x4=4.0,mtf=0,fl=None)
def run(P,n=24,exempt=(),sess=None):
    s.hh24,s.ll24=HH[n]; okA=fs.make_ok(s,P); P2=dict(P); P2['r5']=None; okB=fs.make_ok(s,P2)
    def ok(d):
        free=d['trig'] in exempt or (sess is not None and not sess(s.hm[d['i']]))
        return okB(d) if free else okA(d)
    R=s.run(ok,q=ss.QB['MGC'],gates=dict(R5=0,X4=0,MTF=0)); s.hh24,s.ll24=HH[24]; return R
cur=run(base); v0=[r['res'] for r in cur]; n0=sum(v0); sd=float(np.std(v0)); t0=ss.thirds(cur,s.month,3); C0={(r['i'],r['lg']) for r in cur}
te=s.T[-1]-28*86400000; r40=sum(r['res'] for r in cur if s.T[r['i']]>=te)
print('| Variant | Setups | Win % | Net | Δ vs live (5) | z | Δ by third (Jan–Mar / Apr–Jun / Jul–Nov) | Verdict | Last 4 wk |'); print('|---|---|---|---|---|---|---|---|---|')
def row(nm,R):
    v=[r['res'] for r in R]; n=sum(v); ch=len(C0^{(r['i'],r['lg']) for r in R}) or 1; z=(n-n0)/(sd*np.sqrt(ch))
    d=[a-b for a,b in zip(ss.thirds(R,s.month,3),t0)]; b3=all(x>0 for x in d)
    vd='robust' if z>=2 and b3 else 'promising' if z>=1 and b3 else 'worse' if n<n0 else 'noise'
    w=sum(x>0 for x in v); l=sum(x<0 for x in v)
    print('| %s | %d | %.0f%% | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %+.1f |'%(nm,len(v),100*w/(w+l),n,n-n0,z,*d,vd,sum(r['res'] for r in R if s.T[r['i']]>=te)-r40),flush=True)
P4=dict(base,r5=4)
row('Gate 4.0 (24 bars, 20 %)',run(P4))
for z_ in (.10,.15,.25,.30): row('Gate 4.0, zone %d %%'%(z_*100),run(dict(P4,r5z=z_)))
for n in (12,18,30,36,48): row('Gate 4.0, %d bars'%n,run(P4,n=n))
for n,x in ((18,3.5),(36,4.5),(36,5),(48,5),(48,6)): row('Gate %.1f, %d bars'%(x,n),run(dict(base,r5=x),n=n))
row('Gate 4.0, 15m flips exempt',run(P4,exempt=('flip',)))
row('Gate 4.0, HTF EMA9 pierces exempt',run(P4,exempt=('h9',)))
row('Gate 4.0, NY only (09:30-17:00)',run(P4,sess=lambda m:570<=m<1020))
row('Gate 4.0, London only (03:00-07:45)',run(P4,sess=lambda m:180<=m<465))
row('Gate 4.0, outside NY',run(P4,sess=lambda m:not(570<=m<1020)))
for x in (3.5,4.5,5,6,None): row('Gate 4.0 + VWAP stretch %s'%('OFF' if x is None else x),run(dict(P4,x4=x)))
for e in (.20,.26): row('Gate 4.0 + ER %.2f'%e,run(dict(P4,er=e)))
row('Gate 4.0 + flips >= 4 block',run(dict(P4,fl=4)))
# Apr-Jun loss: what gate 4 lets back in
R=run(P4); add=[r for r in R if (r['i'],r['lg']) not in C0]
g=collections.defaultdict(list)
for r in add: g[(ss.thirds([r],s.month,3).index(r['res']) if r['res'] else 0, r['trig'])].append(r['res'])
by=collections.defaultdict(list)
for r in add:
    th=[k for k,x in enumerate(ss.thirds([r],s.month,3)) if x][0] if r['res'] else -1
    by[(th,r['trig'])].append(r['res'])
print('\nSetups added by gate 4.0 (third, trigger: n / net):', '; '.join('%s %s %d / %+.0f'%(['Jan–Mar','Apr–Jun','Jul–Nov','zero'][k[0]],k[1],len(v),sum(v)) for k,v in sorted(by.items())))
