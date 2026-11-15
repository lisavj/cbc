import sys
exec(open('all_eng117.py').read())
setup('MGC'); b = run({})
def show(nm, a):
    z, d_, l4, vd = cmp(a, b); print('| %s | %d | %+.0f | %+.0f | %+.1f | %s | %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['net'] - b['net'], z, ' / '.join('%+.0f' % t for t in d_), l4, a['dd'], vd), flush=True)
print('Base: %d trades, net %+.0f, DD %.0f' % (b['n'], b['net'], b['dd']))
V = [('Range gate 3 ATR', dict(rg=3)), ('Range gate 4.5 ATR', dict(rg=4.5)),
     ('Late-away 3 pts', dict(P=dict(tw=3.0))), ('Late-away 1.5 pts', dict(P=dict(tw=1.5))),
     ('Lookback 4 bars (12 min) 0.11', dict(slk=4, slope=.11)), ('Lookback 6 bars (18 min) 0.15', dict(slk=6, slope=.15)), ('Lookback 5 bars 0.15', dict(slk=5, slope=.15)), ('Lookback 5 bars 0.165', dict(slk=5, slope=.165)),
     ('Range gate OFF + lookback 5 bars 0.138', dict(rg=0, slk=5, slope=.138)), ('Range gate OFF + lookback 5 bars 0.15', dict(rg=0, slk=5, slope=.15)),
     ('Range gate OFF + late-away 2', dict(rg=0, P=dict(tw=2.0))), ('Lookback 5 bars 0.138 + late-away 2', dict(slk=5, slope=.138, P=dict(tw=2.0))),
     ('Range gate OFF + lookback 5 0.138 + late-away 2', dict(rg=0, slk=5, slope=.138, P=dict(tw=2.0)))]
for nm, o in V: show(nm, run(o))
