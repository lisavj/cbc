#!/usr/bin/env python3
"""CBC "③ Trade Setup Filters" sweep -- 11/01/2026 (11/08: MGC 2m range gate ON as live since v10.77).

Question: would turning on / changing any of the Trade Setup Filters help, per chart? One change at a time on top of each
chart's live settings (v10.50 defaults + the user's per-symbol lists): ER chop filter 0.23 with breakout exception (3 bars) ON
everywhere; range gate 24 bars / 20 % / 5 ATR on MGC 3m + MES 3m + MGC 2m (v10.77); VWAP stretch 4 ATR on MGC 3m; 1H MTF gate on MES 2m;
"Block after frequent HTF flips" 4 in 8 HTF candles on MES 2m. Everything else off. Base exits. Bars Jan 5 - Oct 30 (2m Jun - Oct).
Engine: chop_sim (candidate fields chop / adx / crosses / HTF EMA20 slope / 12-bar range use the 12-bar "Chop filters length").
Not modelled: mixed chart structure, the momentum-break trigger, CBC's multi-bar late window.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 filter_sweep.py MES 3   (one chart per call)
"""
import sys, datetime as D, numpy as np, pandas as pd
import chop_sim as cs, stretch_study as ss

ss.FROM[5] = '2026-01-05'
CAP = {'MGC': 7.0, 'MES': 8.0}
LIVE = {('MES', 3): dict(r5=5, x4=None, mtf=0, fl=None), ('MGC', 3): dict(r5=5, x4=4.0, mtf=0, fl=None),
        ('MES', 2): dict(r5=None, x4=None, mtf=1, fl=4), ('MGC', 2): dict(r5=5, x4=None, mtf=0, fl=None),
        ('MES', 5): dict(r5=None, x4=None, mtf=0, fl=None), ('MGC', 5): dict(r5=None, x4=None, mtf=0, fl=None)}


def prep(s):
    n = 24
    s.hh24 = pd.Series(s.H).rolling(n).max().values; s.ll24 = pd.Series(s.L).rolling(n).min().values
    fl = (s.hf != 0).astype(float)
    s.flips8 = pd.Series(fl).rolling(8 * 5).sum().values   # HTF flips in the last 8 HTF candles (5 chart bars each)


def make_ok(s, P):
    sym = s.sym

    def ok(d):
        i = d['i']; lg = d['lg']; g = 1 if lg else -1; A = s.atr[i]
        e = d['er'][12]
        if P['er'] > 0:
            if d['trig'] == 'flip' and e < P['er']:
                return False
            if e < P['er'] and not (P['bo'] == 3 and d['bo'] or P['bo'] == 1 and d['bo1']):
                return False
        if P['r5']:
            w = s.hh24[i] - s.ll24[i]
            if w > 0 and w / A < P['r5']:
                pos = (s.C[i] - s.ll24[i]) / w
                if (pos if lg else 1 - pos) >= 1 - P['r5z']:
                    return False
        if P['x4'] and d['xv'] > P['x4']:
            return False
        if P['fl'] and s.flips8[i] >= P['fl']:
            return False
        if P.get('chop') and d['chop'] > P['chop']:
            return False
        if P.get('adx') and d['adx'] < P['adx']:
            return False
        if P.get('xs') and d['xs'] >= P['xs']:
            return False
        if P.get('slope') and d['slope'] < P['slope']:
            return False
        if P.get('rng') and d['rng'] < P['rng']:
            return False
        if P.get('nv'):
            dv = g * (s.C[i] - s.vw[i])
            if -3 <= dv <= 2 and not ((s.L[i] >= s.vw[i] + P['nv']) if lg else (s.H[i] <= s.vw[i] - P['nv'])):
                return False
        if P.get('ne'):
            de = g * (s.C[i] - s.e200[i])
            if -3 <= de <= 2:
                return False
        if P.get('vc') and CAP[sym] < P['vc'] * A:
            return False
        if P.get('va') and s.atrrel[i] > P['va']:
            return False
        return True
    return ok


def run(s, P):
    G = dict(R5=0, X4=0, MTF=P['mtf'])
    keep = s.cands
    # the engine's own trigger ER minimum uses ER(12) (0.08 LTF pierce / 0.15 HTF pierces) -- unchanged
    try:
        return s.run(make_ok(s, P), q=ss.QB[s.sym], gates=G)
    finally:
        s.cands = keep


def thirds(res, s, tf):
    return ss.thirds(res, s.month, 3 if tf != 2 else 2)


