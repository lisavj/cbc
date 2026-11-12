#!/usr/bin/env python3
"""Live alerts since 10/19 for the daily MES watch (project claude/mes3_watch_live.py).
11/09: MES 3m periods split 10/19-11/04 / 11/05 / 11/06-11/07 / from 11/08 (TP1 1.75, v10.82+);
(E) Exit Rule hits vs Setup Ended; (F) late trigger x room (Room line) 2x2 tables.
11/12: DATA_NOTES dedupe (same chart + Time line + set of bullet names within 60 s = one alert, keep longest);
two Setup Ended results for one setup -> prefer the one with a 0.5x(TP1) breakdown (MGC 3m old-exit duplicate alert);
Exit Rule hits de-duplicated per setup; MGC 3m period split at 11/08."""
import json, re, sys, pickle, datetime as D
from zoneinfo import ZoneInfo
TZ = ZoneInfo('America/New_York')
YR = 2026
A0 = json.load(open(sys.argv[1]))
# ---- dedupe near copies (DATA_NOTES 1)
A0 = [a for a in A0 if isinstance(a.get('raw'), str)]
A0.sort(key=lambda a: a.get('receivedAt', ''))
kept = {}; A = []; ndup = 0
for a in A0:
    r = a['raw']
    ch = re.search(r'\nChart: ([^\n]*)', r); tl = re.search(r'\nTime: ([^\n]*)', r)
    key = (ch.group(1) if ch else r[:12], tl.group(1) if tl else '', tuple(sorted(re.findall(r'• ([^:\n]+):', r))))
    ts = D.datetime.fromisoformat(a['receivedAt'].replace('Z', '+00:00')).timestamp()
    if key in kept and ts - kept[key][0] <= 60:
        ndup += 1
        if len(r) > len(A[kept[key][1]]['raw']): A[kept[key][1]] = a
        continue
    kept[key] = (ts, len(A)); A.append(a)
TRIGS = ['HTF CBC Flip', 'LTF Pierce beyond EMA9', 'LTF Pierce not beyond', 'LTF Pierce LATE', 'HTF EMA9 Pierce',
         'HTF EMA9 late', 'HTF EMA20 Pierce', 'HTF EMA20 late', 'Momentum break', 'HTF Pullback', 'LTF EMA20 Touch', 'other']
LATE_T = ('LTF Pierce LATE', 'HTF EMA9 late', 'HTF EMA20 late')
ROOM_RE = re.compile(r'\nRoom: (.+?) ([\d.]+(?:-[\d.]+)?) at \+?([-\d.]+) pts = ([\d.]+) x TP1')
def trig(line):
    f = line.strip()
    if f.startswith('HTF CBC Flip'): return 'HTF CBC Flip'
    if f.startswith('LTF EMA20 Pierce (late'): return 'LTF Pierce LATE'
    if f.startswith('LTF EMA20 Pierce (closed beyond EMA9: yes'): return 'LTF Pierce beyond EMA9'
    if f.startswith('LTF EMA20 Pierce'): return 'LTF Pierce not beyond'
    if f.startswith('HTF EMA9 Pierce (late'): return 'HTF EMA9 late'
    if f.startswith('HTF EMA9 Pierce'): return 'HTF EMA9 Pierce'
    if f.startswith('HTF EMA20 Pierce (late'): return 'HTF EMA20 late'
    if f.startswith('HTF EMA20 Pierce'): return 'HTF EMA20 Pierce'
    if f.lower().startswith('momentum'): return 'Momentum break'
    if f.startswith('HTF Pullback'): return 'HTF Pullback'
    if f.startswith('LTF EMA20 Touch'): return 'LTF EMA20 Touch'
    return 'other'
