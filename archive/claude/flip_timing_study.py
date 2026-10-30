#!/usr/bin/env python3
"""CBC flip-timing study: how long after the HTF CBC flip are setups entered and exited, and does it matter?

For every setup: (1) time from the HTF CBC flip that started the current trend direction to the ENTRY candle,
(2) hold time ENTRY -> EXIT, (3) time from the flip to the EXIT. In minutes and in HTF candles (3m chart -> 15m HTF,
2m chart -> 10m HTF). Flip = the last chart candle where the confirmed HTF CBC (bar field hc) changed to the trade
direction, at or before the entry candle.
Cases: MGC 3m, MES 3m (HTF 15m), MGC 2m, MES 2m (HTF 10m), MGC 5m, MES 5m (HTF 25m; base exits, no gates -- set in evening_study.py). Sources:
  LIVE  real Trade Setup alerts matched to their Setup Ended results ("Lasted" and the exit time come from the alert).
  SIM   chop_sim.py replay (current CBC-style rules + exits, ~50 % exact match with real setups) on the BarFeed
        archive: 3m and 5m from 01/05, 2m from 06/01. Use it to compare buckets, not for exact totals.
Each chart also gets a table splitting entry timing by session (Asia 18:00–03:00, London 03:00–09:30, NY 09:30–16:00 ET).
Thirds = the case's sim setups split into three equal time blocks. A cell is "⚠ weak" with >= 20 sim setups
negative in all three thirds, "✓ strong" with >= 20 positive in all three thirds.
Usage: python3 flip_timing_study.py > flip_timing_report_new.md   (needs chop_sim.py and evening_study.py next to it)
"""
import re, json, datetime as D, collections
import numpy as np
import chop_sim as cs
import evening_study as ev   # reuses get(), load_bars(), raw(), BASE, TZ

