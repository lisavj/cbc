#!/usr/bin/env python3
"""ATR length study, MES 3m and MGC 3m -- 11/05/2026.
CBC "ATR length" (Auto Trade Setup, default 14) sizes SL1 / TP1 / trail and the ATR-based gates (range gate width, flip
distance 2 ATR, VWAP stretch). Tested lengths 5 / 7 / 10 / 14 / 20 / 30 / 50, two ways: (1) EXITS only (gates keep ATR 14),
(2) ALL (exits + gates). Replay (chop_sim rules, late window 1, NY OR block 30) on live settings: MES 3m 9 / 20, range gate,
SL1 3 x ATR min 5 / TP1 2 x ATR / time-of-day close; MGC 3m range gate + VWAP stretch 4 ATR, SL1 1.7 ATR min 5 cap 7 /
TP1 1.7 ATR cap 6 / 80 % + BE + trail 1.7. Jan 5 -> now. z / robust / promising as in the other studies."""
import numpy as np, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

LENS = (5, 7, 10, 14, 20, 30, 50)
_rma = cs.rma
class XCase(ls.LCase):
    N = 14; ALL = False
    def __init__(s, sym, tf, B):
        if s.ALL:
            cs.rma = lambda x, n: _rma(x, s.N if n == 14 else n)
        try: super().__init__(sym, tf, B)
        finally: cs.rma = _rma
        pc = np.r_[s.C[0], s.C[:-1]]; s.atrx = _rma(np.maximum(s.H, pc) - np.minimum(s.L, pc), s.N)
    def sim1(s, i, lg, q, stop_at):
        A = s.atr; s.atr = s.atrx
        try: return m.MCase.sim1(s, i, lg, q, stop_at)
        finally: s.atr = A

CH = [('MES 3m', 'MES', dict(m.LIVE, tp=2.0), dict(R5=1, X4=0, MTF=0)), ('MGC 3m', 'MGC', ls.MGCX, dict(R5=1, X4=1, MTF=0))]

def main():
    out = ['# ATR length study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for nm, sym, q, G in CH:
        B = ls.load(sym, 3)
        ls.LCase.LATE = 1; ls.LCase.NYW = 30
        XCase.N, XCase.ALL = 14, False; s0 = XCase(sym, 3, B)
        b = s0.run(lambda d: cs.cur_rule(d), q=q, gates=G); bv = [r['res'] for r in b]; bn = sum(bv); sd = float(np.std(bv)) or 1
        bset = {(r['i'], r['lg']) for r in b}
        T0, T1 = s0.T[300], s0.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
        th = lambda s, res: [sum(r['res'] for r in res if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        bt = th(s0, b); b4 = sum(r['res'] for r in b if s0.T[r['i']] >= t4)
        out += ['## %s — current ATR 14: %d setups, net %+.0f' % (nm, len(b), bn), '',
                '| ATR length | Applied to | Setups | Win % | Net | Δ vs 14 | z | Δ by third | Verdict | Last 4 wk Δ | Median SL1 / TP1 (pts) |',
                '|---|---|---|---|---|---|---|---|---|---|---|']
        for allg in (False, True):
            for n in LENS:
                if n == 14 and allg: continue
                XCase.N, XCase.ALL = n, allg; s = XCase(sym, 3, B) if (allg or n != 14) else s0
                r = s.run(lambda d: cs.cur_rule(d), q=q, gates=G); v = [x['res'] for x in r]; net = sum(v)
                ch = len(bset ^ {(x['i'], x['lg']) for x in r}) or 1; z = (net - bn) / (sd * np.sqrt(ch))
                dth = [a - c for a, c in zip(th(s, r), bt)]; b3 = all(x > 0 for x in dth)
                vd = 'baseline' if n == 14 else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < bn else 'noise'
                a = np.array([s.atrx[x['i']] for x in r])
                sl = np.median(np.maximum(np.minimum(q['sl'] * a, q['cap']), q['mn'])); tp = np.median(np.minimum(q['tp'] * a, q['tcap']))
                out.append('| %d%s | %s | %d | %d%% | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %+.1f | %.1f / %.1f |' % (
                    n, ' (current)' if n == 14 else '', 'exits + gates' if allg else 'exits', len(v), round(100 * sum(x > 0 for x in v) / max(1, sum(x != 0 for x in v))),
                    net, net - bn, 0 if n == 14 else z, *dth, vd, sum(x['res'] for x in r if s.T[x['i']] >= t4) - b4, sl, tp))
                if vd in ('robust', 'promising'): summ.append('%s ATR %d (%s): %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s)' % (nm, n, 'exits + gates' if allg else 'exits', net - bn, z, *dth, vd))
        out.append('')
    out += ['## Candidates', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    main()
