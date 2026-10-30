#!/usr/bin/env python3
"""Room-to-resistance study (CBC v10.47 "room" gate / TP1-before-level option) -- MGC 3m, MES 3m, MGC 2m, MES 2m.

Question: does a setup whose first opposing level sits close in front of TP1 do worse, and would CBC do better by
(a) skipping setups with the first opposing level within x * TP1 ("Skip setup if the first opposing level / OB is within
x x TP1"), or (b) moving TP1 to just before that level ("TP1 just before the first opposing level", min 0.5 / 1.0 ATR)?
Origin: 10/29 live check -- MES 3m setups with a level inside half the TP1 distance -1.77/setup vs +0.07; MGC 3m with an
opposing OB before TP1 -1.63 vs +0.33 (both halves).

Simulator: chop_sim.py (CBC-style setup engine, current ER/breakout rule, R5/X4/MTF gates), with the BASE exits on every
case (SL1 1.7 ATR + min 5, TP1 1.7 ATR capped at 6 pts, 80 % at TP1, breakeven, trail 1.7 ATR -- live on all charts since
CBC v10.45). Level pool per bar = classic PP/R1/S1, prior-day H/L, NY/London/Asia opening-range H/L, VWAP, EMA200, last LTF
swing H/L (N=2) and last HTF swing H/L (N=2 on the HTF candles). Lux order blocks are NOT in the sim pool (live alerts have
them) -- so the sim under-counts close levels a little. ~50 % exact match with real setups: compare variants, not totals.
z = change / (per-trade SD x sqrt(setups changed)); "robust" = z >= 2 and better in all three thirds; "promising" = z >= 1
and better in all three thirds. Usage: python3 room_study.py  (needs chop_sim.py next to it; downloads the bar archive).
"""
import gzip, json, time, urllib.request, datetime as D
import numpy as np, pandas as pd
import chop_sim as cs

BASE = 'https://tv-webhook-dashboard.onrender.com'
CASES = [('MGC', 3), ('MES', 3), ('MGC', 2), ('MES', 2)]
FROM = {3: '2026-01-05', 2: '2026-06-01'}
QB = {s: dict(sl=1.7, mn=5, tp=1.7, part=.8, be=True, ts=0, tr=1.7, cap=c) for s, c in (('MGC', 7), ('MES', 8))}


def get(url):
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
            time.sleep(60)
    raise err


def load(sym, tf):
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    B = pd.DataFrame(get('%s/bars?sym=%s&days=400&from=%s' % (BASE, key, FROM[tf]))['bars'])
    B = B.sort_values('t').drop_duplicates('t').reset_index(drop=True)
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


def htf_swings(s):
    """last confirmed HTF swing high / low (N=2 on HTF candles), known from the close of the confirming HTF candle."""
    B = s.B
    g = pd.DataFrame({'k': B.hk.values, 'h': s.H, 'l': s.L, 'i': np.arange(s.n)}).groupby('k', sort=False).agg(h=('h', 'max'), l=('l', 'min'), last=('i', 'max'))
    H, L, I = g.h.values, g.l.values, g.last.values
    sh = np.full(s.n, np.nan); sl = np.full(s.n, np.nan); ch = cl = np.nan; p = 0
    ev = []
    for j in range(4, len(g)):
        c = j - 2
        if H[c] > max(H[c - 2:c]) and H[c] >= max(H[c + 1:c + 3]):
            ev.append((I[j], 'h', H[c]))
        if L[c] < min(L[c - 2:c]) and L[c] <= min(L[c + 1:c + 3]):
            ev.append((I[j], 'l', L[c]))
    ev.sort()
    for i in range(s.n):
        while p < len(ev) and ev[p][0] <= i:
            if ev[p][1] == 'h':
                ch = ev[p][2]
            else:
                cl = ev[p][2]
            p += 1
        sh[i], sl[i] = ch, cl
    return sh, sl


def add_room(s):
    B = s.B
    cols = [B[c].values.astype(float) for c in ('pp', 'r1', 's1', 'ydh', 'ydl', 'nyh', 'nyl', 'lnh', 'lnl', 'ash', 'asl') if c in B]
    hsh, hsl = htf_swings(s)
    pool = np.vstack(cols + [s.vw.astype(float), s.e200.astype(float), np.r_[np.nan, s.swh[:-1]], np.r_[np.nan, s.swl[:-1]], hsh, hsl])
    for d in s.cands:
        i, lg = d['i'], d['lg']
        en = s.C[i]
        v = pool[:, i]
        dist = (v - en) if lg else (en - v)
        dist = dist[~np.isnan(dist) & (dist > 0)]
        A = s.atr[i]
        d['tpd'] = min(1.7 * A, 6)
        d['room'] = float(dist.min()) if len(dist) else np.nan
        d['ratio'] = d['room'] / d['tpd'] if len(dist) else np.inf


