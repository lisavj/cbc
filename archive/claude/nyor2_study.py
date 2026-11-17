"""NY opening-range block on the 2m / 5m charts -- MES / MGC / MNQ / M2K -- 11/13/2026. Usage: python3 nyor2_study.py [2|5] [SYM ...]
5m: Jan 5 -> now, no gates on any 5m chart.
Question: CBC "No new setups during opening range (forming)" blocks every new Trade Setup on candles opening 9:30-9:59 ET (NY).
On 2m charts, should that block stay, be shortened (9:30-9:45 / 9:30-9:40) or go?
Replay (chop_sim engine with the opening-range skip turned into a label = chop_sim_or; Jun 1 -> now, thirds by date), each
chart's live gates (MES 2m 1H MTF gate; MGC 2m range gate 5 ATR; MNQ / M2K 2m none), London / Asia blocks kept ON.
Turning the block off adds the window setups AND can change later setups (cooldown, one setup at a time).
Exits: CHART = base exits (SL1 1.7 ATR + per-symbol min / cap, TP1 1.7 ATR + cap, 80 % at TP1, BE, trail 1.7);
BRACKET = SL 3 ATR / TP 1.75 ATR, 100 % at TP1 (bot-style). Net after costs: MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35 pts.
z = change / (per-setup SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
LIVE: Trade Setups never fire in the window (block ON), so live evidence = every other directional alert on the 2m chart since
10/19, scored with the bracket from its candle close: 9:30-9:59 vs 10:00-10:29 vs the rest of the day.
"""
import re, json, collections, datetime as D, numpy as np, pandas as pd
from zoneinfo import ZoneInfo
import sys as _s
_a = _s.argv[1:]; _s.argv[1:] = []
import chop_sim as cs, chop_sim_or as cso, stretch_study as ss, flip_order_study as fo
_s.argv[1:] = _a

TZ = ZoneInfo('America/New_York')
ss.FROM[5] = '2026-01-05'
TF = 2
COST = {'MES': .5, 'MGC': .22, 'MNQ': .87, 'M2K': .35}
G2 = {'MES': dict(R5=0, X4=0, MTF=1), 'MGC': dict(R5=1, X4=0, MTF=0), 'MNQ': dict(R5=0, X4=0, MTF=0), 'M2K': dict(R5=0, X4=0, MTF=0)}
Q = {'MES': dict(ss.QB['MES'], tcap=6), 'MGC': dict(ss.QB['MGC'], tcap=6),
     'MNQ': dict(sl=1.7, mn=25, cap=30, tp=1.7, tcap=40, part=.8, be=True, ts=0, tr=1.7),
     'M2K': dict(sl=1.7, mn=3, cap=5, tp=1.7, tcap=3, part=.8, be=True, ts=0, tr=1.7)}

G5 = {k: dict(R5=0, X4=0, MTF=0) for k in ('MES', 'MGC', 'MNQ', 'M2K')}
G = G2


class Case(cso.Case):
    sim1 = cs.Case.sim1
    run = cs.Case.run


VARIANTS = [('Current: block 9:30-10:00', (570, 600)), ('Block 9:30-9:45 only (allow 9:45-10:00)', (570, 585)),
            ('Block 9:30-9:40 only (allow 9:40-10:00)', (570, 580)), ('Block OFF (allow 9:30-10:00)', (570, 570))]


def runv(s, sym, blk, q):
    a, b = blk
    ok = lambda d: cs.cur_rule(d) and d['orw'] not in ('London', 'Asia') and not (d['orw'] == 'NY' and a <= s.orm[d['i']] < b)
    return s.run(ok, q=q, gates=G[sym])


def summ(R, s, cost, cuts):
    v = np.array([r['res'] - cost for r in R])
    th = [sum(r['res'] - cost for r in R if (0 if s.T[r['i']] < cuts[0] else 1 if s.T[r['i']] < cuts[1] else 2) == k) for k in range(3)]
    return dict(n=len(v), net=v.sum(), w=100 * (v > 0).mean() if len(v) else 0, sd=v.std() or 1, th=th, k={(r['i'], r['lg']): r['res'] - cost for r in R})


