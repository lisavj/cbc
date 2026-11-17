import sys, numpy as np, pandas as pd
src = open('ats_inputs_study.py').read().split("CFG = {")[0]
exec(src)
CFG = {'MES': dict(c=.5, x4=False, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0)),
       'MGC': dict(c=.22, x4=True, q=dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, part=0.0))}
VER = {'MES': [('v10.97', dict(slope=0, ride=False, erl=.08)), ('CBC-ES v1.04 (slope 0.30 + flip ride)', dict(slope=.30, ride=True, erl=.08)),
               ('CBC-ES v1.05 (slope 0.42)', dict(slope=.42, ride=True, erl=.08)), ('CBC-ES v1.06 (+ LTF pierce min ER 0.15)', dict(slope=.42, ride=True, erl=.15))],
       'MGC': [('v10.97', dict(slope=0, ride=False, erl=.08)), ('CBC-ES v1.04-v1.06 (slope 0.30)', dict(slope=.30, ride=False, erl=.08))]}
def dd(v):
    if not len(v): return 0.
    eq = np.cumsum(v); return float((np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max())
out = []
for sym in ('MES', 'MGC'):
    x = CFG[sym]; B = eng.load(sym, 3, '/tmp/%s3.pkl' % sym.lower()); h20raw = B.h20.values.astype(float)
    rows = []
    for nm, o in VER[sym]:
        P = dict(DEF, erl=o['erl']); PCase.P = P; s = PCase(sym, 3, B)
        C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n
        hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values; SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A
        def ok(d):
            i, lg = d['i'], d['lg']
            if not cs.cur_rule(d): return False
            w = hh24[i] - ll24[i]
            if w > 0 and w / A[i] < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
            return not (o['slope'] and SLP[i] < o['slope'])
        R = [dict(r) for r in s.run(ok, x['q'], x['x4'])]
        if o['ride']:
            for k, r in enumerate(R):
                if r['trig'] != 'flip': continue
                i, lg = r['i'], r['lg']; stop = R[k + 1]['i'] if k + 1 < len(R) else -1; en = C[i]; g = 1 if lg else -1; sd = max(3 * A[i], 5); slv = en - g * sd; res = 0.
                for j in range(i + 1, N):
                    if (L[j] <= slv) if lg else (H[j] >= slv): res = -sd; break
                    if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop: res = g * (C[j] - en); break
                r['res'] = res
        T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
        th = lambda t: 0 if t < cuts[0] else 1 if t < cuts[1] else 2
        v = np.array([r['res'] - x['c'] for r in R]); tt = np.array([th(T[r['i']]) for r in R]); l4 = np.array([T[r['i']] >= t4 for r in R])
        rows.append((nm, len(v), 100 * (v > 0).mean(), v.sum(), [v[tt == k].sum() for k in range(3)], [dd(v[tt == k]) for k in range(3)], v[l4].sum(), dd(v[l4]), dd(v), [int((tt == k).sum()) for k in range(3)]))
    fmt = lambda t: pd.Timestamp(t, unit='ms').strftime('%m/%d')
    out += ['### %s 3m (thirds %s–%s / %s–%s / %s–%s; last 4 wk from %s)' % (sym, fmt(T0), fmt(cuts[0]), fmt(cuts[0]), fmt(cuts[1]), fmt(cuts[1]), fmt(T1), fmt(t4)), '',
            '| Version | Setups | Win % | Net | Third 1 net / DD | Third 2 net / DD | Third 3 net / DD | Last 4 wk net / DD | Max DD (whole) |', '|---|---|---|---|---|---|---|---|---|']
    for nm, n, w, net, th3, d3, l4n, l4d, mdd, n3 in rows:
        out.append('| %s | %d | %.0f %% | %+.0f | %+.0f / %.0f | %+.0f / %.0f | %+.0f / %.0f | %+.0f / %.0f | %.0f |' % (nm, n, w, net, th3[0], d3[0], th3[1], d3[1], th3[2], d3[2], l4n, l4d, mdd))
    b = rows[0]; c = rows[-1]
    out += ['', 'Change %s vs v10.97: net %+.0f; thirds %+.0f / %+.0f / %+.0f; third drawdowns %+.0f / %+.0f / %+.0f; last 4 wk %+.0f; max DD %+.0f.' % (
        c[0].split(' (')[0], c[3] - b[3], *[c[4][k] - b[4][k] for k in range(3)], *[c[5][k] - b[5][k] for k in range(3)], c[6] - b[6], c[8] - b[8]), '']
print('\n'.join(out)); open('vcmp_report.md', 'w').write('\n'.join(out))
