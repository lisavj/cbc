#!/usr/bin/env python3
"""Exit ideas beyond the plain time-based TP cut -- 11/06/2026, MES 3m + MGC 3m (live settings, replay Jan 5 -> now).
 1 VOL: time-based TP cut (after X min TP1 -> Y %) ONLY while ATR / ATR(100) >= r (high-volatility regime) -- X 21 / Y 70 %
 2 LOCK: before TP1, once the best move (MFE) reaches a x TP1, raise the stop to Entry + b x TP1 (profit lock)
 3 STALL: before TP1, after MFE >= 50 % of TP1, exit at the close when no new best price for N candles
 4 LOSER: before TP1, exit at the close after X min when the trade is still against Entry by >= k x ATR
All other exits unchanged. z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds."""
import numpy as np, pandas as pd, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

class ECase(ls.LCase):
    P = None
    def sim1(s, i, lg, q, stop_at):
        P = s.P
        if not P: return m.MCase.sim1(s, i, lg, q, stop_at)
        C, H, L, O = s.C, s.H, s.L, s.O; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False; mfe = 0.0; lastnew = i
        k = P[0]; vol_ok = k == 'vol' and s.arel[i] >= P[3]
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and k == 'vol' and vol_ok and (j - i) * s.tf > P[1]:
                red = en + g * P[2] * tpd
                if (O[j] >= red) if lg else (O[j] <= red): return g * (O[j] - en), j, 'TPx'
                if (H[j] >= red) if lg else (L[j] <= red): return P[2] * tpd, j, 'TPx'
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            else:
                fav = g * ((H[j] if lg else L[j]) - en)
                if fav > mfe + 1e-9: mfe = fav; lastnew = j
                if k == 'lock' and mfe >= P[1] * tpd:
                    ls_ = en + g * P[2] * tpd; sl = max(sl, ls_) if lg else min(sl, ls_)
                if k == 'stall' and mfe >= .5 * tpd and j - lastnew >= P[1]:
                    return g * (C[j] - en), j, 'stall'
                if k == 'loser' and (j - i) * s.tf >= P[1] and g * (C[j] - en) <= -P[2] * A:
                    return g * (C[j] - en), j, 'loser'
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

CH = [('MES 3m', 'MES', dict(m.LIVE, tp=2.0), dict(R5=1, X4=0, MTF=0)), ('MGC 3m', 'MGC', ls.MGCX, dict(R5=1, X4=1, MTF=0))]
V = [('1 VOL', ('vol', 21, .70, r), 'cut to 70 %% after 21 min while ATR/ATR100 >= %.1f' % r) for r in (0.0, 1.0, 1.2, 1.5)] + \
    [('1 VOL', ('vol', 24, .70, r), 'cut to 70 %% after 24 min while ATR/ATR100 >= %.1f' % r) for r in (1.2,)] + \
    [('2 LOCK', ('lock', a, b), 'MFE >= %d %% of TP1 -> stop to Entry + %d %%' % (a * 100, b * 100)) for a, b in ((.5, 0), (.5, .25), (.75, 0), (.75, .25), (.75, .5), (.9, .5))] + \
    [('3 STALL', ('stall', n), 'MFE >= 50 %% TP1, no new best for %d candles -> exit' % n) for n in (3, 5, 8, 12)] + \
    [('4 LOSER', ('loser', x, k), 'after %d min, still >= %.1f ATR against -> exit' % (x, k)) for x, k in ((15, .5), (30, 0.0), (30, .5), (45, 0.0), (45, .5), (60, .5))]

def main():
    out = ['# Exit ideas beyond the time-based TP cut — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for nm, sym, q, G in CH:
        B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
        s = ECase(sym, 3, B); s.arel = s.atr / pd.Series(s.atr).rolling(100).mean().values
        T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
        th = lambda r: [sum(x['res'] for x in r if (0 if s.T[x['i']] < cuts[0] else 1 if s.T[x['i']] < cuts[1] else 2) == k) for k in range(3)]
        def run(P):
            ECase.P = P; return s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
        b = run(None); bv = [x['res'] for x in b]; bn = sum(bv); sd = float(np.std(bv)) or 1; bt = th(b); b4 = sum(x['res'] for x in b if s.T[x['i']] >= t4)
        out += ['## %s — current exits net %+.0f (%d setups)' % (nm, bn, len(b)), '',
                '| Idea | Variant | Net | Δ | z | Δ by third | Last 4 wk Δ | Setups changed | Verdict |', '|---|---|---|---|---|---|---|---|---|']
        for grp, P, desc in V:
            r = run(P); v = [x['res'] for x in r]; net = sum(v)
            bm = {(x['i'], x['lg']): x['res'] for x in b}; rm = {(x['i'], x['lg']): x['res'] for x in r}
            ch = (len(bm.keys() ^ rm.keys()) + sum(1 for k_ in bm.keys() & rm.keys() if abs(bm[k_] - rm[k_]) > 1e-9)) or 1
            z = (net - bn) / (sd * np.sqrt(ch)); dth = [a_ - c_ for a_, c_ in zip(th(r), bt)]; b3 = all(x > 0 for x in dth)
            d4 = sum(x['res'] for x in r if s.T[x['i']] >= t4) - b4
            vd = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < bn else 'noise'
            ne = sum(1 for x in r if x['why'] in ('TPx', 'stall', 'loser'))
            out.append('| %s | %s | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.1f | %d | %s |' % (grp, desc, net, net - bn, z, *dth, d4, ch, vd))
            if vd in ('robust', 'promising'): summ.append('%s %s: %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f (%s)' % (nm, desc, net - bn, z, *dth, d4, vd))
        out.append('')
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    main()
