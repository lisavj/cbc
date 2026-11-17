"""③ Trade Setup Filters vs current -- MES 3m and MGC 3m, CBC v10.97 -- 11/14/2026.
One change at a time on top of each chart's live settings: ER chop 0.23 + breakout exception 3 bars ON; range gate 24 bars / 20 % / 5 ATR
(MES 3m, MGC 3m); VWAP stretch 4 ATR (MGC 3m); everything else OFF. Replay Jan 5 -> now, CBC engine setups (late_study / combo_study), live exits
(MES 3m SL1 3 ATR min 5, TP1 1.75, 100 % at TP1; MGC 3m SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, 0 % at TP1 + BE, closed by the HTF flip).
Chop measures use the 12-bar "Chop filters length": Choppiness Index(12), ADX(12), candles in the last 12 whose close crossed EMA20 or VWAP, |HTF EMA20 now - 12 bars ago| / ATR
(as the Pine tooltip), 12-bar high-low range / ATR. Net after costs (MES 0.50, MGC 0.22). Entry filters: a skipped setup can change later setups.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, better in all three thirds and last 4 wk >= 0; promising = z >= 1 and all thirds.
Note: the combo_study engine never applied the MGC VWAP stretch gate to its main setups (X4 always False in mes3_ema_grid gen),
so earlier MGC 3m replays (cbce, volflip, tp1flip: 1602 setups) ran without it; here it is applied (current = 1136 setups).
Not modelled: mixed chart structure, skip-the-breakout-candle, room to the first opposing level / OB (see room_study), the 2m-only lists."""
import sys, numpy as np, pandas as pd
import combo_study as cb, chop_sim as cs, late_study as ls
X = {'MES': dict(c=.5, cap=1e9, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7), r5=5, x4=None),
     'MGC': dict(c=.22, cap=7.0, q=dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9), r5=5, x4=4.0)}
