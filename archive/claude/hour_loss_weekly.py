#!/usr/bin/env python3
"""Weekly loser-rate-by-hour study for every CBC chart (2m / 3m / 5m, all symbols) from the Alert Feed.

Uses the REAL results in "Setup Ended" alerts (no replay -- each chart has its own exits). For each symbol x chart
timeframe x New York hour (hour of the setup candle's open): setups, loser % (result < 0), net pts, loser % in the
first / second half of that chart's setups, and the last 7 days. Flags:
  !! = loser % > 50 in BOTH halves and n >= 5 (consistent losing hour)
  !  = loser % > 50 overall and n >= 5 (one half only)
Also lists 2-3 hour blocks of adjacent !! / ! hours. Usage: python3 hour_loss_weekly.py [days]  (default: all stored)
"""
import json, re, sys, urllib.request, datetime as D, collections
from zoneinfo import ZoneInfo
TZ = ZoneInfo('America/New_York')
URL = 'https://tv-webhook-dashboard.onrender.com/alerts'
TFS = ('2m', '3m', '5m')

def get():
    err = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(URL, timeout=150) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            err = e
    raise err

def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else None
    A = get()
    now = D.datetime.now(TZ)
    S = {}
    for x in A:
        r = x['raw'] if isinstance(x.get('raw'), str) else ''
        if '• Setup Ended:' not in r:
            continue
        ch = re.search(r'Chart: (\S+)\s+(\d+m)', r)
        tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
        st = re.search(r'Started: (\d+):(\d+)', r)
        rs = re.search(r'Result: ([+-]?[\d.]+)', r)
        en = re.search(r'Setup Entry: ([\d.]+)', r)
        if not (ch and tm and st and rs and en) or ch.group(2) not in TFS:
            continue
        sym = re.sub(r'\d*!$', '', ch.group(1)).rstrip('1')
        mo, dd, hh, mi = map(int, tm.groups())
        sh, sm = int(st.group(1)), int(st.group(2))
        yr = now.year - (1 if mo > now.month else 0)
        day = D.date(yr, mo, dd) - (D.timedelta(days=1) if (sh, sm) > (hh, mi) else D.timedelta(0))
        t = D.datetime(day.year, day.month, day.day, sh, sm, tzinfo=TZ) - D.timedelta(minutes=int(ch.group(2)[:-1]))
        if days and t < now - D.timedelta(days=days):
            continue
        S[(sym, ch.group(2), t, float(en.group(1)))] = float(rs.group(1))
    G = collections.defaultdict(list)
    for (sym, tf, t, _), res in S.items():
        G[(sym, tf)].append((t, res))
    L = ['# CBC loser rate by hour -- all charts -- %s' % now.strftime('%a %m/%d/%Y %H:%M ET'), '',
         'Real results from "Setup Ended" alerts (no replay; each chart keeps its own exits). Hour = New York hour of the setup candle open. '
         'Loser = result < 0. **!!** = loser % > 50 in both halves, n >= 5. **!** = > 50 % overall, n >= 5. "7d" = last 7 days.', '']
    summary = []
    for key in sorted(G, key=lambda k: (k[0], int(k[1][:-1]))):
        R = sorted(G[key])
        n = len(R); h = n // 2
        recent = now - D.timedelta(days=7)
        tot_l = sum(r < 0 for _, r in R)
        L += ['## %s %s -- %d setups (%s - %s), losers %d%%, net %+.1f pts' % (key[0], key[1], n, R[0][0].strftime('%m/%d'), R[-1][0].strftime('%m/%d'),
              round(100 * tot_l / n), sum(r for _, r in R)), '',
              '| Hour ET | n | Losers | Net | 1st half | 2nd half | 7d (n) | Flag |', '|---|---|---|---|---|---|---|---|']
        H = collections.defaultdict(list)
        for k, (t, r) in enumerate(R):
            H[t.hour].append((k < h, t >= recent, r))
        flags = {}
        for hr in sorted(H):
            v = H[hr]; a = [x[2] for x in v]; f = [x[2] for x in v if x[0]]; b = [x[2] for x in v if not x[0]]; w = [x[2] for x in v if x[1]]
            pc = lambda q: '%d%%' % round(100 * sum(r < 0 for r in q) / len(q)) if q else '-'
            lo = lambda q: q and sum(r < 0 for r in q) / len(q) > 0.5
            fl = '!!' if len(a) >= 5 and lo(f) and lo(b) else '!' if len(a) >= 5 and lo(a) else ''
            flags[hr] = (fl, len(a), sum(a))
            L.append('| %02d-%02d | %d | %s | %+.1f | %s (%d) | %s (%d) | %s (%d) | %s |' % (hr, (hr + 1) % 24, len(a), pc(a), sum(a), pc(f), len(f), pc(b), len(b), pc(w), len(w), fl))
        L.append('')
        for hr, (fl, cnt, net) in sorted(flags.items()):
            if fl:
                summary.append((key[0], key[1], hr, fl, cnt, net))
    L += ['## Summary: flagged hours', '']
    if summary:
        L += ['| Chart | Hour ET | Flag | n | Net |', '|---|---|---|---|---|']
        L += ['| %s %s | %02d-%02d | %s | %d | %+.1f |' % (s, tf, hr, (hr + 1) % 24, fl, cnt, net) for s, tf, hr, fl, cnt, net in summary]
        # adjacent flagged hours -> blocks
        L += ['', 'Blocks (adjacent flagged hours, same chart):']
        by = collections.defaultdict(list)
        for s, tf, hr, fl, cnt, net in summary:
            by[(s, tf)].append((hr, cnt, net))
        for k, v in sorted(by.items()):
            v.sort(); blk = [v[0]]
            for x in v[1:] + [None]:
                if x and x[0] == blk[-1][0] + 1:
                    blk.append(x); continue
                if len(blk) >= 2:
                    L.append('- %s %s %02d:00-%02d:00: %d setups, %+.1f pts' % (k[0], k[1], blk[0][0], blk[-1][0] + 1, sum(b[1] for b in blk), sum(b[2] for b in blk)))
                if x: blk = [x]
    else:
        L.append('No hour with n >= 5 and loser % > 50.')
    print('\n'.join(L))

if __name__ == '__main__':
    main()