S, E = {}, {}; EXR = []; ndual = 0
for a in A:
    r = a.get('raw')
    if not isinstance(r, str) or r[:3] not in ('MES', 'MGC', 'MNQ'): continue
    m = re.search(r'\nChart: \S+\s+(\d+)m', r)
    if not m: continue
    tf = int(m.group(1)); sym = r[:3]
    tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
    if not tm: continue
    mo, dd, hh, mi = map(int, tm.groups())
    t = D.datetime(YR, mo, dd, hh, mi, tzinfo=TZ)
    if 'Exit Rule:' in r:
        EXR.append((sym, tf, t, r)); continue
    if '• Trade Setup:' in r:
        dr = re.search(r'Trade Setup: (\w+)', r).group(1)
        en = float(re.search(r'\nEntry: ([\d.]+)', r).group(1))
        tl = re.search(r'\nTrigger: ([^\n]*)', r)
        sl = re.search(r'\nSL1: ([\d.]+)', r)
        tp = re.search(r'\nTP1: ([\d.]+)', r)
        rm = ROOM_RE.search(r)
        vx = re.search(r'VWAP ext ([+-]?[\d.]+) ATR', r)
        tg = trig(tl.group(1)) if tl else 'other'
        S[(sym, tf, dr, en, hh, mi, mo, dd)] = dict(sym=sym, tf=tf, dr=dr, en=en, t=t, trig=tg,
            sl1=float(sl.group(1)) if sl else None, tp1=float(tp.group(1)) if tp else None, raw_trig=tl.group(1) if tl else '',
            late=tg in LATE_T, room=float(rm.group(4)) if rm else None, room_txt=('%s %s at %s pts' % (rm.group(1), rm.group(2), rm.group(3))) if rm else '',
            vwx=float(vx.group(1)) if vx else None)
    elif '• Setup Ended:' in r:
        dr = re.search(r'Setup Ended: (\w+)', r).group(1)
        st = re.search(r'Started: (\d+):(\d+)', r); res = re.search(r'Result: ([+-]?[\d.]+)', r)
        se = re.search(r'Setup Entry: ([\d.]+)', r)
        if not (st and res and se): continue
        sh, sm = int(st.group(1)), int(st.group(2))
        day = t.date() - (D.timedelta(days=1) if (sh, sm) > (hh, mi) else D.timedelta(0))
        if day.weekday() == 5: day -= D.timedelta(days=1)
        k = (sym, tf, dr, float(se.group(1)), sh, sm, day.month, day.day)
        new = dict(res=float(res.group(1)), te=t, half='0.5×' in r)
        if k in E:
            ndual += 1
            old = E[k]
            if old['half'] and not new['half']: continue
            if not old['half'] and not new['half'] and old['te'] <= t: continue   # keep the first if neither shows 0.5x
        E[k] = new
setups = []
for k, s in S.items():
    s = dict(s); e = E.get(k)
    s['ended'] = e is not None; s['res'] = e['res'] if e else None; s['te'] = e['te'] if e else None
    setups.append(s)
setups.sort(key=lambda x: x['t'])
unmatched_E = sum(1 for k in E if k not in S)
NOW = D.datetime.now(TZ)
five = [s for s in setups if s['sym'] == 'MES' and s['tf'] == 5]
def confirmed(s):
    for f in five:
        if f['dr'] != s['dr']: continue
        end = f['te'] or NOW
        if f['t'] <= s['t'] <= end: return True
        if abs((f['t'] - s['t']).total_seconds()) <= 600: return True
    return False
for s in setups:
    if s['sym'] == 'MES' and s['tf'] in (2, 3): s['conf'] = confirmed(s)
def stats(L):
    v = [x['res'] for x in L if x['ended']]
    n = len(v); w = sum(x > 0 for x in v); l = sum(x < 0 for x in v); h = n // 2
    return dict(setups=len(L), ended=n, win=round(100 * w / max(1, w + l)), net=sum(v), avg=sum(v) / n if n else 0, h1=sum(v[:h]), h2=sum(v[h:]))
def row(name, L):
    st = stats(L)
    return '| %s | %d | %d | %d%% | %+.1f | %+.2f | %+.1f / %+.1f |' % (name, st['setups'], st['ended'], st['win'], st['net'], st['avg'], st['h1'], st['h2']), st
HDR = ['| %s | Setups | Ended | Win %% | Net | Avg | Halves |', '|---|---|---|---|---|---|---|']
out = []; J = {}
last = max(s['t'] for s in setups)
out += ['### Live per chart (10/19 → %s)' % last.strftime('%m/%d %H:%M'), '', HDR[0] % 'Chart', HDR[1]]
for sym in ('MES', 'MGC', 'MNQ'):
    for tf in (2, 3, 5):
        L = [s for s in setups if s['sym'] == sym and s['tf'] == tf]
        r, st = row('%s %dm' % (sym, tf), L); out.append(r); J['%s%d' % (sym, tf)] = st
m3 = [s for s in setups if s['sym'] == 'MES' and s['tf'] == 3]
d1105, d1108 = D.date(2026, 11, 5), D.date(2026, 11, 8)
for nm, f in (('MES 3m 10/19–11/04 (9 / 20)', lambda s: s['t'].date() < d1105), ('MES 3m 11/05 (7 / 14 build)', lambda s: s['t'].date() == d1105),
              ('MES 3m 11/06–11/07 (9 / 20, TP1 2.0)', lambda s: d1105 < s['t'].date() < d1108),
              ('MES 3m from 11/08 (TP1 1.75, v10.82+)', lambda s: s['t'].date() >= d1108)):
    r, st = row(nm, [s for s in m3 if f(s)]); out.append(r); J[nm] = st
