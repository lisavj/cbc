"""Chop-filter simulator on the Databento-rebuilt bars (Jan-Oct 2026). Approximates CBC v10.35 setup engine:
triggers HTF CBC Flip (side gate + VWAP slope + flip ER min), LTF EMA20 Pierce (+1-bar late), HTF EMA9 / EMA20 Pierce
(+1-bar late); cooldown 10 bars (flip / opposite direction bypass); a new setup ends the open one at its close;
R5 range gate on 3m, X4 stretch on MGC 3m, 1H MTF gate on MES 2m; exits per case (v10.31 defaults)."""
import pickle, numpy as np, pandas as pd
EXIT = {('MGC',3):dict(sl=1.3,mn=0,tp=2.0,part=.5,be=False,ts=10,tr=1.7,cap=7),
        ('MES',3):dict(sl=1.3,mn=0,tp=2.0,part=.8,be=False,ts=0,tr=1.7,cap=8),
        ('MGC',2):dict(sl=1.7,mn=5,tp=1.7,part=.8,be=True,ts=0,tr=1.7,cap=7),
        ('MES',2):dict(sl=1.7,mn=5,tp=1.7,part=.8,be=True,ts=0,tr=1.7,cap=8)}
GATE = {('MGC',3):dict(R5=1,X4=1,MTF=0),('MES',3):dict(R5=1,X4=0,MTF=0),('MGC',2):dict(R5=0,X4=0,MTF=0),('MES',2):dict(R5=0,X4=0,MTF=1)}

def rma(x,n):
    o=np.full(len(x),np.nan); s=np.nan
    for i,v in enumerate(x):
        if np.isnan(v): continue
        s=v if np.isnan(s) else (s*(n-1)+v)/n; o[i]=s
    return o
def roll_sum(x,n): c=np.concatenate([[0],np.cumsum(x)]); o=np.full(len(x),np.nan); o[n-1:]=c[n:]-c[:-n]; return o

