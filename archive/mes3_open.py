exec(open('all_eng.py').read())
setup('MES'); b = run({})
def show(nm, a):
    z, d_, l4, vd = cmp(a, b); print('%-46s %d %+.0f thirds %s l4 %+.0f dd %.0f | %+.0f z %+.1f chg %s l4chg %+.0f %s' % (nm, a['n'], a['net'], [round(t) for t in a['th']], a['l4'], a['dd'], a['net'] - b['net'], z, [round(t) for t in d_], l4, vd), flush=True)
show('MES 3m v1.13 base', b)
for nm, o in [('No new setups 16:00-19:00', dict(P=dict(qwin=(960, 1140)))), ('End setups at 16:00 OFF', dict(P=dict(eod=False))), ('both', dict(P=dict(qwin=(960, 1140), eod=False))),
              ('ATR length 15', dict(P=dict(atrn=15))), ('ATR 15 + both', dict(P=dict(qwin=(960, 1140), eod=False, atrn=15))),
              ('window 16:00-18:30 (neighbour)', dict(P=dict(qwin=(960, 1110)))), ('window 16:00-19:30 (neighbour)', dict(P=dict(qwin=(960, 1170)))), ('window 16:00-20:00', dict(P=dict(qwin=(960, 1200))))]:
    show(nm, run(o))
