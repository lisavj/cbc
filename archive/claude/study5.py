#!/usr/bin/env python3
"""5m version of the 3m exit / filter / stop work -- MES 5m and MGC 5m -- 11/08/2026.
Same steps as on 3m, re-searched on 5m (the 3m settings are not assumed to carry over):
 1. EXITS: TP rule (TP1 -> Y % of its distance from the candle after X min) x SL rule (one check X min after entry: CUT = close,
    HALF = SL1 to half distance, if negative / < 25 % / < 50 % of TP1). X = 10-40 min (5m candles).
 2. ENTRY FILTERS: skip setups against 60m CBC / EMA200 slope 1 h, 3 h / VWAP / previous session close / 5-day EMA (both sides or
    shorts only).
 3. SESSION STOPS: per 18-18 session (K losses in a row or N flip-outs), the same only when the previous 5 sessions lost, and K
    losses counted separately in Asia (18-03 ET) / London (03-09:30) / NY (09:30-16).
 4. COMBINED: the best of each step (best = largest whole-period gain among rules better than current in all three thirds after
    costs / beyond random), every combination re-simulated together.
Each step also shows a walk-forward check: the rule picked on thirds 1-2 only, scored on third 3.
Replay = chop_sim rules (late window 1, NY OR block 30) on CBC default 5m exits: SL1 1.7 x ATR, min 5, cap MES 8 / MGC 7,
TP1 1.7 x ATR cap 6, 80 % at TP1 + BE + trail 1.7; no range / stretch gate (5m charts are not listed). 5m bars Jan 5 -> now.
Costs: commission + 1 tick per trade (MES 0.50 / MGC 0.22 pts), +1 tick for a rule exit at the candle close.
Cells: net after costs; (beyond random) = gain minus dropping the same number of trades at random."""
import sys, itertools, pickle, numpy as np, pandas as pd, collections as C, datetime as D
import combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg

SET = {'MES': ('MES 5m', ls.MESX, .50, .25), 'MGC': ('MGC 5m', ls.MGCX, .22, .10)}
GD = dict(R5=0, X4=0, MTF=0)
TXS = [10, 15, 20, 25, 30, 40]; TYS = [.65, .75, .85]
SLS = [('CUT', 0.0), ('CUT', .25), ('CUT', .5), ('HALF', 0.0), ('HALF', .5)]; SXS = [10, 15, 20, 25, 30]
TPO = [(0, 0.0)] + [(x, y) for y in TYS for x in TXS]; SLO = [(None, 0.0, 0)] + [(a, y, x) for a, y in SLS for x in SXS]
YN = {0.0: 'negative', .25: '< 25 %', .5: '< 50 %'}
def tpn(t): return 'TP off' if t[0] == 0 else 'TP1 -> %d %% after %d min' % (round(t[1] * 100), t[0])
def sln(c): return 'SL off' if c[0] is None else '%s if %s at %d min' % ('close' if c[0] == 'CUT' else 'half SL1', YN[c[1]], c[2])
SUBS = ['Asia', 'London', 'NY']
def sub(mm): return 'Asia' if (mm >= 1080 or mm < 180) else 'London' if mm < 570 else 'NY' if mm < 960 else 'late'
PER = [('Third 1', lambda t: t['th'] == 0), ('Third 2', lambda t: t['th'] == 1), ('Third 3', lambda t: t['th'] == 2), ('Last 4 wk', lambda t: t['l4']), ('Whole', lambda t: True)]

# ---------- session stops ----------
def g_session(r, K, N):
    keep = []; stop = set()
    for t in sorted(r, key=lambda t: t['i']):
        if t['ss'] in stop: continue
        fin = sorted([u for u in keep if u['ss'] == t['ss'] and u['j'] < t['i']], key=lambda u: u['j']); ls_ = 0
        for u in fin: ls_ = ls_ + 1 if u['n'] < 0 else 0
        fo = sum(1 for u in fin if u['why'] == 'flip' and u['n'] < 0)
        if (K and ls_ >= K) or (N and fo >= N): stop.add(t['ss']); continue
        keep.append(t)
    return keep
def regime(b, ns):
    net = C.OrderedDict()
    for t in sorted(b, key=lambda t: t['i']): net[t['ss']] = net.get(t['ss'], 0) + t['n']
    ks = list(net); return {s: sum(net[x] for x in ks[max(0, k - ns):k]) < 0 for k, s in enumerate(ks)}
def g_regime(r, b, K, N, ns):
    act = regime(b, ns); gi = {t['i'] for t in g_session(r, K, N)}
    return [t for t in r if t['i'] in gi or not act.get(t['ss'], False)]
