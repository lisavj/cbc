#!/usr/bin/env python3
"""Staying in strong moves longer -- MES 3m and MGC 3m -- 11/08/2026.
The MFE study showed trades give back almost all of their best move, and 20 % (MES) / 31 % (MGC) run 1.5 x TP1 or more. This tests
what happens AFTER TP1 is hit (before TP1 nothing changes):
  flip  = keep  : the HTF CBC flip still closes the runner (current) | ignore : after TP1 the flip no longer closes it
  trail = x ATR : the trailing stop on the runner (current 1.7) -- 1.7 / 2.5 / 3.5
  TP2   = k x TP1 distance : close the runner there (off / 1.5 / 2 / 3)
  part  = share closed at TP1 : current (MES 80 % in 06-16 and 18-22:30 ET, else 100 %; MGC 80 %) or 50 %
Breakeven after TP1, the 16:00 exit and a new opposite setup still close the runner.
Run on two baselines: plain current setups, and with the recommended entry rules (MES: shorts only below the 5-day EMA + stop after
2 losses / 2 flip-outs when the previous 5 sessions lost + half SL1 if negative at 18 min; MGC: skip against VWAP + London stops
after its first loss). Net after costs (commission + 1 tick per trade, +1 tick for a rule exit); Δ vs the same baseline with current
runner exits. T = better in all three thirds, 4 = better in the last 4 weeks, R = T and every one-step neighbour (trail / TP2) better too."""
import itertools, numpy as np, pandas as pd, datetime as D
import combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg, study5 as s5, mes3_ema_grid as m

class RCase(cb.CCase):
    NOFLIP = False; TRX = None; TP2 = 0.0; PART = None
    def sim1(s, i, lg, q, stop_at):
        C, H, L, O = s.C, s.H, s.L, s.O; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        if s.PART is not None and part < 1: part = s.PART
        tr = s.TRX or q['tr']
        sl = en - g * sd; t1 = en + g * tpd; hit = False; t2 = en + g * s.TP2 * tpd
        snb = int(round(s.SX / s.tf)) if s.ACT else -1
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit and s.TP2 > 0 and (H[j] >= t2 if lg else L[j] <= t2):
                return part * tpd + (1 - part) * s.TP2 * tpd, j, 'TP2'
            if hit:
                ns = C[j] - g * tr * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            if not hit and j - i == snb:
                p = g * (C[j] - en)
                if (p <= 0 if s.SY == 0 else p < s.SY * tpd):
                    if s.ACT == 'CUT': return p, j, 'cut'
                    nsl = en - g * 0.5 * sd
                    if g * (C[j] - nsl) <= 0: return p, j, 'cut'
                    sl = max(sl, nsl) if lg else min(sl, nsl)
            why = None
            if s.hdir[j] == (0 if lg else 1) and not (hit and s.NOFLIP): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

BASES = {'MES': [('plain setups', None, None, (None, 0.0, 0)), ('with recommended rules', ('d5', 'S'), ('r', 2, 2), ('HALF', 0.0, 18))],
         'MGC': [('plain setups', None, None, (None, 0.0, 0)), ('with recommended rules', ('vwap', 'B'), ('u', (0, 1, 0)), (None, 0.0, 0))]}
COST = {'MES': (.5, .25), 'MGC': (.22, .1)}
FLIPS = [False, True]; TRS = [1.7, 2.5, 3.5]; TP2S = [0.0, 1.5, 2.0, 3.0]; PARTS = [None, .5]
PER = [('Third 1', lambda t: t['th'] == 0), ('Third 2', lambda t: t['th'] == 1), ('Third 3', lambda t: t['th'] == 2), ('Last 4 wk', lambda t: t['l4']), ('Whole', lambda t: True)]
def vname(k):
    f, tr, t2, p = k
    return 'flip %s, trail %.1f, TP2 %s, %s at TP1' % ('ignored' if f else 'kept', tr, ('%.1fx' % t2) if t2 else 'off', 'current %' if p is None else '50 %')
