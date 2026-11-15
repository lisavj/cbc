"""Time-block analysis on the current CBC EMA Slope 3m settings (MES / MGC / MNQ / M2K) -- every 3 weeks (created 11/15/2026).
Patches claude/all_eng.py at runtime to the v1.19 3m bases. One extra one-hour block at a time (candle open time, ET), current
blocks removed one at a time, no-new-setup window, End setups at 16:00, opening-range forming blocks per session.
Needs (same folder): all_eng.py, ats_inputs_study.py, chop_sim.py, ema716_eng.py, mes3_ema_grid.py (project claude/).
Usage: python3 blk_watch.py MES   (one chart per call; fresh bars unless --cached)
"""
import sys, os, glob
if '--cached' not in sys.argv:
    for f in glob.glob('/tmp/m??3.pkl'): os.remove(f)
src = open('all_eng.py').read()
for a, c in (("SLP = np.abs(h20raw - np.roll(h20raw, 12)) / A", "SLP = np.abs(h20raw - np.roll(h20raw, o.get('slk', 12))) / A"),
             ("    o = dict(CFGX['base'], **o)", "    o = {**CFGX['base'], **{k: ({**CFGX['base'].get(k, {}), **v} if isinstance(v, dict) else v) for k, v in o.items()}}"),
             (" 'MGC': dict(cost=.22, f='/tmp/mgc3.pkl', fdp=8., tw=None,", " 'MGC': dict(cost=.22, f='/tmp/mgc3.pkl', fdp=8., tw=1.0,"),
             ("base=dict(slope=.42, erl=.15, rg=5, ride=True, hb=(13, 14))", "base=dict(slope=.42, erl=.15, rg=5, ride=True, hb=(13, 14), P=dict(qwin=(960, 1140), eod=False))"),
             ("base=dict(slope=.30, rg=5, x4=4)", "base=dict(slope=.165, slk=5, rg=5, x4=4)"),
             ("base=dict(slope=.48, erl=.23, x4=4), q=dict(sl=1.7, mn=3, cap=5,", "base=dict(slope=.48, erl=.23, x4=4, q=dict(sl=3.5, part=0.0)), q=dict(sl=1.7, mn=3, cap=8,"),
             ("base=dict(slope=.75, erl=.15)", "base=dict(slope=.75, erl=.15, q=dict(cap=60), P=dict(orny=False))")):
    assert src.count(a) == 1, 'all_eng.py changed: ' + a[:50]
    src = src.replace(a, c)
exec(src)
sym = sys.argv[1]; setup(sym); b = run({})
cur = tuple(CFGX['base'].get('hb', ()))
def row(nm, a):
    z, d_, l4, vd = cmp(a, b); return '| %s | %d | %+.0f | %+.0f | %+.1f | %s | %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['net'] - b['net'], z, ' / '.join('%+.0f' % t for t in d_), l4, a['dd'], vd)
out = ['## %s 3m (current settings, data to %s)' % (sym, __import__('datetime').datetime.utcfromtimestamp(B.t.values[-1] / 1000).strftime('%m/%d')), '', 'Base: %d trades, %+.0f, thirds %s, last 4 wk %+.0f, max DD %.0f; current hour blocks %s' % (b['n'], b['net'], ' / '.join('%+.0f' % t for t in b['th']), b['l4'], b['dd'], cur or 'none'), '',
       '| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |', '|---|---|---|---|---|---|---|---|---|']
res = {}
for h in [18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    if h in cur: continue
    a = run(dict(hb=cur + (h,))); res[h] = a; out.append(row('Block %02d:00-%02d:00' % (h, (h + 1) % 24), a))
for h in cur:
    out.append(row('Unblock %02d:00-%02d:00 (current block)' % (h, h + 1), run(dict(hb=tuple(x for x in cur if x != h)))))
out += [row('No new setups 16:00-19:00 (instead of 18:45)', run(dict(P=dict(qwin=(960, 1140))))) if sym != 'MES' else row('No new setups to 18:45 (v10.97 window)', run(dict(P=dict(qwin=(960, 1125))))),
        row('No-new-setup window OFF', run(dict(P=dict(qwin=(None, None))))),
        row('End setups at 16:00 ' + ('ON' if sym == 'MES' else 'OFF'), run(dict(P=dict(eod=(sym == 'MES'))))),
        row('OR forming block NY ' + ('ON' if sym == 'MNQ' else 'OFF'), run(dict(P=dict(orny=(sym == 'MNQ'))))),
        row('OR forming block London OFF', run(dict(P=dict(orln=False)))), row('OR forming block Asia OFF', run(dict(P=dict(oras=False))))]
good = [h for h, a in res.items() if cmp(a, b)[3] in ('robust', 'promising')]
if len(good) >= 2:
    out.append(row('Combined promising hours %s' % ', '.join('%02d' % h for h in sorted(good)), run(dict(hb=cur + tuple(good)))))
print('\n'.join(out) + '\n', flush=True)
