#!/usr/bin/env python3
"""CBC order-block setup study -- do Trade Setups that start inside an order block do better?

Per symbol AND chart timeframe ("Chart: <TICKER> <N>m"). Fetches /alerts and /bars from the Render dashboard
(same matching as cbc_daily_stats.py: every "• Trade Setup:" alert -> its "• Setup Ended:" result via direction +
Setup Entry + Started time), replays order blocks offline from the bars and buckets each setup by where its entry
candle sits.

Two OB definitions (both chart TF, length 5, mitigation Close, last 5 per side):
  A  OB v1.08 (standalone, LuxAlgo/PAC style; ob_sim.py logic): internal OBs, Leg swings, Lowest-in-leg candle,
     OB created on the break bar, mitigation on the same bar, display = 5 newest unmitigated per side, then
     "Keep newest" hides older overlapping ones (a hidden block comes back if the newer one is mitigated).
  B  CBC ⑨ Order Blocks (Lux-style) (ESLib2 f_ob2_detect / f_ob2_manage): same detection, but the block is delivered
     on the bar AFTER the break (request.security lookahead_on -> previous bar), Hide Overlap permanently hides the
     older overlapping block (it keeps its slot), max 5 slots incl. hidden, mitigated blocks are removed.
No look-ahead: the OB state used for a setup is the state after the bar BEFORE the setup candle (bars that closed
before the setup candle closed). The setup candle itself is then classified against that state.

Buckets (entry candle = the bar that closed at the alert time):
  ALIGNED   long: candle traded into an active bullish OB (low <= top) and closed at/above its bottom;
            short mirrored with a bearish OB (high >= bottom, close <= top)
  OPPOSING  long: high >= bottom of an active bearish OB and close <= its top (short mirrored with a bullish OB)
  NEAR      not the above, candle within 0.5 ATR(14) of an aligned OB's edge
  NONE      everything else
Cross-checks: (1) OB v1.08 indicator alerts in the feed ("• Bullish OB Entered" / "• Bearish OB Entered" /
"order block created", same ticker, 5 candles before the setup); (2) CBC's own "In OB+ / In OB- / OB: none" line in the
Trade Setup alert (since CBC v10.05) vs a close-inside check with each replay (state after the setup candle, as CBC
computes it).
Usage: python3 ob_setup_study.py [out.md] [prev_report.md | "since-last-run text"]
  With a previous report file, the "Since last run" line is built automatically (setups per case then -> now, verdict changes).
"""
import gzip, json, os, re, sys, time, urllib.request, datetime as D
from zoneinfo import ZoneInfo

BASE = 'https://tv-webhook-dashboard.onrender.com'
TZ = ZoneInfo('America/New_York')
SYMS = {'MES': 'MES1!', 'MGC': 'MGC1!', 'MNQ': 'MNQ1!'}
CASES = [(s, tf) for tf in (3, 2, 5) for s in ('MES', 'MGC', 'MNQ')]
LEN, LAST, NEAR_ATR = 5, 5, 0.5
BUCKETS = ('ALIGNED', 'NEAR', 'NONE', 'OPPOSING')


def get(url, tries=2):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=180) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(60)   # Render free tier wake-up


def raw(x):
    return x['raw'] if isinstance(x['raw'], str) else json.dumps(x['raw'])


def atime(x, r):
    tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
    if not tm:
        return None
    mo, dd, hh, mi = map(int, tm.groups())
    return D.datetime(int(x['receivedAt'][:4]), mo, dd, hh, mi, tzinfo=TZ)


def load_setups(alerts, sym, tf):
    S, E = {}, {}
    for x in alerts:
        r = raw(x)
        if not r.startswith(sym) or not re.search(r'Chart: \S+\s+%dm' % tf, r):
            continue
        t = atime(x, r)
        if not t:
            continue
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
            bw = re.search(r'Best: ([+-]?[\d.]+) \| Worst: ([+-]?[\d.]+)', r)
            if st and m:
                E[(d, en, int(st.group(1)), int(st.group(2)))] = (m.group(1).strip(), float(m.group(2)),
                                                                 float(bw.group(1)) if bw else None, float(bw.group(2)) if bw else None)
    return S, E


