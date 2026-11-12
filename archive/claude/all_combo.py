"""Everything together, MES 3m and MGC 3m -- 11/08/2026.
Entry filter x session stop x exit rules, all in one replay (net after costs; gain beyond random skipping in brackets).
MES 3m: filter = skip shorts when price is below... above the 5-day EMA rule (shorts only when price is below the 5-day EMA of session closes);
        stop = 2 losses in a row or 2 flip-outs per 18-18 session, ONLY when the previous 5 sessions lost (regime switch);
        TP rule = TP1 -> 85 % after 18 min; SL rule = SL1 to half its distance if negative at 18 min.
MGC 3m: filter = skip setups against VWAP; stop = London (03:00-09:30 ET) stops after its first loss;
        TP rule = TP1 -> 65 % after 21 min; SL rule = close if under 25 % of TP1 at 18 min.
Costs: commission + 1 tick per trade (MES 0.50 / MGC 0.22), +1 tick for a rule exit at the candle close."""
import numpy as np, pandas as pd, itertools, collections as C, datetime as D
import combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg
from skip_why import guard2, sub
from skip_fix import regime
from sess_loss import guard as sguard
SET = {'MES': dict(filt=('d5', 'S'), tp=(18, .85), sl=('HALF', 0.0, 18), cost=.5, tick=.25),
       'MGC': dict(filt=('vwap', 'B'), tp=(21, .65), sl=('CUT', .25, 18), cost=.22, tick=.1)}
def stop(sym, r, b):
    if sym == 'MES':
        act = regime(b, 5); g = guard2(r, 2, 2)[0]; gi = {t['i'] for t in g}
        return [t for t in r if t['i'] in gi or not act[t['ss']]]
    return sguard(r, (0, 1, 0))
PER = [('Third 1', lambda t: t['th'] == 0), ('Third 2', lambda t: t['th'] == 1), ('Third 3', lambda t: t['th'] == 2), ('Last 4 wk', lambda t: t['l4']), ('Whole', lambda t: True)]
def pstats(v):
    v = np.array(v) if len(v) else np.zeros(0); w = v[v > 0].sum(); l = -v[v < 0].sum(); eq = np.cumsum(v)
    dd = (np.maximum.accumulate(np.r_[0, eq])[1:] - eq).max() if len(v) else 0
    return len(v), v.sum(), round(100 * (v > 0).sum() / max(1, (v != 0).sum())), (w / l if l else 0), dd
L = [__doc__, '']
for sym in ('MES', 'MGC'):
    P = SET[sym]; nm, q, G = cb.CH[sym]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B); TR, ss = tg.trend_arrays(s)
    et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); mm = (et.dt.hour * 60 + et.dt.minute).values
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    runs = {}
    for fon, xk in itertools.product((False, True), ('current', 'TP', 'SL', 'TP+SL')):
        f = P['filt'] if fon else None
        def ok(d, f=f):
            if not cs.cur_rule(d): return False
            if f is None or (f[1] == 'S' and d['lg']): return True
            v = TR[f[0]][d['i']]; return v == 0 or v == (1 if d['lg'] else -1)
        cb.CCase.TX, cb.CCase.TY = P['tp'] if 'TP' in xk else (0, 0.0)
        cb.CCase.ACT, cb.CCase.SY, cb.CCase.SX = P['sl'] if 'SL' in xk else (None, 0.0, 0)
        r = s.run(ok, q=q, gates=G)
        runs[(fon, xk)] = [dict(i=t['i'], j=t['j'], lg=t['lg'], why=t['why'], n=t['res'] - P['cost'] - (P['tick'] if t['why'] == 'cut' else 0),
                                th=0 if s.T[t['i']] < cuts[0] else 1 if s.T[t['i']] < cuts[1] else 2, l4=bool(s.T[t['i']] >= t4), ss=ss[t['i']], sub=sub(mm[t['i']])) for t in r]
    b = runs[(False, 'current')]; ab = np.mean([t['n'] for t in b])
    rows = []
    for (fon, xk), r in runs.items():
        for son in (False, True):
            v = stop(sym, r, b) if son else r
            o = []
            for _, Pf in PER:
                n1 = sum(t['n'] for t in v if Pf(t)); n0 = sum(t['n'] for t in b if Pf(t)); c1 = sum(1 for t in v if Pf(t)); c0 = sum(1 for t in b if Pf(t))
                o.append((n1, n1 - n0 + (c0 - c1) * ab))
            rows.append(((fon, son, xk), o, v))
    lab = lambda k: '%s / %s / %s' % ('filter' if k[0] else '—', 'stop' if k[1] else '—', {'current': 'current exits', 'TP': 'TP rule', 'SL': 'SL rule', 'TP+SL': 'TP + SL rules'}[k[2]])
    L += ['## %s' % nm, '', 'Filter / session stop / exits. ✓ = beyond random positive in all three thirds; ↑ = last 4 weeks not worse than current exits.', '',
          '| Filter / stop / exits | ' + ' | '.join(p for p, _ in PER) + ' | Trades | |', '|---|' + '---|' * (len(PER) + 2)]
    cur4 = rows[0][1][3][0]
    for k, o, v in sorted(rows, key=lambda x: -x[1][4][0]):
        ok3 = all(o[i][1] > 0 for i in range(3)) if k != (False, False, 'current') else False
        L.append('| %s | %s | %d | %s%s |' % (lab(k), ' | '.join('%+.0f (%+.0f)' % x for x in o), len(v), '✓' if ok3 else '', '↑' if o[3][0] >= cur4 else ''))
    # full stats for current vs best all-in
    best = max(rows, key=lambda x: x[1][4][0]); full = [x for x in rows if x[0] == (True, True, 'TP+SL')][0]
    L += ['', '**Full stats** (after costs): trades / net / win %% / profit factor / max drawdown', '', '| Period | Current exits | All four (filter + stop + TP + SL) | Best row (%s) |' % lab(best[0]), '|---|---|---|---|']
    for pn, Pf in PER:
        L.append('| %s | %s | %s | %s |' % (pn, *['%d / %+.0f / %d %% / %.2f / %.0f' % pstats([t['n'] for t in v if Pf(t)]) for v in (b, full[2], best[2])]))
    L.append('')
    print(sym, 'done', flush=True)
open('all_combo_report.md', 'w').write('\n'.join(L))
