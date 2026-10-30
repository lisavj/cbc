#!/usr/bin/env python3
"""CBC minimum-pullback study: does a minimum pullback from the trend extreme before the entry help?

Pullback (long) = highest high since the move started - entry close (short: entry close - lowest low).
  "since flip" anchor: extreme since the last HTF CBC direction change (bounded to 200 bars).
  "20-bar" anchor:    extreme of the last 20 chart candles (incl. the alert candle).
Measured in points and in ATR(14).

Entries: replayed LTF EMA20 Pierce (cooldown 3), HTF EMA9 Pierce, HTF EMA20 Pierce (spacing 3), session-gated,
same logic as claude/alert_param_sweep.py (validated 76-94 % vs stored alerts). Only with-trend fires are used
(the "Option 2: Reverse" pierces trade against the trend, so a pullback measure does not apply).
Outcomes: (a) exit at first opposite HTF CBC flip / 17:00 ET / 2 h; (b) 1.3 ATR stop / 2.0 ATR target.
Bars: BarFeed archive (3m from 01/05, 2m from 06/01), files <KEY>.json written by the fetch step.
Usage: python3 pullback_study.py  (expects MES.json MGC.json MES_2.json MGC_2.json in the cwd)
"""
import json, sys, datetime as D
from zoneinfo import ZoneInfo

TZ = ZoneInfo('America/New_York')
CASES = [('MGC', 3), ('MES', 3), ('MGC', 2), ('MES', 2)]
PTS = {'MGC': [0, 2, 3, 4, 5, 6, 8, 10, 12, 15], 'MES': [0, 2, 3, 4, 5, 6, 8, 10, 12, 15]}
ATRS = [0, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0]
BUCK = [(0, .5), (.5, 1), (1, 1.5), (1.5, 2), (2, 3), (3, 99)]
TYPES = [('e20', 'LTF EMA20 Pierce'), ('h9', 'HTF EMA9 Pierce'), ('h20', 'HTF EMA20 Pierce')]


def et(ms):
    return D.datetime.fromtimestamp(ms / 1000, TZ)


def in_sess(ms):
    t = et(ms); m = t.hour * 60 + t.minute
    return 18 * 60 <= m < 22 * 60 + 30 or 3 * 60 <= m < 7 * 60 + 45 or 9 * 60 + 30 <= m < 17 * 60


def prep(B):
    n = len(B)
    atr, a = [], None
    for i, b in enumerate(B):
        tr = max(b['h'], B[i - 1]['c']) - min(b['l'], B[i - 1]['c']) if i else b['h'] - b['l']
        a = tr if a is None else (a * 13 + tr) / 14
        atr.append(a)
    sdir, sok = [0] * n, [False] * n
    ok, d0 = False, 0
    for i, b in enumerate(B):
        nb = B[i + 1] if i + 1 < n else None
        d = nb['hf'] if nb is not None and nb.get('hf') in (1, -1) else (1 if b['hc'] == 1 else -1)
        if d != d0:
            ok = b['c'] > b['h20'] if d == 1 else b['c'] < b['h20']; d0 = d
        elif not ok and (b['c'] >= b['h20'] + 1 if d == 1 else b['c'] <= b['h20'] - 1):
            ok = True
        sdir[i], sok[i] = d, ok
    away, aw = [False] * n, False
    for i, b in enumerate(B):
        if b.get('hf') in (1, -1):
            aw = b['c'] > b['h20'] if b['hf'] == 1 else b['c'] < b['h20']
        away[i] = aw
    # start index of the current HTF direction run (for each of the two direction definitions)
    st_hc, st_sd = [0] * n, [0] * n
    for i in range(n):
        st_hc[i] = i if i == 0 or B[i]['hc'] != B[i - 1]['hc'] else st_hc[i - 1]
        st_sd[i] = i if i == 0 or sdir[i] != sdir[i - 1] else st_sd[i - 1]
    return dict(atr=atr, sdir=sdir, sok=sok, away=away, st_hc=st_hc, st_sd=st_sd)


