#!/usr/bin/env python3
"""Maximum favourable price (MFE) with and without the recommended rules -- MES 3m and MGC 3m -- 11/08/2026.
For every trade: MFE in trade = the best price reached in the trade's direction between entry and exit (points, and as a share of
the TP1 distance); MAE = the worst price against; giveback = MFE minus the result (gross, before costs); MFE 60 = the best price in
the first 60 min after entry whatever the exit (what the setup offered); for trades a rule closes early: how far price went
afterwards, up to where the current exits would have closed the same trade.
Rule sets (same replay as all_combo.py; live 3m exits):
  MES 3m: current | TP1 -> 85 % after 18 min | balanced = shorts only below the 5-day EMA + stop after 2 losses / 2 flip-outs only
          when the previous 5 sessions lost + half SL1 if negative at 18 min | all four (balanced + the TP rule)
  MGC 3m: current | London stops after its first loss | London stop + skip against VWAP | all four (+ TP1 -> 65 % after 21 min +
          close if under 25 % of TP1 at 18 min)"""
import numpy as np, pandas as pd, datetime as D
import combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg, study5 as s5

SETS = {'MES': [('Current exits', None, None, (0, 0.0), (None, 0.0, 0)),
                ('TP1 -> 85 % after 18 min', None, None, (18, .85), (None, 0.0, 0)),
                ('Balanced (filter + losing-stretch stop + SL rule)', ('d5', 'S'), ('r', 2, 2), (0, 0.0), ('HALF', 0.0, 18)),
                ('All four', ('d5', 'S'), ('r', 2, 2), (18, .85), ('HALF', 0.0, 18))],
        'MGC': [('Current exits', None, None, (0, 0.0), (None, 0.0, 0)),
                ('London stop after 1st loss', None, ('u', (0, 1, 0)), (0, 0.0), (None, 0.0, 0)),
                ('London stop + VWAP filter', ('vwap', 'B'), ('u', (0, 1, 0)), (0, 0.0), (None, 0.0, 0)),
                ('All four', ('vwap', 'B'), ('u', (0, 1, 0)), (21, .65), ('CUT', .25, 18))]}
