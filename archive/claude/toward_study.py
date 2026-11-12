#!/usr/bin/env python3
"""'Toward' HTF flip study -- 11/03/2026. All symbols x 2m / 3m / 5m.

Question: CBC skips setups after a TOWARD HTF CBC flip ("Include 'toward' HTF flips" OFF, the default) and, with "toward flip:
allow setups once a candle closes on the away side by (pts)" ON (1 pt), lets them in from the first candle that closes 1 pt beyond
the HTF EMA20 on the away side (that candle also fires the HTF CBC Flip trigger). Toward flip = long flip closing BELOW the HTF
EMA20 (short: above). Should toward flips be allowed, and is the late-away rule worth keeping?
Modes: LIVE = toward off + late-away 1 pt (current defaults) · STRICT = toward off, no late-away · LATE0 = late-away 0 pts ·
ON = toward flips allowed (every trigger, flip trigger on every flip).
Engine: chop_sim (triggers HTF CBC Flip with the live flip gates -- VWAP+EMA200 side 1 pt, VWAP slope, distance 2 ATR / pts floor --
LTF EMA20 Pierce, HTF EMA9 / EMA20 Pierce, 1-bar late; ER 0.23 chop rule with breakout exception; VWAP bounce block; cooldown 10;
opening-range windows; live per-chart gates: range gate MES/MGC 3m, VWAP stretch 4 ATR MGC 3m, 1H MTF gate MES 2m).
Exits: live per symbol -- base SL1 1.7 ATR (cap / minimum per symbol), TP1 1.7 ATR (cap per symbol), 80 % at TP1, BE, trail 1.7;
MES 3m: SL1 3.0 ATR (min 5, no cap), TP1 1.75 ATR (no cap), 100 % at TP1.
Data: server archive (Databento rebuild + BarFeed): 3m / 5m from 01/05, 2m from 06/01; MCL / BTC only since late Oct.
~50 % exact match with live setups: compare modes, not totals. z = change / (SD x sqrt(setups changed)); robust = z >= 2 and
better in all three equal-time thirds; promising = z >= 1 and all three better.
Usage: python3 toward_study.py SYM TF  (needs chop_sim.py next to it)
"""
import sys, gzip, json, time, urllib.request, datetime as D
import numpy as np, pandas as pd
import chop_sim as cs

BASE = 'https://tv-webhook-dashboard.onrender.com'
FROM = {3: '2026-01-05', 2: '2026-06-01', 5: '2026-01-05'}
MIN = dict(MGC=5, MES=5, MNQ=25, M2K=3, MCL=0.3, BTC=300)
SCAP = dict(MGC=7, MES=8, MNQ=30, M2K=5, MCL=0.3, BTC=500)
TCAP = dict(MGC=6, MES=6, MNQ=40, M2K=3, MCL=0.3, BTC=300)
FDP = dict(MGC=10, MES=8, MCL=0.3, BTC=300, MNQ=50)
TW = 1.0


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
            err = e; time.sleep(30)
    raise err


def load(sym, tf):
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    B = pd.DataFrame(get('%s/bars?sym=%s&days=400&from=%s' % (BASE, key, FROM[tf]))['bars'])
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
    B['last'] = B.groupby('hk').t.transform('max')
    B['hf'] = B['hf'].fillna(0)
    return B


