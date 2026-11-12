#!/usr/bin/env python3
"""VWAP stretch filter study (MGC 3m "...stretch x ATR per symbol" = MGC 3m 4) -- 10/30/2026.

Question: the X4 filter (no short when close > 4 ATR below VWAP, no long > 4 ATR above) blocked every MGC 3m setup on the
10/30 trend day (06:15 flip -> 09:42, ~60 pts down). Would it be better to lift it on strong-trend candles (ER(12) >= x,
HTF ER >= x, flip trigger), raise the cap, or turn it off?
Simulator: chop_sim.py (CBC-style setup engine, ER/breakout rule, R5 range gate ON), BASE exits (SL1 1.7 ATR + min 5,
TP1 1.7 ATR capped 6, 80 % at TP1, BE, trail 1.7 ATR -- live since CBC v10.45). No momentum-break trigger in the sim
(momentum breaks are already exempt live). ~50 % exact match with live setups: compare variants, not totals.
z = change / (per-trade SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and
better in all three thirds. Usage: python3 stretch_study.py [SYM TF]  (needs chop_sim.py next to it).
"""
import gzip, json, sys, time, urllib.request, datetime as D
import numpy as np, pandas as pd
import chop_sim as cs

BASE = 'https://tv-webhook-dashboard.onrender.com'
FROM = {3: '2026-01-05', 2: '2026-06-01'}
QB = {s: dict(sl=1.7, mn=5, tp=1.7, part=.8, be=True, ts=0, tr=1.7, cap=c) for s, c in (('MGC', 7), ('MES', 8))}


def get(url):
    err = None
    for k in range(4):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=300) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception as e:
            err = e
            time.sleep(30)
    raise err


def load(sym, tf):
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    B = pd.DataFrame(get('%s/bars?sym=%s&days=400&from=%s' % (BASE, key, FROM[tf]))['bars'])
    if 'live' in B:
        B = B[B['live'].isna() | (B['live'] == 0)]
    B = B.sort_values('t').drop_duplicates('t', keep='last').reset_index(drop=True)
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


def run(s, cap=4.0, er=None, her=None, flip=False, off=False):
    """cap: stretch limit in ATR; exempt when ER(12) >= er, HTF ER >= her, or trigger == flip."""
    def ok(d):
        if not cs.cur_rule(d):
            return False
        if off or d['xv'] <= cap:
            return True
        if er is not None and d['er'][12] >= er:
            return True
        if her is not None and not np.isnan(d['her']) and d['her'] >= her:
            return True
        if flip and d['trig'] == 'flip':
            return True
        return False
    G = dict(cs.GATE.get((s.sym, s.tf), dict(R5=0, MTF=0)))
    G['X4'] = 0
    return s.run(ok, q=QB[s.sym], gates=G)


def thirds(res, months, tf):
    cuts = ((1, 3), (4, 6), (7, 12)) if tf == 3 else ((6, 7), (8, 8), (9, 12))
    return [sum(r['res'] for r in res if lo <= months[r['i']] <= hi) for lo, hi in cuts]


def study(sym, tf):
    B = load(sym, tf)
    s = cs.Case(sym, tf, B)
    cur = run(s)
    cn = sum(r['res'] for r in cur); sd = float(np.std([r['res'] for r in cur])) or 1
    t0 = thirds(cur, s.month, tf); curset = {(r['i'], r['lg']) for r in cur}
    first, last = [D.datetime.fromtimestamp(B.t.iloc[k] / 1000).strftime('%m/%d') for k in (0, -1)]
    tn = 'Jan–Mar / Apr–Jun / Jul–now' if tf == 3 else 'Jun–Jul / Aug / Sep–now'
    L = ['## %s %dm — %s to %s · current (X4 = stretch cap 4 ATR): %d setups, net %+.0f (thirds %+.0f / %+.0f / %+.0f), SD %.1f'
         % (sym, tf, first, last, len(cur), cn, *t0, sd), '']
    off = run(s, off=True)
    blk = [r for r in off if r['xv'] > 4]
    if blk:
        L += ['Setups the 4-ATR cap removes (stretch-off run): %d, net %+.0f, avg %+.2f, win %d%%' % (
            len(blk), sum(r['res'] for r in blk), sum(r['res'] for r in blk) / len(blk), round(100 * sum(r['res'] > 0 for r in blk) / len(blk))), '']
        L += ['| Stretched setups by ER(12) | N | Win % | Net | Avg |', '|---|---|---|---|---|']
        for lo, hi in ((0, .3), (.3, .4), (.4, .5), (.5, 2)):
            g = [r for r in blk if lo <= r['er'][12] < hi]
            if g:
                L.append('| %.1f–%s | %d | %d%% | %+.0f | %+.2f |' % (lo, '%.1f' % hi if hi < 2 else '1', len(g), round(100 * sum(r['res'] > 0 for r in g) / len(g)), sum(r['res'] for r in g), sum(r['res'] for r in g) / len(g)))
        L.append('')
    L += ['| Variant | Setups | Net | Δ vs current | z | Δ by third (%s) | Verdict |' % tn, '|---|---|---|---|---|---|---|']
    V = [('Stretch filter OFF', dict(off=True))]
    V += [('Cap %d ATR' % c, dict(cap=float(c))) for c in (5, 6, 8)]
    V += [('Cap 4 + exempt when ER(12) >= %.1f' % e, dict(er=e)) for e in (.3, .4, .5, .6)]
    V += [('Cap 4 + exempt when HTF ER >= %.1f' % e, dict(her=e)) for e in (.4, .5, .6)]
    V += [('Cap 4 + exempt HTF CBC Flip setups', dict(flip=True))]
    rows = []
    for nm, kw in V:
        res = run(s, **kw)
        net = sum(r['res'] for r in res)
        ch = len(curset ^ {(r['i'], r['lg']) for r in res}) or 1
        z = (net - cn) / (sd * np.sqrt(ch))
        dth = [a - b for a, b in zip(thirds(res, s.month, tf), t0)]
        b3 = all(x > 0 for x in dth)
        v = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < cn else 'noise'
        L.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (nm, len(res), net, net - cn, z, *dth, v))
        rows.append((nm, net - cn, z, dth, v, res))
    # today
    td = [r for r in off if s.date[r['i']].startswith(D.datetime.now().strftime('%m/%d'))]
    if td:
        L += ['', '**Today (%s), stretch OFF run:** ' % D.datetime.now().strftime('%m/%d') + '; '.join(
            '%s %s %s %.1f ATR ER %.2f -> %+.1f (%s)' % (s.date[r['i']][6:], 'L' if r['lg'] else 'S', r['trig'], r['xv'], r['er'][12], r['res'], r['why']) for r in td)]
    return '\n'.join(L), rows


def main():
    cases = [(sys.argv[1], int(sys.argv[2]))] if len(sys.argv) > 2 else [('MGC', 3)]
    out = ['# VWAP stretch filter study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for sym, tf in cases:
        txt, rows = study(sym, tf)
        out += [txt, '']
        summ += ['%s %dm: %s → %+.0f pts, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s)' % (sym, tf, r[0], r[1], r[2], *r[3], r[4]) for r in rows if r[4] in ('robust', 'promising')]
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))


if __name__ == '__main__':
    main()
