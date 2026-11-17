"""Opening-range block check -- "No new setups during opening range (forming)": NY 9:30-10:00, London 3:00-3:30, Asia 20:00-20:30 ET.
Replay (CBC engine, opening-range skip turned into a label), each chart's live gates, per session: block OFF vs current (all ON).
Charts MES / MGC 2m 3m 5m + MNQ / M2K 3m. 3m/5m Jan 5 -> now, 2m Jun 1 -> now; thirds by date.
Exits: LIVE = MES 3m 100 % at TP1 (SL1 3 ATR, TP1 1.75), MGC 3m FLIP 0 % (CBC v10.96), others base (1.7 / 1.7 / 80 % / BE / trail 1.7);
BRACKET = SL 3 / TP 1.75 ATR, 100 % at TP1. Net after costs (MES .50, MGC .22, MNQ .87, M2K .35).
z = Δ / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three."""
import sys as _s
_a = _s.argv[1:]; _s.argv[1:] = []
import numpy as np, datetime as D
import chop_sim as cs, chop_sim_or as cso, stretch_study as ss, nyor2_study as ny
_s.argv[1:] = _a
ss.FROM[5] = '2026-01-05'
COST = ny.COST
GATES = {('MES', 3): dict(R5=1, X4=0, MTF=0), ('MGC', 3): dict(R5=1, X4=1, MTF=0), ('MES', 2): dict(R5=0, X4=0, MTF=1), ('MGC', 2): dict(R5=1, X4=0, MTF=0)}
def liveq(sym, tf):
    if (sym, tf) == ('MES', 3): return dict(sl=3.0, mn=5, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=True, ts=0, tr=1.7)
    if (sym, tf) == ('MGC', 3): return dict(cs.EXIT[('MGC', 3)], part=0.0, tr=1e9)
    return ny.Q[sym]
BR = dict(sl=3.0, mn=0, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=False, ts=0, tr=1.7)
SES = {'NY': 'NY', 'London': 'London', 'Asia': 'Asia'}
CH = [('MES', 3), ('MGC', 3), ('MNQ', 3), ('M2K', 3), ('MES', 2), ('MGC', 2), ('MES', 5), ('MGC', 5)]
out = [__doc__, '', '| Chart | Exits | Block OFF | Δ | z | Δ by third | Δ last 4 wk | Window setups when OFF (n / net) | Verdict |', '|---|---|---|---|---|---|---|---|---|']
for sym, tf in CH:
    s = ny.Case(sym, tf, ss.load(sym, tf)); c = COST[sym]; G = GATES.get((sym, tf), dict(R5=0, X4=0, MTF=0))
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def run(off, q):
        R = s.run(lambda d: cs.cur_rule(d) and (d['orw'] == '' or d['orw'] in off), q=q, gates=G)
        v = np.array([r['res'] - c for r in R])
        return dict(net=v.sum(), sd=v.std(), th=[sum(r['res'] - c for r in R if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)],
                    l4=sum(r['res'] - c for r in R if s.T[r['i']] >= t4), K={(r['i'], r['lg']): r['res'] - c for r in R}, R=R)
    for qn, q in (('live', liveq(sym, tf)), ('bracket', BR)):
        b = run(set(), q)
        for nm, off in (('NY', {'NY'}), ('London', {'London'}), ('Asia', {'Asia'}), ('all three', {'NY', 'London', 'Asia'})):
            a = run(off, q); ch = sum(1 for k in set(a['K']) | set(b['K']) if abs(a['K'].get(k, 1e9) - b['K'].get(k, 1e9)) > 1e-9) or 1
            z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d = [x - y for x, y in zip(a['th'], b['th'])]
            w = [r['res'] - c for r in a['R'] if r.get('orw') in off]
            vd = 'robust' if z >= 2 and all(x > 0 for x in d) else 'promising' if z >= 1 and all(x > 0 for x in d) else 'block robustly right' if z <= -2 and all(x < 0 for x in d) else 'worse' if a['net'] < b['net'] else 'noise'
            out.append('| %s %dm | %s | %s | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %+.0f | %d / %+.0f | %s |' % (sym, tf, qn, nm, a['net'] - b['net'], z, *d, a['l4'] - b['l4'], len(w), sum(w), vd))
    print('done', sym, tf, file=_s.stderr, flush=True)
open('orb_all_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
