#!/usr/bin/env python3
"""HTF EMA20 / EMA200 stretch study -- 10/30/2026.

Question: instead of (or on top of) the VWAP stretch cap (MGC 3m 4 ATR), would a cap on the distance from the HTF (15m;
10m on 2m charts) EMA20, or from the EMA200, keep the good setups and drop the bad ones? Distance = close - level in ATR,
signed in the trade direction (+ = stretched in the trade's favour, e.g. a short far below the line).
Simulator: chop_sim.py (CBC-style engine, ER/breakout rule, R5 range gate on 3m, MTF gate on MES 2m), BASE exits
(SL1 1.7 ATR + min 5, TP1 1.7 ATR capped 6, 80 % at TP1, BE, trail 1.7 ATR). HTF EMA20 = live value (forming candle).
~50 % exact match with live setups: compare variants, not totals. z = change / (SD x sqrt(setups changed));
robust = z >= 2 and better in all three thirds; promising = z >= 1 and better in all three thirds.
Usage: python3 ema_stretch_study.py  (needs chop_sim.py + stretch_study.py next to it).
"""
import sys, datetime as D, numpy as np
import chop_sim as cs, stretch_study as ss

CASES = [('MGC', 3), ('MES', 3), ('MGC', 2), ('MES', 2)]


def dist(s, d, which):
    i = d['i']; g = 1 if d['lg'] else -1
    lv = {'vw': s.vw, 'h20': s.h20, 'e200': s.e200}[which][i]
    return g * (s.C[i] - lv) / s.atr[i]


def run(s, vw=None, h20=None, e200=None):
    """vw / h20 / e200 = cap in ATR (None = no cap on that line)."""
    def ok(d):
        if not cs.cur_rule(d):
            return False
        for k, cap in (('vw', vw), ('h20', h20), ('e200', e200)):
            if cap is not None and dist(s, d, k) > cap:
                return False
        return True
    G = dict(cs.GATE[(s.sym, s.tf)]); G['X4'] = 0
    return s.run(ok, q=ss.QB[s.sym], gates=G)


def study(sym, tf):
    s = cs.Case(sym, tf, ss.load(sym, tf))
    live_vw = 4.0 if (sym, tf) == ('MGC', 3) else None
    cur = run(s, vw=live_vw)
    cn = sum(r['res'] for r in cur); sd = float(np.std([r['res'] for r in cur])) or 1
    t0 = ss.thirds(cur, s.month, tf); C0 = {(r['i'], r['lg']) for r in cur}
    tn = 'Jan–Mar / Apr–Jun / Jul–now' if tf == 3 else 'Jun–Jul / Aug / Sep–now'
    L = ['## %s %dm · current (%s): %d setups, net %+.0f (thirds %+.0f / %+.0f / %+.0f)' % (
        sym, tf, 'VWAP cap 4 ATR' if live_vw else 'no stretch cap', len(cur), cn, *t0), '']
    base = run(s)  # no cap at all: where do the losers sit?
    for k, nm, bands in (('h20', 'HTF EMA20', (-9, 0, 1, 2, 3, 4, 5, 6, 8, 99)), ('e200', 'EMA200', (-99, 0, 2, 4, 6, 8, 10, 12, 15, 999)),
                         ('vw', 'VWAP', (-99, 0, 2, 3, 4, 5, 6, 8, 10, 999))):
        L += ['**All setups (no stretch cap) by distance from %s (ATR, + = in the trade direction)**' % nm, '',
              '| Distance | N | Win % | Net | Avg |', '|---|---|---|---|---|']
        for lo, hi in zip(bands[:-1], bands[1:]):
            g = [r for r in base if lo <= dist(s, r, k) < hi]
            if g:
                L.append('| %s to %s | %d | %d%% | %+.0f | %+.2f |' % (lo if lo > -50 else '<', hi if hi < 50 else '+', len(g), round(100 * sum(r['res'] > 0 for r in g) / len(g)), sum(r['res'] for r in g), sum(r['res'] for r in g) / len(g)))
        L.append('')
    V = [('No stretch cap at all', {})]
    V += [('HTF EMA20 cap %s ATR (instead of VWAP)' % x, dict(h20=x)) for x in (1, 1.5, 2, 2.5, 3, 4, 5, 6)]
    V += [('EMA200 cap %s ATR (instead of VWAP)' % x, dict(e200=x)) for x in (3, 4, 5, 6, 8, 10, 12)]
    if live_vw:
        V += [('VWAP 4 + HTF EMA20 cap %s ATR' % x, dict(vw=4, h20=x)) for x in (2, 3, 4)]
        V += [('VWAP 4 + EMA200 cap %s ATR' % x, dict(vw=4, e200=x)) for x in (4, 6, 8)]
    L += ['| Variant | Setups | Net | Δ vs current | z | Δ by third (%s) | Verdict |' % tn, '|---|---|---|---|---|---|---|']
    rows = []
    for nm, kw in V:
        res = run(s, **kw)
        net = sum(r['res'] for r in res); ch = len(C0 ^ {(r['i'], r['lg']) for r in res}) or 1
        z = (net - cn) / (sd * np.sqrt(ch)); dth = [a - b for a, b in zip(ss.thirds(res, s.month, tf), t0)]
        b3 = all(x > 0 for x in dth)
        v = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < cn else 'noise'
        L.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (nm, len(res), net, net - cn, z, *dth, v))
        rows.append((nm, net - cn, z, dth, v))
        if (sym, tf) == ('MGC', 3):
            td = [r for r in res if s.date[r['i']].startswith('10/30') and (r['i'], r['lg']) not in C0]
            if td:
                L[-1] += ' · 10/30 adds ' + ', '.join('%s %+.1f' % (s.date[r['i']][6:], r['res']) for r in td)
    return '\n'.join(L), rows


def main():
    out = ['# HTF EMA20 / EMA200 stretch study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for sym, tf in CASES:
        try:
            txt, rows = study(sym, tf)
        except Exception as e:
            out += ['## %s %dm' % (sym, tf), '', 'error: %s' % e, '']; continue
        out += [txt, '']
        summ += ['%s %dm: %s → %+.0f pts, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s)' % (sym, tf, r[0], r[1], r[2], *r[3], r[4]) for r in rows if r[4] in ('robust', 'promising')]
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))


if __name__ == '__main__':
    main()
