#!/usr/bin/env python3
"""CBC Stop Management sweep -- "Breakeven + Step Trail: Custom points" x "Max Loss Per Trade: points".

Replays CBC's LTF+HTF Agreement entries (confirmed HTF) from BarFeed bars and manages each trade with CBC's
own LTF Trailing Stop (pine CBC v10.36, lines ~3261-3300 + 3400):
  * LTF CBC state: close > high[1] -> long, close < low[1] -> short (f_cbc_state).
  * HTF = 5 x chart TF (3m->15m, 2m->10m, 5m->25m), session-anchored at 18:00 ET; confirmed HTF CBC known on the
    first LTF bar after the HTF bar closes (matches the live alerts in the feed).
  * Agreement entry: LTF CBC == confirmed HTF CBC on this bar, no agreement (either side) on the previous bar, one per
    direction per closed-HTF bar; Max Loss ON skips it when |close - trail stop| > X.
  * Trail stop: ratchet of the prior LTF candle low (long) / high (short) since the last LTF flip; BE + step trail with
    step S (auto MES/MGC 5, MNQ 30, M2K 3): steps = floor(MFE / S) from the LTF flip close; managed = flip close +
    (steps-1) x S; stop = the more protective of the two.
  * Exit: (touch) the stop shown at the previous close is touched -> fill at stop (or the open if gapped through);
    (close) a close beyond it. Also exit at the close on an LTF CBC flip against the trade, 17:00 ET, or a > 30 min
    data gap. P&L in points, no commission/slippage.
Usage: python3 stop_sweep.py [cache_dir]   (fetches /bars and /alerts from the Render dashboard when no cache given)
"""
import gzip, json, os, re, sys, urllib.request, datetime as D
from zoneinfo import ZoneInfo

BASE = 'https://tv-webhook-dashboard.onrender.com'
TZ = ZoneInfo('America/New_York')
CASES = [('MES', 3), ('MGC', 3), ('MNQ', 3), ('MES', 2), ('MGC', 2), ('MES', 5), ('MGC', 5), ('MNQ', 5)]
AUTO = {'MES': 5.0, 'MGC': 5.0, 'MNQ': 30.0, 'M2K': 3.0}
S_GRID = {'MES': [0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15], 'MGC': [0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15],
          'MNQ': [0, 2, 3, 5, 8, 10, 15, 20, 25, 30, 40, 50, 60, 80]}          # 0 = Breakeven + Step Trail unchecked
X_GRID = {'MES': [None, 2, 3, 4, 5, 6, 8, 10, 12, 15], 'MGC': [None, 2, 3, 4, 5, 6, 8, 10, 12, 15],
          'MNQ': [None, 10, 15, 20, 25, 30, 40, 50, 60, 80]}          # None = Max Loss unchecked
USD = {'MES': 5, 'MGC': 10, 'MNQ': 2}
# round-trip cost in points: 1 tick slippage on the exit + ~$1.24 commission (MES .25+.25, MGC .1+.12, MNQ .25+.62)
COST = {'MES': 0.5, 'MGC': 0.22, 'MNQ': 0.87}


def get(url, tries=4):
    import time
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=300) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(30)


def load(cache, name, url):
    p = os.path.join(cache, name) if cache else None
    if p and os.path.exists(p):
        return json.load(open(p))
    d = get(url)
    if p:
        json.dump(d, open(p, 'w'))
    return d


