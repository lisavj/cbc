exec(open('all_eng.py').read())
o = []
setup('MNQ'); b = run({})
o += table('MNQ 3m Max SL1 cap neighbours (live 30 pts)', b, [('cap %d' % c, run(dict(q=dict(cap=c)))) for c in (20, 25, 35, 40, 50, 60, 80)] + [('cap OFF', run(dict(q=dict(cap=1e9))))])
setup('M2K'); b = run({})
o += table('M2K 3m cap / close-at-TP1 neighbours (live cap 5, 80 %)', b, [('cap %g' % c, run(dict(q=dict(cap=c)))) for c in (4, 6, 7, 8)] + [('cap OFF', run(dict(q=dict(cap=1e9)))), ('close 0 % + cap OFF', run(dict(q=dict(part=0.0, cap=1e9)))), ('close 0 % + no trail', run(dict(q=dict(part=0.0, tr=0)))), ('close 25 %', run(dict(q=dict(part=.25))))])
setup('MGC'); b = run({})
o += table('MGC 3m range gate neighbours (live 5 ATR / 20 %)', b, [('gate 3.5', run(dict(rg=3.5))), ('gate 4', run(dict(rg=4))), ('gate 4.5', run(dict(rg=4.5))), ('gate 4 + zone 30 %', run(dict(rg=4, rz=.3)))])
open('all_nb_report.md', 'w').write('\n'.join(o)); print('\n'.join(o))
