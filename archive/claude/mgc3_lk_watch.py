"""Weekly watch (Tuesdays): MGC 3m 15-min HTF EMA20 slope lookback (CBC EMA Slope v1.18) + MES 3m check + MNQ / M2K 3m candidates -- created 11/15/2026.
v1.19 (11/15) adopted MNQ 3m cap 60 + NY OR forming block OFF (+2511, z 3.9 vs v1.18) and M2K 3m SL1 3.5 ATR + 0 % at TP1 (+111, z 2.6).
Revert watch for both: the 'v1.18' row is v1.18 vs v1.19 (negative = v1.19 better); REVERT CANDIDATE if the v1.18 row is positive since go-live on 3 consecutive runs or v1.19's edge (v1.18 row z) rises above -1.

v1.18 put MGC 3m on slope lookback 5 bars (15 min) / threshold 0.165 (was 12 bars / 0.30) on a PROMISING-only result
(+601, z 1.8, last 4 wk -51). This re-runs the replay on fresh bars each week and compares v1.18 with v1.17 on
(a) the full period Jan 5 -> latest, (b) the last 4 weeks, (c) live period since go-live (bars from 2026-11-16 on),
plus neighbours, and MES 3m (unchanged, 36-min lookback 0.42) against 15 / 30 / 45-min lookbacks.
Rule: REVERT CANDIDATE if v1.18 - v1.17 since go-live < 0 on 3 consecutive Tuesday runs, or the full-period z < 1;
KEEP otherwise. Upgrade to robust when z >= 2 with all thirds and the last 4 weeks positive.
Needs (same folder): all_eng.py, ats_inputs_study.py, chop_sim.py, ema716_eng.py, mes3_ema_grid.py (project claude/).
Usage: python3 mgc3_lk_watch.py   -> prints a markdown section (append it to claude/mgc3_lk_watch.md).
"""
import sys, os, glob, datetime as D
if '--cached' not in sys.argv:
    for f in glob.glob('/tmp/m??3.pkl'): os.remove(f)          # fresh bars every run
src = open('all_eng.py').read()
for a, b in (("SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A", "SLP = np.abs(h20raw - np.roll(h20raw, o.get('slk', 12))) / A"),
             ("    o = dict(CFGX['base'], **o)", "    o = {**CFGX['base'], **{k: ({**CFGX['base'].get(k, {}), **v} if isinstance(v, dict) else v) for k, v in o.items()}}"),
             (" 'MGC': dict(cost=.22, f='/tmp/mgc3.pkl', fdp=8., tw=None,", " 'MGC': dict(cost=.22, f='/tmp/mgc3.pkl', fdp=8., tw=1.0,"),
             ("base=dict(slope=.42, erl=.15, rg=5, ride=True, hb=(13, 14))", "base=dict(slope=.42, erl=.15, rg=5, ride=True, hb=(13, 14), P=dict(qwin=(960, 1140), eod=False))"),
             ("base=dict(slope=.30, rg=5, x4=4)", "base=dict(slope=.165, slk=5, rg=5, x4=4)"),
             ("base=dict(slope=.48, erl=.23, x4=4), q=dict(sl=1.7, mn=3, cap=5,", "base=dict(slope=.48, erl=.23, x4=4, q=dict(sl=3.5, part=0.0)), q=dict(sl=1.7, mn=3, cap=8,"),
             ("base=dict(slope=.75, erl=.15)", "base=dict(slope=.75, erl=.15, q=dict(cap=60), P=dict(orny=False))")):
    assert src.count(a) == 1, 'all_eng.py changed: ' + a[:50]
    src = src.replace(a, b)
exec(src)
LIVE0 = int(D.datetime(2026, 11, 16, 18, 0).timestamp() * 1000)   # first session on v1.18 (approx, UTC-agnostic)


def seg(a, s):
    v = [x for (t, lg), x in a['K'].items() if t >= LIVE0]; return sum(v), len(v)


def row(nm, a, b, s):
    z, d_, l4, vd = cmp(a, b); lv, ln = seg(a, s); bv, bn = seg(b, s)
    return '| %s | %d | %+.0f | %+.0f | %+.1f | %s | %+.0f | %.0f | %d / %+.0f (%+.0f) | %s |' % (
        nm, a['n'], a['net'], a['net'] - b['net'], z, ' / '.join('%+.0f' % t for t in d_), l4, a['dd'], ln, lv, lv - bv, vd)


