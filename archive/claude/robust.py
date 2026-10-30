from sim2 import Case
def tot(r): return sum(o['res'] for o in r)
def thirds(c,r,base):
    ts=sorted(o['t'] for o in base); a,b=ts[len(ts)//3],ts[2*len(ts)//3]
    f=lambda rr:[tot([o for o in rr if o['t']<a]),tot([o for o in rr if a<=o['t']<b]),tot([o for o in rr if o['t']>=b])]
    return [x-y for x,y in zip(f(r),f(base))]
def show(c,name,q=None,keep=lambda st:True):
    base=c.run(); r=c.run(q,keep)
    t=thirds(c,r,base); w=sum(o['res']>0 for o in r)
    print(f"  {name:52s} n {len(r):3d} (base {len(base)}) win {100*w/len(r):3.0f}% net {tot(r):+7.1f} (base {tot(base):+.1f}) per {tot(r)/len(r):+.2f}  gain by thirds {t[0]:+5.1f} {t[1]:+5.1f} {t[2]:+5.1f}")
c=Case('MGC',3); print('MGC 3m')
for x in (0,0.1,0.2,0.3,0.4): show(c,f'require setup candle body >= {x} ATR',keep=lambda st,x=x: st['f']['body']>=x)
show(c,'skip London (03:00-09:30 ET)',keep=lambda st: st['f']['sess']!='London')
for sl,tp in ((1.3,1.5),(1.3,2.0),(1.7,1.5),(1.7,2.0),(2.0,1.5)):
    show(c,f'exit 100% at TP1 {tp} ATR, SL {sl}',dict(c.p,sl=sl,tp=tp,part=1.0))
show(c,'body>=0.2 + 100% at TP1 1.5, SL 1.7',dict(c.p,sl=1.7,tp=1.5,part=1.0),lambda st: st['f']['body']>=0.2)
for x in (0.1,0.15,0.2,0.25): show(c,f'ER min {x} (all triggers)',keep=lambda st,x=x: st['f']['er']>=x)
c=Case('MES',2); print('MES 2m')
for x in (0.12,0.15,0.18,0.2,0.23,0.26): show(c,f'ER min {x} (all triggers)',keep=lambda st,x=x: st['f']['er']>=x)
for sl,tp in ((1.0,2.0),(1.0,2.5),(1.0,3.0),(1.3,2.5),(1.3,3.0),(1.7,3.0)):
    show(c,f'exit 100% at TP1 {tp} ATR, SL {sl} (no min 5)',dict(c.p,sl=sl,tp=tp,part=1.0,mn=0,tpcap=99))
show(c,'exit SL 1.0 TP1 3.0 100% WITH TP cap 6',dict(c.p,sl=1.0,tp=3.0,part=1.0,mn=0))
show(c,'ER 0.2 + SL 1.0 TP1 3.0 100%',dict(c.p,sl=1.0,tp=3.0,part=1.0,mn=0,tpcap=99),lambda st: st['f']['er']>=0.2)
for x in (0,0.1,0.2,0.3): show(c,f'require body >= {x}',keep=lambda st,x=x: st['f']['body']>=x)
c=Case('MGC',2); print('MGC 2m')
for x in (0.15,0.2,0.23): show(c,f'ER min {x}',keep=lambda st,x=x: st['f']['er']>=x)
for x in (0,0.2): show(c,f'require body >= {x}',keep=lambda st,x=x: st['f']['body']>=x)
show(c,'skip flips when ATR > 1.0x its 100-bar avg',keep=lambda st: not(st['trig']=='flip' and st['f']['atrrel']>1.0))
c=Case('MES',3); print('MES 3m')
for x in (0.15,0.2): show(c,f'ER min {x}',keep=lambda st,x=x: st['f']['er']>=x)
for x in (0,0.2): show(c,f'require body >= {x}',keep=lambda st,x=x: st['f']['body']>=x)
show(c,'skip London',keep=lambda st: st['f']['sess']!='London')
show(c,'SL 1.7 trail 2.5',dict(c.p,sl=1.7,tr=2.5))
