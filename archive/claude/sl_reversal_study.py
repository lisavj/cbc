#!/usr/bin/env python3
"""CBC stop-out reversal study: after a setup hits SL1, does price turn around within the next 1-10 candles and reach
the setup's TP1 -- i.e. would a slightly wider stop have turned the loss into a TP1 win?

For every setup that ended "SL1 hit": the stop candle = the candle that touched SL1. For N = 1..10 we check the N
candles AFTER the stop candle: did any of them reach TP1 (long: high >= TP1, short: low <= TP1)? For those that did,
"extra stop needed" = how far price went beyond SL1 (from the stop candle up to the TP1 candle), in points and ATR.
Then a what-if: the same setups with SL1 wider by 0.25 / 0.5 / 0.75 / 1.0 ATR, replayed with the chart's exits
(net change counts the setups the wider stop saves AND the extra loss on the ones that still stop out; setups that
never touched SL1 are not affected by a wider stop).
Cases: MGC 3m, MES 3m (HTF 15m), MGC 2m, MES 2m (HTF 10m), MGC 5m, MES 5m (HTF 25m).
Sources:
  LIVE  real setups that ended "SL1 hit" (Entry / SL1 / TP1 from the Trade Setup alert, stop time from the Setup
        Ended alert), checked against the BarFeed candles.
  SIM   chop_sim.py replay (CBC v10.42 exits per chart; ~50 % exact match with real setups) on the BarFeed archive:
        3m and 5m from 01/05, 2m from 06/01. Thirds = the case's sim SL1 setups split into three equal time blocks.
Usage: python3 sl_reversal_study.py > sl_reversal_report_new.md   (needs chop_sim.py and evening_study.py next to it)
"""
import re, datetime as D, collections
import numpy as np
import chop_sim as cs
import evening_study as ev   # get(), load_bars(), raw(), BASE, TZ; sets the 5m and v10.42 MES 3m exits

CASES = [('MGC', 3), ('MES', 3), ('MGC', 2), ('MES', 2), ('MGC', 5), ('MES', 5)]
NS = list(range(1, 11))
MAXN = NS[-1]
WIDEN = [0.25, 0.5, 0.75, 1.0]
TN = {'flip': 'HTF CBC Flip', 'ltf20': 'LTF EMA20 Pierce', 'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce', 'mom': 'Momentum', 'other': 'other'}


def trig_of(trg):
    return 'flip' if 'HTF CBC Flip' in trg else 'mom' if 'Momentum' in trg else 'ltf20' if 'LTF EMA20' in trg else 'h9' if 'HTF EMA9' in trg else 'h20' if 'HTF EMA20' in trg else 'other'


def sim_exit(s, i, lg, q, sd, tpd):
    """chop_sim.Case.sim1 with an explicit stop distance sd and TP1 distance tpd (points)."""
    C, H, L = s.C, s.H, s.L
    en = C[i]; A = s.atr[i]; g = 1 if lg else -1
    sl = en - g * sd; t1 = en + g * tpd; hit = False; best = 0
    for j in range(i + 1, s.n):
        if (L[j] <= sl if lg else H[j] >= sl):
            rem = g * (sl - en)
            return (q['part'] * tpd + (1 - q['part']) * rem if hit else rem), j, ('trail' if hit else 'SL1')
        if not hit and (H[j] >= t1 if lg else L[j] <= t1):
            hit = True
            if q['be']:
                sl = max(sl, en) if lg else min(sl, en)
        best = max(best, g * ((H[j] if lg else L[j]) - en))
        if hit:
            ns = C[j] - g * q['tr'] * s.atr[j]
            sl = max(sl, ns) if lg else min(sl, ns)
        why = None
        if s.hdir[j] == (0 if lg else 1): why = 'flip'
        elif s.hm[j] == 16 * 60: why = '16:00'
        elif q['ts'] and not hit and j - i == q['ts'] and best < 0.5 * A: why = 'time'
        if why:
            rem = g * (C[j] - en)
            return (q['part'] * tpd + (1 - q['part']) * rem if hit else rem), j, why
    return 0.0, s.n - 1, 'end'


def reversal(s, lg, j, slv, tp, A):
    """For N = 1..MAXN: did candles j+1..j+N reach tp? Returns (first N or None, extra points beyond SL1 until then)."""
    H, L = s.H, s.L
    worst = L[j] if lg else H[j]
    for k in range(1, MAXN + 1):
        m = j + k
        if m >= s.n:
            break
        if (H[m] >= tp) if lg else (L[m] <= tp):
            # adverse extreme up to (and including) the TP candle; the TP candle's own low/high may come after its TP touch,
            # so use the candles before it plus the stop candle (conservative: also include it)
            worst = min(worst, L[m]) if lg else max(worst, H[m])
            extra = (slv - worst) if lg else (worst - slv)
            return k, max(extra, 0.0)
        worst = min(worst, L[m]) if lg else max(worst, H[m])
    return None, None


