"""MES 3m BOT -- every alert / trigger type and which bot checkboxes should be ticked -- 11/12/2026.

Bot rules (CBC v10.87): MES 3m only; entry windows 18:30-22:00, 03:00-13:00, 15:00-15:30 ET (candle close); no new entries from
15:45; flatten 15:57; no shorts while price is above the 5-day EMA (bot_d5); 100 % closed at TP1 (bracket TP1 / SL1).
A. REPLAY Jan 5 -> now (chop_sim engine, every CBC trigger on, then the bot filters): per trigger type, bot exits
   (SL1 3 ATR, TP1 1.75 ATR, 100 % at TP1, CBC setup end / 16:00), 0.50 pt cost per trade.
B. LIVE since 10/19: real MES 3m Trade Setup alerts, re-run with the BOT exits on the BarFeed candles (TP1 / SL1 from the alert,
   stop first if one candle touches both, else exit at the close of the candle that ended CBC's setup ("Setup Ended" Time) or
   the 15:57 flatten), 0.50 pt cost. Limit-entry fills are assumed. Also the CBC chart result (Setup Ended) for reference.
C. ALL OTHER ALERT TYPES on MES 3m (not tradable by the bot today -- no checkbox): each directional alert scored with the bot's
   bracket (entry = alert candle close, SL 3 ATR / TP 1.75 ATR, else exit on the opposite HTF CBC flip or the 15:57 flatten),
   inside the bot windows + short filter, 0.50 pt cost -- shows whether any could become a bot trigger later.
Duplicates: alerts with the same chart, Time line and alert names within 60 s count once.
Verdict per checkbox: CHECK = replay positive in all three thirds AND live (bot windows, bot exits) >= 15 trades with net > 0;
KEEP OFF = replay negative in 2+ thirds AND live <= 0 (or <5 live trades and replay negative in all thirds); else WATCH.
"""
import re, json, collections, datetime as D, numpy as np, pandas as pd
from zoneinfo import ZoneInfo
import combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg, mes3_ema_grid as m, all_alerts_study as aas

TZ = ZoneInfo('America/New_York'); COST = .5
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase('MES', 3, B); TR, ss = tg.trend_arrays(s); G = cb.CH['MES'][2]
e9 = B.e9.values.astype(float)
et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); cm = ((et.dt.hour * 60 + et.dt.minute).values + 3) % 1440
W = lambda c: ((1110 <= c <= 1320) or (180 <= c <= 780) or (900 <= c <= 930)) and not (945 <= c < 1080)
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
NAME = {'fl': 'HTF CBC Flip', 'ly': 'LTF EMA20 Pierce (closed beyond EMA9)', 'ln': 'LTF EMA20 Pierce (not beyond EMA9)', 'll': 'LTF EMA20 Pierce (late confirm)',
        'h9': 'HTF EMA9 Pierce (incl. late)', 'h20': 'HTF EMA20 Pierce (incl. late)', 'mo': 'Momentum break', 'pb': 'HTF Pullback Structure', 'tc': 'LTF EMA20 Touch (mid-candle)'}
ON = {'fl', 'ly', 'ln'}  # v10.88: + LTF not beyond EMA9
ORDER = ['fl', 'ly', 'ln', 'll', 'h9', 'h20', 'mo', 'pb', 'tc']

# ---------------- A. replay ----------------
def cat(d):
    i = d['i']
    if d['trig'] == 'flip': return 'fl'
    if d['trig'] == 'ltf20':
        if d.get('late'): return 'll'
        return 'ly' if ((s.C[i] > e9[i]) if d['lg'] else (s.C[i] < e9[i])) else 'ln'
    return d['trig']  # h9 / h20 incl. late
CMAP = {d['i']: cat(d) for d in s.cands}
s.TX, s.TY = (0, 0.0); s.ACT = None
rep = []
for t in s.run(lambda d: cs.cur_rule(d), q=dict(m.LIVE, part=1.0), gates=G):
    i = t['i']
    if not W(cm[i]) or (not t['lg'] and TR['d5'][i] == 1): continue
    rep.append(dict(c=CMAP.get(i, '?'), n=t['res'] - COST, th=0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2, l4=bool(s.T[i] >= t4)))