CASES = [('MGC', 3), ('MES', 3), ('MGC', 2), ('MES', 2), ('MGC', 5), ('MES', 5)]
TN = {'flip': 'HTF CBC Flip', 'ltf20': 'LTF EMA20 Pierce', 'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}
ENTRY_B = [(0, 1, 'flip candle (0)'), (1, 2, '1'), (2, 3, '2'), (3, 5, '3–4'), (5, 9, '5–8'), (9, 17, '9–16'), (17, 33, '17–32'), (33, 10 ** 9, '33+')]
HOLD_B = [(0, 15, '< 15 min'), (15, 30, '15–30'), (30, 60, '30–60'), (60, 120, '1–2 h'), (120, 240, '2–4 h'), (240, 10 ** 9, '4 h+')]


def trig_of(trg):
    return 'flip' if 'HTF CBC Flip' in trg else 'mom' if 'Momentum' in trg else 'ltf20' if 'LTF EMA20' in trg else 'h9' if 'HTF EMA9' in trg else 'h20' if 'HTF EMA20' in trg else 'other'


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
        if not e:
            continue
        trg = re.search(r'Trigger: ([^\n]*)', r)
        hold = (e[2] - t).total_seconds() / 60
        if hold < 0:
            hold += 1440  # exit after midnight with a date line from the next day is handled by the date; guard only
        out.append(dict(t=t, lg=d == 'LONG', trig=trig_of(trg.group(1) if trg else ''), res=e[1], why=e[0], hold=hold))
    return out


def flip_index(hc):
    """st[i] = first chart candle of the current confirmed-HTF-CBC run containing i."""
    st = np.zeros(len(hc), int)
    for i in range(1, len(hc)):
        st[i] = i if hc[i] != hc[i - 1] else st[i - 1]
    return st


def f(g):
    if not g:
        return '–'
    return '%d · %d%% · %+.1f' % (len(g), round(100 * sum(x['res'] > 0 for x in g) / len(g)), sum(x['res'] for x in g))


def med(v):
    return ('%.0f' % float(np.median(v))) if v else '–'


def table(rows, sim, tid, key, B, live_rows, unit):
    L = ['| %s | Sim all | Sim avg | Sim thirds | Live all | ' % unit + ' | '.join('Sim %s' % TN[k] for k in TN) + ' |', '|' + '---|' * (5 + len(TN))]
    flags = []
    for lo, hi, lab in B:
        g = [r for r in sim if lo <= r[key] < hi]
        th = [sum(r['res'] for r in g if id(r) in tid[j]) for j in range(3)]
        mk = ' ⚠ weak' if len(g) >= 20 and all(x < 0 for x in th) else ' ✓ strong' if len(g) >= 20 and all(x > 0 for x in th) else ''
        if mk == ' ⚠ weak':
            flags.append('%s %s: %s, thirds %s' % (unit, lab, f(g), ' / '.join('%+.0f' % x for x in th)))
        cells = []
        for k in TN:
            gk = [r for r in g if r['trig'] == k]
            tk = [sum(r['res'] for r in gk if id(r) in tid[j]) for j in range(3)]
            m2 = ' ⚠' if len(gk) >= 20 and all(x < 0 for x in tk) else ' ✓' if len(gk) >= 20 and all(x > 0 for x in tk) else ''
            if m2 == ' ⚠':
                flags.append('%s %s %s: %s, thirds %s' % (unit, lab, TN[k], f(gk), ' / '.join('%+.0f' % x for x in tk)))
            cells.append(f(gk) + m2)
        lg = [r for r in live_rows if r.get(key) is not None and lo <= r[key] < hi]
        L.append('| %s | %s%s | %s | %s | %s | %s |' % (lab, f(g), mk, ('%+.2f' % (sum(r['res'] for r in g) / len(g))) if g else '–',
                                                    ' / '.join('%+.0f' % x for x in th) if g else '–', f(lg), ' | '.join(cells)))
    return L, flags


def main():
    now = D.datetime.now(ev.TZ)
    alerts = ev.get(ev.BASE + '/alerts?from=2000-01-01')
    out = ['# Flip timing — entry and exit relative to the HTF CBC flip — %s' % now.strftime('%a %m/%d/%Y %H:%M ET'), '', __doc__.strip(), '',
           'Cells: setups · win % · net pts.', '']
    allflags = []
    for sym, tf in CASES:
        case = '%s %dm' % (sym, tf)
        htf = 5 * tf
        B = ev.load_bars(sym, tf)
        s = cs.Case(sym, tf, B)
        st = flip_index(s.hdir)
        res = s.run(cs.cur_rule)
        for r in res:
            i, j = r['i'], r['j']
            r['since'] = (i - st[i]) * tf / htf          # HTF candles from flip to entry
            r['since_min'] = (i - st[i]) * tf
            r['hold'] = (j - i) * tf
            r['flip2exit'] = (j - st[i]) * tf
        n = len(res)
        T = [res[:n // 3], res[n // 3:2 * n // 3], res[2 * n // 3:]]
        tid = [{id(r) for r in t} for t in T]
        # live: flip from the bars
        L = live(alerts, sym, tf)
        tix = {int(t): k for k, t in enumerate(s.T)}
        for r in L:
            i = tix.get(int(r['t'].timestamp() * 1000) - tf * 60000)
            if i is None:
                r['since'] = None
                continue
            r['since'] = (i - st[i]) * tf / htf
            r['since_min'] = (i - st[i]) * tf
            r['flip2exit'] = r['since_min'] + r['hold']
        Lk = [r for r in L if r['since'] is not None]
        out += ['## %s (HTF %dm) — sim %s → %s, %d setups · live %d setups (%d matched to bars)' % (case, htf, s.date[0][:5], s.date[-1][:5], n, len(L), len(Lk)), '']
        out += ['Median minutes — sim: flip→entry %s, hold %s, flip→exit %s · live: flip→entry %s, hold %s, flip→exit %s' % (
            med([r['since_min'] for r in res]), med([r['hold'] for r in res]), med([r['flip2exit'] for r in res]),
            med([r['since_min'] for r in Lk]), med([r['hold'] for r in L]), med([r['flip2exit'] for r in Lk])), '']
        out += ['Median flip→entry by trigger (sim, minutes): ' + ', '.join('%s %s' % (TN[k], med([r['since_min'] for r in res if r['trig'] == k])) for k in TN), '']
        t1, fl1 = table(None, res, tid, 'since', ENTRY_B, Lk, 'HTF candles flip→entry')
        out += ['**Entry: HTF candles since the flip**', ''] + t1 + ['']
        t2, fl2 = table(None, res, tid, 'hold', HOLD_B, L, 'Hold time')
        out += ['**Exit: hold time entry→exit**', ''] + t2 + ['']
        # exit reasons by entry timing (sim)
        out += ['**How setups end, by entry timing (sim)**', '', '| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |', '|---|---|---|---|---|---|---|']
        for lo, hi, lab in ENTRY_B:
            g = [r for r in res if lo <= r['since'] < hi]
            if not g:
                continue
            c = collections.Counter(r['why'] for r in g)
            pct = lambda k: '%d%%' % round(100 * c.get(k, 0) / len(g))
            other = len(g) - c.get('SL1', 0) - c.get('trail', 0) - c.get('flip', 0)
            out.append('| %s | %d | %s | %s | %s | %d%% | %s |' % (lab, len(g), pct('SL1'), pct('trail'), pct('flip'), round(100 * other / len(g)), med([r['hold'] for r in g])))
        out.append('')
        # session view: entry timing by session (entry candle open time, ET)
        for r in res:
            r['om'] = (s.hm[r['i']] - tf) % 1440
        for r in Lk:
            r['om'] = (r['t'].hour * 60 + r['t'].minute - tf) % 1440
        SES = [('Asia 18:00–03:00', lambda m: m >= 18 * 60 or m < 3 * 60), ('London 03:00–09:30', lambda m: 3 * 60 <= m < 9 * 60 + 30), ('NY 09:30–16:00', lambda m: 9 * 60 + 30 <= m < 16 * 60)]
        GB = [(0, 1, 'flip candle'), (1, 5, '1–4'), (5, 9, '5–8'), (9, 10 ** 9, '9+')]
        out += ['**Entry timing by session** (sim N · win · net, thirds · live N · win · net)', '', '| Session | All | ' + ' | '.join('%s HTF candles' % g[2] for g in GB) + ' |', '|' + '---|' * (2 + len(GB))]
        for sn, sf in SES:
            g = [r for r in res if sf(r['om'])]
            gl = [r for r in Lk if sf(r['om'])]
            cells = []
            for lo, hi, lab in GB:
                gg = [r for r in g if lo <= r['since'] < hi]
                th = [sum(r['res'] for r in gg if id(r) in tid[j]) for j in range(3)]
                mk = ' ⚠' if len(gg) >= 20 and all(x < 0 for x in th) else ' ✓' if len(gg) >= 20 and all(x > 0 for x in th) else ''
                if mk == ' ⚠':
                    fl1.append('%s %s HTF candles after the flip: %s, thirds %s' % (sn, lab, f(gg), ' / '.join('%+.0f' % x for x in th)))
                gl2 = [r for r in gl if lo <= r['since'] < hi]
                cells.append('%s%s (%s) · live %s' % (f(gg), mk, ' / '.join('%+.0f' % x for x in th) if gg else '–', f(gl2)))
            out.append('| %s | %s · live %s | %s |' % (sn, f(g), f(gl), ' | '.join(cells)))
        out.append('')
        allflags += ['%s · %s' % (case, x) for x in fl1 + fl2]
    out += ['## Flags (weak cells: ≥ 20 sim setups, negative in all thirds)', ''] + (['- ' + x for x in allflags] if allflags else ['- none'])
    print('\n'.join(out))


if __name__ == '__main__':
    main()
