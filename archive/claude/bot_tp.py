"""MES 3m BOT exits: the bot closes its whole position at TP1 (bracket), so test TP rules with 100 % at TP1 -- 11/08/2026.
Bot setups only: 5-day short filter, proposed entry windows (1830-2200, 0300-0330, 0400-0600, 0630-0730, 0800-1300, 1400-1545),
net after costs (0.50 per trade, +0.25 for a rule exit at market)."""
import numpy as np, pandas as pd, combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg, mes3_ema_grid as m
class BCase(cb.CCase):
    AX = 0.0
    def sim1(s, i, lg, q, stop_at):
        tx = s.TX
        if s.AX > 0 and not (s.atrrel[i] >= s.AX): s.TX = 0
        try: return cb.CCase.sim1(s, i, lg, q, stop_at)
        finally: s.TX = tx
sym='MES'; B=ls.load(sym,3); ls.LCase.LATE=1; ls.LCase.NYW=30; s=BCase(sym,3,B); TR,ss=tg.trend_arrays(s); G=cb.CH[sym][2]
et=pd.to_datetime(s.B.t,unit='ms',utc=True).dt.tz_convert('America/New_York'); mm=(et.dt.hour*60+et.dt.minute).values; cm=(mm+3)%1440
W=[(1110,1320),(180,210),(240,360),(390,450),(480,780),(840,945)]
win=lambda i: any(a<=cm[i]<=b for a,b in W)
T0,T1=s.T[300],s.T[-1]; cuts=[T0+(T1-T0)*k/3 for k in (1,2)]; t4=T1-28*86400000
def run(q, tp=(0,0.0), ax=0.0):
    def ok(d):
        if not cs.cur_rule(d) or not win(d['i']): return False
        if d['lg']: return True
        v=TR['d5'][d['i']]; return v==0 or v==-1
    s.TX,s.TY=tp; s.AX=ax; s.ACT,s.SY,s.SX=(None,0.0,0)
    return [dict(n=t['res']-.5-(.25 if t['why']=='cut' else 0),why=t['why'],th=0 if s.T[t['i']]<cuts[0] else 1 if s.T[t['i']]<cuts[1] else 2,l4=bool(s.T[t['i']]>=t4)) for t in s.run(ok,q=q,gates=G)]
BOTQ=dict(m.LIVE, part=1.0)
rows=[('CBC chart exits (80/100 % by time + runner) — for reference', run(m.LIVE)),
      ('BOT now: 100 % at TP1 1.75 ATR, no exit rule', run(BOTQ)),
      ('Bot + current exit rule (21 min -> 70 %, only ATR >= 1.5x avg), flatten ON', run(BOTQ,(21,.70),1.5))]
for x in (12,15,18,21,24):
    for y in (.75,.85):
        rows.append(('Bot + TP1 -> %d %% after %d min (all trades)'%(round(y*100),x), run(BOTQ,(x,y))))
for tp in (1.25,1.5,2.0,2.5):
    rows.append(('Bot, TP1 %.2f ATR (no rule)'%tp, run(dict(BOTQ,tp=tp))))
b=rows[1][1]
L=[__doc__,'','| Bot exits | Trades | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Win % | Max DD | vs bot now: thirds |','|---|---|---|---|---|---|---|---|---|---|']
for lab,v in rows:
    th=[sum(t['n'] for t in v if t['th']==k) for k in range(3)]; bt=[sum(t['n'] for t in b if t['th']==k) for k in range(3)]
    x=np.array([t['n'] for t in v]); eq=np.cumsum(x); dd=(np.maximum.accumulate(np.r_[0,eq])[1:]-eq).max()
    d=[a-c for a,c in zip(th,bt)]
    L.append('| %s | %d | %+.0f | %+.0f | %+.0f | %+.0f | %+.0f | %d %% | %.0f | %s %s |'%(lab,len(v),*th,sum(t['n'] for t in v if t['l4']),x.sum(),round(100*(x>0).mean()),dd,' / '.join('%+.0f'%a for a in d),'T' if all(a>0 for a in d) else ''))
open('bot_tp_report.md','w').write('\n'.join(L)); print('\n'.join(L))
