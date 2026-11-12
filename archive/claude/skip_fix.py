import pickle, numpy as np, collections as C
from skip_why import guard2
D = pickle.load(open('skip_why.pkl', 'rb'))
def regime(b, nsess=5):
    order = []; net = C.OrderedDict()
    for t in sorted(b, key=lambda t: t['i']): net[t['ss']] = net.get(t['ss'], 0) + t['n']
    ks = list(net); act = {}
    for k_, s in enumerate(ks): act[s] = sum(net[x] for x in ks[max(0, k_ - nsess):k_]) < 0
    return act
def variants(tf, b):
    V = {}
    V['current exits'] = b
    V['filter only (no guard)'] = tf
    V['A. guard per 18-18 session (the 11/08 rule)'] = guard2(tf, 2, 2)[0]
    for k in (3,):
        V['B. looser: %d losses or %d flip-outs, per session' % (k, k)] = guard2(tf, k, k)[0]
    V['C. guard resets at 03:00 and 09:30 (Asia / London / NY separately)'] = guard2(tf, 2, 2, mode='sub')[0]
    for p, lab in ((20, '1 h'), (40, '2 h')):
        V['D. pause %s after 2 losses / 2 flip-outs, then reset' % lab] = guard2(tf, 2, 2, mode='pause', pause=p)[0]
    for ns in (3, 5, 10):
        act = regime(b, ns)
        g = guard2(tf, 2, 2)[0]; gi = {t['i'] for t in g}
        V['E. guard only when the previous %d sessions lost (else take all)' % ns] = [t for t in tf if (t['i'] in gi) or not act[t['ss']]]
    act = regime(b, 5); g = guard2(tf, 2, 2, mode='sub')[0]; gi = {t['i'] for t in g}
    V['F. = C + E5 (sub-session guard, only after 5 losing sessions)'] = [t for t in tf if (t['i'] in gi) or not act[t['ss']]]
    return V
def row(v, b):
    ab = np.mean([t['n'] for t in b]); out = []
    for P in (lambda t: t['th'] == 0, lambda t: t['th'] == 1, lambda t: t['th'] == 2, lambda t: t['l4'], lambda t: True):
        n1 = sum(t['n'] for t in v if P(t)); n0 = sum(t['n'] for t in b if P(t)); c1 = sum(1 for t in v if P(t)); c0 = sum(1 for t in b if P(t))
        out.append((n1, n1 - n0 + (c0 - c1) * ab, c1))
    return out
L = ['# Why the session-guard rule lags in the last 4 weeks — MES 3m and MGC 3m — 11/08/2026', '']
for sym in ('MES', 'MGC'):
    X = D[sym]; b = X['runs'][None]
    for flab, f in (('skip shorts above... below the 5-day EMA', ('d5', 'S')), ('no trend filter', None)):
        tf = X['runs'][f]
        L += ['## %s — %s' % (X['nm'], flab), '', 'Net after costs (beyond random skipping in brackets). Trades in the last column.', '',
              '| Variant | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades |', '|---|---|---|---|---|---|---|']
        for k, v in variants(tf, b).items():
            if f is None and k.startswith('filter only'): continue
            rr = row(v, b)
            L.append('| %s | %s | %d |' % (k, ' | '.join('%+.0f (%+.0f)' % (a, x) for a, x, _ in rr), rr[-1][2]))
        L.append('')
open('skip_fix.md', 'w').write('\n'.join(L)); print('\n'.join(L))