COST = {'MES': (.5, .25), 'MGC': (.22, .1)}
PER = [('Whole', lambda t: True), ('Third 3', lambda t: t['th'] == 2), ('Last 4 wk', lambda t: t['l4'])]
L = [__doc__, '']
for sym in ('MES', 'MGC'):
    nm, q, G = cb.CH[sym]; cost, tick = COST[sym]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = cb.CCase(sym, 3, B); TR, ss = tg.trend_arrays(s)
    et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); mm = (et.dt.hour * 60 + et.dt.minute).values
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    H, Lo, Cl = s.H, s.L, s.C
    def run(f, tp, sl):
        def ok(d):
            if not cs.cur_rule(d): return False
            if f is None or (f[1] == 'S' and d['lg']): return True
            v = TR[f[0]][d['i']]; return v == 0 or v == (1 if d['lg'] else -1)
        cb.CCase.TX, cb.CCase.TY = tp; cb.CCase.ACT, cb.CCase.SY, cb.CCase.SX = sl
        out = []
        for t in s.run(ok, q=q, gates=G):
            i, j, lg = t['i'], t['j'], t['lg']; g = 1 if lg else -1; en = Cl[i]
            tpd = min(q['tp'] * s.atr[i], q['tcap'])
            seg = slice(i + 1, j + 1); h60 = slice(i + 1, min(s.n, i + 1 + 20))
            mfe = max(0.0, g * ((H[seg].max() if lg else Lo[seg].min()) - en)) if j > i else 0.0
            mae = max(0.0, -g * ((Lo[seg].min() if lg else H[seg].max()) - en)) if j > i else 0.0
            m60 = max(0.0, g * ((H[h60].max() if lg else Lo[h60].min()) - en))
            out.append(dict(i=i, j=j, lg=lg, why=t['why'], g=t['res'], n=t['res'] - cost - (tick if t['why'] == 'cut' else 0), tpd=tpd,
                            mfe=mfe, mae=mae, m60=m60, th=0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2,
                            l4=bool(s.T[i] >= t4), ss=ss[i], sub=s5.sub(mm[i])))
        return out
    base = None; rows = []
    for lab, f, st, tp, sl in SETS[sym]:
        r = run(f, tp, sl)
        if base is None: base = r
        if st: r = s5.apply_stop(st, r, base)
        rows.append((lab, r))
    bi = {t['i']: t for t in base}
    L += ['## %s' % nm, '']
    for pn, P in PER:
        L += ['**%s** (points; TP1 = share of the TP1 distance)' % pn, '',
              '| Rule set | Trades | Avg MFE in trade | Median MFE | Avg MFE / TP1 | Reached 50 % of TP1 | Reached TP1 | Reached 1.5 x TP1 | Avg MAE | Avg result (gross) | Giveback (MFE − result) | Captured % of MFE | MFE first 60 min | Net after costs |',
              '|---|' + '---|' * 13]
        for lab, r in rows:
            v = [t for t in r if P(t)]
            if not v: continue
            a = lambda k: np.mean([t[k] for t in v]); fr = lambda x: 100 * np.mean([t['mfe'] >= x * t['tpd'] for t in v])
            mf = sum(t['mfe'] for t in v)
            L.append('| %s | %d | %.2f | %.2f | %.2f | %.0f %% | %.0f %% | %.0f %% | %.2f | %+.2f | %.2f | %.0f %% | %.2f | %+.0f |' % (
                lab, len(v), a('mfe'), np.median([t['mfe'] for t in v]), np.mean([t['mfe'] / t['tpd'] for t in v]), fr(.5), fr(1), fr(1.5),
                a('mae'), a('g'), a('mfe') - a('g'), 100 * sum(t['g'] for t in v) / mf if mf else 0, a('m60'), sum(t['n'] for t in v)))
        L.append('')
    # what happened after an early rule exit
    for lab, r in rows[1:]:
        cut = [t for t in r if t['why'] in ('cut', 'TPx') and t['i'] in bi]
        if not cut: continue
        L += ['**After an early rule exit — %s** (the same trade under current exits)' % lab, '', '| Exit | Trades | Avg result with rule | Avg result current exits | Avg MFE until rule exit | Avg MFE under current exits | Later reached TP1 under current exits | Current exits ended at the full SL1 |', '|---|---|---|---|---|---|---|---|']
        for w in ('cut', 'TPx'):
            v = [t for t in cut if t['why'] == w]
            if not v: continue
            bb = [bi[t['i']] for t in v]
            L.append('| %s | %d | %+.2f | %+.2f | %.2f | %.2f | %.0f %% | %.0f %% |' % (
                'cut / tightened stop' if w == 'cut' else 'reduced TP filled', len(v), np.mean([t['g'] for t in v]), np.mean([t['g'] for t in bb]),
                np.mean([t['mfe'] for t in v]), np.mean([t['mfe'] for t in bb]), 100 * np.mean([t['mfe'] >= t['tpd'] for t in bb]), 100 * np.mean([t['why'] == 'SL1' for t in bb])))
        L.append('')
    # trades removed by filter / stop
    for lab, r in rows[1:]:
        ri = {t['i'] for t in r}; gone = [t for t in base if t['i'] not in ri]
        if not gone: continue
        kept = [t for t in base if t['i'] in ri]
        L += ['**Trades the %s rule set skips** vs the trades it keeps (current exits): skipped %d, avg MFE %.2f (%.0f %% reached TP1), avg result %+.2f gross; kept %d, avg MFE %.2f (%.0f %% reached TP1), avg result %+.2f gross.' % (
            lab, len(gone), np.mean([t['mfe'] for t in gone]), 100 * np.mean([t['mfe'] >= t['tpd'] for t in gone]), np.mean([t['g'] for t in gone]),
            len(kept), np.mean([t['mfe'] for t in kept]), 100 * np.mean([t['mfe'] >= t['tpd'] for t in kept]), np.mean([t['g'] for t in kept])), '']
    print(sym, 'done', flush=True)
open('mfe_report.md', 'w').write('\n'.join(L))
