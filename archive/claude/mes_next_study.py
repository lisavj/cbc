"""MES 3m next ideas -- HTF CBC Flip and the April-July stretch -- 11/14/2026.
BASELINE = current MES 3m filters (ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR) + "Block in chop: HTF EMA20 slope below 0.3 ATR"
(|15m EMA20 now - 12 bars ago| / ATR). Replay Jan 5 -> now, CBC engine setups, live exits (SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1),
net after 0.50 cost. One change at a time on top of the baseline; entry filters can change later setups (one at a time, cooldown).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, better in all three thirds and last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd, collections, datetime as D
import combo_study as cb, chop_sim as cs, late_study as ls
from zoneinfo import ZoneInfo
COST = .5; Q = dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7)
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase('MES', 3, B)
C, H, L, A = s.C, s.H, s.L, s.atr; S = pd.Series; N = s.n
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
hh24, ll24 = S(H).rolling(24).max().values, S(L).rolling(24).min().values
h20 = B.h20.values.astype(float); SLP = np.abs(h20 - np.roll(h20, 12)) / A
TZ = ZoneInfo('America/New_York'); et = pd.to_datetime(s.T, unit='ms', utc=True).tz_convert(TZ)
hour = et.hour.values; mon = et.month.values
# session date (18:00 ET start) -> daily close, 5-day EMA of daily closes (yesterday's value)
sd_ = B.hk.str[:10].values; dfd = pd.DataFrame({'d': sd_, 'c': C}).groupby('d', sort=True).c.last()
e5 = dfd.ewm(span=5, adjust=False).mean().shift(1); pdc = dfd.shift(1)
E5 = pd.Series(sd_).map(e5).values; PDC = pd.Series(sd_).map(pdc).values
ATR20 = S(A).rolling(20 * 460, min_periods=2000).mean().values
# flip-candle flop: HTF candle (hk group) holding the last flip bar crossed EMA200 / VWAP with < 70 % of its range on the flip side
grp = B.hk.values; gi = pd.Series(np.arange(N)).groupby(grp, sort=False)
ghi = S(H).groupby(grp, sort=False).transform('max').values; glo = S(L).groupby(grp, sort=False).transform('min').values
lastflip = np.full(N, -1); lf = -1
for i in range(N):
    if s.hf[i] != 0: lf = i
    lastflip[i] = lf
def flop(i, lg):
    k = lastflip[i]
    if k < 0: return False
    hi, lo = ghi[k], glo[k]; rng = hi - lo
    if rng <= 0: return False
    for lv in (s.e200[k], s.vw[k]):
        if lo < lv < hi and ((hi - lv) / rng if lg else (lv - lo) / rng) < .7: return True
    return False
MTF = getattr(s, 'mtf', None)
def base_ok(d):
    i, lg = d['i'], d['lg']; a = A[i]
    if not cs.cur_rule(d): return False
    w = hh24[i] - ll24[i]
    if w > 0 and w / a < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
    if SLP[i] < .3: return False
    return True
FL = lambda d: d['trig'] == 'flip'
def mkcount(n):
    st = dict(f=-1, c=0)
    def f(d):
        i = d['i']; k = lastflip[i]
        if k != st['f']: st['f'] = k; st['c'] = 0
        st['c'] += 1; return st['c'] <= n
    return f
def run(extra=None, flipq=None):
    st = None
    if extra and getattr(extra, 'stateful', False): pass
    R = s.run(lambda d: base_ok(d) and (extra is None or extra(d)), q=Q, gates=dict(R5=0, X4=0, MTF=0))
    if flipq:
        for k, r in enumerate(R):
            if r['trig'] == 'flip':
                stop = R[k + 1]['i'] if k + 1 < len(R) else -1; r = dict(r); R[k] = r; r['res'] = flipsim(r['i'], r['lg'], stop, **flipq)
    return R
def flipsim(i, lg, stop, tp=None, sl=3.0):
    en = C[i]; g = 1 if lg else -1; sd = max(sl * A[i], 5); slv = en - g * sd; t1 = en + g * tp * A[i] if tp else None
    for j in range(i + 1, N):
        if (L[j] <= slv) if lg else (H[j] >= slv): return -sd
        if t1 is not None and ((H[j] >= t1) if lg else (L[j] <= t1)): return tp * A[i]
        if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop: return g * (C[j] - en)
    return 0.
def score(R):
    v = np.array([r['res'] - COST for r in R]); K = {(r['i'], r['lg']): r['res'] - COST for r in R}
    th = [sum(r['res'] - COST for r in R if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
    l4 = sum(r['res'] - COST for r in R if s.T[r['i']] >= t4); eq = np.cumsum(v)
    fl = sum(r['res'] - COST for r in R if r['trig'] == 'flip')
    return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std(), th=th, l4=l4, K=K, dd=(np.maximum.accumulate(eq) - eq).max(), fl=fl, nf=sum(r['trig'] == 'flip' for r in R), w=100 * (v > 0).mean())
R0 = run(); L0 = score(R0)
V = [('1. HTF CBC Flip trigger OFF', lambda d: not FL(d), None),
     ('2a. Flips: skip when the flip is a flop (EMA200 / VWAP, 70 %)', lambda d: not (FL(d) and flop(d['i'], d['lg'])), None),
     ('2a. All setups: skip while the current flip is a flop', lambda d: not flop(d['i'], d['lg']), None),
     ('2b. Flips: EMA200 slope must agree (now vs 5 bars ago)', lambda d: not FL(d) or (s.e200[d['i']] - s.e200[d['i'] - 5] > 0) == d['lg'], None),
     ('2c. Flip min ER 0.30', lambda d: not FL(d) or d['er'][12] >= .30, None), ('2c. Flip min ER 0.35', lambda d: not FL(d) or d['er'][12] >= .35, None),
     ('2d. Flips: close beyond VWAP and EMA200 by 2 pts', lambda d: not FL(d) or (min(C[d['i']] - s.vw[d['i']], C[d['i']] - s.e200[d['i']]) if d['lg'] else min(s.vw[d['i']] - C[d['i']], s.e200[d['i']] - C[d['i']])) > 2, None),
     ('2d. Flips: close beyond VWAP and EMA200 by 3 pts', lambda d: not FL(d) or (min(C[d['i']] - s.vw[d['i']], C[d['i']] - s.e200[d['i']]) if d['lg'] else min(s.vw[d['i']] - C[d['i']], s.e200[d['i']] - C[d['i']])) > 3, None),
     ('3a. Only the first 1 signal after the HTF flip', 'cnt1', None), ('3b. Only the first 2 signals after the HTF flip', 'cnt2', None), ('3c. Only the first 3 signals after the HTF flip', 'cnt3', None),
     ('3d. Skip the flip itself; first pierce after it only', 'pb1', None),
     ('4a. Flip setups exit: flip + SL1 (no TP)', None, dict(tp=None)), ('4b. Flip setups exit: TP1 2.5 ATR', None, dict(tp=2.5)), ('4c. Flip setups exit: TP1 3.5 ATR', None, dict(tp=3.5)),
     ('5a. Flips only when the 1H CBC agrees', lambda d: not FL(d) or (MTF is not None and MTF[d['i']] == (1 if d['lg'] else 0)), None),
     ('5b. All setups only when the 1H CBC agrees', lambda d: MTF is not None and MTF[d['i']] == (1 if d['lg'] else 0), None),
     ('7a. Daily trend: long above / short below yesterday\'s 5-day EMA', lambda d: not np.isfinite(E5[d['i']]) or (C[d['i']] > E5[d['i']]) == d['lg'], None),
     ('7b. Daily trend: no shorts above the 5-day EMA (bot rule)', lambda d: d['lg'] or not np.isfinite(E5[d['i']]) or C[d['i']] <= E5[d['i']], None),
     ('7c. Long above / short below yesterday\'s close', lambda d: not np.isfinite(PDC[d['i']]) or (C[d['i']] > PDC[d['i']]) == d['lg'], None),
     ('8a. Skip while ATR > 1.3 x its 20-day average', lambda d: not (ATR20[d['i']] > 0 and A[d['i']] > 1.3 * ATR20[d['i']]), None),
     ('8b. Skip while ATR > 1.6 x its 20-day average', lambda d: not (ATR20[d['i']] > 0 and A[d['i']] > 1.6 * ATR20[d['i']]), None),
     ('10a. Longs only', lambda d: d['lg'], None), ('10b. Shorts only', lambda d: not d['lg'], None),
     ('11. + Environment EMA200 vs VWAP (v10.97 checkbox)', lambda d: (s.e200[d['i']] > s.vw[d['i']]) == d['lg'], None),
     ('1 + 11. Flip OFF + EMA200 vs VWAP', lambda d: not FL(d) and (s.e200[d['i']] > s.vw[d['i']]) == d['lg'], None)]
rows = []; cand = []
for nm, f, fq in V:
    if isinstance(f, str):
        if f.startswith('cnt'): f = mkcount(int(f[3:]))
        elif f == 'pb1':
            st = dict(f=-1, used=False)
            def f(d, st=st):
                k = lastflip[d['i']]
                if k != st['f']: st['f'] = k; st['used'] = False
                if FL(d): return False
                if st['used']: return False
                st['used'] = True; return True
    a = score(run(f, fq)); chg = sum(1 for k in set(a['K']) | set(L0['K']) if abs(a['K'].get(k, 1e9) - L0['K'].get(k, 1e9)) > 1e-9) or 1
    z = (a['net'] - L0['net']) / (L0['sd'] * np.sqrt(chg)); d_ = [p - q for p, q in zip(a['th'], L0['th'])]; l4 = a['l4'] - L0['l4']
    vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'robust except last 4 wk' if z >= 2 and all(t > 0 for t in d_) else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'worse' if a['net'] < L0['net'] else 'noise'
    rows.append('| %s | %d | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %d / %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['avg'], a['net'] - L0['net'], z, *d_, l4, a['nf'], a['fl'], a['dd'], vd))
    if vd in ('robust', 'robust except last 4 wk', 'promising'): cand.append('- %s: %+.0f (net %+.0f), z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, %d setups, max DD %.0f (%s)' % (nm, a['net'] - L0['net'], a['net'], z, *d_, l4, a['n'], a['dd'], vd))
    print(nm, file=sys.stderr, flush=True)
# diagnostics on the baseline
def tab(keyf, labels, title):
    g = collections.defaultdict(list)
    for r in R0: g[keyf(r)].append(r)
    o = ['### %s' % title, '', '| Group | Setups | Net | Avg | Win % | Flip net | Longs net | Shorts net | Avg ATR |', '|---|---|---|---|---|---|---|---|---|']
    for k in labels:
        R = g.get(k, [])
        if not R: continue
        v = np.array([r['res'] - COST for r in R])
        o.append('| %s | %d | %+.0f | %+.2f | %.0f %% | %+.0f | %+.0f | %+.0f | %.1f |' % (k, len(R), v.sum(), v.mean(), 100 * (v > 0).mean(), sum(r['res'] - COST for r in R if r['trig'] == 'flip'),
                 sum(r['res'] - COST for r in R if r['lg']), sum(r['res'] - COST for r in R if not r['lg']), np.mean([A[r['i']] for r in R])))
    return o + ['']
MN = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
diag = tab(lambda r: MN[mon[r['i']] - 1], MN, 'Baseline by month')
diag += tab(lambda r: '%02d:00' % hour[r['i']], ['%02d:00' % h for h in [18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], 'Baseline by hour (ET, candle start)')
diag += tab(lambda r: ('RTH 9:30-16:00' if 570 <= hour[r['i']] * 60 + et.minute.values[r['i']] < 960 else 'Overnight'), ['RTH 9:30-16:00', 'Overnight'], 'Baseline by session')
diag += tab(lambda r: {'flip': 'HTF CBC Flip', 'ltf20': 'LTF EMA20 Pierce', 'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}.get(r['trig'], r['trig']) + (' long' if r['lg'] else ' short'),
            [a + b for a in ('HTF CBC Flip', 'LTF EMA20 Pierce', 'HTF EMA9 Pierce', 'HTF EMA20 Pierce') for b in (' long', ' short')], 'Baseline by trigger and direction')
# daily trend context per month: share of trend days (|close - open| > 60 % of range)
dd = pd.DataFrame({'d': sd_, 'o': B.o.values, 'h': H, 'l': L, 'c': C}).groupby('d').agg(o=('o', 'first'), h=('h', 'max'), l=('l', 'min'), c=('c', 'last'))
dd['m'] = pd.to_datetime(dd.index).month; dd['tr'] = (dd.c - dd.o).abs() / (dd.h - dd.l) > .6; dd['rg'] = dd.h - dd.l
diag += ['### Market by month (daily candles)', '', '| Month | Days | Avg daily range | Trend days (body > 60 % of range) | Month change |', '|---|---|---|---|---|']
for m_, g_ in dd.groupby('m'): diag.append('| %s | %d | %.0f | %.0f %% | %+.0f |' % (MN[m_ - 1], len(g_), g_.rg.mean(), 100 * g_.tr.mean(), g_.c.iloc[-1] - g_.o.iloc[0]))
out = [__doc__, '', '## Baseline (current + slope 0.3): %d setups, net %+.0f, avg %+.2f, win %.0f %%, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, flips %d / %+.0f, max DD %.0f' % (
    L0['n'], L0['net'], L0['avg'], L0['w'], *L0['th'], L0['l4'], L0['nf'], L0['fl'], L0['dd']), '', '## Candidates', ''] + (cand or ['- none']) + ['', '## All variants', '',
    '| Change | Setups | Net | Avg | Δ | z | Δ by third | Δ last 4 wk | Flips n / net | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|---|---|'] + rows + ['', '## Diagnostics (baseline)', ''] + diag
open('mes_next_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
