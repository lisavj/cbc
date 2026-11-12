#!/usr/bin/env python3
"""CBC daily stats -- per symbol AND chart timeframe (MGC 3m, MGC 2m, MES 3m, MES 2m).

Fetches the Alert Feed (/alerts) and BarFeed bars (/bars) from the Render dashboard, matches every
"Trade Setup" alert with its "Setup Ended" result, rebuilds the setup context from the bars and prints a
markdown report: totals, losers table, and what each candidate gate would have blocked.

Gates (same definitions as the 10/19 analyses):
  R  range gate      close in the top 20 % (long) / bottom 20 % (short) of the last 24 bars, range < 5 ATR(14)
                     (also 6 ATR shown); Momentum break setups exempt (CBC v10.21)
  X  VWAP stretch    (close - VWAP) / ATR in the trade direction > 4 (6 shown); Momentum exempt
  F  flip counter    "HTF flips n/8" in the alert >= 4
  V  side gate       HTF CBC Flip setup whose close is NOT beyond VWAP and EMA200 by 1 pt
  M  MTF             1H CBC against the trade direction
  P  pattern         engulfing / tweezer in the trade direction on the setup candle or the 2 before
Extra fields (10/27 watch items): pb = pullback since the HTF CBC (hc) turned in the trade direction, in ATR;
s9 / s20 = HTF EMA9 / EMA20 slope over the last 5 chart candles, in the trade direction (pts).
11/06: bars with null indicator fields (BarFeed gap, e.g. MES 3m 11/02 00:12-18:09) no longer crash the case:
VWAP-based gates (X, V) are treated as unknown there; other TypeErrors skip the setup (listed in SKIP).
11/12: duplicate alerts (claude/DATA_NOTES.md): alerts with the same Chart / Time / bullet names within 60 s count once
(longest text kept); when one setup has two "Setup Ended" results, the one with "0.5x...(TP1)" wins (MGC 3m v10.84 exits).
Env CBC_ALERTS_FILE=path reuses a saved /alerts?from=2000-01-01 download instead of fetching again.
Usage: python3 cbc_daily_stats.py [days]   (default: all stored alerts, incl. the server v9 archive)
"""
import gzip, json, os, re, sys, urllib.request, datetime as D
from zoneinfo import ZoneInfo

BASE = 'https://tv-webhook-dashboard.onrender.com'
TZ = ZoneInfo('America/New_York')
TOL = {'MGC': 0.2, 'MES': 0.5}
CASES = [('MGC', 3), ('MGC', 2), ('MES', 3), ('MES', 2)]
DEFAULTS = {('MGC', 3): 'R5 + X4 ON; exits SL1 1.7 ATR + min 5 cap 7, TP1 1.7 cap 6, 50 % at TP1, BE, trail 3.5 (v10.84)',
            ('MES', 3): 'R5 ON, flip-timing gate; exits SL1 3 ATR min 5, TP1 1.75 ATR, 80 %/100 % by time, BE, trail 1.7',
            ('MGC', 2): 'R5 ON + non-flip flop gate (v10.77); base exits',
            ('MES', 2): 'MTF gate ON, flip counter 4; base exits'}


def get(url):
    if '/alerts' in url and os.environ.get('CBC_ALERTS_FILE'):
        return json.load(open(os.environ['CBC_ALERTS_FILE']))
    req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
    with urllib.request.urlopen(req, timeout=180) as r:
        b = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            b = gzip.decompress(b)
        return json.loads(b.decode())


def raw(x):
    return x['raw'] if isinstance(x['raw'], str) else json.dumps(x['raw'])


