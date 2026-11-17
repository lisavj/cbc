"""① Auto Trade Setup inputs not studied before -- MES 3m and MGC 3m on the CBC EMA Slope branch (v1.05) -- 11/14/2026.
One change at a time on top of each chart's branch settings. Replay Jan 5 -> now (BarFeed / Databento bars, TV EMA20), net after costs
(MES 0.50, MGC 0.22). Entry filters are entry filters: a skipped setup can change later setups (cooldown, one-per-direction).
MES 3m base: ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, HTF EMA20 slope >= 0.42 ATR; SL1 3 ATR min 5, TP1 1.75, 100 % at TP1;
  HTF CBC Flip setups ride to the HTF flip back / SL1 / 16:00 / next setup.
MGC 3m base: same filters with slope >= 0.30 + VWAP stretch 4 ATR; SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, 0 % at TP1 + BE, closed by the HTF flip.
Both: flip gates as live (close <= max(2 ATR, 8 pts) from the 3m EMA20 -- the replay engine has always used 8 pts for MGC too, live is 10;
  close beyond VWAP and EMA200 by 1 pt; VWAP slope agrees; flip ER >= 0.23); per-trigger ER mins LTF 0.08 / HTF 0.15; VWAP reclaim block 5 bars;
  min 10 candles between setups; skip a new setup while the same-direction one runs; ATR 14; setups end at 16:00.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, better in all three thirds, last 4 wk >= 0; promising = z >= 1 and all thirds.
Not modelled: pivot reclaim block (R2/R3/S2/S3 not in the bar feed), TP/SL steps (pivot levels; ATR method is live), closed-15m-values mode,
act-on-flip-at-HTF-close, toward flips (studied 11/03), OR blocks (orb_all), min SL / SL / TP / trail / caps / time stop (other studies)."""
import sys, numpy as np, pandas as pd, datetime as D
from zoneinfo import ZoneInfo
import chop_sim as cs, ema716_eng as eng
TZ = ZoneInfo('America/New_York')
DEF = dict(fdx=2.0, fdp=8.0, side=1.0, vws=True, e2s=False, fer=.23, erl=.08, erh=.15, vwbn=5, cool=10, same=True, clr=0, mtf=False,
           atrn=14, eod=True, hsl=False, flop=0)
class PCase(eng.MCase):
    P = DEF
    def gen(s):
        P = s.P; C, H, L = s.C, s.H, s.L; out = []; n = s.n; hk = 5
        pc = np.r_[C[0], C[:-1]]; tr = np.maximum(H, pc) - np.minimum(L, pc); s.atr = cs.rma(tr, P['atrn'])
        e20, h9, h20 = s.e20, s.h9, s.h20
        flip_ok = np.zeros(n, bool); fev = np.zeros(n, int); fo = False
        for i in range(n):
            if s.hf[i] != 0:
                away = (C[i] > h20[i]) if s.hf[i] == 1 else (C[i] < h20[i]); fo = away
                if away: fev[i] = s.hf[i]
            flip_ok[i] = fo
        om = (s.hm - s.tf) % 1440
        orf = ((om >= 570) & (om < 600)) | ((om >= 180) & (om < 210)) | ((om >= 1200) & (om < 1230))
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
        for i in range(250, n - 1):
            if np.isnan(s.atr[i]) or s.hdir[i] < 0: continue
            hm = s.hm[i]
            if 16 * 60 <= hm < 18 * 60 + 30 or orf[i]: continue
            dirn = s.hdir[i] == 1
            if not flip_ok[i]: continue
            if fev[i] != 0:
                lg = fev[i] == 1; vw, e2 = s.vw[i], s.e200[i]; g = 1 if lg else -1
                side = P['side'] is None or ((C[i] > max(vw, e2) + P['side']) if lg else (C[i] < min(vw, e2) - P['side']))
                vws = not P['vws'] or (s.vw[i] - s.vw[i - hk]) * g > 0
                e2s = not P['e2s'] or (s.e200[i] - s.e200[i - hk]) * g > 0
                fd = P['fdx'] is None or abs(C[i] - e20[i]) <= max(P['fdx'] * s.atr[i], P['fdp'])
                if side and vws and e2s and fd: out.append(dict(i=i, lg=lg, trig='flip'))
            for nm, line, mn in (('ltf20', e20, P['erl']), ('h9', h9, P['erh']), ('h20', h20, P['erh'])):
                lg = dirn
                if nm == 'ltf20' and pierce(line, i, lg):
                    if i - lastp <= 3: continue
                    lastp = i
                if pierce(line, i, lg):
                    if (C[i] > line[i]) if lg else (C[i] < line[i]): out.append(dict(i=i, lg=lg, trig=nm, erm=mn))
                    elif i + 1 < n and s.hdir[i + 1] == s.hdir[i] and ((C[i + 1] > line[i + 1]) if lg else (C[i + 1] < line[i + 1])): out.append(dict(i=i + 1, lg=lg, trig=nm, erm=mn, late=1))
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
            if P['mtf'] and d['M']: continue
            if d['VB']: continue
            if d['trig'] != 'flip' and d['er'][12] < d['erm']: continue
            if not ok(d): continue
            i = d['i']; live = op is not None and i <= op['j']
            if res and res[-1]['i'] == i: continue
            if P['same'] and live and d['lg'] == op['lg']: continue
            if not (i - last >= P['cool'] or d['trig'] == 'flip' or (lastlg is not None and d['lg'] != lastlg)): continue
            if live:
                r, j, why = s.sim1(op['i'], op['lg'], q, i); op.update(res=r, j=j, why=why)
            r, j, why = s.sim1(i, d['lg'], q, -1); op = dict(d, res=r, why=why, j=j); res.append(op); last = i; lastlg = d['lg']
        return res
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
                sl = max(sl, en) if lg else min(sl, en)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.P['eod'] and s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

