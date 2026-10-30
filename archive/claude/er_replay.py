import json,re,datetime as dt,math
tz=dt.timezone(dt.timedelta(hours=-4))
B=json.load(open('mgc60.json'))['bars']
T=[b['t'] for b in B]; O=[b['o'] for b in B];H=[b['h'] for b in B];L=[b['l'] for b in B];C=[b['c'] for b in B]
HF=[b.get('hf',0) for b in B]
n=len(B)
# ATR14 (RMA) and ER12
tr=[H[0]-L[0]]+[max(H[i]-L[i],abs(H[i]-C[i-1]),abs(L[i]-C[i-1])) for i in range(1,n)]
atr=[None]*n; a=sum(tr[:14])/14; atr[13]=a
for i in range(14,n): a=(a*13+tr[i])/14; atr[i]=a
def er(i,k=12):
    if i<k: return None
    d=sum(abs(C[j]-C[j-1]) for j in range(i-k+1,i+1)); return abs(C[i]-C[i-k])/d if d>0 else None
idx={t:i for i,t in enumerate(T)}
A=json.load(open('al.json'))
seen=set(); trig=[]
for x in A:
    r=x['raw']
    if not r.startswith('MGC'): continue
    m=re.search(r'Time: 10/(\d+) (\d+):(\d+)',r)
    if not m: continue
    for l in r.split('\n'):
        k=None
        mm=re.match(r'•\s*(LTF EMA20 Pierce|HTF EMA9 Pierce|HTF EMA20 Pierce) - Entry: (LONG|SHORT)',l)
        if mm: k=(mm.group(1),mm.group(2))
        mm=re.match(r'•\s*HTF\(15\) CBC Flip.*?: (LONG|SHORT) .*confirmed',l)
        if mm: k=('HTF CBC Flip',mm.group(1))
        if not k: continue
        d,hh,mi=int(m.group(1)),int(m.group(2)),int(m.group(3))
        # alert time is candle range start-end; bar open = start
        st=dt.datetime(2026,10,d,hh,mi,tzinfo=tz)
        t0=int(st.timestamp()*1000)
        key=(k,t0)
        if key in seen: continue
        seen.add(key)
        if t0 in idx: trig.append((idx[t0],k[0],k[1]=='LONG'))
def sim(i,lg):
    en=C[i]; at=atr[i]
    s=min(1.7*at,7); s=max(s,5); tp=min(1.7*at,6)
    sl=en-s if lg else en+s; t1=en+tp if lg else en-tp
    hit1=False; part=0.8
    for j in range(i+1,min(n,i+200)):
        tj=dt.datetime.fromtimestamp(T[j]/1000,tz)
        if (lg and L[j]<=sl) or (not lg and H[j]>=sl):
            rem=(sl-en)*(1 if lg else -1); return (part*tp+(1-part)*rem) if hit1 else rem
        if not hit1 and ((lg and H[j]>=t1) or (not lg and L[j]<=t1)):
            hit1=True; sl=max(sl,en) if lg else min(sl,en)
        if hit1:
            sl=max(sl,C[j]-1.7*atr[j]) if lg else min(sl,C[j]+1.7*atr[j])
        if (lg and HF[j]==-1) or (not lg and HF[j]==1) or (tj.hour==17 and tj.minute==0):
            rem=(C[j]-en)*(1 if lg else -1); return (part*tp+(1-part)*rem) if hit1 else rem
    return 0
rows=[]
for i,k,lg in trig:
    e=er(i)
    if e is None or atr[i] is None: continue
    rows.append((e,k,lg,sim(i,lg),dt.datetime.fromtimestamp(T[i]/1000,tz).strftime('%m/%d %H:%M')))
def summ(name,rs):
    if not rs: print(name,'n=0'); return
    w=sum(1 for r in rs if r[3]>0); tot=sum(r[3] for r in rs)
    print(f"{name:14s} n={len(rs):3d} win%={100*w/len(rs):5.1f} total={tot:+7.1f} avg={tot/len(rs):+5.2f}")
summ('ER < 0.18',[r for r in rows if r[0]<0.18])
summ('0.18-0.23',[r for r in rows if 0.18<=r[0]<0.23])
summ('ER >= 0.23',[r for r in rows if r[0]>=0.23])
summ('ALL',rows)
print('--- 0.18-0.23 detail'); 
for r in sorted(rows):
    if 0.18<=r[0]<0.23: print(r[4],r[1],'L' if r[2] else 'S',round(r[0],2),round(r[3],2))
print('--- <0.18 detail')
for r in sorted(rows):
    if r[0]<0.18: print(r[4],r[1],'L' if r[2] else 'S',round(r[0],2),round(r[3],2))