# ---------------------------------------------------------------- OB engines (state after each bar)
def swings_step(st, H, L, n):
    """LuxAlgo leg swings (OB v1.08 swings() / ESLib2 f_ob2_detect). Returns nothing, updates st['top'] / st['btm']."""
    if n < LEN:
        return
    up, lo = max(H[n - LEN + 1:n + 1]), min(L[n - LEN + 1:n + 1])
    o2 = 0 if H[n - LEN] > up else (1 if L[n - LEN] < lo else st['os'])
    if o2 == 0 and st['os'] != 0:
        st['top'] = [H[n - LEN], n - LEN, False]
    if o2 == 1 and st['os'] != 1:
        st['btm'] = [L[n - LEN], n - LEN, False]
    st['os'] = o2


def breaks(st, H, L, C, n):
    """Return list of (bull, top, btm, ob_bar) for swings broken by close[n] (lowest/highest candle in the leg)."""
    out = []
    for bull in (True, False):
        sw = st['top'] if bull else st['btm']
        if sw and not sw[2] and (C[n] > sw[0] if bull else C[n] < sw[0]):
            sw[2] = True
            span = max(1, n - sw[1] - 1)
            ext, k = None, 1
            for i in range(1, span + 1):
                if n - i < 0:
                    break
                v = L[n - i] if bull else H[n - i]
                if ext is None or (v <= ext if bull else v >= ext):
                    ext, k = v, i
            out.append((bull, H[n - k], L[n - k], n - k))
    return out


def run_v108(B):
    """OB v1.08 defaults. state[n] = (bulls, bears) shown after bar n: lists of (top, btm)."""
    H = [b['h'] for b in B]; L = [b['l'] for b in B]; C = [b['c'] for b in B]
    st = dict(os=0, top=None, btm=None)
    arr = {True: [], False: []}
    state = []
    for n in range(len(B)):
        swings_step(st, H, L, n)
        for bull, t, b, k in breaks(st, H, L, C, n):
            arr[bull].insert(0, dict(t=t, b=b, brk=False))
        for bull in (True, False):
            if len(arr[bull]) > 60:
                arr[bull].pop()
            for e in list(arr[bull]):
                if not e['brk']:
                    if (C[n] < e['b']) if bull else (C[n] > e['t']):
                        e['brk'] = True
                elif (C[n] > e['t']) if bull else (C[n] < e['b']):
                    arr[bull].remove(e)
        shown = {}
        for bull in (True, False):
            cand = [e for e in arr[bull] if not e['brk']][:LAST]
            out = []
            for e in cand:
                if not any(e['t'] > o[1] and e['b'] < o[0] for o in out):
                    out.append((e['t'], e['b']))
            shown[bull] = out
        state.append((shown[True], shown[False]))
    return state


def run_cbc(B):
    """CBC ⑨ Lux-style OBs (ESLib2). Block from the break on bar n is managed from bar n+1."""
    H = [b['h'] for b in B]; L = [b['l'] for b in B]; C = [b['c'] for b in B]
    st = dict(os=0, top=None, btm=None)
    pend = {True: None, False: None}       # detect output of the previous bar (lookahead_on [1])
    last_tl = {True: None, False: None}
    slots = {True: [], False: []}          # dicts t, b (None = hidden), oldest first
    state = []
    for n in range(len(B)):
        for bull in (True, False):
            p = pend[bull]
            if p and p[2] != last_tl[bull]:
                last_tl[bull] = p[2]
                for e in slots[bull]:
                    if e['t'] is not None and p[1] < e['t'] and p[0] > e['b']:
                        e['t'] = e['b'] = None
                slots[bull].append(dict(t=p[0], b=p[1]))
                while len(slots[bull]) > LAST:
                    slots[bull].pop(0)
            for e in list(slots[bull]):
                if e['t'] is not None and ((C[n] < e['b']) if bull else (C[n] > e['t'])):
                    slots[bull].remove(e)
        swings_step(st, H, L, n)
        for bull, t, b, k in breaks(st, H, L, C, n):
            pend[bull] = (t, b, k)
        state.append(([(e['t'], e['b']) for e in slots[True] if e['t'] is not None],
                      [(e['t'], e['b']) for e in slots[False] if e['t'] is not None]))
    return state


