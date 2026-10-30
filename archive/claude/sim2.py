import json,datetime as D,itertools,sys
from zoneinfo import ZoneInfo
TZ=ZoneInfo('America/New_York')
BASE={('MGC',3):dict(sl=1.3,mn=0,tp=2.0,part=.5,be=False,ts=10,tr=1.7,R5=True,X4=True,cap=7),
   ('MES',3):dict(sl=1.3,mn=0,tp=2.0,part=.8,be=False,ts=0,tr=1.7,R5=True,X4=False,cap=8),
   ('MGC',2):dict(sl=1.7,mn=5,tp=1.7,part=.8,be=True,ts=0,tr=1.7,R5=False,X4=False,cap=7),
   ('MES',2):dict(sl=1.7,mn=5,tp=1.7,part=.8,be=True,ts=0,tr=1.7,R5=False,X4=False,cap=8)}
def ema(x,n):
    k=2/(n+1);o=[];e=None
    for v in x: e=v if e is None else e+k*(v-e); o.append(e)
    return o
class Case:
    def __init__(s,sym,tf):
        s.sym,s.tf=sym,tf; s.p=BASE[(sym,tf)]; key=sym if tf==3 else f'{sym}_{tf}'
        B=json.load(open(f'bars/{key}.json'))['bars']; n=s.n=len(B)
        s.T=[b['t'] for b in B];s.O=[b['o'] for b in B];s.H=[b['h'] for b in B];s.L=[b['l'] for b in B];s.C=[b['c'] for b in B]
        s.VW=[b.get('vw') for b in B];s.E200=[b.get('e200') for b in B]
        s.E9=ema(s.C,9);s.E20=ema(s.C,20)
        atr=[];a=None
        for i in range(n):
            tr=s.H[i]-s.L[i] if i==0 else max(s.H[i],s.C[i-1])-min(s.L[i],s.C[i-1]); a=tr if a is None else (a*13+tr)/14; atr.append(a)
        s.atr=atr
        HT=tf*5*60000; hb=[];cur=None
        for i in range(n):
            k=s.T[i]//HT
            if cur is None or cur['k']!=k:
                if cur: hb.append(cur)
                cur=dict(k=k,o=s.O[i],h=s.H[i],l=s.L[i],c=s.C[i],last=i)
            else: cur['h']=max(cur['h'],s.H[i]);cur['l']=min(cur['l'],s.L[i]);cur['c']=s.C[i];cur['last']=i
        hb.append(cur)
        he20=ema([x['c'] for x in hb],20)
        st=False; s.hdir=[None]*n; s.hflip=[0]*n; s.hstr=[None]*n; s.he20=[None]*n; s.age=[None]*n
        hs=['—','—']; lhi=llo=None; ev={}
        for k,x in enumerate(hb):
            e=ev.setdefault(x['last'],{})
            if k>0:
                pv=hb[k-1]; ns=st
                if st and x['c']<pv['l']: ns=False
                if not st and x['c']>pv['h']: ns=True
                e['flip']=(1 if ns else -1) if ns!=st else 0; st=ns
            e['dir']=st; e['e20']=he20[k]
            if k>=2:
                m=hb[k-1]
                if m['h']>hb[k-2]['h'] and m['h']>x['h']:
                    if lhi is not None: hs[0]='HH' if m['h']>lhi else 'LH'
                    lhi=m['h']
                if m['l']<hb[k-2]['l'] and m['l']<x['l']:
                    if llo is not None: hs[1]='LL' if m['l']<llo else 'HL'
                    llo=m['l']
            e['hs']=tuple(hs)
        d=None;sv=('—','—');w=0;e20v=None;lastflip=None
        for i in range(n):
            e=ev.get(i)
            if e:
                if e.get('flip'): s.hflip[i]=e['flip']; lastflip=i
                d=e['dir'];sv=e['hs'];e20v=e['e20'];w+=1
            s.hdir[i]=d if w>25 else None; s.hstr[i]=sv; s.he20[i]=e20v; s.age[i]=None if lastflip is None else i-lastflip
        s.setups=s.gen()
    def nyhm(s,i):
        t=D.datetime.fromtimestamp((s.T[i]+s.tf*60000)/1000,TZ); return t.hour*60+t.minute,t
    def er(s,i,k=12):
        C=s.C; dd=sum(abs(C[j]-C[j-1]) for j in range(i-k+1,i+1)); return abs(C[i]-C[i-k])/dd if dd else 0
    def feat(s,i,lg):
        C,H,L,O=s.C,s.H,s.L,s.O; A=s.atr[i]; g=1 if lg else -1
        hm,t=s.nyhm(i)
        sess='Asia' if (hm>=18*60 or hm<3*60) else 'London' if hm<9*60+30 else 'NY'
        rng=H[i]-L[i]
        a100=sum(s.atr[i-99:i+1])/100
        hs=s.hstr[i]
        return dict(sess=sess,hour=t.hour,age=s.age[i],
            h20d=g*(C[i]-s.he20[i])/A, e20d=g*(C[i]-s.E20[i])/A,
            vwd=g*(C[i]-s.VW[i])/A if s.VW[i] else 0, e200d=g*(C[i]-s.E200[i])/A if s.E200[i] else 0,
            cloud=(s.E9[i]>s.E20[i])==lg, body=g*(C[i]-O[i])/A, clpos=((C[i]-L[i])/rng if lg else (H[i]-C[i])/rng) if rng else .5,
            atrrel=A/a100, er=s.er(i), rngA=rng/A,
            hpb=(hs[1]=='HL') if lg else (hs[0]=='LH'),
            mom3=g*(C[i]-C[i-3])/A, mom12=g*(C[i]-C[i-12])/A)
    def gen(s):
        p=s.p; C,H,L=s.C,s.H,s.L; out=[]; last=-999
        for i in range(110,s.n-1):
            dirn=s.hdir[i]
            if dirn is None or s.he20[i] is None: continue
            hm,tt=s.nyhm(i)
            if 16*60<=hm<18*60+45: continue
            if s.hflip[i]:
                lg=s.hflip[i]==1; trig='flip'
                vw=s.VW[i] or C[i]; e2=s.E200[i] or C[i]
                if not ((C[i]>max(vw,e2)+1) if lg else (C[i]<min(vw,e2)-1)) or s.er(i)<0.23: continue
            else:
                if i-last<10: continue
                E20=s.E20
                if dirn and L[i-1]>E20[i-1] and L[i]<=E20[i] and C[i]>E20[i]: lg=True
                elif (not dirn) and H[i-1]<E20[i-1] and H[i]>=E20[i] and C[i]<E20[i]: lg=False
                else: continue
                trig='ltf20'
                if s.er(i)<0.08: continue
            A=s.atr[i]
            if p['R5']:
                hi=max(H[i-23:i+1]); lo=min(L[i-23:i+1]); pos=(C[i]-lo)/(hi-lo) if hi>lo else .5
                if (pos if lg else 1-pos)>=.8 and (hi-lo)/A<5: continue
            if p['X4'] and s.VW[i] and ((C[i]-s.VW[i]) if lg else (s.VW[i]-C[i]))/A>4: continue
            out.append(dict(i=i,lg=lg,trig=trig,t=tt,f=s.feat(i,lg))); last=i
        return out
    def sim(s,i,lg,q):
        C,H,L=s.C,s.H,s.L; en=C[i]; A=s.atr[i]; g=1 if lg else -1
        sd=min(max(q['sl']*A,q['mn']),q['cap']); tpd=min(q['tp']*A,q.get('tpcap',6))
        sl=en-g*sd; t1=en+g*tpd; hit=False; best=0
        for j in range(i+1,s.n):
            if (L[j]<=sl if lg else H[j]>=sl):
                rem=g*(sl-en); return (q['part']*tpd+(1-q['part'])*rem if hit else rem),j
            if not hit and (H[j]>=t1 if lg else L[j]<=t1):
                hit=True
                if q['be']: sl=max(sl,en) if lg else min(sl,en)
                if q['part']>=1: return tpd,j
            best=max(best,g*((H[j] if lg else L[j])-en))
            if hit:
                ns=C[j]-g*q['tr']*s.atr[j]; sl=max(sl,ns) if lg else min(sl,ns)
            hm,_=s.nyhm(j)
            if s.hflip[j]==-g or hm==16*60 or (q['ts'] and not hit and j-i==q['ts'] and best<0.5*A):
                rem=g*(C[j]-en); return (q['part']*tpd+(1-q['part'])*rem if hit else rem),j
        return None
    def run(s,q=None,keep=lambda st:True):
        q=q or s.p; res=[]; busy=-1
        for st in s.setups:
            if st['i']<=busy and st['trig']!='flip': continue
            if not keep(st): continue
            r=s.sim(st['i'],st['lg'],q)
            if r is None: continue
            res.append(dict(st,res=r[0])); busy=r[1]
        return res
