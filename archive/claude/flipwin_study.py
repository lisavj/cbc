"""MES 3m HTF CBC Flip setups: TP1 exit vs flip + SL exit, by bot time window -- weekly (Tuesdays).
Baseline = current MES 3m filters (ER 0.23 + breakout 3, range gate 24 / 20 % / 5 ATR) + HTF EMA20 slope < 0.3 ATR block (CBC EMA Slope v1.00
default). Replay Jan 5 -> now, CBC engine setups, live exits (SL1 3 ATR min 5, TP1 1.75 ATR, 100 % at TP1), cost 0.50.
Flip + SL = the CBC EMA Slope "HTF CBC Flip setups: no TP1" exit and the bot's "Flip-only windows" exit: SL1 kept, no TP, closed by the
HTF CBC flip against / 16:00 / next setup. Same flip setups rescored (stop at the next setup). Windows by candle close (ET):
03:00-09:30 and 18:30-22:00 = bot windows not in the flip-only window; 09:30-16:00 = current bot flip-only window; other = hours the bot skips.
Also the total (all setups) with flip + SL on every flip setup, z vs TP1 exit (z = Δ / (SD x sqrt(trades changed)))."""
import sys, numpy as np, pandas as pd, collections
import combo_study as cb, chop_sim as cs, late_study as ls
from zoneinfo import ZoneInfo
COST = .5; Q = dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7)
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase('MES', 3, B)
C, H, L, A = s.C, s.H, s.L, s.atr; S = pd.Series; N = s.n
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
hh24, ll24 = S(H).rolling(24).max().values, S(L).rolling(24).min().values
h20 = B.h20.values.astype(float); SLP = np.abs(h20 - np.roll(h20, 12)) / A
et = pd.to_datetime(s.T, unit='ms', utc=True).tz_convert(ZoneInfo('America/New_York')); mins = et.hour.values * 60 + et.minute.values
def ok(d):
    i, lg = d['i'], d['lg']; a = A[i]
    if not cs.cur_rule(d): return False
    w = hh24[i] - ll24[i]
    if w > 0 and w / a < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
    return SLP[i] >= .3
def flipsim(i, lg, stop):
    en = C[i]; g = 1 if lg else -1; sd = max(3.0 * A[i], 5); slv = en - g * sd
    for j in range(i + 1, N):
        if (L[j] <= slv) if lg else (H[j] >= slv): return -sd
        if s.hdir[j] == (0 if lg else 1) or s.hm[j] == 960 or j == stop: return g * (C[j] - en)
    return None
def win(i):
    x = (mins[i] + 3) % 1440
    for a, b, nm in ((570, 960, '09:30-16:00 (bot flip-only window now)'), (180, 570, '03:00-09:30 (bot window, TP1 bracket now)'), (1110, 1320, '18:30-22:00 (bot window, TP1 bracket now)')):
        if a <= x < b: return nm
    return 'other hours (bot does not trade)'
R = s.run(ok, q=Q, gates=dict(R5=0, X4=0, MTF=0))
th = lambda i: 0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2
g = collections.defaultdict(lambda: dict(n=0, a=0., b=0., th=[0., 0., 0.], l4=0., d=[]))
tot_a = []; tot_b = []; ch = 0; tht = [0., 0., 0.]; l4t = 0.
for k, r in enumerate(R):
    a = r['res'] - COST; b = a
    if r['trig'] == 'flip':
        x = flipsim(r['i'], r['lg'], R[k + 1]['i'] if k + 1 < len(R) else -1)
        if x is not None:
            b = x - COST; G = g[win(r['i'])]; G['n'] += 1; G['a'] += a; G['b'] += b; G['th'][th(r['i'])] += b - a; G['d'].append(b - a)
            if s.T[r['i']] >= t4: G['l4'] += b - a
    tot_a.append(a); tot_b.append(b); ch += abs(b - a) > 1e-9; tht[th(r['i'])] += b - a
    if s.T[r['i']] >= t4: l4t += b - a
tot_a = np.array(tot_a); tot_b = np.array(tot_b); z = (tot_b.sum() - tot_a.sum()) / (tot_a.std() * np.sqrt(max(ch, 1)))
out = [__doc__, '', 'Replay %s -> %s; %d setups (%d flip setups)' % (et[300].strftime('%m/%d'), et[-1].strftime('%m/%d'), len(R), sum(G['n'] for G in g.values())), '',
       '| Window (candle close, ET) | Flip setups | TP1 exit | Flip + SL | Δ | Δ by third | Δ last 4 wk | z |', '|---|---|---|---|---|---|---|---|']
for nm in ('03:00-09:30 (bot window, TP1 bracket now)', '09:30-16:00 (bot flip-only window now)', '18:30-22:00 (bot window, TP1 bracket now)', 'other hours (bot does not trade)'):
    G = g[nm]; d = np.array(G['d']) if G['d'] else np.array([0.])
    zz = d.sum() / (tot_a.std() * np.sqrt(max(len(G['d']), 1)))
    out.append('| %s | %d | %+.0f | %+.0f | %+.0f | %+.0f / %+.0f / %+.0f | %+.0f | %+.1f |' % (nm, G['n'], G['a'], G['b'], G['b'] - G['a'], *G['th'], G['l4'], zz))
out += ['', 'TOTAL (all setups, flip + SL on every flip setup): TP1 exit %+.0f -> %+.0f, Δ %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f' % (tot_a.sum(), tot_b.sum(), tot_b.sum() - tot_a.sum(), z, *tht, l4t)]
open('flipwin_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
