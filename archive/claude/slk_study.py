# Slope lookback in chart bars (36 min = 18 bars on 2m, 7 bars = 35 min on 5m) -- 11/15/2026
import sys
eng_f, tf, sym = sys.argv[1], sys.argv[2], sys.argv[3]
exec(open(eng_f).read()); setup(sym)
if sym == 'MES' and tf == '3': CFGX['base'] = dict(CFGX['base'], P=dict(qwin=(960, 1140), eod=False))
b = run({}); base = CFGX['base'].get('slope', 0)
Ls = {'2': (12, 15, 18, 21), '5': (6, 7, 8, 12), '3': (8, 10, 12, 14)}[tf] if len(sys.argv) < 5 else tuple(int(x) for x in sys.argv[4].split(','))
rows = []
sl0 = base if base else {'MNQ': .55}.get(sym, .5)
for L in Ls:
    for f in (.8, .9, 1.0, 1.1, 1.2, 1.35):
        t = round(sl0 * L / 12 * f, 3)
        if L == 12 and f == 1.0 and base: continue
        rows.append(('lookback %d bars (%d min), slope >= %.3f' % (L, L * int(tf), t), run(dict(slope=t, slk=L)))); print(rows[-1][0], file=sys.stderr, flush=True)
out = table('%s %sm: slope lookback (base = 12 bars, slope %s)' % (sym, tf, base or 'off'), b, rows)
print('\n'.join(out))
