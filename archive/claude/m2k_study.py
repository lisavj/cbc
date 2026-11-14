import sys
exec(open('m2k_eng.py').read())
log = lambda m: print(m, file=sys.stderr, flush=True)
out = ['# M2K 3m -- CBC EMA Slope branch studies -- 11/14/2026', '',
       'Replay Jan 5 -> Nov 13 (BarFeed / Databento M2K 3m, TV EMA20), net after 0.35 pts cost per trade. v10.97 M2K 3m settings: ER 0.23 + breakout 3, no range gate, no VWAP stretch, toward late-away 1 pt (global; M2K not in the per-symbol list), flip distance 2 ATR (M2K not in the pts list), SL1 1.7 ATR min 3 cap 5, TP1 1.7 ATR cap 3, 80 % at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. One change at a time unless stated. In-sample: compare variants, not totals.', '']
V0 = run({}); log('base %d %.0f' % (V0['n'], V0['net']))
out += ['## 0. v10.97 baseline by trigger and session', '', 'Trades %d, net %+.0f, avg %+.2f, win %.0f %%, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f' % (V0['n'], V0['net'], V0['avg'], V0['w'], *V0['th'], V0['l4'], V0['dd']), '',
        'By trigger: ' + ' · '.join('%s %d / %+.0f' % (k, *v) for k, v in V0['bt'].items()), '', 'By session: ' + ' · '.join('%s %d / %+.0f' % (k, *v) for k, v in V0['ses'].items()), '']
# 1. slope grid
SL = [0.2, 0.24, 0.3, 0.36, 0.42, 0.48, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9, 1.0]
S = {t: run(dict(slope=t)) for t in SL}; log('slope done')
out += table('1. HTF EMA20 slope filter threshold (vs v10.97 = off)', V0, [('slope %.2f' % t, S[t]) for t in SL])
best = max(SL, key=lambda t: S[t]['net']); log('best slope %.2f' % best)
# 2. other branch ideas on v10.97 and on best slope
IDEAS = [('Flip setups ride to HTF flip back (no TP1)', dict(ride=True)), ('Range gate 24 / 20 % / 5 ATR', dict(rg=5)), ('Toward late-away OFF (strict away)', dict(P=dict(tw=None))), ('VWAP stretch 4 ATR', dict(x4=4)),
         ('LTF pierce min ER 0.12', dict(erl=.12)), ('LTF pierce min ER 0.15', dict(erl=.15)), ('LTF pierce min ER 0.20', dict(erl=.20)), ('LTF pierce min ER 0.23', dict(erl=.23)),
         ('100 % at TP1', dict(q=dict(part=1.0))), ('0 % at TP1, BE, closed by HTF flip (FLIP 0 %)', dict(q=dict(part=0.0, tr=0))), ('50 % at TP1 + BE + trail 1.7', dict(q=dict(part=.5))),
         ('End setups at 16:00 OFF', dict(P=dict(eod=False))), ('Trigger HTF EMA9 Pierce OFF', dict(P=dict(t_h9=False))), ('Trigger HTF EMA20 Pierce OFF', dict(P=dict(t_h20=False))),
         ('Trigger HTF CBC Flip OFF', dict(P=dict(t_flip=False))), ('Trigger LTF EMA20 Pierce OFF', dict(P=dict(t_ltf=False)))]
out += table('2a. Branch ideas, one at a time on v10.97', V0, [(nm, run(o)) for nm, o in IDEAS]); log('2a done')
B1 = S[best]
out += table('2b. Same ideas on top of slope %.2f' % best, B1, [(nm, run(dict(o, slope=best))) for nm, o in IDEAS]); log('2b done')
# 3. hour blocks on best slope
HR = [18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
out += table('3. One-hour no-new-setup blocks on top of slope %.2f' % best, B1, [('block %02d:00-%02d:00' % (h, (h + 1) % 24), run(dict(slope=best, hb=(h,)))) for h in HR]); log('3 done')
out += ['## 4. Sessions (slope %.2f vs v10.97)' % best, '', '| Session | v10.97 trades / net | slope %.2f trades / net |' % best, '|---|---|---|'] + ['| %s | %d / %+.0f | %d / %+.0f |' % (k, *V0['ses'][k], *B1['ses'][k]) for k in V0['ses']] + ['']
open('m2k_report.md', 'w').write('\n'.join(out)); print('\n'.join(out))
