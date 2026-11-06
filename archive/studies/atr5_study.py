#!/usr/bin/env python3
"""MES 3m setups with the 5m ATR for SL / TP1 / trail -- 11/05/2026.
Setups: replay of MES 3m on live settings (v10.70: 9 / 20, range gate, late window 1, NY OR block 30). Gates keep the 3m ATR
(as CBC). Exits: SL1 = m x ATR (min 5, no cap), TP1 = k x ATR, close at TP1 by time of day (100 % / 80 % + BE + trail 1.7 x ATR),
opposite 15m flip, 16:00. ATR = 3m ATR(14) (live) or the 5m ATR(14) of the last CLOSED 5m candle (no look-ahead).
Usage: python3 atr5_study.py"""
import numpy as np, pandas as pd, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

class ACase(ls.LCase):
    USE5 = False
    def sim1(s, i, lg, q, stop_at):
        A3 = s.atr
        if s.USE5: s.atr = s.atr5
        try: return m.MCase.sim1(s, i, lg, q, stop_at)
        finally: s.atr = A3

def main():
    B = ls.load('MES', 3); B5 = ls.load('MES', 5)
    H, L, C = (B5[k].values.astype(float) for k in 'hlc')
    pc = np.r_[C[0], C[:-1]]; a5 = cs.rma(np.maximum(H, pc) - np.minimum(L, pc), 14)
    c5 = B5.t.values + 300000                      # 5m candle close time
    ls.LCase.LATE = 1; ls.LCase.NYW = 30
    s = ACase('MES', 3, B)
    c3 = s.T + 180000
    k = np.searchsorted(c5, c3, side='right') - 1   # last 5m candle closed at or before the 3m close
    s.atr5 = np.where(k >= 0, a5[np.clip(k, 0, None)], np.nan)
    ok = ~np.isnan(s.atr5) & ~np.isnan(s.atr)
    r = s.atr5[ok] / s.atr[ok]
    G = dict(R5=1, X4=0, MTF=0)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * j / 3 for j in (1, 2)]; t4 = T1 - 28 * 86400000
    third = lambda i: 0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2
    def run(use5, sl, tp, part='tod'):
        s.USE5 = use5
        res = s.run(lambda d: cs.cur_rule(d), q=dict(m.LIVE, sl=sl, tp=tp, part=part), gates=G)
        v = [x['res'] for x in res]; n = len(v)
        return dict(res=res, n=n, net=sum(v), wr=round(100 * sum(x > 0 for x in v) / max(1, sum(x != 0 for x in v))),
                    th=[sum(x['res'] for x in res if third(x['i']) == j) for j in range(3)], l4=sum(x['res'] for x in res if s.T[x['i']] >= t4),
                    h=(sum(v[:n // 2]), sum(v[n // 2:])))
    f = lambda t: D.datetime.fromtimestamp(t / 1000).strftime('%m/%d')
    out = ['# MES 3m — exits on the 5m ATR vs the 3m ATR — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '',
           'Data %s → %s. 5m ATR / 3m ATR: median %.2f (25–75 %%: %.2f–%.2f). Thirds %s–%s / –%s / –%s.' % (f(s.T[0]), f(T1), np.median(r), *np.percentile(r, [25, 75]), f(T0), f(cuts[0]), f(cuts[1]), f(T1)), '']
    base = run(False, 3.0, 2.0); sd = float(np.std([x['res'] for x in base['res']])) or 1; bset = {(x['i'], x['lg']) for x in base['res']}
    def row(nm, x):
        ch = len(bset ^ {(y['i'], y['lg']) for y in x['res']}) or 1; z = (x['net'] - base['net']) / (sd * np.sqrt(ch))
        dth = [a - b for a, b in zip(x['th'], base['th'])]; b3 = all(d > 0 for d in dth)
        vd = 'baseline' if x is base else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if x['net'] < base['net'] else 'noise'
        return '| %s | %d | %d%% | %+.0f | %+.0f / %+.0f | %+.0f / %+.0f / %+.0f | %+.0f | %+.1f | %s | %+.1f |' % (
            nm, x['n'], x['wr'], x['net'], *x['h'], *x['th'], x['net'] - base['net'], 0 if x is base else z, vd, x['l4'] - base['l4']), vd, z, dth
    hdr = ['| Exits | Setups | Win % | Net | Halves | Thirds | Δ vs live | z | Verdict | Last 4 wk Δ |', '|---|---|---|---|---|---|---|---|---|---|']
    out += ['## A. Same multipliers (SL 3.0 / TP1 2.0), 3m vs 5m ATR', ''] + hdr
    out.append(row('3m ATR (live)', base)[0])
    x5 = run(True, 3.0, 2.0); out.append(row('5m ATR', x5)[0])
    # matched distance: multipliers scaled by 1 / median ratio
    q = np.median(r)
    xm = run(True, round(3.0 / q, 2), round(2.0 / q, 2)); out.append(row('5m ATR, same median distance (SL %.2f / TP1 %.2f)' % (3.0 / q, 2.0 / q), xm)[0])
    out += ['', '## B. Grid on the 5m ATR (net; ✱ both halves +, T all three thirds +; Δ vs live 3m-ATR %+.0f)' % base['net'], '']
    SL = (1.5, 2.0, 2.5, 3.0); TP = (1.0, 1.25, 1.5, 1.75, 2.0)
    out += ['| SL \\ TP1 (x 5m ATR) | ' + ' | '.join('%.2f' % t for t in TP) + ' |', '|---|' + '---|' * len(TP)]
    best = []
    for a in SL:
        cells = []
        for b in TP:
            x = run(True, a, b)
            cells.append('%+.0f%s%s' % (x['net'], ' ✱' if min(x['h']) > 0 else '', ' T' if min(x['th']) > 0 else ''))
            best.append((x['net'], a, b, x))
        out.append('| %.1f | %s |' % (a, ' | '.join(cells)))
    out += ['', 'Same grid on the 3m ATR for reference:', '', '| SL \\ TP1 (x 3m ATR) | ' + ' | '.join('%.2f' % t for t in TP) + ' |', '|---|' + '---|' * len(TP)]
    for a in (2.0, 2.5, 3.0, 3.5):
        out.append('| %.1f | %s |' % (a, ' | '.join('%+.0f' % run(False, a, b)['net'] for b in TP)))
    best.sort(key=lambda y: -y[0])
    out += ['', '## C. Best 5m-ATR cells vs live', ''] + hdr
    summ = []
    for net, a, b, x in best[:5]:
        line, vd, z, dth = row('5m ATR SL %.1f / TP1 %.2f' % (a, b), x); out.append(line)
        if vd in ('robust', 'promising'): summ.append('5m ATR SL %.1f / TP1 %.2f: %+.0f vs live, z %+.1f (%s)' % (a, b, net - base['net'], z, vd))
    out += ['', '## Candidates', ''] + (['- ' + y for y in summ] if summ else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    main()
