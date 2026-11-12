#!/usr/bin/env python3
"""Combined time-based TP reduction + time-based stop / cut, MES 3m and MGC 3m -- 11/07/2026.
Both rules active together on the same trade (before TP1 only):
  TP rule (11/06 study, mode A "modified TP"): from the candle after Xtp minutes, TP1 becomes a limit at Ytp % of the TP1
          distance (fills when the high / low reaches it; at the open if the candle opens past it). Closes 100 %.
  SL rule (11/07 study): one check at the close of the candle Xsl minutes after entry; if the trade is negative / below
          Ysl % of TP1: CUT = close at that close; HALF = SL1 to half its distance (close now if already past it).
Grid: TP Xtp 12-42 (12,15,18,21,24,27,30,33,36,42) x Ytp 65/70/75/85 % + "TP rule off";
      SL CUT x (negative, < 25 %, < 50 %) and HALF x (negative, < 50 %), Xsl 12-24 by 3 + "SL rule off".
Replay = sltime_study / tptime_study engine on live settings (MES 3m TP1 1.75 ATR v10.82, MGC 3m MGCX). Jan 5 -> now.
Cell = Δ net pts vs current exits. T = better in all three thirds, 4 = better in the last 4 weeks, R = T and all neighbours
(Xtp ±1 grid step, Xsl ±3 min) better overall. z = Δ / (SD x sqrt(setups changed)). Also shown: what each rule gives alone,
and whether the combination adds up (combo vs TP-alone + SL-alone).
Usage: python3 combo_study.py MES|MGC  (writes combo_<SYM>.pkl) ; python3 combo_study.py report"""
import sys, pickle, os, numpy as np, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

class CCase(ls.LCase):
    TX = 0; TY = 0.0; SX = 0; SY = 0.0; ACT = None
    def sim1(s, i, lg, q, stop_at):
        if s.TX <= 0 and s.ACT is None: return m.MCase.sim1(s, i, lg, q, stop_at)
        C, H, L, O = s.C, s.H, s.L, s.O; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        tnb = int(np.ceil(s.TX / s.tf)) if s.TX > 0 else 10 ** 9; red = en + g * s.TY * tpd
        snb = int(round(s.SX / s.tf)) if s.ACT else -1
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and j - i > tnb:
                if (O[j] >= red) if lg else (O[j] <= red): return g * (O[j] - en), j, 'TPx'
                if (H[j] >= red) if lg else (L[j] <= red): return s.TY * tpd, j, 'TPx'
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            if not hit and j - i == snb:
                p = g * (C[j] - en)
                if (p <= 0 if s.SY == 0 else p < s.SY * tpd):
                    if s.ACT == 'CUT': return p, j, 'cut'
                    nsl = en - g * 0.5 * sd
                    if g * (C[j] - nsl) <= 0: return p, j, 'cut'
                    sl = max(sl, nsl) if lg else min(sl, nsl)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

CH = {'MES': ('MES 3m', m.LIVE, dict(R5=1, X4=0, MTF=0)), 'MGC': ('MGC 3m', ls.MGCX, dict(R5=1, X4=1, MTF=0))}
TXS = [12, 15, 18, 21, 24, 27, 30, 33, 36, 42]; TYS = [.65, .70, .75, .85]
SLS = [('CUT', 0.0), ('CUT', .25), ('CUT', .5), ('HALF', 0.0), ('HALF', .5)]; SXS = [12, 15, 18, 21, 24]
TPO = [(0, 0.0)] + [(x, y) for y in TYS for x in TXS]
SLO = [(None, 0.0, 0)] + [(a, y, x) for a, y in SLS for x in SXS]
YN = {0.0: 'negative', .25: '< 25 %', .5: '< 50 %'}
def tpn(t): return 'TP off' if t[0] == 0 else 'TP %d%% after %d min' % (round(t[1] * 100), t[0])
def sln(c): return 'SL off' if c[0] is None else '%s if %s at %d min' % ('cut' if c[0] == 'CUT' else 'half SL1', YN[c[1]], c[2])

def run_sym(sym):
    nm, q, G = CH[sym]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
    s = CCase(sym, 3, B)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    th = lambda r: [sum(t['res'] for t in r if (0 if s.T[t['i']] < cuts[0] else 1 if s.T[t['i']] < cuts[1] else 2) == k) for k in range(3)]
    def run(tp, slr):
        CCase.TX, CCase.TY = tp; CCase.ACT, CCase.SY, CCase.SX = slr
        return s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
    b = run(TPO[0], SLO[0]); bv = [t['res'] for t in b]; bn = sum(bv); sd = float(np.std(bv)) or 1
    bt = th(b); b4 = sum(t['res'] for t in b if s.T[t['i']] >= t4)
    base = dict(n=len(b), net=bn, last=D.datetime.utcfromtimestamp(T1 / 1000).strftime('%m/%d'))
    res = {}; k = 0
    for tp in TPO:
        for slr in SLO:
            if tp == TPO[0] and slr == SLO[0]: continue
            r = run(tp, slr); net = sum(t['res'] for t in r)
            ch = sum(1 for p, c in zip(b, r) if abs(p['res'] - c['res']) > 1e-9) or 1
            res[(tp, slr)] = dict(d=net - bn, z=(net - bn) / (sd * np.sqrt(ch)), th=[c - p for c, p in zip(th(r), bt)],
                                  d4=sum(t['res'] for t in r if s.T[t['i']] >= t4) - b4, n=len(r),
                                  win=round(100 * sum(t['res'] > 0 for t in r) / max(1, sum(t['res'] != 0 for t in r))))
            k += 1
            if k % 50 == 0: print(sym, k, flush=True); pickle.dump((nm, base, res), open('combo_%s.pkl' % sym, 'wb'))
    pickle.dump((nm, base, res), open('combo_%s.pkl' % sym, 'wb')); print(sym, 'done', flush=True)