def live(alerts, sym, tf):
    S, E = {}, {}
    for x in alerts:
        r = ev.raw(x)
        if not r.startswith(sym) or not re.search(r'Chart: \S+\s+%dm' % tf, r):
            continue
        tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
        if not tm:
            continue
        mo, dd, hh, mi = map(int, tm.groups())
        t = D.datetime(int(x['receivedAt'][:4]), mo, dd, hh, mi, tzinfo=ev.TZ)
        if '• Trade Setup:' in r:
            d = re.search(r'Trade Setup: (\w+)', r).group(1)
            en = float(re.search(r'\nEntry: ([\d.]+)', r).group(1))
            k = (t, d, en)
            if k not in S or len(r) > len(S[k]):
                S[k] = r
        elif '• Setup Ended:' in r:
            en = float(re.search(r'Setup Entry: ([\d.]+)', r).group(1))
            st = re.search(r'Started: (\d+):(\d+)', r)
            d = re.search(r'Setup Ended: (\w+)', r).group(1)
            m = re.search(r'Ended: ([^|\n]*?) \| Result: ([+-]?[\d.]+)', r)
            if st and m:
                E[(d, en, int(st.group(1)), int(st.group(2)))] = (m.group(1).strip(), float(m.group(2)), t)
    out = []
    for (t, d, en), r in sorted(S.items()):
        e = E.get((d, en, t.hour, t.minute))
        if not e or not e[0].startswith('SL1'):
            continue
        sl = re.search(r'\nSL1: ([\d.]+)', r); tp = re.search(r'\nTP1: ([\d.]+)', r)
        trg = re.search(r'Trigger: ([^\n]*)', r)
        if not (sl and tp):
            continue
        out.append(dict(t=t, te=e[2], lg=d == 'LONG', en=en, sl=float(sl.group(1)), tp=float(tp.group(1)), res=e[1], trig=trig_of(trg.group(1) if trg else '')))
    return out


def pct(a, b):
    return '%d%%' % round(100 * a / b) if b else '–'


