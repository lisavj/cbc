"""MGC 3m SL1 size under the v10.96 exit (FLIP 0 %: nothing closed at TP1, stop to breakeven at TP1, then closed by the HTF CBC
flip against / 16:00 / next setup). Replay Jan 5 -> now (CBC engine setups, live gates), TP1 = 1.7 ATR cap 6 (the breakeven
trigger). SL1 = x ATR, minimum 5 pts, cap (Max ATR SL1) 7 (live) / 10 / none. Net after 0.22 cost. z vs live (1.7 ATR, cap 7).
Also the same grid under the old exit (TRAIL 50 %, trail 3.5) for reference."""
import numpy as np
import combo_study as cb, chop_sim as cs, late_study as ls
B = ls.load('MGC', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase('MGC', 3, B); G = cb.CH['MGC'][2]; s.TX, s.TY = (0, 0.0); s.ACT = None
R = s.run(lambda d: cs.cur_rule(d), q=cs.EXIT[('MGC', 3)], gates=G)
ST = [(r['i'], r['lg'], R[k + 1]['i'] if k + 1 < len(R) else -1) for k, r in enumerate(R)]
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000; c = .22
C, H, L = s.C, s.H, s.L
def sim(i, lg, stop, slm, mn, cap, p, mode):
    en = C[i]; A = s.atr[i]; g = 1 if lg else -1
    sd = max(min(slm * A, cap), mn); tpd = min(1.7 * A, 6); sl = en - g * sd; t1 = en + g * tpd; hit = False
    for j in range(i + 1, s.n):
        if (L[j] <= sl) if lg else (H[j] >= sl):
            rem = g * (sl - en); return (p * tpd + (1 - p) * rem if hit else rem), sd
        if not hit and ((H[j] >= t1) if lg else (L[j] <= t1)):
            hit = True; sl = max(sl, en) if lg else min(sl, en)
        if hit and mode == 'TRAIL':
            ns = C[j] - g * 3.5 * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
        if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop:
            rem = g * (C[j] - en); return (p * tpd + (1 - p) * rem if hit else rem), sd
    return None, sd
def go(slm, mn, cap, p, mode):
    v = []; K = {}; th = [0, 0, 0]; l4 = 0; sds = []
    for (i, lg, stop) in ST:
        r, sd = sim(i, lg, stop, slm, mn, cap, p, mode)
        if r is None: continue
        r -= c; v.append(r); K[(i, lg)] = r; sds.append(sd); th[0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2] += r
        if s.T[i] >= t4: l4 += r
    v = np.array(v); eq = np.cumsum(v)
    return dict(net=v.sum(), sd=v.std(), th=th, l4=l4, w=100 * (v > 0).mean(), dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K=K, avgsd=np.mean(sds), n=len(v))
out = [__doc__, '', 'Setups: %d. Median ATR %.2f pts (1.7 ATR = %.1f; cap 7 binds when ATR > %.2f).' % (len(ST), np.nanmedian(s.atr[[i for i, _, _ in ST]]), 1.7 * np.nanmedian(s.atr[[i for i, _, _ in ST]]), 7 / 1.7), '']
for mode, p, lab in (('FLIP', 0.0, 'FLIP 0 % (v10.96 live)'), ('TRAIL', .5, 'TRAIL 50 % + trail 3.5 (old)')):
    L0 = go(1.7, 5, 7, p, mode)
    out += ['## %s -- live SL1 1.7 ATR / min 5 / cap 7: net %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f' % (lab, L0['net'], *L0['th'], L0['l4'], L0['dd']), '',
            '| SL1 x ATR | Cap | Avg stop pts | Net | Δ vs live | z | Δ by third | Δ last 4 wk | Win % | Max DD |', '|---|---|---|---|---|---|---|---|---|---|']
    for cap in (7, 10, 1e9):
        for slm in (1.0, 1.3, 1.5, 1.7, 2.0, 2.5, 3.0, 3.5):
            a = go(slm, 5, cap, p, mode)
            ch = sum(1 for k in a['K'] if abs(a['K'][k] - L0['K'].get(k, 1e9)) > 1e-9) or 1
            z = (a['net'] - L0['net']) / (L0['sd'] * np.sqrt(ch)) if ch > 1 else 0
            d = [x - y for x, y in zip(a['th'], L0['th'])]
            tag = ' **(live)**' if (slm == 1.7 and cap == 7) else (' ✓' if all(x > 0 for x in d) and a['l4'] >= L0['l4'] else '')
            out.append('| %.1f%s | %s | %.1f | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f %% | %.0f |' % (slm, tag, 'none' if cap > 100 else '%d' % cap, a['avgsd'], a['net'], a['net'] - L0['net'], z, *d, a['l4'] - L0['l4'], a['w'], a['dd']))
    out.append('')
out.append('✓ = better than live in all three thirds and in the last 4 weeks.')
open('mgc_sl_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
