#!/usr/bin/env python3
"""5m-confirmation backtest (MES) -- 11/05/2026.
Question (from the live 10/19-11/05 combo check): are MES 2m / 3m setups better when a MES 5m setup agrees -- a same-direction
5m setup is open at the setup's entry candle close, or a 5m setup in the same direction started within 10 min before / after?
Also: 5m setups confirmed by 2m / 3m.
Replay (late_study LCase = chop_sim rules, LTF late window 1, NY OR block 30 min, toward flips strict), each chart on its live
settings: MES 3m 9 / 20, range gate 24 / 5 ATR, exits SL 3 / TP1 2.0 / time-of-day close (v10.70); MES 2m slow 14, 1H MTF gate,
base exits (HTF flip counter not modelled); MES 5m 9 / 20, no gates, base exits. 3m / 5m Jan 5 -> now, 2m Jun 1 -> now.
Thirds = equal time over each pair's common period. z = (confirmed avg - all avg) / (SD / sqrt(confirmed n)) style test via the
excluded setups: z = (net(confirmed) - net(all) * share) ... see code. Robust = z >= 2 and confirmed avg > unconfirmed avg in all
three thirds; promising = z >= 1 and all three.
Usage: python3 confirm5_study.py   (needs chop_sim.py, mes3_ema_grid.py, late_study.py next to it)"""
import numpy as np, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

CH = {2: ('MES', 2, 14, ls.MESX, dict(R5=0, X4=0, MTF=1)),
      3: ('MES', 3, 20, dict(m.LIVE, tp=2.0), dict(R5=1, X4=0, MTF=0)),
      5: ('MES', 5, 20, ls.MESX, dict(R5=0, X4=0, MTF=0))}

def setups(tf):
    sym, tf, sl, q, G = CH[tf]
    B = ls.load(sym, tf); B['e20'] = m.ema(B.c.values.astype(float), sl)
    ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = ls.LCase(sym, tf, B)
    res = s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
    out = []
    for r in res:
        t0 = int(s.T[r['i']]) + tf * 60000; t1 = int(s.T[r['j']]) + tf * 60000
        out.append(dict(tf=tf, lg=r['lg'], t0=t0, t1=t1, res=r['res'], trig=r['trig']))
    return out

def conf(x, others, win=600000):
    return any(o['lg'] == x['lg'] and ((o['t0'] <= x['t0'] < o['t1']) or abs(o['t0'] - x['t0']) <= win) for o in others)

def main():
    S = {tf: setups(tf) for tf in (2, 3, 5)}
    out = ['# MES 5m-confirmation backtest — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    import bisect
    for a, b in ((2, 5), (3, 5), (5, 2), (5, 3), (2, 3), (3, 2)):
        lo = max(min(x['t0'] for x in S[a]), min(x['t0'] for x in S[b])); hi = min(max(x['t0'] for x in S[a]), max(x['t0'] for x in S[b]))
        A = [x for x in S[a] if lo <= x['t0'] <= hi]; Bo = sorted([x for x in S[b] if lo - 86400000 <= x['t0'] <= hi + 86400000], key=lambda x: x['t0'])
        bt = [x['t0'] for x in Bo]
        def near(x):
            k = bisect.bisect_left(bt, x['t0'] - 6 * 3600000); return Bo[k:bisect.bisect_right(bt, x['t0'] + 600000)]
        C = [x for x in A if conf(x, near(x))]; U = [x for x in A if x not in C]
        cuts = [lo + (hi - lo) * k / 3 for k in (1, 2)]
        thd = lambda L: [[x['res'] for x in L if (0 if x['t0'] < cuts[0] else 1 if x['t0'] < cuts[1] else 2) == k] for k in range(3)]
        av = lambda v: sum(v) / len(v) if v else 0
        va = [x['res'] for x in A]; vc = [x['res'] for x in C]; vu = [x['res'] for x in U]
        sd = float(np.std(va)) or 1
        z = (av(vc) - av(vu)) / (sd * np.sqrt(1 / max(1, len(vc)) + 1 / max(1, len(vu))))
        tc, tu = thd(C), thd(U); better = [av(c) > av(u) for c, u in zip(tc, tu)]
        vd = 'robust' if z >= 2 and all(better) else 'promising' if z >= 1 and all(better) else 'worse' if av(vc) < av(vu) else 'noise'
        w = lambda v: round(100 * sum(x > 0 for x in v) / max(1, sum(x != 0 for x in v)))
        f = lambda t: D.datetime.fromtimestamp(t / 1000).strftime('%m/%d')
        out += ['## MES %dm setups confirmed by MES %dm (%s → %s)' % (a, b, f(lo), f(hi)), '',
                '| Group | Setups | Win % | Net | Avg | Thirds net | Thirds avg |', '|---|---|---|---|---|---|---|']
        for nm, L, v in (('All %dm' % a, A, va), ('Confirmed by %dm' % b, C, vc), ('Not confirmed', U, vu)):
            t = thd(L)
            out.append('| %s | %d | %d%% | %+.0f | %+.2f | %+.0f / %+.0f / %+.0f | %+.2f / %+.2f / %+.2f |' % (nm, len(v), w(v), sum(v), av(v), *[sum(x) for x in t], *[av(x) for x in t]))
        bt2 = {}
        for x in C: bt2.setdefault(x['trig'], []).append(x['res'])
        out += ['', 'Confirmed minus unconfirmed avg: %+.2f pts/setup, z %+.1f, better in thirds: %s → **%s**. Taking only confirmed setups: %+.0f vs %+.0f for all.' % (
            av(vc) - av(vu), z, ' / '.join('yes' if b_ else 'no' for b_ in better), vd, sum(vc), sum(va)),
                'Confirmed by trigger: ' + ' · '.join('%s %d / %+.0f' % (k, len(v), sum(v)) for k, v in sorted(bt2.items())), '']
        if vd in ('robust', 'promising'):
            summ.append('MES %dm confirmed by %dm: avg %+.2f vs %+.2f unconfirmed, z %+.1f, only-confirmed net %+.0f vs all %+.0f (%s)' % (a, b, av(vc), av(vu), z, sum(vc), sum(va), vd))
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    main()
