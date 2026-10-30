import json,datetime as dt,sys
d=json.load(open(sys.argv[1]))['bars']
tz=dt.timezone(dt.timedelta(hours=-4))
T=[dt.datetime.fromtimestamp(b['t']/1000,tz) for b in d]
H=[b['h'] for b in d];L=[b['l'] for b in d];C=[b['c'] for b in d];O=[b['o'] for b in d];V=[b['v'] for b in d]
def ts(i): return T[i].strftime('%m-%d %H:%M')
def run(mode='Leg',ln=5,mit='Close',ov='skip',verbose=False):
    os_=0;prev=0;top=None;btm=None  # swing: [y,x,crossed]
    bulls=[];bears=[];log=[]
    for n in range(len(d)):
        if n>=ln:
            if mode=='Leg':
                up=max(H[n-ln+1:n+1]);lo=min(L[n-ln+1:n+1])
                o2=0 if H[n-ln]>up else (1 if L[n-ln]<lo else os_)
                if o2==0 and os_!=0: top=[H[n-ln],n-ln,False]
                if o2==1 and os_!=1: btm=[L[n-ln],n-ln,False]
                os_=o2
            else:
                if n>=2*ln:
                    c=n-ln
                    if H[c]>max(H[c-ln:c]) and H[c]>=max(H[c+1:n+1]): top=[H[c],c,False]
                    if L[c]<min(L[c-ln:c]) and L[c]<=min(L[c+1:n+1]): btm=[L[c],c,False]
        for side in ('bull','bear'):
            sw=top if side=='bull' else btm
            if sw and not sw[2] and ((C[n]>sw[0]) if side=='bull' else (C[n]<sw[0])):
                sw[2]=True
                span=max(1,n-sw[1]-1);ext=None
                for i in range(1,span+1):
                    v=L[n-i] if side=='bull' else H[n-i]
                    if ext is None or (v<=ext if side=='bull' else v>=ext):
                        ext=v;k=i
                t,b=(H[n-k],L[n-k]) if side=='bull' else (H[n-k],L[n-k])
                arr=bulls if side=='bull' else bears
                skip= ov=='skip' and any((not e['brk']) and t>e['b'] and b<e['t'] for e in arr)
                e=dict(t=t,b=b,k=n-k,made=n,brk=False,sw=sw[1],skip=skip)
                log.append((side,e))
                if not skip: arr.insert(0,e)
        for arr,bull in ((bulls,True),(bears,False)):
            for e in list(arr):
                if not e['brk']:
                    hit=(C[n]<e['b']) if bull else (C[n]>e['t'])
                    if mit=='Body': hit=(min(C[n],O[n])<e['b']) if bull else (max(C[n],O[n])>e['t'])
                    if hit: e['brk']=True;e['bt']=n
                elif (C[n]>e['t']) if bull else (C[n]<e['b']): arr.remove(e)
    return bulls,bears,log
if __name__=='__main__':
    mode=sys.argv[2] if len(sys.argv)>2 else 'Leg'; ov=sys.argv[3] if len(sys.argv)>3 else 'skip'
    bulls,bears,log=run(mode=mode,ov=ov)
    day=dt.date(2026,10,14)
    print('--- created today (side, OB candle, top-btm, swing, made, skipped)')
    for s,e in log:
        if T[e['made']].date()==day and T[e['made']].time()>=dt.time(11,0):
            print(s,ts(e['k']),e['t'],e['b'],'sw',ts(e['sw']),'made',ts(e['made']),'SKIP' if e['skip'] else '', 'brk '+ts(e['bt']) if e.get('bt') else '')
    print('--- active bulls at end (not breaker)')
    for e in bulls:
        if not e['brk']: print(ts(e['k']),e['t'],e['b'])
    print('--- active bears at end')
    for e in bears:
        if not e['brk']: print(ts(e['k']),e['t'],e['b'])