def main():
    now = D.datetime.now(ev.TZ)
    alerts = ev.get(ev.BASE + '/alerts?from=2000-01-01')
    out = ['# Stop-out reversals — SL1 hit, then TP1 within 1–10 candles? — %s' % now.strftime('%a %m/%d/%Y %H:%M ET'), '', __doc__.strip(), '']
    summ = []
    for sym, tf in CASES:
        case = '%s %dm' % (sym, tf)
        q = cs.EXIT[(sym, tf)]
        s = cs.Case(sym, tf, ev.load_bars(sym, tf))
        res = s.run(cs.cur_rule)
        A_ = s.atr
        sl_rows = []
        for r in res:
            if r['why'] != 'SL1':
                continue
            i, lg = r['i'], r['lg']; A = A_[i]; g = 1 if lg else -1
            sd = min(max(q['sl'] * A, q['mn']), q['cap']); tpd = min(q['tp'] * A, 6)
            slv, tp = s.C[i] - g * sd, s.C[i] + g * tpd
            k, extra = reversal(s, lg, r['j'], slv, tp, A)
            sl_rows.append(dict(r=r, k=k, extra=extra, A=A, sd=sd, tpd=tpd))
        n_all, n_sl = len(res), len(sl_rows)
        T = [sl_rows[:n_sl // 3], sl_rows[n_sl // 3:2 * n_sl // 3], sl_rows[2 * n_sl // 3:]]
        # live
        L = live(alerts, sym, tf)
        tix = {int(t): k for k, t in enumerate(s.T)}
        lrows = []
        for x in L:
            i = tix.get(int(x['t'].timestamp() * 1000) - tf * 60000)
            j = tix.get(int(x['te'].timestamp() * 1000) - tf * 60000)
            if i is None or j is None:
                continue
            k, extra = reversal(s, x['lg'], j, x['sl'], x['tp'], A_[i])
            lrows.append(dict(x, i=i, j=j, k=k, extra=extra, A=A_[i], sd=abs(x['en'] - x['sl']), tpd=abs(x['tp'] - x['en'])))
        out += ['## %s — sim %d setups, %d hit SL1 (%s) · live %d SL1 setups (%d matched to bars)' % (case, n_all, n_sl, pct(n_sl, n_all), len(L), len(lrows)), '']
        # reversal rates
        out += ['| Candles after the stop | Sim: reached TP1 | Sim by third | Live: reached TP1 |', '|---|---|---|---|']
        for N in NS:
            c = sum(1 for x in sl_rows if x['k'] and x['k'] <= N)
            th = ' / '.join(pct(sum(1 for x in t if x['k'] and x['k'] <= N), len(t)) for t in T)
            cl = sum(1 for x in lrows if x['k'] and x['k'] <= N)
            out.append('| within %d | %d of %d (%s) | %s | %d of %d (%s) |' % (N, c, n_sl, pct(c, n_sl), th, cl, len(lrows), pct(cl, len(lrows))))
        rev = [x for x in sl_rows if x['k']]
        if rev:
            ea = sorted(x['extra'] / x['A'] for x in rev); ep = sorted(x['extra'] for x in rev)
            q_ = lambda v, p: v[int(p * (len(v) - 1))]
            out += ['', 'Sim setups that reached TP1 within 10 candles: extra distance beyond SL1 needed — median %.2f ATR / %.2f pts, 75 %% %.2f ATR / %.2f pts, 90 %% %.2f ATR / %.2f pts.' % (
                q_(ea, .5), q_(ep, .5), q_(ea, .75), q_(ep, .75), q_(ea, .9), q_(ep, .9))]
            lrev = [x for x in lrows if x['k']]
            if lrev:
                out.append('Live: %s' % '; '.join('%s %s %s +%.2f pts beyond SL1, TP1 %d candle(s) after the stop' % (x['t'].strftime('%m/%d %H:%M'), 'L' if x['lg'] else 'S', TN[x['trig']], x['extra'], x['k']) for x in lrev))
        # by trigger
        out += ['', '**By setup type (sim, reached TP1 within 1 / 10 candles)**', '']
        bt = collections.defaultdict(list)
        for x in sl_rows:
            bt[x['r']['trig']].append(x)
        out.append(', '.join('%s %d SL → %s / %s' % (TN[k], len(v), pct(sum(1 for x in v if x['k'] and x['k'] <= 1), len(v)), pct(sum(1 for x in v if x['k']), len(v))) for k, v in bt.items()))
        # what-if wider stop
        out += ['', '**What-if: SL1 wider by x ATR (setups that hit SL1 replayed; others unchanged)**', '',
                '| Wider by | Sim saved (no longer SL1) | Sim net change | Sim change by third | Live saved | Live net change |', '|---|---|---|---|---|---|']
        for w in WIDEN:
            ch, saved, thc = 0.0, 0, [0.0, 0.0, 0.0]
            idx = {id(x): t for t in range(3) for x in T[t]}
            for x in sl_rows:
                r = x['r']
                nr, _, why = sim_exit(s, r['i'], r['lg'], q, x['sd'] + w * x['A'], x['tpd'])
                d = nr - r['res']; ch += d; thc[idx[id(x)]] += d
                saved += why != 'SL1'
            lch, lsaved = 0.0, 0
            for x in lrows:
                nr, _, why = sim_exit(s, x['i'], x['lg'], q, x['sd'] + w * x['A'], x['tpd'])
                lch += nr - x['res']; lsaved += why != 'SL1'
            mark = ' ✓' if all(v > 0 for v in thc) else ' ⚠' if all(v < 0 for v in thc) else ''
            out.append('| %.2f ATR | %d of %d | %+.1f%s | %s | %d of %d | %+.1f |' % (w, saved, n_sl, ch, mark, ' / '.join('%+.0f' % v for v in thc), lsaved, len(lrows), lch))
            if w == 0.5:
                summ.append('%s: %s of sim SL1 setups reach TP1 within 1 candle, %s within 10 (live %s of %d); SL1 +0.5 ATR → sim %+.0f (thirds %s), live %+.1f' % (
                    case, pct(sum(1 for x in sl_rows if x['k'] and x['k'] <= 1), n_sl), pct(len(rev), n_sl),
                    pct(sum(1 for x in lrows if x['k']), len(lrows)), len(lrows), ch, ' / '.join('%+.0f' % v for v in thc), lch))
        out.append('')
    out += ['## Summary', ''] + ['- ' + x for x in summ] + ['', '✓ = better in all three thirds, ⚠ = worse in all three thirds. Stop widths and minimums also change position size / risk per trade, which this does not account for.']
    print('\n'.join(out))


if __name__ == '__main__':
    main()