def classify(x, lg, st, A):
    bulls, bears = st
    al, op = (bulls, bears) if lg else (bears, bulls)
    h, l, c = x['h'], x['l'], x['c']
    if lg:
        a_in = any(l <= t and c >= b for t, b in al)
        o_in = any(h >= b and c <= t for t, b in op)
    else:
        a_in = any(h >= b and c <= t for t, b in al)
        o_in = any(l <= t and c >= b for t, b in op)
    if a_in:
        return 'ALIGNED'
    if o_in:
        return 'OPPOSING'
    dist = min((max(0.0, l - t, b - h) for t, b in al), default=None)
    if dist is not None and dist <= NEAR_ATR * A:
        return 'NEAR'
    return 'NONE'


def close_in(x, st):
    c = x['c']
    return ('+' if any(b <= c <= t for t, b in st[0]) else '') + ('-' if any(b <= c <= t for t, b in st[1]) else '')


def trig_cat(trg):
    t = trg.split(',')[0]
    if 'HTF CBC Flip' in t:
        return 'HTF CBC Flip'
    if 'LTF EMA20' in t:
        return 'LTF EMA20 Pierce/Touch'
    if re.search(r'HTF EMA\d+ Pierce', t):
        return 'HTF EMA pierce'
    if 'Momentum' in t:
        return 'Momentum'
    return 'other'


def ob_alerts(alerts, ticker):
    """OB v1.08 Alert Feed alerts for this ticker: list of (time, text)."""
    out = []
    for x in alerts:
        r = raw(x)
        if r.startswith(ticker) and re.search(r'OB Entered|order block created', r):
            t = atime(x, r)
            if t is None:
                t = D.datetime.fromisoformat(x['receivedAt'].replace('Z', '+00:00')).astimezone(TZ)
            out.append((t, r))
    return out


def analyze(sym, tf, alerts):
    tk = SYMS[sym]
    S, E = load_setups(alerts, tk, tf)
    if not S:
        return None
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    t0 = min(t for (t, d, en) in S) - D.timedelta(days=3)
    B = get('%s/bars?sym=%s&days=60&from=%s' % (BASE, key, t0.strftime('%Y-%m-%d')))['bars']
    ix = {b['t']: i for i, b in enumerate(B)}
    atr, a = [], None
    for i, b in enumerate(B):
        tr = max(b['h'], B[i - 1]['c']) - min(b['l'], B[i - 1]['c']) if i else b['h'] - b['l']
        a = tr if a is None else (a * 13 + tr) / 14
        atr.append(a)
    SA, SB = run_v108(B), run_cbc(B)
    OA = ob_alerts(alerts, tk)
    out, miss = [], 0
    for (t, d, en), r in sorted(S.items()):
        res = E.get((d, en, t.hour, t.minute))
        if not res:
            continue
        i = ix.get(int(t.timestamp() * 1000) - tf * 60000)
        if i is None or i < 60:
            miss += 1
            continue
        x, lg, A = B[i], d == 'LONG', atr[i] or 1
        trg = re.search(r'Trigger: ([^\n]*)', r)
        m = re.search(r'\n(In OB[+-]|OB: \w+)', r)
        ln = m.group(1) if m else None
        al_line = None if ln in (None, 'OB: off') else ''.join(sorted(set(re.findall(r'In OB([+-])', r)), reverse=True))
        w0 = t - D.timedelta(minutes=tf * 6)
        oba = [z for z in OA if w0 <= z[0] <= t]
        o = dict(t=t, d=d, res=res[1], why=res[0], mfe=(res[2] / A if res[2] is not None else None),
                 mae=(res[3] / A if res[3] is not None else None), trg=trig_cat(trg.group(1) if trg else ''),
                 A=classify(x, lg, SA[i - 1], A), B=classify(x, lg, SB[i - 1], A),
                 al_line=al_line, inA=close_in(x, SA[i]), inB=close_in(x, SB[i]), oba=oba)
        if oba:
            bull_e = any('Bullish OB Entered' in z[1] or 'Bullish order block created' in z[1] for z in oba)
            bear_e = any('Bearish OB Entered' in z[1] or 'Bearish order block created' in z[1] for z in oba)
            o['oba_al'] = (bull_e if lg else bear_e)
        out.append(o)
    return out, miss, len(OA)


