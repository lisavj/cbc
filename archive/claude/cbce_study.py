"""Four "CBC Engine [MMT]" ideas tested on CBC -- MES 3m and MGC 3m -- 11/14/2026. Replay Jan 5 -> now, CBC engine setups, live gates.
Live exits: MES 3m SL1 3 ATR (min 5, no cap), TP1 1.75 ATR, 100 % at TP1. MGC 3m SL1 1.7 ATR (min 5, cap 7), TP1 1.7 ATR (cap 6),
0 % at TP1 + breakeven, then closed by the HTF CBC flip ("FLIP 0 %", CBC v10.96). Every setup also ends at 16:00 or the next setup.
1. CLOSE STOP: the stop only counts when a candle CLOSES beyond it (exit at that close) instead of a touch. (a) SL1 only, (b) SL1 + BE.
2. LAST-N STOP: SL1 = lowest low (long) / highest high (short) of the last N candles incl. the entry candle, N = 2 / 3 / 5;
   raw, and clamped to the symbol's min / cap. TP1 unchanged.
3. STRONG FLIP: keep a setup only if its candle swept the previous candle's low (long) then closed above the previous high
   (mirrored short). (a) the 3m entry candle, (b) the 15m candle of the HTF flip (flip setups only; others kept), (c) both.
4. ENVIRONMENT: longs only when slow EMA > VWAP, shorts only when slow EMA < VWAP; slow EMA = 3m EMA20 / 15m EMA20 / EMA200.
Ideas 3-4 are entry gates (a skipped setup can change later setups); 1-2 are exits on the same setups.
Net after costs (MES 0.50, MGC 0.22). z = Δ / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds."""
import numpy as np, pandas as pd
import combo_study as cb, chop_sim as cs, late_study as ls
X = {'MES': dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, p=1.0, be=False, c=.5, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7)),
     'MGC': dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, p=0.0, be=True, c=.22, q=dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9))}
