#!/usr/bin/env python3
"""(A) MES 3m slow chart EMA 20 vs 14 vs 16 replay (copy of project claude/mes3_watch_a.py).
11/09: LIVE tp 1.75 (v10.82+); variants TP1 1.75 (live) and TP1 1.5."""
import sys, json, datetime as D
import numpy as np, pandas as pd
import chop_sim as cs
SLOWS = [(20, '9 / 20 (live)'), (14, '7 / 14'), (16, '7 / 16')]
def load(path, tf=3):
    B = pd.DataFrame(json.load(open(path))['bars'])
    if 'live' in B:
        B = B[B['live'].isna() | (B['live'] == 0)]
    B = B.sort_values('t').drop_duplicates('t', keep='last').reset_index(drop=True)
    for c in B.columns:
        if c != 'fl':
            B[c] = pd.to_numeric(B[c], errors='coerce')
    for c in ('nyh', 'nyl', 'lnh', 'lnl', 'ash', 'asl', 'e200', 'vw', 'e20', 'h9', 'h20', 'hc', 'hf'):
        if c not in B:
            B[c] = np.nan
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // (5 * tf)).astype(str)
    B['sess'] = start.dt.strftime('%Y-%m-%d')
    B['last'] = B.groupby('hk').t.transform('max')
    B['hf'] = B['hf'].fillna(0)
    return B
class MCase(cs.Case):
    LATEW = 1
    LATEAWAY = 0.0  # None = strict (MES 3m v10.60); number = late-away pts
    def gen(s):
        C, H, L = s.C, s.H, s.L; out = []; n = s.n; hk = 5
        e20, h9, h20 = s.e20, s.h9, s.h20
        flip_ok = np.zeros(n, bool); fev = np.zeros(n, int); fo = False; pend = 0; TW = s.LATEAWAY
        for i in range(n):
            if s.hf[i] != 0:
                away = (C[i] > h20[i]) if s.hf[i] == 1 else (C[i] < h20[i])
                fo = away; pend = 0
                if away: fev[i] = s.hf[i]
                elif TW is not None: pend = s.hf[i]
            elif pend:
                if (pend == 1 and C[i] > h20[i] + TW) or (pend == -1 and C[i] < h20[i] - TW):
                    fo = True; fev[i] = pend; pend = 0
            flip_ok[i] = fo
        om = (s.hm - s.tf) % 1440
        orf = ((om >= 570) & (om < 600)) | ((om >= 180) & (om < 210)) | ((om >= 1200) & (om < 1230))
        vwb = np.zeros(n, int); st = 0; lastb = -99; bdir = 0
        for i in range(1, n):
            xd = C[i] < s.vw[i] and C[i - 1] >= s.vw[i - 1]; xu = C[i] > s.vw[i] and C[i - 1] <= s.vw[i - 1]
            if (xu and st == -1) or (xd and st == 1): lastb = i; bdir = st
            st = 0 if s.hf[i] != 0 else (-1 if (xd and s.hdir[i] == 0) else 1 if (xu and s.hdir[i] == 1) else 0 if (xu or xd) else st)
            vwb[i] = bdir if i - lastb <= 5 else 0
        s.vwb = vwb
        lastp = -99
        FD = {'MGC': 10, 'MES': 8}.get(s.sym, 0)
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
                lg = fev[i] == 1; vw, e2 = s.vw[i], s.e200[i]
                side = (C[i] > max(vw, e2) + 1) if lg else (C[i] < min(vw, e2) - 1)
                vws = (s.vw[i] - s.vw[i - hk]) * (1 if lg else -1) > 0
                fd = abs(C[i] - e20[i]) <= max(2 * s.atr[i], FD)
                if side and vws and fd: out.append(dict(i=i, lg=lg, trig='flip'))
            for nm, line, mn in (('ltf20', e20, .08), ('h9', h9, .15), ('h20', h20, .15)):
                lg = dirn
                if nm == 'ltf20' and pierce(line, i, lg):
                    if i - lastp <= 3: continue
                    lastp = i
                if pierce(line, i, lg):
                    if (C[i] > line[i]) if lg else (C[i] < line[i]): out.append(dict(i=i, lg=lg, trig=nm, erm=mn))
                    else:
                        W = s.LATEW if nm == 'ltf20' else 1
                        for k in range(1, W + 1):
                            if i + k >= n or s.hdir[i + k] != s.hdir[i]: break
                            if (C[i + k] > line[i + k]) if lg else (C[i + k] < line[i + k]):
                                out.append(dict(i=i + k, lg=lg, trig=nm, erm=mn, late=k)); break
        out.sort(key=lambda d: (d['i'], d['trig'] != 'flip'))
        for d in out:
            i = d['i']; lg = d['lg']; A = s.atr[i]; gg = 1 if lg else -1
            hi = s.H[i - 23:i + 1].max(); lo = s.L[i - 23:i + 1].min(); pos = (C[i] - lo) / (hi - lo) if hi > lo else .5
            d['R5'] = (pos if lg else 1 - pos) >= .8 and (hi - lo) / A < 5
            d['X4'] = gg * (C[i] - s.vw[i]) / A > 4
            d['M'] = s.mtf[i] >= 0 and s.mtf[i] != (1 if lg else 0)
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={k: s.er[k][i] for k in s.er}, bo=bool(s.bo[i]), month=s.month[i], atrrel=s.atrrel[i])
        return out
    def sim1(s, i, lg, q, stop_at):
        C, H, L, O = s.C, s.H, s.L, s.O; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            m = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= m < 960 or 1080 <= m < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'
