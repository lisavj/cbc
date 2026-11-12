"""MES 3m entry-time study in 30-min slots (entry candle CLOSE time, ET), with and without the 5-day short filter -- 11/08/2026.
Net after costs (0.50 pts per trade). Post-hoc: the bot only OPENS trades in the chosen slots; CBC setups themselves are unchanged."""
import numpy as np, pandas as pd, combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg
sym='MES'; nm,q,G=cb.CH[sym]; B=ls.load(sym,3); ls.LCase.LATE=1; ls.LCase.NYW=30; s=cb.CCase(sym,3,B); TR,ss=tg.trend_arrays(s)
et=pd.to_datetime(s.B.t,unit='ms',utc=True).dt.tz_convert('America/New_York'); mm=(et.dt.hour*60+et.dt.minute).values; cm=(mm+3)%1440
T0,T1=s.T[300],s.T[-1]; cuts=[T0+(T1-T0)*k/3 for k in (1,2)]; t4=T1-28*86400000
def run(f):
    def ok(d):
        if not cs.cur_rule(d): return False
        if f is None or d['lg']: return True
        v=TR['d5'][d['i']]; return v==0 or v==-1
    cb.CCase.TX,cb.CCase.TY=(0,0.0); cb.CCase.ACT,cb.CCase.SY,cb.CCase.SX=(None,0.0,0)
    return [dict(i=t['i'],n=t['res']-.5,lg=t['lg'],slot=int(cm[t['i']]//30),th=0 if s.T[t['i']]<cuts[0] else 1 if s.T[t['i']]<cuts[1] else 2,l4=bool(s.T[t['i']]>=t4)) for t in s.run(ok,q=q,gates=G)]
R={'no filter':run(None),'5-day short filter':run(1)}
lab=lambda k:'%02d:%02d-%02d:%02d'%(k*30//60,k*30%60,(k+1)*30//60%24,(k+1)*30%60)
ORDER=list(range(36,48))+list(range(0,32))   # 18:00 -> 16:00
BOT=lambda c:(1110<=c<=1320) or (180<=c<=840) or (900<=c<=930)
def inbot(k): return BOT(k*30+15)
L=[__doc__,'']
for name,r in R.items():
    L+=['## %s'%name,'','| Slot (ET, candle close) | In bot window now | Trades | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Avg / trade | Thirds positive |','|---|---|---|---|---|---|---|---|---|---|']
    for k in ORDER:
        v=[t for t in r if t['slot']==k]
        if not v: continue
        th=[sum(t['n'] for t in v if t['th']==x) for x in range(3)]; w=sum(t['n'] for t in v)
        L.append('| %s | %s | %d | %+.0f | %+.0f | %+.0f | %+.0f | %+.0f | %+.2f | %d |'%(lab(k),'yes' if inbot(k) else '',len(v),*th,sum(t['n'] for t in v if t['l4']),w,w/len(v),sum(x>0 for x in th)))
    L.append('')
    # window choices
    slots=sorted({t['slot'] for t in r})
    def tot(sel,P=lambda t:True): v=[t for t in r if t['slot'] in sel and P(t)]; return sum(t['n'] for t in v),len(v)
    def row(lb,sel):
        o=[tot(sel,lambda t,x=x:t['th']==x) for x in range(3)]; l4=tot(sel,lambda t:t['l4']); w=tot(sel)
        return '| %s | %d | %s | %+.0f | %+.0f |'%(lb,w[1],' | '.join('%+.0f'%a for a,_ in o),l4[0],w[0])
    botsel={k for k in slots if inbot(k)}
    cons={k for k in slots if sum(sum(t['n'] for t in r if t['slot']==k and t['th']==x)>0 for x in range(3))>=2 and sum(t['n'] for t in r if t['slot']==k)>0}
    wf={k for k in slots if sum(t['n'] for t in r if t['slot']==k and t['th']<2)>0}
    L+=['**Window choices (%s)**'%name,'','| Window | Trades | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole |','|---|---|---|---|---|---|---|',
        row('All hours',set(slots)),row('Current bot windows',botsel),
        row('Slots positive overall AND in >= 2 of 3 thirds (%d slots)'%len(cons),cons),
        row('Walk-forward: slots positive in thirds 1-2 only (%d slots) — judge on Third 3 / Last 4 wk'%len(wf),wf),
        row('Current bot windows minus slots negative in >= 2 thirds',botsel-{k for k in slots if sum(sum(t['n'] for t in r if t['slot']==k and t['th']==x)<0 for x in range(3))>=2}),'',
        'Consistent slots: '+', '.join(lab(k) for k in ORDER if k in cons),'',
        'Walk-forward slots: '+', '.join(lab(k) for k in ORDER if k in wf),'']
open('slot30_report.md','w').write('\n'.join(L)); print('\n'.join(L))

# proposal: drop slots negative in thirds 1+2 AND every third, add 14:00-15:00 and 15:30-16:00
DROP={7,12,15,26,27}; ADD={28,29,31}
L2=['','## Proposed bot windows (5-day short filter on)','','Drop 03:30-04:00, 06:00-06:30, 07:30-08:00, 13:00-14:00 (negative in every third, and already negative in thirds 1-2 = would have been dropped in a walk-forward); add 14:00-15:00 and 15:30-16:00 (bot flattens 15:57).','',
    '| Window | Trades | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Max DD |','|---|---|---|---|---|---|---|---|']
for name in ('no filter','5-day short filter'):
    r=R[name]; slots={t['slot'] for t in r}; botsel={k for k in slots if inbot(k)}
    for lb,sel in (('Current bot windows',botsel),('Current minus the 5 bad slots',botsel-DROP),('Proposed (minus bad + 14:00-15:00 + 15:30-16:00)',(botsel-DROP)|ADD)):
        v=sorted([t for t in r if t['slot'] in sel],key=lambda t:t['i']); x=np.array([t['n'] for t in v]); eq=np.cumsum(x); dd=(np.maximum.accumulate(np.r_[0,eq])[1:]-eq).max()
        L2.append('| %s — %s | %d | %s | %+.0f | %+.0f | %.0f |'%(name,lb,len(v),' | '.join('%+.0f'%sum(t['n'] for t in v if t['th']==k) for k in range(3)),sum(t['n'] for t in v if t['l4']),x.sum(),dd))
L2+=['','Bot input ("Entry windows", candle close ET) for the proposal: `1830-2200, 0300-0330, 0400-0600, 0630-0730, 0800-1300, 1400-1554`']
open('slot30_report.md','a').write('\n'.join(L2)+'\n'); print('\n'.join(L2))
