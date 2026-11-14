"""② Setup Triggers inputs -- MES 3m and MGC 3m on CBC EMA Slope v1.06 settings -- 11/14/2026.
One change at a time. Base = v1.06: MES 3m slope 0.42 + LTF pierce min ER 0.15 + flip ride; MGC 3m slope 0.30 + stretch 4 + FLIP 0 %
(other filters / exits as in ats_inputs_study). Base now also checks the live default "HTF pierce late confirm: trade-color candle" (ON),
which the earlier replays did not. Replay Jan 5 -> now, net after costs (MES 0.50, MGC 0.22).
Modelled per the Pine / ESLib code: trigger on/off (HTF CBC Flip, LTF EMA20 Pierce, HTF EMA9 Pierce, HTF EMA20 Pierce); LTF late window;
HTF late window + trade-colour candle; "HTF EMA9/EMA20 Pierce replaces the current setup" (= HTF pierces skip the min-candles cooldown,
ats_cooldown_ok); "HTF pierce: also require close beyond LTF EMA9/20" (intended rule; see note); "HTF CBC Flip: require a pullback first"
(ESLib f_ats_flip_pb: within N bars of the flip a candle touches the chart EMA20 -- the BRSG zone is not in the bar feed -- then within N bars
a candle closes back beyond it in the trade colour; the flip setup is drawn there; two-step on/off).
NOT modelled: LTF EMA20 Touch (mid-candle), Momentum break, HTF Pullback - Structure Confirmed (live-only triggers).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd
exec(open('ats_inputs_study.py').read().split("CFG = {")[0].replace('"""①', '_d = """①', 1))
TDEF = dict(DEF, erl=.08, t_flip=True, t_ltf=True, t_h9=True, t_h20=True, llate=1, hlate=1, hcol=True, hrep=False, hreq=False, fpb=0, f2=True)
class TCase(PCase):
    def gen(s):
        P = s.P; C, H, L, O = s.C, s.H, s.L, s.O; out = []; n = s.n; hk = 5
        pc = np.r_[C[0], C[:-1]]; tr = np.maximum(H, pc) - np.minimum(L, pc); s.atr = cs.rma(tr, P['atrn'])
        e20, h9, h20, e9 = s.e20, s.h9, s.h20, s.B.e9.values.astype(float)
        flip_ok = np.zeros(n, bool); fev = np.zeros(n, int); fo = False
        TW = P.get('tw'); pend = 0
        for i in range(n):
            if s.hf[i] != 0:
                away = (C[i] > h20[i]) if s.hf[i] == 1 else (C[i] < h20[i]); fo = away; pend = 0
                if away: fev[i] = s.hf[i]
                elif TW is not None: pend = s.hf[i]
            elif pend:
                if (pend == 1 and C[i] > h20[i] + TW) or (pend == -1 and C[i] < h20[i] - TW): fo = True; fev[i] = pend; pend = 0
            flip_ok[i] = fo
        om = (s.hm - s.tf) % 1440
        orf = (((om >= 570) & (om < 600)) & P.get('orny', True)) | (((om >= 180) & (om < 210)) & P.get('orln', True)) | (((om >= 1200) & (om < 1230)) & P.get('oras', True))
        qa, qb = P.get('qwin', (960, 1125))
        qblk = np.zeros(n, bool) if qa is None else ((om >= qa) & (om < qb))
        vwb = np.zeros(n, int); st = 0; lastb = -99; bdir = 0
        for i in range(1, n):
            xd = C[i] < s.vw[i] and C[i - 1] >= s.vw[i - 1]; xu = C[i] > s.vw[i] and C[i - 1] <= s.vw[i - 1]
            if (xu and st == -1) or (xd and st == 1): lastb = i; bdir = st
            st = 0 if s.hf[i] != 0 else (-1 if (xd and s.hdir[i] == 0) else 1 if (xu and s.hdir[i] == 1) else 0 if (xu or xd) else st)
            vwb[i] = bdir if i - lastb <= P['vwbn'] else 0
        s.vwb = vwb; lastp = -99
        def pierce(line, i, lg):
            if lg: return L[i - 1] > line[i - 1] and L[i] <= line[i] <= H[i]
            return H[i - 1] < line[i - 1] and L[i] <= line[i] <= H[i]
        blocked = lambda i: np.isnan(s.atr[i]) or s.hdir[i] < 0 or qblk[i] or orf[i] or not flip_ok[i]
        arm = None
        for i in range(250, n - 1):
            # flip pullback wait (state machine runs every bar)
            if arm is not None:
                a = arm; age = i - a['f']
                if s.hdir[i] != (1 if a['lg'] else 0) or (a['t'] is None and age > P['fpb']) or (a['t'] is not None and i - a['t'] > P['fpb']): arm = None
                else:
                    if a['t'] is None and L[i] <= e20[i] <= H[i]: a['t'] = i
                    if a['t'] is not None and (P['f2'] or a['t'] == i):
                        if (C[i] > e20[i] and C[i] > O[i]) if a['lg'] else (C[i] < e20[i] and C[i] < O[i]):
                            if not blocked(i): out.append(dict(i=i, lg=a['lg'], trig='flip'))
                            arm = None
                    elif a['t'] is not None and not P['f2']: a['t'] = None
            if blocked(i): continue
            dirn = s.hdir[i] == 1
            if fev[i] != 0 and P['t_flip']:
                lg = fev[i] == 1; vw, e2 = s.vw[i], s.e200[i]; g = 1 if lg else -1
                side = (C[i] > max(vw, e2) + P['side']) if lg else (C[i] < min(vw, e2) - P['side'])
                vws = (s.vw[i] - s.vw[i - hk]) * g > 0
                fd = abs(C[i] - e20[i]) <= max(P['fdx'] * s.atr[i], P['fdp'])
                if side and vws and fd:
                    if P['fpb'] > 0: arm = dict(f=i, lg=lg, t=None)
                    else: out.append(dict(i=i, lg=lg, trig='flip'))
            for nm, line, mn, on in (('ltf20', e20, P['erl'], P['t_ltf']), ('h9', h9, P['erh'], P['t_h9']), ('h20', h20, P['erh'], P['t_h20'])):
                lg = dirn
                if not pierce(line, i, lg): continue
                if nm == 'ltf20':
                    if i - lastp <= 3: continue
                    lastp = i
                if not on: continue
                clr = (lambda k: not P['hreq'] or nm == 'ltf20' or ((C[k] > max(e9[k], e20[k])) if lg else (C[k] < min(e9[k], e20[k]))))
                if ((C[i] > line[i]) if lg else (C[i] < line[i])):
                    if clr(i): out.append(dict(i=i, lg=lg, trig=nm, erm=mn))
                    continue
                W = P['llate'] if nm == 'ltf20' else P['hlate']
                for k in range(1, W + 1):
                    j = i + k
                    if j >= n or s.hdir[j] != s.hdir[i]: break
                    col = nm == 'ltf20' or not P['hcol'] or ((C[j] > O[j]) if lg else (C[j] < O[j]))
                    if ((C[j] > line[j]) if lg else (C[j] < line[j])) and col:
                        if clr(j): out.append(dict(i=j, lg=lg, trig=nm, erm=mn, late=k))
                        break
        out.sort(key=lambda d: (d['i'], d['trig'] != 'flip'))
        for d in out:
            i = d['i']; lg = d['lg']; A = s.atr[i]; gg = 1 if lg else -1
            hi = s.H[i - 23:i + 1].max(); lo = s.L[i - 23:i + 1].min(); pos = (C[i] - lo) / (hi - lo) if hi > lo else .5
            d['R5'] = (pos if lg else 1 - pos) >= .8 and (hi - lo) / A < 5
            d['xv'] = gg * (C[i] - s.vw[i]) / A; d['X4'] = d['xv'] > 4; d['M'] = s.mtf[i] >= 0 and s.mtf[i] != (1 if lg else 0)
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={k: s.er[k][i] for k in s.er}, bo=bool(s.bo[i]), month=s.month[i])
        return out
    def run(s, ok, q, x4):
        P = s.P; res = []; last = -999; lastlg = None; op = None
        for d in s.cands:
            if x4 and d['X4']: continue
            if d['VB']: continue
            if d['trig'] != 'flip' and d['er'][12] < d['erm']: continue
            if not ok(d): continue
            i = d['i']; live = op is not None and i <= op['j']
            if res and res[-1]['i'] == i: continue
            if live and d['lg'] == op['lg']: continue
            if not (i - last >= P['cool'] or d['trig'] == 'flip' or (P['hrep'] and d['trig'] in ('h9', 'h20')) or (lastlg is not None and d['lg'] != lastlg)): continue
            if live:
                r, j, why = s.sim1(op['i'], op['lg'], q, i); op.update(res=r, j=j, why=why)
            r, j, why = s.sim1(i, d['lg'], q, -1); op = dict(d, res=r, why=why, j=j); res.append(op); last = i; lastlg = d['lg']
        return res
# ---- MNQ 3m study (CBC EMA Slope branch ideas applied to MNQ 3m) ----
class MCase3(TCase):
    def sim1(s, i, lg, q, stop_at):
        C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap']); part = q['part']
        sl = en - g * sd; t1 = en + g * tpd; hit = False; best = 0.
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q.get('be', True): sl = max(sl, en) if lg else min(sl, en)
            if q.get('ts', 0) and not hit and j - i == q['ts'] and best < q.get('tsx', .5) * A: return g * (C[j] - en), j, 'time'
            best = max(best, g * ((H[j] if lg else L[j]) - en))
            if hit and q.get('tr', 0) > 0:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.P['eod'] and s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

TF = 2   # LIVE 2m model: existing 2m list entries in v1.12 (MES 2m: MTF gate, flips>=4/8, skip ALL new setups from 9 HTF candles after flip, slow EMA 14; MGC 2m: range gate 5; NOT modelled: MGC 2m flip-flop skip, VWAP Bounce)
CH = {   # v1.12 / v10.97 defaults for the 2m charts: no 2m entries in any per-symbol/timeframe list -> global values + symbol-level lists
 'MES': dict(slow=14, cost=.5, fdp=8., tw=1.0, base={'F': {'mtg': 1, 'fl': 4, 'faall': 9}, 'slope': 0.75, 'P': {'tw': None}, 'q': {'cap': 1e9}}, q=dict(sl=1.7, mn=5, cap=8, tp=1.7, tcap=6, part=.8, be=True, tr=1.7)),
 'MGC': dict(cost=.22, fdp=10., tw=1.0, base={'rg': 5, 'slope': 0.42}, q=dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, part=.8, be=True, tr=1.7)),
 'MNQ': dict(cost=.87, fdp=50., tw=1.0, base={'slope': 0.55, 'q': {'part': 0.0, 'tr': 0}}, q=dict(sl=1.7, mn=25, cap=30, tp=1.7, tcap=40, part=.8, be=True, tr=1.7)),
 'M2K': dict(cost=.35, fdp=0., tw=1.0, base={'slope': 1.0, 'erl': 0.2}, q=dict(sl=1.7, mn=3, cap=8, tp=1.7, tcap=3, part=.8, be=True, tr=1.7))}
def setup(sym):
    global SYM, COST, LIVEQ, B, h20raw, CACHE, CFGX
    CFGX = CH[sym]; SYM = sym; COST = CFGX['cost']; LIVEQ = CFGX['q']; B = eng.load(sym, TF, '/tmp/%s%d.pkl' % (sym.lower(), TF)); B = B.copy(); B['e20'] = B.c.astype(float).ewm(span=CFGX.get('slow', 20), adjust=False).mean() if CFGX.get('slow', 20) != 20 else B['e20']; h20raw = B.h20.values.astype(float); CACHE = {}
def case(P):
    key = tuple(sorted((k, str(v)) for k, v in P.items() if k in ('tw', 'atrn', 'fdx', 'fdp', 'side', 'erl', 'erh', 'vwbn', 't_flip', 't_ltf', 't_h9', 't_h20', 'llate', 'hlate', 'hcol', 'qwin', 'orny', 'orln', 'oras')))
    if key not in CACHE:
        MCase3.P = P; CACHE[key] = MCase3(SYM, TF, B)
    c = CACHE[key]; c.P = P; return c
def run(o):
    o = {**CFGX['base'], **{k: ({**CFGX['base'].get(k, {}), **v} if isinstance(v, dict) else v) for k, v in o.items()}}
    P = dict(TDEF, fdp=CFGX['fdp'], tw=CFGX['tw'], erl=o.get('erl', .08)); P.update(o.get('P', {})); s = case(P)
    C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n; q = dict(LIVEQ, **o.get('q', {}))
    hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values; SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A
    rg = o.get('rg', 0); rz = o.get('rz', .2); x4 = o.get('x4', 0); slope = o.get('slope', 0); hb = o.get('hb', ())
    F = {k: v for k, v in o.get('F', {}).items() if v is not None}
    if 'fl' in F or 'fa' in F or 'faall' in F:
        flips = pd.Series((s.hf != 0).astype(float)).rolling(40).sum().values
        lastf = np.maximum.accumulate(np.where(s.hf != 0, np.arange(N), -1))
    def ok(d):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
        if not cs.cur_rule(d, thr=F.get('er', .23), flip_thr=o.get('fer', .23), bo=F.get('bo', True)): return False
        if F.get('bs') and d['bo'] and not (d['er'][12] >= F.get('er', .23)) and s.bo1[i] if hasattr(s, 'bo1') else False: return False
        w = hh24[i] - ll24[i]
        if rg and w > 0 and w / a < rg and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= 1 - rz: return False
        if x4 and g * (C[i] - s.vw[i]) / a > x4: return False
        if slope and SLP[i] < slope: return False
        if hb and ((s.hm[i] - TF) % 1440) // 60 in hb: return False
        if 'chop' in F and s.chop[i] > F['chop']: return False
        if 'adx' in F and s.adx[i] < F['adx']: return False
        if 'xs' in F and s.xs[i] >= F['xs']: return False
        if 'rng' in F and s.rng[i] < F['rng']: return False
        if 'fl' in F and flips[i] >= F['fl']: return False
        if F.get('mtg') and d['M']: return False
        if 'faall' in F and lastf[i] >= 0 and (i - lastf[i]) // 5 >= F['faall']: return False
        if 'fa' in F and lastf[i] >= 0 and d['trig'] != 'flip' and (i - lastf[i]) // 5 >= F['fa']: return False
        if 'nv' in F:
            dv = g * (C[i] - s.vw[i]); a_, b_ = F['nv']
            if -a_ <= dv <= b_: return False
        if 'ne' in F:
            de = g * (C[i] - s.e200[i]); a_, b_ = F['ne']
            if -a_ <= de <= b_: return False
        if F.get('env') and (s.e200[i] > s.vw[i]) != lg: return False
        if 'va' in F and s.atrrel[i] > F['va']: return False
        if 'vc' in F and q['cap'] < 1e8 and q['cap'] < F['vc'] * a: return False
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
    om_ = lambda r: (s.hm[r['i']] - TF) % 1440
    SES = (('Asia', lambda m: m >= 1080 or m < 180), ('London', lambda m: 180 <= m < 570), ('NY AM', lambda m: 570 <= m < 720), ('NY PM', lambda m: 720 <= m < 960))
    ses = {sn: (sum(1 for r in R if f(om_(r))), sum(r['res'] - COST for r in R if f(om_(r)))) for sn, f in SES}
    bt = {t: (sum(r['trig'] == t for r in R), sum(r['res'] - COST for r in R if r['trig'] == t)) for t in ('flip', 'ltf20', 'h9', 'h20')}
    v = np.array([r['res'] - COST for r in R]); eq = np.cumsum(v)
    th = [sum(r['res'] - COST for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
    return dict(n=len(v), net=v.sum(), avg=v.mean() if len(v) else 0, sd=v.std() or 1, th=th, l4=sum(r['res'] - COST for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max() if len(v) else 0, K={(T[r['i']], r['lg']): r['res'] - COST for r in R}, ses=ses, bt=bt)
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
