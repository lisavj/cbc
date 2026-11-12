import pickle, numpy as np, pandas as pd, collections as C, sys
import chop_sim as cs, late_study as ls, trend_guard_study as tg
def sub(mm):  # ET minutes -> sub-session
    return 'Asia 18-03' if (mm >= 1080 or mm < 180) else 'London 03-09:30' if mm < 570 else 'NY 09:30-16' if mm < 960 else 'late 16-18'
def guard2(r, K, N, mode='session', pause=0, et=None):
    """mode: session = stop rest of 18-18 session; sub = reset at 03:00 and 09:30 ET; pause = stop for `pause` candles then reset counts"""
    keep = []; skip = {}; st = {}
    for t in sorted(r, key=lambda t: t['i']):
        key = t['ss'] if mode != 'sub' else (t['ss'], t['sub'])
        S = st.setdefault(key, dict(until=-1, since=-1, why=None))
        if mode == 'pause' and S['until'] >= 0 and t['i'] >= S['until']: S.update(until=-1, since=t['i'], why=None)
        if S['until'] != -1 and (mode != 'pause' or t['i'] < S['until']): skip[t['i']] = S['why']; continue
        fin = sorted([u for u in keep if (u['ss'] if mode != 'sub' else (u['ss'], u['sub'])) == key and u['j'] < t['i'] and u['i'] > S['since']], key=lambda u: u['j'])
        ls_ = 0
        for u in fin: ls_ = ls_ + 1 if u['n'] < 0 else 0
        fo = sum(1 for u in fin if u['why'] == 'flip' and u['n'] < 0)
        w = 'losses' if K and ls_ >= K else 'flip-outs' if N and fo >= N else None
        if w:
            S['why'] = w; S['until'] = (t['i'] + pause) if mode == 'pause' else 10**9; skip[t['i']] = w; continue
        keep.append(t)
    return keep, skip
if __name__ == '__main__':
    out = {}
    for sym in ('MES', 'MGC'):
        nm, q, G, cost = tg.CH[sym]
        B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = ls.LCase(sym, 3, B); TR, ss = tg.trend_arrays(s)
        et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); mm = (et.dt.hour * 60 + et.dt.minute).values
        T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
        runs = {}
        for f in (None, ('d5', 'S'), ('d5', 'B')):
            def ok(d, f=f):
                if not cs.cur_rule(d): return False
                if f is None or (f[1] == 'S' and d['lg']): return True
                v = TR[f[0]][d['i']]; return v == 0 or v == (1 if d['lg'] else -1)
            r = s.run(ok, q=q, gates=G)
            runs[f] = [dict(i=t['i'], j=t['j'], lg=t['lg'], why=t['why'], trig=t['trig'], n=t['res'] - cost, g=t['res'],
                            th=0 if s.T[t['i']] < cuts[0] else 1 if s.T[t['i']] < cuts[1] else 2, l4=bool(s.T[t['i']] >= t4), ss=ss[t['i']],
                            hr=int(mm[t['i']] // 60), sub=sub(mm[t['i']]), day=et.iloc[t['i']].strftime('%a %m/%d'), tm=et.iloc[t['i']].strftime('%H:%M'),
                            d5=int(TR['d5'][t['i']]), atr=float(s.atr[t['i']])) for t in r]
        out[sym] = dict(nm=nm, cost=cost, runs=runs)
        print(sym, 'loaded', flush=True)
    pickle.dump(out, open('skip_why.pkl', 'wb'))