def prep(B, tf):
    n = len(B)
    o = [b['o'] for b in B]; h = [b['h'] for b in B]; l = [b['l'] for b in B]; c = [b['c'] for b in B]
    t = [b['t'] for b in B]
    et = [D.datetime.fromtimestamp(x / 1000, TZ) for x in t]
    # LTF CBC
    cbc = [False] * n
    for i in range(1, n):
        s = cbc[i - 1]
        if s and c[i] < l[i - 1]: s = False
        if not s and c[i] > h[i - 1]: s = True
        cbc[i] = s
    # HTF buckets anchored 18:00 ET
    H = tf * 5
    def bucket(i):
        x = et[i]
        base = x.replace(hour=18, minute=0, second=0, microsecond=0)
        if x < base: base -= D.timedelta(days=1)
        return (base.date(), int((x - base).total_seconds() // 60) // H)
    bk = [bucket(i) for i in range(n)]
    groups = []  # (start, end)
    s0 = 0
    for i in range(1, n + 1):
        if i == n or bk[i] != bk[s0]:
            groups.append((s0, i - 1)); s0 = i
    # HTF CBC per group, confirmed index
    hd = [None] * n         # confirmed HTF dir (True long) known at bar i close
    hid = [-1] * n          # id of last closed HTF bar
    flipbar = [False] * n   # confirmed HTF flip registered on this bar
    st = False; ph = pl = None; cur = None; cid = -1
    events = {}
    for g, (a, b) in enumerate(groups):
        gh, gl, gc = max(h[a:b + 1]), min(l[a:b + 1]), c[b]
        if ph is not None:
            if st and gc < pl: st = False
            if not st and gc > ph: st = True
        ph, pl = gh, gl
        end_ok = (t[b] + tf * 60000 - t[a]) >= 0 and ((et[b] + D.timedelta(minutes=tf)).minute % H == 0 or H % 60 != 0)
        # complete when last bar ends at the bucket end; otherwise register on the next group's first bar
        x = et[b] + D.timedelta(minutes=tf)
        base = x.replace(hour=18, minute=0, second=0, microsecond=0)
        if x < base: base -= D.timedelta(days=1)
        complete = int((x - base).total_seconds() // 60) % H == 0
        # live CBC sees the confirmed HTF bar on the first LTF bar AFTER it closes (feed: 04:45-04:48 bar for the 04:30-04:45 HTF bar)
        reg = groups[g + 1][0] if g + 1 < len(groups) else None
        if reg is not None and g >= 1:
            events.setdefault(reg, []).append((g, st))
    for i in range(n):
        if i in events:
            for g, s in events[i]:
                if cur is not None and s != cur: flipbar[i] = True
                cur = s; cid = g
        hd[i] = cur; hid[i] = cid
    # ratchet stop + flip entry + MFE
    rat = [None] * n; fen = [None] * n; mfe = [None] * n
    r = e = m = None
    for i in range(1, n):
        lo1, hi1 = l[i - 1], h[i - 1]
        base = lo1 if cbc[i] else hi1
        flip = cbc[i] != cbc[i - 1]
        if flip:
            e = c[i]; m = c[i]; r = base
        else:
            if m is not None:
                m = max(m, h[i]) if cbc[i] else min(m, l[i])
            if r is not None:
                r = max(r, base) if cbc[i] else min(r, base)
        rat[i], fen[i], mfe[i] = r, e, m
    gap = [False] * n
    for i in range(n - 1):
        gap[i] = (t[i + 1] - t[i]) > 30 * 60000
    gap[n - 1] = True
    eod = [(x + D.timedelta(minutes=tf)).hour == 17 and (x + D.timedelta(minutes=tf)).minute == 0 for x in et]
    return dict(o=o, h=h, l=l, c=c, t=t, et=et, cbc=cbc, hd=hd, hid=hid, flipbar=flipbar, rat=rat, fen=fen, mfe=mfe,
                gap=gap, eod=eod, n=n)


def trail(P, S):
    n = P['n']; out = [None] * n
    for i in range(n):
        r, e, m = P['rat'][i], P['fen'][i], P['mfe'][i]
        if r is None:
            continue
        lg = P['cbc'][i]
        ms = None
        if S > 0 and e is not None:
            fav = (m - e) if lg else (e - m)
            k = int(fav // S)
            if k >= 1:
                ms = e + (k - 1) * S * (1 if lg else -1)
        out[i] = r if ms is None else (max(r, ms) if lg else min(r, ms))
    return out


def entries(P):
    n = P['n']; cbc, hd, hid = P['cbc'], P['hd'], P['hid']
    ag = [hd[i] is not None and cbc[i] == hd[i] for i in range(n)]
    E = []; last = {True: -2, False: -2}
    for i in range(2, n - 1):
        if ag[i] and not ag[i - 1] and hid[i] != last[cbc[i]]:
            E.append(i)   # dedup bookkeeping is applied per X in sweep (skipped entries don't update it)
    return E, ag


def run(P, S, X, mode, E_all):
    o, h, l, c, cbc = P['o'], P['h'], P['l'], P['c'], P['cbc']
    ts = P['_ts'][S]
    res = []; last = {True: -2, False: -2}; ag = P['_ag']; hid = P['hid']
    for e in E_all:
        lg = cbc[e]
        if hid[e] == last[lg]:
            continue
        stp = ts[e]
        if X is not None and stp is not None and abs(c[e] - stp) > X:
            continue
        last[lg] = hid[e]; last[not lg] = -2
        en = c[e]; ex = None; why = ''
        j = e
        while ex is None:
            j += 1
            if j >= P['n']:
                ex, why = c[j - 1], 'end'; j -= 1; break
            s = ts[j - 1]
            if mode == 'touch' and s is not None and (l[j] <= s if lg else h[j] >= s):
                ex = min(o[j], s) if lg else max(o[j], s); why = 'stop'
            elif mode == 'close' and s is not None and (c[j] < s if lg else c[j] > s):
                ex, why = c[j], 'stop'
            elif cbc[j] != lg:
                ex, why = c[j], 'flip'
            elif P['eod'][j] or P['gap'][j]:
                ex, why = c[j], 'eod'
        pts = (ex - en) if lg else (en - ex)
        res.append((P['t'][e], pts, why, abs(en - stp) if stp is not None else 0.0, j - e))
    return res


def stats(R, t_split=None):
    if not R:
        return dict(n=0, win=0, avg=0, net=0, pf=0, dd=0, h=(0, 0), th=(0, 0, 0), rec=0, bars=0)
    p = [x[1] for x in R]
    gw = sum(x for x in p if x > 0); gl = -sum(x for x in p if x < 0)
    eq = pk = dd = 0
    for x in p:
        eq += x; pk = max(pk, eq); dd = min(dd, eq - pk)
    n = len(p); h1 = sum(p[:n // 2]); h2 = sum(p[n // 2:])
    th = (sum(p[:n // 3]), sum(p[n // 3:2 * n // 3]), sum(p[2 * n // 3:]))
    rec = sum(x[1] for x in R if t_split and x[0] >= t_split)
    return dict(n=n, win=100 * sum(x > 0 for x in p) / n, avg=sum(p) / n, net=sum(p), pf=gw / gl if gl else 99,
                dd=dd, h=(h1, h2), th=th, rec=rec, nrec=sum(1 for x in R if t_split and x[0] >= t_split),
                bars=sum(x[4] for x in R) / n)


def flags(s):
    f = ''
    if s['h'][0] > 0 and s['h'][1] > 0: f += '✱'
    if all(x > 0 for x in s['th']): f += 'T'
    return f


def validate(P, sym, tf, alerts, E_all):
    """Stored 'HTF(..) CBC Flip + LTF(..) Agreement' alerts vs replayed agreement entries on a confirmed HTF flip bar."""
    got = set()
    for x in alerts:
        r = x['raw'] if isinstance(x['raw'], str) else json.dumps(x['raw'])
        if not r.startswith(sym) or 'CBC Flip + LTF(' not in r or not re.search(r'Chart: \S+\s+%dm' % tf, r):
            continue
        m = re.search(r'Agreement: (LONG|SHORT) \(confirmed', r)
        tm = re.search(r'Time: (\d+)/(\d+) \d+:\d+-(\d+):(\d+)', r)
        if not m or not tm:
            continue
        yr = int(x['receivedAt'][:4]); mo, dd, hh, mi = map(int, tm.groups())
        got.add((D.datetime(yr, mo, dd, hh, mi, tzinfo=TZ), m.group(1) == 'LONG'))
    if not got:
        return None
    t0 = min(g[0] for g in got) - D.timedelta(minutes=1)
    t1 = max(g[0] for g in got) + D.timedelta(minutes=1)
    rep = set()
    for e in E_all:
        if P['flipbar'][e]:
            ct = P['et'][e] + D.timedelta(minutes=tf)
            if t0 <= ct <= t1:
                rep.add((ct, P['cbc'][e]))
    both = len(got & rep)
    return len(got), len(rep), both


def main():
    cache = sys.argv[1] if len(sys.argv) > 1 else None
    if cache: os.makedirs(cache, exist_ok=True)
    alerts = load(cache, 'alerts.json', BASE + '/alerts?from=2000-01-01')
    now = D.datetime.now(TZ)
    L = ['# CBC Stop Management sweep -- %s' % now.strftime('%Y-%m-%d %H:%M ET'), '',
         'Replay of the **HTF CBC Flip + LTF Agreement** entry alert (the Agreement alert your feed receives; 94-100 % of stored ones are reproduced) managed by CBC\'s **LTF Trailing Stop**. '
         'S = "Breakeven + Step Trail -> Custom points" (0 in CBC = auto: MES/MGC 5, MNQ 30; **off** = BE+Step unchecked). '
         'X = "Max Loss Per Trade" points (skip the entry when |close - stop| > X; **off** = unchecked). '
         'Exit "touch" = stop touched (fill at stop/open); "close" = candle closes beyond it; both also exit on an LTF CBC flip, 17:00 ET or a data gap. '
         'Points per contract; "net after costs" subtracts 1 tick exit slippage + ~$1.24 commission per trade (MES 0.5, MGC 0.22, MNQ 0.87 pts). ✱ = positive in both halves, T = positive in all three thirds. Recent = last 20 calendar days.', '',
         '> Note: with the Max Loss box **checked and Points = 0**, every Agreement entry alert whose stop is not exactly at the close is skipped '
         '(i.e. almost all of them). Leave it unchecked or set a real number.', '']
    summary = []
    for sym, tf in CASES:
        key = sym if tf == 3 else '%s_%d' % (sym, tf)
        try:
            B = load(cache, key + '.json', '%s/bars?sym=%s&days=60&from=2026-01-01' % (BASE, key))['bars']
        except Exception as ex:
            L += ['## %s %dm' % (sym, tf), '', 'error loading bars: %s' % ex, '']
            continue
        if len(B) < 500:
            continue
        P = prep(B, tf)
        E_any, ag = entries(P)
        P['_ag'] = ag
        E_all = [e for e in E_any if P['flipbar'][e]]   # HTF CBC Flip + LTF Agreement (combo alert)
        auto = AUTO.get(sym, 5.0)
        P['_ts'] = {S: trail(P, S if S > 0 else 0) for S in S_GRID[sym]}
        t_rec = int((now - D.timedelta(days=20)).timestamp() * 1000)
        d0 = P['et'][0].strftime('%m/%d'); d1 = P['et'][-1].strftime('%m/%d')
        L += ['## %s %dm  (bars %s → %s, HTF %dm)' % (sym, tf, d0, d1, tf * 5), '']
        v = validate(P, sym, tf, alerts, E_all)
        sa = stats(run(P, auto, None, 'touch', E_any), t_rec)
        L += ['All Agreement starts (incl. LTF joining an existing HTF trend, alert option "LTF join" -- not in your feed): %d trades, net %+.1f, avg %+.2f, win %.0f %% at S auto / no max loss.' % (sa['n'], sa['net'], sa['avg'], sa['win']), '']
        if v:
            L += ['Validation (HTF flip + Agreement alerts in the feed vs replay, same window): stored %d · replayed %d · matched %d (%.0f %% of stored).' % (v[0], v[1], v[2], 100 * v[2] / v[0]), '']
        # A: S sweep, X off, both modes
        L += ['**A. Custom points sweep (Max Loss off)**', '',
              '| S | mode | trades | win % | avg | net | net after costs | PF | max DD | halves | thirds | recent (n) | flags |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        best = {}
        for mode in ('touch', 'close'):
            for S in S_GRID[sym]:
                s = stats(run(P, S, None, mode, E_all), t_rec)
                lab = 'off' if S == 0 else ('%g (auto)' % S if S == auto else '%g' % S)
                L.append('| %s | %s | %d | %.0f | %+.2f | %+.1f | %+.1f | %.2f | %.1f | %+.0f / %+.0f | %+.0f / %+.0f / %+.0f | %+.1f (%d) | %s |' % (
                    lab, mode, s['n'], s['win'], s['avg'], s['net'], s['net'] - s['n'] * COST[sym], s['pf'], s['dd'], s['h'][0], s['h'][1], *s['th'], s['rec'], s['nrec'], flags(s)))
                best.setdefault(mode, []).append((s['net'], S, s))
        L.append('')
        # B: X sweep at auto S, touch
        L += ['**B. Max Loss sweep (S = auto %g, touch exits)**' % auto, '',
              '| X | trades | skipped | win % | avg | net | net after costs | PF | max DD | halves | recent (n) | flags |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
        n_all = None
        for X in X_GRID[sym]:
            s = stats(run(P, auto, X, 'touch', E_all), t_rec)
            if X is None: n_all = s['n']
            L.append('| %s | %d | %d | %.0f | %+.2f | %+.1f | %+.1f | %.2f | %.1f | %+.0f / %+.0f | %+.1f (%d) | %s |' % (
                'off' if X is None else '%g' % X, s['n'], (n_all or s['n']) - s['n'], s['win'], s['avg'], s['net'], s['net'] - s['n'] * COST[sym], s['pf'], s['dd'], s['h'][0], s['h'][1], s['rec'], s['nrec'], flags(s)))
        L.append('')
        # C: full grid touch, top 8 by avg with >= 30% of trades kept and flags
        G = []
        for S in S_GRID[sym]:
            for X in X_GRID[sym]:
                s = stats(run(P, S, X, 'touch', E_all), t_rec)
                G.append((S, X, s))
        base = [g for g in G if g[0] == auto and g[1] is None][0][2]
        cand = [g for g in G if g[2]['n'] >= max(30, 0.3 * base['n'])]
        cand.sort(key=lambda g: -g[2]['net'])
        L += ['**C. Grid S x X (touch), top 8 by net, keeping >= 30 %% of trades (current = S auto, X off: %d trades, net %+.1f, avg %+.2f)**' % (base['n'], base['net'], base['avg']), '',
              '| S | X | trades | win % | avg | net | net after costs | PF | max DD | halves | thirds | flags |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
        for S, X, s in cand[:8]:
            L.append('| %s | %s | %d | %.0f | %+.2f | %+.1f | %+.1f | %.2f | %.1f | %+.0f / %+.0f | %+.0f / %+.0f / %+.0f | %s |' % (
                'off' if S == 0 else '%g' % S, 'off' if X is None else '%g' % X, s['n'], s['win'], s['avg'], s['net'], s['net'] - s['n'] * COST[sym], s['pf'], s['dd'], s['h'][0], s['h'][1], *s['th'], flags(s)))
        L.append('')
        bt = max(best['touch'], key=lambda z: z[0])
        top = cand[0] if cand else None
        bc = max(G, key=lambda g: g[2]['net'] - g[2]['n'] * COST[sym])
        cur_txt = 'current (S auto %g, no max loss) %d trades, %+.1f pts gross (%+.2f/trade), %+.1f after costs' % (auto, base['n'], base['net'], base['avg'], base['net'] - base['n'] * COST[sym])
        bc_txt = 'best after costs S %s / X %s: %d trades, %+.1f after costs (%+.1f gross) %s' % ('off' if bc[0] == 0 else '%g' % bc[0], 'off' if bc[1] is None else '%g' % bc[1], bc[2]['n'], bc[2]['net'] - bc[2]['n'] * COST[sym], bc[2]['net'], flags(bc[2]))
        summary.append('**%s %dm** -- %s; %s.' % (sym, tf, cur_txt, bc_txt))
        summary[-1] += (' Gross: best S = %s: %+.1f %s; best grid S %s / X %s: %d trades %+.1f %s.' % (
            'off' if bt[1] == 0 else '%g' % bt[1], bt[0], flags(bt[2]),
            ('off' if top[0] == 0 else '%g' % top[0]) if top else '-', ('off' if top[1] is None else '%g' % top[1]) if top else '-', top[2]['n'] if top else 0, top[2]['net'] if top else 0, flags(top[2]) if top else ''))
        print('done', sym, tf, file=sys.stderr)
    L[6:6] = ['## Summary', ''] + ['- ' + s for s in summary] + ['']
    print('\n'.join(L))


if __name__ == '__main__':
    main()
