#!/usr/bin/env python3
"""Early-exit lab -- 3m charts MES, MGC, MNQ, M2K -- 11/07/2026.
Follow-up to the time-stop and TP+SL combo studies. One replay that tests, together:
 1. CHECK TIME: fixed X min after entry (12/15/18/21/24) vs the HTF (15m) candle close -- H1 = first 15m close after entry,
    H1+ = first 15m close at least 12 min after entry, H2 = second 15m close.
 2. COSTS: every result is shown gross and after costs. Cost per trade = round-trip commission (~$1.24 / micro) + 1 tick entry
    slippage; a rule exit at the candle close (market order) pays 1 more tick. MES 0.25+0.25 / MGC 0.12+0.10 / MNQ 0.62+0.25 /
    M2K 0.25+0.10 pts per trade; tick MES .25 / MGC .1 / MNQ .25 / M2K .1. Extra trades (re-entries after a cut) pay too.
 3. WALK-FORWARD: the best rule is chosen on the first two thirds of the period only (after costs), then scored on the last third.
 4. CONDITION at the check (before TP1 only): neg = close at / beyond Entry against; <25 % / <50 % = close less than that share
    of the way to TP1; h9 = close on the wrong side of the HTF EMA9; mfe25 / mfe50 = the best price so far never reached
    25 / 50 % of TP1 ("never got going").
    ACTION: CUT = close at that close; HALF = SL1 to half its distance; BE = SL1 to Entry (close now if already past it).
 5. SPLIT: Δ by session (NY 09:30-16:00 vs rest) and by trigger (HTF flip vs others) for the top rules.
 6. RE-ENTRY: trades that start within 30 min after a cut in the same direction -- count, net, avg vs all trades.
 7. BOT GUARDS (post-hoc on the trade list, after costs): stop for the rest of the session (18:00-18:00 ET) after K losses in
    a row or after the session is down L points (L = 1 / 2 / 3 x the average full SL1 loss).
MES 3m and MGC 3m are also run with the best TP-reduction rule on top (MES TP1 -> 85 % after 18 min, MGC -> 65 % after 21 min).
Replay = chop_sim rules (late window 1, NY OR block 30) on live exits: MES 3m SL1 3 ATR min 5, TP1 1.75 ATR, 80/100 % by time
of day; MGC 3m MGCX; MNQ / M2K 3m CBC defaults. Jan 5 -> now. Flags: T = better in all three thirds, 4 = better in the last
4 weeks, R = T and both time neighbours (±3 min) better (fixed-time rows only). z = Δ / (SD x sqrt(setups changed)).
Usage: python3 exit_lab.py MES|MGC|MNQ|M2K ; python3 exit_lab.py report"""
import sys, os, pickle, numpy as np, pandas as pd, datetime as D
import chop_sim as cs, late_study as ls, mes3_ema_grid as m

class XCase(ls.LCase):
    CHK = None; COND = 'neg'; ACT = 'CUT'; TX = 0; TY = 0.0
    def prep(s):
        s.isc = s.T == s.B['last'].values
        et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
        mm = (et.dt.hour * 60 + et.dt.minute).values
        s.ny = (mm >= 570) & (mm < 960); s.sess = s.B.hk.str[:10].values
    def sim1(s, i, lg, q, stop_at):
        if s.CHK is None and s.TX <= 0: return m.MCase.sim1(s, i, lg, q, stop_at)
        C, H, L, O = s.C, s.H, s.L, s.O; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False; best = 0.0
        tnb = int(np.ceil(s.TX / s.tf)) if s.TX > 0 else 10 ** 9; red = en + g * s.TY * tpd
        ck = s.CHK; done = ck is None; nh = 0
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
            best = max(best, g * ((H[j] if lg else L[j]) - en))
            if not done and not hit:
                if s.isc[j]: nh += 1
                if isinstance(ck, int): now = j - i == int(round(ck / s.tf))
                elif ck == 'H1': now = s.isc[j] and nh == 1
                elif ck == 'H1+': now = s.isc[j] and (j - i) * s.tf >= 12
                else: now = s.isc[j] and nh == 2
                if now:
                    done = True; p = g * (C[j] - en); c = s.COND
                    bad = (p <= 0 if c == 'neg' else p < .25 * tpd if c == 'p25' else p < .5 * tpd if c == 'p50' else
                           g * (C[j] - s.h9[j]) < 0 if c == 'h9' else best < .25 * tpd if c == 'mfe25' else best < .5 * tpd)
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

