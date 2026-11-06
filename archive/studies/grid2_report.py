import pickle
XS = list(range(12, 46, 3)); YS = [y / 100 for y in range(50, 91, 5)]
out = ['# Time-based TP1 reduction — fine grid (X 12–45 min by 3, Y 50–90 % by 5) — 11/06/2026', '',
       'Replay Jan 5 → Nov 5, live settings (see tptime_study.py). Cell = Δ net pts vs current exits. Flags: T = better in all three thirds,',
       '4 = better in the last 4 weeks, R = T and all four neighbours (±3 min, ±5 %) also better overall. Bold = T + 4 + R.', '']
for sym, nm in (('MES', 'MES 3m'), ('MGC', 'MGC 3m')):
    bn, res = pickle.load(open('grid2_%s.pkl' % sym, 'rb'))
    for mode, mn in (('A', 'A. Modified TP limit'), ('B', 'B. Close at candle close')):
        out += ['## %s — %s (current net %+.0f)' % (nm, mn, bn), '', '| X min \\ Y | ' + ' | '.join('%d%%' % round(y * 100) for y in YS) + ' |', '|---|' + '---|' * len(YS)]
        cnt = {'T': 0, 'T4': 0, 'R': 0, 'pos': 0}; best = []
        for xi, x in enumerate(XS):
            cells = []
            for yi, y in enumerate(YS):
                d, dth, d4 = res[(mode, x, y)]
                t = all(k > 0 for k in dth); f = d4 > 0
                nb = [res[(mode, XS[a], YS[b])][0] for a, b in ((xi - 1, yi), (xi + 1, yi), (xi, yi - 1), (xi, yi + 1)) if 0 <= a < len(XS) and 0 <= b < len(YS)]
                r = t and d > 0 and all(v > 0 for v in nb)
                cnt['pos'] += d > 0; cnt['T'] += t; cnt['T4'] += t and f; cnt['R'] += r
                c = '%+.0f%s' % (d, (' ' + ''.join(k for k, v in (('T', t), ('4', f), ('R', r)) if v)) if (t or f or r) else '')
                cells.append('**%s**' % c if t and f and r else c)
                best.append((d, x, y, dth, d4, t, f, r))
            out.append('| %d | %s |' % (x, ' | '.join(cells)))
        best.sort(key=lambda k: -k[0])
        out += ['', 'Cells %d · positive %d · T %d · T+4 %d · R %d. Best: %s.' % (len(XS) * len(YS), cnt['pos'], cnt['T'], cnt['T4'], cnt['R'],
                '; '.join('X %d / Y %d%% %+.0f (thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f)' % (x, round(y * 100), d, *dt, d4) for d, x, y, dt, d4, *_ in best[:3])), '']
print('\n'.join(out))
