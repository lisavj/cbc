"""Prior day / week / month high-low levels in CBC EMA Slope 3m -- MES / MGC / MNQ / M2K -- 11/18/2026.
Base = current 3m settings (claude/noflip_study.py CH = v1.19 logic = v1.23). Replay Jan 5 -> now, net after costs.
Levels (CME session days from 18:00 ET, completed periods only): PDH/PDL = prior session day, PWH/PWL = prior week, PMH/PML = prior month.
Gates (one at a time):
 R<k> <set>: skip when the nearest level of <set> in the trade direction is within k x TP1 distance (long: level above entry).
 X <set>: skip trades against an accepted break -- long while close < prior low, short while close > prior high.
 M  : prior-day midpoint side -- long only above (PDH+PDL)/2, short only below.
Exits:
 T1 : if a D/W/M level sits between entry and TP1 (and >= 0.5 x TP1 away), TP1 moves to that level minus 0.1 ATR.
 T2 : (ride trades, MES flip) close at the first D/W/M level reached (minus 0.1 ATR) instead of riding to the HTF flip.
 S1 : if a D/W/M level sits between entry and SL1 (>= 0.5 x SL1 away), SL1 moves to 0.25 ATR beyond that level (tighter only).
z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, os, glob, numpy as np, pandas as pd, datetime as D
import chop_sim as cs, ema716_eng as eng, noflip_study as nf
S = pd.Series
def levels(B, C, H, L):
    sd = pd.to_datetime(B.hk.str[:10])
    g = pd.DataFrame({'d': sd, 'h': H, 'l': L})
    out = {}
    for nm, key in (('D', sd), ('W', sd - pd.to_timedelta((sd.dt.weekday + 1) % 7, unit='D')), ('M', sd.dt.to_period('M').dt.start_time)):
        # week key: session date of Sunday (session from Sunday 18:00) -- sd is session date (= next calendar day for evening bars)
        if nm == 'W': key = sd - pd.to_timedelta(sd.dt.weekday, unit='D')   # Monday session date
        agg = g.assign(k=key.values).groupby('k').agg(h=('h', 'max'), l=('l', 'min'))
        prv = agg.shift(1)
        out[nm + 'H'] = key.map(prv.h).values.astype(float); out[nm + 'L'] = key.map(prv.l).values.astype(float)
    return out
SETS = {'D': ('D',), 'W': ('W',), 'M': ('M',), 'DWM': ('D', 'W', 'M')}
def runsym(sym):
    X = nf.CH[sym]; B = eng.load(sym, 3, X['f']); h20raw = B.h20.values.astype(float); o = X['base']
    P = dict(nf.TDEF, fdp=X['fdp'], tw=X['tw'], erl=o.get('erl', .08)); P.update(o.get('P', {}))
    nf.TCase.P = P; s = nf.TCase(sym, 3, B); s.P = P
    C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n
    LV = levels(B, C, H, L)
    hh24, ll24 = S(H).rolling(24).max().values, S(L).rolling(24).min().values
    SLP = np.abs(h20raw - np.roll(h20raw, o.get('slk', 12))) / A
    rg, x4, slope, hb = o.get('rg', 0), o.get('x4', 0), o.get('slope', 0), o.get('hb', ())
    q0 = X['q']
    def base(d):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
        if not cs.cur_rule(d): return False
        w = hh24[i] - ll24[i]
        if rg and w > 0 and w / a < rg and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        if x4 and g * (C[i] - s.vw[i]) / a > x4: return False
        if slope and SLP[i] < slope: return False
        if hb and ((s.hm[i] - 3) % 1440) // 60 in hb: return False
        return True
    def near(i, lg, st, en=None):   # distance to nearest level of set in trade direction (>0), inf if none
        en = C[i] if en is None else en; best = np.inf
        for p in st:
            for side in ('H', 'L'):
                v = LV[p + side][i]
                if np.isnan(v): continue
                d = (v - en) if lg else (en - v)
                if d > 0: best = min(best, d)
        return best
    def behind(i, lg, st):          # distance to nearest level against the trade (stop side)
        best = np.inf
        for p in st:
            for side in ('H', 'L'):
                v = LV[p + side][i]
                if np.isnan(v): continue
                d = (C[i] - v) if lg else (v - C[i])
                if d > 0: best = min(best, d)
        return best
    tp1 = lambda i: min(q0['tp'] * A[i], q0['tcap'])
    sl1 = lambda i: max(min(q0['sl'] * A[i], q0['cap']), q0['mn'])
    # exit wrapper
    orig = nf.TCase.sim1
    MODE = {'m': None}
    def sim1(self, i, lg, q, stop_at, trig=''):
        m = MODE['m']
        if m is None: return orig(self, i, lg, q, stop_at, trig)
        q = dict(q); ride = q.get('ride') and trig == 'flip'
        if m == 'T1' and not ride:
            d = near(i, lg, ('D', 'W', 'M')); t = tp1(i)
            if .5 * t <= d - .1 * A[i] < t: q['tp'] = (d - .1 * A[i]) / A[i]; q['tcap'] = 1e9
        if m == 'S1':
            d = behind(i, lg, ('D', 'W', 'M')); sd = sl1(i)
            if .5 * sd <= d + .25 * A[i] < sd: q['sl'] = (d + .25 * A[i]) / A[i]; q['cap'] = 1e9; q['mn'] = 0
        if m == 'T2' and ride:
            d = near(i, lg, ('D', 'W', 'M'))
            if d < np.inf:
                q['ride'] = False; q['tp'] = max(d - .1 * A[i], .25 * A[i]) / A[i]; q['tcap'] = 1e9; q['part'] = 1.0
        return orig(self, i, lg, q, stop_at, trig)
    nf.TCase.sim1 = sim1
    T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def sc(extra=None, mode=None):
        MODE['m'] = mode
        R = s.run(lambda d: base(d) and (extra is None or extra(d)), dict(q0, nf=0), False); MODE['m'] = None
        v = np.array([r['res'] - X['cost'] for r in R]); eq = np.cumsum(v)
        th = [sum(r['res'] - X['cost'] for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        return dict(n=len(v), net=v.sum(), sd=v.std() or 1, th=th, l4=sum(r['res'] - X['cost'] for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(r['i'], r['lg']): r['res'] - X['cost'] for r in R}, R=R)
    V = []
    for k in (.5, 1.0, 1.5):
        for st in ('D', 'W', 'M', 'DWM'):
            V.append(('R%.1f %s: skip if %s level within %.1f x TP1' % (k, st, st, k), (lambda d, k=k, st=st: near(d['i'], d['lg'], SETS[st]) >= k * tp1(d['i'])), None))
    for st in ('D', 'W', 'M'):
        def xb(d, st=st):
            i = d['i']; hi, lo = LV[st + 'H'][i], LV[st + 'L'][i]
            if np.isnan(hi): return True
            return not ((d['lg'] and C[i] < lo) or ((not d['lg']) and C[i] > hi))
        V.append(('X %s: skip trades against an accepted %s break' % (st, {'D': 'prior-day', 'W': 'prior-week', 'M': 'prior-month'}[st]), xb, None))
    V.append(('M: long only above prior-day midpoint, short only below', lambda d: np.isnan(LV['DH'][d['i']]) or ((C[d['i']] > (LV['DH'][d['i']] + LV['DL'][d['i']]) / 2) == d['lg']), None))
    V.append(('T1: TP1 at the D/W/M level when it sits inside TP1', None, 'T1'))
    V.append(('S1: SL1 just beyond the D/W/M level when it sits inside SL1', None, 'S1'))
    if sym == 'MES': V.append(('T2: flip-ride trades close at the first D/W/M level', None, 'T2'))
    b = sc(); rows = []
    # descriptive: trades by room to nearest DWM level in TP1 units
    bins = [(0, .5), (.5, 1), (1, 1.5), (1.5, 3), (3, np.inf)]; desc = []
    for lo, hi in bins:
        sel = [b['K'][(r['i'], r['lg'])] for r in b['R'] if lo <= near(r['i'], r['lg'], SETS['DWM']) / tp1(r['i']) < hi]
        desc.append('| %s | %d | %+.0f | %+.2f |' % ('%.1f-%s' % (lo, '%.1f' % hi if hi < np.inf else 'up'), len(sel), sum(sel), np.mean(sel) if sel else 0))
    for nm, f, mode in V:
        a = sc(f, mode)
        ch = sum(1 for kk in set(a['K']) | set(b['K']) if abs(a['K'].get(kk, 1e9) - b['K'].get(kk, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
        vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
        rows.append((z, '| %s | %d | %+.0f | %+.0f | %d | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f (%+.0f) | %s |' % (nm, a['n'], a['net'], a['net'] - b['net'], ch, z, *d_, l4, a['dd'], a['dd'] - b['dd'], vd)))
        print(sym, rows[-1][1], file=sys.stderr, flush=True)
    nf.TCase.sim1 = orig
    return ['## %s 3m (bars to %s)' % (sym, D.datetime.utcfromtimestamp(T[-1] / 1000).strftime('%m/%d')), '',
            'Base: %d trades, net %+.0f, win %.0f %%, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f.' % (b['n'], b['net'], b['w'], *b['th'], b['l4'], b['dd']), '',
            'Base trades by room to the nearest D/W/M level (in TP1 units):', '', '| Room | Trades | Net | Avg |', '|---|---|---|---|'] + desc + ['',
            '| Change | Trades | Net | vs base | Changed | z | Change by third | Last 4 wk | Max DD (vs base) | Verdict |', '|---|---|---|---|---|---|---|---|---|---|'] + [r for _, r in rows] + ['']
if __name__ == '__main__':
    for f in glob.glob('/tmp/m??3.pkl'): os.remove(f)
    out = [__doc__, '']
    for sym in (sys.argv[1:] or ['MES', 'MGC', 'MNQ', 'M2K']):
        out += runsym(sym)
        open('/root/w2/dwm_report.md', 'w').write('\n'.join(out))
    print('\n'.join(out))
