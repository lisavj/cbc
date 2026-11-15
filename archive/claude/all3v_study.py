import sys
exec(open('all_eng117.py').read())
log = lambda m: print(m, file=sys.stderr, flush=True)
def V(sym):
    b = CH[sym]['base']; q = CH[sym]['q']
    v = [('③ CHOP > 61.8 block', dict(F=dict(chop=61.8))), ('③ CHOP > 58 block', dict(F=dict(chop=58))), ('③ ADX < 20 block', dict(F=dict(adx=20))), ('③ ADX < 15 block', dict(F=dict(adx=15))),
         ('③ EMA20/VWAP crosses >= 4 block', dict(F=dict(xs=4))), ('③ crosses >= 6 block', dict(F=dict(xs=6))), ('③ N-bar range < 2 ATR block', dict(F=dict(rng=2))), ('③ N-bar range < 3 ATR block', dict(F=dict(rng=3))),
         ('③ HTF flips >= 2 in 8 block', dict(F=dict(fl=2))), ('③ HTF flips >= 3 in 8 block', dict(F=dict(fl=3))), ('③ HTF flips >= 4 in 8 block', dict(F=dict(fl=4))),
         ('③ Skip non-flip setups from 6 HTF candles after flip', dict(F=dict(fa=6))), ('③ ... from 9', dict(F=dict(fa=9))), ('③ ... from 12', dict(F=dict(fa=12))),
         ('③ Block if VWAP -3 / +2 pts', dict(F=dict(nv=(3, 2)))), ('③ Block if EMA200 -3 / +2 pts', dict(F=dict(ne=(3, 2)))), ('③ Environment EMA200 vs VWAP', dict(F=dict(env=True))),
         ('③ Skip while ATR > 1.8 x ATR(100)', dict(F=dict(va=1.8))), ('③ Skip if SL1 cap < 1.5 ATR', dict(F=dict(vc=1.5))),
         ('③ ER 0.18', dict(F=dict(er=.18))), ('③ ER 0.20', dict(F=dict(er=.20))), ('③ ER 0.26', dict(F=dict(er=.26))), ('③ ER 0.30', dict(F=dict(er=.30))), ('③ ER filter OFF', dict(F=dict(er=0.0))),
         ('③ ER breakout exception OFF', dict(F=dict(bo=False))),
         ('③ Range gate 4 ATR', dict(rg=4)), ('③ Range gate 6 ATR', dict(rg=6)), ('③ Range gate zone 30 %', dict(rg=b.get('rg') or 5, rz=.3)), ('③ Range gate ' + ('OFF' if b.get('rg') else 'ON 5 ATR'), dict(rg=0 if b.get('rg') else 5)),
         ('③ VWAP stretch 3 ATR', dict(x4=3)), ('③ VWAP stretch 6 ATR', dict(x4=6)), ('③ VWAP stretch ' + ('OFF' if b.get('x4') else 'ON 4 ATR'), dict(x4=0 if b.get('x4') else 4)),
         ('① Flip min ER 0.15', dict(fer=.15)), ('① Flip min ER 0.30', dict(fer=.30)), ('① Toward late-away 1 pt (instead of strict)', dict(P=dict(tw=1.0))),
         ('① SL1 x 1.5 ATR', dict(q=dict(sl=1.5))), ('① SL1 x 2.0', dict(q=dict(sl=2.0))), ('① SL1 x 2.5', dict(q=dict(sl=2.5))), ('① SL1 x 3.0', dict(q=dict(sl=3.0))), ('① SL1 x 3.5', dict(q=dict(sl=3.5))),
         ('① TP1 x 1.25 ATR', dict(q=dict(tp=1.25))), ('① TP1 x 1.5', dict(q=dict(tp=1.5))), ('① TP1 x 1.75', dict(q=dict(tp=1.75))), ('① TP1 x 2.0', dict(q=dict(tp=2.0))), ('① TP1 x 2.5', dict(q=dict(tp=2.5))),
         ('① Close at TP1 0 %', dict(q=dict(part=0.0))), ('① Close at TP1 50 %', dict(q=dict(part=.5))), ('① Close at TP1 80 %', dict(q=dict(part=.8))), ('① Close at TP1 100 %', dict(q=dict(part=1.0))),
         ('① Breakeven at TP1 OFF', dict(q=dict(be=False))), ('① Trail 1.3 ATR', dict(q=dict(tr=1.3))), ('① Trail 1.7 ATR', dict(q=dict(tr=1.7))), ('① Trail 2.5 ATR', dict(q=dict(tr=2.5))), ('① Trail 3.5 ATR', dict(q=dict(tr=3.5))), ('① No trail', dict(q=dict(tr=0))),
         ('① Min SL x 0.6', dict(q=dict(mn=q['mn'] * .6))), ('① Min SL x 1.4', dict(q=dict(mn=q['mn'] * 1.4))), ('① Max SL1 cap OFF', dict(q=dict(cap=1e9))), ('① Max TP1 cap OFF', dict(q=dict(tcap=1e9))),
         ('① Time stop 10 candles (< 0.5 ATR progress)', dict(q=dict(ts=10))), ('① Time stop 20 candles', dict(q=dict(ts=20)))]
    if b.get('ride'): v.append(('① Flip ride OFF (flip setups use TP1)', dict(ride=False)))
    else: v.append(('① Flip ride ON', dict(ride=True)))
    if sym == 'MGC': v += [('① Flip distance floor 10 pts', dict(P=dict(fdp=10.))), ('① Toward late-away strict (0)', dict(P=dict(tw=None))), ('① Toward late-away 2 pts', dict(P=dict(tw=2.0)))]
    if sym == 'MES': v += [('① 13:00-15:00 block OFF', dict(hb=())), ('① Block 13:00-14:00 only', dict(hb=(13,))), ('① No new setups to 18:45 (window as v10.97)', dict(P=dict(qwin=(960, 1125)))), ('① End setups at 16:00 ON', dict(P=dict(eod=True))), ('① Toward late-away 1 pt', dict(P=dict(tw=1.0))), ('① Skip setups against MTF (60m) CBC', dict(P=dict(mtf=True)))]
    bs = b['slope']
    v += [('③ Slope %.2f' % (bs * f), dict(slope=round(bs * f, 3))) for f in (.8, .9, 1.1, 1.2)]
    v += [('③ Slope lookback %d bars (%d min), slope %.3f' % (L, 3 * L, bs * L / 12 * f), dict(slk=L, slope=round(bs * L / 12 * f, 3))) for L in (5, 10, 15) for f in (.9, 1.0, 1.1)]
    v += [('② LTF pierce late window 0', dict(P=dict(llate=0))), ('② LTF pierce late window 2', dict(P=dict(llate=2))), ('② HTF pierce late window 0', dict(P=dict(hlate=0))), ('② HTF pierce late window 2', dict(P=dict(hlate=2))),
          ('② HTF late trade-colour OFF', dict(P=dict(hcol=False))), ('② HTF pierce replaces current setup', dict(P=dict(hrep=True))), ('② HTF pierce requires close beyond LTF EMA9/20', dict(P=dict(hreq=True))),
          ('② Flip: require pullback first (wait 10)', dict(P=dict(fpb=10))),
          ('② Trigger HTF CBC Flip OFF', dict(P=dict(t_flip=False))), ('② Trigger LTF EMA20 Pierce OFF', dict(P=dict(t_ltf=False))), ('② Trigger HTF EMA9 Pierce OFF', dict(P=dict(t_h9=False))), ('② Trigger HTF EMA20 Pierce OFF', dict(P=dict(t_h20=False))),
          ('① Flip distance 1.5 ATR', dict(P=dict(fdx=1.5))), ('① Flip distance 3 ATR', dict(P=dict(fdx=3.0))), ('① Flip side gate OFF', dict(P=dict(side=-1e9))), ('① Flip side gate 2 pts', dict(P=dict(side=2.0))),
          ('① Flip VWAP slope OFF', dict(P=dict(vws=False))), ('① HTF pierce min ER 0', dict(P=dict(erh=0.0))), ('① HTF pierce min ER 0.23', dict(P=dict(erh=.23))),
          ('① LTF pierce min ER 0.12', dict(erl=.12)), ('① LTF pierce min ER 0.15', dict(erl=.15)), ('① LTF pierce min ER 0.23', dict(erl=.23)),
          ('① VWAP reclaim block OFF', dict(P=dict(vwbn=-1))), ('① VWAP reclaim block 8', dict(P=dict(vwbn=8))), ('① Min candles between setups 5', dict(P=dict(cool=5))), ('① Min candles 15', dict(P=dict(cool=15))),
          ('① ATR length 10', dict(P=dict(atrn=10))), ('① ATR length 20', dict(P=dict(atrn=20))), ('① No new setups 16:00-19:00', dict(P=dict(qwin=(960, 1140)))), ('① No-new-setup window OFF', dict(P=dict(qwin=(None, None)))),
          ('① OR forming blocks all OFF', dict(P=dict(orny=False, orln=False, oras=False))), ('① End setups at 16:00 OFF', dict(P=dict(eod=False)))]
    return v
