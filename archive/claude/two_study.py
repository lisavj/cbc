import sys
exec(open('two_eng.py').read())
sym = sys.argv[1]; setup(sym)
log = lambda m: print(m, file=sys.stderr, flush=True)
V0 = run({})
out = ['# %s 2m -- CBC EMA Slope branch studies -- 11/14/2026' % sym, '',
       'Replay Jun 1 -> Nov 13 (2m feed starts Jun 1), %s 2m (HTF = 10m), net after %.2f pts cost. v10.97 / v1.12 2m settings (no 2m entries in any per-chart list): ER 0.23 + breakout 3, no range gate / stretch / slope, toward late-away 1 pt, flip distance max(2 ATR, %g pts), SL1 1.7 ATR min %g cap %g, TP1 1.7 ATR cap %g, 80 %% at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. In-sample.' % (sym, COST, CFGX['fdp'], LIVEQ['mn'], LIVEQ['cap'], LIVEQ['tcap']), '',
       '## 0. v10.97 baseline', '', 'Trades %d, net %+.0f, avg %+.2f, win %.0f %%, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f' % (V0['n'], V0['net'], V0['avg'], V0['w'], *V0['th'], V0['l4'], V0['dd']), '',
       'By trigger: ' + ' · '.join('%s %d / %+.0f' % (k, *v) for k, v in V0['bt'].items()), '', 'By session: ' + ' · '.join('%s %d / %+.0f' % (k, *v) for k, v in V0['ses'].items()), '']
SL = [0.2, 0.3, 0.42, 0.48, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9, 1.0]
S = {t: run(dict(slope=t)) for t in SL}; log('slope')
out += table('1. HTF EMA20 slope filter (vs v10.97)', V0, [('slope %.2f' % t, S[t]) for t in SL])
sm = {t: np.mean([S[u]['net'] for u in SL[max(0, k - 1):k + 2]]) for k, t in enumerate(SL)}   # plateau pick: best 3-point average
best = max(SL, key=lambda t: sm[t]) if max(S[t]['net'] for t in SL) > V0['net'] else 0
B1 = S[best] if best else V0; log('best %s' % best)
q = LIVEQ
IDEAS = [('Flip setups ride to HTF flip back', dict(ride=True)), ('FLIP 0 % exit (0 % at TP1, BE, HTF flip)', dict(q=dict(part=0.0, tr=0))), ('100 % at TP1', dict(q=dict(part=1.0))), ('50 % at TP1', dict(q=dict(part=.5))),
         ('Range gate 5 ATR', dict(rg=5)), ('VWAP stretch 4 ATR', dict(x4=4)), ('LTF pierce min ER 0.12', dict(erl=.12)), ('LTF pierce min ER 0.15', dict(erl=.15)), ('LTF pierce min ER 0.20', dict(erl=.20)), ('LTF pierce min ER 0.23', dict(erl=.23)),
         ('Strict away flips (late-away OFF)', dict(P=dict(tw=None))), ('Trigger HTF CBC Flip OFF', dict(P=dict(t_flip=False))), ('Trigger LTF EMA20 Pierce OFF', dict(P=dict(t_ltf=False))),
         ('Trigger HTF EMA9 Pierce OFF', dict(P=dict(t_h9=False))), ('Trigger HTF EMA20 Pierce OFF', dict(P=dict(t_h20=False))), ('End setups at 16:00 OFF', dict(P=dict(eod=False))),
         ('SL1 1.5 ATR', dict(q=dict(sl=1.5))), ('SL1 2.5 ATR', dict(q=dict(sl=2.5))), ('SL1 3.0 ATR', dict(q=dict(sl=3.0))), ('TP1 1.5 ATR', dict(q=dict(tp=1.5))), ('TP1 2.0 ATR', dict(q=dict(tp=2.0))), ('TP1 2.5 ATR', dict(q=dict(tp=2.5))),
         ('Max SL1 cap OFF', dict(q=dict(cap=1e9))), ('Max TP1 cap OFF', dict(q=dict(tcap=1e9))), ('Trail 3.5 ATR', dict(q=dict(tr=3.5))), ('Breakeven OFF', dict(q=dict(be=False))),
         ('CHOP > 58 block', dict(F=dict(chop=58))), ('ADX < 20 block', dict(F=dict(adx=20))), ('Crosses >= 4 block', dict(F=dict(xs=4))), ('HTF flips >= 3 in 8 block', dict(F=dict(fl=3))), ('Environment EMA200 vs VWAP', dict(F=dict(env=True))),
         ('ER 0.18', dict(F=dict(er=.18))), ('ER 0.30', dict(F=dict(er=.30)))]
bo = dict(slope=best) if best else {}
R2 = [(nm, run(dict(bo, **o))) for nm, o in IDEAS]; log('ideas')
out += table('2. Ideas on top of %s' % ('slope %.2f' % best if best else 'v10.97'), B1, R2)
# greedy combine: add the best qualifying idea (z >= 1, all thirds better, last 4 wk >= 0) until none qualifies
cur = dict(bo); curr = B1; picked = []; pool = list(IDEAS)
def merge(a, b):
    m = dict(a)
    for k, v in b.items():
        m[k] = dict(m.get(k, {}), **v) if isinstance(v, dict) else v
    return m
for step in range(5):
    best_c = None
    for nm, o in pool:
        cand = merge(cur, o); a = run(cand); z, d_, l4, vd = cmp(a, curr)
        if z >= 1 and all(t > 0 for t in d_) and l4 >= 0 and (best_c is None or a['net'] > best_c[2]['net']): best_c = (nm, cand, a)
    if not best_c: break
    picked.append(best_c[0]); cur, curr = best_c[1], best_c[2]; pool = [p for p in pool if p[0] != best_c[0]]; log('pick %s' % best_c[0])
out += table('3. Final set vs v10.97: %s' % (' + '.join((['slope %.2f' % best] if best else []) + picked) or 'none'), V0, [('final', curr)] + ([('slope only', B1)] if best else []))
HR = [18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
out += table('4. One-hour blocks on top of the final set', curr, [('block %02d:00-%02d:00' % (h, (h + 1) % 24), run(merge(cur, dict(hb=(h,))))) for h in HR]); log('hours')
out += ['## 5. Sessions (final vs v10.97)', '', '| Session | v10.97 trades / net | final trades / net |', '|---|---|---|'] + ['| %s | %d / %+.0f | %d / %+.0f |' % (k, *V0['ses'][k], *curr['ses'][k]) for k in V0['ses']] + ['']
out += ['FINAL_SET %s %s' % (sym, repr(cur))]
open('two_%s_report.md' % sym.lower(), 'w').write('\n'.join(out)); print('\n'.join(out))