out = [__doc__, '']; top = ['## Candidates (promising or better)', '']
for sym in ('MES', 'MGC'):
    x = X[sym]; B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B)
    C, H, L = s.C, s.H, s.L; A = s.atr; n = 12; T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    S = pd.Series; pc = S(C).shift(1); tr = pd.concat([S(H) - S(L), (S(H) - pc).abs(), (S(L) - pc).abs()], axis=1).max(axis=1)
    hh, ll = S(H).rolling(n).max(), S(L).rolling(n).min()
    CHOP = (100 * np.log10(tr.rolling(n).sum() / (hh - ll)) / np.log10(n)).values
    up, dn = S(H).diff(), -S(L).diff(); pdm = np.where((up > dn) & (up > 0), up, 0.); ndm = np.where((dn > up) & (dn > 0), dn, 0.)
    atw = tr.ewm(alpha=1 / n, adjust=False).mean(); pdi = 100 * S(pdm).ewm(alpha=1 / n, adjust=False).mean() / atw; ndi = 100 * S(ndm).ewm(alpha=1 / n, adjust=False).mean() / atw
    ADX = (100 * (pdi - ndi).abs() / (pdi + ndi)).ewm(alpha=1 / n, adjust=False).mean().values
    XS = s.xs  # candles in the last 12 whose close crossed the chart EMA20 or VWAP (Pine tooltip; chop_sim)
    h20 = B.h20.values.astype(float); SLP = np.abs(h20 - np.roll(h20, n)) / A; RNG = ((hh - ll).values) / A
    hh24, ll24 = S(H).rolling(24).max().values, S(L).rolling(24).min().values; FL = S((s.hf != 0).astype(float)).rolling(40).sum().values
    def ok(d, P):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
        if P['er'] > 0 and not cs.cur_rule(d, thr=P['er'], flip_thr=P['er'], bo=P['bo']): return False
        if P['r5']:
            w = hh24[i] - ll24[i]
            if w > 0 and w / a < P['r5'] and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        if P['x4'] and g * (C[i] - s.vw[i]) / a > P['x4']: return False
        if P.get('chop') and CHOP[i] > P['chop']: return False
        if P.get('adx') and ADX[i] < P['adx']: return False
        if P.get('xs') and XS[i] >= P['xs']: return False
        if P.get('slope') and SLP[i] < P['slope']: return False
        if P.get('rng') and RNG[i] < P['rng']: return False
        if P.get('fl') and FL[i] >= P['fl']: return False
        if P.get('nv'):
            dv = g * (C[i] - s.vw[i])
            if -3 <= dv <= 2 and not ((L[i] >= s.vw[i] + P['nv']) if lg else (H[i] <= s.vw[i] - P['nv'])): return False
        if P.get('ne') and -3 <= g * (C[i] - s.e200[i]) <= 2: return False
        if P.get('vc') and x['cap'] < P['vc'] * a: return False
        if P.get('va') and s.atrrel[i] > P['va']: return False
        if P.get('env') and (s.e200[i] > s.vw[i]) != lg: return False
        return True
    def run(P):
        R = s.run(lambda d: ok(d, P), q=x['q'], gates=dict(R5=0, X4=0, MTF=0)); v = []; K = {}; th = [0, 0, 0]; l4 = 0
        for r in R:
            res = r['res'] - x['c']; v.append(res); K[(r['i'], r['lg'])] = res; th[0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2] += res
            if s.T[r['i']] >= t4: l4 += res
        v = np.array(v); return dict(n=len(v), net=v.sum(), sd=v.std(), th=th, l4=l4, w=100 * (v > 0).mean(), avg=v.mean(), K=K)
    base = dict(er=.23, bo=True, r5=x['r5'], x4=x['x4']); L0 = run(base)
    V = [('ER filter OFF', dict(er=0)), ('ER threshold 0.18', dict(er=.18)), ('ER threshold 0.20', dict(er=.20)), ('ER threshold 0.26', dict(er=.26)), ('ER threshold 0.30', dict(er=.30)),
         ('ER breakout exception OFF', dict(bo=False)),
         ('Choppiness Index > 61.8 block', dict(chop=61.8)), ('Choppiness Index > 58 block', dict(chop=58)), ('ADX < 20 block', dict(adx=20)), ('ADX < 15 block', dict(adx=15)),
         ('EMA20 / VWAP crosses >= 4 block', dict(xs=4)), ('EMA20 / VWAP crosses >= 6 block', dict(xs=6)),
         ('HTF EMA20 slope < 0.2 ATR block', dict(slope=.2)), ('HTF EMA20 slope < 0.3 ATR block (default value)', dict(slope=.3)), ('HTF EMA20 slope < 0.5 ATR block', dict(slope=.5)), ('HTF EMA20 slope < 0.8 ATR block', dict(slope=.8)),
         ('N-bar range < 2 ATR block', dict(rng=2)), ('N-bar range < 3 ATR block', dict(rng=3)),
         ('VWAP stretch 3 ATR', dict(x4=3.0)), ('VWAP stretch 4 ATR', dict(x4=4.0)), ('VWAP stretch 6 ATR', dict(x4=6.0)), ('VWAP stretch OFF', dict(x4=None)),
         ('Range gate OFF', dict(r5=None)), ('Range gate 4 ATR', dict(r5=4)), ('Range gate 5 ATR', dict(r5=5)), ('Range gate 6 ATR', dict(r5=6)),
         ('Block after HTF flips >= 2 in 8', dict(fl=2)), ('Block after HTF flips >= 3 in 8', dict(fl=3)), ('Block after HTF flips >= 4 in 8', dict(fl=4)),
         ('Block if VWAP -3 / +2 pts (unless candle 1 pt beyond)', dict(nv=1.0)), ('Block if EMA200 -3 / +2 pts', dict(ne=True)),
         ('Environment: EMA200 vs VWAP (v10.97)', dict(env=True)),
         ('Skip if Max ATR SL1 cap < 1.5 x ATR', dict(vc=1.5)), ('Skip while ATR > 1.8 x ATR(100)', dict(va=1.8))]
    rows = []
    for nm, ch in V:
        P = dict(base); P.update(ch)
        if P == base: continue
        if nm.startswith('Skip if Max') and x['cap'] > 100: rows.append('| %s | — | | | | | | | | | n/a (no cap on %s 3m) |' % (nm, sym)); continue
        a = run(P); chg = sum(1 for k in set(a['K']) | set(L0['K']) if abs(a['K'].get(k, 1e9) - L0['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - L0['net']) / (L0['sd'] * np.sqrt(chg)); d = [p - q for p, q in zip(a['th'], L0['th'])]; l4 = a['l4'] - L0['l4']
        vd = 'robust' if z >= 2 and all(t > 0 for t in d) and l4 >= 0 else 'robust except last 4 wk' if z >= 2 and all(t > 0 for t in d) else 'promising' if z >= 1 and all(t > 0 for t in d) else 'robustly worse' if z <= -2 and all(t < 0 for t in d) else 'worse' if a['net'] < L0['net'] else 'noise'
        rows.append('| %s | %d | %.0f %% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %s |' % (nm, a['n'], a['w'], a['net'], a['avg'], a['net'] - L0['net'], z, *d, l4, vd))
        if vd.startswith('robust') and 'worse' not in vd or vd == 'promising': top.append('- %s 3m: %s → %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, avg %+.2f vs %+.2f (%s)' % (sym, nm, a['net'] - L0['net'], z, *d, l4, a['avg'], L0['avg'], vd))
        print(sym, nm, file=sys.stderr, flush=True)
    out += ['## %s 3m -- current: %d setups, win %.0f %%, net %+.0f, avg %+.2f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f' % (sym, L0['n'], L0['w'], L0['net'], L0['avg'], *L0['th'], L0['l4']), '',
            '| Change (one at a time) | Setups | Win % | Net | Avg/setup | Δ vs current | z | Δ by third | Δ last 4 wk | Verdict |', '|---|---|---|---|---|---|---|---|---|---|'] + rows + ['']
rep = '\n'.join(out[:2] + top + [''] + out[2:]); open('tsf_report.md', 'w').write(rep); print(rep)