HDR = ['| Variant | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Since go-live trades / net (vs base) | Verdict |', '|---|---|---|---|---|---|---|---|---|---|']
out = ['## Run %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '']
# MGC 3m: base = v1.18
setup('MGC'); s = case(dict(TDEF, fdp=CFGX['fdp'], tw=CFGX['tw'], erl=.08)); b18 = run({})
v17 = run(dict(slope=.30, slk=12))
out += ['### MGC 3m: v1.18 (15-min lookback 0.165) vs v1.17 (36-min 0.30)', '', 'Base = v1.18: %d trades, %+.0f, max DD %.0f; data to %s.' % (
    b18['n'], b18['net'], b18['dd'], D.datetime.utcfromtimestamp(s.T[-1] / 1000).strftime('%m/%d %H:%M UTC')), ''] + HDR
out.append(row('v1.17 (12 bars, 0.30)', v17, b18, s))
for nm, o in (('5 bars 0.15', dict(slope=.15)), ('5 bars 0.18', dict(slope=.18)), ('4 bars 0.13', dict(slk=4, slope=.13)), ('6 bars 0.20', dict(slk=6, slope=.20)),
              ('10 bars 0.33', dict(slk=10, slope=.33)), ('Range gate OFF', dict(rg=0)), ('Late-away 2 pts', dict(P=dict(tw=2.0)))):
    out.append(row(nm, run(o), b18, s))
z, d_, l4, vd = cmp(b18, v17); lv, ln = seg(b18, s); bv, bn = seg(v17, s)
out += ['', '**MGC verdict:** v1.18 vs v1.17 full period %+.0f (z %+.1f, thirds %s, last 4 wk %+.0f) -> %s; since go-live %+.0f (%d vs %d trades).' % (
    b18['net'] - v17['net'], z, ' / '.join('%+.0f' % t for t in d_), l4, vd, lv - bv, ln, bn),
    'Rule: REVERT CANDIDATE if since-go-live < 0 on 3 consecutive runs (check previous runs below) or full-period z < 1.', '']
# MES 3m: unchanged, re-check lookback
setup('MES'); s = case(dict(TDEF, fdp=CFGX['fdp'], tw=CFGX['tw'], erl=.15, **CFGX['base']['P'])); bm = run({})
out += ['### MES 3m (unchanged: 36-min lookback 0.42)', '', 'Base: %d trades, %+.0f, max DD %.0f.' % (bm['n'], bm['net'], bm['dd']), ''] + HDR
for nm, o in (('15 min (5 bars) 0.175', dict(slk=5, slope=.175)), ('30 min (10 bars) 0.35', dict(slk=10, slope=.35)), ('45 min (15 bars) 0.525', dict(slk=15, slope=.525)), ('slope 0.38', dict(slope=.38)), ('slope 0.46', dict(slope=.46))):
    out.append(row(nm, run(o), bm, s))
out.append('')
# MNQ / M2K 3m: v1.19 sets (adopted 11/15) vs v1.18 + neighbours -- revert watch
for sym, VV in (('MNQ', (('v1.18 (cap 30, NY OR block ON)', dict(q=dict(cap=30), P=dict(orny=True))), ('cap 30 only (NY block stays OFF)', dict(q=dict(cap=30))), ('NY block ON only (cap stays 60)', dict(P=dict(orny=True))),
                         ('cap 45', dict(q=dict(cap=45))), ('cap OFF', dict(q=dict(cap=1e9))), ('+ all OR blocks OFF', dict(P=dict(orln=False, oras=False))))),
                ('M2K', (('v1.18 (SL1 1.7, 80 % at TP1)', dict(q=dict(sl=1.7, part=.8))), ('SL1 1.7 + 0 % (only TP1 % changed)', dict(q=dict(sl=1.7))), ('80 % at TP1 (only SL changed)', dict(q=dict(part=.8))),
                         ('SL1 3.0', dict(q=dict(sl=3.0))), ('SL1 4.0', dict(q=dict(sl=4.0))), ('25 % at TP1', dict(q=dict(part=.25)))))):
    setup(sym); s = case(dict(TDEF, fdp=CFGX['fdp'], tw=CFGX['tw'], erl=CFGX['base'].get('erl', .08))); bb = run({})
    out += ['### %s 3m: v1.19 vs v1.18 (revert watch)' % sym, '', 'Base = v1.19: %d trades, %+.0f, max DD %.0f.' % (bb['n'], bb['net'], bb['dd']), ''] + HDR
    for nm, o in VV:
        out.append(row(nm, run(o), bb, s))
    out.append('')
print('\n'.join(out))