g3 = [s for s in setups if s['sym'] == 'MGC' and s['tf'] == 3]
for nm, f in (('MGC 3m before 11/08', lambda s: s['t'].date() < d1108), ('MGC 3m from 11/08 (50 % + trail 3.5; partly old exits to 11/12)', lambda s: s['t'].date() >= d1108)):
    r, st = row(nm, [s for s in g3 if f(s)]); out.append(r); J[nm] = st
out += ['', 'Matched: %d Trade Setup alerts, %d ended; %d Setup Ended alerts without a matching Trade Setup (not counted). Near-duplicate alerts dropped: %d; setups with two Setup Ended results: %d (0.5×(TP1) version kept).' % (
    len(setups), sum(s['ended'] for s in setups), unmatched_E, ndup, ndual), '']
J['trig'] = {}
for sym, tf in (('MES', 2), ('MES', 3), ('MES', 5)):
    L = [s for s in setups if s['sym'] == sym and s['tf'] == tf]
    out += ['### (D) Live per trigger — %s %dm (first listed trigger)' % (sym, tf), '', HDR[0] % 'Trigger', HDR[1]]
    for t in TRIGS:
        LL = [s for s in L if s['trig'] == t]
        if not LL: continue
        r, st = row(t, LL); out.append(r); J['trig']['%s%d %s' % (sym, tf, t)] = st
    if tf == 3:
        bot = [s for s in L if s['trig'] in ('HTF CBC Flip', 'LTF Pierce beyond EMA9')]
        r, st = row('**Bot set (Flip + LTF Pierce beyond EMA9)**', bot); out.append(r); J['bot'] = st
        r, st = row('Everything else', [s for s in L if s['trig'] not in ('HTF CBC Flip', 'LTF Pierce beyond EMA9')]); out.append(r); J['nonbot'] = st
    out.append('')
out += ['### (D) Live per trigger — MGC / MNQ, ended setups / net pts', '',
        '| Trigger | MGC 2m | MGC 3m | MGC 5m | MNQ 2m | MNQ 3m | MNQ 5m |', '|---|---|---|---|---|---|---|']
for t in TRIGS:
    cells = []; anyx = False
    for sym in ('MGC', 'MNQ'):
        for tf in (2, 3, 5):
            LL = [s for s in setups if s['sym'] == sym and s['tf'] == tf and s['trig'] == t and s['ended']]
            anyx |= bool(LL)
            cells.append('%d / %+.1f' % (len(LL), sum(s['res'] for s in LL)) if LL else '—')
            J['trig']['%s%d %s' % (sym, tf, t)] = stats([s for s in setups if s['sym'] == sym and s['tf'] == tf and s['trig'] == t])
    if anyx: out.append('| %s | %s |' % (t, ' | '.join(cells)))
out += ['']
J['conf'] = {}
out += ['### (C) Live MES 5m confirmation', '', '| Chart / window | Group | Setups | Ended | Win % | Net | Avg | Halves |', '|---|---|---|---|---|---|---|---|']
for tf in (2, 3):
    for wn, d0 in (('since 10/19', D.date(2026, 10, 19)), ('since 11/06', D.date(2026, 11, 6))):
        L = [s for s in setups if s['sym'] == 'MES' and s['tf'] == tf and s['t'].date() >= d0]
        for g, f in (('confirmed', True), ('unconfirmed', False)):
            st = stats([s for s in L if s['conf'] == f]); J['conf']['%d %s %s' % (tf, wn, g)] = st
            out.append('| MES %dm %s | %s | %d | %d | %d%% | %+.1f | %+.2f | %+.1f / %+.1f |' % (tf, wn, g, st['setups'], st['ended'], st['win'], st['net'], st['avg'], st['h1'], st['h2']))
