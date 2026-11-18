"""MES 3m -- VWAP stretch gate, flop skip, flip-count gate -- 11/18/2026.
Base = current CBC EMA Slope MES 3m (v1.19 logic = v1.23): slope 0.42 / 12 bars, LTF ER 0.15, range gate 5, hour block 13-15,
no new setups 16:00-19:00, flip setups ride (closed by HTF flip back / SL1 / next setup); SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1.
Engine = claude/noflip_study.py TCase (Jan 5 -> now). Net after 0.50 cost. One gate at a time on top of the base.
Stretch = (close - VWAP) / ATR in the trade direction against you, i.e. short = (VWAP - close)/ATR (price far below VWAP).
Flop = the 15m candle holding the current HTF flip crossed EMA200 / VWAP with < 70 % of its range on the flip side (= ats_flg);
 '+ pivots' also counts any cross of PP / R1-R3 / S1-S3 (= the alert's "Flip flop: crossed ..." text).
Flip count = HTF flips in the last N 15m candles (5 x 3m bars each), incl. the current one.
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds."""
import sys, numpy as np, pandas as pd, datetime as D
import chop_sim as cs, ema716_eng as eng, noflip_study as nf
X = nf.CH['MES']; B = eng.load('MES', 3, X['f']); h20raw = B.h20.values.astype(float); o = X['base']
P = dict(nf.TDEF, fdp=X['fdp'], tw=X['tw'], erl=o['erl']); P.update(o['P'])
nf.TCase.P = P; s = nf.TCase('MES', 3, B); s.P = P
C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n; S = pd.Series
hh24, ll24 = S(H).rolling(24).max().values, S(L).rolling(24).min().values
SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A
grp = B.hk.values
ghi = S(H).groupby(grp, sort=False).transform('max').values; glo = S(L).groupby(grp, sort=False).transform('min').values
pp, r1, s1 = B.pp.values.astype(float), B.r1.values.astype(float), B.s1.values.astype(float)
dh, dl = 2 * pp - s1, 2 * pp - r1
PIV = [pp, r1, s1, pp + (dh - dl), pp - (dh - dl), dh + 2 * (pp - dl), dl - 2 * (dh - pp)]
lastflip = np.full(N, -1); lf = -1; fl = (s.hf != 0).astype(float)
for i in range(N):
    if s.hf[i] != 0: lf = i
    lastflip[i] = lf
FC = {n: S(fl).rolling(5 * n, min_periods=1).sum().values for n in (4, 8, 16)}
def flop(i, lg, piv):
    k = lastflip[i]
    if k < 0: return False
    hi, lo = ghi[k], glo[k]; rng = hi - lo
    if rng <= 0: return False
    for lv in (s.e200[k], s.vw[k]):
        if lo < lv < hi and ((hi - lv) / rng if lg else (lv - lo) / rng) < .7: return True
    if piv:
        for p in PIV:
            if not np.isnan(p[k]) and lo < p[k] < hi: return True
    return False
def base(d):
    i, lg = d['i'], d['lg']; a = A[i]
    if not cs.cur_rule(d): return False
    w = hh24[i] - ll24[i]
    if w > 0 and w / a < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
    if SLP[i] < .42: return False
    if ((s.hm[i] - 3) % 1440) // 60 in (13, 14): return False
    return True
