#!/usr/bin/env python3
"""Time-based TP1 reduction study, MES 3m and MGC 3m -- 11/06/2026.
Question: once a setup has been open X minutes without reaching TP1, should TP1 be pulled in to Y % of its distance from
Entry (the trade then closes as soon as price touches that new level), instead of waiting for the full TP1 / stop / flip?
Variants: X = 9, 15, 30, 45, 60, 90, 120 min; Y = 25, 50, 75, 90 %. Mode A "modified TP" = new limit at Entry + Y % x TP1
distance from the candle after X minutes (fills intrabar when the high / low reaches it; if price is already past it, fills at
that candle's open). Mode B "close at candle" = close at the candle close once X minutes have passed and the close is at least
Y % of the way to TP1. Before TP1 only; the stop, flip, 16:00 and new-setup exits are unchanged.
Replay (chop_sim rules, late window 1, NY OR block 30) on live settings: MES 3m 9 / 20, range gate, SL1 3 x ATR min 5 /
TP1 2 x ATR / close at TP1 by time of day (80 % + BE + trail inside 06-16 and 18-22:30, else 100 %); MGC 3m range gate +
VWAP stretch 4 ATR, SL1 1.7 ATR min 5 cap 7 / TP1 1.7 ATR cap 6 / 80 % + BE + trail 1.7. A reduced TP closes 100 %.
Jan 5 -> now. ~50 % exact match with live setups: compare rows, not totals. z = change / (SD x sqrt(setups changed));
robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 tptime_study.py"""
import numpy as np, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

class TCase(ls.LCase):
    X = 0; Y = 0.0; MODE = 'A'
    def sim1(s, i, lg, q, stop_at):
        if s.X <= 0: return m.MCase.sim1(s, i, lg, q, stop_at)
        C, H, L, O = s.C, s.H, s.L, s.O; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        nb = int(np.ceil(s.X / s.tf)); red = en + g * s.Y * tpd
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and s.MODE == 'A' and j - i > nb:     # reduced TP active from the candle after X minutes
                if (O[j] >= red) if lg else (O[j] <= red): return g * (O[j] - en), j, 'TPx'
                if (H[j] >= red) if lg else (L[j] <= red): return s.Y * tpd, j, 'TPx'
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            if not hit and s.MODE == 'B' and j - i >= nb and g * (C[j] - en) >= s.Y * tpd:
                return g * (C[j] - en), j, 'TPx'
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

CH = [('MES 3m', 'MES', dict(m.LIVE, tp=2.0), dict(R5=1, X4=0, MTF=0)), ('MGC 3m', 'MGC', ls.MGCX, dict(R5=1, X4=1, MTF=0))]
XS = (9, 15, 30, 45, 60, 90, 120); YS = (.25, .5, .75, .9)

def main():
    out = ['# Time-based TP1 reduction — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for nm, sym, q, G in CH:
        B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
        s = TCase(sym, 3, B)
        e9 = m.ema(s.C, 9)
        T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
        th = lambda res: [sum(r['res'] for r in res if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        def run(x, y, mode):
            TCase.X, TCase.Y, TCase.MODE = x, y, mode
            return s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
        b = run(0, 0, 'A'); bv = [r['res'] for r in b]; bn = sum(bv); sd = float(np.std(bv)) or 1; bt = th(b)
        b4 = sum(r['res'] for r in b if s.T[r['i']] >= t4)
        nev = sum(1 for r in b if r['why'] not in ('TP1', 'trail')) ; ntp = sum(1 for r in b if r['why'] in ('TP1', 'trail'))
        dur = np.median([(r['j'] - r['i']) * 3 for r in b])
        out += ['## %s — current exits: %d setups, net %+.0f, win %d%%, TP1 reached %d, median time in trade %d min' % (
            nm, len(b), bn, round(100 * sum(x > 0 for x in bv) / max(1, sum(x != 0 for x in bv))), ntp, dur), '']
        for mode, mn in (('A', 'A. Modified TP (new limit at Y % after X min)'), ('B', 'B. Close at the candle close (after X min, close >= Y % of TP1)')):
            out += ['**%s** — Δ net vs current (✱ both halves better, T all three thirds better; z)' % mn, '',
                    '| X min \\ Y | ' + ' | '.join('%d %%' % (y * 100) for y in YS) + ' |', '|---|' + '---|' * len(YS)]
            best = []
            for x in XS:
                cells = []
                for y in YS:
                    r = run(x, y, mode); v = [t['res'] for t in r]; net = sum(v)
                    ch = sum(1 for a, c in zip(b, r) if abs(a['res'] - c['res']) > 1e-9) or 1
                    z = (net - bn) / (sd * np.sqrt(ch)); dth = [a - c for a, c in zip(th(r), bt)]
                    h = len(v) // 2; bh = len(bv) // 2
                    both = sum(v[:h]) > sum(bv[:bh]) and sum(v[h:]) > sum(bv[bh:])
                    t3 = all(d > 0 for d in dth)
                    cells.append('%+.0f%s%s (%+.1f)' % (net - bn, ' ✱' if both else '', ' T' if t3 else '', z))
                    best.append((net - bn, x, y, z, dth, sum(t['res'] for t in r if s.T[t['i']] >= t4) - b4,
                                 round(100 * sum(t > 0 for t in v) / max(1, sum(t != 0 for t in v))), sum(1 for t in r if t['why'] == 'TPx')))
                out.append('| %d | %s |' % (x, ' | '.join(cells)))
            best.sort(key=lambda k: -k[0])
            out += ['', 'Top 3: ' + '; '.join('X %d / Y %d %% → %+.0f (z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f, win %d %%, %d early exits)' % (
                x, y * 100, d, z, *dt, l4, w, ne) for d, x, y, z, dt, l4, w, ne in best[:3]), '']
            for d, x, y, z, dt, l4, w, ne in best:
                vd = 'robust' if z >= 2 and all(k > 0 for k in dt) else 'promising' if z >= 1 and all(k > 0 for k in dt) else None
                if vd: summ.append('%s mode %s X %d / Y %d %%: %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f (%s)' % (nm, mode, x, y * 100, d, z, *dt, l4, vd))
    out += ['## Candidates (robust / promising)', ''] + (['- ' + k for k in summ] if summ else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    main()
