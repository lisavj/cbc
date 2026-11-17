"""Equal highs / lows on 15m / 30m / 60m / 240m -- skip a long when an untaken EQH is close above the entry (short: EQL below) --
CBC EMA Slope current 3m settings (v1.19 logic = v1.22 / v1.23), MES / MGC / MNQ / M2K 3m -- 11/17/2026.
EQH / EQL: higher-timeframe candles built from the 3m bars (15m = CBC HTF candles; 30m / 60m / 240m from the 18:00 ET session start, so
240m = CME 4-hour candles). Swing high = a candle whose high is the highest of 3 candles each side (confirmed 3 candles later, no look-ahead).
Two consecutive swing highs within 0.10 x that timeframe's ATR(14) = EQH at the higher of the two (CBC's own EQH rule: ATR multiple 0.10);
it stays "untaken" until a later 3m high trades above it (swept). EQL mirrored. Only levels known at the setup candle's close count.
Gate: skip the long when the nearest untaken EQH above the entry is within x (x = 0.5 / 1 / 1.5 x TP1 distance, or 1 / 2 x 3m ATR);
short mirrored with EQL. TP1 distance = the chart's TP1 (ATR x mult, capped). Entry filter: skipping can change later setups.
Exits / filters = noflip_study.py CH bases (current settings, flip close ON). Net after costs. z = Δ / (SD x sqrt(trades changed));
robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd, datetime as D, collections
import chop_sim as cs, ema716_eng as eng
import noflip_study as nf
import os
TFS = (15, 30, 60, 240); R = 3; TOL = float(os.environ.get("EQTOL", ".10"))
def eq_levels(B, tf, H, L, C):
    T = B.t.values; et = pd.to_datetime(T, unit='ms', utc=True).tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).total_seconds() // 60).astype(int)
    key = pd.Series(start.strftime('%Y-%m-%d')) + '_' + pd.Series(mins // tf).astype(str)
    g = pd.DataFrame({'k': key.values, 'h': H, 'l': L, 'c': C, 'i': np.arange(len(H))}).groupby('k', sort=False).agg(h=('h', 'max'), l=('l', 'min'), c=('c', 'last'), e=('i', 'max'))
    gh, gl, gc, ge = g.h.values, g.l.values, g.c.values, g.e.values; m = len(gh)
    pc = np.r_[gc[0], gc[:-1]]; tr = np.maximum(gh, pc) - np.minimum(gl, pc); atr = cs.rma(tr, 14)
    out = {1: [], -1: []}   # 1 = EQH: (avail bar, level, swept bar); -1 = EQL
    for side, X in ((1, gh), (-1, gl)):
        prev = None
        for k in range(R, m - R):
            w = X[k - R:k + R + 1]
            if not (X[k] == (w.max() if side == 1 else w.min())): continue
            av = ge[k + R]   # confirmed when candle k+R closes
            if prev is not None and abs(X[k] - X[prev]) <= TOL * atr[k + R]:
                lvl = max(X[k], X[prev]) if side == 1 else min(X[k], X[prev])
                out[side].append((av, lvl))
            prev = k
    res = {}
    for side in (1, -1):
        lst = []
        for av, lvl in out[side]:
            seg = (H[av + 1:] > lvl) if side == 1 else (L[av + 1:] < lvl)
            j = np.argmax(seg) if seg.any() else None
            lst.append((av, lvl, av + 1 + j if j is not None else 10 ** 9))
        res[side] = lst
    return res
def nearest(levels, side, i, c):
    best = np.inf
    for av, lvl, sw in levels[side]:
        if av <= i and sw > i:
            d = (lvl - c) if side == 1 else (c - lvl)
            if d >= 0 and d < best: best = d
    return best
def runsym(sym):
    X = nf.CH[sym]; B = eng.load(sym, 3, X['f']); h20raw = B.h20.values.astype(float); o = X['base']
    P = dict(nf.TDEF, fdp=X['fdp'], tw=X['tw'], erl=o.get('erl', .08)); P.update(o.get('P', {}))
    nf.TCase.P = P; s = nf.TCase(sym, 3, B); s.P = P
    C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n; q = X['q']
    hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values
    SLP = np.abs(h20raw - np.roll(h20raw, o.get('slk', 12))) / A
    rg, x4, slope, hb = o.get('rg', 0), o.get('x4', 0), o.get('slope', 0), o.get('hb', ())
    LV = {tf: eq_levels(B, tf, H, L, C) for tf in TFS}
    cnt = {tf: (len(LV[tf][1]), len(LV[tf][-1])) for tf in TFS}
    DIST = {}
    def dist(i, lg, tf):
        k = (i, lg, tf)
        if k not in DIST: DIST[k] = nearest(LV[tf], 1 if lg else -1, i, C[i])
        return DIST[k]
    def ok_base(d):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
        if not cs.cur_rule(d): return False
        w = hh24[i] - ll24[i]
        if rg and w > 0 and w / a < rg and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        if x4 and g * (C[i] - s.vw[i]) / a > x4: return False
        if slope and SLP[i] < slope: return False
        if hb and ((s.hm[i] - 3) % 1440) // 60 in hb: return False
        return True
    tpd = lambda i: min(q['tp'] * A[i], q['tcap'])
    T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def sc(gate=None):
        ok = ok_base if gate is None else (lambda d: ok_base(d) and not gate(d))
        R_ = s.run(ok, dict(q, nf=0), False); v = np.array([r['res'] - X['cost'] for r in R_]); eq = np.cumsum(v)
        th = [sum(r['res'] - X['cost'] for r in R_ if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std() or 1, th=th, l4=sum(r['res'] - X['cost'] for r in R_ if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(r['i'], r['lg']): r['res'] - X['cost'] for r in R_}, R=R_)
    b = sc(); rows = []; cand = []
    def cmp(a, nm):
        ch = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d_ = [p - q_ for p, q_ in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
        vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
        rows.append('| %s | %d | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['avg'], a['net'] - b['net'], z, *d_, l4, a['dd'], vd))
        if vd in ('robust', 'promising'): cand.append('- %s 3m: %s %+.0f (z %+.1f, %+.0f / %+.0f / %+.0f, last 4 wk %+.0f) %s' % (sym, nm, a['net'] - b['net'], z, *d_, l4, vd))
    for tf in TFS + ('any',):
        tfs = TFS if tf == 'any' else (tf,)
        lab = 'any of 15/30/60/240m' if tf == 'any' else '%dm' % tf
        for xn, xf in (('0.5 x TP1', lambda i: .5 * tpd(i)), ('1 x TP1', lambda i: tpd(i)), ('1.5 x TP1', lambda i: 1.5 * tpd(i)), ('1 ATR', lambda i: A[i]), ('2 ATR', lambda i: 2 * A[i])):
            g = lambda d, tfs=tfs, xf=xf: min(dist(d['i'], d['lg'], t) for t in tfs) < xf(d['i'])
            cmp(sc(g), 'Skip: %s EQH/EQL within %s' % (lab, xn))
        print(sym, tf, file=sys.stderr, flush=True)
    # diagnostic: the current trades split by an EQH/EQL within 1 x TP1 (target side) on each timeframe
    dg = ['', '| Timeframe | Trades with EQH/EQL within 1 x TP1: n / net / avg / win | Others: n / net / avg / win | Within 1 x TP1 by third |', '|---|---|---|---|']
    for tf in TFS:
        a_ = [r for r in b['R'] if dist(r['i'], r['lg'], tf) < tpd(r['i'])]; o_ = [r for r in b['R'] if not dist(r['i'], r['lg'], tf) < tpd(r['i'])]
        f = lambda Rr: (len(Rr), sum(r['res'] - X['cost'] for r in Rr), np.mean([r['res'] - X['cost'] for r in Rr]) if Rr else 0, 100 * np.mean([r['res'] - X['cost'] > 0 for r in Rr]) if Rr else 0)
        th = [sum(r['res'] - X['cost'] for r in a_ if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        dg.append('| %dm | %d / %+.0f / %+.2f / %.0f %% | %d / %+.0f / %+.2f / %.0f %% | %+.0f / %+.0f / %+.0f |' % (tf, *f(a_), *f(o_), *th))
    head = ['## %s 3m (bars to %s)' % (sym, D.datetime.utcfromtimestamp(T[-1] / 1000).strftime('%m/%d')), '',
            'Current: %d trades, net %+.0f, avg %+.2f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f. EQH / EQL found: %s' % (b['n'], b['net'], b['avg'], *b['th'], b['l4'], b['dd'], ', '.join('%dm %d / %d' % (tf, *cnt[tf]) for tf in TFS)), '',
            '| Change | Trades | Net | Avg | vs current | z | Change by third | Last 4 wk | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|---|']
    return head + rows + dg + [''], cand
if __name__ == '__main__':
    out = [__doc__, '']; allc = []
    for sym in (sys.argv[1:] or ['MES', 'MGC', 'MNQ', 'M2K']):
        o_, c_ = runsym(sym); out += o_; allc += c_
    out[2:2] = ['## Candidates (promising or better)', ''] + (allc or ['- none']) + ['']
    open('eqhl_report_%s.md' % os.environ.get('EQTOL', '.10'), 'w').write('\n'.join(out)); print('\n'.join(out))