# ---------------- alerts (deduped) ----------------
A = m.get(m.BASE + '/alerts?from=2026-10-19')
A = A if isinstance(A, list) else A.get('alerts', [])
rawt = lambda a: a['raw'] if isinstance(a['raw'], str) else json.dumps(a['raw'])
A.sort(key=lambda a: a['receivedAt'])
def nkey(r):
    ch = re.search(r'Chart: ([^\n]*)', r); tm = re.search(r'Time: ([^\n]*)', r)
    if not ch or not tm: return None
    return (r.split('\n')[0].strip(), ch[1].strip(), tm[1].strip(), '|'.join(sorted(l.strip().split(':')[0] for l in r.split('\n') if l.strip().startswith('•'))))
seen = {}; AD = []; ndup = 0
for a in A:
    r = rawt(a)
    if not r.startswith('MES') or not re.search(r'Chart: \S+\s+3m', r): continue
    k = nkey(r); ms = D.datetime.fromisoformat(a['receivedAt'].replace('Z', '+00:00')).timestamp()
    if k and k in seen and ms - seen[k] <= 60: ndup += 1; continue
    if k: seen[k] = ms
    AD.append((a, r))
tix = {int(t): k for k, t in enumerate(s.T)}
H, L_, C_, hfv = s.B.h.values, s.B.l.values, s.B.c.values, s.B.hf.values
d5 = TR['d5']; atr = s.atr
def ctime(r, rcv):  # candle close datetime from the Time line
    mt = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
    if not mt: return None
    return D.datetime(int(rcv[:4]), int(mt[1]), int(mt[2]), int(mt[3]), int(mt[4]), tzinfo=TZ)
def flat_at(j):  # candle j closes at/after 15:57 and before 18:00
    c = (cm[j]) ; return 957 <= c < 1080

# ---------------- B. live trade setups ----------------
setups, ends = {}, {}
for a, r in AD:
    for sec in ('\n' + r).split('\n• ')[1:]:
        if sec.startswith('Trade Setup:'):
            dr = re.match(r'Trade Setup: (\w+)', sec)[1]; en = re.search(r'\nEntry: ([\d.]+)', sec); tg_ = re.search(r'Trigger: ([^\n]*)', sec)
            tp = re.search(r'\nTP1: ([\d.]+)', sec); sl = re.search(r'\nSL1: ([\d.]+)', sec); ct = ctime(r, a['receivedAt'])
            if en and tg_ and tp and sl and ct:
                k = (dr, en[1], ct.strftime('%H:%M'))
                if k not in setups or setups[k]['ct'] < ct - D.timedelta(hours=20): setups[k] = dict(dr=dr, en=float(en[1]), tp=float(tp[1]), sl=float(sl[1]), trg=tg_[1], ct=ct)
        elif sec.startswith('Setup Ended:'):
            dr = re.match(r'Setup Ended: (\w+)', sec)[1]; se = re.search(r'Setup Entry: ([\d.]+) \| Started: (\d+):(\d+)', sec); rs = re.search(r'Result: ([+-]?[\d.]+)', sec)
            ct = ctime(r, a['receivedAt'])
            if se and rs: ends[(dr, se[1], '%s:%s' % (se[2].zfill(2), se[3]))] = (float(rs[1]), ct)
def lcat(t):
    f = t.split(',')[0].strip()
    if f.startswith('HTF CBC Flip') or f.startswith('HTF('): return 'fl'
    if f.startswith('LTF EMA20 Pierce'):
        if 'late' in f: return 'll'
        return 'ly' if 'closed beyond EMA9: yes' in t else 'ln'
    if f.startswith('HTF EMA9 Pierce'): return 'h9'
    if f.startswith('HTF EMA20 Pierce'): return 'h20'
    if f.startswith('Momentum'): return 'mo'
    if 'Pullback' in f: return 'pb'
    if 'Touch' in f: return 'tc'
    return 'other'
