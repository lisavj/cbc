"""(flip_exit_bot.py = bot windows 09:30-13:00 + 15:00-15:30 + 5-day short filter)  MES 3m, 09:30-16:00 ET: does exiting on the HTF (15m) CBC flip beat the other exits? -- every alert type -- 11/12/2026.
Entry = close of the alert / setup candle, candle closing 09:30-15:45 ET (no filters: every alert of the type, both directions).
Exit variants (all flat at the 15:57 candle close at the latest; 0.50 pt cost per trade; ATR = 14 on 3m):
  BRACKET      SL 3 ATR / TP 1.75 ATR only (the bot bracket, no flip exit)
  BRACKET+FLIP SL 3 ATR / TP 1.75 ATR, or exit at the close of the candle where the HTF CBC flips against the trade (current bot)
  FLIP+SL      no target: SL 3 ATR, else exit on the HTF CBC flip against
  FLIP ONLY    no target, no stop: exit on the HTF CBC flip against (or 15:57)
LIVE = alert store since 10/19 (duplicates removed). REPLAY = Trade Setups from the chop_sim replay Jan 5 -> now, by trigger."""
import re, json, collections, datetime as D, numpy as np, pandas as pd
from zoneinfo import ZoneInfo
import trend_guard_study as tg, combo_study as cb, chop_sim as cs, late_study as ls, mes3_ema_grid as m, all_alerts_study as aas
TZ = ZoneInfo('America/New_York')
B = ls.load('MES', 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase('MES', 3, B); G = cb.CH['MES'][2]
TR, _ = tg.trend_arrays(s)
C, H, L, hf, atr = s.C, s.H, s.L, s.B.hf.values, s.atr
e9 = B.e9.values.astype(float)
et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); cm = ((et.dt.hour * 60 + et.dt.minute).values + 3) % 1440
INW = lambda c: (570 < c <= 780) or (900 <= c <= 930)
V = ['BRACKET', 'BRACKET+FLIP', 'FLIP+SL', 'FLIP ONLY']
def ex(i, d):
    en, A = C[i], atr[i]; sl, tp = en - d * 3 * A, en + d * 1.75 * A; out = {}
    for v in V:
        r = None
        for j in range(i + 1, s.n):
            if v != 'FLIP ONLY' and ((L[j] <= sl) if d == 1 else (H[j] >= sl)): r = -3 * A; break
            if v in ('BRACKET', 'BRACKET+FLIP') and ((H[j] >= tp) if d == 1 else (L[j] <= tp)): r = 1.75 * A; break
            if (v != 'BRACKET' and hf[j] == -d) or cm[j] == 957 or cm[j] < 570: r = d * (C[j] - en); break
        out[v] = None if r is None else r - .5
    return out
tix = {int(t): k for k, t in enumerate(s.T)}
# ---- live alerts
A = m.get(m.BASE + '/alerts?from=2026-10-19'); A = A if isinstance(A, list) else A.get('alerts', [])
A.sort(key=lambda a: a['receivedAt']); seen = {}; ev = {}
for a in A:
    r = a['raw'] if isinstance(a['raw'], str) else json.dumps(a['raw'])
    if not r.startswith('MES') or not re.search(r'Chart: \S+\s+3m', r): continue
    mt = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
    if not mt: continue
    ct = D.datetime(int(a['receivedAt'][:4]), int(mt[1]), int(mt[2]), int(mt[3]), int(mt[4]), tzinfo=TZ)
    i = tix.get(int(ct.timestamp() * 1000) - 180000)
    if i is None or not INW(cm[i]): continue
    for sec in ('\n' + r).split('\n• ')[1:]:
        head = sec.split('\n')[0]
        if head.startswith('Trade Setup:'):
            tg_ = re.search(r'Trigger: ([^\n]*)', sec); f = tg_[1].split(',')[0].strip() if tg_ else ''
            nm = 'SETUP: ' + ('HTF CBC Flip' if f.startswith('HTF CBC Flip') else 'LTF Pierce late' if ('LTF EMA20 Pierce' in f and 'late' in f) else 'LTF Pierce beyond EMA9' if 'closed beyond EMA9: yes' in (tg_[1] if tg_ else '') else 'LTF Pierce not beyond EMA9' if f.startswith('LTF EMA20 Pierce') else re.sub(r'\s*\(.*', '', f))
            d = 1 if 'LONG' in head else -1
        else:
            if aas.SKIP.search('• ' + head) or 'Bot Order' in head or 'Setup Blocked' in head: continue
            d = aas.direction('• ' + head)
            if not d: continue
            nm = aas.norm_type('• ' + head); nm = {'HTF': 'HTF CBC Flip + LTF Agreement'}.get(nm, nm)
        if d == -1 and TR['d5'][i] == 1: continue
        ev[(nm, i, d)] = 1