def fires(B, P, key, cool=3):
    out, last = {}, -10 ** 9
    eng = key != 'e20'
    for i in range(1, len(B)):
        b, p = B[i], B[i - 1]
        lv, lp = b.get(key), p.get(key)
        if lv is None or lp is None:
            continue
        if not (b['l'] <= lv <= b['h'] and not (p['l'] <= lp <= p['h']) and i - last > cool and (P['sok'][i] if eng else P['away'][i])):
            continue
        d = P['sdir'][i] if eng else (1 if b['hc'] == 1 else -1)
        if d == 1 and p['l'] > lp or d == -1 and p['h'] < lp:
            last = i
            word = d if (d == 1 and b['c'] >= lv or d == -1 and b['c'] <= lv) else -d
            if in_sess(b['t']):
                out[i] = (word, d)
    return out


def outcome(B, P, i, d, tf):
    b0 = B[i]; en = b0['c']; t_end0 = b0['t'] + tf * 60000
    day17 = et(b0['t']).replace(hour=17, minute=0, second=0, microsecond=0)
    if et(b0['t']).hour >= 17:
        day17 += D.timedelta(days=1)
    e17 = int(day17.timestamp() * 1000)
    ra = rb = None
    for j in range(i + 1, len(B)):
        b = B[j]; te = b['t'] + tf * 60000
        if b.get('hf') == -d or te >= e17 or te - t_end0 >= 2 * 3600000:
            ra = d * (b['c'] - en); break
    A = P['atr'][i]; sl, tp = en - d * 1.3 * A, en + d * 2.0 * A
    for j in range(i + 1, len(B)):
        b = B[j]
        if (b['l'] <= sl if d == 1 else b['h'] >= sl):
            rb = -1.3 * A; break
        if (b['h'] >= tp if d == 1 else b['l'] <= tp):
            rb = 2.0 * A; break
        if b['t'] + tf * 60000 >= e17:
            rb = d * (b['c'] - en); break
    return ra, rb


def rows_for(B, P, key, tf):
    F = fires(B, P, key)
    st = P['st_hc'] if key == 'e20' else P['st_sd']
    R, rev = [], 0
    for i, (word, d) in sorted(F.items()):
        if word != d:
            rev += 1; continue
        ra, rb = outcome(B, P, i, d, tf)
        if ra is None or rb is None:
            continue
        en, A = B[i]['c'], P['atr'][i] or 1
        s = max(st[i], i - 200)
        if d == 1:
            pf = max(b['h'] for b in B[s:i + 1]) - en
            p20 = max(b['h'] for b in B[i - 19:i + 1]) - en
        else:
            pf = en - min(b['l'] for b in B[s:i + 1])
            p20 = en - min(b['l'] for b in B[i - 19:i + 1])
        R.append(dict(t=B[i]['t'], d=d, pf=pf, p20=p20, pfa=pf / A, p20a=p20 / A, A=A, a=ra, b=rb, age=i - st[i]))
    return R, rev


