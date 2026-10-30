import json,datetime as D,sys
from zoneinfo import ZoneInfo
TZ=ZoneInfo('America/New_York')
P={('MGC',3):dict(sl=1.3,mn=0,tp=2.0,part=.5,be=False,ts=10,R5=True,X4=True,cap=7),
   ('MES',3):dict(sl=1.3,mn=0,tp=2.0,part=.8,be=False,ts=0,R5=True,X4=False,cap=8),
   ('MGC',2):dict(sl=1.7,mn=5,tp=1.7,part=.8,be=True,ts=0,R5=False,X4=False,cap=7),
   ('MES',2):dict(sl=1.7,mn=5,tp=1.7,part=.8,be=True,ts=0,R5=False,X4=False,cap=8)}
def ema(x,n):
    k=2/(n+1);o=[];e=None
    for v in x: e=v if e is None else e+k*(v-e); o.append(e)
    return o
def run(sym,tf):
    p=P[(sym,tf)]; key=sym if tf==3 else f'{sym}_{tf}'
    B=json.load(open(f'bars/{key}.json'))['bars']
    n=len(B); T=[b['t'] for b in B];O=[b['o'] for b in B];H=[b['h'] for b in B];L=[b['l'] for b in B];C=[b['c'] for b in B]
    VW=[b.get('vw') for b in B]; E200=[b.get('e200') for b in B]
    E9=ema(C,9);E20=ema(C,20)
    atr=[];a=None
    for i in range(n):
        tr=H[i]-L[i] if i==0 else max(H[i],C[i-1])-min(L[i],C[i-1]); a=tr if a is None else (a*13+tr)/14; atr.append(a)
    HT=tf*5*60000
    # HTF aggregation; closing chart bar index per HTF bar
    hb=[];cur=None
    for i in range(n):
        k=T[i]//HT
        if cur is None or cur['k']!=k:
            if cur: hb.append(cur)
            cur=dict(k=k,o=O[i],h=H[i],l=L[i],c=C[i],last=i,cnt=1)
        else:
            cur['h']=max(cur['h'],H[i]);cur['l']=min(cur['l'],L[i]);cur['c']=C[i];cur['last']=i;cur['cnt']+=1
    hb.append(cur)
    # HTF CBC + pivots N=1 + structure, events keyed by closing chart bar
    st=False; hdir=[None]*n; hflip=[0]*n
    hs={'hi':'—','lo':'—'}; last_hi=last_lo=None
    Hstr=[None]*n
    ev={}
    for k in range(len(hb)):
        x=hb[k]
        if k>0:
            pv=hb[k-1]
            ns=st
            if st and x['c']<pv['l']: ns=False
            if not st and x['c']>pv['h']: ns=True
            ev.setdefault(x['last'],{})['flip']=(1 if ns else -1) if ns!=st else 0
            st=ns
        ev.setdefault(x['last'],{})['dir']=st
        if k>=2:
            m=hb[k-1]
            if m['h']>hb[k-2]['h'] and m['h']>x['h']:
                if last_hi is not None: hs['hi']='HH' if m['h']>last_hi else 'LH'
                last_hi=m['h']
            if m['l']<hb[k-2]['l'] and m['l']<x['l']:
                if last_lo is not None: hs['lo']='LL' if m['l']<last_lo else 'HL'
                last_lo=m['l']
        ev[x['last']]['hs']=(hs['hi'],hs['lo'])
    d=None;s=('—','—');warm=0
    for i in range(n):
        e=ev.get(i)
        if e:
            if 'flip' in e and e['flip']: hflip[i]=e['flip']
            d=e['dir']; s=e['hs']; warm+=1
        hdir[i]=d if warm>25 else None; Hstr[i]=s
    # LTF pivots N=2
    ls={'hi':'—','lo':'—'}; lh=ll=None; Lstr=[None]*n
    for i in range(n):
        j=i-2
        if j>=2:
            if H[j]>max(H[j-2],H[j-1]) and H[j]>=max(H[j+1],H[j+2]) and H[j]>H[j+1] or (H[j]>max(H[j-2],H[j-1]) and H[j]>max(H[j+1],H[j+2])):
                if lh is not None: ls['hi']='HH' if H[j]>lh else 'LH'
                lh=H[j]
            if L[j]<min(L[j-2],L[j-1]) and L[j]<min(L[j+1],L[j+2]):
                if ll is not None: ls['lo']='LL' if L[j]<ll else 'HL'
                ll=L[j]
        Lstr[i]=(ls['hi'],ls['lo'])
    def er(i,k=12):
        dd=sum(abs(C[j]-C[j-1]) for j in range(i-k+1,i+1)); return abs(C[i]-C[i-k])/dd if dd else 0
    def nyhm(i):
        t=D.datetime.fromtimestamp((T[i]+tf*60000)/1000,TZ); return t.hour*60+t.minute,t
    trades=[]; busy_until=-1; last_setup=-999
    def sim(i,lg):
        en=C[i]; A=atr[i]; sgn=1 if lg else -1
        s=max(p['sl']*A,p['mn']); s=min(s,p['cap']); tpd=min(p['tp']*A,6)
        sl=en-sgn*s; t1=en+sgn*tpd; hit=False; best=0
        for j in range(i+1,n):
            if hflip[j]==-sgn and not hit or hflip[j]==-sgn:
                pass
            if (L[j]<=sl if lg else H[j]>=sl):
                rem=sgn*(sl-en); return (p['part']*tpd+(1-p['part'])*rem if hit else rem),j,'SL' if not hit else 'Trail'
            if not hit and (H[j]>=t1 if lg else L[j]<=t1):
                hit=True
                if p['be']: sl=max(sl,en) if lg else min(sl,en)
            best=max(best,sgn*((H[j] if lg else L[j])-en))
            if hit:
                nsl=C[j]-1.7*atr[j] if lg else C[j]+1.7*atr[j]; sl=max(sl,nsl) if lg else min(sl,nsl)
            hm,_=nyhm(j)
            ex=None
            if hflip[j]==-sgn: ex='Flip'
            elif hm==16*60: ex='16:00'
            elif p['ts'] and not hit and j-i==p['ts'] and best<0.5*A: ex='Time'
            if ex:
                rem=sgn*(C[j]-en); return (p['part']*tpd+(1-p['part'])*rem if hit else rem),j,ex
        return None
    for i in range(60,n-1):
        if i<=busy_until: 
            if not hflip[i]: continue
        dirn=hdir[i]
        if dirn is None: continue
        hm,tt=nyhm(i)
        if 16*60<=hm<18*60+45: continue
        lg=None; trig=None
        if hflip[i]:
            lg=hflip[i]==1; trig='flip'
            side=(C[i]>max(VW[i] or C[i],E200[i] or C[i])+1) if lg else (C[i]<min(VW[i] or C[i],E200[i] or C[i])-1)
            if not side or er(i)<0.23: continue
        else:
            if i-last_setup<10 or i<=busy_until: continue
            if dirn and L[i-1]>E20[i-1] and L[i]<=E20[i] and C[i]>E20[i]: lg=True
            elif (not dirn) and H[i-1]<E20[i-1] and H[i]>=E20[i] and C[i]<E20[i]: lg=False
            else: continue
            trig='ltf20'
            if er(i)<0.08: continue
        # gates
        A=atr[i]
        if p['R5']:
            w=range(i-23,i+1); hi=max(H[j] for j in w); lo=min(L[j] for j in w)
            pos=(C[i]-lo)/(hi-lo) if hi>lo else .5
            if (pos if lg else 1-pos)>=.8 and (hi-lo)/A<5: continue
        if p['X4'] and VW[i] and ((C[i]-VW[i]) if lg else (VW[i]-C[i]))/A>4: continue
        r=sim(i,lg)
        if not r: continue
        res,j,why=r
        trades.append(dict(t=tt.isoformat(),lg=lg,trig=trig,res=res,why=why,L=Lstr[i],H=Hstr[i]))
        busy_until=j; last_setup=i
    return trades
