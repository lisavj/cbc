#!/usr/bin/env python3
"""(B) TP1 1.5 / 1.75 / 2.0 x ATR on the real MES 3m setups since 10/19 (exit model of mes_sltp_grid.py + live time-of-day close).
11/09: current = 1.75 (v10.82+); deltas vs 1.75."""
import json, pickle, re, datetime as D
from zoneinfo import ZoneInfo
TZ = ZoneInfo('America/New_York')
raw = json.load(open('dl/bars60.json'))['bars']
seen = {}
for b in raw:
    seen[b['t']] = b
B = [seen[t] for t in sorted(seen)]
ix = {b['t']: i for i, b in enumerate(B)}
atr, a = [], None
for i, x in enumerate(B):
    tr = max(x['h'], B[i - 1]['c']) - min(x['l'], B[i - 1]['c']) if i else x['h'] - x['l']
    a = tr if a is None else (a * 13 + tr) / 14
    atr.append(a)
S = [s for s in pickle.load(open('mes3_setups.pkl', 'rb')) if s['ended']]
T = []; miss = 0
for s in S:
    i = ix.get(int(s['t'].timestamp() * 1000) - 180000)
    if i is None or i < 20 or s['sl1'] is None: miss += 1; continue
    T.append(dict(s, i=i, lg=s['dr'] == 'LONG'))
T.sort(key=lambda x: x['t'])


def inside(t):  # candle open time ET
    m = (t - D.timedelta(minutes=3)); mm = m.hour * 60 + m.minute
    return 360 <= mm < 960 or 1080 <= mm < 1350


def sim(tr, tpd):
    i, lg, en = tr['i'], tr['lg'], tr['en']; s = 1 if lg else -1
    sd = abs(en - tr['sl1']); sl = en - s * sd; tp1 = en + s * tpd
    part = .8 if inside(tr['t']) else 1.0; hit = False
    fin = lambda px: part * tpd + (1 - part) * (px - en) * s if hit else (px - en) * s
    for j in range(i + 1, min(len(B), i + 500)):
        x = B[j]
        if (x['l'] <= sl) if lg else (x['h'] >= sl): return fin(sl)
        if not hit and ((x['h'] >= tp1) if lg else (x['l'] <= tp1)):
            hit = True
            if part >= 1: return tpd
            sl = max(sl, en) if lg else min(sl, en)
        if hit:
            ns = x['c'] - s * 1.7 * atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
        hc, hp = x['hc'], B[j - 1]['hc']
        if hc is not None and hp is not None and hc != hp and ((lg and hc == 0) or (not lg and hc == 1)): return fin(x['c'])
        t = D.datetime.fromtimestamp(x['t'] / 1000, TZ)
        if t.hour == 15 and t.minute >= 57: return fin(x['c'])
    return 0.0


n = len(T); h = n // 2; t3 = n // 3
TH = lambda R: [sum(R[k * t3:(k + 1) * t3 if k < 2 else n]) for k in range(3)]
J = {}
L = ['### (B) TP1 on the real MES 3m setups (10/19 → %s, %d ended setups with bars + SL1; %d skipped: no bar / no SL1)' % (T[-1]['t'].strftime('%m/%d'), n, miss), '',
     '| TP1 | Net | Win % | Avg | Halves | Thirds |', '|---|---|---|---|---|---|']
for m in (1.5, 1.75, 2.0):
    R = [sim(t, m * atr[t['i']]) for t in T]
    w = sum(r > 0 for r in R); l = sum(r < 0 for r in R)
    J[m] = dict(net=sum(R), win=round(100 * w / max(1, w + l)), avg=sum(R) / n, h=[sum(R[:h]), sum(R[h:])], th=TH(R), R=R)
    L.append('| %.2f ATR%s | %+.1f | %d%% | %+.2f | %+.1f / %+.1f | %+.1f / %+.1f / %+.1f |' % (m, ' (live)' if m == 1.75 else '', sum(R), J[m]['win'], sum(R) / n, *J[m]['h'], *J[m]['th']))
D_ = {}
for nm, a_, b_ in (('1.5 − 1.75', 1.5, 1.75), ('2.0 − 1.75', 2.0, 1.75)):
    d = [x - y for x, y in zip(J[a_]['R'], J[b_]['R'])]; D_[nm] = [sum(d), sum(d[:h]), sum(d[h:])] + TH(d)
    L.append('| Δ %s | %+.1f | | | %+.1f / %+.1f | %+.1f / %+.1f / %+.1f |' % (nm, *D_[nm]))
own = [sim(t, abs(t['tp1'] - t['en'])) if t.get('tp1') else r for t, r in zip(T, J[1.75]['R'])]; act = [t['res'] for t in T]
agree = sum((o > 0) == (a > 0) for o, a in zip(own, act))
L += ['', 'Validation (own SL1 + own TP1 from the Trade Setup alert): replay %+.1f vs actual %+.1f; win/loss agreement %d / %d (%d%%).' % (
    sum(own), sum(act), agree, n, round(100 * agree / n)),
      'Note: live MES 3m TP1 was 1.75 (v10.54–10.66), 2.0 (v10.67–10.81) and 1.75 again from v10.82 (11/08), so actual results mix both targets.', '']
print('\n'.join(L))
for m in (1.5, 1.75, 2.0): J[m].pop('R')
J['n'] = n; J['agree'] = agree; J['d'] = D_
json.dump(J, open('tp1_summary.json', 'w'))
