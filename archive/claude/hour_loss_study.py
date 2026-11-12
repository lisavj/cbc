import sys, datetime as D, collections
import mes_sltp_grid as g
sym=sys.argv[1]; g.SYM=sym
B,atr,T=g.load()
if sym=='MES': SK,TM,TCAP,PART=3.0,1.75,None,1.0
else: SK,TM,TCAP,PART=1.7,1.7,6,0.8
def sim(tr):
    i,lg,en=tr['i'],tr['lg'],tr['en']; s=1 if lg else -1
    sd=max(SK*atr[i],5); td=TM*atr[i]
    if TCAP: td=min(td,TCAP)
    sl=en-s*sd; tp1=en+s*td; hit=False
    def fin(px):
        rem=(px-en)*s; return PART*td+(1-PART)*rem if hit else rem
    for j in range(i+1,min(len(B),i+500)):
        x=B[j]; hi,lo,c=x['h'],x['l'],x['c']
        if (lo<=sl) if lg else (hi>=sl): return fin(sl)
        if not hit and ((hi>=tp1) if lg else (lo<=tp1)):
            hit=True
            if PART>=1: return td
            sl=max(sl,en) if lg else min(sl,en)
        if hit:
            ns=c-1.7*atr[j] if lg else c+1.7*atr[j]; sl=max(sl,ns) if lg else min(sl,ns)
        hc,hp=x['hc'],B[j-1]['hc']
        if hc is not None and hp is not None and hc!=hp and ((lg and hc==0) or (not lg and hc==1)): return fin(c)
        t=D.datetime.fromtimestamp(x['t']/1000,g.TZ)
        if t.hour==15 and t.minute>=57: return fin(c)
    return 0.0
n=len(T); h=n//2
H=collections.defaultdict(list)
for k,t in enumerate(T):
    hr=(t['t']-D.timedelta(minutes=3)).hour
    H[hr].append((k<h,t['act'],sim(t)))
print('%s 3m: %d setups %s-%s. Loser = result < 0. "sim" = replay with current exits (%s).'%(sym,n,T[0]['t'].strftime('%m/%d'),T[-1]['t'].strftime('%m/%d'),'stop 3.0 / TP1 1.75 ATR, 100%%' if sym=='MES' else 'base: 1.7/1.7 ATR cap 6, 80%%, BE'))
print('hour ET | n  | actual: loss%%  net  | 1st half loss%% (n) | 2nd half loss%% (n) | sim: loss%%  net')
for hr in sorted(H):
    L=H[hr]; a=[x[1] for x in L]; s=[x[2] for x in L]
    f=[x[1] for x in L if x[0]]; b=[x[1] for x in L if not x[0]]
    pc=lambda v: '%3.0f%%'%(100*sum(r<0 for r in v)/len(v)) if v else '  - '
    flag=' <<' if sum(r<0 for r in a)/len(a)>0.5 else ''
    print('%02d-%02d   | %2d | %s %+6.1f | %s (%2d) | %s (%2d) | %s %+6.1f%s'%(hr,hr+1,len(L),pc(a),sum(a),pc(f),len(f),pc(b),len(b),pc(s),sum(s),flag))
a=[t['act'] for t in T]; print('all     | %2d | %3.0f%% %+6.1f'%(n,100*sum(r<0 for r in a)/n,sum(a)))