def g_sub(r, Ks):
    keep = []; stop = set()
    for t in sorted(r, key=lambda t: t['i']):
        key = (t['ss'], t['sub']); K = Ks[SUBS.index(t['sub'])] if t['sub'] in SUBS else 0
        if not K: keep.append(t); continue
        if key in stop: continue
        fin = sorted([u for u in keep if (u['ss'], u['sub']) == key and u['j'] < t['i']], key=lambda u: u['j']); ls_ = 0
        for u in fin: ls_ = ls_ + 1 if u['n'] < 0 else 0
        if ls_ >= K: stop.add(key); continue
        keep.append(t)
    return keep
STOPS = {}
for K, N in itertools.product((0, 2, 3), (0, 2, 3)):
    if K or N:
        STOPS['session: %s' % ' or '.join(x for x in ('%d losses' % K if K else '', '%d flip-outs' % N if N else '') if x)] = ('s', K, N)
        STOPS['session, only after 5 losing sessions: %s' % ' or '.join(x for x in ('%d losses' % K if K else '', '%d flip-outs' % N if N else '') if x)] = ('r', K, N)
for Ks in itertools.product((0, 1, 2, 3), repeat=3):
    if any(Ks): STOPS['sub-session losses: Asia %s / London %s / NY %s' % tuple(k or 'off' for k in Ks)] = ('u', Ks)
def apply_stop(st, r, b):
    if st is None: return r
    if st[0] == 's': return g_session(r, st[1], st[2])
    if st[0] == 'r': return g_regime(r, b, st[1], st[2], 5)
    return g_sub(r, st[1])

def ev(v, b):
    ab = np.mean([t['n'] for t in b]); o = []
    for _, P in PER:
        n1 = sum(t['n'] for t in v if P(t)); n0 = sum(t['n'] for t in b if P(t)); c1 = sum(1 for t in v if P(t)); c0 = sum(1 for t in b if P(t))
        o.append((n1, n1 - n0, n1 - n0 + (c0 - c1) * ab))
    return o
def pstats(v):
    v = np.array(v) if len(v) else np.zeros(0); w = v[v > 0].sum(); l = -v[v < 0].sum(); eq = np.cumsum(v)
    dd = (np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max() if len(v) else 0
    return '%d / %+.0f / %d %% / %.2f / %.0f' % (len(v), v.sum(), round(100 * (v > 0).sum() / max(1, (v != 0).sum())), (w / l if l else 0), dd)

def run_sym(sym):
    nm, q, cost, tick = SET[sym]
    B = ls.load(sym, 5); ls.LCase.LATE = 1; ls.LCase.NYW = 30
    s = cb.CCase(sym, 5, B); TR, ss = tg.trend_arrays(s)
    et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); mm = (et.dt.hour * 60 + et.dt.minute).values
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def run(f, tp, slr):
        def ok(d):
            if not cs.cur_rule(d): return False
            if f is None or (f[1] == 'S' and d['lg']): return True
            v = TR[f[0]][d['i']]; return v == 0 or v == (1 if d['lg'] else -1)
        cb.CCase.TX, cb.CCase.TY = tp; cb.CCase.ACT, cb.CCase.SY, cb.CCase.SX = slr
        r = s.run(ok, q=q, gates=GD)
        return [dict(i=t['i'], j=t['j'], lg=t['lg'], why=t['why'], n=t['res'] - cost - (tick if t['why'] == 'cut' else 0),
                     th=0 if s.T[t['i']] < cuts[0] else 1 if s.T[t['i']] < cuts[1] else 2, l4=bool(s.T[t['i']] >= t4), ss=ss[t['i']], sub=sub(mm[t['i']])) for t in r]
    X = dict(nm=nm, first=D.datetime.utcfromtimestamp(T0 / 1000).strftime('%m/%d'), last=D.datetime.utcfromtimestamp(T1 / 1000).strftime('%m/%d'))
    X['ex'] = {(tp, sl): run(None, tp, sl) for tp in TPO for sl in SLO}
    print(sym, 'exits done', flush=True)
    FILTS = [None] + [(t, w) for t in tg.TRENDS for w in ('B', 'S')]
    X['flt'] = {f: run(f, TPO[0], SLO[0]) for f in FILTS}
    pickle.dump(X, open('s5_%s.pkl' % sym, 'wb'))
    # step 4 needs the picks: computed here so the combined runs use the same picks as the report
    b = X['ex'][(TPO[0], SLO[0])]
    def good(o): return all(o[k][2] > 0 for k in range(3))
    ex = {k: ev(v, b) for k, v in X['ex'].items() if k != (TPO[0], SLO[0])}
    exg = [k for k in ex if all(ex[k][i][1] > 0 for i in range(3))]
    pick_ex = max(exg, key=lambda k: ex[k][4][1]) if exg else None
    fl = {f: ev(v, b) for f, v in X['flt'].items() if f is not None}
    flg = [f for f in fl if good(fl[f])]; pick_f = max(flg, key=lambda f: fl[f][4][2]) if flg else None
    stp = {k: ev(apply_stop(st, b, b), b) for k, st in STOPS.items()}
    stg = [k for k in stp if good(stp[k])]; pick_s = max(stg, key=lambda k: stp[k][4][2]) if stg else None
    X['pick'] = (pick_ex, pick_f, pick_s)
    comb = {}
    tps = [(TPO[0], SLO[0])] + ([pick_ex] if pick_ex else [])
    if pick_ex: tps += [(pick_ex[0], SLO[0]), (TPO[0], pick_ex[1])]
    for f in [None] + ([pick_f] if pick_f else []):
        for exk in dict.fromkeys(tps):
            r = run(f, *exk)
            for son in (False, True) if pick_s else (False,):
                comb[(f, son, exk)] = apply_stop(STOPS[pick_s], r, b) if son else r
    X['comb'] = comb
    pickle.dump(X, open('s5_%s.pkl' % sym, 'wb')); print(sym, 'done', flush=True)