GD = dict(R5=0, X4=0, MTF=0)
CH = {'MES': ('MES 3m', m.LIVE, dict(R5=1, X4=0, MTF=0), .25, .25, (18, .85)),
      'MGC': ('MGC 3m', ls.MGCX, dict(R5=1, X4=1, MTF=0), .10, .12, (21, .65)),
      'MNQ': ('MNQ 3m', dict(sl=1.7, mn=25, cap=30, tp=1.7, tcap=40, part=.8, be=True, tr=1.7), GD, .25, .62, None),
      'M2K': ('M2K 3m', dict(sl=1.7, mn=3, cap=5, tp=1.7, tcap=3, part=.8, be=True, tr=1.7), GD, .10, .25, None)}
CHKS = [12, 15, 18, 21, 24, 'H1', 'H1+', 'H2']; CONDS = ['neg', 'p25', 'p50', 'h9', 'mfe25', 'mfe50']; ACTS = ['CUT', 'HALF', 'BE']
CN = dict(neg='negative', p25='< 25 % of TP1', p50='< 50 % of TP1', h9='wrong side of HTF EMA9', mfe25='never reached 25 %', mfe50='never reached 50 %')
AN = dict(CUT='cut', HALF='half SL1', BE='SL1 to BE')
def ckn(c): return '%d min' % c if isinstance(c, int) else {'H1': '1st 15m close', 'H1+': '1st 15m close >= 12 min', 'H2': '2nd 15m close'}[c]
def vn(v): return '%s if %s at %s' % (AN[v[2]], CN[v[1]], ckn(v[0]))

def run_sym(sym):
    nm, q, G, tick, comm = CH[sym][:5]; tpr = CH[sym][5]
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30
    s = XCase(sym, 3, B); s.prep()
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    third = lambda i: 0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2
    def run(chk, cond, act, tp):
        XCase.CHK, XCase.COND, XCase.ACT = chk, cond, act; XCase.TX, XCase.TY = tp if tp else (0, 0.0)
        r = s.run(lambda d: cs.cur_rule(d), q=q, gates=G)
        return [dict(i=t['i'], j=t['j'], lg=t['lg'], trig=t['trig'], why=t['why'], g=t['res'],
                     n=t['res'] - (tick + comm) - (tick if t['why'] == 'cut' else 0), th=third(t['i']), l4=s.T[t['i']] >= t4,
                     ny=bool(s.ny[t['i']]), ss=s.sess[t['i']]) for t in r]
    out = dict(nm=nm, tick=tick, comm=comm, tpr=tpr, last=D.datetime.utcfromtimestamp(T1 / 1000).strftime('%m/%d'), runs={})
    tps = [None] + ([tpr] if tpr else [])
    for tp in tps:
        out['runs'][(None, None, None, tp)] = run(None, None, None, tp)
        for chk in CHKS:
            for cond in CONDS:
                for act in ACTS:
                    if act == 'BE' and cond == 'neg': continue   # = CUT
                    out['runs'][(chk, cond, act, tp)] = run(chk, cond, act, tp)
        print(sym, 'tp', tp, 'done', flush=True)
    pickle.dump(out, open('xlab_%s.pkl' % sym, 'wb'))

def stats(r, b, k='n'):
    v = sum(t[k] for t in r) - sum(t[k] for t in b)
    th = [sum(t[k] for t in r if t['th'] == x) - sum(t[k] for t in b if t['th'] == x) for x in range(3)]
    d4 = sum(t[k] for t in r if t['l4']) - sum(t[k] for t in b if t['l4'])
    bi = {t['i']: t[k] for t in b}; ri = {t['i']: t[k] for t in r}
    ch = sum(1 for i in set(bi) | set(ri) if abs(bi.get(i, 0) - ri.get(i, 0)) > 1e-9) or 1
    sd = float(np.std([t[k] for t in b])) or 1
    return dict(d=v, th=th, d4=d4, z=v / (sd * np.sqrt(ch)), n=len(r), cut=sum(1 for t in r if t['why'] == 'cut'))

def guard(r, K, Lp):
    keep = []; cur = None; cum = 0; ls_ = 0
    for t in sorted(r, key=lambda t: t['i']):
        if t['ss'] != cur: cur, cum, ls_ = t['ss'], 0, 0
        if (K and ls_ >= K) or (Lp and cum <= -Lp): continue
        keep.append(t); cum += t['n']; ls_ = ls_ + 1 if t['n'] < 0 else 0
    return keep

