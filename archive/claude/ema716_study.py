"""MES 3m chart EMA 7 / 16 vs 9 / 20 on the CBC EMA Slope branch (CBC-ES v1.04) -- 11/14/2026.
Branch baseline = mes_next_study baseline (ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR, HTF EMA20 slope >= 0.3 ATR
|15m EMA20 now - 12 bars ago| / ATR) + exits SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1, and HTF CBC Flip setups ride
to the HTF flip back / SL1 / 16:00 / next setup (no TP, branch item 2). Replay Jan 5 -> now, net after 0.50 cost.
Only the SLOW chart EMA changes the replay (LTF EMA20 Pierce line, flip distance); the fast EMA (7 vs 9) only feeds the
cloud / "closed beyond EMA9" text, which is not modelled. Slow EMA is recomputed from closes for every variant (20 too).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all three thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd, datetime as D
from zoneinfo import ZoneInfo
import chop_sim as cs, ema716_eng as eng  # ema716_eng.py + chop_sim.py from the project next to it
COST = .5
Q = dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7)
B0 = eng.load('MES', 3, '/tmp/mes3.pkl'); C0 = B0.c.values.astype(float)
TZ = ZoneInfo('America/New_York')
def build(slow):
    B = B0.copy()
    if slow: B['e20'] = eng.ema(C0, slow)
    eng.LCase.LATE = 1; eng.LCase.NYW = 30
    return eng.LCase('MES', 3, B)
CASES = {sl: build(sl) for sl in (20, 16, 14, 0)}
s0 = CASES[20]; T = s0.T; N = s0.n
T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
H, L, C, A = s0.H, s0.L, s0.C, s0.atr
hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values
h20 = B0.h20.values.astype(float); SLP = np.abs(h20 - np.roll(h20, 12)) / A
et = pd.to_datetime(T, unit='ms', utc=True).tz_convert(TZ); mins = et.hour.values * 60 + et.minute.values
def base_ok(d, slope=True):
    i, lg = d['i'], d['lg']; a = A[i]
    if not cs.cur_rule(d): return False
    w = hh24[i] - ll24[i]
    if w > 0 and w / a < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
    if slope and SLP[i] < .3: return False
    return True
def flipsim(s, i, lg, stop, sl=3.0):
    en = C[i]; g = 1 if lg else -1; sd = max(sl * A[i], 5); slv = en - g * sd
    for j in range(i + 1, N):
        if (L[j] <= slv) if lg else (H[j] >= slv): return -sd
        if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop: return g * (C[j] - en)
    return 0.
def run(slow, tp=1.75, flipride=True, slope=True):
    s = CASES[slow]; R = s.run(lambda d: base_ok(d, slope), q=dict(Q, tp=tp), gates=dict(R5=0, X4=0, MTF=0))
    R = [dict(r) for r in R]
    if flipride:
        for k, r in enumerate(R):
            if r['trig'] == 'flip':
                stop = R[k + 1]['i'] if k + 1 < len(R) else -1; r['res'] = flipsim(s, r['i'], r['lg'], stop)
    return R
def score(R):
    v = np.array([r['res'] - COST for r in R]); K = {(r['i'], r['lg']): r['res'] - COST for r in R}
    th = [sum(r['res'] - COST for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
    l4 = sum(r['res'] - COST for r in R if T[r['i']] >= t4); eq = np.cumsum(v)
    bt = {t: (sum(r['trig'] == t for r in R), sum(r['res'] - COST for r in R if r['trig'] == t)) for t in ('flip', 'ltf20', 'h9', 'h20')}
    rth = sum(r['res'] - COST for r in R if 570 <= mins[r['i']] < 960)
    return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std(), th=th, l4=l4, K=K, dd=(np.maximum.accumulate(eq) - eq).max(), w=100 * (v > 0).mean(), bt=bt, rth=rth)
def cmp(a, b):
    chg = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
    z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(chg)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
    vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
    return z, d_, l4, vd
if 'chk' in sys.argv:
    for sl in (0, 20):
        for kw in (dict(), dict(flipride=False), dict(flipride=False, slope=False)):
            a = score(run(sl, **kw)); print(sl, kw, a['n'], round(a['net']), [round(x) for x in a['th']], round(a['l4']))
    sys.exit()
fmt = lambda t: D.datetime.fromtimestamp(t / 1000, TZ).strftime('%m/%d')
out = [__doc__, '', 'Data: %d candles, %s → %s. Thirds %s–%s / %s–%s / %s–%s. Last 4 weeks from %s.' % (
    N, fmt(T[0]), fmt(T1), fmt(T0), fmt(cuts[0]), fmt(cuts[0]), fmt(cuts[1]), fmt(cuts[1]), fmt(T1), fmt(t4)), '']
TN = {'flip': 'Flip', 'ltf20': 'LTF20', 'h9': 'HTF9', 'h20': 'HTF20'}
for title, kw in (('A. Branch settings (slope 0.3 + flip ride), TP1 1.75', dict()),
                  ('B. Branch settings, TP1 1.5', dict(tp=1.5)),
                  ('C. Without the branch changes (v10.97 settings: no slope filter, flip setups use TP1)', dict(flipride=False, slope=False))):
    S = {sl: score(run(sl, **kw)) for sl in (20, 16, 14)}
    b = S[20]
    out += ['## ' + title, '', '| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9/20 | z | Δ by third | Δ last 4 wk | RTH net | Max DD | Verdict | By trigger (n / net) |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for sl, nm in ((20, '9 / 20 (current)'), (16, '7 / 16'), (14, '7 / 14')):
        a = S[sl]; z, d_, l4, vd = (0, [0, 0, 0], 0, 'baseline') if sl == 20 else cmp(a, b)
        out.append('| %s | %d | %.0f %% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %+.0f | %.0f | %s | %s |' % (
            nm, a['n'], a['w'], a['net'], a['avg'], a['net'] - b['net'], z, *d_, l4 if sl != 20 else a['l4'], a['rth'], a['dd'], vd,
            ' · '.join('%s %d / %+.0f' % (TN[t], *a['bt'][t]) for t in TN)))
    out += ['', '(9 / 20 row: "Δ last 4 wk" column = its own last-4-week net.)', '']
    print(title, file=sys.stderr, flush=True)
# 11/11 10:00-14:30 ET: setups drawn by each slow EMA (branch settings)
out += ['## 11/11 rally (10:00-14:30 ET), branch settings: setups per slow EMA', '']
for sl in (20, 16):
    R = run(sl); rr = [r for r in R if et[r['i']].strftime('%m/%d') == '11/11' and 600 <= mins[r['i']] <= 870]
    out.append('- slow %d: %s' % (sl, ', '.join('%s %s %s %+.2f' % (et[r['i']].strftime('%H:%M'), 'L' if r['lg'] else 'S', TN[r['trig']], r['res'] - COST) for r in rr) or 'none'))
# candidates before the branch filters, slow 16, same window (why skipped)
s = CASES[16]
cc = [d for d in s.cands if et[d['i']].strftime('%m/%d') == '11/11' and 600 <= mins[d['i']] <= 870]
out.append('- slow 16 raw triggers in the window: ' + (', '.join('%s %s %s (ER %.2f, range %s, slope %.2f)' % (et[d['i']].strftime('%H:%M'), 'L' if d['lg'] else 'S', TN[d['trig']], d['er'][12],
    'blk' if (lambda i, lg: (hh24[i] - ll24[i]) / A[i] < 5 and ((C[i] - ll24[i]) / (hh24[i] - ll24[i]) if lg else (hh24[i] - C[i]) / (hh24[i] - ll24[i])) >= .8)(d['i'], d['lg']) else 'ok', SLP[d['i']]) for d in cc) or 'none'))
V = {}
for kw in (dict(), dict(flipride=False, slope=False)):
    V[str(kw)] = score(run(0, **kw))['net']
out += ['', '## Check: baseline with the TradingView EMA20 from the bar feed (= project numbers)', '',
        '- Branch settings: %+.0f (mes_next 4a: +138). v10.97 settings: %+.0f (tsf / mes_next: -801).' % (V['{}'], V[str(dict(flipride=False, slope=False))]),
        '- The recomputed EMA20 baseline is lower (%+.0f / %+.0f), the gap is all in the last third (BarFeed period). Variants are compared to the recomputed 20 so all three use the same EMA method; against the TV-EMA20 baseline 7 / 16 is worse still.' % (
            score(run(20))['net'], score(run(20, flipride=False, slope=False))['net'])]
open('ema716_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