G = dict(R5=1, X4=0, MTF=0)
LIVE = dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part='tod', be=True, tr=1.7)   # = mes3_ema_grid.LIVE (v10.82+)
TRG = (('flip', 'Flip'), ('ltf20', 'LTF20'), ('h9', 'HTF9'), ('h20', 'HTF20'))
def ema(x, n):
    return pd.Series(x).ewm(span=n, adjust=False).mean().values
def main():
    B0 = load(sys.argv[1]); C = B0.c.values.astype(float)
    cases = {}
    MCase.LATEAWAY = None
    for sl, _ in SLOWS:
        B = B0.copy(); B['e20'] = ema(C, sl); cases[sl] = MCase('MES', 3, B)
    s0 = cases[20]
    T0, T1 = s0.T[300], s0.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
    third = lambda t: 0 if t < cuts[0] else 1 if t < cuts[1] else 2
    t4 = T1 - 28 * 86400000
    sess = B0['sess'].values; days = sorted(set(sess)); last5 = set(days[-6:-1]) if days[-1] == sess[-1] and len(B0[B0.sess == days[-1]]) < 200 else set(days[-5:])
    sess_t = dict(zip(B0.t.values, sess))
    fmt = lambda t: D.datetime.fromtimestamp(t / 1000).strftime('%m/%d')
    L = ['Data: %d candles, %s → %s. Thirds %s–%s / %s–%s / %s–%s. Last 4 weeks from %s; last 5 trading days: %s (Globex sessions).' % (
        len(B0), fmt(s0.T[0]), fmt(T1), fmt(T0), fmt(cuts[0]), fmt(cuts[0]), fmt(cuts[1]), fmt(cuts[1]), fmt(T1), fmt(t4), ', '.join(d[5:].replace('-', '/') for d in sorted(last5))), '']
    J = {}
    for tpn, tp in (('TP1 1.75 (live)', 1.75), ('TP1 1.5', 1.5)):
        q = dict(LIVE, tp=tp)
        R = {sl: cases[sl].run(lambda d: cs.cur_rule(d), q=q, gates=G) for sl, _ in SLOWS}
        b = R[20]; bv = [r['res'] for r in b]; bn = sum(bv); sd = float(np.std(bv)) or 1; bset = {(r['i'], r['lg']) for r in b}
        def agg(sl, res, f):
            return sum(r['res'] for r in res if f(cases[sl].T[r['i']]))
        L += ['#### Live exits, %s' % tpn, '',
              '| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |',
              '|---|---|---|---|---|---|---|---|---|---|---|---|']
        bt = [agg(20, b, lambda t, k=k: third(t) == k) for k in range(3)]
        b4 = agg(20, b, lambda t: t >= t4); b5 = agg(20, b, lambda t: sess_t[t] in last5)
        for sl, nm in SLOWS:
            res = R[sl]; v = [r['res'] for r in res]; net = sum(v); w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
            ch = len(bset ^ {(r['i'], r['lg']) for r in res}) or 1; z = (net - bn) / (sd * np.sqrt(ch))
            dth = [agg(sl, res, lambda t, k=k: third(t) == k) - bt[k] for k in range(3)]; b3 = all(x > 0 for x in dth)
            vd = 'baseline' if sl == 20 else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < bn else 'noise'
            d4 = agg(sl, res, lambda t: t >= t4) - b4; d5 = agg(sl, res, lambda t: sess_t[t] in last5) - b5
            bytr = []
            for tg, tn in TRG:
                rr = [r for r in res if r['trig'] == tg]; bb = [r for r in b if r['trig'] == tg]
                dt4 = sum(r['res'] for r in rr if cases[sl].T[r['i']] >= t4) - sum(r['res'] for r in bb if s0.T[r['i']] >= t4)
                bytr.append('%s %d / %+.0f (%+.0f)' % (tn, len(rr), sum(r['res'] for r in rr), dt4))
            L.append('| %s | %d | %d%% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %+.1f | %+.1f | %s |' % (
                nm, len(v), round(100 * w / max(1, w + l)), net, net / max(1, len(v)), net - bn, 0 if sl == 20 else z, *dth, vd,
                d4 if sl != 20 else b4, d5 if sl != 20 else b5, ' · '.join(bytr)))
            J['%s|%d' % (tp, sl)] = dict(net=net, d=net - bn, z=0 if sl == 20 else z, th=dth, vd=vd, d4=d4, d5=d5, n=len(v))
        L += ['', '(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)', '']
    print('\n'.join(L))
    json.dump(J, open('a_summary.json', 'w'), default=float)
if __name__ == '__main__':
    main()
