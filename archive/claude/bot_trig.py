"""MES 3m BOT trigger checkboxes -- which setup types should the bot take? -- 11/08/2026.
REPLAY: all CBC setups (every trigger on, as CBC draws them), then the bot takes only setups whose trigger is ticked, inside the v10.87
windows (candle close 18:30-22:00, 03:00-13:00, 15:00-15:30 ET) with the 5-day short filter; bot exits = 100 % at TP1 1.75 ATR, SL1 3 ATR,
CBC setup end / 16:00. Net after costs (0.50 per trade). LIVE: real MES 3m Trade Setup -> Setup Ended pairs since 10/19 (CBC chart exits,
not bot exits), same windows + short filter."""
import re, json, itertools, numpy as np, pandas as pd, combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg, mes3_ema_grid as m
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase('MES', 3, B); TR, ss = tg.trend_arrays(s); G = cb.CH['MES'][2]
e9 = B.e9.values.astype(float)
et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); cm = ((et.dt.hour * 60 + et.dt.minute).values + 3) % 1440
W = lambda c: (1110 <= c <= 1320) or (180 <= c <= 780) or (900 <= c <= 930)
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
def cat(d):
    i = d['i']; late = bool(d.get('late'))
    if d['trig'] == 'flip': return 'fl'
    if d['trig'] == 'ltf20':
        if late: return 'll'
        return 'ly' if ((s.C[i] > e9[i]) if d['lg'] else (s.C[i] < e9[i])) else 'ln'
    return d['trig'] + ('L' if late else '')
CMAP = {}
for d in s.cands: CMAP[d['i']] = cat(d)
s.TX, s.TY = (0, 0.0); s.ACT = None
r = s.run(lambda d: cs.cur_rule(d), q=dict(m.LIVE, part=1.0), gates=G)
tr = []
for t in r:
    i = t['i']
    if not W(cm[i]): continue
    if not t['lg'] and TR['d5'][i] == 1: continue
    tr.append(dict(c=CMAP.get(i, '?'), n=t['res'] - .5, th=0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2, l4=bool(s.T[i] >= t4)))
NAME = {'fl': 'HTF CBC Flip', 'ly': 'LTF EMA20 Pierce (closed beyond EMA9)', 'ln': 'LTF EMA20 Pierce (not beyond EMA9)', 'll': 'LTF EMA20 Pierce (late confirm)',
        'h9': 'HTF EMA9 Pierce', 'h9L': 'HTF EMA9 Pierce (late)', 'h20': 'HTF EMA20 Pierce', 'h20L': 'HTF EMA20 Pierce (late)'}
BOX = {'fl': ['fl'], 'ly': ['ly'], 'ln': ['ln'], 'll': ['ll'], 'h9': ['h9', 'h9L'], 'h20': ['h20', 'h20L']}
BN = {'fl': 'Trigger: HTF CBC Flip', 'ly': 'Trigger: LTF EMA20 Pierce (closed beyond EMA9)', 'ln': 'Trigger: LTF EMA20 Pierce (not beyond EMA9)', 'll': 'Trigger: LTF EMA20 Pierce (late confirm)',
      'h9': 'Trigger: HTF EMA9 Pierce (incl. late)', 'h20': 'Trigger: HTF EMA20 Pierce (incl. late)'}
ON = {'fl', 'ly', 'ln'}  # v10.88: + LTF not beyond EMA9
def st(v):
    x = np.array([t['n'] for t in v]) if v else np.zeros(0)
    return len(v), x.sum(), round(100 * (x > 0).mean()) if len(x) else 0, x.mean() if len(x) else 0, [sum(t['n'] for t in v if t['th'] == k) for k in range(3)], sum(t['n'] for t in v if t['l4'])
# live
A = m.get(m.BASE + '/alerts?from=2026-10-19'); setups = {}; ends = {}
for a in A:
    raw = a['raw'] if isinstance(a['raw'], str) else json.dumps(a['raw'])
    if not raw.startswith('MES') or not re.search(r'Chart: \S+\s+3m', raw): continue
    for sec in ('\n' + raw).split('\n• ')[1:]:
        mt = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', sec)
        if sec.startswith('Trade Setup:') and mt:
            dr = re.match(r'Trade Setup: (\w+)', sec).group(1); en = re.search(r'\nEntry: ([\d.]+)', sec); tg_ = re.search(r'Trigger: ([^\n]*)', sec)
            if en and tg_: setups[(dr, en.group(1), '%s:%s' % (mt.group(3).zfill(2), mt.group(4)))] = (a['receivedAt'], tg_.group(1), int(mt.group(3)) * 60 + int(mt.group(4)))
        if sec.startswith('Setup Ended:'):
            dr = re.match(r'Setup Ended: (\w+)', sec).group(1); se = re.search(r'Setup Entry: ([\d.]+) \| Started: (\d+):(\d+)', sec); rs = re.search(r'Result: ([+-]?[\d.]+)', sec)
            if se and rs: ends[(dr, se.group(1), '%s:%s' % (se.group(2).zfill(2), se.group(3)))] = float(rs.group(1))
def lcat(t):
    f = t.split(',')[0].strip()
    if f.startswith('HTF CBC Flip') or f.startswith('HTF(') : return 'fl'
    if f.startswith('LTF EMA20 Pierce'):
        if 'late' in f: return 'll'
        return 'ly' if 'closed beyond EMA9: yes' in t else 'ln'
    if f.startswith('HTF EMA9 Pierce'): return 'h9L' if 'late' in f else 'h9'
    if f.startswith('HTF EMA20 Pierce'): return 'h20L' if 'late' in f else 'h20'
    if f.startswith('Momentum'): return 'mo'
    if 'Pullback' in f: return 'pb'
    if 'Touch' in f: return 'tc'
    return 'other'
