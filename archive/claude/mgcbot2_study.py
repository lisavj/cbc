"""MGC 3m BOT settings for CBC v10.98 (main line) -- triggers, entry windows, 5-day filter, exit style, flatten time -- 11/17/2026.
Chart setups = CBC v10.98 MGC 3m (no slope filter): ER 0.23 + breakout, range gate 24 / 20 % / 5 ATR, VWAP stretch 4 ATR (applied), late-away
1 pt; chart exits FLIP 0 % (decide the one-setup-at-a-time sequence). Engine = claude/noflip_study.py TCase (all_eng gen).
The bot takes a chart setup when its FIRST trigger is ticked, its candle closes inside an entry window and before the no-new-entry time,
and the 5-day filter passes. Bot exits: BRACKET = SL1 / TP1 (the setup's, 100 % at TP1, broker side) or CBC ends the setup (HTF flip
against, next setup) or the flatten time; FLIP = SL1 kept, no TP, same other exits. 1 contract, net after 0.22 pt (1 pt = $10).
Thirds by date; z = Δ / (SD x sqrt(trades changed)) vs the reference row; robust = z >= 2 + all thirds + last 4 wk >= 0."""
import sys, numpy as np, pandas as pd, datetime as D, itertools
import chop_sim as cs, ema716_eng as eng, noflip_study as nf
COST = .22; X = nf.CH['MGC']; B = eng.load('MGC', 3, X['f']); o = dict(X['base'], slope=0)
P = dict(nf.TDEF, fdp=X['fdp'], tw=X['tw'], erl=.08); nf.TCase.P = P; s = nf.TCase('MGC', 3, B); s.P = P
C, H, L, A, T, N = s.C, s.H, s.L, s.atr, s.T, s.n; e9 = B.e9.values.astype(float)
hh24, ll24 = pd.Series(H).rolling(24).max().values, pd.Series(L).rolling(24).min().values
def ok(d):
    i, lg = d['i'], d['lg']; g = 1 if lg else -1; a = A[i]
    if not cs.cur_rule(d): return False
    w = hh24[i] - ll24[i]
    if w > 0 and w / a < 5 and ((C[i] - ll24[i]) / w if lg else (hh24[i] - C[i]) / w) >= .8: return False
    return not (g * (C[i] - s.vw[i]) / a > 4)
R = s.run(ok, dict(X['q'], nf=0), False)
cm = (s.hm) % 1440     # candle CLOSE minute ET (hm = open + tf)
sd_ = B.hk.str[:10].values; dc = pd.DataFrame({'d': sd_, 'c': C}).groupby('d', sort=True).c.last(); E5 = pd.Series(sd_).map(dc.ewm(span=5, adjust=False).mean().shift(1)).values
T0, T1 = T[300], T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
def cat(r):
    i = r['i']
    if r['trig'] == 'flip': return 'fl'
    if r['trig'] == 'ltf20': return 'll' if r.get('late') else ('ly' if ((C[i] > e9[i]) if r['lg'] else (C[i] < e9[i])) else 'ln')
    return r['trig']
