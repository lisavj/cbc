#!/usr/bin/env python3
"""NY opening-range setup block length -- 11/05/2026.
CBC "No new setups during opening range (forming): NY" blocks every trigger 9:30-10:00 ET (the NY OR length, 30 min).
Would 15 min (9:30-9:45) be better? Windows tested: 0 (off), 10, 15, 20, 30 (current), 45 min. London / Asia blocks unchanged
(30 min). Also: setups that only exist with the block off, split by 15-min slot (9:30-9:45 / 9:45-10:00).
Engine: late_study LCase (mes3_ema_grid MCase + LTF late window 1). Charts on live settings (see late_study.py).
Usage: python3 orw_study.py   (needs chop_sim.py, mes3_ema_grid.py, late_study.py next to it)"""
import numpy as np, datetime as D
import chop_sim as cs, late_study as ls

CH = [(a, b, 3, c, d, e) for a, b, c, d, e in ls.CHARTS] + ls.CHARTS2
WIN = (0, 10, 15, 20, 30, 45)

def main():
    out = ['# NY opening-range setup block length — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    data = {}; summ = []
    for nm, sym, tf, sl, q, G in CH:
        if (sym, tf) not in data: data[(sym, tf)] = ls.load(sym, tf)
        B = data[(sym, tf)].copy(); B['e20'] = ls.m.ema(B.c.values.astype(float), sl)
        R = {}
        for w in WIN:
            ls.LCase.LATE = 1; ls.LCase.NYW = w; s = ls.LCase(sym, tf, B)
            R[w] = (s, s.run(lambda d: cs.cur_rule(d), q=q, gates=G))
        s0, b = R[30]; bv = [r['res'] for r in b]; bn = sum(bv); sd = float(np.std(bv)) or 1; bset = {(r['i'], r['lg']) for r in b}
        T0, T1 = s0.T[300], s0.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
        th = lambda res: [sum(r['res'] for r in res if (0 if s0.T[r['i']] < cuts[0] else 1 if s0.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        bt = th(b); t4 = s0.T[-1] - 28 * 86400000
        out += ['## %s' % nm, '', '| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |', '|---|---|---|---|---|---|---|---|---|']
        for w in WIN:
            s, res = R[w]; v = [r['res'] for r in res]; net = sum(v); W = sum(x > 0 for x in v); L = sum(x < 0 for x in v)
            ch = len(bset ^ {(r['i'], r['lg']) for r in res}) or 1; z = (net - bn) / (sd * np.sqrt(ch))
            dth = [a - c for a, c in zip(th(res), bt)]; b3 = all(x > 0 for x in dth)
            vd = 'baseline' if w == 30 else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < bn else 'noise'
            d4 = sum(r['res'] for r in res if s.T[r['i']] >= t4) - sum(r['res'] for r in b if s0.T[r['i']] >= t4)
            out.append('| %s | %d | %d%% | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %+.1f |' % (
                'off' if w == 0 else '%d min%s' % (w, ' (current)' if w == 30 else ''), len(v), round(100 * W / max(1, W + L)), net, net - bn, 0 if w == 30 else z, *dth, vd, d4))
            if vd in ('robust', 'promising'): summ.append('%s: NY block %s → %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s)' % (nm, 'off' if w == 0 else '%d min' % w, net - bn, z, *dth, vd))
        s, res = R[0]
        om = lambda r: (s.hm[r['i']] - s.tf) % 1440
        for lo, hi, lab in ((570, 585, '9:30-9:45'), (585, 600, '9:45-10:00')):
            g = [r for r in res if lo <= om(r) < hi]
            out.append('With the block off, setups on candles opening %s ET: %d, net %+.1f, win %d%%, avg %+.2f.' % (
                lab, len(g), sum(r['res'] for r in g), round(100 * sum(r['res'] > 0 for r in g) / max(1, len(g))), sum(r['res'] for r in g) / max(1, len(g))))
        out.append('')
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    main()
