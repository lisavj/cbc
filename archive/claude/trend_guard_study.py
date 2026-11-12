#!/usr/bin/env python3
"""Trend filter + session guard study -- 3m charts MES, MGC, MNQ, M2K -- 11/08/2026.
Why: the MES 3m month split (11/08) showed the losing months were June (volatile, no direction, 37 % win) and August (quiet drift up,
shorts -159), with many more setups closed by an HTF flip against them (85-95 a month vs 61-71 in good months). Chop measures
(ER, flips per day) were the same in all thirds. Two kinds of fix are tested here:
 A. TREND FILTER (entry gate, re-simulated: a skipped setup does not end the open trade) -- skip setups against:
    mtf = the 60m CBC direction; e200-20 / e200-60 = the chart EMA200 slope over 20 / 60 candles (1 h / 3 h);
    vwap = session VWAP (long only above, short only below); pdc = the previous session close; d5 = a 5-day EMA of session closes
    (up to the previous session). Applied to both directions, or to shorts only ("S").
 B. SESSION GUARD (bot rule; session = 18:00-18:00 ET): stop taking setups for the rest of the session after K losing trades in a
    row (after costs) or after N trades closed by an HTF flip against them. Only trades that have already ENDED count.
Costs (as exit_lab): commission + 1 tick per trade, +1 tick for a rule exit; MES 0.50 / MGC 0.22 / MNQ 0.87 / M2K 0.35 pts per trade.
"Beyond random" = Δ after costs minus what dropping the same number of trades at random would give (current exits lose
money after costs, so ANY skipping looks good). Walk-forward = best rule picked on thirds 1-2 (beyond-random, after costs),
scored on third 3. Replay = chop_sim rules, live exits (MES 3m SL1 3 ATR / TP1 1.75 ATR / by time of day, MGC 3m MGCX,
MNQ / M2K CBC defaults), Jan 5 -> now. T = better in all three thirds, 4 = better in the last 4 weeks.
Usage: python3 trend_guard_study.py MES|MGC|MNQ|M2K ; python3 trend_guard_study.py report"""
import sys, os, pickle, numpy as np, pandas as pd, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

GD = dict(R5=0, X4=0, MTF=0)
CH = {'MES': ('MES 3m', m.LIVE, dict(R5=1, X4=0, MTF=0), .50),
      'MGC': ('MGC 3m', ls.MGCX, dict(R5=1, X4=1, MTF=0), .22),
      'MNQ': ('MNQ 3m', dict(sl=1.7, mn=25, cap=30, tp=1.7, tcap=40, part=.8, be=True, tr=1.7), GD, .87),
      'M2K': ('M2K 3m', dict(sl=1.7, mn=3, cap=5, tp=1.7, tcap=3, part=.8, be=True, tr=1.7), GD, .35)}
TRENDS = ['mtf', 'e200-20', 'e200-60', 'vwap', 'pdc', 'd5']
TN = {'mtf': '60m CBC', 'e200-20': 'EMA200 slope 1 h', 'e200-60': 'EMA200 slope 3 h', 'vwap': 'VWAP', 'pdc': 'prev session close', 'd5': '5-day EMA'}
GUARDS = [(K, N) for K in (0, 2, 3, 4) for N in (0, 2, 3, 4)]
def tfn(f): return 'no trend filter' if f is None else 'skip against %s%s' % (TN[f[0]], ' (shorts only)' if f[1] == 'S' else '')
def gn(g): return 'no guard' if g == (0, 0) else ' or '.join(x for x in ('%d losses in a row' % g[0] if g[0] else '', '%d flip-outs' % g[1] if g[1] else '') if x)

def trend_arrays(s):
    C = s.C; n = s.n; e2 = s.B.e200.values.astype(float)
    T = {}
    T['mtf'] = np.where(s.mtf < 0, 0, np.where(s.mtf == 1, 1, -1))
    for k in (20, 60):
        d = e2 - np.r_[np.full(k, np.nan), e2[:-k]]; T['e200-%d' % k] = np.nan_to_num(np.sign(d))
    T['vwap'] = np.nan_to_num(np.sign(C - s.vw))
    ss = s.B.hk.str[:10].values; df = pd.DataFrame({'s': ss, 'c': C}); last = df.groupby('s', sort=False).c.last()
    prev = last.shift(1); e5 = last.ewm(span=5, adjust=False).mean().shift(1)
    T['pdc'] = np.nan_to_num(np.sign(C - prev.reindex(ss).values)); T['d5'] = np.nan_to_num(np.sign(C - e5.reindex(ss).values))
    return T, ss

