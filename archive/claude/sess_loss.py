"""Stop after K losses in a row, counted separately in each sub-session (Asia 18:00-03:00, London 03:00-09:30, NY 09:30-16:00 ET),
each with its own K (0 = no stop). Only trades that already ended count; losses = after costs. MES 3m and MGC 3m. 11/08/2026."""
import pickle, itertools, numpy as np
D = pickle.load(open('skip_why.pkl', 'rb'))
SUBS = ['Asia 18-03', 'London 03-09:30', 'NY 09:30-16']; KS = [0, 1, 2, 3, 4]
def guard(r, Ks, total=False):
    keep = []; stop = set(); streak = {}
    for t in sorted(r, key=lambda t: t['i']):
        key = (t['ss'], t['sub']); K = Ks[SUBS.index(t['sub'])] if t['sub'] in SUBS else 0
        if not K: keep.append(t); continue
        if key in stop: continue
        fin = sorted([u for u in keep if (u['ss'], u['sub']) == key and u['j'] < t['i']], key=lambda u: u['j'])
        ls_ = 0
        for u in fin: ls_ = ls_ + 1 if u['n'] < 0 else 0
        if ls_ >= K: stop.add(key); continue
        keep.append(t)
    return keep
PER = [('Third 1', lambda t: t['th'] == 0), ('Third 2', lambda t: t['th'] == 1), ('Third 3', lambda t: t['th'] == 2), ('Last 4 wk', lambda t: t['l4']), ('Whole', lambda t: True)]
def ev(v, b):
    ab = np.mean([t['n'] for t in b]); o = []
    for _, P in PER:
        n1 = sum(t['n'] for t in v if P(t)); n0 = sum(t['n'] for t in b if P(t)); c1 = sum(1 for t in v if P(t)); c0 = sum(1 for t in b if P(t))
        o.append((n1, n1 - n0 + (c0 - c1) * ab))
    return o, len(v)
def kn(Ks): return ', '.join('%s %s' % (s.split()[0], k if k else 'off') for s, k in zip(SUBS, Ks))
L = [__doc__, '', 'Cells: net after costs (beyond random skipping). ✓ = beyond random positive in all three thirds; ★ = ✓ and last 4 weeks not worse than current.', '']
for sym in ('MES', 'MGC'):
    X = D[sym]; b = X['runs'][None]
    for flab, f in (('no trend filter', None),) + ((('with 5-day EMA short filter', ('d5', 'S')),) if sym == 'MES' else ()):
        tf = X['runs'][f]; res = {}
        for Ks in itertools.product(KS, repeat=3): res[Ks] = ev(guard(tf, Ks), b)
        base = res[(0, 0, 0)][0]
        def mark(Ks):
            o = res[Ks][0]; ok = all(o[k][1] > 0 for k in range(3)); return ('★' if ok and o[3][0] >= ev(b, b)[0][3][0] - 1e-9 else '✓') if ok else ''
        def line(Ks):
            o, n = res[Ks]; return '| %s | %s | %d | %s |' % (kn(Ks), ' | '.join('%+.0f (%+.0f)' % x for x in o), n, mark(Ks))
        hdr = ['| Stop after K losses in a row | ' + ' | '.join(p for p, _ in PER) + ' | Trades | |', '|---|' + '---|' * (len(PER) + 2)]
        cur = ev(b, b)[0]
        L += ['## %s — %s' % (X['nm'], flab), '', 'Current exits: ' + ', '.join('%s %+.0f' % (p, cur[k][0]) for k, (p, _) in enumerate(PER)), '',
              '**One sub-session at a time** (the others off)', ''] + hdr
        for si in range(3):
            for k in KS[1:]:
                Ks = tuple(k if j == si else 0 for j in range(3)); L.append(line(Ks))
        L += ['', '**Same K in all three sub-sessions**', ''] + hdr + [line((k, k, k)) for k in KS[1:]]
        good = sorted([K for K in res if mark(K)], key=lambda K: -res[K][0][4][1])
        L += ['', '**Best combinations (beyond random positive in all three thirds), top 10 by whole-period beyond random** — %d of 124 qualify' % len(good), ''] + hdr + [line(K) for K in good[:10]]
        top = sorted([K for K in res if K != (0, 0, 0)], key=lambda K: -res[K][0][4][1])[:5]
        L += ['', '**Top 5 by whole-period beyond random (any)**', ''] + hdr + [line(K) for K in top]
        pick = max([K for K in res if K != (0, 0, 0)], key=lambda K: res[K][0][0][1] + res[K][0][1][1])
        l3 = sorted(res[K][0][2][1] for K in res if K != (0, 0, 0))
        L += ['', 'Walk-forward: best on thirds 1-2 = **%s** → third 3 beyond random **%+.0f** (rank %d of 124; median %+.0f).' % (
            kn(pick), res[pick][0][2][1], sum(1 for v in l3 if v > res[pick][0][2][1]) + 1, l3[62]), '']
open('sess_loss_report.md', 'w').write('\n'.join(L)); print('\n'.join(L))
