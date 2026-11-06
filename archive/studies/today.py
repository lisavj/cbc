import mes3_ema_grid as m, numpy as np, pandas as pd, datetime as D
m.load.__globals__  # noqa
import os
B=pd.DataFrame(m.get(m.BASE+'/bars?sym=MES&days=400&from=2026-10-01')['bars'])
if 'live' in B: B=B[B['live'].isna()|(B['live']==0)]
B=B.sort_values('t').drop_duplicates('t',keep='last').reset_index(drop=True)
for c in B.columns:
    if c!='fl': B[c]=pd.to_numeric(B[c],errors='coerce')
for c in ('nyh','nyl','lnh','lnl','ash','asl','e200','vw','e20','h9','h20','hc','hf'):
    if c not in B: B[c]=np.nan
et=pd.to_datetime(B.t,unit='ms',utc=True).dt.tz_convert('America/New_York')
start=(et+pd.Timedelta(hours=6)).dt.normalize()-pd.Timedelta(hours=6)
mins=((et-start).dt.total_seconds()//60).astype(int)
B['hk']=start.dt.strftime('%Y-%m-%d')+'_'+(mins//15).astype(str); B['last']=B.groupby('hk').t.transform('max'); B['hf']=B['hf'].fillna(0)
print('last bar', et.iloc[-1])
C=B.c.values.astype(float)
for sl in (20,14):
    X=B.copy(); X['e20']=m.ema(C,sl); s=m.MCase('MES',3,X)
    q=dict(m.LIVE,tp=2.0)
    res=m.run(s,q)
    print('== slow',sl)
    for r in res:
        if s.date[r['i']].startswith('11/05'):
            print(s.date[r['i']],'L' if r['lg'] else 'S',r['trig'],round(s.C[r['i']],2),r['why'],round(r['res'],2))
    # raw candidates today
    print(' cands:',[(s.date[d['i']][6:],d['trig'],'R5' if d['R5'] else '','VB' if d['VB'] else '',round(d['er'][12],2)) for d in s.cands if s.date[d['i']].startswith('11/05')])
