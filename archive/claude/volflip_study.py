"""Volume Strong Flip (CBC Engine idea 5) + EMA200-vs-VWAP watch -- MES 3m and MGC 3m. Weekly, Sundays 2 pm ET.
Replay Jan 5 -> now, CBC engine setups, live gates and live exits (MES 3m SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1;
MGC 3m SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6, 0 % at TP1 + BE, closed by the HTF flip = "FLIP 0 %").
VOLUME STRONG FLIP: keep a setup only when volume > the average volume of the previous N candles (N = 20 / 50 / 100; 50 = CBC Engine default).
  (a) the 3m setup candle, (b) the 15m candle of the HTF flip (flip setups only; other setups kept), (c) 3m setup candle OR any of the
  last 3 candles, (d) volume AND the sweep-and-close strong-flip candle, (e) volume gate + EMA200 vs VWAP.
ENVIRONMENT WATCH: longs only when EMA200 > VWAP, shorts only when EMA200 < VWAP (and 3m EMA20 vs VWAP) -- tracked weekly toward 3 runs.
Gates are entry filters: a skipped setup can change later setups (one setup at a time, cooldown). Net after costs (MES 0.50, MGC 0.22).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds AND last 4 wk not negative; promising = z >= 1 and all thirds."""
import sys, datetime as D, numpy as np, pandas as pd
import combo_study as cb, chop_sim as cs, late_study as ls
from zoneinfo import ZoneInfo
X = {'MES': dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, p=1.0, be=False, c=.5, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7)),
     'MGC': dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, p=0.0, be=True, c=.22, q=dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9))}
now = D.datetime.now(ZoneInfo('America/New_York')).strftime('%Y-%m-%d %H:%M ET')
out = ['# Volume Strong Flip + EMA200-vs-VWAP watch -- %s' % now, '', __doc__, '']; top = ['## Overview', '', '| Chart | Variant | Setups | Δ | z | Δ thirds | Δ last 4 wk | Verdict |', '|---|---|---|---|---|---|---|---|']
for sym in ('MES', 'MGC'):
    x = X[sym]; B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B); G = cb.CH[sym][2]
    C, H, L = s.C, s.H, s.L; V = B.v.fillna(0).values.astype(float); T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    VA = {N: pd.Series(V).shift(1).rolling(N, min_periods=N).mean().values for N in (20, 50, 100)}
    g = pd.DataFrame({'k': B.hk.values, 'h': H, 'l': L, 'c': C, 'v': V, 'i': np.arange(s.n)}).groupby('k', sort=False).agg(h=('h', 'max'), l=('l', 'min'), c=('c', 'last'), v=('v', 'sum'), last=('i', 'max'))
    gv = g.v.values; gi = g['last'].values; gl, gh, gc = g.l.values, g.h.values, g.c.values
    HVA = {N: pd.Series(gv).shift(1).rolling(N, min_periods=N).mean().values for N in (20, 50, 100)}
    hv = {N: {gi[k]: gv[k] > HVA[N][k] for k in range(len(g)) if HVA[N][k] == HVA[N][k]} for N in (20, 50, 100)}
    def vol3(i, N): a = VA[N][i]; return a == a and V[i] > a
    def volH(i, N): return hv[N].get(i, True)
    def strong3(i, lg): return (L[i] < L[i - 1] and C[i] > H[i - 1]) if lg else (H[i] > H[i - 1] and C[i] < L[i - 1])
    def env(i, lg, e): return (e[i] > s.vw[i]) == lg
    def score(R):
        v = []; K = {}; th = [0, 0, 0]; l4 = 0
        for r in R:
            res = r['res'] - x['c']; v.append(res); K[(r['i'], r['lg'])] = res; th[0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2] += res
            if s.T[r['i']] >= t4: l4 += res
        v = np.array(v); return dict(n=len(v), net=v.sum(), sd=v.std(), th=th, l4=l4, w=100 * (v > 0).mean(), K=K)
    run = lambda f: score(s.run(lambda d: cs.cur_rule(d) and f(d), q=x['q'], gates=G))
    L0 = run(lambda d: True); vok = 100 * (V[300:] > 0).mean()
    rows = []
    def add(nm, a):
        ch = sum(1 for k in set(a['K']) | set(L0['K']) if abs(a['K'].get(k, 1e9) - L0['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - L0['net']) / (L0['sd'] * np.sqrt(ch)); d = [p - q for p, q in zip(a['th'], L0['th'])]; l4 = a['l4'] - L0['l4']
        vd = 'robust' if z >= 2 and all(t > 0 for t in d) and l4 >= 0 else 'robust except last 4 wk' if z >= 2 and all(t > 0 for t in d) else 'promising' if z >= 1 and all(t > 0 for t in d) else 'worse' if a['net'] < L0['net'] else 'noise'
        rows.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f %% | %s |' % (nm, a['n'], a['net'], a['net'] - L0['net'], z, *d, l4, a['w'], vd))
        if nm != '**Current (live)**': top.append('| %s 3m | %s | %d | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %s |' % (sym, nm, a['n'], a['net'] - L0['net'], z, *d, l4, vd))
    add('**Current (live)**', L0)
    for N in (20, 50, 100): add('5a. Volume > avg %d: 3m setup candle' % N, run(lambda d, N=N: vol3(d['i'], N)))
    for N in (20, 50, 100): add('5b. Volume > avg %d: 15m flip candle (flip setups)' % N, run(lambda d, N=N: d['trig'] != 'flip' or volH(d['i'], N)))
    add('5c. Volume > avg 50: setup candle or one of last 3', run(lambda d: any(vol3(d['i'] - k, 50) for k in range(4))))
    add('5d. Volume > avg 50 AND sweep-close strong candle', run(lambda d: vol3(d['i'], 50) and strong3(d['i'], d['lg'])))
    add('5e. Volume > avg 50 (3m) + EMA200 vs VWAP', run(lambda d: vol3(d['i'], 50) and env(d['i'], d['lg'], s.e200)))
    add('W1. Watch: EMA200 vs VWAP', run(lambda d: env(d['i'], d['lg'], s.e200)))
    add('W2. Watch: 3m EMA20 vs VWAP', run(lambda d: env(d['i'], d['lg'], s.e20)))
    out += ['## %s 3m -- current: %d setups, net %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, win %.0f %% (volume present on %.0f %% of candles)' % (sym, L0['n'], L0['net'], *L0['th'], L0['l4'], L0['w'], vok), '',
            '| Variant | Setups | Net | Δ | z | Δ by third | Δ last 4 wk | Win % | Verdict |', '|---|---|---|---|---|---|---|---|---|'] + rows + ['']
    print('done', sym, file=sys.stderr, flush=True)
rep = '\n'.join(out[:4] + top + [''] + out[4:]); open('volflip_report.md', 'w').write(rep); print('\n'.join(top))