def dedupe(alerts):
    """DATA_NOTES 11/12: same chart + Time line + bullet names within 60 s = one alert (keep longest)."""
    keep = {}
    out = []
    for x in sorted(alerts, key=lambda x: x['receivedAt']):
        r = raw(x)
        ch = re.search(r'Chart: ([^\n]+)', r)
        tm = re.search(r'Time: ([^\n]+)', r)
        if not ch or not tm:
            out.append(x); continue
        k = (ch.group(1).strip(), tm.group(1).strip(), tuple(sorted(re.findall(r'• ([^:\n]+)', r))))
        ts = D.datetime.fromisoformat(x['receivedAt'].replace('Z', '+00:00')).timestamp()
        if k in keep and ts - keep[k][0] <= 60:
            j = keep[k][1]
            o = raw(out[j])
            # prefer the v10.84 "0.5x(TP1)" breakdown, else the longer text
            new05, old05 = bool(re.search(r'0\.5×[\d.]+\(TP1\)', r)), bool(re.search(r'0\.5×[\d.]+\(TP1\)', o))
            if (new05 and not old05) or (new05 == old05 and len(r) > len(o)):
                out[j] = x
            continue
        keep[k] = (ts, len(out))
        out.append(x)
    return out


def load_setups(alerts, sym, tf):
    S, E = {}, {}
    for x in alerts:
        r = raw(x)
        if not r.startswith(sym) or not re.search(r'Chart: \S+\s+%dm' % tf, r):
            continue
        tm = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r)
        if not tm:
            continue
        mo, dd, hh, mi = map(int, tm.groups())
        yr = int(x['receivedAt'][:4])
        t = D.datetime(yr, mo, dd, hh, mi, tzinfo=TZ)
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
            m = re.search(r'Ended: ([^|\n]*?) \| Result: ([+-]?[\d.]+)([^|\n]*)', r)
            if st and m:
                k = (d, en, int(st.group(1)), int(st.group(2)))
                is05 = bool(re.search(r'0\.5×[\d.]+\(TP1\)', m.group(3)))
                if k in E and E[k][3] and not is05:
                    continue
                E[k] = (m.group(1).strip(), float(m.group(2)), m.group(3).strip(), is05, t)
    return S, E


def ctx_flags(r, lg, en):
    F = set()
    s = 1 if lg else -1
    m = re.search(r'\nTP1: ([\d.]+)', r)
    if not m:
        return F
    dtp = abs(float(m.group(1)) - en)
    obd = None
    ob = re.search(r'nearest OB([+-]) ([\d.]+)-([\d.]+), ([\d.]+) pts away', r)
    if ob and ((lg and ob.group(1) == '-' and float(ob.group(3)) > en) or (not lg and ob.group(1) == '+' and float(ob.group(2)) < en)):
        obd = float(ob.group(4))
    if re.search(r'In OB' + ('-' if lg else r'\+'), r):
        obd = 0.0
    if obd is not None and obd < dtp:
        F.add('OB')
    rm = re.search(r'\nRoom: .*? = ([\d.]+) x TP1', r)
    if rm:
        ratio = float(rm.group(1))
    else:
        lv = [(float(x.group(1)) - en) * s for x in re.finditer(r'\nTP\d(?: Piv)?: ([\d.]+) \| ([^|\n]+) \|', r) if 'ATR' not in x.group(2) and x.group(2).strip() not in ('—', '-')]
        lv = [d for d in lv if d > 0] + ([obd] if obd is not None else [])
        ratio = min(lv) / dtp if lv and dtp > 0 else None
    if ratio is not None and ratio < 0.5:
        F.add('L5')
    if 'Flip flop' in r:
        F.add('FL')
    cl = re.search(r'EMA cloud \(1[05]m\): (\w+)', r)
    if cl and cl.group(1) != ('Bullish' if lg else 'Bearish'):
        F.add('CL')
    return F


BARS = {}


