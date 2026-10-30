#!/usr/bin/env python3
"""Breakout-exception + HTF-flip-ER variant study (MGC / MES, 3m and 2m), on the server bar archive (Jan 5 2026 -> today).

Builds on claude/chop_filter_study.md (10/24): the breakout exception and the flip ER minimum 0.23 are the parts of the ER
filter that work. This script tests variants of both with the chop simulator (claude/chop_sim.py, must sit next to this
file) and prints a markdown report. Each variant changes ONE thing vs the current v10.36 rule:
  current rule: ER(12) >= 0.23, or a breakout (close through the last swing H/L or an opening-range H/L) in the last 3 bars;
                HTF CBC Flip additionally needs ER(12) >= 0.23; per-trigger minimums LTF 0.08 / HTF EMA 0.15 unchanged.
Variants:
  1  breakout window 1 / 2 / 5 / 8 bars (current 3)
  2  clean break: close beyond the level by >= 0.25 ATR; volume: breakout candle volume >= 1.2 x its 20-bar average
  3  breakout levels: add prior-day RTH H/L, add daily pivots PP/R1/S1, swings only, opening ranges only
  6  flip ER minimum 0.15 / 0.20 / 0.26 / 0.30 / 0.35 / 0.40 (current 0.23)
  7  flip needs 15m ER (last 6 closed 15m candles) >= 0.30 / 0.40 instead of / in addition to ER(12) 0.23
  8  flip needs ER(12) rising (now > 3 bars ago) on top of 0.23
For every variant: net points, setups, change vs current, z (change / (per-trade SD x sqrt(setups changed))),
and the change in each third of the data (Jan-Mar / Apr-Jun / Jul-now). "Robust" = z >= 2 AND better in all 3 thirds.
Usage: python3 breakout_flip_study.py            (all four cases)
       python3 breakout_flip_study.py MGC 3      (one case)
"""
import sys, json, gzip, time, urllib.request, datetime as D
import numpy as np, pandas as pd
import chop_sim as cs

BASE = 'https://tv-webhook-dashboard.onrender.com'
CASES = [('MGC', 3), ('MES', 3), ('MGC', 2), ('MES', 2)]


def _fetch(url):
    req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
    for k in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                raw = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    raw = gzip.decompress(raw)
            return json.loads(raw)['bars']
        except Exception:
            if k == 2:
                raise
            time.sleep(60)


def get_bars(sym, tf):
    # one request per month: the full Jan->today 2m request makes the Render server run out of memory (502)
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    rows = []
    m = D.date(2026, 1, 1)
    today = D.date.today()
    while m <= today:
        nxt = D.date(m.year + (m.month == 12), m.month % 12 + 1, 1)
        lo = max(m, D.date(2026, 1, 5))
        rows += _fetch('%s/bars?sym=%s&from=%s&to=%s' % (BASE, key, lo.isoformat(), (nxt - D.timedelta(days=1)).isoformat()))
        m = nxt
    B = pd.DataFrame(rows).sort_values('t').drop_duplicates('t').reset_index(drop=True)
    for c in B.columns:
        if c != 'fl':
            B[c] = pd.to_numeric(B[c], errors='coerce')
    # HTF bucket key (5 x tf, anchored to the 18:00 ET session start) and the bucket's last chart candle, as databento_build
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // (5 * tf)).astype(str)
    B['last'] = B.groupby('hk').t.transform('max')
    B['hf'] = B['hf'].fillna(0)
    return B


def extra_features(s):
    """per-bar arrays for the breakout / flip variants (attached to the simulator case)."""
    C, H, L, B, n = s.C, s.H, s.L, s.B, s.n
    pc = np.r_[C[0], C[:-1]]
    vol = B['v'].values.astype(float)
    v20 = pd.Series(vol).rolling(20).mean().values
    swh = np.r_[np.nan, s.swh[:-1]]
    swl = np.r_[np.nan, s.swl[:-1]]
    groups = {
        'swing': [swh, swl],
        'or': [B[c].values for c in ('nyh', 'nyl', 'lnh', 'lnl', 'ash', 'asl')],
        'pdhl': [B['ydh'].values, B['ydl'].values],
        'piv': [B['pp'].values, B['r1'].values, B['s1'].values],
    }

    def cross(levels, clean=0.0):
        up = np.zeros(n, bool)
        dn = np.zeros(n, bool)
        for v in levels:
            pv = np.r_[np.nan, v[:-1]]
            up |= (C > v + clean * s.atr) & (pc <= pv)
            dn |= (C < v - clean * s.atr) & (pc >= pv)
        return up | dn

    def window(b, w):
        o = b.copy()
        for k in range(1, w):
            o |= np.r_[np.zeros(k, bool), b[:-k]]
        return o
    base = groups['swing'] + groups['or']
    b1 = cross(base)
    s.bov = {
        'w1': window(b1, 1), 'w2': window(b1, 2), 'w3': window(b1, 3), 'w5': window(b1, 5), 'w8': window(b1, 8),
        'clean': window(cross(base, .25), 3),
        'vol': window(b1 & (vol >= 1.2 * v20), 3),
        '+pdhl': window(cross(base + groups['pdhl']), 3),
        '+piv': window(cross(base + groups['piv']), 3),
        'swing': window(cross(groups['swing']), 3),
        'or': window(cross(groups['or']), 3),
    }
    e12 = s.er[12]
    s.er_rise = e12 > np.r_[np.full(3, np.nan), e12[:-3]]
    for d in s.cands:
        i = d['i']
        d['bov'] = {k: bool(v[i]) for k, v in s.bov.items()}
        d['rise'] = bool(s.er_rise[i])


