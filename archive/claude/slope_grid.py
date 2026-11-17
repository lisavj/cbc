"""HTF EMA20 slope filter threshold grid 0.24-0.36 (step 0.03) -- MES 3m and MGC 3m, CBC EMA Slope branch -- 11/14/2026.
Slope = |15m EMA20 now - 12 chart bars ago| / ATR; block when below the threshold (all triggers). Branch default 0.3 on both charts.
MES 3m: ER 0.23 + breakout, range gate 24 / 20 % / 5 ATR; SL1 3 ATR min 5, TP1 1.75, 100 % at TP1; HTF CBC Flip setups ride to the
HTF flip back / SL1 / 16:00 / next setup. MGC 3m: same filters + VWAP stretch 4 ATR (fixed engine); SL1 1.7 ATR min 5 cap 7, TP1 1.7
cap 6, 0 % at TP1 + BE, closed by the HTF flip (FLIP 0 %). TV EMA20 from the bar feed (= project baselines). Replay Jan 5 -> now,
net after costs (MES 0.50, MGC 0.22). Δ vs 0.30. z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all thirds better, last 4 wk >= 0;
promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd, datetime as D
from zoneinfo import ZoneInfo
import chop_sim as cs, ema716_eng as eng
TZ = ZoneInfo('America/New_York'); TH = [float(a) for a in sys.argv[1].split(',')] if len(sys.argv) > 1 and ',' in sys.argv[1] else [0, .24, .27, .30, .33, .36]   # e.g. python3 slope_grid.py 0,0.30,0.39,0.42
CFG = {'MES': dict(c=.5, x4=False, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7), ride=True),
       'MGC': dict(c=.22, x4=True, q=dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9), ride=False)}
out = [__doc__, '']; summ = []
for sym in ('MES', 'MGC'):
    x = CFG[sym]; B = eng.load(sym, 3, '/tmp/%s3.pkl' % sym.lower()); eng.LCase.LATE = 1; eng.LCase.NYW = 30; s = eng.LCase(sym, 3, B)
    H, L, C, A, T, N = s.H, s.L, s.C, s.atr, s.T, s.n
    T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values
    h20 = B.h20.values.astype(float); SLP = np.abs(h20 - np.roll(h20, 12)) / A
    def ok(d, th):
        i, lg = d['i'], d['lg']; w = hh24[i] - ll24[i]
        if not cs.cur_rule(d): return False
        if w > 0 and w / A[i] < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        return not (th and SLP[i] < th)
    def flipsim(i, lg, stop):
        en = C[i]; g = 1 if lg else -1; sd = max(3 * A[i], 5); slv = en - g * sd
        for j in range(i + 1, N):
            if (L[j] <= slv) if lg else (H[j] >= slv): return -sd
            if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop: return g * (C[j] - en)
        return 0.
    def run(th):
        R = [dict(r) for r in s.run(lambda d: ok(d, th), q=x['q'], gates=dict(R5=0, X4=1 if x['x4'] else 0, MTF=0))]
        if x['ride']:
            for k, r in enumerate(R):
                if r['trig'] == 'flip': r['res'] = flipsim(r['i'], r['lg'], R[k + 1]['i'] if k + 1 < len(R) else -1)
        v = np.array([r['res'] - x['c'] for r in R]); eq = np.cumsum(v)
        th3 = [sum(r['res'] - x['c'] for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std(), th=th3, l4=sum(r['res'] - x['c'] for r in R if T[r['i']] >= t4),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), w=100 * (v > 0).mean(), K={(r['i'], r['lg']): r['res'] - x['c'] for r in R})
    S = {th: run(th) for th in TH}; b = S[min(S, key=lambda t: abs(t - .30))]
    out += ['## %s 3m' % sym, '', '| Slope threshold | Setups | Win % | Net | Avg | Δ vs 0.30 | z | Thirds | Δ by third | Last 4 wk | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for th in TH:
        a = S[th]; chg = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(chg)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
        vd = 'current' if abs(th - .30) < 1e-9 else 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
        out.append('| %s | %d | %.0f %% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %s |' % (
            'off (v10.97)' if th == 0 else '%.2f%s' % (th, ' (branch)' if abs(th - .30) < 1e-9 else ''), a['n'], a['w'], a['net'], a['avg'], a['net'] - b['net'], 0 if abs(th - .30) < 1e-9 else z, *a['th'], *d_, a['l4'], a['dd'], vd))
        if vd in ('robust', 'promising'): summ.append('- %s 3m slope %.2f: %+.0f vs 0.30, z %+.1f (%s)' % (sym, th, a['net'] - b['net'], z, vd))
    out.append('')
    print(sym, file=sys.stderr, flush=True)
out += ['## Candidates (robust / promising vs 0.30)', ''] + (summ or ['- none'])
open('slope_grid_report%s.md' % ('_' + sys.argv[1].replace(',', '_') if len(sys.argv) > 1 else ''), 'w').write('\n'.join(out)); print('\n'.join(out))
