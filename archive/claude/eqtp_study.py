"""Untaken equal high / low (EQH / EQL) as the take-profit -- CBC EMA Slope current 3m settings -- MES (+ MGC / MNQ / M2K) -- 11/18/2026.
Follow-up to claude/eqhl_report.md (11/17): MES trades with a 15m EQH/EQL within 1 x TP1 averaged +2.19 vs +1.12 (27 trades).
EQH / EQL = claude/eqhl_study.py (15m / 30m / 60m candles from the 3m bars, swing R = 3 each side, two consecutive swings within
TOL x that timeframe's ATR, untaken until a later 3m high/low trades through; only levels known at the setup candle's close).
Exit change (entries unchanged): when the nearest untaken EQH above a long (EQL below a short) is within [lo, hi] x TP1 distance,
TP1 is moved to the level - 0.1 ATR ("front"), or level + 0.1 ATR ("through" = past the level, catching the sweep).
'ext' = only when the level is beyond TP1 (TP1 pushed out), 'tight' = only when inside TP1 (TP1 pulled in).
'ride' = MES flip-ride trades (no TP today) also get the level as a TP. Everything else = live exits (noflip_study.py CH).
Net after costs. z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, os, glob, numpy as np, pandas as pd, datetime as D
import chop_sim as cs, ema716_eng as eng, noflip_study as nf, eqhl_study as eqs
TOL = float(os.environ.get('EQTOL', '.25')); eqs.TOL = TOL
def runsym(sym):
    X = nf.CH[sym]; B = eng.load(sym, 3, X['f']); h20raw = B.h20.values.astype(float); o = X['base']
    P = dict(nf.TDEF, fdp=X['fdp'], tw=X['tw'], erl=o.get('erl', .08)); P.update(o.get('P', {}))
    nf.TCase.P = P; s = nf.TCase(sym, 3, B); s.P = P
    C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n; q0 = X['q']
    hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values
    SLP = np.abs(h20raw - np.roll(h20raw, o.get('slk', 12))) / A
    rg, x4, slope, hb = o.get('rg', 0), o.get('x4', 0), o.get('slope', 0), o.get('hb', ())
    LV = {tf: eqs.eq_levels(B, tf, H, L, C) for tf in (15, 30, 60)}
    DC = {}
    def dist(i, lg, tfs):
        k = (i, lg, tfs)
        if k not in DC: DC[k] = min(eqs.nearest(LV[t], 1 if lg else -1, i, C[i]) for t in tfs)
        return DC[k]
    def ok(d):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
        if not cs.cur_rule(d): return False
        w = hh24[i] - ll24[i]
        if rg and w > 0 and w / a < rg and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        if x4 and g * (C[i] - s.vw[i]) / a > x4: return False
        if slope and SLP[i] < slope: return False
        if hb and ((s.hm[i] - 3) % 1440) // 60 in hb: return False
        return True
    tpd = lambda i: min(q0['tp'] * A[i], q0['tcap'])
    orig = nf.TCase.sim1; MODE = {'m': None}
    def sim1(self, i, lg, q, stop_at, trig=''):
        m = MODE['m']
        if m is None: return orig(self, i, lg, q, stop_at, trig)
        tfs, lo, hi, place, ride_too = m
        ride = q.get('ride') and trig == 'flip'
        if ride and not ride_too: return orig(self, i, lg, q, stop_at, trig)
        d = dist(i, lg, tfs); t = tpd(i)
        if d < np.inf and lo * t <= d <= hi * t:
            nt = d + (.1 if place == 'through' else -.1) * A[i]
            if nt > .2 * A[i]:
                q = dict(q, tp=nt / A[i], tcap=1e9)
                if ride: q.update(ride=False, part=1.0)
        return orig(self, i, lg, q, stop_at, trig)
    nf.TCase.sim1 = sim1
    T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def sc(mode=None):
        MODE['m'] = mode; R = s.run(ok, dict(q0, nf=0), False); MODE['m'] = None
        v = np.array([r['res'] - X['cost'] for r in R]); eq = np.cumsum(v)
        th = [sum(r['res'] - X['cost'] for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        return dict(n=len(v), net=v.sum(), sd=v.std() or 1, th=th, l4=sum(r['res'] - X['cost'] for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(r['i'], r['lg']): r['res'] - X['cost'] for r in R})
    b = sc(); rows = []; best = []
    TF = {'15m': (15,), '30m': (30,), '60m': (60,), '15/30/60m': (15, 30, 60)}
    WIN = {'0.5-1.5 x TP1': (.5, 1.5), 'tight 0.5-1': (.5, 1.0), 'ext 1-1.5': (1.0, 1.5), 'ext 1-2': (1.0, 2.0)}
    V = [(tn, wn, pl, False) for tn in TF for wn in WIN for pl in ('front', 'through')]
    if sym == 'MES': V += [(tn, '0.5-1.5 x TP1', pl, True) for tn in TF for pl in ('front', 'through')]
    for tn, wn, pl, rt in V:
        a = sc((TF[tn], *WIN[wn], pl, rt))
        ch = sum(1 for kk in set(a['K']) | set(b['K']) if abs(a['K'].get(kk, 1e9) - b['K'].get(kk, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
        vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
        nm = '%s EQH/EQL %s, %s%s' % (tn, wn, pl, ' + ride trades' if rt else '')
        rows.append('| %s | %d | %+.0f | %+.0f | %d | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f %% | %.0f (%+.0f) | %s |' % (nm, a['n'], a['net'], a['net'] - b['net'], ch, z, *d_, l4, a['w'], a['dd'], a['dd'] - b['dd'], vd))
        if vd in ('robust', 'promising'): best.append('- %s 3m: %s %+.0f (z %+.1f, %+.0f / %+.0f / %+.0f, last 4 wk %+.0f) %s' % (sym, nm, a['net'] - b['net'], z, *d_, l4, vd))
        print(sym, rows[-1], file=sys.stderr, flush=True)
    nf.TCase.sim1 = orig
    return ['## %s 3m (bars to %s, tolerance %.2f)' % (sym, D.datetime.utcfromtimestamp(T[-1] / 1000).strftime('%m/%d'), TOL), '',
            'Current exits: %d trades, net %+.0f, win %.0f %%, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f.' % (b['n'], b['net'], b['w'], *b['th'], b['l4'], b['dd']), '',
            '| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |', '|---|---|---|---|---|---|---|---|---|---|---|'] + rows + [''], best
if __name__ == '__main__':
    out = [__doc__, '']; allb = []
    for sym in (sys.argv[1:] or ['MES', 'MGC', 'MNQ', 'M2K']):
        o_, b_ = runsym(sym); out += o_; allb += b_
    out[2:2] = ['## Candidates (promising or better)', ''] + (allb or ['- none']) + ['']
    open('/root/w2/eqtp_report_%s.md' % os.environ.get('EQTOL', '.25'), 'w').write('\n'.join(out)); print('\n'.join(out))