L = [__doc__, '']
for sym in ('MES', 'MGC'):
    nm, q, G = cb.CH[sym]; cost, tick = COST[sym]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = RCase(sym, 3, B); TR, ss = tg.trend_arrays(s)
    et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); mm = (et.dt.hour * 60 + et.dt.minute).values
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def run(f, sl, k):
        def ok(d):
            if not cs.cur_rule(d): return False
            if f is None or (f[1] == 'S' and d['lg']): return True
            v = TR[f[0]][d['i']]; return v == 0 or v == (1 if d['lg'] else -1)
        RCase.TX, RCase.TY = 0, 0.0; RCase.ACT, RCase.SY, RCase.SX = sl
        RCase.NOFLIP, RCase.TRX, RCase.TP2, RCase.PART = k
        return [dict(i=t['i'], j=t['j'], why=t['why'], lg=t['lg'], n=t['res'] - cost - (tick if t['why'] == 'cut' else 0),
                     th=0 if s.T[t['i']] < cuts[0] else 1 if s.T[t['i']] < cuts[1] else 2, l4=bool(s.T[t['i']] >= t4), ss=ss[t['i']], sub=s5.sub(mm[t['i']]))
                for t in s.run(ok, q=q, gates=G)]
    L += ['## %s' % nm, '']
    plain0 = None
    for blab, f, st, sl in BASES[sym]:
        res = {}
        for k in itertools.product(FLIPS, TRS, TP2S, PARTS):
            r = run(f, sl, k)
            if plain0 is None: plain0 = r
            if st: r = s5.apply_stop(st, r, plain0)
            res[k] = r
        k0 = (False, 1.7, 0.0, None); b = res[k0]
        tot = lambda r, P: sum(t['n'] for t in r if P(t))
        S = {k: [tot(r, P) for _, P in PER] for k, r in res.items()}
        D_ = {k: [S[k][x] - S[k0][x] for x in range(5)] for k in S}
        def flags(k):
            d = D_[k]; T = all(d[x] > 0 for x in range(3)); F = d[3] > 0
            f_, tr, t2, p = k; nb = []
            ti = TRS.index(tr); nb += [(f_, TRS[x], t2, p) for x in (ti - 1, ti + 1) if 0 <= x < len(TRS)]
            ji = TP2S.index(t2); nb += [(f_, tr, TP2S[x], p) for x in (ji - 1, ji + 1) if 0 <= x < len(TP2S)]
            R = T and all(D_[n][4] > 0 for n in nb)
            return ''.join(a for a, v in (('T', T), ('4', F), ('R', R)) if v)
        L += ['### %s — current runner exits: %s' % (blab, ', '.join('%s %+.0f' % (p, S[k0][x]) for x, (p, _) in enumerate(PER))), '',
              '**Δ whole period after costs** (flags: T all thirds better, 4 last 4 weeks better, R = T + neighbours better)', '',
              '| Flip after TP1 / part at TP1 | Trail | TP2 off | TP2 1.5x | TP2 2x | TP2 3x |', '|---|---|---|---|---|---|']
        for f_, p in itertools.product(FLIPS, PARTS):
            for tr in TRS:
                L.append('| %s / %s | %.1f | %s |' % ('ignored' if f_ else 'kept', 'current %' if p is None else '50 %', tr,
                         ' | '.join(('%+.0f %s' % (D_[(f_, tr, t2, p)][4], flags((f_, tr, t2, p)))).strip() if (f_, tr, t2, p) != k0 else 'current' for t2 in TP2S)))
        good = sorted([k for k in S if 'T' in flags(k)], key=lambda k: -D_[k][4])
        L += ['', '**Better in all three thirds: %d of %d.** Top 8 (net after costs, Δ in brackets):' % (len(good), len(S) - 1), '',
              '| Runner rule | ' + ' | '.join(p for p, _ in PER) + ' | Flags |', '|---|' + '---|' * 6]
        for k in good[:8]: L.append('| %s | %s | %s |' % (vname(k), ' | '.join('%+.0f (%+.0f)' % (S[k][x], D_[k][x]) for x in range(5)), flags(k)))
        pk = max([k for k in S if k != k0], key=lambda k: D_[k][0] + D_[k][1]); l3 = sorted(D_[k][2] for k in S if k != k0)
        L += ['', 'Walk-forward: best on thirds 1-2 = **%s** → third 3 Δ **%+.0f** (rank %d of %d; median %+.0f).' % (
            vname(pk), D_[pk][2], sum(1 for v in l3 if v > D_[pk][2]) + 1, len(l3), l3[len(l3) // 2])]
        # single-change effects
        L += ['', 'One change at a time (Δ whole / third 3 / last 4 wk): ' + '; '.join('%s %+.0f / %+.0f / %+.0f' % (lab, D_[k][4], D_[k][2], D_[k][3]) for lab, k in (
            ('ignore flip', (True, 1.7, 0.0, None)), ('trail 2.5', (False, 2.5, 0.0, None)), ('trail 3.5', (False, 3.5, 0.0, None)),
            ('TP2 1.5x', (False, 1.7, 1.5, None)), ('TP2 2x', (False, 1.7, 2.0, None)), ('TP2 3x', (False, 1.7, 3.0, None)), ('50 % at TP1', (False, 1.7, 0.0, .5)))), '']
    print(sym, 'done', flush=True)
open('runner_report.md', 'w').write('\n'.join(L))
