#!/usr/bin/env python3
"""Time-based stop study, MES 3m and MGC 3m -- 11/07/2026 (companion to the 11/06 TP1-reduction study).
Question: once a setup has been open X minutes and is NOT working (still negative, or less than Y % of the way to TP1),
should it be cut at that candle's close, or should SL1 be tightened?
Rule (one check, at the close of the candle X minutes after entry, only if TP1 has not been reached yet):
  condition  Y = 'neg'  -> close is at or below Entry (long; short mirrored)
             Y = 25 / 50 -> close is less than 25 / 50 % of the way from Entry to TP1 (includes negative trades)
  action     CUT  -> close the whole trade at that candle close
             HALF -> SL1 moves to half its original distance from Entry (if the close is already past it: close now)
             BE   -> SL1 moves to Entry (if the close is below Entry: close now; with Y = 'neg' this equals CUT)
X = 12..45 min by 3 (same spread as the TP study). Everything else unchanged: stop, TP1 partial / BE / trail, HTF flip,
16:00 and new-setup exits.
Replay (chop_sim rules, late window 1, NY OR block 30) on live settings: MES 3m 9 / 20 + range gate, SL1 3 x ATR min 5,
TP1 1.75 x ATR (v10.82), close at TP1 by time of day; MGC 3m range gate + VWAP stretch 4, SL1 1.7 ATR min 5 cap 7,
TP1 1.7 ATR cap 6, 80 % + BE + trail 1.7; MNQ 3m / M2K 3m CBC defaults (SL1 1.7 ATR min 25 / 3 cap 30 / 5, TP1 1.7 ATR
cap 40 / 3, 80 % + BE + trail 1.7, no range gate). Jan 5 -> now, repaired bar data (11/07).
Cell = Δ net pts vs current exits. Flags: T = better in all three thirds, 4 = better in the last 4 weeks,
R = T and both X neighbours (±3 min) also better overall. z = Δ / (SD x sqrt(setups changed)).
Usage: python3 sltime_study.py MES|MGC|MNQ|M2K  (writes sltime_<SYM>.pkl) ; python3 sltime_study.py report"""
import sys, pickle, numpy as np, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

class SCase(ls.LCase):
    X = 0; Y = 0.0; ACT = 'CUT'
    def sim1(s, i, lg, q, stop_at):
        if s.X <= 0: return m.MCase.sim1(s, i, lg, q, stop_at)
        C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        nb = int(round(s.X / s.tf))
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SLx' if g * (sl - en) > -sd + 1e-9 else 'SL1')
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            if not hit and j - i == nb:
                p = g * (C[j] - en)
                bad = p <= 0 if s.Y == 0 else p < s.Y * tpd
                if bad:
                    if s.ACT == 'CUT': return p, j, 'cut'
                    nsl = en - g * 0.5 * sd if s.ACT == 'HALF' else en
                    if g * (C[j] - nsl) <= 0: return p, j, 'cut'
                    sl = max(sl, nsl) if lg else min(sl, nsl)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

CH = {'MES': ('MES 3m', m.LIVE, dict(R5=1, X4=0, MTF=0)), 'MGC': ('MGC 3m', ls.MGCX, dict(R5=1, X4=1, MTF=0)),
      # MNQ / M2K 3m: CBC default exits (SL1 1.7 ATR, per-symbol min / cap, TP1 1.7 ATR + cap, 80 % + BE + trail 1.7), no range / stretch gate
      'MNQ': ('MNQ 3m', dict(sl=1.7, mn=25, cap=30, tp=1.7, tcap=40, part=.8, be=True, tr=1.7), dict(R5=0, X4=0, MTF=0)),
      'M2K': ('M2K 3m', dict(sl=1.7, mn=3, cap=5, tp=1.7, tcap=3, part=.8, be=True, tr=1.7), dict(R5=0, X4=0, MTF=0))}
SYMS = [k for k in ('MES', 'MGC', 'MNQ', 'M2K')]
XS = list(range(12, 46, 3)); YS = [0.0, 0.25, 0.5]; ACTS = ['CUT', 'HALF', 'BE']
YN = {0.0: 'negative', 0.25: '< 25 % of TP1', 0.5: '< 50 % of TP1'}

