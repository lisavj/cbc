# ---- MNQ 3m study (CBC EMA Slope branch ideas applied to MNQ 3m) ----
class MCase3(TCase):
    def sim1(s, i, lg, q, stop_at):
        C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap']); part = q['part']
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q.get('be', True): sl = max(sl, en) if lg else min(sl, en)
            if hit and q.get('tr', 0) > 0:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.P['eod'] and s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'
SYM = 'MNQ'; COST = .87
LIVEQ = dict(sl=1.7, mn=25, cap=30, tp=1.7, tcap=40, part=.8, be=True, tr=1.7)   # v10.97 MNQ 3m: global SL1 1.7 / min 25 / cap 30, TP1 1.7 cap 40, 80 % + BE + trail 1.7
B = eng.load(SYM, 3, '/tmp/mnq3.pkl'); h20raw = B.h20.values.astype(float)
CACHE = {}
def case(P):
    key = tuple(sorted((k, str(v)) for k, v in P.items() if k in ('pivn', 'orlen', 'bn', 'orsrc', 'fdx', 'fdp', 'side', 'erl', 'erh', 'vwbn', 'atrn', 't_flip', 't_ltf', 't_h9', 't_h20', 'llate', 'hlate', 'hcol', 'qwin', 'orny', 'orln', 'oras')))
    if key not in CACHE:
        MCase3.P = P; CACHE[key] = MCase3(SYM, 3, B)
    c = CACHE[key]; c.P = P; return c
def run(o):
    P = dict(TDEF, fdp=50.0, erl=o.get('erl', .08)); P.update(o.get('P', {})); s = case(P)
    C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n; q = dict(LIVEQ, **o.get('q', {}))
    hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values; SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A
    rg = o.get('rg', 0); x4 = o.get('x4', 0); slope = o.get('slope', 0); hb = o.get('hb', ())
    def ok(d):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1
        if not cs.cur_rule(d): return False
        w = hh24[i] - ll24[i]
        if rg and w > 0 and w / A[i] < rg and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        if x4 and g * (C[i] - s.vw[i]) / A[i] > x4: return False
        if slope and SLP[i] < slope: return False
        if hb and ((s.hm[i] - 3) % 1440) // 60 in hb: return False
        return True
    R = [dict(r) for r in s.run(ok, q, False)]
    if o.get('ride'):
        for k, r in enumerate(R):
            if r['trig'] != 'flip': continue
            i, lg = r['i'], r['lg']; stop = R[k + 1]['i'] if k + 1 < len(R) else -1; en = C[i]; g = 1 if lg else -1; sd = max(min(q['sl'] * A[i], q['cap']), q['mn']); slv = en - g * sd; res = 0.
            for j in range(i + 1, N):
                if (L[j] <= slv) if lg else (H[j] >= slv): res = -sd; break
                if s.hdir[j] == (0 if lg else 1) or (P['eod'] and s.hm[j] == 960) or j == stop: res = g * (C[j] - en); break
            r['res'] = res
    T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    v = np.array([r['res'] - COST for r in R]); eq = np.cumsum(v)
    th = [sum(r['res'] - COST for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
    om = lambda r: (s.hm[r['i']] - 3) % 1440
    SES = (('Asia', lambda m: m >= 1080 or m < 180), ('London', lambda m: 180 <= m < 570), ('NY AM', lambda m: 570 <= m < 720), ('NY PM', lambda m: 720 <= m < 960))
    ses = {sn: (sum(1 for r in R if f(om(r))), sum(r['res'] - COST for r in R if f(om(r)))) for sn, f in SES}
    bt = {t: (sum(r['trig'] == t for r in R), sum(r['res'] - COST for r in R if r['trig'] == t)) for t in ('flip', 'ltf20', 'h9', 'h20')}
    return dict(n=len(v), net=v.sum(), avg=v.mean() if len(v) else 0, sd=v.std() or 1, th=th, l4=sum(r['res'] - COST for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(T[r['i']], r['lg']): r['res'] - COST for r in R}, ses=ses, bt=bt)
def cmp(a, b):
    chg = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
    z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(chg)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
    vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'robust except last 4 wk' if z >= 2 and all(t > 0 for t in d_) else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
    return z, d_, l4, vd
def table(title, base, rows):
    o = ['## ' + title, '', 'Base: %d trades, net %+.0f, avg %+.2f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f' % (base['n'], base['net'], base['avg'], *base['th'], base['l4'], base['dd']), '',
         '| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|']
    for nm, a in rows:
        z, d_, l4, vd = cmp(a, base)
        o.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['net'] - base['net'], z, *d_, l4, a['dd'], vd))
    return o + ['']