def thirds(R):
    n = len(R)
    return [R[:n // 3], R[n // 3:2 * n // 3], R[2 * n // 3:]]


def sweep(R, fld, grid, unit):
    """Blocking setups with pullback < X: blocked N, blocked net (a)/(b), (b) per third, kept avg (b)."""
    T = thirds(R)
    L = ['| Min %s | Kept | Blocked | Blocked win %% (b) | Blocked net (a) | Blocked net (b) | (b) blocked net by third | Kept avg (a) | Kept avg (b) | Helps? |' % unit,
         '|---|---|---|---|---|---|---|---|---|---|']
    res = []
    for x in grid:
        bl = [r for r in R if r[fld] < x]; kp = [r for r in R if r[fld] >= x]
        if not kp:
            continue
        ba, bb = sum(r['a'] for r in bl), sum(r['b'] for r in bl)
        th = [sum(r['b'] for r in t if r[fld] < x) for t in T]
        tha = [sum(r['a'] for r in t if r[fld] < x) for t in T]
        helps = bl and all(v < 0 for v in th) and all(v < 0 for v in tha)
        w = 100 * sum(r['b'] > 0 for r in bl) / len(bl) if bl else 0
        L.append('| %s | %d | %d | %s | %+.1f | %+.1f | %s | %+.2f | %+.2f | %s |' % (
            x, len(kp), len(bl), ('%.0f' % w) if bl else '–', ba, bb, ' / '.join('%+.0f' % v for v in th),
            sum(r['a'] for r in kp) / len(kp), sum(r['b'] for r in kp) / len(kp), '**yes (all thirds, both rules)**' if helps else ''))
        res.append((x, len(bl), ba, bb, helps))
    return L, res


def buckets(R, fld):
    L = ['| Pullback (ATR) | N | Win % (b) | Avg (a) | Avg (b) | Avg (b) by third |', '|---|---|---|---|---|---|']
    T = thirds(R)
    for lo, hi in BUCK:
        g = [r for r in R if lo <= r[fld] < hi]
        if not g:
            continue
        tt = []
        for t in T:
            gg = [r for r in t if lo <= r[fld] < hi]
            tt.append(('%+.2f' % (sum(r['b'] for r in gg) / len(gg))) if gg else '–')
        L.append('| %s–%s | %d | %.0f | %+.2f | %+.2f | %s |' % (lo, hi if hi < 99 else '∞', len(g), 100 * sum(r['b'] > 0 for r in g) / len(g),
                                                       sum(r['a'] for r in g) / len(g), sum(r['b'] for r in g) / len(g), ' / '.join(tt)))
    return L


def main():
    out = ['# CBC minimum-pullback study -- %s' % D.datetime.now(TZ).strftime('%Y-%m-%d %H:%M ET'), '', __doc__.strip(), '']
    summary = []
    for sym, tf in CASES:
        key = sym if tf == 3 else '%s_%d' % (sym, tf)
        B = json.load(open(key + '.json'))
        B = [b for b in B if all(b.get(k) is not None for k in ('o', 'h', 'l', 'c', 'e20', 'h9', 'h20', 'hc'))]
        P = prep(B)
        out += ['## %s %dm -- bars %s to %s' % (sym, tf, et(B[0]['t']).strftime('%m/%d'), et(B[-1]['t']).strftime('%m/%d')), '']
        for k, name in TYPES:
            R, rev = rows_for(B, P, k, tf)
            if not R:
                continue
            pf = sorted(r['pf'] for r in R); pfa = sorted(r['pfa'] for r in R)
            q = lambda v, p: v[int(p * (len(v) - 1))]
            T = thirds(R)
            out += ['### %s %dm · %s' % (sym, tf, name), '',
                    'With-trend fires: %d (reverse pierces excluded: %d). All: (a) %+.1f, (b) %+.1f. Thirds split at %s / %s.' % (
                        len(R), rev, sum(r['a'] for r in R), sum(r['b'] for r in R), et(T[1][0]['t']).strftime('%m/%d'), et(T[2][0]['t']).strftime('%m/%d')),
                    'Pullback since flip: median %.1f pts / %.2f ATR (25 %%: %.1f / %.2f, 75 %%: %.1f / %.2f).' % (
                        q(pf, .5), q(pfa, .5), q(pf, .25), q(pfa, .25), q(pf, .75), q(pfa, .75)), '']
            out += ['**Outcome by pullback depth (since flip, ATR)**', ''] + buckets(R, 'pfa') + ['']
            Lp, rp = sweep(R, 'pf', PTS[sym], 'pts (since flip)')
            La, ra = sweep(R, 'pfa', ATRS, 'ATR (since flip)')
            L2, r2 = sweep(R, 'p20a', ATRS, 'ATR (20-bar high/low)')
            out += ['**Minimum pullback in points (since flip)**', ''] + Lp + ['', '**Minimum pullback in ATR (since flip)**', ''] + La + \
                   ['', '**Minimum pullback in ATR (20-bar extreme)**', ''] + L2 + ['']
            good = [('%s pts' % x) for x, n, a, b, h in rp if h] + [('%s ATR' % x) for x, n, a, b, h in ra if h] + [('%s ATR (20-bar)' % x) for x, n, a, b, h in r2 if h]
            summary.append((sym, tf, name, len(R), good, ra))
    out += ['## Summary', '']
    for sym, tf, name, n, good, ra in summary:
        best = min(ra, key=lambda r: r[3])
        out.append('- %s %dm %s (%d fires): %s; largest (b) gain from ATR floor %s (blocks %d, blocked net (b) %+.1f).' % (
            sym, tf, name, n, ('helps in all thirds: ' + ', '.join(good)) if good else 'no floor helps in all thirds', best[0], best[1], best[3]))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