# ---------------------------------------------------------------- stats / report
def stats(g):
    n = len(g)
    if not n:
        return None
    w = [o['res'] for o in g if o['res'] > 0]
    ls = [o['res'] for o in g if o['res'] < 0]
    net = sum(o['res'] for o in g)
    pf = (sum(w) / -sum(ls)) if ls else (float('inf') if w else 0)
    mf = [o['mfe'] for o in g if o['mfe'] is not None]
    ma = [o['mae'] for o in g if o['mae'] is not None]
    return dict(n=n, win=100 * len(w) / n, avg=net / n, net=net, pf=pf,
                mfe=sum(mf) / len(mf) if mf else None, mae=sum(ma) / len(ma) if ma else None)


def halves(out):
    s = sorted(out, key=lambda o: o['t'])
    h = len(s) // 2
    return s[:h], s[h:]


def row(label, g, h1, h2):
    s = stats(g)
    if not s:
        return '| %s | 0 | – | – | – | – | – | |' % label
    n1 = sum(o['res'] for o in g if o in h1)
    n2 = sum(o['res'] for o in g if o in h2)
    star = ' ✱' if (n1 > 0 and n2 > 0) else ''
    pf = '∞' if s['pf'] == float('inf') else '%.2f' % s['pf']
    mm = ('%.2f / %.2f' % (s['mfe'], s['mae'])) if s['mfe'] is not None else '–'
    return '| %s | %d | %.0f%% | %+.2f | %+.1f%s | %s | %s | %+.1f / %+.1f |' % (label, s['n'], s['win'], s['avg'], s['net'], star, pf, mm, n1, n2)


def avg(g):
    return sum(o['res'] for o in g) / len(g) if g else None


def compare(out, key, a, b, h1, h2):
    """Direction of (avg pts a) - (avg pts b), overall and per half. a/b are bucket sets."""
    ga = [o for o in out if o[key] in a]; gb = [o for o in out if o[key] in b]
    d = lambda X, Y: (avg(X) - avg(Y)) if X and Y else None
    return dict(na=len(ga), nb=len(gb), d=d(ga, gb),
                d1=d([o for o in ga if o in h1], [o for o in gb if o in h1]),
                d2=d([o for o in ga if o in h2], [o for o in gb if o in h2]))


def sgn(v):
    return 0 if v is None else (1 if v > 0 else -1 if v < 0 else 0)


def verdict(out, h1, h2):
    msgs = []
    for name, a, b in (('require ALIGNED (ALIGNED vs NONE)', {'ALIGNED'}, {'NONE'}),
                       ('block OPPOSING (OPPOSING vs rest)', {'OPPOSING'}, {'ALIGNED', 'NEAR', 'NONE'})):
        cA, cB = compare(out, 'A', a, b, h1, h2), compare(out, 'B', a, b, h1, h2)
        ok = all(c['na'] >= 20 and c['nb'] >= 20 and c['d'] is not None and sgn(c['d1']) == sgn(c['d2']) == sgn(c['d']) != 0 for c in (cA, cB)) \
            and sgn(cA['d']) == sgn(cB['d'])
        good = ok and ((sgn(cA['d']) > 0) if 'ALIGNED' in a else (sgn(cA['d']) < 0))
        f = lambda c: '%d vs %d, Δavg %s' % (c['na'], c['nb'], ('%+.2f' % c['d']) if c['d'] is not None else '–')
        msgs.append('%s: **%s** (v1.08 %s · CBC %s)' % (name, 'OB filter worth testing' if good else
                                                     ('consistent but points the other way' if ok else 'not enough evidence yet'), f(cA), f(cB)))
    return msgs