def report():
    out = ['# Early-exit lab — 3m charts — %s' % D.datetime.now().strftime('%m/%d/%Y %H:%M'), '', __doc__.strip().split('Usage:')[0].strip(), '']
    summ = []
    for sym in ('MES', 'MGC', 'MNQ', 'M2K'):
        if not os.path.exists('xlab_%s.pkl' % sym): continue
        X = pickle.load(open('xlab_%s.pkl' % sym, 'rb')); R = X['runs']; nm = X['nm']
        b = R[(None, None, None, None)]
        out += ['## %s — current exits: %d setups to %s, net %+.0f gross / %+.0f after costs (%.2f pts per trade)' % (
            nm, len(b), X['last'], sum(t['g'] for t in b), sum(t['n'] for t in b), X['tick'] + X['comm']), '']
        S = {k: stats(R[k], b) for k in R if k[0] is not None}
        G_ = {k: stats(R[k], b, 'g') for k in R if k[0] is not None}
        def fl(k):
            c = S[k]; t = all(x > 0 for x in c['th']); f = c['d4'] > 0; r_ = False
            if t and isinstance(k[0], int):
                ix = CHKS.index(k[0]); nb = [S.get((CHKS[x], k[1], k[2], k[3])) for x in (ix - 1, ix + 1) if 0 <= x < 5]
                r_ = c['d'] > 0 and all(v and v['d'] > 0 for v in nb)
            return ''.join(a for a, v in (('T', t), ('4', f), ('R', r_)) if v)
        def line(k):
            c = S[k]; f = fl(k)
            vd = ' — robust' if c['z'] >= 2 and 'T' in f else ' — promising' if c['z'] >= 1 and 'T' in f else ''
            return '%s%s: **%+.0f** after costs (gross %+.0f) %s(z %+.1f, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f, %d cuts, %+d trades)%s' % (
                vn(k), ' + TP rule' if k[3] else '', c['d'], G_[k]['d'], f + ' ' if f else '', c['z'], *c['th'], c['d4'], c['cut'], c['n'] - len(b), vd)
        # 1. check time table (best action/condition per check time, no TP rule)
        out += ['**1. When to check — best rule per check time (after costs; no TP rule)**', '', '| Check | Best rule | Δ after costs | Gross | Thirds | Last 4 wk | Positive rules |', '|---|---|---|---|---|---|---|']
        for chk in CHKS:
            ks = [k for k in S if k[0] == chk and k[3] is None]; bk = max(ks, key=lambda k: S[k]['d'])
            out.append('| %s | %s if %s | %+.0f %s | %+.0f | %+.0f / %+.0f / %+.0f | %+.1f | %d / %d |' % (
                ckn(chk), AN[bk[2]], CN[bk[1]], S[bk]['d'], fl(bk), G_[bk]['d'], *S[bk]['th'], S[bk]['d4'], sum(S[k]['d'] > 0 for k in ks), len(ks)))
        # 4. condition table
        out += ['', '**4. Which condition — best per condition (any check time / action, no TP rule)**', '', '| Condition | Best rule | Δ after costs | Gross | Positive rules |', '|---|---|---|---|---|']
        for cond in CONDS:
            ks = [k for k in S if k[1] == cond and k[3] is None]; bk = max(ks, key=lambda k: S[k]['d'])
            out.append('| %s | %s | %+.0f %s | %+.0f | %d / %d |' % (CN[cond], vn(bk), S[bk]['d'], fl(bk), G_[bk]['d'], sum(S[k]['d'] > 0 for k in ks), len(ks)))
        # costs
        allk = [k for k in S if k[3] is None]
        gp = sum(G_[k]['d'] > 0 for k in allk); np_ = sum(S[k]['d'] > 0 for k in allk)
        out += ['', '**2. Costs:** %d of %d rules are better gross, %d after costs. Avg cost of the rules: %+.0f pts.' % (
            gp, len(allk), np_, np.mean([S[k]['d'] - G_[k]['d'] for k in allk])), '']
        top = sorted(S, key=lambda k: -S[k]['d'])[:8]
        out += ['**Top 8 rules after costs** (incl. with the TP rule where run)', ''] + ['%d. %s' % (n + 1, line(k)) for n, k in enumerate(top)] + ['']
        if X['tpr']:
            tb = R[(None, None, None, X['tpr'])]; st = stats(tb, b)
            out += ['TP rule alone (TP1 -> %d %% after %d min): %+.0f after costs, thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f.' % (
                round(X['tpr'][1] * 100), X['tpr'][0], st['d'], *st['th'], st['d4']), '']
        # 3. walk-forward
        wf = []
        for tpk in sorted({k[3] for k in S}, key=lambda v: v is not None):
            ks = [k for k in S if k[3] == tpk]
            pick = max(ks, key=lambda k: S[k]['th'][0] + S[k]['th'][1])
            l3 = sorted(S[k]['th'][2] for k in ks)
            rank = sum(1 for v in l3 if v > S[pick]['th'][2])
            wf.append('- %s: picked on thirds 1-2 = **%s** (%+.0f in-sample) → last third **%+.0f** (rank %d of %d; median rule %+.0f; current exits 0)' % (
                'with TP rule' if tpk else 'SL rules only', vn(pick), S[pick]['th'][0] + S[pick]['th'][1], S[pick]['th'][2], rank + 1, len(ks), l3[len(l3) // 2]))
        out += ['**3. Walk-forward** (choose on the first two thirds, test on the last third, after costs)', ''] + wf + ['']
        # 5. split for top 3 (no TP)
        top3 = sorted([k for k in S if k[3] is None], key=lambda k: -S[k]['d'])[:3]
        out += ['**5. Split by session / trigger** (Δ after costs)', '', '| Rule | NY 09:30-16:00 | Other hours | HTF flip | Other triggers |', '|---|---|---|---|---|']
        for k in top3:
            r = R[k]; f = lambda P: sum(t['n'] for t in r if P(t)) - sum(t['n'] for t in b if P(t))
            out.append('| %s | %+.0f | %+.0f | %+.0f | %+.0f |' % (vn(k), f(lambda t: t['ny']), f(lambda t: not t['ny']), f(lambda t: t['trig'] == 'flip'), f(lambda t: t['trig'] != 'flip')))
        # 6. re-entry
        out += ['', '**6. Re-entry after a cut** (next same-direction trade starting within 30 min after the cut)', '']
        for k in top3:
            r = sorted(R[k], key=lambda t: t['i']); re_ = []
            for a, t in enumerate(r):
                if t['why'] != 'cut': continue
                for u in r[a + 1:]:
                    if u['i'] > t['j'] + 10: break
                    if u['i'] > t['j'] - 1 and u['lg'] == t['lg']: re_.append(u); break
            avg = np.mean([t['n'] for t in r])
            out.append('- %s: %d cuts → %d re-entries, net %+.0f, avg %+.2f vs all trades %+.2f' % (
                vn(k), sum(1 for t in r if t['why'] == 'cut'), len(re_), sum(t['n'] for t in re_), np.mean([t['n'] for t in re_]) if re_ else 0, avg))
        # 7. bot guards
        sl1 = [-t['n'] for t in b if t['why'] == 'SL1']; ul = float(np.mean(sl1)) if sl1 else 10
        out += ['', '**7. Session guards** (skip the rest of the session after K losses in a row or after −L pts; avg full SL1 loss %.1f pts)' % ul, '',
                '| Guard | on current exits | beyond random skipping* | on best rule (%s) |' % vn(top3[0]), '|---|---|---|---|']
        bn = sum(t['n'] for t in b); bt = R[top3[0]]; btn = sum(t['n'] for t in bt)
        gl = []
        for K in (0, 2, 3, 4):
            for Lm in (0, 1, 2, 3):
                if not K and not Lm: continue
                g1 = guard(b, K, Lm * ul); g2 = guard(bt, K, Lm * ul)
                s1 = stats(g1, b); s2 = stats(g2, b)
                d2 = sum(t['n'] for t in g2) - btn
                ex = s1['d'] + (len(b) - len(g1)) * bn / len(b)
                gl.append((ex, '| %s | %+.0f %s (thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.1f, %d skipped) | **%+.0f** | %+.0f vs rule alone |' % (
                    ' + '.join(x for x in ('%d losses in a row' % K if K else '', '−%d x SL1 (%.0f pts)' % (Lm, Lm * ul) if Lm else '') if x),
                    s1['d'], 'T' if all(x > 0 for x in s1['th']) else '', *s1['th'], s1['d4'], len(b) - len(g1), ex, d2)))
        out += [x for _, x in sorted(gl, key=lambda v: -v[0])] + ['', '*Current exits lose %.2f pts per trade after costs, so skipping ANY trades looks good. This column = guard result minus what skipping the same number of random trades would give; positive = the guard picks the bad trades.' % (-bn / len(b)), '']
        bk = top[0]
        summ.append('- %s: best %s → %+.0f after costs (z %+.1f, %s); walk-forward last third %s' % (nm, vn(bk) + (' + TP rule' if bk[3] else ''), S[bk]['d'], S[bk]['z'], fl(bk) or 'no flags', wf[-1].split('→ last third ')[1].split(' (')[0]))
    print('\n'.join(out[:1] + ['', '## Summary', ''] + summ + [''] + out[1:]))

if __name__ == '__main__':
    report() if sys.argv[1] == 'report' else run_sym(sys.argv[1])