def run_sym(sym):
    nm, q, G = CH[sym]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
    s = SCase(sym, 3, B)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    th = lambda r: [sum(t['res'] for t in r if (0 if s.T[t['i']] < cuts[0] else 1 if s.T[t['i']] < cuts[1] else 2) == k) for k in range(3)]
    def run(x, y, a):
        SCase.X, SCase.Y, SCase.ACT = x, y, a
        return s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
    b = run(0, 0, 'CUT'); bv = [t['res'] for t in b]; bn = sum(bv); sd = float(np.std(bv)) or 1
    bt = th(b); b4 = sum(t['res'] for t in b if s.T[t['i']] >= t4)
    base = dict(n=len(b), net=bn, win=round(100 * sum(v > 0 for v in bv) / max(1, sum(v != 0 for v in bv))),
                first=D.datetime.utcfromtimestamp(s.T[300] / 1000).strftime('%m/%d'), last=D.datetime.utcfromtimestamp(T1 / 1000).strftime('%m/%d'),
                sl1=sum(1 for t in b if t['why'] == 'SL1'), sl1net=sum(t['res'] for t in b if t['why'] == 'SL1'))
    res = {}
    for a in ACTS:
        for y in YS:
            for x in XS:
                r = run(x, y, a); v = [t['res'] for t in r]; net = sum(v)
                ch = sum(1 for p, c in zip(b, r) if abs(p['res'] - c['res']) > 1e-9) or 1
                res[(a, y, x)] = dict(d=net - bn, z=(net - bn) / (sd * np.sqrt(ch)), th=[c - p for c, p in zip(th(r), bt)],
                                      d4=sum(t['res'] for t in r if s.T[t['i']] >= t4) - b4, act=sum(1 for t in r if t['why'] == 'cut'), ch=ch,
                                      win=round(100 * sum(t > 0 for t in v) / max(1, sum(t != 0 for t in v))))
        print(sym, a, 'done', flush=True)
    pickle.dump((nm, base, res), open('sltime_%s.pkl' % sym, 'wb'))

def report():
    out = ['# Time-based stop / cut study — 3m charts — %s' % D.datetime.now().strftime('%m/%d/%Y %H:%M'), '', __doc__.strip().split('Usage:')[0].strip(), '']
    cand = []
    for sym in [k for k in SYMS if __import__('os').path.exists('sltime_%s.pkl' % k)]:
        nm, base, res = pickle.load(open('sltime_%s.pkl' % sym, 'rb'))
        out += ['## %s — current exits: %d setups %s–%s, net %+.0f, win %d %%, full SL1 losses %d (%+.0f)' % (
            nm, base['n'], base['first'], base['last'], base['net'], base['win'], base['sl1'], base['sl1net']), '']
        for a, an in (('CUT', 'CUT at the candle close'), ('HALF', 'Tighten SL1 to half its distance'), ('BE', 'SL1 to breakeven')):
            out += ['**%s** — Δ net vs current' % an, '', '| X min | ' + ' | '.join(YN[y] for y in YS) + ' |', '|---|' + '---|' * len(YS)]
            for xi, x in enumerate(XS):
                cells = []
                for y in YS:
                    c = res[(a, y, x)]; t = all(k > 0 for k in c['th']); f = c['d4'] > 0
                    nbr = [res[(a, y, XS[k])]['d'] for k in (xi - 1, xi + 1) if 0 <= k < len(XS)]
                    r = t and c['d'] > 0 and all(v > 0 for v in nbr)
                    fl = ''.join(k for k, v in (('T', t), ('4', f), ('R', r)) if v)
                    s_ = '%+.0f%s' % (c['d'], ' ' + fl if fl else '')
                    cells.append('**%s**' % s_ if t and f and r else s_)
                    vd = 'robust' if c['z'] >= 2 and t else 'promising' if c['z'] >= 1 and t else None
                    if vd and r: cand.append((c['d'], '%s %s, X %d min, %s: %+.0f, z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f, %d trades acted on, win %d %% (%s)' % (
                        nm, an, x, YN[y], c['d'], c['z'], *c['th'], c['d4'], c['act'], c['win'], vd)))
                out.append('| %d | %s |' % (x, ' | '.join(cells)))
            allc = sorted(((res[(a, y, x)]['d'], x, y) for x in XS for y in YS), reverse=True)
            pos = sum(1 for d, *_ in allc if d > 0)
            out += ['', 'Positive cells %d of %d. Best: %s.' % (pos, len(allc), '; '.join(
                'X %d / %s %+.0f (z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f)' % (x, YN[y], d, res[(a, y, x)]['z'], *res[(a, y, x)]['th'], res[(a, y, x)]['d4'])
                for d, x, y in allc[:3])), '']
    cand.sort(key=lambda k: -k[0])
    out += ['## Candidates (robust / promising AND both X neighbours better)', ''] + (['- ' + k for _, k in cand[:12]] if cand else ['- none'])
    print('\n'.join(out))

if __name__ == '__main__':
    report() if sys.argv[1] == 'report' else run_sym(sys.argv[1])