out = ['# ①②③ inputs check -- MES / MGC 3m on v1.17 settings -- 11/15/2026', '',
       'Replay Jan 5 -> Nov 13, one change at a time on each chart\'s v1.17 settings (MES 3m: slope 0.42, LTF ER 0.15, range gate 5, flip ride, SL1 3 ATR no cap, TP1 1.75 ATR, 100 % at TP1, BE, strict away, 13-15 block, no setups 16:00-19:00, End 16:00 OFF; MGC 3m: slope 0.30, range gate 5, stretch 4, FLIP 0 %, SL1 1.7 cap 7, TP1 1.7 cap 6, toward late-away 1 pt), net after costs (MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35). ', '']
top = ['## Candidates (promising or better)', '']
for sym in sys.argv[1:]:
    setup(sym); b = run({}); rows = []
    for nm, o in V(sym):
        try: a = run(o)
        except Exception as e: log('%s %s ERR %s' % (sym, nm, e)); continue
        rows.append((nm, a)); z, d_, l4, vd = cmp(a, b)
        if vd in ('robust', 'robust except last 4 wk', 'promising'): top.append('- %s 3m: %s -> %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, max DD %.0f vs %.0f (%s)' % (sym, nm, a['net'] - b['net'], z, *d_, l4, a['dd'], b['dd'], vd))
    log('%s done' % sym)
    out += table('%s 3m (v1.17)' % sym, b, rows)
if len(top) == 2: top.append('- none')
rep = '\n'.join(out[:3] + top + [''] + out[3:]); open('all3v_%s.md' % sys.argv[1], 'w').write(rep); print(rep)