def run_chart(sym, out):
    s = Case(sym, TF, ss.load(sym, TF)); cost = COST[sym]
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    out += ['', '# %s %dm' % (sym, TF), '', 'Replay %s -> %s; gates %s; cost %.2f.' % (s.date[300], s.date[-1], G[sym], cost)]
    verdict = []
    for qn, q in (('CHART exits', Q[sym]), ('BRACKET SL 3 / TP 1.75 ATR', dict(sl=3.0, mn=0, cap=1e9, tp=1.75, tcap=1e9, part=1.0, be=False, ts=0, tr=1.7))):
        R0 = runv(s, sym, VARIANTS[0][1], q); b = summ(R0, s, cost, cuts)
        out += ['', '## %s %dm -- %s' % (sym, TF, qn), '', 'Current: %d setups, net %+.1f, win %.0f %%, thirds %+.0f / %+.0f / %+.0f' % (b['n'], b['net'], b['w'], *b['th']), '',
                '| Variant | Setups | Net | Δ vs current | z | Δ by third | Δ last 4 wk | Verdict |', '|---|---|---|---|---|---|---|---|']
        for nm, blk in VARIANTS[1:]:
            R = runv(s, sym, blk, q); a = summ(R, s, cost, cuts)
            ch = sum(1 for k in set(a['k']) | set(b['k']) if abs(a['k'].get(k, 1e9) - b['k'].get(k, 1e9)) > 1e-9) or 1
            z = (a['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); d = [x - y for x, y in zip(a['th'], b['th'])]
            l4 = sum(r['res'] - cost for r in R if s.T[r['i']] >= t4) - sum(r['res'] - cost for r in R0 if s.T[r['i']] >= t4)
            vd = 'robust' if z >= 2 and all(x > 0 for x in d) else 'promising' if z >= 1 and all(x > 0 for x in d) else 'robustly worse' if z <= -2 and all(x < 0 for x in d) else 'worse' if a['net'] < b['net'] else 'noise'
            out.append('| %s | %d | %+.1f | %+.1f | %+.1f | %+.0f / %+.0f / %+.0f | %+.1f | %s |' % (nm, a['n'], a['net'], a['net'] - b['net'], z, *d, l4, vd))
            verdict.append((qn, nm, a['net'] - b['net'], z, d, vd))
        # the window setups themselves (block OFF)
        RO = runv(s, sym, (570, 570), q)
        for lab, a_, b_ in (('9:30-9:44', 570, 585), ('9:45-9:59', 585, 600)):
            w = [r['res'] - cost for r in RO if r.get('orw') == 'NY' and a_ <= s.orm[r['i']] < b_]
            if w: out.append('| (window setups %s when OFF) | %d | %+.1f | avg %+.2f, win %.0f %% | | | | |' % (lab, len(w), sum(w), np.mean(w), 100 * np.mean(np.array(w) > 0)))
    # live: other alert types by time bucket
    lv = fo.live_signals(s, sym, TF)
    om = s.orm
    buckets = collections.defaultdict(list)
    for (i, lg, typ, x) in lv:
        if typ.startswith('SETUP'): buckets['Trade Setups in 9:30-9:59 (should be 0)' if 570 <= om[i] < 600 else '_'].append(0); continue
        r, j = fo.bot_exit(s, i, lg)
        if r is None: continue
        b_ = '9:30-9:59' if 570 <= om[i] < 600 else '10:00-10:29' if 600 <= om[i] < 630 else 'rest of day'
        buckets[b_].append(r - cost)
    out += ['', '## %s %dm -- live directional alerts (not Trade Setups) since 10/19, bracket SL 3 / TP 1.75 ATR' % (sym, TF), '', '| Candle opens | Alerts | Win % | Net | Avg |', '|---|---|---|---|---|']
    for b_ in ('9:30-9:59', '10:00-10:29', 'rest of day'):
        v = buckets[b_]
        out.append('| %s | %d | %s | %+.1f | %s |' % (b_, len(v), ('%.0f %%' % (100 * np.mean(np.array(v) > 0))) if v else '-', sum(v), ('%+.2f' % np.mean(v)) if v else '-'))
    out.append('Trade Setups found in 9:30-9:59 live: %d' % len(buckets['Trade Setups in 9:30-9:59 (should be 0)']))
    return verdict


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if args and args[0].isdigit(): TF = int(args.pop(0))
    if TF == 5: G = G5
    syms = args or ['MES', 'MGC', 'MNQ', 'M2K']
    out = ['# NY opening-range block on %dm charts -- %s' % (TF, D.datetime.now(TZ).strftime('%Y-%m-%d %H:%M ET')), '', __doc__]
    top = ['', '## Overview (Δ net vs current block, z, Δ by third, verdict)', '', '| Chart | Exits | Variant | Δ | z | Δ thirds | Verdict |', '|---|---|---|---|---|---|---|']
    for sym in syms:
        try:
            for (qn, nm, dn, z, d, vd) in run_chart(sym, out):
                top.append('| %s %dm | %s | %s | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (sym, TF, qn.split(' ')[0], nm, dn, z, *d, vd))
        except Exception as e:
            import traceback; traceback.print_exc(); out += ['', '# %s %dm FAILED: %r' % (sym, TF, e)]
        print('done', sym, file=sys.stderr, flush=True)
    open('nyor%d_report.md' % TF, 'w').write('\n'.join(out[:3] + top + out[3:])); print('\n'.join(top))