class TCase(cs.Case):
    MODE = 'live'

    def gen(s):
        mode = s.MODE
        C, H, L = s.C, s.H, s.L; out = []; n = s.n; hk = 5
        e20, h9, h20 = s.e20, s.h9, s.h20
        flip_ok = np.zeros(n, bool); fev = np.zeros(n, int); tow = np.zeros(n, bool); fo = False; pend = 0
        for i in range(n):
            if s.hf[i] != 0:
                away = (C[i] > h20[i]) if s.hf[i] == 1 else (C[i] < h20[i])
                pend = 0
                if mode == 'on':
                    fo = True; fev[i] = s.hf[i]; tow[i] = not away
                else:
                    fo = away
                    if away:
                        fev[i] = s.hf[i]
                    elif mode in ('live', 'late0'):
                        pend = s.hf[i]
            elif pend:
                tp = TW if mode == 'live' else 0.0
                if (pend == 1 and C[i] > h20[i] + tp) or (pend == -1 and C[i] < h20[i] - tp):
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
        s.flip_ok = flip_ok; s.orf = orf; s.vwb = vwb
        FD = FDP.get(s.sym, 0)
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
                fd = abs(C[i] - e20[i]) <= max(2 * s.atr[i], FD)
                if side and vws and fd: out.append(dict(i=i, lg=lg, trig='flip', tow=bool(tow[i]), late=int(s.hf[i] == 0)))
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
            i = d['i']; lg = d['lg']; A = s.atr[i]; gg = 1 if lg else -1
            hi = s.H[i - 23:i + 1].max(); lo = s.L[i - 23:i + 1].min(); pos = (C[i] - lo) / (hi - lo) if hi > lo else .5
            d['R5'] = (pos if lg else 1 - pos) >= .8 and (hi - lo) / A < 5
            d['xv'] = gg * (C[i] - s.vw[i]) / A
            d['X4'] = d['xv'] > 4
            d['M'] = s.mtf[i] >= 0 and s.mtf[i] != (1 if lg else 0)
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={k: s.er[k][i] for k in s.er}, bo=bool(s.bo[i]), month=s.month[i])
        return out

    def sim1(s, i, lg, q, stop_at):
        C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (q['part'] * tpd + (1 - q['part']) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if q['part'] >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (q['part'] * tpd + (1 - q['part']) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'


def exits(sym, tf):
    if (sym, tf) == ('MES', 3):
        return dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=False, tr=1.7)
    return dict(sl=1.7, mn=MIN[sym], cap=SCAP[sym], tp=1.7, tcap=TCAP[sym], part=.8, be=True, tr=1.7)


def run(s):
    G = cs.GATE.get((s.sym, s.tf), dict(R5=0, X4=0, MTF=0))
    return s.run(lambda d: cs.cur_rule(d), q=exits(s.sym, s.tf), gates=G)


def main():
    sym, tf = sys.argv[1], int(sys.argv[2])
    B = load(sym, tf)
    if len(B) < 600:
        print('## %s %dm — only %d candles, skipped\n' % (sym, tf, len(B))); return
    s = TCase(sym, tf, B)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
    third = lambda i: 0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2
    R = {}
    for m in ('live', 'strict', 'late0', 'on'):
        s.MODE = m; s.cands = s.gen(); R[m] = run(s)
    base = R['live']; bv = [r['res'] for r in base]; bn = sum(bv); sd = float(np.std(bv)) or 1
    bset = {(r['i'], r['lg']) for r in base}
    th = lambda res: [sum(r['res'] for r in res if third(r['i']) == k) for k in range(3)]
    bt = th(base)
    first, last = [D.datetime.fromtimestamp(t / 1000).strftime('%m/%d') for t in (s.T[0], s.T[-1])]
    nflip = int((s.hf != 0).sum()); ntow = sum(1 for i in np.where(s.hf != 0)[0] if not ((s.C[i] > s.h20[i]) if s.hf[i] == 1 else (s.C[i] < s.h20[i])))
    L = ['## %s %dm — %s to %s, %d candles; HTF flips %d, toward %d (%.0f%%)' % (sym, tf, first, last, len(B), nflip, ntow, 100 * ntow / max(1, nflip)), '',
         '| Mode | Setups | Win % | Net | Avg | Δ vs live | z | Δ by third | Verdict | Flip setups (late) |', '|---|---|---|---|---|---|---|---|---|---|']
    nm = dict(live='LIVE: toward off + late-away 1 pt', strict='STRICT: toward off, no late-away', late0='Late-away 0 pts', on='ON: toward flips allowed')
    summ = []
    for m in ('live', 'strict', 'late0', 'on'):
        res = R[m]; v = [r['res'] for r in res]; net = sum(v); w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
        ch = len(bset ^ {(r['i'], r['lg']) for r in res}) or 1; z = (net - bn) / (sd * np.sqrt(ch))
        dth = [a - b for a, b in zip(th(res), bt)]; b3 = all(x > 0 for x in dth)
        vd = 'baseline' if m == 'live' else 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < bn else 'noise'
        fl = [r for r in res if r['trig'] == 'flip']
        L.append('| %s | %d | %d%% | %+.1f | %+.2f | %+.1f | %+.1f | %+.1f / %+.1f / %+.1f | %s | %d / %+.1f (late %d) |' % (
            nm[m], len(v), round(100 * w / max(1, w + l)), net, net / max(1, len(v)), net - bn, z if m != 'live' else 0, *dth, vd,
            len(fl), sum(r['res'] for r in fl), sum(1 for r in fl if r.get('late'))))
        if vd in ('robust', 'promising'): summ.append('%s %dm: %s → %+.1f, z %+.1f, thirds %+.1f / %+.1f / %+.1f (%s)' % (sym, tf, nm[m], net - bn, z, *dth, vd))
    # setups that exist only with toward ON (after toward flips)
    extra = [r for r in R['on'] if (r['i'], r['lg']) not in bset]
    gone = [r for r in base if (r['i'], r['lg']) not in {(x['i'], x['lg']) for x in R['on']}]
    L += ['', 'ON vs LIVE: %d setups only with toward ON, net %+.1f, win %d%% (flip trigger %d / %+.1f); %d live setups displaced, net %+.1f.' % (
        len(extra), sum(r['res'] for r in extra), round(100 * sum(r['res'] > 0 for r in extra) / max(1, sum(r['res'] != 0 for r in extra))),
        sum(r['trig'] == 'flip' for r in extra), sum(r['res'] for r in extra if r['trig'] == 'flip'), len(gone), sum(r['res'] for r in gone))]
    lt = [r for r in base if r['trig'] == 'flip' and r.get('late')]
    L.append('Late-away flip setups in LIVE: %d, net %+.1f, win %d%%.' % (len(lt), sum(r['res'] for r in lt), round(100 * sum(r['res'] > 0 for r in lt) / max(1, len(lt)))))
    L.append('SUMMARY: ' + (' | '.join(summ) if summ else 'none'))
    print('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
