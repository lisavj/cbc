#!/usr/bin/env python3
"""MES 3m chart (LTF) EMA + SL/TP grid study -- 11/04/2026.

Question: with chart EMAs 7 / 14, 7 / 16 or 6 / 14 instead of 9 / 20 (CBC v10.50 "Chart EMA fast / slow / 200"), how does
MES 3m do on the live exits (v10.54: SL1 3.0 ATR min 5, TP1 1.75 ATR, no caps; close at TP1 80 % 06:00-16:00 and
18:00-22:30 ET with BE + trail 1.7, else 100 %), and is SL 3 / TP1 1.75 still the best stop / target with each EMA set?
Engine: chop_sim (HTF CBC Flip with live flip gates, LTF EMA20 Pierce on the SLOW chart EMA, HTF EMA9 / EMA20 Pierce, 1-bar
late; ER 0.23 chop rule + breakout exception; VWAP bounce block; cooldown 10; opening-range windows; range gate 24 bars /
5 ATR ON; toward HTF flips off, late-away OFF on MES 3m (v10.60)). Only the SLOW chart EMA changes the replay -- the fast EMA
only feeds the cloud / "price past both EMA clouds" gate, which is not modelled -- so 7 / 14 and 6 / 14 replay the same.
Data: server archive MES 3m (Databento rebuild + BarFeed) Jan 5 -> now. ~50 % exact match with live setups: compare
variants, not totals. z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds
(Jan-Mar / Apr-Jun / Jul-now); promising = z >= 1 and all three better.
Usage: python3 mes3_ema_grid.py   (needs chop_sim.py next to it)
"""
import sys, gzip, json, time, pickle, os, urllib.request, datetime as D
import numpy as np, pandas as pd
import chop_sim as cs

BASE = 'https://tv-webhook-dashboard.onrender.com'
SLOWS = [(20, '9 / 20 (current)'), (14, '7 / 14 and 6 / 14'), (16, '7 / 16')]


def get(url):
    err = None
    for _ in range(4):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=300) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception as e:
            err = e; time.sleep(20)
    raise err


def load():
    cache = '/tmp/mes3_bars.pkl'
    if os.path.exists(cache):
        return pd.read_pickle(cache)
    B = pd.DataFrame(get(BASE + '/bars?sym=MES&days=400&from=2026-01-05')['bars'])
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
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // 15).astype(str)
    B['last'] = B.groupby('hk').t.transform('max')
    B['hf'] = B['hf'].fillna(0)
    B.to_pickle(cache)
    return B


class MCase(cs.Case):
    """Strict toward-flip mode (MES 3m v10.60) + exits with per-setup close-at-TP1 % by NY time of day."""

    def gen(s):
        C, H, L = s.C, s.H, s.L; out = []; n = s.n; hk = 5
        e20, h9, h20 = s.e20, s.h9, s.h20
        flip_ok = np.zeros(n, bool); fev = np.zeros(n, int); fo = False
        for i in range(n):
            if s.hf[i] != 0:
                away = (C[i] > h20[i]) if s.hf[i] == 1 else (C[i] < h20[i])
                fo = away
                if away: fev[i] = s.hf[i]
            flip_ok[i] = fo
        om = (s.hm - s.tf) % 1440
        orf = ((om >= 570) & (om < 570 + getattr(s, 'NYW', 30))) | ((om >= 180) & (om < 210)) | ((om >= 1200) & (om < 1230))
        vwb = np.zeros(n, int); st = 0; lastb = -99; bdir = 0
        for i in range(1, n):
            xd = C[i] < s.vw[i] and C[i - 1] >= s.vw[i - 1]; xu = C[i] > s.vw[i] and C[i - 1] <= s.vw[i - 1]
            if (xu and st == -1) or (xd and st == 1): lastb = i; bdir = st
            st = 0 if s.hf[i] != 0 else (-1 if (xd and s.hdir[i] == 0) else 1 if (xu and s.hdir[i] == 1) else 0 if (xu or xd) else st)
            vwb[i] = bdir if i - lastb <= 5 else 0
        s.vwb = vwb
        lastp = -99

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
                fd = abs(C[i] - e20[i]) <= max(2 * s.atr[i], 8)
                if side and vws and fd: out.append(dict(i=i, lg=lg, trig='flip'))
            for nm, line, mn in (('ltf20', e20, .08), ('h9', h9, .15), ('h20', h20, .15)):
                lg = dirn
                if nm == 'ltf20' and pierce(line, i, lg):
                    if i - lastp <= 3: continue
                    lastp = i
                if pierce(line, i, lg):
                    if (C[i] > line[i]) if lg else (C[i] < line[i]): out.append(dict(i=i, lg=lg, trig=nm, erm=mn))
                    elif i + 1 < n and s.hdir[i + 1] == s.hdir[i] and ((C[i + 1] > line[i + 1]) if lg else (C[i + 1] < line[i + 1])): out.append(dict(i=i + 1, lg=lg, trig=nm, erm=mn, late=1))
        out.sort(key=lambda d: (d['i'], d['trig'] != 'flip'))
        for d in out:
            i = d['i']; lg = d['lg']; A = s.atr[i]
            hi = s.H[i - 23:i + 1].max(); lo = s.L[i - 23:i + 1].min(); pos = (C[i] - lo) / (hi - lo) if hi > lo else .5
            d['R5'] = (pos if lg else 1 - pos) >= .8 and (hi - lo) / A < 5
            d['X4'] = False; d['M'] = False
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={k: s.er[k][i] for k in s.er}, bo=bool(s.bo[i]), month=s.month[i])
        return out

    def sim1(s, i, lg, q, stop_at):
        C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':  # live MES 3m: 80 % inside 06:00-16:00 / 18:00-22:30 ET (candle open time), else 100 %
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