def main():
    sym, tf = sys.argv[1], int(sys.argv[2])
    L0 = LIVE[(sym, tf)]
    base_P = dict(er=.23, bo=3, r5=L0['r5'], r5z=.2, x4=L0['x4'], mtf=L0['mtf'], fl=L0['fl'])
    s = cs.Case(sym, tf, ss.load(sym, tf)); prep(s)
    cur = run(s, base_P)
    v0 = [r['res'] for r in cur]; net0 = sum(v0); sd = float(np.std(v0)) or 1; t0 = thirds(cur, s, tf); C0 = {(r['i'], r['lg']) for r in cur}
    w0 = sum(x > 0 for x in v0); l0 = sum(x < 0 for x in v0)
    tn = 'Jan–Mar / Apr–Jun / Jul–Oct' if tf != 2 else 'Jun–Jul / Aug / Sep–Oct'
    live_txt = ', '.join(x for x in ['ER 0.23 + breakout 3 bars', 'range gate 24 / 20 %% / %s ATR' % L0['r5'] if L0['r5'] else '', 'VWAP stretch %s ATR' % L0['x4'] if L0['x4'] else '',
                                     '1H MTF gate' if L0['mtf'] else '', 'HTF flips >= %s in 8' % L0['fl'] if L0['fl'] else ''] if x)
    out = ['## %s %dm — current (%s): %d setups, win %.0f%%, net %+.0f' % (sym, tf, live_txt, len(v0), 100 * w0 / max(1, w0 + l0), net0), '',
           '| Change (one at a time) | Setups | Win %% | Net | Δ vs current | z | Δ by third (%s) | Verdict |' % tn, '|---|---|---|---|---|---|---|---|']
    V = [('ER threshold 0.18', dict(er=.18)), ('ER threshold 0.20', dict(er=.20)), ('ER threshold 0.26', dict(er=.26)), ('ER threshold 0.30', dict(er=.30)),
         ('ER filter OFF', dict(er=0)), ('ER breakout exception OFF', dict(bo=0)), ('ER breakout window 1 bar', dict(bo=1)),
         ('Choppiness Index > 61.8 block', dict(chop=61.8)), ('Choppiness Index > 58 block', dict(chop=58)),
         ('ADX < 20 block', dict(adx=20)), ('ADX < 15 block', dict(adx=15)),
         ('EMA20 / VWAP crosses >= 4 block', dict(xs=4)), ('EMA20 / VWAP crosses >= 6 block', dict(xs=6)),
         ('HTF EMA20 slope < 0.3 ATR block', dict(slope=.3)), ('HTF EMA20 slope < 0.2 ATR block', dict(slope=.2)),
         ('12-bar range < 2 ATR block', dict(rng=2)), ('12-bar range < 3 ATR block', dict(rng=3)),
         ('VWAP stretch 3 ATR', dict(x4=3.0)), ('VWAP stretch 4 ATR', dict(x4=4.0)), ('VWAP stretch 6 ATR', dict(x4=6.0)), ('VWAP stretch OFF', dict(x4=None)),
         ('Range gate OFF', dict(r5=None)), ('Range gate 24 / 20 % / 4 ATR', dict(r5=4)), ('Range gate 24 / 20 % / 5 ATR', dict(r5=5)), ('Range gate 24 / 20 % / 6 ATR', dict(r5=6)),
         ('Block if VWAP -3 / +2 pts (unless candle 1 pt beyond)', dict(nv=1.0)), ('Block if EMA200 -3 / +2 pts', dict(ne=True)),
         ('HTF flips >= 2 in 8 block', dict(fl=2)), ('HTF flips >= 3 in 8 block', dict(fl=3)), ('HTF flips >= 4 in 8 block', dict(fl=4)), ('HTF flips block OFF', dict(fl=None)),
         ('Skip if Max ATR SL1 cap < 1.5 x ATR', dict(vc=1.5)), ('Skip while ATR > 1.8 x ATR(100)', dict(va=1.8)), ('Skip while ATR > 1.5 x ATR(100)', dict(va=1.5))]
    rows = []
    for nm, ch in V:
        P = dict(base_P); P.update(ch)
        if P == base_P:
            continue
        res = run(s, P); v = [r['res'] for r in res]; net = sum(v)
        chg = len(C0 ^ {(r['i'], r['lg']) for r in res}) or 1
        z = (net - net0) / (sd * np.sqrt(chg)); dth = [a - b for a, b in zip(thirds(res, s, tf), t0)]
        b3 = all(x > 0 for x in dth)
        verdict = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < net0 else 'noise'
        w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
        out.append('| %s | %d | %.0f%% | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (nm, len(v), 100 * w / max(1, w + l), net, net - net0, z, *dth, verdict))
        rows.append((nm, net - net0, z, dth, verdict))
    out += ['', 'Candidates: ' + ('; '.join('%s → %+.0f, z %+.1f, %+.0f / %+.0f / %+.0f (%s)' % (r[0], r[1], r[2], *r[3], r[4]) for r in rows if r[4] in ('robust', 'promising')) or 'none'), '']
    print('\n'.join(out))


if __name__ == '__main__':
    main()
