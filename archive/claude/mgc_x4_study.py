"""MGC 3m after the replay-engine stretch-gate fix (11/14/2026): (1) check, (2) tp1flip exits rerun, (3) chart EMA 7 / 16 on the branch.
Engine fix: mes3_ema_grid MCase.gen set X4 = False for every main setup, so gates=dict(X4=1) only blocked late LTF setups; now
X4 = close more than 4 ATR beyond VWAP on the trade side (same as late_study / chop_sim / tsf_study's own check).
MGC 3m live settings: ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, VWAP stretch 4 ATR; exits SL1 1.7 ATR min 5 cap 7,
TP1 1.7 ATR cap 6. Branch adds HTF EMA20 slope >= 0.3 ATR (MGC 3m; flip ride is MES 3m only). Replay Jan 5 -> now, net after 0.22 cost.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all three thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd, datetime as D
from zoneinfo import ZoneInfo
import chop_sim as cs, ema716_eng as eng
COST = .22; TZ = ZoneInfo('America/New_York')
B0 = eng.load('MGC', 3, '/tmp/mgc3.pkl'); C0 = B0.c.values.astype(float)
def build(slow):
    B = B0.copy()
    if slow: B['e20'] = eng.ema(C0, slow)
    eng.LCase.LATE = 1; eng.LCase.NYW = 30
    return eng.LCase('MGC', 3, B)
CASES = {sl: build(sl) for sl in (0, 20, 16, 14)}
s0 = CASES[0]; T = s0.T; N = s0.n; H, L, C, A = s0.H, s0.L, s0.C, s0.atr
T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values
SLP = np.abs(B0.h20.values.astype(float) - np.roll(B0.h20.values.astype(float), 12)) / A
X = dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6)
def rg(d):
    i, lg = d['i'], d['lg']; w = hh24[i] - ll24[i]
    return w > 0 and w / A[i] < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8
def ok(d, slope=0., own_x4=False):
    i = d['i']; g = 1 if d['lg'] else -1
    if not cs.cur_rule(d) or rg(d): return False
    if own_x4 and g * (C[i] - s0.vw[i]) / A[i] > 4: return False
    if slope and SLP[i] < slope: return False
    return True
def setups(sl, slope=0., x4gate=1, own_x4=False):
    s = CASES[sl]
    R = s.run(lambda d: ok(d, slope, own_x4), q=dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9), gates=dict(R5=0, X4=x4gate, MTF=0))
    return s, [(r['i'], r['lg'], R[k + 1]['i'] if k + 1 < len(R) else -1, r['trig']) for k, r in enumerate(R)]
def sim(s, i, lg, stop, p, mode):
    en = C[i]; a = A[i]; g = 1 if lg else -1; x = X
    sd = max(min(x['sl'] * a, x['cap']), x['mn']); tpd = min(x['tp'] * a, x['tcap'])
    sl = en - g * sd; t1 = en + g * tpd; hit = False; usetp = mode != 'FLIP+SL'
    for j in range(i + 1, N):
        if (L[j] <= sl) if lg else (H[j] >= sl):
            rem = g * (sl - en); return p * tpd + (1 - p) * rem if hit else rem
        if usetp and not hit and ((H[j] >= t1) if lg else (L[j] <= t1)):
            hit = True
            if p >= 1: return tpd
            if mode in ('TRAIL', 'FLIP'): sl = max(sl, en) if lg else min(sl, en)
        if hit and mode == 'TRAIL':
            ns = C[j] - g * 3.5 * A[j]; sl = max(sl, ns) if lg else min(sl, ns)
        if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop:
            rem = g * (C[j] - en); return p * tpd + (1 - p) * rem if hit else rem
    return 0.
def go(s, ST, p=0.0, mode='FLIP'):
    v = []; th = [0, 0, 0]; l4 = 0; K = {}; bt = {}
    for (i, lg, stop, tg) in ST:
        r = sim(s, i, lg, stop, p, mode) - COST; v.append(r); K[(i, lg)] = r; th[0 if T[i] < cuts[0] else 1 if T[i] < cuts[1] else 2] += r
        if T[i] >= t4: l4 += r
        n_, t_ = bt.get(tg, (0, 0.)); bt[tg] = (n_ + 1, t_ + r)
    v = np.array(v); eq = np.cumsum(v)
    return dict(n=len(v), net=v.sum(), sd=v.std(), th=th, l4=l4, w=100 * (v > 0).mean(), dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K=K, avg=v.mean(), bt=bt)
def cmp(a, b):
    chg = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
    z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(chg)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
    vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
    return z, d_, l4, vd
fmt = lambda t: D.datetime.fromtimestamp(t / 1000, TZ).strftime('%m/%d')
out = [__doc__, '', 'Data: %d candles, %s → %s. Thirds %s–%s / %s–%s / %s–%s. Last 4 weeks from %s.' % (
    N, fmt(T[0]), fmt(T1), fmt(T0), fmt(cuts[0]), fmt(cuts[0]), fmt(cuts[1]), fmt(cuts[1]), fmt(T1), fmt(t4)), '']
# (1) check
a_fix = go(*setups(0)); a_own = go(*setups(0, x4gate=0, own_x4=True)); a_old = go(*setups(0, x4gate=0))
out += ['## 1. Check (TV EMA20, v10.97 MGC 3m settings, FLIP 0 % exits)', '',
        '- Fixed engine, gates X4=1: %d setups, net %+.0f.' % (a_fix['n'], a_fix['net']),
        '- Stretch check inside the study (tsf_study way): %d setups, net %+.0f (tsf_report "current": 1136 setups).' % (a_own['n'], a_own['net']),
        '- Old engine behaviour (main setups never stretch-blocked): %d setups, net %+.0f (tp1flip / cbce / volflip ran like this).' % (a_old['n'], a_old['net']), '']
print('check', a_fix['n'], a_own['n'], a_old['n'], file=sys.stderr, flush=True)
# (2) tp1flip rerun, with and without the gate
for title, kw in (('2a. tp1flip exits, gate applied (fixed) -- v10.97 settings', dict()), ('2b. Same, branch settings (+ slope 0.3)', dict(slope=.3)),
                  ('2c. For reference: old engine (no gate on main setups) -- what the 11/13 tp1flip used', dict(x4gate=0))):
    s, ST = setups(0, **kw); L0 = go(s, ST, 0.0, 'FLIP')
    out += ['## ' + title + ' -- %d setups; live = FLIP 0 %% at TP1' % L0['n'], '', '| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |', '|---|---|---|---|---|---|---|---|---|']
    rows = [(m, p, go(s, ST, p, m)) for m in ('TRAIL', 'FLIP', 'FLIP-noBE') for p in (0, .25, .5, .75, 1.0) if not (p == 1.0 and m != 'TRAIL')]
    rows.append(('FLIP+SL', None, go(s, ST, 0, 'FLIP+SL')))
    for m, p, a in rows:
        z, d_, l4, vd = cmp(a, L0); live = m == 'FLIP' and p == 0
        out.append('| %s | %s | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f %% | %.0f |' % ('**FLIP (live)**' if live else m, '-' if p is None else '%d %%' % (p * 100), a['net'], a['net'] - L0['net'], z, *a['th'], a['l4'], a['w'], a['dd']))
    b = max(rows, key=lambda r: r[2]['net']); okr = [r for r in rows if all(t > tt for t, tt in zip(r[2]['th'], L0['th']))]
    out += ['', 'Largest: %s %s = %+.0f. Better than live in all three thirds: %s' % (b[0], '-' if b[1] is None else '%d %%' % (b[1] * 100), b[2]['net'],
            ', '.join('%s %s (%+.0f)' % (m, '-' if p is None else '%d %%' % (p * 100), a['net']) for m, p, a in okr) or 'none'), '']
    print(title, file=sys.stderr, flush=True)
# (3) chart EMA 7 / 16 on the branch (gate fixed, slope 0.3, FLIP 0 %)
TN = {'flip': 'Flip', 'ltf20': 'LTF20', 'h9': 'HTF9', 'h20': 'HTF20'}
for title, kw in (('3a. Chart EMA, branch settings (stretch 4 + slope 0.3, FLIP 0 %)', dict(slope=.3)), ('3b. Chart EMA, v10.97 settings (no slope filter)', dict())):
    S = {sl: go(*setups(sl, **kw)) for sl in (20, 16, 14, 0)}; b = S[20]
    out += ['## ' + title, '', '| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9/20 | z | Δ by third | Δ last 4 wk | Max DD | Verdict | By trigger (n / net) |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for sl, nm in ((0, '9 / 20, TV EMA20 (project baseline)'), (20, '9 / 20 recomputed (comparison base)'), (16, '7 / 16'), (14, '7 / 14')):
        a = S[sl]; z, d_, l4, vd = (0, [0, 0, 0], a['l4'], 'baseline') if sl == 20 else cmp(a, b)
        out.append('| %s | %d | %.0f %% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %s | %s |' % (
            nm, a['n'], a['w'], a['net'], a['avg'], a['net'] - b['net'], z, *d_, l4, a['dd'], vd, ' · '.join('%s %d / %+.0f' % (TN[t], *a['bt'].get(t, (0, 0))) for t in TN)))
    out += ['', '(Recomputed 9 / 20 row: "Δ last 4 wk" = its own last-4-week net.)', '']
    print(title, file=sys.stderr, flush=True)
open('mgc_x4_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