def report():
    out = ['# Combined TP-reduction + time-stop study — MES 3m and MGC 3m — %s' % D.datetime.now().strftime('%m/%d/%Y %H:%M'), '',
           __doc__.strip().split('Usage:')[0].strip(), '']
    for sym in ('MES', 'MGC'):
        if not os.path.exists('combo_%s.pkl' % sym): continue
        nm, base, res = pickle.load(open('combo_%s.pkl' % sym, 'rb'))
        def flags(tp, slr):
            c = res[(tp, slr)]; t = all(v > 0 for v in c['th']); f = c['d4'] > 0
            nb = []
            if tp[0]:
                xi = TXS.index(tp[0]); nb += [res.get(((TXS[k], tp[1]), slr)) for k in (xi - 1, xi + 1) if 0 <= k < len(TXS)]
            if slr[0]:
                xi = SXS.index(slr[2]); nb += [res.get((tp, (slr[0], slr[1], SXS[k]))) for k in (xi - 1, xi + 1) if 0 <= k < len(SXS)]
            r = t and c['d'] > 0 and all(v and v['d'] > 0 for v in nb)
            return t, f, r
        def line(tp, slr):
            c = res[(tp, slr)]; t, f, r = flags(tp, slr)
            fl = ''.join(k for k, v in (('T', t), ('4', f), ('R', r)) if v)
            vd = ' — robust' if c['z'] >= 2 and t else ' — promising' if c['z'] >= 1 and t else ''
            return '%s + %s: **%+.0f** %s(z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f, win %d %%)%s' % (
                tpn(tp), sln(slr), c['d'], fl + ' ' if fl else '', c['z'], *c['th'], c['d4'], c['win'], vd)
        out += ['## %s — current exits: %d setups to %s, net %+.0f' % (nm, base['n'], base['last'], base['net']), '']
        allk = list(res)
        tpo = sorted((k for k in allk if k[1] == SLO[0]), key=lambda k: -res[k]['d'])
        slo = sorted((k for k in allk if k[0] == TPO[0]), key=lambda k: -res[k]['d'])
        cmb = sorted((k for k in allk if k[0] != TPO[0] and k[1] != SLO[0]), key=lambda k: -res[k]['d'])
        out += ['**Best TP rule alone:** ' + line(*tpo[0]), '', '**Best SL rule alone:** ' + line(*slo[0]), '']
        pos = sum(1 for k in cmb if res[k]['d'] > 0); tfl = [k for k in cmb if flags(*k)[0]]; rfl = [k for k in cmb if flags(*k)[2]]
        out += ['Combinations: %d, positive %d, better in all thirds %d, T + neighbours (R) %d, T + 4 + R %d.' % (
            len(cmb), pos, len(tfl), len(rfl), sum(1 for k in rfl if flags(*k)[1])), '', '**Top 10 combinations by Δ**', '']
        out += ['%d. %s' % (n + 1, line(*k)) for n, k in enumerate(cmb[:10])]
        good = [k for k in cmb if flags(*k)[0] and flags(*k)[2]]
        out += ['', '**Steadiest combinations (all thirds better AND every neighbour better), top 10 by Δ**', '']
        out += ['%d. %s' % (n + 1, line(*k)) for n, k in enumerate(good[:10])] or ['- none']
        # additivity: for the top TP-alone rows, best SL partner and whether it adds
        out += ['', '**Does adding the SL rule help the TP rule?** (top 5 TP rules; best SL partner; combo vs TP alone)', '',
                '| TP rule | TP alone | + best SL rule | Combo | SL adds | SL alone |', '|---|---|---|---|---|---|']
        for tk in tpo[:5]:
            tp = tk[0]; part = max((k for k in cmb if k[0] == tp), key=lambda k: res[k]['d'])
            out.append('| %s | %+.0f | %s | %+.0f | %+.0f | %+.0f |' % (tpn(tp), res[tk]['d'], sln(part[1]), res[part]['d'],
                       res[part]['d'] - res[tk]['d'], res[(TPO[0], part[1])]['d']))
        # heat: best SL partner per TP cell
        out += ['', '**Grid: best combo Δ per TP cell (any SL rule) / TP alone**', '', '| Xtp \\ Ytp | ' + ' | '.join('%d%%' % round(y * 100) for y in TYS) + ' |',
                '|---|' + '---|' * len(TYS)]
        for x in TXS:
            out.append('| %d | %s |' % (x, ' | '.join('%+.0f / %+.0f' % (max(res[((x, y), sl)]['d'] for sl in SLO[1:]), res[((x, y), SLO[0])]['d']) for y in TYS)))
        out.append('')
    print('\n'.join(out))

if __name__ == '__main__':
    report() if sys.argv[1] == 'report' else run_sym(sys.argv[1])
