"""TP1 % vs HTF CBC flip exits, and combos -- MES 3m / MGC 3m -- replay Jan 5 -> now (CBC engine setups, live gates). Weekly (Sat).
CBC v10.95 inputs: "...close at TP1 (%) per symbol/timeframe" (any %) and "...trail x ATR per symbol/timeframe" (0 = FLIP: BE then HTF flip only).
Each setup keeps its live SL1 / TP1 distances (MES SL1 3 ATR min 5, TP1 1.75 ATR; MGC SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6).
A setup also always ends at 16:00 or when CBC draws the next setup. Runner = the part not closed at TP1. Exit families:
  TRAIL   x % at TP1, runner: BE + ATR trail (MES 1.7 / MGC 3.5) or the HTF CBC flip against   (= live CBC exits)
  FLIP    x % at TP1, runner: BE, then ONLY the HTF CBC flip against (no trail)
  FLIP-noBE  same without moving the stop to breakeven
  FLIP+SL  no TP at all: SL1 or the HTF CBC flip against (the bot's flip-only exit)
Net after costs (MES 0.50, MGC 0.22). z vs live = Δ / (SD x sqrt(setups changed))."""
import numpy as np
import combo_study as cb, chop_sim as cs, late_study as ls
COST = {'MES': .5, 'MGC': .22}
X = {'MES': dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, tr=1.7), 'MGC': dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, tr=3.5)}
out = [__doc__, '']
for sym in ('MES', 'MGC'):
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B); G = cb.CH[sym][2]; s.TX, s.TY = (0, 0.0); s.ACT = None
    R = s.run(lambda d: cs.cur_rule(d), q=cs.EXIT[(sym, 3)], gates=G)
    ST = [(r['i'], r['lg'], R[k + 1]['i'] if k + 1 < len(R) else -1) for k, r in enumerate(R)]
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000; c = COST[sym]; x = X[sym]
    C, H, L = s.C, s.H, s.L
    def sim(i, lg, stop, p, mode):
        en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(x['sl'] * A, x['cap']), x['mn']); tpd = min(x['tp'] * A, x['tcap'])
        sl = en - g * sd; t1 = en + g * tpd; hit = False; usetp = mode != 'FLIP+SL'
        for j in range(i + 1, s.n):
            if (L[j] <= sl) if lg else (H[j] >= sl):
                rem = g * (sl - en); return p * tpd + (1 - p) * rem if hit else rem
            if usetp and not hit and ((H[j] >= t1) if lg else (L[j] <= t1)):
                hit = True
                if p >= 1: return tpd
                if mode in ('TRAIL', 'FLIP'): sl = max(sl, en) if lg else min(sl, en)
            if hit and mode == 'TRAIL':
                ns = C[j] - g * x['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop:
                rem = g * (C[j] - en); return p * tpd + (1 - p) * rem if hit else rem
        return None
    def go(p, mode):
        v = []; th = [0, 0, 0]; l4 = 0; K = {}
        for (i, lg, stop) in ST:
            r = sim(i, lg, stop, p, mode)
            if r is None: continue
            r -= c; v.append(r); K[(i, lg)] = r; th[0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2] += r
            if s.T[i] >= t4: l4 += r
        v = np.array(v); eq = np.cumsum(v)
        return dict(n=len(v), net=v.sum(), sd=v.std(), th=th, l4=l4, w=100 * (v > 0).mean(), dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K=K)
    lp, lm = (0.0, 'FLIP') if sym == 'MGC' else (1.0, 'TRAIL')   # CBC v10.96 defaults: MGC 3m 0 % + trail 0 (FLIP 0 %), MES 3m 100 %
    L0 = go(lp, lm)
    out += ['## %s 3m -- %d setups; live = %s %d %% at TP1 (CBC v10.96 defaults: MES 3m TRAIL 100 %%, MGC 3m FLIP 0 %% = 0 %% at TP1 + trail 0)' % (sym, L0['n'], lm, lp * 100), '',
            '| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |', '|---|---|---|---|---|---|---|---|---|']
    rows = []
    for mode in ('TRAIL', 'FLIP', 'FLIP-noBE'):
        for p in (0, .25, .5, .75, 1.0):
            if p == 1.0 and mode != 'TRAIL': continue
            rows.append((mode, p, go(p, mode)))
    rows.append(('FLIP+SL', None, go(0, 'FLIP+SL')))
    for mode, p, a in rows:
        z = (a['net'] - L0['net']) / (L0['sd'] * np.sqrt(sum(1 for k in a['K'] if abs(a['K'][k] - L0['K'].get(k, 1e9)) > 1e-9) or 1))
        lab = '-' if p is None else '%d %%' % (p * 100)
        live = mode == lm and p == lp
        out.append('| %s | %s | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f %% | %.0f |' % ('**' + mode + ' (live)**' if live else mode, lab, a['net'], a['net'] - L0['net'], z, *a['th'], a['l4'], a['w'], a['dd']))
    b = max(rows, key=lambda r: r[2]['net']); ok = [r for r in rows if all(t > tt for t, tt in zip(r[2]['th'], L0['th']))]
    out += ['', 'Largest: %s %s = %+.0f. Better than live in all three thirds: %s' % (b[0], '-' if b[1] is None else '%d %%' % (b[1] * 100), b[2]['net'],
            ', '.join('%s %s (%+.0f)' % (m, '-' if p is None else '%d %%' % (p * 100), a['net']) for m, p, a in ok) or 'none'), '']
open('tp1flip_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