out.append('')
for tf in (2, 3):
    L = [s for s in setups if s['sym'] == 'MES' and s['tf'] == tf and s['ended']]
    mid = L[len(L) // 2]['t']; r = {}
    for g in (True, False):
        for hn, f in (('h1', lambda s: s['t'] < mid), ('h2', lambda s: s['t'] >= mid)):
            v = [s['res'] for s in L if s['conf'] == g and f(s)]
            r['%s %s' % ('conf' if g else 'unconf', hn)] = (len(v), sum(v), sum(v) / max(1, len(v)))
    J['conf']['%d common halves' % tf] = r
    out.append('MES %dm common date halves (split %s): ' % (tf, mid.strftime('%m/%d %H:%M')) + ' · '.join('%s %d / %+.1f (avg %+.2f)' % (k, *v) for k, v in r.items()))
out.append('')

# ---------------- (E) Exit Rule alerts
out += ['### (E) Exit Rule alerts (v10.79+)', '']
kinds = {}
for sym, tf, t, r in EXR:
    k = 'hit' if ' hit ' in r else 'armed' if 'armed' in r else 'other'
    kinds[(sym, tf, k)] = kinds.get((sym, tf, k), 0) + 1
out.append('Exit Rule alerts found (after dedupe): %d (%s); first %s.' % (len(EXR), ', '.join('%s %dm %s %d' % (a, b, c, n) for (a, b, c), n in sorted(kinds.items())) or 'none',
           min(x[2] for x in EXR).strftime('%m/%d %H:%M') if EXR else '—'))
hits = []; hseen = set()
for sym, tf, t, r in EXR:
    m = re.search(r'Exit Rule: (TP cut|Profit lock) hit \((LONG|SHORT)\) \| Result: ([+-]?[\d.]+)', r)
    if not m: continue
    se = re.search(r'Setup Entry: ([\d.]+) \| Started: (\d+):(\d+)', r)
    en, sh, sm = float(se.group(1)), int(se.group(2)), int(se.group(3))
    hk_ = (sym, tf, m.group(1), m.group(2), en, sh, sm)
    if hk_ in hseen: continue
    hseen.add(hk_)
    cand = [s for s in setups if s['sym'] == sym and s['tf'] == tf and s['dr'] == m.group(2) and s['en'] == en and s['t'].hour == sh and s['t'].minute == sm and s['t'] <= t]
    s = max(cand, key=lambda x: x['t']) if cand else None
    if s is None:   # no Trade Setup alert stored: match the Setup Ended alert directly (same chart / dir / entry / start)
        day = t.date() - (D.timedelta(days=1) if (sh, sm) > (t.hour, t.minute) else D.timedelta(0))
        e = E.get((sym, tf, m.group(2), en, sh, sm, day.month, day.day))
        if e: s = dict(ended=True, res=e['res'], t=t, noTS=True)
    hits.append(dict(sym=sym, tf=tf, t=t, rule=m.group(1), dr=m.group(2), rres=float(m.group(3)), s=s))
out += ['', '| Chart | Rule | Time | Dir | Rule result | CBC result (Setup Ended) | Rule − CBC |', '|---|---|---|---|---|---|---|']
for h in sorted(hits, key=lambda x: x['t']):
    cr = h['s']['res'] if h['s'] and h['s']['ended'] else None
    out.append('| %s %dm | %s | %s | %s | %+.2f | %s | %s |' % (h['sym'], h['tf'], h['rule'], h['t'].strftime('%m/%d %H:%M'), h['dr'], h['rres'],
               '%+.2f' % cr if cr is not None else ('open' if h['s'] else 'no matching setup'), '%+.2f' % (h['rres'] - cr) if cr is not None else '—'))
J['exr'] = dict(n=len(EXR), hits=[])
out += ['', '| Chart (period) | Hits with ended setup | Sum rule | Sum CBC | Rule − CBC | Halves (rule − CBC) |', '|---|---|---|---|---|---|']
for nm, f in (('MES 3m', lambda h: h['sym'] == 'MES' and h['tf'] == 3), ('MGC 3m before 11/08', lambda h: h['sym'] == 'MGC' and h['tf'] == 3 and h['t'].date() < d1108),
              ('MGC 3m from 11/08 (50 % + trail 3.5)', lambda h: h['sym'] == 'MGC' and h['tf'] == 3 and h['t'].date() >= d1108)):
    H = [h for h in sorted(hits, key=lambda x: x['t']) if f(h) and h['s'] and h['s']['ended']]
    d = [h['rres'] - h['s']['res'] for h in H]; hh = len(d) // 2
    out.append('| %s | %d | %+.2f | %+.2f | %+.2f | %+.2f / %+.2f |' % (nm, len(H), sum(h['rres'] for h in H), sum(h['s']['res'] for h in H), sum(d), sum(d[:hh]), sum(d[hh:])))
    J['exr']['hits'].append(dict(chart=nm, n=len(H), rule=sum(h['rres'] for h in H), cbc=sum(h['s']['res'] for h in H), d=sum(d), h1=sum(d[:hh]), h2=sum(d[hh:])))
out.append('')

# ---------------- (F) late trigger x room
def inwin(t):
    cm = t.hour * 60 + t.minute
    return 1110 <= cm <= 1320 or 180 <= cm <= 780 or 900 <= cm <= 930
J['F'] = {}
out += ['### (F) Late trigger × room (first trigger late; room = x TP1 from the "Room:" line)', '']
charts = [('MES 2m', lambda s: s['sym'] == 'MES' and s['tf'] == 2), ('MES 3m', lambda s: s['sym'] == 'MES' and s['tf'] == 3),
          ('MES 5m', lambda s: s['sym'] == 'MES' and s['tf'] == 5), ('MES 3m bot windows', lambda s: s['sym'] == 'MES' and s['tf'] == 3 and inwin(s['t']))]
for nm, f in charts:
    L = [s for s in setups if f(s)]
    Le = [s for s in L if s['ended'] and s['room'] is not None]
    mid = Le[len(Le) // 2]['t'] if Le else None
    noroom = [s for s in L if s['room'] is None]
    out += ['#### %s — %d setups (%d ended), %d without a Room line (kept out of the room cells); halves = date split of the Room-line setups at %s' % (
        nm, len(L), sum(x['ended'] for x in L), len(noroom), mid.strftime('%m/%d %H:%M') if mid else '—'), '',
        '| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |', '|---|---|---|---|---|---|---|']
    def cell(LL):
        st = stats(LL); v1 = sum(s['res'] for s in LL if s['ended'] and s['t'] < mid); v2 = sum(s['res'] for s in LL if s['ended'] and s['t'] >= mid)
        st['h1'], st['h2'] = v1, v2; return st
    R = [s for s in L if s['room'] is not None]
    J['F'][nm] = {}
    for cn, cf in (('late & room < 0.5', lambda s: s['late'] and s['room'] < .5), ('late & room ≥ 0.5', lambda s: s['late'] and s['room'] >= .5),
                   ('not late & room < 0.5', lambda s: not s['late'] and s['room'] < .5), ('not late & room ≥ 0.5', lambda s: not s['late'] and s['room'] >= .5),
                   ('late & room < 0.3', lambda s: s['late'] and s['room'] < .3), ('late & room < 0.75', lambda s: s['late'] and s['room'] < .75),
                   ('(no Room line) late', lambda s: s['late']), ('(no Room line) not late', lambda s: not s['late'])):
        LL = [s for s in (noroom if cn.startswith('(no') else R) if cf(s)]
        st = cell(LL); J['F'][nm][cn] = st
        out.append('| %s | %d | %d | %d%% | %+.1f | %+.2f | %+.1f / %+.1f |' % (cn, st['setups'], st['ended'], st['win'], st['net'], st['avg'], st['h1'], st['h2']))
    c = J['F'][nm]['late & room < 0.5']
    out += ['', 'Combo skip effect (minus the late & room < 0.5 net): %+.1f pts on %d ended setups%s.' % (-c['net'], c['ended'], ' — too few yet' if c['ended'] < 10 else ''), '']
sday = lambda t: (t + D.timedelta(hours=6)).date()   # Globex session date (18:00 ET start)
days = sorted({sday(s['t']) for s in setups if s['sym'] == 'MES' and sday(s['t']).weekday() < 5})[-5:]
out += ['#### Late & room < 0.5 setups, last 5 trading days (%s)' % ', '.join(d.strftime('%m/%d') for d in days), '',
        '| Chart | Time | Dir | First trigger | Room | Room x TP1 | VWAP ext | Result |', '|---|---|---|---|---|---|---|---|']
cnt = 0
for s in setups:
    if s['sym'] == 'MES' and s['late'] and s['room'] is not None and s['room'] < .5 and sday(s['t']) in days:
        cnt += 1
        out.append('| MES %dm | %s | %s | %s | %s | %.2f | %s | %s |' % (s['tf'], s['t'].strftime('%m/%d %H:%M'), s['dr'], s['raw_trig'].split('),')[0] + (')' if '),' in s['raw_trig'] else ''),
                   s['room_txt'], s['room'], '%+.1f ATR' % s['vwx'] if s['vwx'] is not None else '—', '%+.2f' % s['res'] if s['ended'] else 'open'))
if not cnt: out.append('| — | none | | | | | | |')
fr = [s for s in setups if s['sym'] == 'MES' and s['room'] is not None]
out += ['', 'First MES setup with a Room line: %s.' % (min(s['t'] for s in fr).strftime('%m/%d %H:%M') if fr else 'none'), '']
print('\n'.join(out))
json.dump(J, open('live_summary.json', 'w'), indent=1, default=str)
pickle.dump(m3, open('mes3_setups.pkl', 'wb'))
pickle.dump([s for s in setups if s['sym'] == 'MES'], open('mes_setups.pkl', 'wb'))
