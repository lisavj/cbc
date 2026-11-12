#!/usr/bin/env python3
"""HTF EMA length study -- 11/01/2026.

Question: would other HTF EMA lengths (the 15m EMAs on 3m charts, 25m on 5m charts; CBC hard-codes 9 / 20) do better on
MES / MGC 3m and 5m? In the replay the HTF EMAs feed (1) the HTF EMA9 Pierce and HTF EMA20 Pierce trigger lines (live value of
the forming HTF candle) and (2) the "away flip" check (flip candle closed beyond the HTF EMA20). They are recomputed from the
HTF candle closes for every variation (baseline 9 / 20 included, so all rows use the same method).
Charts on their live settings: chart EMAs 9 / 20 / 200; MES 3m range gate on; MGC 3m range gate + VWAP stretch 4 ATR on;
5m charts no gates. Base exits. Jan 5 - Oct 30. ~50 % exact match with live setups on 3m: compare variants, not totals.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 htf_ema_study.py MES 3   (one chart per call; needs chop_sim.py, stretch_study.py, ema5_study.py)
"""
import sys, datetime as D, numpy as np, pandas as pd
import chop_sim as cs, stretch_study as ss, ema5_study as es

ss.FROM[5] = '2026-01-05'
VAR = [('A', 9, 20, 'standard'), ('B', 7, 16, 'faster'), ('C', 8, 18, 'slightly faster'), ('D', 5, 12, 'much faster'),
       ('E', 12, 26, 'slower'), ('F', 14, 30, 'slower'), ('G', 9, 26, 'slow line slower'), ('H', 9, 34, 'slow line much slower'),
       ('I', 7, 20, 'fast line faster'), ('J', 12, 20, 'fast line slower')]


def htf_lines(B, f, sl):
    """Final HTF EMA per HTF candle (B.hk groups), written on every bar of the group (chop_sim reads the last bar's value)."""
    B = B.copy()
    last = B.t.values == B['last'].values
    hc = pd.Series(B.c.values[last].astype(float))
    keys = B.hk.values[last]
    e9 = dict(zip(keys, hc.ewm(span=f, adjust=False).mean().values))
    e20 = dict(zip(keys, hc.ewm(span=sl, adjust=False).mean().values))
    B['h9'] = [e9.get(k, np.nan) for k in B.hk.values]
    B['h20'] = [e20.get(k, np.nan) for k in B.hk.values]
    return B


def run(s, skip=(), x4=False, r5=None):
    keep = s.cands
    s.cands = [d for d in keep if d['trig'] not in skip and not (x4 and d['xv'] > 4)]
    try:
        return es.run(s, r5=r5)
    finally:
        s.cands = keep


def main():
    sym, tf = sys.argv[1], int(sys.argv[2])
    kw = dict(r5=(24, 5)) if tf == 3 else {}
    x4 = (sym, tf) == ('MGC', 3)
    B0 = ss.load(sym, tf)
    out = ['## %s %dm — HTF %dm EMAs (%d candles, chart EMAs 9 / 20 / 200%s)' % (sym, tf, 5 * tf, len(B0), ', range gate on' if tf == 3 else '', ) + (', VWAP stretch 4 ATR' if x4 else ''), '']
    # sanity: recomputed 9 / 20 vs BarFeed's own HTF EMA20 on the HTF candles' last bars
    Bs = htf_lines(B0, 9, 20); m = B0.t.values == B0['last'].values
    d = np.abs(Bs.h20.values[m] - B0.h20.values[m]) / np.nanmedian(np.abs(np.diff(B0.c.values)))
    out += ['Check: recomputed HTF EMA20 vs BarFeed value — median gap %.2f typical candle moves (after the first 200 HTF candles: %.2f)' % (np.nanmedian(d), np.nanmedian(d[200:])), '']
    sets = [(k, f, sl, why, B0, None) for k, f, sl, why in VAR]
    if (sym, tf) == ('MES', 5):
        C = B0.c.values.astype(float); B5 = B0.copy(); B5['e9'] = es.ema(C, 16); B5['e20'] = es.ema(C, 34); B5['e200'] = es.ema(C, 120)
        sets += [(k + '+', f, sl, why + ', chart 16/34/120', B5, 1) for k, f, sl, why in VAR]
    cases = {}
    base_case = cs.Case(sym, tf, htf_lines(B0, 9, 20)); bres = run(base_case, x4=x4, **kw); base = es.stats(bres, base_case)
    out += es.HDR
    rows = []
    for k, f, sl, why, Bx, extra in sets:
        s = base_case if (k == 'A') else cs.Case(sym, tf, htf_lines(Bx, f, sl))
        res = bres if k == 'A' else run(s, x4=x4, **kw)
        x, z, dth, v = (base, 0.0, [0, 0, 0], 'baseline') if k == 'A' else es.cmp(base, bres, res, s)
        out.append(es.line('%s HTF %d / %d (%s)' % (k, f, sl, why), x, z, dth, v, base) + ' ' + es.by_trig(res))
        rows.append((k, f, sl, why, x['net'] - base['net'], z, dth, v))
    for nm, sk in (('HTF EMA9 Pierce trigger OFF', ('h9',)), ('HTF EMA20 Pierce trigger OFF', ('h20',)), ('both HTF EMA pierce triggers OFF', ('h9', 'h20'))):
        res = run(base_case, skip=sk, x4=x4, **kw); x, z, dth, v = es.cmp(base, bres, res, base_case)
        out.append(es.line('Reference: ' + nm, x, z, dth, v, base) + ' ' + es.by_trig(res))
        rows.append((nm, 0, 0, '', x['net'] - base['net'], z, dth, v))
    out += ['', 'Candidates: ' + ('; '.join('%s %s → %+.0f, z %+.1f, %+.0f / %+.0f / %+.0f (%s)' % (r[0], ('HTF %d / %d' % (r[1], r[2])) if r[1] else '', r[4], r[5], *r[6], r[7]) for r in rows if r[7] in ('robust', 'promising')) or 'none'), '']
    print('\n'.join(out))


if __name__ == '__main__':
    main()
