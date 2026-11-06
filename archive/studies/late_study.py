#!/usr/bin/env python3
"""LTF EMA20 Pierce late-confirm window study -- 11/05/2026.
Question: CBC "LTF pierce late-confirm window (bars)" = 1 (one setting for every chart). If the pierce candle does not close back
beyond the slow chart EMA, the next N candles may (first close back beyond the line, HTF direction unchanged). Best N per chart?
Engine: mes3_ema_grid MCase (chop_sim rules), LTF late window = N (0 = pierce candle only). Charts on live settings:
MES 3m slow 14 and slow 20 (live exits SL 3 / TP1 2.0 / time-of-day close), MGC 3m slow 20 (range gate + VWAP stretch 4 ATR,
base exits). Jan 5 -> now. z / robust / promising as in the other studies (thirds = equal time).
Usage: python3 late_study.py   (needs chop_sim.py + mes3_ema_grid.py next to it)"""
import numpy as np, pandas as pd, datetime as D
import chop_sim as cs, mes3_ema_grid as m

class LCase(m.MCase):
    LATE = 1
    def gen(s):
        # same as MCase.gen, but the LTF late confirm looks N bars ahead
        late = s.LATE; keep = m.MCase.gen
        out = keep(s)
        out = [d for d in out if not (d['trig'] == 'ltf20' and d.get('late'))]
        C, H, L = s.C, s.H, s.L; e20 = s.e20; n = s.n
        have = {(d['i'], d['trig']) for d in out}
        # LTF pierce candles that did NOT close beyond: rebuild with window N
        lastp = -99; extra = []
        flip_ok = np.zeros(n, bool); fo = False
        for i in range(n):
            if s.hf[i] != 0: fo = (C[i] > s.h20[i]) if s.hf[i] == 1 else (C[i] < s.h20[i])
            flip_ok[i] = fo
        om = (s.hm - s.tf) % 1440
        orf = ((om >= 570) & (om < 570 + getattr(s, 'NYW', 30))) | ((om >= 180) & (om < 210)) | ((om >= 1200) & (om < 1230))
        for i in range(250, n - 1):
            if np.isnan(s.atr[i]) or s.hdir[i] < 0 or (16 * 60 <= s.hm[i] < 18 * 60 + 30) or orf[i] or not flip_ok[i]: continue
            lg = s.hdir[i] == 1
            pier = (L[i - 1] > e20[i - 1] and L[i] <= e20[i] <= H[i]) if lg else (H[i - 1] < e20[i - 1] and L[i] <= e20[i] <= H[i])
            if not pier: continue
            if i - lastp <= 3: continue
            lastp = i
            if (C[i] > e20[i]) if lg else (C[i] < e20[i]): continue
            for k in range(1, late + 1):
                j = i + k
                if j >= n or s.hdir[j] != s.hdir[i]: break
                if (C[j] > e20[j]) if lg else (C[j] < e20[j]):
                    extra.append(dict(i=j, lg=lg, trig='ltf20', erm=.08, late=k)); break
        for d in extra:
            i = d['i']; A = s.atr[i]; lg = d['lg']; gg = 1 if lg else -1
            hi = s.H[i - 23:i + 1].max(); lo = s.L[i - 23:i + 1].min(); pos = (C[i] - lo) / (hi - lo) if hi > lo else .5
            d['R5'] = (pos if lg else 1 - pos) >= .8 and (hi - lo) / A < 5
            d['xv'] = gg * (C[i] - s.vw[i]) / A; d['X4'] = d['xv'] > 4; d['M'] = False
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={kk: s.er[kk][i] for kk in s.er}, bo=bool(s.bo[i]), month=s.month[i])
        out += extra
        out.sort(key=lambda d: (d['i'], d['trig'] != 'flip'))
        return out

def load(sym, tf=3):
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    B = pd.DataFrame(m.get(m.BASE + '/bars?sym=%s&days=400&from=%s' % (key, '2026-06-01' if tf == 2 else '2026-01-05'))['bars'])
    if 'live' in B: B = B[B['live'].isna() | (B['live'] == 0)]
    B = B.sort_values('t').drop_duplicates('t', keep='last').reset_index(drop=True)
    for c in B.columns:
        if c != 'fl': B[c] = pd.to_numeric(B[c], errors='coerce')
    for c in ('nyh','nyl','lnh','lnl','ash','asl','e200','vw','e20','h9','h20','hc','hf'):
        if c not in B: B[c] = np.nan
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // (5 * tf)).astype(str); B['last'] = B.groupby('hk').t.transform('max'); B['hf'] = B['hf'].fillna(0)
    return B