class Case:
    def __init__(s, sym, tf, B):
        s.sym,s.tf=sym,tf; B=B.reset_index(drop=True); s.B=B; n=s.n=len(B)
        O,H,L,C=[B[k].values.astype(float) for k in 'ohlc']; s.O,s.H,s.L,s.C=O,H,L,C
        s.T=B.t.values; s.e20=B.e20.values; s.vw=B.vw.values; s.e200=B.e200.values
        # HTF EMA9/20 as seen LIVE (forming HTF candle uses the current chart close; no look-ahead)
        hkey=B.hk.values; newb=np.r_[True,hkey[1:]!=hkey[:-1]]
        for nm,n_ in (('h9',9),('h20',20)):
            fin=B[nm].values; prevfin=np.full(len(B),np.nan); pf=np.nan
            for i in range(len(B)):
                if newb[i] and i>0: pf=fin[i-1]
                prevfin[i]=pf
            k_=2/(n_+1); setattr(s,nm,np.where(np.isnan(prevfin),fin,prevfin+k_*(B.c.values-prevfin)))
        pc=np.r_[C[0],C[:-1]]; tr=np.maximum(H,pc)-np.minimum(L,pc); s.atr=rma(tr,14)
        et=pd.to_datetime(B.t,unit='ms',utc=True).dt.tz_convert('America/New_York')
        s.hm=((et.dt.hour*60+et.dt.minute).values+tf)%1440  # candle CLOSE time-of-day
        s.month=et.dt.month.values; s.date=et.dt.strftime('%m/%d %H:%M').values
        hc=B.hc.values; s.hdir=np.where(np.isnan(hc),-1,hc).astype(int)  # 1 bull 0 bear -1 unknown
        s.hf=B.hf.values.astype(int)
        # features
        d=np.abs(np.diff(C,prepend=C[0]))
        s.er={}
        for k in (6,8,10,12,16,20,30):
            den=roll_sum(d,k); num=np.abs(C-np.r_[np.full(k,np.nan),C[:-k]]); s.er[k]=np.where(den>0,num/den,0)
        k=12
        hh=pd.Series(H).rolling(k).max().values; ll=pd.Series(L).rolling(k).min().values
        s.rng=(hh-ll)/s.atr
        s.chop=100*np.log10(roll_sum(tr,k)/(hh-ll))/np.log10(k)
        up=H-np.r_[H[0],H[:-1]]; dn=np.r_[L[0],L[:-1]]-L
        pdm=np.where((up>dn)&(up>0),up,0.); mdm=np.where((dn>up)&(dn>0),dn,0.)
        trr=rma(tr,k); pdi=100*rma(pdm,k)/trr; mdi=100*rma(mdm,k)/trr
        dx=100*np.abs(pdi-mdi)/np.where(pdi+mdi>0,pdi+mdi,1); s.adx=rma(dx,k)
        xe=(C>s.e20)!=(np.r_[C[0],C[:-1]]>np.r_[s.e20[0],s.e20[:-1]]); xv=(C>s.vw)!=(np.r_[C[0],C[:-1]]>np.r_[s.vw[0],s.vw[:-1]])
        s.xs=roll_sum((xe|xv).astype(float),k)
        s.slope=np.abs(s.h20-np.r_[np.full(k,np.nan),s.h20[:-k]])/s.atr
        a100=pd.Series(s.atr).rolling(100).mean().values; s.atrrel=s.atr/a100
        # HTF ER over the last 6 closed HTF candles (5x tf), known at each HTF close bar, held
        last=B['last'].values; isc=(s.T==last)
        hcl=C[isc]; hidx=np.where(isc)[0]; herv=np.full(len(hcl),np.nan)
        for j in range(6,len(hcl)):
            den=np.abs(np.diff(hcl[j-6:j+1])).sum(); herv[j]=abs(hcl[j]-hcl[j-6])/den if den else 0
        s.her=np.full(n,np.nan); cur=np.nan; p=0
        for i in range(n):
            if p<len(hidx) and hidx[p]==i: cur=herv[p]; p+=1
            s.her[i]=cur
        # LTF swing pivots N=2 (confirmed 2 bars later)
        s.swh=np.full(n,np.nan); s.swl=np.full(n,np.nan); lh=ll2=np.nan
        for i in range(n):
            j=i-2
            if j>=2 and H[j]>max(H[j-2:j]) and H[j]>=max(H[j+1:j+3]): lh=H[j]
            if j>=2 and L[j]<min(L[j-2:j]) and L[j]<=min(L[j+1:j+3]): ll2=L[j]
            s.swh[i],s.swl[i]=lh,ll2
        # breakout: close through last swing H/L or a session OR H/L (prev close on the other side); window 3 bars
        bo=np.zeros(n,bool)
        lv=[np.r_[np.nan,s.swh[:-1]],np.r_[np.nan,s.swl[:-1]]]+[B[c].values for c in ('nyh','nyl','lnh','lnl','ash','asl')]
        for v in lv:
            pv=np.r_[np.nan,v[:-1]]
            bo|=((C>v)&(np.r_[C[0],C[:-1]]<=pv))|((C<v)&(np.r_[C[0],C[:-1]]>=pv))
        s.bo1=bo; s.bo=bo|np.r_[False,bo[:-1]]|np.r_[False,False,bo[:-2]]
        # 1H CBC (last closed 60m candle)
        hb=s.T//3600000; s.mtf=np.full(n,-1); st=None; ph=pl=None; cur=-1
        df=pd.DataFrame({'k':hb,'h':H,'l':L,'c':C}); g=df.groupby('k',sort=False).agg(h=('h','max'),l=('l','min'),c=('c','last'))
        states={}; prev=None; stt=False
        for k2,row in g.iterrows():
            if prev is not None:
                if stt and row.c<prev.l: stt=False
                if not stt and row.c>prev.h: stt=True
            states[k2]=1 if stt else 0; prev=row
        keys=list(g.index); nxt={keys[i]:keys[i-1] for i in range(1,len(keys))}
        s.mtf=np.array([states.get(nxt.get(k2),-1) for k2 in hb])
        s.cands=s.gen()
    def gen(s):
        """all trigger events with NO chop filter; returns list of dicts"""
        C,H,L,O=s.C,s.H,s.L,s.O; out=[]; n=s.n; hk=5
        e20,h9,h20=s.e20,s.h9,s.h20
        flip_ok=np.zeros(n,bool); fo=False
        for i in range(n):
            if s.hf[i]!=0: fo=(C[i]>h20[i]) if s.hf[i]==1 else (C[i]<h20[i])
            flip_ok[i]=fo
        om=(s.hm-s.tf)%1440  # candle open minute
        orf=((om>=570)&(om<600))|((om>=180)&(om<210))|((om>=1200)&(om<1230))
        # VWAP reclaim against HTF dir blocks 5 bars: HTF short, close below VWAP then a later close back above -> no short
        vwb=np.zeros(n,int); st=0; lastb=-99; bdir=0
        for i in range(1,n):
            xd=C[i]<s.vw[i] and C[i-1]>=s.vw[i-1]; xu=C[i]>s.vw[i] and C[i-1]<=s.vw[i-1]
            if (xu and st==-1) or (xd and st==1): lastb=i; bdir=st
            st=0 if s.hf[i]!=0 else (-1 if (xd and s.hdir[i]==0) else 1 if (xu and s.hdir[i]==1) else 0 if (xu or xd) else st)
            vwb[i]=bdir if i-lastb<=5 else 0
        s.flip_ok=flip_ok; s.orf=orf; s.vwb=vwb
        FD={'MGC':10,'MES':8}.get(s.sym,0)
        lastp=-99
        def pierce(line,i,lg):
            if lg: return L[i-1]>line[i-1] and L[i]<=line[i]<=H[i]
            return H[i-1]<line[i-1] and L[i]<=line[i]<=H[i]
        for i in range(250,n-1):
            if np.isnan(s.atr[i]) or s.hdir[i]<0: continue
            hm=s.hm[i]
            if 16*60<=hm<18*60+30 or orf[i]: continue
            dirn=s.hdir[i]==1
            if not flip_ok[i]: continue
            # flip
            if s.hf[i]!=0:
                lg=s.hf[i]==1; vw,e2=s.vw[i],s.e200[i]
                side=(C[i]>max(vw,e2)+1) if lg else (C[i]<min(vw,e2)-1)
                vws=(s.vw[i]-s.vw[i-hk])*(1 if lg else -1)>0
                fd=abs(C[i]-e20[i])<=max(2*s.atr[i],FD)
                if side and vws and fd: out.append(dict(i=i,lg=lg,trig='flip'))
            for nm,line,mn in (('ltf20',e20,.08),('h9',h9,.15),('h20',h20,.15)):
                lg=dirn
                if nm=='ltf20' and pierce(line,i,lg):
                    if i-lastp<=3: continue
                    lastp=i
                if pierce(line,i,lg):
                    if (C[i]>line[i]) if lg else (C[i]<line[i]): out.append(dict(i=i,lg=lg,trig=nm,erm=mn))
                    elif i+1<n and s.hdir[i+1]==s.hdir[i] and ((C[i+1]>line[i+1]) if lg else (C[i+1]<line[i+1])): out.append(dict(i=i+1,lg=lg,trig=nm,erm=mn,late=1))
        out.sort(key=lambda d:(d['i'],d['trig']!='flip'))
        g=1
        for d in out:
            i=d['i']; lg=d['lg']; A=s.atr[i]; gg=1 if lg else -1
            hi=s.H[i-23:i+1].max(); lo=s.L[i-23:i+1].min(); pos=(C[i]-lo)/(hi-lo) if hi>lo else .5
            d['R5']=(pos if lg else 1-pos)>=.8 and (hi-lo)/A<5
            d['X4']=gg*(C[i]-s.vw[i])/A>4
            d['M']=s.mtf[i]>=0 and s.mtf[i]!=(1 if lg else 0)
            d['VB']=s.vwb[i]==(1 if lg else -1)
            d.update(er={k:s.er[k][i] for k in s.er}, bo=bool(s.bo[i]), bo1=bool(s.bo1[i]), chop=s.chop[i], adx=s.adx[i], xs=s.xs[i], slope=s.slope[i], rng=s.rng[i], her=s.her[i], atrrel=s.atrrel[i], month=s.month[i])
        return out
    def sim1(s,i,lg,q,stop_at):
        C,H,L=s.C,s.H,s.L; en=C[i]; A=s.atr[i]; g=1 if lg else -1
        sd=min(max(q['sl']*A,q['mn']),q['cap']); tpd=min(q['tp']*A,6)
        sl=en-g*sd; t1=en+g*tpd; hit=False; best=0
        for j in range(i+1,s.n):
            if (L[j]<=sl if lg else H[j]>=sl):
                rem=g*(sl-en); return (q['part']*tpd+(1-q['part'])*rem if hit else rem),j,('trail' if hit else 'SL1')
            if not hit and (H[j]>=t1 if lg else L[j]<=t1):
                hit=True
                if q['be']: sl=max(sl,en) if lg else min(sl,en)
            best=max(best,g*((H[j] if lg else L[j])-en))
            if hit:
                ns=C[j]-g*q['tr']*s.atr[j]; sl=max(sl,ns) if lg else min(sl,ns)
            why=None
            if s.hdir[j]==(0 if lg else 1): why='flip'
            elif s.hm[j]==16*60: why='16:00'
            elif q['ts'] and not hit and j-i==q['ts'] and best<0.5*A: why='time'
            elif j==stop_at: why='new'
            if why:
                rem=g*(C[j]-en); return (q['part']*tpd+(1-q['part'])*rem if hit else rem),j,why
        return 0.0,s.n-1,'end'
    def run(s, ok, q=None, gates=None):
        """ok(cand)->bool chop filter. Event-driven: cooldown 10 (flip/opposite bypass), new setup ends the open one."""
        q=q or EXIT[(s.sym,s.tf)]; G=gates or GATE[(s.sym,s.tf)]
        res=[]; last=-999; lastlg=None; op=None
        for d in s.cands:
            if G['R5'] and d['R5']: continue
            if G['X4'] and d['X4']: continue
            if G['MTF'] and d['M']: continue
            if d['VB']: continue
            if d['trig']!='flip' and d['er'][12]<d['erm']: continue  # per-trigger minimum (not lifted by breakout)
            if not ok(d): continue
            i=d['i']
            live=op is not None and i<=op['j']
            if res and res[-1]['i']==i: continue
            if live and d['lg']==op['lg']: continue          # one live setup per direction (ats_one_on)
            if not (i-last>=10 or d['trig']=='flip' or (lastlg is not None and d['lg']!=lastlg)): continue
            if live:                                          # opposite setup replaces the live one at this close
                r,j,why=s.sim1(op['i'],op['lg'],q,i); op.update(res=r,j=j,why=why)
            r,j,why=s.sim1(i,d['lg'],q,-1); op=dict(d,res=r,why=why,j=j); res.append(op); last=i; lastlg=d['lg']
        return res

def cur_rule(d, thr=.23, flip_thr=.23, k=12, bo=True):
    e=d['er'][k]
    if d['trig']=='flip' and e<flip_thr: return False
    return e>=thr or (bo and d['bo'])