FLIP = lambda d: d['trig'] == 'flip'
strx = lambda d: -(1 if d['lg'] else -1) * (C[d['i']] - s.vw[d['i']]) / A[d['i']]   # >0 = price stretched AGAINST the trade side (short far below VWAP)
strw = lambda d: (1 if d['lg'] else -1) * (C[d['i']] - s.vw[d['i']]) / A[d['i']]    # >0 = price on the trade side (short below VWAP) = chop_sim X4 sense
T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
def sc(extra):
    R = s.run(lambda d: base(d) and (extra is None or extra(d)), dict(X['q'], nf=0), False)
    v = np.array([r['res'] - .5 for r in R]); eq = np.cumsum(v)
    th = [sum(r['res'] - .5 for r in R if (0 if T[r['i']] < cuts[0] else 1 if T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
    return dict(n=len(v), net=v.sum(), avg=v.mean(), sd=v.std() or 1, th=th, l4=sum(r['res'] - .5 for r in R if T[r['i']] >= t4), w=100 * (v > 0).mean(),
                dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(r['i'], r['lg']): r['res'] - .5 for r in R}, R=R)
V = [('Base (current MES 3m)', None)]
for x in (3, 3.5, 4):
    V.append(('Stretch: skip all setups > %.1f ATR beyond VWAP on the trade side' % x, lambda d, x=x: strw(d) <= x))
    V.append(('Stretch: skip FLIP setups > %.1f ATR beyond VWAP' % x, lambda d, x=x: not FLIP(d) or strw(d) <= x))
V += [('Flop skip, flip setups (EMA200/VWAP, 70 %) = ats_flg', lambda d: not (FLIP(d) and flop(d['i'], d['lg'], False))),
      ('Flop skip, flip setups, + pivots', lambda d: not (FLIP(d) and flop(d['i'], d['lg'], True))),
      ('Flop skip, ALL setups (EMA200/VWAP)', lambda d: not flop(d['i'], d['lg'], False)),
      ('Flop skip, ALL setups, + pivots', lambda d: not flop(d['i'], d['lg'], True))]
for n, k in ((4, 2), (4, 3), (8, 3), (8, 4), (16, 4), (16, 5)):
    V.append(('Flip count: skip when >= %d HTF flips in last %d 15m candles' % (k, n), lambda d, n=n, k=k: FC[n][d['i']] < k))
if __name__ == '__main__':
    b = sc(None); rows = []; ex = {}
    for nm, f in V:
        a = b if f is None else sc(f)
        ch = sum(1 for kk in set(a['K']) | set(b['K']) if abs(a['K'].get(kk, 1e9) - b['K'].get(kk, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d_ = [p - q for p, q in zip(a['th'], b['th'])]; l4 = a['l4'] - b['l4']
        vd = '' if f is None else 'robust' if z >= 2 and all(t > 0 for t in d_) and l4 >= 0 else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'robustly worse' if z <= -2 and all(t < 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
        rows.append('| %s | %d | %+.0f | %+.2f | %.0f %% | %+.0f | %d | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['avg'], a['w'], a['net'] - b['net'], ch, z, *d_, l4, a['dd'], vd))
        print(rows[-1], file=sys.stderr, flush=True)
        # 11/17 marked setups
        if f is not None:
            hit = []
            for r in b['R']:
                t = pd.Timestamp(T[r['i']] + 180000, unit='ms', tz='UTC').tz_convert('America/New_York')
                if t.strftime('%m/%d') in ('11/17', '11/18') and not f(r): hit.append('%s %s %s' % (t.strftime('%m/%d %H:%M'), 'L' if r['lg'] else 'S', r['trig']))
            ex[nm] = hit
    mk = []
    for r in b['R']:
        t = pd.Timestamp(T[r['i']] + 180000, unit='ms', tz='UTC').tz_convert('America/New_York')
        if t.strftime('%m/%d') in ('11/17', '11/18'):
            mk.append('| %s | %s | %s | %.2f | %+.1f | %+.1f | %s / %d / %d |' % (t.strftime('%m/%d %H:%M'), 'LONG' if r['lg'] else 'SHORT', r['trig'], C[r['i']], strw(r), r['res'] - .5,
                      'flop' if flop(r['i'], r['lg'], False) else ('pivot flop' if flop(r['i'], r['lg'], True) else '-'), FC[8][r['i']], FC[16][r['i']]))
    out = [__doc__, '', 'Bars to %s. Base: %d setups, net %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f.' % (D.datetime.utcfromtimestamp(T[-1] / 1000).strftime('%m/%d %H:%M UTC'), b['n'], b['net'], *b['th'], b['l4']), '',
           '| Gate | Setups | Net | Avg | Win % | vs base | Changed | z | Change by third | Last 4 wk | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|---|---|---|'] + rows + ['',
           '## 11/17-11/18 setups in the replay (base)', '', '| Close ET | Dir | Trigger | Entry | Stretch (ATR, trade side) | Net | Flop / flips last 8 / 16 |', '|---|---|---|---|---|---|---|'] + mk + ['', '## Which 11/17-11/18 setups each gate removes', ''] + \
          ['- %s: %s' % (k, ', '.join(v) or 'none') for k, v in ex.items()]
    open('mes_stretch_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
