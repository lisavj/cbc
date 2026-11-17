import sys
exec(open('orpa_eng2.py').read())
log = lambda m: print(m, file=sys.stderr, flush=True)
VARS = [('OR session New York OFF (no NY OR levels)', dict(lv_ny=False)), ('OR session London OFF', dict(lv_ln=False)), ('OR session Asian OFF', dict(lv_as=False)), ('All three OR sessions OFF', dict(lv_ny=False, lv_ln=False, lv_as=False))]
out = ['# ㉒ Opening Range session toggles (NY / London / Asian) -- MES 3m, MGC 3m (v1.08 settings), MNQ 3m (v1.08 settings) -- 11/14/2026', '',
       'OR length (㉒, live 30 min) sets the OR-forming no-setup windows (NY 09:30, London 03:00, Asia 20:00) and the session OR highs / lows used by the ③ ER breakout exception. LTF pivot N (⑥ LTF Signals "N", live 2) sets the swing highs / lows used by the breakout exception and the Momentum break trigger (Momentum not replayed). ⑩ Price Action Structure lengths (internal 5 / swing 50) only draw HH/HL markers -- not used by setups. Breakout window = "...breakout exception" bars (live 3). OR levels recomputed from bars for every row (base included). One change at a time.', '']
top = ['## Candidates (promising or better)', '']
def sec(sym, runf):
    global out, top
    b = runf({}); rows = []
    for nm, p in VARS:
        a = runf(p); rows.append((nm, a)); z, d_, l4, vd = cmp(a, b)
        if vd in ('robust', 'robust except last 4 wk', 'promising'): top.append('- %s 3m: %s -> %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f (%s)' % (sym, nm, a['net'] - b['net'], z, *d_, l4, vd))
        log('%s %s %+.0f' % (sym, nm, a['net'] - b['net']))
    out += table('%s 3m' % sym, b, rows)
# MES / MGC via the time-blocks engine (v1.07 = v1.08 for these charts: MES 13-15 block included)
def mk(sym, extra):
    x = CFG[sym]; B = eng.load(sym, 3, '/tmp/%s3.pkl' % sym.lower()); h20raw = B.h20.values.astype(float)
    def run1(p):
        P = dict(TDEF, erl=x['erl']); P.update(extra); P.update(p); TCase.P = P; s = TCase(sym, 3, B); s.P = P; C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n
        hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values; SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A
        def ok(d):
            i, lg = d['i'], d['lg']
            if not cs.cur_rule(d): return False
            w = hh24[i] - ll24[i]
            if w > 0 and w / A[i] < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
            if SLP[i] < x['slope']: return False
            return not (P.get('hb') and ((s.hm[i] - 3) % 1440) // 60 in P['hb'])
        R = [dict(r) for r in s.run(ok, x['q'], x['x4'])]
        if x['ride']:
            for k, r in enumerate(R):
                if r['trig'] != 'flip': continue
                i, lg = r['i'], r['lg']; stop = R[k + 1]['i'] if k + 1 < len(R) else -1; en = C[i]; g = 1 if lg else -1; sd = max(3 * A[i], 5); slv = en - g * sd; res = 0.
                for j in range(i + 1, N):
                    if (L[j] <= slv) if lg else (H[j] >= slv): res = -sd; break
                    if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop: res = g * (C[j] - en); break
                r['res'] = res
        T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
        v = np.array([r['res'] - x['c'] for r in R]); eq = np.cumsum(v)
        th = [sum(r['res'] - x['c'] for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std(), th=th, l4=sum(r['res'] - x['c'] for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(T[r['i']], r['lg']): r['res'] - x['c'] for r in R})
    return run1
def cmp(a, b):
    chg = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
    z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(chg)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
    vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'robust except last 4 wk' if z >= 2 and all(t > 0 for t in d_) else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
    return z, d_, l4, vd
def table(title, base, rows):
    o = ['## ' + title, '', 'Base: %d trades, net %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f' % (base['n'], base['net'], *base['th'], base['l4'], base['dd']), '',
         '| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|']
    for nm, a in rows:
        z, d_, l4, vd = cmp(a, base)
        o.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['net'] - base['net'], z, *d_, l4, a['dd'], vd))
    return o + ['']
sec('MES', mk('MES', dict(hb=(13, 14))))
sec('MGC', mk('MGC', {}))
# MNQ via the MNQ engine (v1.08: slope 0.75, FLIP 0 %, LTF ER 0.15)
exec(open('orpa_mnq.py').read().replace("if k in ('pivn',", "if k in ('lv_ny', 'lv_ln', 'lv_as', 'pivn',").split("def cmp(a, b):")[0])
_mnq = run
sec('MNQ', lambda p: _mnq(dict(slope=.75, erl=.15, q=dict(part=0.0, tr=0), P=p)))
if len(top) == 2: top.append('- none')
rep = '\n'.join(out[:3] + top + [''] + out[3:]); open('orsess_report.md', 'w').write(rep); print(rep)