LIVE = dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part='tod', be=True, tr=1.7)
BASEX = dict(sl=1.7, mn=5, cap=8, tp=1.7, tcap=6, part=.8, be=True, tr=1.7)
G = dict(R5=1, X4=0, MTF=0)


def run(s, q):
    return s.run(lambda d: cs.cur_rule(d), q=q, gates=G)


def ema(x, n):
    return pd.Series(x).ewm(span=n, adjust=False).mean().values


def main():
    B0 = load()
    C = B0.c.values.astype(float)
    cases = {}
    for sl, _ in SLOWS:
        B = B0.copy(); B['e20'] = ema(C, sl)
        cases[sl] = MCase('MES', 3, B)
    s0 = cases[20]
    T0, T1 = s0.T[300], s0.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
    third = lambda s, i: 0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2
    fmt = lambda t: D.datetime.fromtimestamp(t / 1000).strftime('%m/%d')
    out = ['# MES 3m chart EMA + SL/TP grid — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '',
           'Data: %d candles, %s → %s. Thirds: %s–%s / %s–%s / %s–%s.' % (len(B0), fmt(s0.T[0]), fmt(s0.T[-1]), fmt(T0), fmt(cuts[0]), fmt(cuts[0]), fmt(cuts[1]), fmt(cuts[1]), fmt(T1)), '']
    th = lambda s, res: [sum(r['res'] for r in res if third(s, r['i']) == k) for k in range(3)]

    def bytrig(res):
        return ' · '.join('%s %d / %+.0f' % (nm, sum(r['trig'] == t for r in res), sum(r['res'] for r in res if r['trig'] == t))
                          for t, nm in (('flip', 'Flip'), ('ltf20', 'LTF20'), ('h9', 'HTF9'), ('h20', 'HTF20')))

    # ---- A. EMA comparison on live exits and on base exits
    summ = []
    for qn, q in (('live MES 3m exits (SL 3 / TP1 1.75 / time-of-day 80-100 %)', LIVE), ('base exits (SL 1.7 + min 5 cap 8 / TP1 1.7 cap 6 / 80 % + BE + trail)', BASEX)):
        R = {sl: run(cases[sl], q) for sl, _ in SLOWS}
        b = R[20]; bv = [r['res'] for r in b]; bn = sum(bv); sd = float(np.std(bv)) or 1; bset = {(r['i'], r['lg']) for r in b}; bt = th(s0, b)
        out += ['## A. Chart EMA, %s' % qn, '', '| Chart EMA | Setups | Win % | Net | Avg | Δ vs 9 / 20 | z | Δ by third | Verdict | By trigger (setups / net) |', '|---|---|---|---|---|---|---|---|---|---|']
        for sl, nm in SLOWS:
            res = R[sl]; v = [r['res'] for r in res]; net = sum(v); w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
            ch = len(bset ^ {(r['i'], r['lg']) for r in res}) or 1; z = (net - bn) / (sd * np.sqrt(ch))
            dth = [a - c for a, c in zip(th(cases[sl], res), bt)]; b3 = all(x > 0 for x in dth)
            vd = 'baseline' if sl == 20 else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < bn else 'noise'
            out.append('| %s | %d | %d%% | %+.0f | %+.2f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s | %s |' % (
                nm, len(v), round(100 * w / max(1, w + l)), net, net / max(1, len(v)), net - bn, 0 if sl == 20 else z, *dth, vd, bytrig(res)))
            t4 = s0.T[-1] - 28 * 86400000
            if sl != 20:
                summ.append('%s, %s: Δ %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f (%s); last 4 weeks Δ %+.1f' % (
                    nm, 'live exits' if q is LIVE else 'base exits', net - bn, z, *dth, vd,
                    sum(r['res'] for r in res if cases[sl].T[r['i']] >= t4) - sum(r['res'] for r in b if s0.T[r['i']] >= t4)))
        out.append('')

    # ---- B. SL / TP grid per EMA
    STOPS = (1.7, 2.0, 2.5, 3.0, 3.5)
    TPS = (1.25, 1.5, 1.75, 2.0, 2.5)
    PARTS = (('tod', 'live 80/100 % by time'), (1.0, '100 %'), (.8, '80 % + BE + trail'))
    best_all = {}
    for sl, nm in SLOWS:
        s = cases[sl]
        grid = {}
        for sk in STOPS:
            for tk in TPS:
                for pk, _ in PARTS:
                    q = dict(LIVE, sl=sk, tp=tk, part=pk)
                    res = run(s, q); v = [r['res'] for r in res]
                    n = len(v); h = n // 2
                    grid[(sk, tk, pk)] = (sum(v), n, sum(v[:h]) > 0 and sum(v[h:]) > 0, all(x > 0 for x in th(s, res)),
                                          round(100 * sum(x > 0 for x in v) / max(1, sum(x != 0 for x in v))))

        def nb(k):
            sk, tk, pk = k; o = []
            for arr, idx in ((STOPS, 0), (TPS, 1)):
                i = arr.index(k[idx])
                for j in (i - 1, i + 1):
                    if 0 <= j < len(arr):
                        k2 = list(k); k2[idx] = arr[j]; o.append(grid[tuple(k2)][0])
            return o
        rob = lambda k: grid[k][3] and grid[k][0] > 0 and all(x > 0 for x in nb(k))
        out += ['## B. SL / TP1 grid — chart EMA %s (net pts; ✱ both halves +, T all three thirds +, R = T and every ±1-step stop / TP neighbour +)' % nm, '']
        for pk, pn in PARTS:
            out += ['**Close at TP1: %s**' % pn, '', '| Stop \\ TP1 | ' + ' | '.join('%.2f ATR' % t for t in TPS) + ' |', '|---|' + '---|' * len(TPS)]
            for sk in STOPS:
                cells = []
                for tk in TPS:
                    net, n, both, t3, wr = grid[(sk, tk, pk)]
                    cells.append('%+.0f%s%s%s' % (net, ' ✱' if both else '', ' T' if t3 else '', ' R' if rob((sk, tk, pk)) else ''))
                out.append('| %.1f ATR | %s |' % (sk, ' | '.join(cells)))
            out.append('')
        top = sorted(grid.items(), key=lambda kv: -kv[1][0])[:5]
        cur = grid[(3.0, 1.75, 'tod')]
        out += ['Current live (3.0 / 1.75 / time of day): %+.0f, %d setups, win %d%%%s.' % (cur[0], cur[1], cur[4], ', R' if rob((3.0, 1.75, 'tod')) else ''),
                'Top 5: ' + '; '.join('SL %.1f / TP1 %.2f / %s = %+.0f (win %d%%%s)' % (k[0], k[1], dict(PARTS)[k[2]], v[0], v[4], ', R' if rob(k) else '') for k, v in top),
                'Robust cells: %d of %d.' % (sum(rob(k) for k in grid), len(grid)), '']
        best_all[sl] = (cur, top[0])
    out += ['## Summary', ''] + ['- ' + x for x in summ] + ['- Grid best vs current live exits: ' + '; '.join(
        '%s: best SL %.1f / TP1 %.2f / %s %+.0f vs current %+.0f' % (dict(SLOWS)[sl], b[1][0][0], b[1][0][1], dict(PARTS)[b[1][0][2]], b[1][1][0], b[0][0]) for sl, b in best_all.items())]
    print('\n'.join(out))


if __name__ == '__main__':
    main()