NM = {'fl': 'HTF CBC Flip', 'ly': 'LTF EMA20 Pierce (beyond EMA9)', 'ln': 'LTF EMA20 Pierce (not beyond EMA9)', 'll': 'LTF EMA20 Pierce (late)', 'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}
for k, r in enumerate(R): r['c'] = cat(r); r['stop'] = R[k + 1]['i'] if k + 1 < len(R) else -1
def inwin(m, wins):
    if not wins: return True
    for a, b in wins:
        if (a <= m < b) if a <= b else (m >= a or m < b): return True
    return False
def botsim(r, flip, flat):
    i, lg = r['i'], r['lg']; en = C[i]; g = 1 if lg else -1
    sd = max(min(1.7 * A[i], 7), 5); tpd = min(1.7 * A[i], 6); sl = en - g * sd; t1 = en + g * tpd
    for j in range(i + 1, N):
        if (L[j] <= sl) if lg else (H[j] >= sl): return -sd
        if not flip and ((H[j] >= t1) if lg else (L[j] <= t1)): return tpd
        if s.hdir[j] == (0 if lg else 1) or j == r['stop'] or cm[j] == flat: return g * (C[j] - en)
    return 0.
def bot(trig=('fl', 'ly', 'ln'), wins=None, d5=0, fo=None, flat=957, noe=(945, 1080)):
    out = []
    for r in R:
        i = r['i']
        if r['c'] not in trig or not inwin(cm[i], wins): continue
        a, b = noe
        if (a <= cm[i] < b) if a <= b else (cm[i] >= a or cm[i] < b): continue
        if d5 and np.isfinite(E5[i]):
            if not r['lg'] and C[i] > E5[i]: continue
            if d5 == 2 and r['lg'] and C[i] < E5[i]: continue
        flip = fo is not None and inwin(cm[i], fo)
        out.append((i, r['lg'], botsim(r, flip, flat) - COST))
    v = np.array([x[2] for x in out]) if out else np.zeros(1)
    th = [sum(x[2] for x in out if (0 if T[x[0]] < cuts[0] else 1 if T[x[0]] < cuts[1] else 2) == k) for k in range(3)]
    eq = np.cumsum(v)
    return dict(n=len(out), net=v.sum(), avg=v.mean(), sd=v.std() or 1, th=th, l4=sum(x[2] for x in out if T[x[0]] >= t4), w=100 * (v > 0).mean(),
                dd=(np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max(), K={(x[0], x[1]): x[2] for x in out})
def row(nm, a, b=None):
    s_ = '| %s | %d | %.0f %% | %+.0f | %+.2f | %+.0f / %+.0f / %+.0f | %+.0f | %.0f |' % (nm, a['n'], a['w'], a['net'], a['avg'], *a['th'], a['l4'], a['dd'])
    if b is not None:
        ch = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
        z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d_ = [p - q for p, q in zip(a['th'], b['th'])]
        vd = 'robust' if z >= 2 and all(t > 0 for t in d_) and a['l4'] >= b['l4'] else 'promising' if z >= 1 and all(t > 0 for t in d_) else 'worse' if a['net'] < b['net'] else 'noise'
        s_ += ' %+.0f | %+.1f | %s |' % (a['net'] - b['net'], z, vd)
    return s_
HD = '| Variant | Trades | Win % | Net | Avg | Thirds | Last 4 wk | Max DD |'; HD2 = HD + ' Δ vs ref | z | Verdict |'
SEP = '|---|---|---|---|---|---|---|---|'; SEP2 = SEP + '---|---|---|'
MESW = [(1110, 1320), (180, 780), (900, 930)]
ASIA, LON, NY = (1080, 180), (180, 570), (570, 945)
out = [__doc__, '', 'Chart: %d setups %s -> %s' % (len(R), D.datetime.utcfromtimestamp(T[300] / 1000).strftime('%m/%d'), D.datetime.utcfromtimestamp(T[-1] / 1000).strftime('%m/%d')), '']
# 1. triggers alone, all hours
out += ['## 1. Each trigger alone (all hours, bracket, no 5-day filter)', '', HD, SEP]
for k in NM: out.append(row(NM[k], bot(trig=(k,))))
# 2. trigger sets
sets = [('MES bot default: Flip + LTF beyond + LTF not beyond', ('fl', 'ly', 'ln')), ('Flip only', ('fl',)), ('Flip + HTF EMA20', ('fl', 'h20')), ('Flip + LTF beyond', ('fl', 'ly')),
        ('Flip + LTF beyond + HTF EMA20', ('fl', 'ly', 'h20')), ('HTF EMA20 only', ('h20',)), ('All six', tuple(NM))]
ref = bot(trig=('fl', 'ly', 'ln'), wins=MESW, d5=1)
out += ['', '## 2. Trigger sets (all hours, bracket)', '', HD, SEP] + [row(n, bot(trig=t)) for n, t in sets]
# 3. sessions per trigger set
out += ['', '## 3. By session (candle close ET; bracket; no 5-day filter)', '', '| Trigger set | Asia 18:00-03:00 | London 03:00-09:30 | NY 09:30-15:45 |', '|---|---|---|---|']
for n, t in sets:
    cells = []
    for w in (ASIA, LON, NY):
        a = bot(trig=t, wins=[w]); cells.append('%d / %+.0f (%+.0f / %+.0f / %+.0f)' % (a['n'], a['net'], *a['th']))
    out.append('| %s | %s |' % (n, ' | '.join(cells)))
# 4. full candidate grid vs the MES configuration on MGC
WS = [('MES windows 1830-2200, 0300-1300, 1500-1530', MESW), ('all hours', None), ('Asia + London 1800-0930', [(1080, 570)]), ('London + NY 0300-1545', [(180, 945)]),
      ('NY only 0930-1545', [NY]), ('London only', [LON]), ('Asia only', [ASIA])]
grid = []
for (tn, t), (wn, w), d5, fon in itertools.product(sets, WS, (0, 1, 2), ('none', 'NY', 'all')):
    fo = None if fon == 'none' else ([(570, 960)] if fon == 'NY' else [(0, 1440)])
    a = bot(trig=t, wins=w, d5=d5, fo=fo); a['nm'] = '%s; %s; 5-day %s; flip-only %s' % (tn, wn, ['off', 'no shorts above', 'both sides'][d5], fon); grid.append(a)
def score(a):
    return (all(x > 0 for x in a['th']) and a['l4'] >= 0, a['net'] / max(a['dd'], 1))
grid.sort(key=score, reverse=True)
out += ['', '## 4. MES bot configuration on MGC (reference) and the best combinations', '', 'Reference = the MES bot settings unchanged (Flip + LTF beyond + not beyond, MES windows, no shorts above 5-day EMA, flip-only 09:30-16:00):', '',
        HD2, SEP2, row('Reference: MES settings on MGC', bot(trig=('fl', 'ly', 'ln'), wins=MESW, d5=1, fo=[(570, 960)]), ref)]
ref = bot(trig=('fl', 'ly', 'ln'), wins=MESW, d5=1, fo=[(570, 960)])
out += ['', 'Top 15 of %d combinations (all thirds positive and last 4 wk >= 0 first, then net / max DD):' % len(grid), '', HD2, SEP2] + [row(a['nm'], a, ref) for a in grid[:15]]
# 5. flatten time
best = grid[0]; out += ['', '## 5. Flatten / no-new-entry time for the top combination', '', HD, SEP]
bt = [x for x in sets if x[0] == best['nm'].split(';')[0]][0][1]; bw = [x for x in WS if x[0] == best['nm'].split('; ')[1]][0][1]
bd = ['off', 'no shorts above', 'both sides'].index(best['nm'].split('5-day ')[1].split(';')[0]); bf = best['nm'].split('flip-only ')[1]; bfo = None if bf == 'none' else ([(570, 960)] if bf == 'NY' else [(0, 1440)])
for fl_, ne in ((957, (945, 1080)), (1017, (1005, 1080)), (-1, (1440, 1440))):
    out.append(row('flatten %s, no new %s' % ('15:57' if fl_ == 957 else '16:57' if fl_ == 1017 else 'never', '15:45-18:00' if fl_ == 957 else '16:45-18:00' if fl_ == 1017 else '-'), bot(trig=bt, wins=bw, d5=bd, fo=bfo, flat=fl_, noe=ne)))
open('mgcbot2_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