MGCX = dict(sl=1.7, mn=5, cap=7, tp=1.7, tcap=6, part=.8, be=True, tr=1.7)
MESX = dict(sl=1.7, mn=5, cap=8, tp=1.7, tcap=6, part=.8, be=True, tr=1.7)
CHARTS2 = [('MES 2m slow 14 (MTF gate)', 'MES', 2, 14, MESX, dict(R5=0, X4=0, MTF=1)),
           ('MGC 2m slow 20', 'MGC', 2, 20, MGCX, dict(R5=0, X4=0, MTF=0)),
           ('MES 5m slow 20', 'MES', 5, 20, MESX, dict(R5=0, X4=0, MTF=0)),
           ('MGC 5m slow 20', 'MGC', 5, 20, MGCX, dict(R5=0, X4=0, MTF=0))]
CHARTS = [('MES 3m slow 14 (live 7/14)', 'MES', 14, dict(m.LIVE, tp=2.0), dict(R5=1, X4=0, MTF=0)),
          ('MES 3m slow 20 (9/20)', 'MES', 20, dict(m.LIVE, tp=2.0), dict(R5=1, X4=0, MTF=0)),
          ('MGC 3m slow 20', 'MGC', 20, MGCX, dict(R5=1, X4=1, MTF=0))]

def main():
    out = ['# LTF EMA20 Pierce late-confirm window — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    data = {}; summ = []
    import sys
    LIST = CHARTS2 if 'more' in sys.argv else [(a, b, 3, c, d, e) for a, b, c, d, e in CHARTS]
    for nm, sym, tf, sl, q, G in LIST:
        if (sym, tf) not in data: data[(sym, tf)] = load(sym, tf)
        B = data[(sym, tf)].copy(); B['e20'] = m.ema(B.c.values.astype(float), sl)
        R = {}
        for N in range(0, 6):
            LCase.LATE = N; s = LCase(sym, tf, B)
            R[N] = (s, s.run(lambda d: cs.cur_rule(d), q=q, gates=G))
        s1, b = R[1]; bv = [r['res'] for r in b]; bn = sum(bv); sd = float(np.std(bv)) or 1; bset = {(r['i'], r['lg']) for r in b}
        T0, T1 = s1.T[300], s1.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
        th = lambda res: [sum(r['res'] for r in res if (0 if s1.T[r['i']] < cuts[0] else 1 if s1.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
        bt = th(b); t4 = s1.T[-1] - 28 * 86400000
        out += ['## %s — %d candles' % (nm, len(B)), '', '| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |', '|---|---|---|---|---|---|---|---|---|---|---|']
        for N in range(0, 6):
            s, res = R[N]; v = [r['res'] for r in res]; net = sum(v); w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
            ch = len(bset ^ {(r['i'], r['lg']) for r in res}) or 1; z = (net - bn) / (sd * np.sqrt(ch))
            dth = [a - c for a, c in zip(th(res), bt)]; b3 = all(x > 0 for x in dth)
            vd = 'baseline' if N == 1 else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < bn else 'noise'
            lt = [r for r in res if r['trig'] == 'ltf20']; ll = [r for r in lt if r.get('late')]
            d4 = sum(r['res'] for r in res if s.T[r['i']] >= t4) - sum(r['res'] for r in b if s1.T[r['i']] >= t4)
            out.append('| %d%s | %d | %d%% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %d / %+.0f (late %d / %+.0f) | %+.1f |' % (
                N, ' (current)' if N == 1 else '', len(v), round(100 * w / max(1, w + l)), net, net / max(1, len(v)), net - bn, 0 if N == 1 else z, *dth, vd,
                len(lt), sum(r['res'] for r in lt), len(ll), sum(r['res'] for r in ll), d4))
            if vd in ('robust', 'promising'): summ.append('%s: window %d → %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s)' % (nm, N, net - bn, z, *dth, vd))
        out.append('')
    out += ['## Candidates (robust / promising)', ''] + (['- ' + x for x in summ] if summ else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    main()
