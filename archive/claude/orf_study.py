#!/usr/bin/env python3
"""Opening-range block study -- 11/01/2026 (11/08: MGC 2m range gate ON as live since v10.77).

Question: CBC v9.60+ "No new setups during opening range (forming)" is ON for NY (9:30-10:00 ET), London (3:00-3:30) and
Asia (20:00-20:30). Is it helping? Replay with the block per session ON (current) vs OFF, per chart on its live settings
(MES 3m range gate; MGC 3m range gate + VWAP stretch 4; MGC 2m range gate; MES 2m 1H MTF gate; 5m no gates; base exits; chart / HTF EMAs 9 / 20).
Engine: chop_sim_or.py = chop_sim.py with the OR-window skip replaced by a label (otherwise identical; with every block ON it
reproduces chop_sim). A blocked setup is not just removed: the setups after it can change (cooldown, one open setup at a time).
Also lists the setups the block removes (window setups when it is OFF) and the live alerts in the windows.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 orf_study.py
"""
import re, json, collections, datetime as D, numpy as np
import chop_sim_or as cs, stretch_study as ss

ss.FROM[5] = '2026-01-05'
CHARTS = [('MES', 3, dict(R5=1, X4=0, MTF=0)), ('MGC', 3, dict(R5=1, X4=1, MTF=0)), ('MES', 2, dict(R5=0, X4=0, MTF=1)),
          ('MGC', 2, dict(R5=1, X4=0, MTF=0)), ('MES', 5, dict(R5=0, X4=0, MTF=0)), ('MGC', 5, dict(R5=0, X4=0, MTF=0))]
ALL = {'NY', 'London', 'Asia'}


def run(s, G, blocked):
    return s.run(lambda d: cs.cur_rule(d) and d['orw'] not in blocked, q=ss.QB[s.sym], gates=G)


def st(res, s, tf):
    v = [r['res'] for r in res]; w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
    return dict(n=len(v), net=sum(v), wr=100 * w / max(1, w + l), sd=float(np.std(v)) or 1, th=ss.thirds(res, s.month, tf))


def main():
    out = ['# Opening-range block study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    hdr = ['| Variant | Setups | Win % | Net | Δ vs current | z | Δ by third | Verdict |', '|---|---|---|---|---|---|---|---|']
    for sym, tf, G in CHARTS:
        s = cs.Case(sym, tf, ss.load(sym, tf))
        cur = run(s, G, ALL); b = st(cur, s, tf); C0 = {(r['i'], r['lg']) for r in cur}
        tn = 'Jan–Mar / Apr–Jun / Jul–Oct' if tf != 2 else 'Jun–Jul / Aug / Sep–Oct'
        out += ['## %s %dm — current (all three blocks ON): %d setups, net %+.0f, win %.0f%%' % (sym, tf, b['n'], b['net'], b['wr']), '',
                hdr[0].replace('Δ by third', 'Δ by third (%s)' % tn), hdr[1]]
        for nm, bl in (('Block OFF: NY only', ALL - {'NY'}), ('Block OFF: London only', ALL - {'London'}), ('Block OFF: Asia only', ALL - {'Asia'}),
                       ('Block OFF: all three', set())):
            res = run(s, G, bl); x = st(res, s, tf)
            ch = len(C0 ^ {(r['i'], r['lg']) for r in res}) or 1
            z = (x['net'] - b['net']) / (b['sd'] * np.sqrt(ch)); dth = [p - q for p, q in zip(x['th'], b['th'])]
            b3 = all(d > 0 for d in dth)
            v = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if x['net'] < b['net'] else 'noise'
            out.append('| %s | %d | %.0f%% | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (nm, x['n'], x['wr'], x['net'], x['net'] - b['net'], z, *dth, v))
        off = run(s, G, set())
        out += ['', '**Setups inside the windows when the block is OFF** (what the block removes):', '', '| Window | Setups | Win % | Net | Avg | by trigger |', '|---|---|---|---|---|---|']
        for w in ('NY', 'London', 'Asia'):
            g = [r for r in off if r['orw'] == w]; v = [r['res'] for r in g]
            if g:
                tr = collections.Counter(r['trig'] for r in g)
                out.append('| %s | %d | %.0f%% | %+.1f | %+.2f | %s |' % (w, len(v), 100 * sum(x > 0 for x in v) / max(1, sum(x != 0 for x in v)), sum(v), np.mean(v),
                           ', '.join('%s %d / %+.0f' % (t, tr[t], sum(r['res'] for r in g if r['trig'] == t)) for t in tr)))
            else:
                out.append('| %s | 0 | | | | |' % w)
        out.append('')
    # live alerts in the windows
    A = ss.get(ss.BASE + '/alerts?from=2000-01-01'); A = A if isinstance(A, list) else A.get('alerts', [])
    A.sort(key=lambda a: a.get('receivedAt', ''))
    ends = {}
    for a in A:
        r = a.get('raw', '')
        if 'Setup Ended:' in r:
            ch = re.search(r'\nChart: (\S+) (\d+)m', r); se = re.search(r'Setup Entry: ([-\d.]+)', r); res = re.search(r'Result: ([-+\d.]+)', r)
            if ch and se and res:
                ends.setdefault((ch.group(1), ch.group(2), float(se.group(1))), []).append((a['receivedAt'], float(res.group(1))))
    G2 = collections.defaultdict(list)
    for a in A:
        r = a.get('raw', '')
        if 'Trade Setup:' not in r:
            continue
        ch = re.search(r'\nChart: (\S+) (\d+)m', r); tm = re.search(r'\nTime: (\d+/\d+) (\d+):(\d+)', r); en = re.search(r'\nEntry: ([-\d.]+)', r)
        if not (ch and tm and en) or not ch.group(1).startswith(('MES', 'MGC')):
            continue
        tf = int(ch.group(2)); m = (int(tm.group(2)) * 60 + int(tm.group(3)) - tf) % 1440  # candle open minute
        w = 'NY' if 570 <= m < 600 else 'London' if 180 <= m < 210 else 'Asia' if 1200 <= m < 1230 else ''
        if not w:
            continue
        e = [x for x in ends.get((ch.group(1), ch.group(2), float(en.group(1))), []) if x[0] > a['receivedAt']]
        G2[(ch.group(1)[:3] + ' ' + ch.group(2) + 'm', w)].append((tm.group(1), e[0][1] if e else None))
    out += ['## Live Trade Setup alerts inside the OR windows (should be none since the v9.60 default, 10/13)', '']
    if not G2:
        out.append('None.')
    for k in sorted(G2):
        v = [x for _, x in G2[k] if x is not None]
        out.append('- %s %s: %d setups (%s), ended %d, net %+.1f' % (k[0], k[1], len(G2[k]), ', '.join(sorted({d for d, _ in G2[k]})), len(v), sum(v)))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
