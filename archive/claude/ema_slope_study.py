#!/usr/bin/env python3
"""EMA direction (slope) gate study -- MGC 3m and MES 3m.

Question: should a setup be skipped when the HTF EMA9 and/or HTF EMA20 (and/or the chart EMA20) is not sloping in the
trade direction?  CBC already has this input (v9.73-v9.76, default Off): "Skip setups when HTF EMA slope is against
the trade / min slope (pts)" with Off / HTF EMA9 / HTF EMA20 / Both EMA9 + EMA20. Slope = live 15m EMA now minus its
value one HTF candle (5 chart candles) ago; long needs slope >= min, short <= -min; applies to every trigger.

Simulator: chop_sim.py (CBC v10.35-style setup engine incl. current ER/breakout rule, R5/X4 gates and v10.31 exits;
~50 % exact match with real setups, so compare variants rather than absolute numbers). Bars: BarFeed archive 01/05 ->
today (MES.json / MGC.json in the cwd). Each variant changes ONE thing vs current (gate Off).
z = change / (per-trade SD x sqrt(setups changed)); "robust" = z >= 2 and better in all three thirds; "promising" =
z >= 1 and better in all three thirds.
"""
import json, sys, datetime as D
import numpy as np, pandas as pd
import chop_sim as cs

HK = 5


def load(sym, tf=3):
    B = pd.DataFrame(json.load(open(sym + '.json'))).sort_values('t').drop_duplicates('t').reset_index(drop=True)
    for c in B.columns:
        if c != 'fl':
            B[c] = pd.to_numeric(B[c], errors='coerce')
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // (5 * tf)).astype(str)
    B['last'] = B.groupby('hk').t.transform('max')
    B['hf'] = B['hf'].fillna(0)
    return B


def features(s):
    lag = lambda x: np.r_[np.full(HK, np.nan), x[:-HK]]
    s9, s20, l20 = s.h9 - lag(s.h9), s.h20 - lag(s.h20), s.e20 - lag(s.e20)
    for d in s.cands:
        i, g = d['i'], (1 if d['lg'] else -1)
        d['s9'], d['s20'], d['l20'] = g * s9[i], g * s20[i], g * l20[i]
        d['cl'] = g * (s.h9[i] - s.h20[i])          # HTF cloud: EMA9 above EMA20 for longs
        d['s9a'], d['s20a'] = d['s9'] / s.atr[i], d['s20'] / s.atr[i]


def mk(gate, trig=None):
    """gate(d)->True = allowed. trig: only apply the gate to these trigger types."""
    def ok(d):
        if not cs.cur_rule(d):
            return False
        if trig and d['trig'] not in trig:
            return True
        return gate(d)
    return ok


def variants():
    V = [('— current (gate Off)', lambda d: True)]
    for m in (0, .25, .5, 1.0):
        V.append(('HTF EMA9 slope with trade, min %s pt' % m, lambda d, m=m: d['s9'] >= m))
    for m in (0, .25, .5, 1.0):
        V.append(('HTF EMA20 slope with trade, min %s pt' % m, lambda d, m=m: d['s20'] >= m))
    for m in (0, .25, .5, 1.0):
        V.append(('Both HTF EMA9 + EMA20, min %s pt' % m, lambda d, m=m: min(d['s9'], d['s20']) >= m))
    V += [('Either HTF EMA9 or EMA20 with trade (not in CBC)', lambda d: max(d['s9'], d['s20']) >= 0),
          ('Chart EMA20 slope with trade (not in CBC)', lambda d: d['l20'] >= 0),
          ('Chart EMA20 + HTF EMA9 + HTF EMA20 all with trade (not in CBC)', lambda d: min(d['s9'], d['s20'], d['l20']) >= 0),
          ('HTF cloud with trade: EMA9 beyond EMA20 (not in CBC)', lambda d: d['cl'] >= 0),
          ('HTF EMA9 slope >= 0.1 ATR (not in CBC)', lambda d: d['s9a'] >= .1),
          ('HTF EMA20 slope >= 0.1 ATR (not in CBC)', lambda d: d['s20a'] >= .1)]
    return V


TRIGSETS = [('all triggers', None), ('pierces only (LTF20/HTF9/HTF20)', ('ltf20', 'h9', 'h20'))]
TN = {'flip': 'HTF CBC Flip', 'ltf20': 'LTF EMA20 Pierce', 'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}


def thirds(res, months):
    return [sum(r['res'] for r in res if lo <= months[r['i']] <= hi) for lo, hi in ((1, 3), (4, 6), (7, 12))]


def study(sym):
    B = load(sym)
    s = cs.Case(sym, 3, B)
    features(s)
    cur = s.run(mk(lambda d: True))
    cn = sum(r['res'] for r in cur)
    sd = float(np.std([r['res'] for r in cur])) or 1
    t0 = thirds(cur, s.month)
    curset = {(r['i'], r['lg']) for r in cur}
    first, last = [D.datetime.fromtimestamp(B.t.iloc[k] / 1000).strftime('%m/%d') for k in (0, -1)]
    L = ['## %s 3m — %s to %s · current: %d setups, net %+.0f (thirds %+.0f / %+.0f / %+.0f), SD %.1f' % (sym, first, last, len(cur), cn, *t0, sd), '']
    # how often each EMA is against the trade at current setups, and what those setups made
    L += ['**Current setups split by EMA direction at entry (slope over the last 5 candles)**', '',
          '| Trigger | N | HTF EMA9 with / against (net) | HTF EMA20 with / against (net) | Chart EMA20 with / against (net) | Both HTF with / not (net) |', '|---|---|---|---|---|---|']
    for tg in (None, 'flip', 'ltf20', 'h9', 'h20'):
        g = [r for r in cur if tg is None or r['trig'] == tg]
        if not g:
            continue
        def sp(f):
            a = [r for r in g if f(r)]; b = [r for r in g if not f(r)]
            return '%d %+.0f / %d %+.0f' % (len(a), sum(r['res'] for r in a), len(b), sum(r['res'] for r in b))
        L.append('| %s | %d | %s | %s | %s | %s |' % (TN.get(tg, 'All'), len(g), sp(lambda r: r['s9'] >= 0), sp(lambda r: r['s20'] >= 0),
                                                 sp(lambda r: r['l20'] >= 0), sp(lambda r: min(r['s9'], r['s20']) >= 0)))
    L.append('')
    rows = []
    for tsn, ts in TRIGSETS:
        L += ['**Gate applied to %s**' % tsn, '', '| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |', '|---|---|---|---|---|---|---|']
        for name, gate in variants()[1:]:
            res = s.run(mk(gate, ts))
            net = sum(r['res'] for r in res)
            ch = len(curset ^ {(r['i'], r['lg']) for r in res}) or 1
            z = (net - cn) / (sd * np.sqrt(ch))
            dth = [a - b for a, b in zip(thirds(res, s.month), t0)]
            b3 = all(x > 0 for x in dth)
            v = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < cn else 'noise'
            L.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (name, len(res), net, net - cn, z, *dth, v))
            rows.append((tsn, name, len(res), net - cn, z, dth, v))
        L.append('')
    return '\n'.join(L), rows, s, cur


def main():
    out = ['# EMA direction gate study (MGC 3m, MES 3m) — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for sym in ('MGC', 'MES'):
        txt, rows, s, cur = study(sym)
        out += [txt, '']
        for r in rows:
            if r[6] in ('robust', 'promising'):
                summ.append('%s 3m (%s): %s → %+.0f pts, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s)' % (sym, r[0], r[1], r[3], r[4], *r[5], r[6]))
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))


if __name__ == '__main__':
    main()