out = [__doc__, '']
for sym in ('MES', 'MGC'):
    x = X[sym]; B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B); G = cb.CH[sym][2]; s.TX, s.TY = (0, 0.0); s.ACT = None
    C, H, L, O = s.C, s.H, s.L, s.O; T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    # 15m candles for strong HTF flip
    hk = B.hk.values; g = pd.DataFrame({'k': hk, 'h': H, 'l': L, 'c': C, 'i': np.arange(s.n)}).groupby('k', sort=False).agg(h=('h', 'max'), l=('l', 'min'), c=('c', 'last'), last=('i', 'max'))
    hs = {}; gh, gl, gc, gi = g.h.values, g.l.values, g.c.values, g['last'].values
    for k in range(1, len(g)): hs[gi[k]] = (gl[k] < gl[k - 1] and gc[k] > gh[k - 1], gh[k] > gh[k - 1] and gc[k] < gl[k - 1])
    def strong3(i, lg): return (L[i] < L[i - 1] and C[i] > H[i - 1]) if lg else (H[i] > H[i - 1] and C[i] < L[i - 1])
    def strongH(i, lg):
        v = hs.get(i); return True if v is None else (v[0] if lg else v[1])
    def sim(i, lg, stop, sd=None, cst=False, cbe=False):
        en = C[i]; A = s.atr[i]; gg = 1 if lg else -1
        if sd is None: sd = max(min(x['sl'] * A, x['cap']), x['mn'])
        tpd = min(x['tp'] * A, x['tcap']); sl = en - gg * sd; t1 = en + gg * tpd; hit = False; p = x['p']
        for j in range(i + 1, s.n):
            closeonly = cbe if hit else cst
            br = ((C[j] <= sl) if lg else (C[j] >= sl)) if closeonly else ((L[j] <= sl) if lg else (H[j] >= sl))
            if br:
                ex = C[j] if closeonly else sl; rem = gg * (ex - en); return (p * tpd + (1 - p) * rem if hit else rem), sd
            if not hit and ((H[j] >= t1) if lg else (L[j] <= t1)):
                hit = True
                if p >= 1: return tpd, sd
                if x['be']: sl = max(sl, en) if lg else min(sl, en)
            if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop:
                rem = gg * (C[j] - en); return (p * tpd + (1 - p) * rem if hit else rem), sd
        return None, sd
    def score(R, **kw):
        ST = [(r['i'], r['lg'], R[k + 1]['i'] if k + 1 < len(R) else -1, r) for k, r in enumerate(R)]
        v = []; K = {}; th = [0, 0, 0]; l4 = 0; sds = []
        for (i, lg, stop, r) in ST:
            sdf = kw.get('sdf'); res, sd = sim(i, lg, stop, sd=sdf(i, lg) if sdf else None, cst=kw.get('cst', False), cbe=kw.get('cbe', False))
            if res is None: continue
            res -= x['c']; v.append(res); sds.append(sd); K[(i, lg)] = res; th[0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2] += res
            if s.T[i] >= t4: l4 += res
        v = np.array(v)
        return dict(n=len(v), net=v.sum(), sd=v.std(), th=th, l4=l4, w=100 * (v > 0).mean(), mx=v.min(), sdm=np.mean(sds), K=K)
    base_R = s.run(lambda d: cs.cur_rule(d), q=x['q'], gates=G); L0 = score(base_R)
    rows = []
    def add(name, a):
        ch = sum(1 for k in set(a['K']) | set(L0['K']) if abs(a['K'].get(k, 1e9) - L0['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - L0['net']) / (L0['sd'] * np.sqrt(ch)); d = [p - q for p, q in zip(a['th'], L0['th'])]
        vd = 'robust' if z >= 2 and all(t > 0 for t in d) else 'promising' if z >= 1 and all(t > 0 for t in d) else 'worse' if a['net'] < L0['net'] else 'noise'
        rows.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f %% | %.1f | %+.1f | %s |' % (name, a['n'], a['net'], a['net'] - L0['net'], z, *d, a['l4'] - L0['l4'], a['w'], a['sdm'], a['mx'], vd))
    add('**Current (live)**', L0)
    add('1a. Close stop: SL1 on a close (BE still a touch)', score(base_R, cst=True))
    add('1b. Close stop: SL1 and BE on a close', score(base_R, cst=True, cbe=True))
    for N in (2, 3, 5):
        def sdf(i, lg, N=N):
            lo = L[i - N + 1:i + 1].min(); hi = H[i - N + 1:i + 1].max(); return max((C[i] - lo) if lg else (hi - C[i]), s.atr[i] * .1)
        add('2. Last-%d-candle stop, raw' % N, score(base_R, sdf=sdf))
        add('2. Last-%d-candle stop, min %d%s' % (N, x['mn'], '' if x['cap'] > 100 else ' / cap %d' % x['cap']), score(base_R, sdf=lambda i, lg, f=sdf: max(min(f(i, lg), x['cap']), x['mn'])))
    for nm, f in (('3a. Strong flip: 3m entry candle', lambda d: strong3(d['i'], d['lg'])), ('3b. Strong flip: 15m flip candle (flip setups)', lambda d: d['trig'] != 'flip' or strongH(d['i'], d['lg'])),
                  ('3c. Strong flip: both', lambda d: strong3(d['i'], d['lg']) and (d['trig'] != 'flip' or strongH(d['i'], d['lg']))),
                  ('4. Environment: 3m EMA20 vs VWAP', lambda d: (s.e20[d['i']] > s.vw[d['i']]) == d['lg']), ('4. Environment: 15m EMA20 vs VWAP', lambda d: (s.h20[d['i']] > s.vw[d['i']]) == d['lg']),
                  ('4. Environment: EMA200 vs VWAP', lambda d: (s.e200[d['i']] > s.vw[d['i']]) == d['lg'])):
        add(nm, score(s.run(lambda d, f=f: cs.cur_rule(d) and f(d), q=x['q'], gates=G)))
    out += ['## %s 3m -- current: %d setups, net %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, win %.0f %%' % (sym, L0['n'], L0['net'], *L0['th'], L0['l4'], L0['w']), '',
            '| Variant | Setups | Net | Δ | z | Δ by third | Δ last 4 wk | Win % | Avg stop pts | Worst trade | Verdict |', '|---|---|---|---|---|---|---|---|---|---|---|'] + rows + ['']
open('cbce_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