def report(alerts, prev=None):
    now = D.datetime.now(TZ)
    first = min(x['receivedAt'] for x in alerts)[:10]
    L = ['# CBC order-block setup study -- %s' % now.strftime('%Y-%m-%d %H:%M ET'), '',
         'Question: do CBC Trade Setups whose entry candle sits inside an order block do better? Alerts stored: %d (since %s).' % (len(alerts), first),
         'OB definitions: **A** = OB v1.08 defaults (internal, length 5, Leg swings, Lowest in leg, mitigation Close, Keep newest, last 5/5); '
         '**B** = CBC ⑨ Lux-style (ESLib2: length 5, Close, chart TF, last 5, block appears the bar after the break, Hide Overlap removes the older block). '
         'OB state = after the bar before the setup candle (no look-ahead). Buckets: ALIGNED (long traded into an active OB+ and closed at/above its bottom; short mirrored), '
         'OPPOSING (long into an OB- and closed at/below its top), NEAR (within 0.5 ATR of an aligned OB), NONE. '
         '✱ = net positive in both chronological halves (half nets shown last). MFE/MAE = Best / Worst from the Setup Ended alert in ATR(14).', '']
    if prev:
        L += ['**Since last run:** %s' % prev, '']
    summary, allout, oba_total = [], [], 0
    for sym, tf in CASES:
        try:
            r = analyze(sym, tf, alerts)
        except Exception as e:
            L += ['## %s %dm' % (sym, tf), '', 'error: %s' % e, '']
            continue
        if not r:
            continue
        out, miss, noa = r
        oba_total += noa
        if not out:
            continue
        allout += [dict(o, case='%s %dm' % (sym, tf)) for o in out]
        h1, h2 = halves(out)
        agree = sum(o['A'] == o['B'] for o in out)
        L += ['## %s %dm' % (sym, tf), '',
              'Setups with results: %d (skipped %d without bars) · net %+.1f pts · halves split at %s · A/B bucket agreement %d/%d (%.0f%%)' % (
                  len(out), miss, sum(o['res'] for o in out), h2[0]['t'].strftime('%m/%d %H:%M') if h2 else '–', agree, len(out), 100 * agree / len(out)), '']
        for key, nm in (('A', 'A · OB v1.08'), ('B', 'B · CBC Lux-style')):
            L += ['**%s**' % nm, '', '| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |', '|---|---|---|---|---|---|---|---|']
            for bk in BUCKETS:
                L.append(row(bk, [o for o in out if o[key] == bk], h1, h2))
            L.append('')
        # trigger split (A and B), ALIGNED vs NONE, triggers with 5+ setups
        tl = []
        for tg in ('HTF CBC Flip', 'LTF EMA20 Pierce/Touch', 'HTF EMA pierce', 'Momentum', 'other'):
            g = [o for o in out if o['trg'] == tg]
            if len(g) < 5:
                continue
            cell = []
            for key in ('A', 'B'):
                for bk in ('ALIGNED', 'NONE'):
                    s = stats([o for o in g if o[key] == bk])
                    cell.append('%d · %.0f%% · %+.2f' % (s['n'], s['win'], s['avg']) if s else '0')
            tl.append('| %s (%d) | %s |' % (tg, len(g), ' | '.join(cell)))
        if tl:
            L += ['By trigger (n · win % · avg pts):', '', '| Trigger | A ALIGNED | A NONE | B ALIGNED | B NONE |', '|---|---|---|---|---|'] + tl + ['']
        # cross-checks
        wl = [o for o in out if o['al_line'] is not None]
        if wl:
            ag_a = sum(o['al_line'] == o['inA'] for o in wl); ag_b = sum(o['al_line'] == o['inB'] for o in wl)
            nin = sum(o['al_line'] != '' for o in wl)
            L.append('Cross-check vs CBC alert "In OB±/OB: none" line (close inside, %d setups, %d say In OB): replay A agrees %d (%.0f%%), replay B %d (%.0f%%).' % (
                len(wl), nin, ag_a, 100 * ag_a / len(wl), ag_b, 100 * ag_b / len(wl)))
        wo = [o for o in out if o['oba']]
        if wo:
            ag = sum(o['oba_al'] == (o['A'] == 'ALIGNED') for o in wo)
            L.append('OB v1.08 indicator alerts within 5 candles before the setup: %d setups; replay A ALIGNED agrees %d (%.0f%%).' % (len(wo), ag, 100 * ag / len(wo)))
        else:
            L.append('OB v1.08 indicator alerts for %s in the feed: %d (none within 5 candles of a setup) -- cross-check not possible.' % (SYMS[sym], noa))
        L.append('')
        v = verdict(out, h1, h2)
        L += ['Verdict: ' + v[0], '', 'Verdict: ' + v[1], '']
        sa = {bk: stats([o for o in out if o['A'] == bk]) for bk in BUCKETS}
        sb = {bk: stats([o for o in out if o['B'] == bk]) for bk in BUCKETS}
        f = lambda s: ('%d · %.0f%% · %+.2f' % (s['n'], s['win'], s['avg'])) if s else '0'
        summary.append('%s %dm: ALIGNED %s / NONE %s / OPPOSING %s (A; B ALIGNED %s, NONE %s) -> %s' % (
            sym, tf, f(sa['ALIGNED']), f(sa['NONE']), f(sa['OPPOSING']), f(sb['ALIGNED']), f(sb['NONE']),
            'worth testing' if any('worth testing' in m for m in v) else 'not enough evidence yet'))
    # pooled (info only -- decisions stay per case)
    if allout:
        h1, h2 = halves(allout)
        L += ['## All cases pooled (info only -- decide per symbol + timeframe)', '']
        for key, nm in (('A', 'A · OB v1.08'), ('B', 'B · CBC Lux-style')):
            L += ['**%s**' % nm, '', '| Bucket | Setups | Win % | Avg pts | Net pts | PF | MFE / MAE (ATR) | Half 1 / Half 2 net |', '|---|---|---|---|---|---|---|---|']
            for bk in BUCKETS:
                L.append(row(bk, [o for o in allout if o[key] == bk], h1, h2))
            L.append('')
        agree = sum(o['A'] == o['B'] for o in allout)
        L += ['A/B bucket agreement: %d/%d (%.0f%%). Points differ in size between symbols (MNQ >> MES > MGC), so pooled pts are dominated by MNQ.' % (
            agree, len(allout), 100 * agree / len(allout)), '']
    L += ['## Summary (A buckets: n · win % · avg pts)', ''] + ['- ' + s for s in summary] + ['']
    return '\n'.join(L), summary