def bot_exit(i, lg, en, tp, sl, end_j):
    g = 1 if lg else -1
    for j in range(i + 1, s.n):
        if (L_[j] <= sl) if lg else (H[j] >= sl): return g * (sl - en), 'SL1'
        if (H[j] >= tp) if lg else (L_[j] <= tp): return g * (tp - en), 'TP1'
        if (end_j is not None and j >= end_j) or flat_at(j): return g * (C_[j] - en), 'end'
    return None, None
live = []
for k, x in setups.items():
    e = ends.get(k)
    if not e: continue
    i = tix.get(int(x['ct'].timestamp() * 1000) - 180000)
    if i is None: continue
    lg = x['dr'] == 'LONG'
    inw = W(cm[i]) and not (not lg and d5[i] == 1)
    end_j = tix.get(int(e[1].timestamp() * 1000) - 180000) if e[1] else None
    br, why = bot_exit(i, lg, x['en'], x['tp'], x['sl'], end_j)
    if br is None: continue
    live.append(dict(c=lcat(x['trg']), w=inw, bot=br - COST, why=why, chart=e[0], t=x['ct']))
live.sort(key=lambda z: z['t']); hl = live[len(live) // 2]['t'] if live else None

# ---------------- C. every other alert type ----------------
SK = re.compile(aas.SKIP.pattern + r'|Trade Setup|Bot Order|Setup Blocked')
evs = {}
for a, r in AD:
    ct = ctime(r, a['receivedAt'])
    if not ct: continue
    i = tix.get(int(ct.timestamp() * 1000) - 180000)
    if i is None: continue
    for ln in r.split('\n'):
        if not ln.startswith('• ') or SK.search(ln): continue
        dd = aas.direction(ln)
        if not dd: continue
        evs[(aas.norm_type(ln), i, dd)] = 1
def bracket(i, d):
    en = C_[i]; A_ = atr[i]; sl, tp = en - d * 3 * A_, en + d * 1.75 * A_
    for j in range(i + 1, s.n):
        if (L_[j] <= sl) if d == 1 else (H[j] >= sl): return -3 * A_
        if (H[j] >= tp) if d == 1 else (L_[j] <= tp): return 1.75 * A_
        if hfv[j] == -d or flat_at(j): return d * (C_[j] - en)
    return None
oth = collections.defaultdict(list)
for (typ, i, d) in evs:
    if not W(cm[i]) or (d == -1 and d5[i] == 1): continue
    v = bracket(i, d)
    if v is not None: oth[{'HTF': 'HTF CBC Flip + LTF Agreement'}.get(typ, typ)].append((s.T[i], v - COST, d))
# baseline: every candle in the bot windows since the first live alert, long and (short filter allowed) short
i0 = min(i for (_, i, _) in evs) if evs else s.n
base = {1: [], -1: []}
for i in range(i0, s.n - 1):
    if not W(cm[i]): continue
    for d in (1, -1):
        if d == -1 and d5[i] == 1: continue
        v = bracket(i, d)
        if v is not None: base[d].append(v - COST)

# ---------------- report ----------------
def st(v):
    x = np.array([t['n'] for t in v]) if v else np.zeros(0)
    return len(v), x.sum(), round(100 * (x > 0).mean()) if len(x) else 0, [sum(t['n'] for t in v if t['th'] == k) for k in range(3)], sum(t['n'] for t in v if t['l4'])
out = ['# MES 3m bot -- every alert type and which checkboxes to tick -- %s' % D.datetime.now(TZ).strftime('%Y-%m-%d %H:%M ET'), '', __doc__.strip(), '',
       'Replay %s -> %s. Live alerts since 10/19 (%d MES 3m duplicates dropped). Live halves split at %s.' % (s.date[300][:5], s.date[-1][:5], ndup, hl.strftime('%m/%d') if hl else '-'), '',
       '## 1. Bot checkboxes (Trade Setup triggers)', '',
       '| Checkbox | Now | Replay trades / net | Replay thirds | Replay last 4 wk | Live in bot windows: n / bot-exit net / win % (halves) | Live CBC result same setups | Live all hours (bot exits) | Verdict |',
       '|---|---|---|---|---|---|---|---|---|']
verd = {}
for c in ORDER:
    rv = [t for t in rep if t['c'] == c]; n, net, w, th, l4 = st(rv)
    lv = [t for t in live if t['c'] == c]; lw = [t for t in lv if t['w']]
    bn = sum(t['bot'] for t in lw); cn = sum(t['chart'] for t in lw); wr = round(100 * np.mean([t['bot'] > 0 for t in lw])) if lw else 0
    h1 = sum(t['bot'] for t in lw if t['t'] < hl); h2 = bn - h1
    if rv:
        neg = sum(x < 0 for x in th)
        if all(x > 0 for x in th) and len(lw) >= 15 and bn > 0: v = 'CHECK'
        elif (neg >= 2 and lw and bn <= 0) or (neg == 3 and len(lw) < 5): v = 'KEEP OFF'
        else: v = 'WATCH'
    else:
        v = 'CHECK' if len(lw) >= 20 and h1 > 0 and h2 > 0 else 'KEEP OFF' if len(lw) >= 10 and bn < 0 else 'WATCH (live only)'
    verd[c] = v
    out.append('| %s | %s | %s | %s | %s | %d / %+.1f / %d %% (%+.1f / %+.1f) | %+.1f | %d / %+.1f | **%s** |' % (
        NAME[c], 'ON' if c in ON else 'off', ('%d / %+.0f' % (n, net)) if rv else 'not in replay', ('%+.0f / %+.0f / %+.0f' % tuple(th)) if rv else '-', ('%+.0f' % l4) if rv else '-',
        len(lw), bn, wr, h1, h2, cn, len(lv), sum(t['bot'] for t in lv), v))
out += ['', '## 2. Every other MES 3m alert type, scored as if the bot traded it (bot windows + short filter, SL 3 / TP 1.75 ATR, after costs)', '',
        'Baseline (no signal: EVERY 3m candle in the bot windows, same bracket): long avg %+.2f (%d), short avg %+.2f (%d) -- an alert type is only useful if it beats these.' % (
            np.mean(base[1]) if base[1] else 0, len(base[1]), np.mean(base[-1]) if base[-1] else 0, len(base[-1])), '',
        '| Alert type | Trades | Win % | Net | Avg | Long n / avg | Short n / avg | 1st half / 2nd half | Note |', '|---|---|---|---|---|---|---|---|---|']
rows = []
for typ, v in oth.items():
    v.sort(); x = np.array([z[1] for z in v]); h = len(v) // 2
    xl = [z[1] for z in v if z[2] == 1]; xs = [z[1] for z in v if z[2] == -1]
    a1, a2 = x[:h].sum(), x[h:].sum()
    note = 'positive in both halves' if (a1 > 0 and a2 > 0 and len(v) >= 20) else ('too few' if len(v) < 20 else '')
    rows.append((x.sum(), '| %s | %d | %d %% | %+.1f | %+.2f | %d / %+.2f | %d / %+.2f | %+.1f / %+.1f | %s |' % (typ, len(v), round(100 * (x > 0).mean()), x.sum(), x.mean(),
        len(xl), np.mean(xl) if xl else 0, len(xs), np.mean(xs) if xs else 0, a1, a2, note)))
out += [r for _, r in sorted(rows, key=lambda z: -z[0])]
ck = [NAME[c] for c in ORDER if verd[c] == 'CHECK']; ko = [NAME[c] for c in ORDER if verd[c] == 'KEEP OFF']; wa = [NAME[c] for c in ORDER if verd[c].startswith('WATCH')]
cand = [r for x, r in sorted(rows, key=lambda z: -z[0]) if 'both halves' in r]
out += ['', '## Summary', '',
        '- Tick: ' + (', '.join(ck) or 'nothing passes the CHECK rule'),
        '- Keep unticked: ' + (', '.join(ko) or '-'),
        '- Watch (not enough evidence either way): ' + (', '.join(wa) or '-'),
        '- Other alert types positive in both halves with 20+ trades (would need a new bot checkbox): ' + (str(len(cand)) if cand else 'none')]
open('bot_alerts_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