def cls(s,lg):
    h,l=s
    w=('HH','HL') if lg else ('LH','LL'); a=('LH','LL') if lg else ('HH','HL')
    return 'with' if (h,l)==w else 'against' if (h,l)==a else 'mixed'
def comp(s,lg):  # low-side for long: HL good; high-side for short: LH good
    h,l=s
    return ('pullback-side OK' if (l=='HL' if lg else h=='LH') else 'pullback-side broken')
def S(g):
    if not g: return '   0              '
    return f"{len(g):4d} {round(100*sum(o['res']>0 for o in g)/len(g)):3d}% {sum(o['res'] for o in g):+7.1f} ({sum(o['res'] for o in g)/len(g):+.2f})"
out={}
for sym,tf in [('MGC',3),('MGC',2),('MES',3),('MES',2)]:
    tr=run(sym,tf); out[f'{sym} {tf}m']=tr
    for o in tr:
        o['Lc']=cls(o['L'],o['lg']); o['Hc']=cls(o['H'],o['lg']); o['Lp']=comp(o['L'],o['lg']); o['Hp']=comp(o['H'],o['lg'])
    h=len(tr)//2
    print(f"\n== {sym} {tf}m replay: {S(tr)}  {tr[0]['t'][:10]}..{tr[-1]['t'][:10]}  (flip {len([o for o in tr if o['trig']=='flip'])}, LTF20 {len([o for o in tr if o['trig']=='ltf20'])})")
    for k,vals in (('Lc',('with','mixed','against')),('Hc',('with','mixed','against')),('Lp',('pullback-side OK','pullback-side broken')),('Hp',('pullback-side OK','pullback-side broken'))):
        for v in vals:
            print(f"  {k} {v:21s} {S([o for o in tr if o[k]==v])} | h1 {S([o for o in tr[:h] if o[k]==v])} | h2 {S([o for o in tr[h:] if o[k]==v])}")
json.dump(out,open('struct_replay_out.json','w'))