CFG = {'MES': dict(c=.5, slope=.42, x4=False, ride=True, q=dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0)),
       'MGC': dict(c=.22, slope=.30, x4=True, ride=False, q=dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, part=0.0))}
V = [('Flip distance 1.5 ATR', dict(fdx=1.5)), ('Flip distance 2.5 ATR', dict(fdx=2.5)), ('Flip distance 3 ATR', dict(fdx=3.0)), ('Flip distance Off', dict(fdx=None)),
     ('Flip distance floor 10 pts (MGC live value)', dict(fdp=10.0)),
     ('Flip side gate 0 pts', dict(side=0.0)), ('Flip side gate 2 pts', dict(side=2.0)), ('Flip side gate Off', dict(side=None)),
     ('Flip VWAP slope must agree Off', dict(vws=False)), ('Flip EMA200 slope must agree On', dict(e2s=True)),
     ('Flip min ER 0 (off)', dict(fer=0.0)), ('Flip min ER 0.15', dict(fer=.15)), ('Flip min ER 0.30', dict(fer=.30)),
     ('Skip the flip setup when the flip is a flop', dict(flop=1)), ('Also skip non-flip setups while the flip is a flop', dict(flop=2)),
     ('Min ER LTF EMA20 Pierce 0', dict(erl=0.0)), ('Min ER LTF EMA20 Pierce 0.15', dict(erl=.15)), ('Min ER HTF EMA9/20 0', dict(erh=0.0)), ('Min ER HTF EMA9/20 0.23', dict(erh=.23)),
     ('Skip setups against the MTF (60m) CBC', dict(mtf=True)), ('HTF EMA20 slope against the trade = skip (min 0)', dict(hsl=True)),
     ('VWAP reclaim block Off', dict(vwbn=-1)), ('VWAP reclaim block 3 bars', dict(vwbn=3)), ('VWAP reclaim block 8 bars', dict(vwbn=8)),
     ('Require price past both EMA clouds (chart 9/20)', dict(clr=1)), ('... + close beyond HTF EMA9', dict(clr=2)), ('... + close beyond HTF EMA20', dict(clr=3)),
     ('Skip same-direction setup while running Off', dict(same=False)),
     ('Min candles between setups 5', dict(cool=5)), ('Min candles between setups 8', dict(cool=8)), ('Min candles between setups 12', dict(cool=12)),
     ('Min candles between setups 15', dict(cool=15)), ('Min candles between setups 20', dict(cool=20)),
     ('ATR length 10', dict(atrn=10)), ('ATR length 15 (your chart)', dict(atrn=15)), ('ATR length 20', dict(atrn=20)),
     ('End setups at 16:00 Off', dict(eod=False))]
if 'nb' in sys.argv:
    V = [('Min ER LTF EMA20 Pierce %.2f' % e, dict(erl=e)) for e in (.10, .12, .14, .15, .16, .18, .20, .23)] + [
         ('End 16:00 Off + Min ER LTF 0.15', dict(eod=False, erl=.15)), ('ATR 15 + Min ER LTF 0.15', dict(atrn=15, erl=.15)), ('ATR 15 + End 16:00 Off', dict(atrn=15, eod=False))]
