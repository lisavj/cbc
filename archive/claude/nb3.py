import sys
exec(open('all_eng117.py').read())
sym = sys.argv[1]; setup(sym); b = run({})
def show(nm, a):
    z, d_, l4, vd = cmp(a, b); print('| %s | %d | %+.0f | %+.0f | %+.1f | %s | %+.0f | %.0f | %s |' % (nm, a['n'], a['net'], a['net'] - b['net'], z, ' / '.join('%+.0f' % t for t in d_), l4, a['dd'], vd), flush=True)
print('Base %s: %d trades, net %+.0f, DD %.0f' % (sym, b['n'], b['net'], b['dd']))
V = {'MNQ': [('OR block OFF: NY only', dict(P=dict(orny=False))), ('OR block OFF: London only', dict(P=dict(orln=False))), ('OR block OFF: Asia only', dict(P=dict(oras=False))),
             ('OR blocks OFF NY + London', dict(P=dict(orny=False, orln=False))),
             ('SL1 cap 45', dict(q=dict(cap=45))), ('SL1 cap 60', dict(q=dict(cap=60))), ('SL1 cap 90', dict(q=dict(cap=90))),
             ('cap OFF + OR blocks OFF', dict(q=dict(cap=1e9), P=dict(orny=False, orln=False, oras=False)))],
     'M2K': [('Close at TP1 25 %', dict(q=dict(part=.25))), ('Close at TP1 0 % no trail', dict(q=dict(part=0., tr=0))), ('SL1 x 3.0', dict(q=dict(sl=3.0))), ('SL1 x 4.0', dict(q=dict(sl=4.0))), ('SL1 x 3.5 + TP1 0 %', dict(q=dict(sl=3.5, part=0.)))]}[sym]
for nm, o in V: show(nm, run(o))
