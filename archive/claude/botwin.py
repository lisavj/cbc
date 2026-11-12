import numpy as np, pandas as pd, combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg, study5 as s5
sym='MES'; nm,q,G=cb.CH[sym]; B=ls.load(sym,3); ls.LCase.LATE=1; ls.LCase.NYW=30; s=cb.CCase(sym,3,B); TR,ss=tg.trend_arrays(s)
et=pd.to_datetime(s.B.t,unit='ms',utc=True).dt.tz_convert('America/New_York'); mm=(et.dt.hour*60+et.dt.minute).values
cm=(mm+3)%1440  # candle close time
inwin=lambda i: (1110<=cm[i]<=1320) or (180<=cm[i]<=780) or (900<=cm[i]<=930)   # v10.87 bot windows 1830-2200, 0300-1300, 1500-1530
T0,T1=s.T[300],s.T[-1]; cuts=[T0+(T1-T0)*k/3 for k in (1,2)]; t4=T1-28*86400000
def run(f,tp,sl):
    def ok(d):
        if not cs.cur_rule(d) or not inwin(d['i']): return False
        if f is None or (f[1]=='S' and d['lg']): return True
        v=TR[f[0]][d['i']]; return v==0 or v==(1 if d['lg'] else -1)
    cb.CCase.TX,cb.CCase.TY=tp; cb.CCase.ACT,cb.CCase.SY,cb.CCase.SX=sl
    return [dict(i=t['i'],j=t['j'],why=t['why'],n=t['res']-.5-(.25 if t['why']=='cut' else 0),th=0 if s.T[t['i']]<cuts[0] else 1 if s.T[t['i']]<cuts[1] else 2,l4=bool(s.T[t['i']]>=t4),ss=ss[t['i']],sub=s5.sub(mm[t['i']])) for t in s.run(ok,q=q,gates=G)]
N=(0,0.0); X=(None,0.0,0); TP=(18,.85); SL=('HALF',0.0,18)
b=run(None,N,X)
sets=[('Current exits',b),('TP1 -> 85 % after 18 min',run(None,TP,X)),('SL: half SL1 if negative at 18 min',run(None,N,SL)),('TP + SL rules',run(None,TP,SL)),
      ('5-day short filter',run(('d5','S'),N,X)),('Filter + TP rule',run(('d5','S'),TP,X))]
f2=run(('d5','S'),N,SL); sets.append(('Balanced: filter + losing-stretch stop + SL rule',s5.apply_stop(('r',2,2),f2,b)))
f3=run(('d5','S'),TP,X); sets.append(('Filter + losing-stretch stop + TP rule',s5.apply_stop(('r',2,2),f3,b)))
ab=np.mean([t['n'] for t in b])
P=[lambda t:t['th']==0,lambda t:t['th']==1,lambda t:t['th']==2,lambda t:t['l4'],lambda t:True]
OUT=['# MES 3m bot-window check — run '+pd.Timestamp.now().strftime('%m/%d/%Y'),'','Replay of MES 3m setups that START inside the bot entry windows (candle close 18:30-22:00, 03:00-13:00, 15:00-15:30 ET = v10.87 bot windows), live MES 3m exits, net after costs (0.50 pts per trade, +0.25 for a rule exit). Brackets = gain beyond dropping the same number of trades at random. Bot trigger choices are not modelled.','']
OUT.append('| Rule set (bot windows only) | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | PF | Max DD |'); OUT.append('|---|---|---|---|---|---|---|---|---|')
for lab,v in sets:
    cells=[]
    for p in P:
        n1=sum(t['n'] for t in v if p(t)); n0=sum(t['n'] for t in b if p(t)); c1=sum(1 for t in v if p(t)); c0=sum(1 for t in b if p(t))
        cells.append('%+.0f (%+.0f)'%(n1,n1-n0+(c0-c1)*ab))
    x=np.array([t['n'] for t in v]); eq=np.cumsum(x); dd=(np.maximum.accumulate(np.r_[0,eq])[1:]-eq).max()
    OUT.append('| %s | %s | %d | %.2f | %.0f |'%(lab,' | '.join(cells),len(v),x[x>0].sum()/-x[x<0].sum(),dd))

open('botwin_report.md','w').write('\n'.join(OUT)+'\n'); print('\n'.join(OUT))
