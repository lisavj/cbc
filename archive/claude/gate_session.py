"""Is the entry gate session-specific? MGC 3m: range gate (R5) + VWAP stretch gate (X4); MES 3m: range gate (R5) -- switched OFF per sub-session.
Usage: python3 gate_session.py MGC|MES"""
import sys, itertools, numpy as np, pandas as pd, chop_sim as cs, late_study as ls, trend_guard_study as tg, mes3_ema_grid as m
SYM=sys.argv[1] if len(sys.argv)>1 else 'MGC'
B=ls.load(SYM,3); ls.LCase.LATE=1; ls.LCase.NYW=30; s=ls.LCase(SYM,3,B); TR,ss=tg.trend_arrays(s)
et=pd.to_datetime(s.B.t,unit='ms',utc=True).dt.tz_convert('America/New_York'); mm=(et.dt.hour*60+et.dt.minute).values
def sub(m): return 'Asia' if (m>=1080 or m<180) else 'London' if m<570 else 'NY' if m<960 else 'late'
T0,T1=s.T[300],s.T[-1]; cuts=[T0+(T1-T0)*k/3 for k in (1,2)]; t4=T1-28*86400000
if SYM=='MGC': EX={'live 50 % / trail 3.5':dict(ls.MGCX,part=.5,tr=3.5),'old 80 % / trail 1.7':ls.MGCX}; COST=.22; GATES=('R5','X4')
else: EX={'live (SL1 3 ATR / TP1 1.75 / 80-100 % by time)':m.LIVE}; COST=.50; GATES=('R5',)
SUBS=['Asia','London','NY']
def run(q,off,gates=None,vwf=False):
    gates=gates or GATES
    def ok(d):
        if not cs.cur_rule(d): return False
        se=sub(mm[d['i']])
        for g in gates:
            if d[g] and se not in off: return False
        if vwf:
            v=TR['vwap'][d['i']]
            if not (v==0 or v==(1 if d['lg'] else -1)): return False
        return True
    r=s.run(ok,q=q,gates=dict(R5=0,X4=0,MTF=0))
    return [dict(n=t['res']-COST,th=0 if s.T[t['i']]<cuts[0] else 1 if s.T[t['i']]<cuts[1] else 2,l4=s.T[t['i']]>=t4,se=sub(mm[t['i']]),r5=bool(t['R5']),x4=bool(t['X4'])) for t in r]
def row(v,b):
    f=lambda r,P: sum(t['n'] for t in r if P(t))
    P=[lambda t:t['th']==0,lambda t:t['th']==1,lambda t:t['th']==2,lambda t:t['l4'],lambda t:True]
    d=[f(v,p)-f(b,p) for p in P]
    return len(v)-len(b),d,[f(v,lambda t,x=x:t['se']==x)-f(b,lambda t,x=x:t['se']==x) for x in SUBS]
L=['# %s 3m — entry gate off by session (%s)'%(SYM,pd.Timestamp.now().strftime('%m/%d/%Y')),'',
 ('Replay Jan 5 -> now, chop_sim rules, net after costs (%.2f pts/trade). Live gates = range gate (24 bars, top/bottom 20 %%, < 5 ATR)%s. '%(COST,' + VWAP stretch (> 4 ATR)' if SYM=='MGC' else ' (no stretch gate on MES 3m; the flip-timing gate is not modelled)'))+
 '"Off in X" = setups starting in that sub-session (ET: Asia 18:00-03:00, London 03:00-09:30, NY 09:30-16:00) are NOT gated; elsewhere the gate stays on. '
 'Δ vs gate on everywhere. ✓ = better in all three thirds.','']
for en,q in EX.items():
    base=run(q,set())
    GL=(('both gates (range + stretch)',('R5','X4')),('range gate only (stretch stays on)',('R5',)),('stretch gate only (range stays on)',('X4',))) if SYM=='MGC' else (('range gate',('R5',)),)
    for gl,gs in GL:
        L+=['## %s — exits %s: gate on everywhere = %d trades, net %+.0f'%(gl,en,len(base),sum(t['n'] for t in base)),'',
            '| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |','|---|---|---|---|---|---|---|---|---|']
        for k in range(1,4):
            for off in itertools.combinations(SUBS,k):
                other=[g for g in GATES if g not in gs]
                # gate(s) in gs off in `off`; other gate always on
                def ok_run():
                    def okf(d):
                        if not cs.cur_rule(d): return False
                        se=sub(mm[d['i']])
                        for g in gs:
                            if d[g] and se not in off: return False
                        for g in other:
                            if d[g]: return False
                        return True
                    r=s.run(okf,q=q,gates=dict(R5=0,X4=0,MTF=0))
                    return [dict(n=t['res']-COST,th=0 if s.T[t['i']]<cuts[0] else 1 if s.T[t['i']]<cuts[1] else 2,l4=s.T[t['i']]>=t4,se=sub(mm[t['i']])) for t in r]
                v=ok_run(); n,d,ds=row(v,base)
                L.append('| %s | %+d | %+.0f | %+.0f | %+.0f | %+.0f | **%+.0f** | %+.0f / %+.0f / %+.0f | %s |'%(' + '.join(off),n,*d,*ds,'✓' if all(x>0 for x in d[:3]) else ''))
        L.append('')
    # gated-out setups: what they would do, per session (gates off everywhere, trades flagged)
    allr=run(q,set(SUBS))
    L+=['**Setups the gates block (gates off everywhere, exits %s)** — trades / net / avg by session'%en,'','| Session | Range-gated | Stretch-gated | Not gated |','|---|---|---|---|']
    for x in SUBS:
        c=lambda P:[t['n'] for t in allr if t['se']==x and P(t)]
        L.append('| %s | %s | %s | %s |'%(x,*['%d / %+.0f / %+.2f'%(len(v),sum(v),np.mean(v) if v else 0) for v in (c(lambda t:t['r5']),c(lambda t:t['x4'] and not t['r5']),c(lambda t:not t['r5'] and not t['x4']))]))
    L.append('')
open('%s3_gate_session_report.md'%SYM.lower(),'w').write('\n'.join(L)); print('\n'.join(L))
q=list(EX.values())[0]; a=run(q,set(SUBS)); v=np.array([t['n'] for t in a if t['se']=='NY' and t['r5']]); sd=np.std([t['n'] for t in a])
print('NYR5', len(v), v.sum(), v.std(), 'z vs 0:', v.sum()/(sd*np.sqrt(len(v))), [round(sum(t['n'] for t in a if t['se']=='NY' and t['r5'] and t['th']==k),1) for k in range(3)], round(sum(t['n'] for t in a if t['se']=='NY' and t['r5'] and t['l4']),1), sum(1 for t in a if t['se']=='NY' and t['r5'] and t['l4']))