def run_sym(sym):
    nm, q, G, cost = CH[sym]; tick = {'MES': .25, 'MGC': .1, 'MNQ': .25, 'M2K': .1}[sym]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
    s = ls.LCase(sym, 3, B); TR, ss = trend_arrays(s)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    mo = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York').dt.strftime('%m').values
    runs = {}
    for f in [None] + [(t, w) for t in TRENDS for w in ('B', 'S')]:
        def ok(d, f=f):
            if not cs.cur_rule(d): return False
            if f is None: return True
            if f[1] == 'S' and d['lg']: return True
            v = TR[f[0]][d['i']]; return v == 0 or v == (1 if d['lg'] else -1)
        r = s.run(ok, q=q, gates=G)
        runs[f] = [dict(i=t['i'], j=t['j'], lg=t['lg'], why=t['why'], n=t['res'] - cost, th=0 if s.T[t['i']] < cuts[0] else 1 if s.T[t['i']] < cuts[1] else 2,
                        l4=bool(s.T[t['i']] >= t4), ss=ss[t['i']], mo=mo[t['i']]) for t in r]
    pickle.dump(dict(nm=nm, cost=cost, runs=runs, last=D.datetime.utcfromtimestamp(T1 / 1000).strftime('%m/%d')), open('tg_%s.pkl' % sym, 'wb'))
    print(sym, 'done', flush=True)

def guard(r, K, N):
    if not K and not N: return r
    keep = []; stt = {}
    done = []  # trades taken, with end index
    for t in sorted(r, key=lambda t: t['i']):
        S = stt.setdefault(t['ss'], dict(stop=False))
        if S['stop']: continue
        # update session state from taken trades in this session that ended before this entry
        fin = [u for u in keep if u['ss'] == t['ss'] and u['j'] < t['i']]
        ls_ = 0
        for u in sorted(fin, key=lambda u: u['j']):
            ls_ = ls_ + 1 if u['n'] < 0 else 0
        fo = sum(1 for u in fin if u['why'] == 'flip' and u['n'] < 0)
        if (K and ls_ >= K) or (N and fo >= N): S['stop'] = True; continue
        keep.append(t)
    return keep

def stats(r, b):
    ab = np.mean([t['n'] for t in b])
    d = sum(t['n'] for t in r) - sum(t['n'] for t in b)
    th = [sum(t['n'] for t in r if t['th'] == k) - sum(t['n'] for t in b if t['th'] == k) for k in range(3)]
    thx = [th[k] + (sum(1 for t in b if t['th'] == k) - sum(1 for t in r if t['th'] == k)) * ab for k in range(3)]
    d4 = sum(t['n'] for t in r if t['l4']) - sum(t['n'] for t in b if t['l4'])
    ex = d + (len(b) - len(r)) * ab
    return dict(d=d, ex=ex, th=th, thx=thx, d4=d4, n=len(r), net=sum(t['n'] for t in r))