def report():
    L = ['# 5m charts: exits, filters, session stops and all combined — MES 5m and MGC 5m — %s' % D.datetime.now().strftime('%m/%d/%Y'), '', __doc__.strip(), '']
    summ = []
    for sym in ('MES', 'MGC'):
        X = pickle.load(open('s5_%s.pkl' % sym, 'rb')); b = X['ex'][(TPO[0], SLO[0])]; cur = ev(b, b)
        def good(o): return all(o[k][2] > 0 for k in range(3))
        def cells(o, beyond=True): return ' | '.join('%+.0f (%+.0f)' % (o[k][0], o[k][2]) for k in range(5))
        hdr = ['| Rule | ' + ' | '.join(p for p, _ in PER) + ' | Trades | |', '|---|' + '---|' * (len(PER) + 2)]
        L += ['## %s — current exits: %d setups %s–%s' % (X['nm'], len(b), X['first'], X['last']), '',
              'Current exits after costs: ' + ', '.join('%s %+.0f' % (p, cur[k][0]) for k, (p, _) in enumerate(PER)) + '. Full stats (trades / net / win % / profit factor / max drawdown): ' + pstats([t['n'] for t in b]), '']
        # 1 exits
        ex = {k: ev(v, b) for k, v in X['ex'].items() if k != (TPO[0], SLO[0])}
        def exflag(k):
            o = ex[k]; t = all(o[i][1] > 0 for i in range(3)); return ('T' if t else '') + ('4' if o[3][1] > 0 else '')
        L += ['### 1. Exit rules (Δ vs current exits after costs; T = better in all three thirds, 4 = better in the last 4 weeks)', '']
        L += ['**TP rule alone — Δ whole period**', '', '| X min | ' + ' | '.join('%d %%' % round(y * 100) for y in TYS) + ' |', '|---|' + '---|' * len(TYS)]
        for x in TXS: L.append('| %d | %s |' % (x, ' | '.join('%+.0f %s' % (ex[((x, y), SLO[0])][4][1], exflag(((x, y), SLO[0]))) for y in TYS)))
        L += ['', '**SL rule alone — Δ whole period**', '', '| X min | ' + ' | '.join('%s %s' % ('close' if a == 'CUT' else 'half SL1', YN[y]) for a, y in SLS) + ' |', '|---|' + '---|' * len(SLS)]
        for x in SXS: L.append('| %d | %s |' % (x, ' | '.join('%+.0f %s' % (ex[(TPO[0], (a, y, x))][4][1], exflag((TPO[0], (a, y, x)))) for a, y in SLS)))
        exg = sorted([k for k in ex if all(ex[k][i][1] > 0 for i in range(3))], key=lambda k: -ex[k][4][1])
        L += ['', 'Combinations better in all three thirds: %d of %d. Top 5:' % (len(exg), len(ex)), ''] + hdr
        for k in exg[:5]: L.append('| %s + %s | %s | %d | %s |' % (tpn(k[0]), sln(k[1]), ' | '.join('%+.0f (Δ %+.0f)' % (ex[k][i][0], ex[k][i][1]) for i in range(5)), len(X['ex'][k]), exflag(k)))
        pk = max(ex, key=lambda k: ex[k][0][1] + ex[k][1][1]); l3 = sorted(v[2][1] for v in ex.values())
        L += ['', 'Walk-forward: picked on thirds 1-2 = **%s + %s** → third 3 Δ **%+.0f** (rank %d of %d; median %+.0f).' % (
            tpn(pk[0]), sln(pk[1]), ex[pk][2][1], sum(1 for v in l3 if v > ex[pk][2][1]) + 1, len(l3), l3[len(l3) // 2]), '']
        # 2 filters
        fl = {f: ev(v, b) for f, v in X['flt'].items() if f is not None}
        L += ['### 2. Entry filters (current exits; net after costs, beyond random in brackets; ✓ = beyond random positive in all three thirds)', ''] + hdr
        for f in sorted(fl, key=lambda f: -fl[f][4][2]): L.append('| %s | %s | %d | %s |' % (tg.tfn(f), cells(fl[f]), len(X['flt'][f]), '✓' if good(fl[f]) else ''))
        pf = max(fl, key=lambda f: fl[f][0][2] + fl[f][1][2]); l3 = sorted(v[2][2] for v in fl.values())
        L += ['', 'Walk-forward: picked on thirds 1-2 = **%s** → third 3 beyond random **%+.0f** (rank %d of %d).' % (tg.tfn(pf), fl[pf][2][2], sum(1 for v in l3 if v > fl[pf][2][2]) + 1, len(l3)), '']
        # 3 stops
        stp = {k: ev(apply_stop(st, b, b), b) for k, st in STOPS.items()}
        stg = sorted([k for k in stp if good(stp[k])], key=lambda k: -stp[k][4][2])
        L += ['### 3. Session stops (current exits, no filter) — %d of %d qualify (✓); top 8 qualifying, then top 5 overall' % (len(stg), len(stp)), ''] + hdr
        for k in stg[:8]: L.append('| %s | %s | %d | ✓ |' % (k, cells(stp[k]), len(apply_stop(STOPS[k], b, b))))
        for k in sorted(stp, key=lambda k: -stp[k][4][2])[:5]:
            if k not in stg[:8]: L.append('| %s | %s | %d | %s |' % (k, cells(stp[k]), len(apply_stop(STOPS[k], b, b)), '✓' if good(stp[k]) else ''))
        ps = max(stp, key=lambda k: stp[k][0][2] + stp[k][1][2]); l3 = sorted(v[2][2] for v in stp.values())
        L += ['', 'Walk-forward: picked on thirds 1-2 = **%s** → third 3 beyond random **%+.0f** (rank %d of %d).' % (ps, stp[ps][2][2], sum(1 for v in l3 if v > stp[ps][2][2]) + 1, len(l3)), '']
        # 4 combined
        pe, pf_, ps_ = X['pick']
        L += ['### 4. Combined (the best qualifying rule of each step)', '',
              '- Exits: %s' % ('%s + %s' % (tpn(pe[0]), sln(pe[1])) if pe else 'none qualified (kept current)'),
              '- Filter: %s' % (tg.tfn(pf_) if pf_ else 'none qualified'), '- Session stop: %s' % (ps_ or 'none qualified'), '',
              '| Filter / stop / exits | ' + ' | '.join(p for p, _ in PER) + ' | Trades | |', '|---|' + '---|' * (len(PER) + 2)]
        rows = []
        for (f, son, exk), v in X['comb'].items():
            o = ev(v, b); xl = 'current exits' if exk == (TPO[0], SLO[0]) else 'TP + SL rules' if exk[0] != TPO[0] and exk[1] != SLO[0] else 'TP rule' if exk[0] != TPO[0] else 'SL rule'
            rows.append(('%s / %s / %s' % ('filter' if f else '—', 'stop' if son else '—', xl), o, v))
        for lab, o, v in sorted(rows, key=lambda x: -x[1][4][0]):
            L.append('| %s | %s | %d | %s%s |' % (lab, cells(o), len(v), '✓' if good(o) and lab != '— / — / current exits' else '', '↑' if o[3][0] >= cur[3][0] else ''))
        best = max(rows, key=lambda x: x[1][4][0])
        L += ['', '**Full stats, after costs** (trades / net / win % / profit factor / max drawdown)', '', '| Period | Current exits | Best combined (%s) |' % best[0], '|---|---|---|']
        for pn, P in PER: L.append('| %s | %s | %s |' % (pn, pstats([t['n'] for t in b if P(t)]), pstats([t['n'] for t in best[2] if P(t)])))
        L.append('')
        summ.append('- %s: current %+.0f after costs → best combined (%s) %+.0f; thirds %s; last 4 wk %+.0f vs %+.0f' % (
            X['nm'], cur[4][0], best[0], best[1][4][0], ' / '.join('%+.0f' % best[1][k][0] for k in range(3)), best[1][3][0], cur[3][0]))
    print('\n'.join(L[:1] + ['', '## Summary', ''] + summ + [''] + L[1:]))

if __name__ == '__main__':
    report() if sys.argv[1] == 'report' else run_sym(sys.argv[1])