live = collections.defaultdict(list)
for (nm, i, d) in ev:
    o = ex(i, d)
    if all(o[v] is not None for v in V): live[nm].append((s.T[i], o))
# ---- replay trade setups
s.TX, s.TY = (0, 0.0); s.ACT = None
def cat(d):
    i = d['i']
    if d['trig'] == 'flip': return 'HTF CBC Flip'
    if d['trig'] == 'ltf20':
        if d.get('late'): return 'LTF Pierce late'
        return 'LTF Pierce beyond EMA9' if ((C[i] > e9[i]) if d['lg'] else (C[i] < e9[i])) else 'LTF Pierce not beyond EMA9'
    return {'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}.get(d['trig'], d['trig'])
CM = {d['i']: cat(d) for d in s.cands}
rep = collections.defaultdict(list)
T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
for t in s.run(lambda d: cs.cur_rule(d), q=dict(m.LIVE, part=1.0), gates=G):
    i = t['i']
    if not INW(cm[i]) or (not t['lg'] and TR['d5'][i] == 1): continue
    o = ex(i, 1 if t['lg'] else -1)
    if all(o[v] is not None for v in V): rep[CM.get(i, '?')].append((s.T[i], o))
def th_(t): return 0 if t < cuts[0] else 1 if t < cuts[1] else 2
def line(nm, v, thirds):
    v.sort(key=lambda z: z[0]); n = len(v)
    tot = {k: sum(z[1][k] for z in v) for k in V}
    best = max(V, key=lambda k: tot[k])
    dd = lambda z: z[1]['FLIP ONLY'] - z[1]['BRACKET+FLIP']
    if thirds:
        tail = ' / '.join('%+.0f' % sum(dd(z) for z in v if th_(z[0]) == x) for x in range(3))
    else:
        h = n // 2; tail = '%+.1f / %+.1f' % (sum(dd(z) for z in v[:h]), sum(dd(z) for z in v[h:]))
    w = 100 * np.mean([z[1]['FLIP ONLY'] > 0 for z in v]) if v else 0
    return '| %s | %d | %s | %+.1f | %s | %.0f %% | **%s** |' % (nm, n, ' | '.join('%+.1f' % tot[k] for k in V), sum(dd(z) for z in v), tail, w, best)
out = ['# MES 3m BOT WINDOWS ONLY (entries 09:30-13:00 + 15:00-15:30 ET, 5-day short filter) -- HTF CBC flip exit vs bracket, every alert type -- %s' % D.datetime.now(TZ).strftime('%Y-%m-%d %H:%M ET'), '', __doc__, '',
       '## Live alerts since 10/19 (net pts after costs)', '', '| Alert type | Trades | Bracket (TP/SL only) | Bracket + flip (now) | Flip + SL | FLIP ONLY | Flip only vs now | ...by half | Flip-only win % | Best |', '|---|---|---|---|---|---|---|---|---|---|']
lv = sorted(live.items(), key=lambda kv: -len(kv[1]))
out += [line(nm, v, False) for nm, v in lv if len(v) >= 10]
allv = [z for v in live.values() for z in v]
out += [line('ALL live alerts (types with 10+)', [z for nm, v in live.items() if len(v) >= 10 for z in v], False)]
out += ['', '## Replay Trade Setups Jan 5 -> now, by trigger (thirds Jan-Mar / Apr-Jul / Aug-Nov approx.)', '',
        '| Trigger | Trades | Bracket (TP/SL only) | Bracket + flip (now) | Flip + SL | FLIP ONLY | Flip only vs now | ...by third | Flip-only win % | Best |', '|---|---|---|---|---|---|---|---|---|---|']
out += [line(nm, v, True) for nm, v in sorted(rep.items(), key=lambda kv: -len(kv[1]))]
out += [line('ALL replay setups', [z for v in rep.values() for z in v], True)]
open('flip_exit_bot_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