def report():
    out = ['# Trend filter + session guard study — 3m charts — %s' % D.datetime.now().strftime('%m/%d/%Y %H:%M'), '', __doc__.strip().split('Usage:')[0].strip(), '']
    summ = []
    for sym in ('MES', 'MGC', 'MNQ', 'M2K'):
        if not os.path.exists('tg_%s.pkl' % sym): continue
        X = pickle.load(open('tg_%s.pkl' % sym, 'rb')); R = X['runs']; b = R[None]
        S = {}
        for f in R:
            for g in GUARDS:
                if f is None and g == (0, 0): continue
                S[(f, g)] = stats(guard(R[f], *g), b)
        bn = sum(t['n'] for t in b)
        def fl(k):
            c = S[k]; return ''.join(a for a, v in (('T', all(x > 0 for x in c['th'])), ('Tx', all(x > 0 for x in c['thx'])), ('4', c['d4'] > 0)) if v)
        def line(k):
            c = S[k]; return '%s + %s: Δ **%+.0f** after costs, beyond random **%+.0f**, %d trades (%+d) %s(thirds %+.0f / %+.0f / %+.0f; beyond random %+.0f / %+.0f / %+.0f; last 4 wk %+.1f)' % (
                tfn(k[0]), gn(k[1]), c['d'], c['ex'], c['n'], c['n'] - len(b), fl(k) + ' ' if fl(k) else '', *c['th'], *c['thx'], c['d4'])
        out += ['## %s — current: %d trades to %s, net %+.0f after costs (%.2f pts per trade)' % (X['nm'], len(b), X['last'], bn, X['cost']), '']
        # A: trend filters alone
        out += ['**A. Trend filters alone** (no guard)', '', '| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |', '|---|---|---|---|---|---|']
        for f in [k for k in R if k is not None]:
            c = S[(f, (0, 0))]
            out.append('| %s | %d | %+.0f | **%+.0f** %s | %+.0f / %+.0f / %+.0f | %+.1f |' % (tfn(f), c['n'], c['d'], c['ex'], 'T' if all(x > 0 for x in c['thx']) else '', *c['thx'], c['d4']))
        # B: guards alone
        out += ['', '**B. Session guards alone** (no trend filter)', '', '| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |', '|---|---|---|---|---|---|']
        for g in GUARDS[1:]:
            c = S[(None, g)]
            out.append('| %s | %d | %+.0f | **%+.0f** %s | %+.0f / %+.0f / %+.0f | %+.1f |' % (gn(g), c['n'], c['d'], c['ex'], 'T' if all(x > 0 for x in c['thx']) else '', *c['thx'], c['d4']))
        # top combos
        top = sorted(S, key=lambda k: -S[k]['ex'])[:8]
        out += ['', '**Top 8 (filter + guard) by beyond-random gain**', ''] + ['%d. %s' % (n + 1, line(k)) for n, k in enumerate(top)]
        # walk-forward
        pick = max(S, key=lambda k: S[k]['thx'][0] + S[k]['thx'][1]); l3 = sorted(S[k]['thx'][2] for k in S)
        pickd = max(S, key=lambda k: S[k]['th'][0] + S[k]['th'][1]); l3d = sorted(S[k]['th'][2] for k in S)
        wf = S[pick]['thx'][2]; wfd = S[pickd]['th'][2]
        out += ['', '**Walk-forward** (pick on thirds 1-2, score on third 3)', '',
                '- by beyond-random: **%s + %s** (%+.0f in-sample) → third 3 beyond random **%+.0f** (rank %d of %d, median %+.0f)' % (
                    tfn(pick[0]), gn(pick[1]), S[pick]['thx'][0] + S[pick]['thx'][1], wf, sum(1 for v in l3 if v > wf) + 1, len(l3), l3[len(l3) // 2]),
                '- by plain Δ after costs: **%s + %s** (%+.0f in-sample) → third 3 Δ **%+.0f** (rank %d of %d, median %+.0f)' % (
                    tfn(pickd[0]), gn(pickd[1]), S[pickd]['th'][0] + S[pickd]['th'][1], wfd, sum(1 for v in l3d if v > wfd) + 1, len(l3d), l3d[len(l3d) // 2])]
        # months for current + top 3
        mos = sorted({t['mo'] for t in b})
        out += ['', '**By month, net after costs** (current exits vs top 3 rules)', '', '| Rule | ' + ' | '.join(mos) + ' |', '|---|' + '---|' * len(mos)]
        out.append('| current | ' + ' | '.join('%+.0f' % sum(t['n'] for t in b if t['mo'] == M) for M in mos) + ' |')
        for k in top[:3]:
            r = guard(R[k[0]], *k[1]); out.append('| %s + %s | ' % (tfn(k[0]), gn(k[1])) + ' | '.join('%+.0f' % sum(t['n'] for t in r if t['mo'] == M) for M in mos) + ' |')
        out.append('')
        summ.append('- %s: best %s + %s → beyond random %+.0f (Δ %+.0f, %s); walk-forward third 3 beyond random %+.0f' % (
            X['nm'], tfn(top[0][0]), gn(top[0][1]), S[top[0]]['ex'], S[top[0]]['d'], fl(top[0]) or 'no flags', wf))
    print('\n'.join(out[:1] + ['', '## Summary', ''] + summ + [''] + out[1:]))

if __name__ == '__main__':
    report() if sys.argv[1] == 'report' else run_sym(sys.argv[1])