ts_ = pd.to_datetime(s.B.t, unit='ms', utc=True)
live = []
for k, (rcv, trg, mnt) in setups.items():
    if k not in ends: continue
    cmn = (mnt + 3) % 1440; inw = W(cmn)
    ix = ts_.searchsorted(pd.Timestamp(rcv)) - 1; d5 = TR['d5'][ix] if 0 <= ix < s.n else 0
    sf = not (k[0] == 'SHORT' and d5 == 1)
    live.append(dict(c=lcat(trg), n=ends[k], w=inw and sf, t=rcv))
live.sort(key=lambda t: t['t']); half = live[len(live) // 2]['t'] if live else ''
L = [__doc__, '', '## 1. Every trigger type (replay Jan 5 -> Nov 6 + live since 10/19)', '',
     '| Trigger (bot checkbox) | Bot now | Replay trades | Replay net | Win % | Avg | Thirds | Last 4 wk | Live (bot windows) n / net / avg | Live all hours n / net |', '|---|---|---|---|---|---|---|---|---|---|']
for c in ['fl', 'ly', 'ln', 'll', 'h9', 'h9L', 'h20', 'h20L']:
    n, net, w, avg, th, l4 = st([t for t in tr if t['c'] == c])
    lv = [t for t in live if t['c'] == c]; lw = [t for t in lv if t['w']]
    on = 'ON' if any(c in BOX[b] and b in ON for b in BOX) else 'off'
    L.append('| %s | %s | %d | %+.0f | %d %% | %+.2f | %+.0f / %+.0f / %+.0f | %+.0f | %d / %+.1f / %+.2f | %d / %+.1f |' % (NAME[c], on, n, net, w, avg, *th, l4, len(lw), sum(t['n'] for t in lw), (sum(t['n'] for t in lw) / len(lw)) if lw else 0, len(lv), sum(t['n'] for t in lv)))
for c in ('mo', 'pb', 'tc', 'other'):
    lv = [t for t in live if t['c'] == c]; lw = [t for t in lv if t['w']]
    if lv: L.append('| %s | off | (not in replay) | | | | | | %d / %+.1f / %+.2f | %d / %+.1f |' % ({'mo': 'Momentum break', 'pb': 'HTF Pullback Structure', 'tc': 'LTF EMA20 Touch', 'other': 'other'}[c], len(lw), sum(t['n'] for t in lw), (sum(t['n'] for t in lw) / len(lw)) if lw else 0, len(lv), sum(t['n'] for t in lv)))
# combos
def combo(boxes):
    cs_ = set(sum((BOX[b] for b in boxes), [])); return [t for t in tr if t['c'] in cs_]
base = st(combo(ON))
L += ['', '## 2. Turning one checkbox on / off (replay, bot exits, after costs; Δ vs the current bot set Flip + LTF beyond + not beyond EMA9 (v10.88) = %+.0f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f)' % (base[1], *base[4], base[5]), '',
      '| Change | Trades | Net | Δ | Δ by third | Δ last 4 wk | Better in all thirds |', '|---|---|---|---|---|---|---|']
for b in ['fl', 'ly', 'ln', 'll', 'h9', 'h20']:
    S = (ON - {b}) if b in ON else (ON | {b}); x = st(combo(S)); d = [x[4][k] - base[4][k] for k in range(3)]
    L.append('| %s %s | %d | %+.0f | %+.0f | %+.0f / %+.0f / %+.0f | %+.0f | %s |' % ('turn OFF' if b in ON else 'turn ON', BN[b], x[0], x[1], x[1] - base[1], *d, x[5] - base[5], 'yes' if all(v > 0 for v in d) else ''))
allc = []
for k in range(1, 7):
    for S in itertools.combinations(['fl', 'ly', 'ln', 'll', 'h9', 'h20'], k):
        x = st(combo(set(S))); allc.append((S, x))
allc.sort(key=lambda z: -z[1][1])
L += ['', '## 3. Best checkbox combinations (replay, all 63)', '', '| Checkboxes ON | Trades | Net | Thirds | Last 4 wk | All thirds positive |', '|---|---|---|---|---|---|']
for S, x in allc[:8]: L.append('| %s | %d | %+.0f | %+.0f / %+.0f / %+.0f | %+.0f | %s |' % (' + '.join(BN[b].replace('Trigger: ', '') for b in S), x[0], x[1], *x[4], x[5], 'yes' if all(v > 0 for v in x[4]) else ''))
pk = max(allc, key=lambda z: z[1][4][0] + z[1][4][1]); r3 = sorted(z[1][4][2] for z in allc)
L += ['', 'Current (Flip + LTF beyond EMA9 + LTF not beyond EMA9, v10.88) ranks %d of 63 by net. Walk-forward: best on thirds 1-2 = %s -> third 3 %+.0f (rank %d of 63; current %+.0f).' % (
    1 + [z[0] for z in allc].index(tuple(sorted(ON, key=['fl', 'ly', 'ln', 'll', 'h9', 'h20'].index))), ' + '.join(BN[b].replace('Trigger: ', '') for b in pk[0]), pk[1][4][2], sum(1 for v in r3 if v > pk[1][4][2]) + 1, base[4][2])]
open('bot_trig_report.md', 'w').write('\n'.join(L)); print('\n'.join(L))