if __name__ == '__main__':
    alerts = get(BASE + '/alerts?from=2000-01-01')
    prev = sys.argv[2] if len(sys.argv) > 2 else None
    if prev and os.path.isfile(prev):
        old = open(prev).read()
        ts = re.search(r'study -- ([\d-]+ [\d:]+ ET)', old)
        pv = {m.group(1): (int(m.group(2)) + int(m.group(3)) + int(m.group(4)), m.group(5)) for m in
              re.finditer(r'- (\w+ \dm): ALIGNED (\d+)[^/]*/ NONE (\d+)[^/]*/ OPPOSING (\d+).*-> (.*)', old)}
        _, summ0 = report(alerts, None)
        ch = []
        for line in summ0:
            m = re.match(r'(\w+ \dm): ALIGNED (\d+)[^/]*/ NONE (\d+)[^/]*/ OPPOSING (\d+).*-> (.*)', line)
            if m and m.group(1) in pv:
                n = int(m.group(2)) + int(m.group(3)) + int(m.group(4))
                o = pv[m.group(1)]
                ch.append('%s %d->%d%s' % (m.group(1), o[0], n, '' if o[1] == m.group(5) else ' (verdict now: %s)' % m.group(5)))
        prev = 'vs %s: setups (ALIGNED+NONE+OPPOSING, OB v1.08) %s.' % (ts.group(1) if ts else 'previous run', ', '.join(ch) or 'no comparable cases')
    md, summ = report(alerts, prev)
    if len(sys.argv) > 1:
        open(sys.argv[1], 'w').write(md)
    print(md)
