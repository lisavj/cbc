#!/usr/bin/env python3
"""MES 3m bot set by 30-min entry slot (ET) -- 11/05/2026. Bot set = HTF CBC Flip + LTF EMA20 Pierce on-candle closed beyond
EMA9. Replay Jan 5 -> now (chop_sim rules, live gates, late window 1 but late setups excluded), bot exits: SL1 3 x ATR min 5,
TP1 2 x ATR, 100 % at TP1, CBC flip / 16:00 / new setup exits; entries 15:45+ not taken, 15:57 flatten."""
import numpy as np, pandas as pd, datetime as D, collections
import chop_sim as cs, late_study as ls, mes3_ema_grid as m
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
s = ls.LCase('MES', 3, B)
e9 = m.ema(s.C, 9)
G = dict(R5=1, X4=0, MTF=0)
q = dict(m.LIVE, tp=2.0, part=1.0)
res = s.run(lambda d: cs.cur_rule(d), q=q, gates=G)   # full engine (other setups still end / block like live)
def bot(r):
    if r['trig'] == 'flip': return True
    if r['trig'] == 'ltf20' and not r.get('late'):
        return (s.C[r['i']] > e9[r['i']]) if r['lg'] else (s.C[r['i']] < e9[r['i']])
    return False
R = [r for r in res if bot(r)]
cm = lambda r: (s.hm[r['i']]) % 1440   # candle close minute ET
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
th = lambda r: 0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2
S = collections.defaultdict(list)
for r in R:
    mm = cm(r)
    if 945 <= mm < 1080: continue  # no entries 15:45-18:00
    S[(mm // 30) * 30].append(r)
order = sorted(S, key=lambda k: (k - 1080) % 1440)
print('Replay: bot set %d setups, net %+.0f (all setups %d, net %+.0f)' % (len(R), sum(r['res'] for r in R), len(res), sum(r['res'] for r in res)))
print('| Slot (ET, entry candle close) | Setups | Win %% | Net | Avg | Thirds net | + thirds |')
print('|---|---|---|---|---|---|---|')
for k in order:
    L = S[k]; v = [r['res'] for r in L]; t = [sum(r['res'] for r in L if th(r) == j) for j in range(3)]
    print('| %02d:%02d-%02d:%02d | %d | %d%% | %+.1f | %+.2f | %+.0f / %+.0f / %+.0f | %d/3 |' % (k // 60, k % 60, (k + 30) // 60 % 24, (k + 30) % 60, len(v),
          round(100 * sum(x > 0 for x in v) / max(1, sum(x != 0 for x in v))), sum(v), sum(v) / len(v), *t, sum(x > 0 for x in t)))
import pickle; pickle.dump([(cm(r), r['res'], th(r), r['trig']) for r in R], open('slot_rows.pkl', 'wb'))