def analyze(sym, tf, alerts, since):
    S, E = load_setups(alerts, sym, tf)
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    t0 = min((t for (t, d, en) in S if not since or t >= since), default=D.datetime.now(TZ)) - D.timedelta(days=3)
    B = get('%s/bars?sym=%s&days=60&from=%s' % (BASE, key, t0.strftime('%Y-%m-%d')))['bars']
    BARS[(sym, tf)] = B
    ix = {b['t']: i for i, b in enumerate(B)}
    atr, a = [], None
    for i, b in enumerate(B):
        tr = max(b['h'], B[i - 1]['c']) - min(b['l'], B[i - 1]['c']) if i else b['h'] - b['l']
        a = tr if a is None else (a * 13 + tr) / 14
        atr.append(a)
    c = [b['c'] for b in B]
    st_hc = [0] * len(B)
    for i in range(len(B)):
        st_hc[i] = i if i == 0 or B[i].get('hc') != B[i - 1].get('hc') else st_hc[i - 1]

    def pat(i, lg):
        tol = TOL.get(sym, 0.5)
        for j in (i, i - 1, i - 2):
            x, p = B[j], B[j - 1]
            if lg and ((p['c'] < p['o'] and x['c'] > x['o'] and x['o'] <= p['c'] and x['c'] >= p['o']) or (abs(x['l'] - p['l']) <= tol and p['c'] < p['o'] and x['c'] > x['o'])):
                return True
            if not lg and ((p['c'] > p['o'] and x['c'] < x['o'] and x['o'] >= p['c'] and x['c'] <= p['o']) or (abs(x['h'] - p['h']) <= tol and p['c'] > p['o'] and x['c'] < x['o'])):
                return True
        return False

    out = []
    for (t, d, en), r in sorted(S.items()):
        if since and t < since:
            continue
        res = E.get((d, en, t.hour, t.minute))
        if not res:
            continue
        i = ix.get(int(t.timestamp() * 1000) - tf * 60000)
        if i is None or i < 40:
            NOBAR.append((sym, tf, t, d, en, r, res))
            continue
        try:
            o = _one(B, i, t, d, en, r, res, atr, c, st_hc, pat)
        except TypeError:
            SKIP.append((sym, tf, t)); continue
        out.append(o)
    return out


SKIP = []
NOBAR = []


def _one(B, i, t, d, en, r, res, atr, c, st_hc, pat):
    if True:
        x = B[i]
        lg = d == 'LONG'
        g = lambda p: (re.search(p, r).group(1) if re.search(p, r) else '')
        trg = g(r'Trigger: ([^\n]*)')
        flip, mom = 'HTF CBC Flip' in trg, 'Momentum' in trg
        A = atr[i] or 1
        nov = x.get('vw') is None or x.get('e200') is None
        ex = 0.0 if nov else ((x['c'] - x['vw']) if lg else (x['vw'] - x['c'])) / A
        w = B[i - 23:i + 1]
        hi, lo = max(y['h'] for y in w), min(y['l'] for y in w)
        p = (x['c'] - lo) / (hi - lo) if hi > lo else .5
        pd, rw = (p if lg else 1 - p), (hi - lo) / A
        n = sum(abs(c[j] - c[j - 1]) for j in range(i - 11, i + 1))
        er = abs(c[i] - c[i - 12]) / n if n else 0
        fl = int(g(r'HTF flips (\d+)/8') or 0)
        side = True if nov else ((x['c'] > max(x['vw'], x['e200']) + 1) if lg else (x['c'] < min(x['vw'], x['e200']) - 1))
        mtf = g(r'MTF CBC \(1H\): (\w+)')
        s0 = max(st_hc[i], i - 200)
        pb = ((max(y['h'] for y in B[s0:i + 1]) - x['c']) if lg else (x['c'] - min(y['l'] for y in B[s0:i + 1]))) / A
        sg = 1 if lg else -1
        try:
            s9 = sg * (x['h9'] - B[i - 5]['h9']); s20 = sg * (x['h20'] - B[i - 5]['h20'])
        except (TypeError, KeyError):
            s9 = s20 = None
        G = set()
        if flip and not side: G.add('V')
        if not mom and pd >= .8 and rw < 5: G.add('R5')
        if not mom and pd >= .8 and rw < 6: G.add('R6')
        if not mom and ex > 4: G.add('X4')
        if not mom and ex > 6: G.add('X6')
        if fl >= 4: G.add('F')
        if (mtf == 'Bearish' and lg) or (mtf == 'Bullish' and not lg): G.add('M')
        if pat(i, lg): G.add('P')
        G |= ctx_flags(r, lg, en)
        trg2 = re.sub(r' \(closed beyond EMA9: \w+\)', '', trg).replace('HTF CBC Flip', 'Flip').replace('(late, 1 bars after)', '(late)')
        return (dict(t=t, d=d, en=en, trg=trg2[:28], trgfull=trg, why=res[0], res=res[1], brk=res[2], is05=res[3], tend=res[4],
                     ex=ex, pd=pd, rw=rw, er=er, fl=fl, mtf=mtf, G=G, pb=pb, s9=s9, s20=s20, A=A, raw=r, i=i))