def sim1_room(s, i, lg, q, stop_at, tpd_over=None):
    """chop_sim Case.sim1 with an optional TP1 distance override."""
    C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
    sd = min(max(q['sl'] * A, q['mn']), q['cap']); tpd = tpd_over if tpd_over else min(q['tp'] * A, 6)
    sl = en - g * sd; t1 = en + g * tpd; hit = False; best = 0
    for j in range(i + 1, s.n):
        if (L[j] <= sl if lg else H[j] >= sl):
            rem = g * (sl - en); return (q['part'] * tpd + (1 - q['part']) * rem if hit else rem), j, ('trail' if hit else 'SL1')
        if not hit and (H[j] >= t1 if lg else L[j] <= t1):
            hit = True
            if q['be']: sl = max(sl, en) if lg else min(sl, en)
        best = max(best, g * ((H[j] if lg else L[j]) - en))
        if hit:
            ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
        why = None
        if s.hdir[j] == (0 if lg else 1): why = 'flip'
        elif s.hm[j] == 16 * 60: why = '16:00'
        elif j == stop_at: why = 'new'
        if why:
            rem = g * (C[j] - en); return (q['part'] * tpd + (1 - q['part']) * rem if hit else rem), j, why
    return 0.0, s.n - 1, 'end'


def run(s, gate_x=None, tp_min=None):
    """gate_x: skip when room < gate_x * TP1; tp_min: TP1 -> room - tick when room < TP1 and room - tick >= tp_min * ATR."""
    tick = .1 if s.sym == 'MGC' else .25
    TPO = {}
    def ok(d):
        if not cs.cur_rule(d):
            return False
        if gate_x is not None and d['ratio'] < gate_x:
            return False
        if tp_min is not None:
            r = d['room'] - tick
            TPO[d['i']] = r if (not np.isnan(r) and r < d['tpd'] and r >= tp_min * s.atr[d['i']]) else None
        return True
    orig = s.sim1
    s.sim1 = lambda i, lg, q, stop_at: sim1_room(s, i, lg, q, stop_at, TPO.get(i))
    try:
        return s.run(ok, q=QB[s.sym])
    finally:
        s.sim1 = orig


def thirds(res, months, tf):
    cuts = ((1, 3), (4, 6), (7, 12)) if tf == 3 else ((6, 7), (8, 8), (9, 12))
    return [sum(r['res'] for r in res if lo <= months[r['i']] <= hi) for lo, hi in cuts]


def study(sym, tf):
    B = load(sym, tf)
    s = cs.Case(sym, tf, B)
    add_room(s)
    cur = run(s)
    cn = sum(r['res'] for r in cur); sd = float(np.std([r['res'] for r in cur])) or 1
    t0 = thirds(cur, s.month, tf); curset = {(r['i'], r['lg']) for r in cur}
    first, last = [D.datetime.fromtimestamp(B.t.iloc[k] / 1000).strftime('%m/%d') for k in (0, -1)]
    tn = 'Jan–Mar / Apr–Jun / Jul–now' if tf == 3 else 'Jun–Jul / Aug / Sep–now'
    L = ['## %s %dm — %s to %s · current (base exits, no room rule): %d setups, net %+.0f (thirds %+.0f / %+.0f / %+.0f), SD %.1f'
         % (sym, tf, first, last, len(cur), cn, *t0, sd), '',
         '**Current setups by room to the first opposing level (x TP1)**', '', '| Room | N | Win % | Net | Avg |', '|---|---|---|---|---|']
    for lo, hi, nm in ((0, .25, '< 0.25'), (.25, .5, '0.25–0.5'), (.5, .75, '0.5–0.75'), (.75, 1, '0.75–1'), (1, 9e9, '>= 1 / none')):
        g = [r for r in cur if lo <= r['ratio'] < hi]
        if g:
            L.append('| %s | %d | %d%% | %+.0f | %+.2f |' % (nm, len(g), round(100 * sum(r['res'] > 0 for r in g) / len(g)), sum(r['res'] for r in g), sum(r['res'] for r in g) / len(g)))
    L += ['', '| Variant | Setups | Net | Δ vs current | z | Δ by third (%s) | Verdict |' % tn, '|---|---|---|---|---|---|---|']
    V = [('Skip if room < %s x TP1' % x, dict(gate_x=x)) for x in (.25, .5, .75, 1.0)]
    V += [('TP1 just before the level (min %s ATR)' % m, dict(tp_min=m)) for m in (.5, 1.0)]
    V += [('Skip if room < 0.25 x TP1 + TP1 before the level (min 0.5 ATR)', dict(gate_x=.25, tp_min=.5))]
    rows = []
    for nm, kw in V:
        res = run(s, **kw)
        net = sum(r['res'] for r in res)
        ch = len(curset ^ {(r['i'], r['lg']) for r in res}) or sum(1 for a, b in zip(cur, res) if abs(a['res'] - b['res']) > 1e-9) or 1
        z = (net - cn) / (sd * np.sqrt(ch))
        dth = [a - b for a, b in zip(thirds(res, s.month, tf), t0)]
        b3 = all(x > 0 for x in dth)
        v = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < cn else 'noise'
        L.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (nm, len(res), net, net - cn, z, *dth, v))
        rows.append((nm, net - cn, z, dth, v))
    return '\n'.join(L), rows


def main():
    out = ['# Room-to-resistance study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    summ = []
    for sym, tf in CASES:
        try:
            txt, rows = study(sym, tf)
        except Exception as e:
            out += ['## %s %dm' % (sym, tf), '', 'error: %s' % e, '']
            continue
        out += [txt, '']
        summ += ['%s %dm: %s → %+.0f pts, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s)' % (sym, tf, r[0], r[1], r[2], *r[3], r[4]) for r in rows if r[4] in ('robust', 'promising')]
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))


if __name__ == '__main__':
    main()
