#!/usr/bin/env python3
"""CBC Setup Triggers study -- 11/01/2026.

Question: does each "② Setup Triggers" trigger earn its place, per chart? (HTF CBC Flip, LTF EMA20 Pierce, HTF EMA9 Pierce,
HTF EMA20 Pierce in the replay; LTF EMA20 Touch, Momentum break and HTF Pullback Structure are live-only -- not in the replay.)
(A) Replay Jan 5 - Oct 30 (2m Jun - Oct), each chart on its live settings (filter_sweep.LIVE), base exits: per-trigger results,
    and each trigger turned OFF one at a time vs current (a removed trigger also changes the setups after it: one open setup,
    cooldown). (B) Live: every Trade Setup alert by its first trigger (and late / mid-candle variants), matched to its Setup Ended.
z = change / (SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 trigger_study.py [SYM TF]   (no args = live part + all six charts)
"""
import sys, re, collections, datetime as D, numpy as np
import chop_sim as cs, stretch_study as ss, filter_sweep as fs

ss.FROM[5] = '2026-01-05'
TR = [('flip', 'HTF CBC Flip'), ('ltf20', 'LTF EMA20 Pierce'), ('h9', 'HTF EMA9 Pierce'), ('h20', 'HTF EMA20 Pierce')]


def replay(sym, tf):
    L0 = fs.LIVE[(sym, tf)]
    P = dict(er=.23, bo=3, r5=L0['r5'], r5z=.2, x4=L0['x4'], mtf=L0['mtf'], fl=L0['fl'])
    s = cs.Case(sym, tf, ss.load(sym, tf)); fs.prep(s)
    th3 = 3 if tf != 2 else 2
    keep = list(s.cands)

    def run(skip=()):
        s.cands = [d for d in keep if d['trig'] not in skip]
        try:
            return fs.run(s, P)
        finally:
            s.cands = keep
    cur = run(); v0 = [r['res'] for r in cur]; net0 = sum(v0); sd = float(np.std(v0)) or 1
    t0 = ss.thirds(cur, s.month, th3); C0 = {(r['i'], r['lg']) for r in cur}
    tn = 'Jan–Mar / Apr–Jun / Jul–Oct' if tf != 2 else 'Jun–Jul / Aug / Sep–Oct'
    out = ['## %s %dm — current: %d setups, net %+.0f' % (sym, tf, len(v0), net0), '',
           '**Per trigger (current settings)**', '', '| Trigger | Setups | Win %% | Net | Avg | Net by third (%s) |' % tn, '|---|---|---|---|---|---|']
    for t, nm in TR:
        g = [r for r in cur if r['trig'] == t]; v = [r['res'] for r in g]
        if v:
            out.append('| %s | %d | %.0f%% | %+.0f | %+.2f | %+.0f / %+.0f / %+.0f |' % (nm, len(v), 100 * np.mean([x > 0 for x in v]), sum(v), np.mean(v), *ss.thirds(g, s.month, th3)))
    out += ['', '**Trigger turned OFF (one at a time)**', '', '| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |', '|---|---|---|---|---|---|---|']
    for t, nm in TR:
        res = run((t,)); v = [r['res'] for r in res]; net = sum(v)
        ch = len(C0 ^ {(r['i'], r['lg']) for r in res}) or 1
        z = (net - net0) / (sd * np.sqrt(ch)); dth = [a - b for a, b in zip(ss.thirds(res, s.month, th3), t0)]
        b3 = all(x > 0 for x in dth)
        vd = 'robust' if z >= 2 and b3 else 'promising' if z >= 1 and b3 else 'worse' if net < net0 else 'noise'
        out.append('| %s | %d | %+.0f | %+.0f | %+.1f | %+.0f / %+.0f / %+.0f | %s |' % (nm, len(v), net, net - net0, z, *dth, vd))
    return out + ['']


def live():
    A = ss.get(ss.BASE + '/alerts?from=2000-01-01'); A = A if isinstance(A, list) else A.get('alerts', [])
    A.sort(key=lambda a: a.get('receivedAt', ''))
    ends = {}
    for a in A:
        r = a.get('raw', '')
        if isinstance(r, str) and 'Setup Ended:' in r:
            ch = re.search(r'\nChart: (\S+) (\d+)m', r); se = re.search(r'Setup Entry: ([-\d.]+)', r); res = re.search(r'Result: ([-+\d.]+)', r)
            if ch and se and res:
                ends.setdefault((ch.group(1), ch.group(2), float(se.group(1))), []).append((a['receivedAt'], float(res.group(1))))
    G = collections.defaultdict(list)
    for a in A:
        r = a.get('raw', '')
        if not isinstance(r, str) or 'Trade Setup:' not in r:
            continue
        ch = re.search(r'\nChart: (\S+) (\d+)m', r); t = re.search(r'\nTrigger: ([^\n]+)', r); en = re.search(r'\nEntry: ([-\d.]+)', r)
        if not (ch and t and en):
            continue
        first = t.group(1).split(',')[0].strip()
        base = re.sub(r'\s*\(.*$', '', first)
        var = 'late' if 'late' in first else 'mid-candle' if 'mid-candle' in first else 'pullback' if 'pullback' in first else ''
        e = [x for x in ends.get((ch.group(1), ch.group(2), float(en.group(1))), []) if x[0] > a['receivedAt']]
        G[(ch.group(1).replace('1!', '') + ' ' + ch.group(2) + 'm', base + (' (%s)' % var if var else ''))].append(e[0][1] if e else None)
    out = ['## Live Trade Setups by first trigger (alert store, with Setup Ended results)', '',
           '| Chart | Trigger | Setups | Ended | Win % | Net | Avg |', '|---|---|---|---|---|---|---|']
    for k in sorted(G):
        v = [x for x in G[k] if x is not None]; w = sum(x > 0 for x in v); l = sum(x < 0 for x in v)
        out.append('| %s | %s | %d | %d | %s | %+.1f | %s |' % (k[0], k[1], len(G[k]), len(v), '%d%%' % round(100 * w / (w + l)) if w + l else '–', sum(v), '%+.2f' % np.mean(v) if v else '–'))
    return out + ['']


def main():
    if len(sys.argv) > 2:
        print('\n'.join(replay(sys.argv[1], int(sys.argv[2]))))
        return
    out = ['# Setup Triggers study — %s' % D.datetime.now().strftime('%a %m/%d/%Y %H:%M'), '', __doc__.strip(), '']
    out += live()
    for sym, tf in fs.LIVE:
        out += replay(sym, tf)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
