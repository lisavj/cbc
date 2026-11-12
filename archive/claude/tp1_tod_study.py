import sys, datetime as D
import mes_sltp_grid as g
g.SYM=sys.argv[1] if len(sys.argv)>1 else 'MES'
B,atr,T=g.load()
def sim(tr,sk,tm,part,trail,be,minsl=5):
    i,lg,en=tr['i'],tr['lg'],tr['en']; s=1 if lg else -1
    sd=max(sk*atr[i],minsl); td=tm*atr[i]; sl=en-s*sd; tp1=en+s*td; hit=False
    def fin(px):
        rem=(px-en)*s; return part*td+(1-part)*rem if hit else rem
    for j in range(i+1,min(len(B),i+500)):
        x=B[j]; hi,lo,c=x['h'],x['l'],x['c']
        if (lo<=sl) if lg else (hi>=sl): return fin(sl)
        if not hit and ((hi>=tp1) if lg else (lo<=tp1)):
            hit=True
            if part>=1: return td
            if be: sl=max(sl,en) if lg else min(sl,en)
        if hit and trail:
            ns=c-trail*atr[j] if lg else c+trail*atr[j]; sl=max(sl,ns) if lg else min(sl,ns)
        hc,hp=x['hc'],B[j-1]['hc']
        if hc is not None and hp is not None and hc!=hp and ((lg and hc==0) or (not lg and hc==1)): return fin(c)
        t=D.datetime.fromtimestamp(x['t']/1000,g.TZ)
        if t.hour==15 and t.minute>=57: return fin(c)
    return 0.0
def inwin(tr):
    t=tr['t']-D.timedelta(minutes=3); m=t.hour*60+t.minute
    return 360<=m<960 or 1080<=m<1350
n=len(T);h=n//2;t3=n//3
def stats(R):
    th=[sum(R[k*t3:(k+1)*t3 if k<2 else n]) for k in range(3)]
    live=[r for r,t in zip(R,T) if t['t']>=D.datetime(2026,10,27,tzinfo=g.TZ)]
    return '%+7.1f | %+6.1f / %+6.1f | %s | %s | %+6.1f' % (sum(R),sum(R[:h]),sum(R[h:]),' '.join('%+6.1f'%x for x in th),'✱T' if all(x>0 for x in th) and sum(R[:h])>0 and sum(R[h:])>0 else '  ',sum(live))
W=[inwin(t) for t in T]
print('%s 3m: %d setups (%s-%s), %d inside 06-16/18-22:30, %d outside'%(g.SYM,n,T[0]['t'].strftime('%m/%d'),T[-1]['t'].strftime('%m/%d'),sum(W),n-sum(W)))
print('variant (stop 3.0 / TP1 1.75 ATR, min 5)          | net | halves | thirds | | since 10/27')
P100=[sim(t,3,1.75,1.0,None,False) for t in T]
P80=[sim(t,3,1.75,.8,1.7,True) for t in T]
P80n=[sim(t,3,1.75,.8,1.7,False) for t in T]
P8013=[sim(t,3,1.75,.8,1.3,True) for t in T]
P8013n=[sim(t,3,1.75,.8,1.3,False) for t in T]
rows=[('100% all day',P100),('80% all day, trail 1.7 + BE',P80),('80% all day, trail 1.7 no BE',P80n),('80% all day, trail 1.3 + BE',P8013),
('TIME MIX (box): 80% in windows (tr1.7+BE), else 100%',[b if w else a for a,b,w in zip(P100,P80,W)]),
('time mix, 80% trail 1.3 + BE',[b if w else a for a,b,w in zip(P100,P8013,W)]),
('reverse mix: 100% in windows, 80% outside',[a if w else b for a,b,w in zip(P100,P80,W)])]
for nm,R in rows: print('%-52s %s'%(nm,stats(R)))
print()
for lab,sel in (('inside windows',True),('outside windows',False)):
    idx=[k for k in range(n) if W[k]==sel]
    print('%-16s n=%2d  100%%: %+6.1f   80%% tr1.7+BE: %+6.1f   80%% tr1.3+BE: %+6.1f'%(lab,len(idx),sum(P100[k] for k in idx),sum(P80[k] for k in idx),sum(P8013[k] for k in idx)))
# by hour bucket
import collections
bk=collections.defaultdict(lambda:[0,0,0])
for k,t in enumerate(T):
    hh=(t['t']-D.timedelta(minutes=3)).hour
    b='00-06' if hh<6 else '06-09:30' if (hh,0)<(9,30) and hh<10 and (hh<9 or (t['t']-D.timedelta(minutes=3)).minute<30) else '09:30-12' if hh<12 else '12-16' if hh<16 else '18-22:30' if hh<22 or (hh==22 and (t['t']-D.timedelta(minutes=3)).minute<30) else '22:30-24'
    bk[b][0]+=1; bk[b][1]+=P100[k]; bk[b][2]+=P80[k]
for b in ['00-06','06-09:30','09:30-12','12-16','18-22:30','22:30-24']:
    if b in bk: print('%-9s n=%2d  100%%: %+6.1f  80%%: %+6.1f  diff %+5.1f'%(b,bk[b][0],bk[b][1],bk[b][2],bk[b][2]-bk[b][1]))