out = [__doc__, '']; top = ['## Candidates (promising or better)', '']
for sym in (('MES', 'MGC') if 'nb' not in sys.argv else ('MES', 'MGC')):
    x = CFG[sym]; B = eng.load(sym, 3, '/tmp/%s3.pkl' % sym.lower()); h20raw = B.h20.values.astype(float); e9 = B.e9.values.astype(float)
    cache = {}
    def case(P):
        key = tuple(sorted((k, P[k]) for k in ('fdx', 'fdp', 'side', 'vws', 'e2s', 'erl', 'erh', 'vwbn', 'atrn')))
        if key not in cache:
            PCase.P = P; cache[key] = PCase(sym, 3, B)
        s = cache[key]; s.P = P; return s
    def run(P):
        s = case(P); C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n
        hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values; SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A
        hs = s.h20 - np.r_[np.full(5, np.nan), s.h20[:-5]]
        lastflip = np.maximum.accumulate(np.where(s.hf != 0, np.arange(N), -1))
        grp = B.hk.values; ghi = pd.Series(H).groupby(grp, sort=False).transform('max').values; glo = pd.Series(L).groupby(grp, sort=False).transform('min').values
        def flop(i, lg):
            k = lastflip[i]
            if k < 0: return False
            hi, lo = ghi[k], glo[k]; rg = hi - lo
            if rg <= 0: return False
            return any(lo < lv < hi and ((hi - lv) / rg if lg else (lv - lo) / rg) < .7 for lv in (s.e200[k], s.vw[k]))
        def ok(d):
            i, lg = d['i'], d['lg']; g = 1 if lg else -1
            if not cs.cur_rule(d, flip_thr=P['fer']): return False
            w = hh24[i] - ll24[i]
            if w > 0 and w / A[i] < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
            if SLP[i] < x['slope']: return False
            if P['hsl'] and not (g * hs[i] >= 0): return False
            if P['clr']:
                if not ((C[i] > max(e9[i], s.e20[i])) if lg else (C[i] < min(e9[i], s.e20[i]))): return False
                if P['clr'] >= 2 and not (g * (C[i] - s.h9[i]) > 0): return False
                if P['clr'] >= 3 and not (g * (C[i] - s.h20[i]) > 0): return False
            if P['flop'] and flop(i, lg) and (d['trig'] == 'flip' or P['flop'] == 2): return False
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
        return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std(), th=th, l4=sum(r['res'] - x['c'] for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                    dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(T[r['i']], r['lg']): r['res'] - x['c'] for r in R})
    L0 = run(dict(DEF)); rows = []
    print(sym, 'base', L0['n'], round(L0['net']), file=sys.stderr, flush=True)
    for nm, ch in V:
        P = dict(DEF); P.update(ch)
        if sym == 'MES' and nm.startswith('Flip distance floor'): continue
        a = run(P); chg = sum(1 for k in set(a['K']) | set(L0['K']) if abs(a['K'].get(k, 1e9) - L0['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - L0['net']) / (L0['sd'] * np.sqrt(chg)); d_ = [p - q for p, q in zip(a['th'], L0['th'])]; l4 = a['l4'] - L0['l4']
        vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'robust except last 4 wk' if z >= 2 and all(t > 0 for t in d_) else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < L0['net'] else 'noise'
        rows.append('| %s | %d | %.0f %% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %s |' % (nm, a['n'], a['w'], a['net'], a['avg'], a['net'] - L0['net'], z, *d_, l4, a['dd'], vd))
        if vd in ('robust', 'robust except last 4 wk', 'promising'):
            top.append('- %s 3m: %s → %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f vs %.0f (%s)' % (sym, nm, a['net'] - L0['net'], z, *d_, l4, a['dd'], L0['dd'], vd))
        print(sym, nm, round(a['net'] - L0['net']), file=sys.stderr, flush=True)
    out += ['## %s 3m -- branch base: %d setups, win %.0f %%, net %+.0f, avg %+.2f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f' % (sym, L0['n'], L0['w'], L0['net'], L0['avg'], *L0['th'], L0['l4'], L0['dd']), '',
            '| Change (one at a time) | Setups | Win % | Net | Avg | Δ vs base | z | Δ by third | Δ last 4 wk | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|---|---|'] + rows + ['']
if len(top) == 2: top.append('- none')
rep = '\n'.join(out[:2] + top + [''] + out[2:]); open('ats_inputs_report%s.md' % ('_nb' if 'nb' in sys.argv else ''), 'w').write(rep); print(rep)