def rule(bo='w3', thr=.23, flip_thr=.23, flip_her=None, her_mode='and', flip_rise=False):
    def ok(d):
        e = d['er'][12]
        if d['trig'] == 'flip':
            base_ok = e >= flip_thr
            if flip_her is not None:
                h = d['her'] if d['her'] == d['her'] else 0
                base_ok = (base_ok and h >= flip_her) if her_mode == 'and' else (h >= flip_her)
            if flip_rise:
                base_ok = base_ok and d['rise']
            if not base_ok:
                return False
        return e >= thr or d['bov'][bo]
    return ok


VARIANTS = [
    ('1 · breakout window 1 bar', dict(bo='w1')),
    ('1 · breakout window 2 bars', dict(bo='w2')),
    ('1 · breakout window 5 bars', dict(bo='w5')),
    ('1 · breakout window 8 bars', dict(bo='w8')),
    ('2 · clean break (>= 0.25 ATR beyond)', dict(bo='clean')),
    ('2 · breakout candle volume >= 1.2x avg', dict(bo='vol')),
    ('3 · levels + prior-day H/L', dict(bo='+pdhl')),
    ('3 · levels + PP/R1/S1', dict(bo='+piv')),
    ('3 · swings only', dict(bo='swing')),
    ('3 · opening ranges only', dict(bo='or')),
    ('6 · flip ER min 0.15', dict(flip_thr=.15)),
    ('6 · flip ER min 0.20', dict(flip_thr=.20)),
    ('6 · flip ER min 0.26', dict(flip_thr=.26)),
    ('6 · flip ER min 0.30', dict(flip_thr=.30)),
    ('6 · flip ER min 0.35', dict(flip_thr=.35)),
    ('6 · flip ER min 0.40', dict(flip_thr=.40)),
    ('7 · flip: 15m ER >= 0.30 instead of ER12', dict(flip_thr=0, flip_her=.30, her_mode='only')),
    ('7 · flip: + 15m ER >= 0.30', dict(flip_her=.30)),
    ('7 · flip: + 15m ER >= 0.40', dict(flip_her=.40)),
    ('8 · flip: + ER rising', dict(flip_rise=True)),
]


def thirds(res, months):
    out = []
    for lo, hi in ((1, 3), (4, 6), (7, 12)):
        out.append(sum(r['res'] for r in res if lo <= months[r['i']] <= hi))
    return out


def study(sym, tf):
    B = get_bars(sym, tf)
    s = cs.Case(sym, tf, B)
    extra_features(s)
    cur = s.run(rule())
    cur_net = sum(r['res'] for r in cur)
    sd = float(np.std([r['res'] for r in cur])) or 1.0
    t0 = thirds(cur, s.month)
    first = D.datetime.fromtimestamp(B.t.iloc[0] / 1000).strftime('%m/%d')
    last = D.datetime.fromtimestamp(B.t.iloc[-1] / 1000).strftime('%m/%d')
    L = ['## %s %dm — %s to %s, current rule %d setups, net %+.0f pts (thirds %+.0f / %+.0f / %+.0f), per-trade SD %.1f' % (
        sym, tf, first, last, len(cur), cur_net, t0[0], t0[1], t0[2], sd), '',
        '| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |', '|---|---|---|---|---|---|---|']
    curset = {(r['i'], r['lg']) for r in cur}
    rows = []
    for name, kw in VARIANTS:
        res = s.run(rule(**kw))
        net = sum(r['res'] for r in res)
        changed = len(curset ^ {(r['i'], r['lg']) for r in res}) or 1
        z = (net - cur_net) / (sd * np.sqrt(changed))
        th = thirds(res, s.month)
        dth = [a - b for a, b in zip(th, t0)]
        better3 = all(x > 0 for x in dth)
        verdict = 'robust' if z >= 2 and better3 else 'promising' if z >= 1 and better3 else 'worse' if net < cur_net else 'noise'
        rows.append((name, len(res), net, net - cur_net, z, dth, verdict))
        L.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (name, len(res), net, net - cur_net, z, dth[0], dth[1], dth[2], verdict))
    return '\n'.join(L), rows


def main():
    cases = CASES
    if len(sys.argv) >= 3:
        cases = [(sys.argv[1].upper(), int(sys.argv[2]))]
    out = ['# Breakout exception + flip-ER variant study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '',
           'Simulator: chop_sim.py (approximates CBC v10.36: about 50 % of real setups matched exactly, so compare variants, not absolute numbers). '
           'z = change / (per-trade SD × √setups changed); "robust" = z ≥ 2 and better in all three thirds, "promising" = z ≥ 1 and all thirds better. '
           'About 100 settings have now been tried across the studies, so expect a few z ≈ 2 results by chance.', '']
    summary = []
    for sym, tf in cases:
        try:
            txt, rows = study(sym, tf)
        except Exception as e:
            out += ['## %s %dm — error: %s' % (sym, tf, e), '']
            continue
        out += [txt, '']
        for r in rows:
            if r[6] in ('robust', 'promising'):
                summary.append('%s %dm: %s (%+.0f pts, z %+.1f, %s)' % (sym, tf, r[0], r[3], r[4], r[6]))
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summary] if summary else ['- none'])
    print('\n'.join(out))


if __name__ == '__main__':
    main()
