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
        for i in range(n):
            if s.hf[i] != 0:
                away = (C[i] > h20[i]) if s.hf[i] == 1 else (C[i] < h20[i]); fo = away
                if away: fev[i] = s.hf[i]
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
CFG = {'MES': dict(c=.5, slope=.42, erl=.15, x4=False, ride=True, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0)),
       'MGC': dict(c=.22, slope=.30, erl=.08, x4=True, ride=False, q=dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, part=0.0))}
VER={'MES':[('v10.97', dict(slope=0, ride=False, erl=.08), {}), ('v1.04 (slope 0.30 + flip ride)', dict(slope=.30, ride=True, erl=.08), {}),
            ('v1.05 (slope 0.42)', dict(slope=.42, ride=True, erl=.08), {}), ('v1.06 (+ LTF pierce min ER 0.15)', dict(slope=.42, ride=True, erl=.15), {}),
            ('v1.07 (+ no setups 13:00-15:00)', dict(slope=.42, ride=True, erl=.15), dict(hb=(13, 14)))],
     'MGC':[('v10.97', dict(slope=0, ride=False, erl=.08), {}), ('v1.04-v1.07 (slope 0.30)', dict(slope=.30, ride=False, erl=.08), {})]}
out=['Results vs v10.97 -- replay Jan 5 -> Nov 13, live 16:00-18:45 window on candle open time, HTF late-confirm colour check, net after costs (MES 0.50, MGC 0.22). z = change / (SD of v10.97 trades x sqrt(trades changed)). In-sample: every branch setting was chosen on this data.','']
for sym in ('MES','MGC'):
    B = eng.load(sym, 3, '/tmp/%s3.pkl' % sym.lower()); h20raw = B.h20.values.astype(float)
    def run(P):

        TCase.P = P; s = TCase(sym, 3, B); s.P = P; C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n
        hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values; SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A
        def ok(d):
            i, lg = d['i'], d['lg']
            if not cs.cur_rule(d): return False
            w = hh24[i] - ll24[i]
            if w > 0 and w / A[i] < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
            if SLP[i] < x['slope']: return False
            om_ = (s.hm[i] - 3) % 1440
            if P.get('hb') is not None and om_ // 60 in (P['hb'] if isinstance(P['hb'], tuple) else (P['hb'],)): return False
            for k_, (lo_, hi_, a_, b_) in (('inny', ('nyl', 'nyh', 600, 960)), ('inln', ('lnl', 'lnh', 210, 570)), ('inas', ('asl', 'ash', 1230, 1620))):
                if P.get(k_):
                    inwin = a_ <= om_ < b_ if b_ <= 1440 else (om_ >= a_ or om_ < b_ - 1440)
                    lv, hv = B[lo_].values[i], B[hi_].values[i]
                    if inwin and np.isfinite(lv) and np.isfinite(hv) and lv <= C[i] <= hv: return False
            return True
        R = [dict(r) for r in s.run(ok, x['q'], x['x4'])]
        if x['ride']:
            for k, r in enumerate(R):
                if r['trig'] != 'flip': continue
                i, lg = r['i'], r['lg']; stop = R[k + 1]['i'] if k + 1 < len(R) else -1; en = C[i]; g = 1 if lg else -1; sd = max(3 * A[i], 5); slv = en - g * sd; res = 0.
                for j in range(i + 1, N):
                    if (L[j] <= slv) if lg else (H[j] >= slv): res = -sd; break
                    if s.hdir[j] == (0 if lg else 1) or (P['eod'] and s.hm[j] == 960) or j == stop: res = g * (C[j] - en); break
                r['res'] = res
        T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
        v = np.array([r['res'] - x['c'] for r in R]); eq = np.cumsum(v)
        th = [sum(r['res'] - x['c'] for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        bt = {t: (sum(r['trig'] == t for r in R), sum(r['res'] - x['c'] for r in R if r['trig'] == t)) for t in ('flip', 'ltf20', 'h9', 'h20')}
        return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std(), th=th, l4=sum(r['res'] - x['c'] for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(T[r['i']], r['lg']): r['res'] - x['c'] for r in R}, bt=bt)

    res=[]
    for nm, o, ch in VER[sym]:
        x = dict(CFG[sym], **{k: o[k] for k in ('slope', 'ride')})
        P = dict(TDEF, erl=o['erl']); P.update(ch); res.append((nm, run(P)))
    b = res[0][1]
    out += ['### %s 3m' % sym, '', '| Change | Trades | vs v10.97 | z | Change by third | Last 4 wk | Max DD |', '|---|---|---|---|---|---|---|']
    for nm, a in res:
        if a is b:
            out.append('| %s | %d | net %+.0f | — | %+.0f / %+.0f / %+.0f (own) | %+.0f (own) | %.0f |' % (nm, a['n'], a['net'], *a['th'], a['l4'], a['dd'])); continue
        chg = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(chg))
        out.append('| %s | %d | %+.0f (net %+.0f) | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f |' % (nm, a['n'], a['net'] - b['net'], a['net'], z, *[p - q for p, q in zip(a['th'], b['th'])], a['l4'] - b['l4'], a['dd']))
    out.append('')
open('vcmp2_report.md','w').write('\n'.join(out)); print('\n'.join(out))
