"""HTF-flip close ON (current) vs OFF -- CBC EMA Slope current 3m settings (v1.19 logic = v1.22 / v1.23) -- MES / MGC / MNQ / M2K 3m -- 11/16/2026.
Engine = project claude/all_eng.py (TCase gen + MCase3 exits) with the claude/blk_watch.py v1.19 3m bases:
 MES 3m slope 0.42 / 12 bars, LTF ER 0.15, range gate 5, hour block 13-15, no new setups 16:00-19:00, End 16:00 OFF, flip setups ride
        (no TP, closed by the HTF flip back / SL1 / next setup); SL1 3 ATR min 5, TP1 1.75, 100 % at TP1.
 MGC 3m slope 0.165 / 5 bars, range gate 5, stretch 4, late-away 1 pt; SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, 0 % at TP1 + BE (FLIP 0 %).
 MNQ 3m slope 0.75, LTF ER 0.15, NY OR forming block OFF; SL1 1.7 ATR min 25 cap 60, TP1 1.7 cap 40, 0 % at TP1 + BE.
 M2K 3m slope 0.48, LTF ER 0.23, stretch 4; SL1 3.5 ATR min 3 cap 8, TP1 1.7 cap 3, 0 % at TP1 + BE, trail 1.7 (after TP1).
Variants (exits only; entries unchanged except that a longer-running trade can block a later same-direction setup):
 A = no close on the HTF CBC flip against, for every trade (flip-ride trades then end only at SL1 / 16:00 if on / next opposite setup)
 B = no close on the HTF flip for normal trades; MES flip-ride trades keep their flip-back exit
 C = (0 % at TP1 charts) close on the HTF flip only before TP1; after TP1 (stop at BE) the runner ignores the flip
Net after costs (MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35). z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, all thirds better,
last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd, datetime as D
import chop_sim as cs, ema716_eng as eng
DEF = dict(fdx=2.0, fdp=8.0, side=1.0, vws=True, e2s=False, fer=.23, erl=.08, erh=.15, vwbn=5, cool=10, same=True, clr=0, mtf=False,
           atrn=14, eod=True, hsl=False, flop=0)   # = claude/ats_inputs_study.py DEF (not imported: that file runs its study on import)
class PCase(eng.MCase):
    P = DEF
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
        for i in range(250, n - 1):
            if blocked(i): continue
            dirn = s.hdir[i] == 1
            if fev[i] != 0 and P['t_flip']:
                lg = fev[i] == 1; vw, e2 = s.vw[i], s.e200[i]; g = 1 if lg else -1
                side = (C[i] > max(vw, e2) + P['side']) if lg else (C[i] < min(vw, e2) - P['side'])
                vws = (s.vw[i] - s.vw[i - hk]) * g > 0
                fd = abs(C[i] - e20[i]) <= max(P['fdx'] * s.atr[i], P['fdp'])
                if side and vws and fd: out.append(dict(i=i, lg=lg, trig='flip'))
            for nm, line, mn, on in (('ltf20', e20, P['erl'], P['t_ltf']), ('h9', h9, P['erh'], P['t_h9']), ('h20', h20, P['erh'], P['t_h20'])):
                lg = dirn
                if not pierce(line, i, lg): continue
                if nm == 'ltf20':
                    if i - lastp <= 3: continue
                    lastp = i
                if not on: continue
                if ((C[i] > line[i]) if lg else (C[i] < line[i])):
                    out.append(dict(i=i, lg=lg, trig=nm, erm=mn)); continue
                W = P['llate'] if nm == 'ltf20' else P['hlate']
                for k in range(1, W + 1):
                    j = i + k
                    if j >= n or s.hdir[j] != s.hdir[i]: break
                    col = nm == 'ltf20' or not P['hcol'] or ((C[j] > O[j]) if lg else (C[j] < O[j]))
                    if ((C[j] > line[j]) if lg else (C[j] < line[j])) and col:
                        out.append(dict(i=j, lg=lg, trig=nm, erm=mn, late=k)); break
        out.sort(key=lambda d: (d['i'], d['trig'] != 'flip'))
        for d in out:
            i = d['i']; lg = d['lg']; A = s.atr[i]; gg = 1 if lg else -1
            d['xv'] = gg * (C[i] - s.vw[i]) / A; d['X4'] = d['xv'] > 4
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={k: s.er[k][i] for k in s.er}, bo=bool(s.bo[i]), month=s.month[i])
        return out
    def run(s, ok, q, x4):
        P = s.P; res = []; last = -999; lastlg = None; op = None
        for d in s.cands:
            if d['VB']: continue
            if d['trig'] != 'flip' and d['er'][12] < d['erm']: continue
            if not ok(d): continue
            i = d['i']; live = op is not None and i <= op['j']
            if res and res[-1]['i'] == i: continue
            if live and d['lg'] == op['lg']: continue
            if not (i - last >= P['cool'] or d['trig'] == 'flip' or (lastlg is not None and d['lg'] != lastlg)): continue
            if live:
                r, j, why = s.sim1(op['i'], op['lg'], q, i, op['trig']); op.update(res=r, j=j, why=why)
            r, j, why = s.sim1(i, d['lg'], q, -1, d['trig']); op = dict(d, res=r, why=why, j=j); res.append(op); last = i; lastlg = d['lg']
        return res
    def sim1(s, i, lg, q, stop_at, trig=''):
        C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap']); part = q['part']
        ride = q.get('ride') and trig == 'flip'; nf = q.get('nf', 0)
        if ride: part = 0.0; tpd_on = False
        else: tpd_on = True
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if tpd_on and not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q.get('be', True): sl = max(sl, en) if lg else min(sl, en)
            if hit and q.get('tr', 0) > 0:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            flipx = s.hdir[j] == (0 if lg else 1)
            if flipx:
                if nf == 1: flipx = False                      # A: never
                elif nf == 2: flipx = ride                       # B: only flip-ride trades
                elif nf == 3: flipx = not hit                    # C: only before TP1
            why = 'flip' if flipx else ('16:00' if (s.P['eod'] and s.hm[j] == 960) else ('new' if j == stop_at else None))
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'
CH = {'MES': dict(cost=.5, f='/tmp/mes3.pkl', fdp=8., tw=None, base=dict(slope=.42, erl=.15, rg=5, hb=(13, 14), P=dict(qwin=(960, 1140), eod=False)), q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, tr=0, ride=True)),
      'MGC': dict(cost=.22, f='/tmp/mgc3.pkl', fdp=8., tw=1.0, base=dict(slope=.165, slk=5, rg=5, x4=4), q=dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, part=0.0, be=True, tr=0)),
      'MNQ': dict(cost=.87, f='/tmp/mnq3.pkl', fdp=50., tw=None, base=dict(slope=.75, erl=.15, P=dict(orny=False)), q=dict(sl=1.7, mn=25, cap=60, tp=1.7, tcap=40, part=0.0, be=True, tr=0)),
      'M2K': dict(cost=.35, f='/tmp/m2k3.pkl', fdp=0., tw=None, base=dict(slope=.48, erl=.23, x4=4), q=dict(sl=3.5, mn=3, cap=8, tp=1.7, tcap=3, part=0.0, be=True, tr=1.7))}
def runsym(sym):
    X = CH[sym]; B = eng.load(sym, 3, X['f']); h20raw = B.h20.values.astype(float); o = X['base']
    P = dict(TDEF, fdp=X['fdp'], tw=X['tw'], erl=o.get('erl', .08)); P.update(o.get('P', {}))
    TCase.P = P; s = TCase(sym, 3, B); s.P = P
    C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n
    hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values
    SLP = np.abs(h20raw - np.roll(h20raw, o.get('slk', 12))) / A
    rg, x4, slope, hb = o.get('rg', 0), o.get('x4', 0), o.get('slope', 0), o.get('hb', ())
    def ok(d):
        i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
        if not cs.cur_rule(d): return False
        w = hh24[i] - ll24[i]
        if rg and w > 0 and w / a < rg and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
        if x4 and g * (C[i] - s.vw[i]) / a > x4: return False
        if slope and SLP[i] < slope: return False
        if hb and ((s.hm[i] - 3) % 1440) // 60 in hb: return False
        return True
    T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def sc(nf):
        R = s.run(ok, dict(X['q'], nf=nf), False); v = np.array([r['res'] - X['cost'] for r in R]); eq = np.cumsum(v)
        th = [sum(r['res'] - X['cost'] for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        ex = {}
        for r in R: ex[r['why']] = ex.get(r['why'], 0) + 1
        hold = np.median([(r['j'] - r['i']) * 3 for r in R])
        return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std() or 1, th=th, l4=sum(r['res'] - X['cost'] for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), worst=v.min(), K={(r['i'], r['lg']): r['res'] - X['cost'] for r in R}, ex=ex, hold=hold)
    b = sc(0); rows = []
    vars_ = [('Current: close on HTF flip', 0), ('A. No close on HTF flip (all trades)', 1)] + ([('B. No flip close; flip-ride trades keep it', 2)] if sym == 'MES' else []) + \
            ([('C. Flip close only before TP1 (runner ignores flip)', 3)] if X['q']['part'] < 1 else [])
    for nm, nf in vars_:
        a = b if nf == 0 else sc(nf)
        ch = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
        vd = '' if nf == 0 else 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
        exs = ', '.join('%s %d' % (k, v) for k, v in sorted(a['ex'].items(), key=lambda x: -x[1]))
        rows.append('| %s | %d | %+.0f | %+.2f | %.0f %% | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %.1f | %.0f min | %s | %s |' % (nm, a['n'], a['net'], a['avg'], a['w'], a['net'] - b['net'], z, *d_, l4, a['dd'], a['worst'], a['hold'], exs, vd))
    return ['## %s 3m (bars to %s)' % (sym, D.datetime.utcfromtimestamp(T[-1] / 1000).strftime('%m/%d')), '', 'Current: thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f' % (*b['th'], b['l4']), '',
            '| Exit | Trades | Net | Avg | Win % | vs current | z | Change by third | Last 4 wk | Max DD | Worst | Median hold | Exits | Verdict |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|'] + rows + ['']
if __name__ == '__main__':
  out = [__doc__, '']
  for sym in (sys.argv[1:] or ['MES', 'MGC', 'MNQ', 'M2K']):
    out += runsym(sym); print('done', sym, file=sys.stderr, flush=True)
  open('noflip_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