def summ(g):
    if not g:
        return '0 | – | –'
    return '%d | %d%% | %+.1f' % (len(g), round(sum(o['res'] > 0 for o in g) / len(g) * 100), sum(o['res'] for o in g))


def load_alerts(days=None):
    frm = (D.datetime.now(TZ) - D.timedelta(days=days + 1)).strftime('%Y-%m-%d') if days else '2000-01-01'
    alerts = get(BASE + '/alerts?from=' + frm)
    return dedupe(alerts)


def report(days=None):
    alerts = load_alerts(days)
    since = D.datetime.now(TZ) - D.timedelta(days=days) if days else None
    first = min(x['receivedAt'] for x in alerts)[:10]
    lines = ['# CBC daily stats -- %s' % D.datetime.now(TZ).strftime('%Y-%m-%d %H:%M ET'), '',
             'Alerts stored: %d after dedupe (since %s). Window: %s. Rule: decide per symbol + timeframe; >= 20 setups before changing a default.' % (len(alerts), first, ('last %d days' % days) if days else 'all stored'), '']
    for sym, tf in CASES:
        try:
            out = analyze(sym, tf, alerts, since)
        except Exception as e:
            lines += ['## %s %dm' % (sym, tf), '', 'error: %s' % e, '']
            continue
        L = [o for o in out if o['res'] < 0]
        lines += ['## %s %dm -- defaults: %s' % (sym, tf, DEFAULTS[(sym, tf)]), '',
                  'Setups with results: %d · losers %d · net %+.1f pts' % (len(out), len(L), sum(o['res'] for o in out)), '',
                  '| Gate | Blocked | Win % | Net of blocked | Halves h1 / h2 (net of blocked) | Verdict |', '|---|---|---|---|---|---|']
        for gname, label in (('R5', 'Range 24/20%/<5 ATR'), ('R6', 'Range 24/20%/<6 ATR'), ('X4', 'VWAP stretch >4 ATR'), ('X6', 'VWAP stretch >6 ATR'), ('F', 'Flips >= 4/8'), ('M', '1H MTF against'), ('V', 'Side gate (would not draw now)'),
                             ('OB', 'Opposing OB before TP1 (watch MGC 3m)'), ('L5', 'Level/OB < 0.5x TP1 (watch MES 3m, MGC 2m)'),
                             ('FL', 'Flip flop warning (watch MGC 2m)'), ('CL', '15m EMA cloud against (watch MGC 3m)')):
            bl = [o for o in out if gname in o['G']]
            net = sum(o['res'] for o in bl)
            verdict = '–' if not bl else ('helps' if net < -3 else 'hurts' if net > 3 else 'neutral')
            h = len(out) // 2
            h1 = sum(o['res'] for o in out[:h] if gname in o['G'])
            h2 = sum(o['res'] for o in out[h:] if gname in o['G'])
            lines.append('| %s | %s | %+.1f / %+.1f | %s |' % (label, summ(bl), h1, h2, verdict))
        pw = [o for o in out if 'P' in o['G']]
        pn = [o for o in out if 'P' not in o['G']]
        lines += ['', 'Pattern WITH: %s · none: %s (N | win %% | net)' % (summ(pw), summ(pn)), '']
        if L:
            lines += ['| Time | Dir | Entry | Trigger | Result | Ended | Ext ATR | Range pos/width | ER | Flips | 1H | Gates |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
            for o in L[-15:]:
                lines.append('| %s | %s | %s | %s | %+.2f | %s | %+.1f | %d%% / %.1f | %.2f | %d | %s | %s |' % (
                    o['t'].strftime('%m/%d %H:%M'), o['d'][0], o['en'], o['trg'], o['res'], o['why'], o['ex'], o['pd'] * 100, o['rw'], o['er'], o['fl'], o['mtf'][:4] or '–',
                    ','.join(sorted(o['G'] - {'P'})) or '–'))
            lines.append('')
    return '\n'.join(lines)


if __name__ == '__main__':
    print(report(int(sys.argv[1]) if len(sys.argv) > 1 else None))
