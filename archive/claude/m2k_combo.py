exec(open('m2k_eng.py').read())
V0 = run({})
C = [('slope 0.60 + stretch 4 + LTF ER 0.23', dict(slope=.6, x4=4, erl=.23)), ('slope 0.60 + stretch 4 + LTF ER 0.23 + strict away', dict(slope=.6, x4=4, erl=.23, P=dict(tw=None))),
     ('slope 0.90 + stretch 4', dict(slope=.9, x4=4)), ('slope 0.90 + stretch 4 + LTF ER 0.23', dict(slope=.9, x4=4, erl=.23)), ('slope 0.90 + stretch 4 + LTF ER 0.23 + flip OFF', dict(slope=.9, x4=4, erl=.23, P=dict(t_flip=False))),
     ('slope 0.48 + stretch 4 + LTF ER 0.23 + strict away', dict(slope=.48, x4=4, erl=.23, P=dict(tw=None))), ('slope 0.75 + stretch 4 + LTF ER 0.23 + strict away', dict(slope=.75, x4=4, erl=.23, P=dict(tw=None))),
     ('slope 0.75 + stretch 3 + LTF ER 0.23 + strict away', dict(slope=.75, x4=3, erl=.23, P=dict(tw=None))), ('slope 0.75 + stretch 4 + LTF ER 0.23 + strict + 100 % at TP1', dict(slope=.75, x4=4, erl=.23, P=dict(tw=None), q=dict(part=1.0)))]
o = table('2c. M2K 3m combinations vs v10.97', V0, [(nm, run(p)) for nm, p in C])
open('m2k_combo_report.md', 'w').write('\n'.join(o)); print('\n'.join(o))
