"""MGC 3m stop-loss mechanisms, with and without the HTF EMA20 slope filter -- 11/14/2026.
Setups: CBC engine replay Jan 5 -> now, current MGC 3m filters (ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, VWAP stretch 4 ATR --
applied correctly, see tsf_study), and the same + "Block in chop: HTF EMA20 slope below 0.3 ATR" (|15m EMA20 now - 12 bars ago| / ATR).
Exit = live FLIP 0 %: nothing closed at TP1 (1.7 ATR, cap 6); at TP1 the stop moves to breakeven; closed by the HTF CBC flip against,
16:00 or the next setup. Only the initial stop (SL1) changes. Same setups for every stop (rescored), net after 0.22 cost per trade.
Stops: (A) SL1 x ATR with min 5 and cap 7 (live 1.7); (B) no cap / cap 10; (C) close-based (stop counts only on a close beyond it);
(D) last-N-candle low/high, raw and clamped min 5 / cap 7; (E) last-N low/high + 0.5 ATR buffer, clamped.
z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, better in all three thirds and last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd
import combo_study as cb, chop_sim as cs, late_study as ls
COST = .22; Q = dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9)
B = ls.load('MGC', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase('MGC', 3, B)
C, H, L, A = s.C, s.H, s.L, s.atr; S = pd.Series; n = 12
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
hh24, ll24 = S(H).rolling(24).max().values, S(L).rolling(24).min().values
h20 = B.h20.values.astype(float); SLP = np.abs(h20 - np.roll(h20, n)) / A
def ok(d, slope):
    i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
    if not cs.cur_rule(d): return False
    w = hh24[i] - ll24[i]
    if w > 0 and w / a < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
    if g * (C[i] - s.vw[i]) / a > 4: return False
    if slope and SLP[i] < slope: return False
    return True
def sim(i, lg, stop, sd, cst=False, cbe=False):
    en = C[i]; gg = 1 if lg else -1; tpd = min(1.7 * A[i], 6); sl = en - gg * sd; t1 = en + gg * tpd; hit = False
    for j in range(i + 1, s.n):
        co = cbe if hit else cst
        br = ((C[j] <= sl) if lg else (C[j] >= sl)) if co else ((L[j] <= sl) if lg else (H[j] >= sl))
        if br: return gg * ((C[j] if co else sl) - en)
        if not hit and ((H[j] >= t1) if lg else (L[j] <= t1)): hit = True; sl = max(sl, en) if lg else min(sl, en)
        if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop: return gg * (C[j] - en)
    return None
def lastn(i, lg, N, buf=0.):
    return (C[i] - L[i - N + 1:i + 1].min() if lg else H[i - N + 1:i + 1].max() - C[i]) + buf * A[i]
cl = lambda v, mn=5, cap=7: max(min(v, cap), mn)
V = [('**Live: 1.7 ATR, min 5, cap 7**', lambda i, lg: cl(1.7 * A[i]), {}),
     ('A. 1.3 ATR, min 5, cap 7', lambda i, lg: cl(1.3 * A[i]), {}), ('A. 1.5 ATR, min 5, cap 7', lambda i, lg: cl(1.5 * A[i]), {}),
     ('A. 2.0 ATR, min 5, cap 7', lambda i, lg: cl(2.0 * A[i]), {}), ('A. 2.5 ATR, min 5, cap 7', lambda i, lg: cl(2.5 * A[i]), {}),
     ('A. 1.7 ATR, min 4, cap 7', lambda i, lg: cl(1.7 * A[i], 4), {}), ('A. 1.7 ATR, min 6, cap 7', lambda i, lg: cl(1.7 * A[i], 6), {}),
     ('A. Fixed 7 pts', lambda i, lg: 7.0, {}), ('A. Fixed 5 pts', lambda i, lg: 5.0, {}),
     ('B. 1.5 ATR, min 5, no cap', lambda i, lg: cl(1.5 * A[i], 5, 1e9), {}), ('B. 1.7 ATR, min 5, no cap', lambda i, lg: cl(1.7 * A[i], 5, 1e9), {}),
     ('B. 2.0 ATR, min 5, no cap', lambda i, lg: cl(2.0 * A[i], 5, 1e9), {}), ('B. 1.7 ATR, min 5, cap 10', lambda i, lg: cl(1.7 * A[i], 5, 10), {}),
     ('B. 2.0 ATR, min 5, cap 10', lambda i, lg: cl(2.0 * A[i], 5, 10), {}),
     ('C. Close stop: SL1 on a close (BE a touch)', lambda i, lg: cl(1.7 * A[i]), dict(cst=True)),
     ('C. Close stop: SL1 and BE on a close', lambda i, lg: cl(1.7 * A[i]), dict(cst=True, cbe=True))]
for N in (2, 3, 5, 8):
    V += [('D. Last-%d-candle low/high, raw' % N, lambda i, lg, N=N: max(lastn(i, lg, N), .1 * A[i]), {}),
          ('D. Last-%d-candle low/high, min 5 / cap 7' % N, lambda i, lg, N=N: cl(lastn(i, lg, N)), {}),
          ('E. Last-%d low/high + 0.5 ATR, min 5 / cap 7' % N, lambda i, lg, N=N: cl(lastn(i, lg, N, .5)), {})]
out = [__doc__, '']; top = ['## Overview -- best stops per filter set (Δ vs live stop in the same set)', '']
for fn, slope in (('Current filters', 0), ('Current + HTF EMA20 slope < 0.3 ATR block', .3)):
    R = s.run(lambda d: ok(d, slope), q=Q, gates=dict(R5=0, X4=0, MTF=0))
    ST = [(r['i'], r['lg'], R[k + 1]['i'] if k + 1 < len(R) else -1) for k, r in enumerate(R)]
    res = []
    for nm, f, kw in V:
        v = []; K = {}; th = [0, 0, 0]; l4 = 0; sds = []
        for (i, lg, stop) in ST:
            sd = f(i, lg); x = sim(i, lg, stop, sd, **kw)
            if x is None: continue
            x -= COST; v.append(x); sds.append(sd); K[i] = x; th[0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2] += x
            if s.T[i] >= t4: l4 += x
        v = np.array(v); eq = np.cumsum(v); dd = (np.maximum.accumulate(eq) - eq).max()
        res.append(dict(nm=nm, n=len(v), net=v.sum(), sd=v.std(), th=th, l4=l4, w=100 * (v > 0).mean(), mx=v.min(), sdm=np.mean(sds), dd=dd, K=K))
    b = res[0]; rows = []
    for r in res:
        ch = sum(1 for k in r['K'] if abs(r['K'][k] - b['K'].get(k, 1e9)) > 1e-9) or 1
        z = (r['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d = [p - q for p, q in zip(r['th'], b['th'])]; l4 = r['l4'] - b['l4']
        vd = '' if r is b else 'robust' if z >= 2 and all(t > 0 for t in d) and l4 >= 0 else 'robust except last 4 wk' if z >= 2 and all(t > 0 for t in d) else 'promising' if z >= 1 and all(t > 0 for t in d) else 'worse' if r['net'] < b['net'] else 'noise'
        r.update(z=z, d=d, dl4=l4, vd=vd)
        rows.append('| %s | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f %% | %.1f | %+.1f | %.0f |' % (r['nm'], r['net'], r['net'] - b['net'], z, *d, l4, r['w'], r['sdm'], r['mx'], r['dd']))
    out += ['## MGC 3m -- %s: %d setups; live stop net %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, win %.0f %%, worst %.1f, max DD %.0f' % (fn, b['n'], b['net'], *b['th'], b['l4'], b['w'], b['mx'], b['dd']), '',
            '| Stop | Net | Δ vs live stop | z | Δ by third | Δ last 4 wk | Win % | Avg stop pts | Worst trade | Max DD |', '|---|---|---|---|---|---|---|---|---|---|'] + rows + ['']
    best = sorted(res[1:], key=lambda r: -r['net'])[:4]
    top.append('**%s** (%d setups, live stop %+.0f, max DD %.0f): ' % (fn, b['n'], b['net'], b['dd']) + '; '.join('%s %+.0f (z %+.1f, %+.0f / %+.0f / %+.0f, l4 %+.0f, worst %.1f, %s)' % (r['nm'], r['net'] - b['net'], r['z'], *r['d'], r['dl4'], r['mx'], r['vd']) for r in best))
    top.append('')
    print('done', fn, file=sys.stderr, flush=True)
rep = '\n'.join(out[:2] + top + out[2:]); open('mgc_slx_report.md', 'w').write(rep); print(rep)
