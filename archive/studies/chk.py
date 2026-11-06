import mes3_ema_grid as m, numpy as np
B0=m.load(); C=B0.c.values.astype(float)
cs={}
for sl in (20,14,16):
    B=B0.copy(); B['e20']=m.ema(C,sl); cs[sl]=m.MCase('MES',3,B)
s0=cs[20]; T0,T1=s0.T[300],s0.T[-1]; cuts=[T0+(T1-T0)*k/3 for k in (1,2)]
for sl in (20,14,16):
    s=cs[sl]
    for sk,tk,pk in ((3.0,1.5,'tod'),(3.0,1.75,'tod'),(3.0,2.0,'tod'),(2.0,1.5,1.0),(2.0,1.5,'tod'),(1.7,1.7,.8)):
        r=m.run(s,dict(m.LIVE,sl=sk,tp=tk,part=pk))
        th=[sum(x['res'] for x in r if (0 if s.T[x['i']]<cuts[0] else 1 if s.T[x['i']]<cuts[1] else 2)==k) for k in range(3)]
        t4=s.T[-1]-28*86400000; l4=[x['res'] for x in r if s.T[x['i']]>=t4]
        print(sl,sk,tk,pk,len(r),round(sum(x['res'] for x in r)),[round(x) for x in th],'last4w',len(l4),round(sum(l4),1))
