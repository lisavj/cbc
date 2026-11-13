"""Setup order since the HTF CBC flip -- 1st / 2nd / 3rd / 4th / 5th signal after the flip, every setup type -- 11/12/2026.
Charts: MES + MGC 2m / 3m / 5m (HTF = 5 x chart TF: 10m / 15m / 25m).
Question: are setups taken soon after the HTF flip better than later ones -- should CBC / the bot skip setups past the Nth?

Signals counted only in the HTF CBC direction, numbered from the flip candle (a setup on the flip candle itself = #1);
the count restarts at every HTF flip.
7-candle rule: a repeat of the SAME setup type within 7 candles of the last counted one is the same signal (ignored) --
unless that counted signal's trade already closed before the repeat (then the repeat counts as a new signal).
Two counts: SHARED (all setup types share one number; several types on one candle = one number) and PER-TYPE.
Exits: BOT = SL 3 ATR / TP 1.75 ATR (100 % at TP1), else close on the HTF CBC flip against or at the 15:57 ET flatten.
       CHART = that chart's CBC exits (live MES 3m / MGC 3m exits; 2m / 5m base exits 1.7 / 1.7 / 80 % / BE / trail 1.7).
Every trade scored on its own (no one-trade-at-a-time). Net after costs: MES 0.50, MGC 0.32 pt per trade.
A. REPLAY (chop_sim engine, Jan 5 -> now; 2m Jun 1 -> now): every setup trigger the engine models -- HTF CBC Flip,
   LTF EMA20 Pierce (closed beyond EMA9 / not beyond / late), HTF EMA9 Pierce (incl. late), HTF EMA20 Pierce (incl. late)
   -- all ticked, with each chart's live gates + ER / breakout rule, NO 10-candle cooldown (the 7-candle rule instead).
B. LIVE alerts since 10/19 (duplicates count once): EVERY directional alert type on that chart (Trade Setups by first
   trigger + all other alerts), scored with the same exits on the BarFeed candles.
"""
import re, sys, json, collections, datetime as D
import numpy as np, pandas as pd
from zoneinfo import ZoneInfo
import chop_sim as cs, stretch_study as ss, all_alerts_study as aas

TZ = ZoneInfo('America/New_York')
ss.FROM[5] = '2026-01-05'
COST = {'MES': .5, 'MGC': .32}
GATE = {('MES', 5): dict(R5=0, X4=0, MTF=0), ('MGC', 5): dict(R5=0, X4=0, MTF=0)}
SEP = 7
CHARTS = [('MES', 3), ('MGC', 3), ('MES', 2), ('MGC', 2), ('MES', 5), ('MGC', 5)]
if len(sys.argv) > 1:
    CHARTS = [(a.split(':')[0], int(a.split(':')[1])) for a in sys.argv[1:]]


def bot_exit(s, i, lg):
    C, H, L = s.C, s.H, s.L; en, A = C[i], s.atr[i]; g = 1 if lg else -1
    sl, tp = en - g * 3 * A, en + g * 1.75 * A
    for j in range(i + 1, s.n):
        if (L[j] <= sl) if lg else (H[j] >= sl): return -3 * A, j
        if (H[j] >= tp) if lg else (L[j] <= tp): return 1.75 * A, j
        if s.hdir[j] == (0 if lg else 1) or 957 <= s.hm[j] < 1080: return g * (C[j] - en), j
    return None, None


def chart_exit(s, i, lg, q):
    r, j, why = s.sim1(i, lg, q, -1)
    return (None, None) if why == 'end' else (r, j)


def number(s, sig, exits):
    """sig: list of (i, lg, typ, extra). Returns rows dict(i, lg, typ, sh, pt, ago, res) for signals in the HTF direction."""
    flip_at = -1; seg = None; out = []
    lastc = {}; shared = 0; lastshared_i = -1; ptc = collections.Counter()
    fi = np.where(s.hf != 0)[0]
    sig = sorted(sig, key=lambda z: z[0])
    k = 0
    for (i, lg, typ, ex) in sig:
        f = fi[np.searchsorted(fi, i, side='right') - 1] if np.searchsorted(fi, i, side='right') else -1
        if f < 0: continue
        if lg != (s.hdir[i] == 1):
            out.append(dict(i=i, lg=lg, typ=typ, sh=-1, pt=-1, ago=i - f, res=exits(i, lg)[0], ex=ex)); continue
        if f != seg:
            seg = f; lastc = {}; shared = 0; lastshared_i = -1; ptc = collections.Counter()
        r, j = exits(i, lg)
        if typ in lastc:
            p, pj = lastc[typ]
            if i - p < SEP and (pj is None or pj >= i): continue
        lastc[typ] = (i, j)
        if i != lastshared_i: shared += 1; lastshared_i = i
        ptc[typ] += 1
        out.append(dict(i=i, lg=lg, typ=typ, sh=shared, pt=ptc[typ], ago=i - f, res=r, ex=ex))
    return out


def stat(v, cost, s, cuts, t4):
    v = [z for z in v if z['res'] is not None]
    if not v: return None
    x = np.array([z['res'] - cost for z in v]); T = s.T
    th = [sum(z['res'] - cost for z in v if (0 if T[z['i']] < cuts[0] else 1 if T[z['i']] < cuts[1] else 2) == k) for k in range(3)]
    l4 = sum(z['res'] - cost for z in v if T[z['i']] >= t4)
    return dict(n=len(x), w=100 * (x > 0).mean(), net=x.sum(), avg=x.mean(), th=th, l4=l4, ago=np.median([z['ago'] for z in v]))


def fmt(lb, st, tf):
    if not st: return '| %s | 0 | | | | | | |' % lb
    return '| %s | %d | %.0f %% | %+.1f | %+.2f | %+.0f / %+.0f / %+.0f | %+.1f | %.0f min |' % (lb, st['n'], st['w'], st['net'], st['avg'], *st['th'], st['l4'], st['ago'] * tf)


HDR = ['| Signal # since flip | Trades | Win % | Net | Avg / trade | Thirds (by date) | Last 4 wk (live: last 7 days) | Median time after flip |', '|---|---|---|---|---|---|---|---|']


def order_tables(rows, key, cost, s, cuts, t4, tf, half_cut=None):
    L = []
    al = [z for z in rows if z[key] > 0]
    L += HDR
    for k in range(1, 6): L.append(fmt('#%d only' % k, stat([z for z in al if z[key] == k], cost, s, cuts, t4), tf))
    L.append(fmt('#6 and later', stat([z for z in al if z[key] >= 6], cost, s, cuts, t4), tf))
    L.append('| **cumulative** | | | | | | | |')
    for k in range(1, 6): L.append(fmt('**1 to %d**' % k if k > 1 else '**1 only**', stat([z for z in al if z[key] <= k], cost, s, cuts, t4), tf))
    L.append(fmt('All (no cut-off)', stat(al, cost, s, cuts, t4), tf))
    L.append(fmt('Against the HTF direction (not counted)', stat([z for z in rows if z[key] < 0], cost, s, cuts, t4), tf))
    return L


def type_table(rows, key, cost, types):
    L = ['| Setup type | #1 | 1 to 2 | 1 to 3 | 1 to 4 | 1 to 5 | #6+ | All |', '|---|---|---|---|---|---|---|---|']
    for ty in types:
        v = [z for z in rows if z['typ'] == ty and z[key] > 0 and z['res'] is not None]
        if len(v) < 5: continue
        cell = lambda w: '%d / %+.0f (%+.2f)' % (len(w), sum(z['res'] - cost for z in w), np.mean([z['res'] - cost for z in w])) if w else '-'
        L.append('| %s | %s |' % (ty, ' | '.join([cell([z for z in v if z[key] <= k]) for k in range(1, 6)] + [cell([z for z in v if z[key] >= 6]), cell(v)])))
    return L


def verdict(rows, key, cost, s, cuts):
    """Smallest N where every later signal (#N+1..) is net negative in all three thirds and the kept 1..N avg beats all."""
    al = [z for z in rows if z[key] > 0 and z['res'] is not None]
    if not al: return 'no data'
    av = np.mean([z['res'] - cost for z in al])
    for N in range(1, 6):
        late = [z for z in al if z[key] > N]; keep = [z for z in al if z[key] <= N]
        if len(late) < 30: continue
        th = [sum(z['res'] - cost for z in late if (0 if s.T[z['i']] < cuts[0] else 1 if s.T[z['i']] < cuts[1] else 2) == k) for k in range(3)]
        if all(t < 0 for t in th) and np.mean([z['res'] - cost for z in keep]) > av:
            return 'cut after #%d: signals #%d+ = %d trades %+.0f (thirds %+.0f / %+.0f / %+.0f), kept avg %+.2f vs all %+.2f' % (
                N, N + 1, len(late), sum(z['res'] - cost for z in late), *th, np.mean([z['res'] - cost for z in keep]), av)
    return 'no cut-off where every later signal loses in all three thirds'


# ---------------- live alerts ----------------
ALERTS = None


def live_signals(s, sym, tf):
    global ALERTS
    if ALERTS is None:
        A = aas.get(ss.BASE + '/alerts?from=2026-10-19'); A = A if isinstance(A, list) else A.get('alerts', [])
        ALERTS = sorted(A, key=lambda a: a['receivedAt'])
    tix = {int(t): k for k, t in enumerate(s.T)}; ev = {}
    for a in ALERTS:
        r = a['raw'] if isinstance(a['raw'], str) else json.dumps(a['raw'])
        if not r.startswith(sym): continue
        m = re.search(r'Chart: \S+\s+(\d+)m', r)
        if not m or int(m[1]) != tf: continue
        mt = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)(?::\d+)?(?:-(\d+):(\d+))?', r)
        if not mt: continue
        ct = D.datetime(int(a['receivedAt'][:4]), int(mt[1]), int(mt[2]), int(mt[3]), int(mt[4]), tzinfo=TZ)
        if mt[5]:   # 'HH:MM-HH:MM' = candle open-close -> use the close
            c2 = ct.replace(hour=int(mt[5]), minute=int(mt[6]))
            ct = c2 if c2 > ct else c2 + D.timedelta(days=1)
        i = tix.get(int(ct.timestamp() * 1000) - tf * 60000)
        if i is None: continue
        for sec in ('\n' + r).split('\n• ')[1:]:
            head = sec.split('\n')[0]
            if head.startswith('Trade Setup:'):
                tg = re.search(r'Trigger: ([^\n]*)', sec); f = tg[1] if tg else ''; f0 = f.split(',')[0].strip()
                nm = 'SETUP: ' + ('HTF CBC Flip' if f0.startswith('HTF CBC Flip') or f0.startswith('HTF(') else
                                  'LTF Pierce late' if ('LTF EMA20 Pierce' in f0 and 'late' in f0) else
                                  'LTF Pierce beyond EMA9' if (f0.startswith('LTF EMA20 Pierce') and 'closed beyond EMA9: yes' in f) else
                                  'LTF Pierce not beyond EMA9' if f0.startswith('LTF EMA20 Pierce') else re.sub(r'\s*\(.*', '', f0))
                d = 1 if 'LONG' in head else -1
            else:
                if aas.SKIP.search('• ' + head) or 'Bot Order' in head or 'Setup Blocked' in head or 'Exit Rule' in head: continue
                d = aas.direction('• ' + head)
                if not d: continue
                nm = aas.norm_type('• ' + head); nm = {'HTF': 'HTF CBC Flip + LTF Agreement'}.get(nm, nm)
            ev[(i, d == 1, nm)] = 1
    return [(i, lg, nm, None) for (i, lg, nm) in ev]


def run_chart(sym, tf, out):
    B = ss.load(sym, tf); s = cs.Case(sym, tf, B); cost = COST[sym]
    G = GATE.get((sym, tf), cs.GATE.get((sym, tf)))
    q = cs.EXIT.get((sym, tf), ss.QB[sym])
    e9 = B.e9.values.astype(float)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    sig = []
    for d in s.cands:
        if G['R5'] and d['R5']: continue
        if G['X4'] and d['X4']: continue
        if G['MTF'] and d['M']: continue
        if d['VB']: continue
        if d['trig'] != 'flip' and d['er'][12] < d['erm']: continue
        if not cs.cur_rule(d): continue
        i = d['i']
        if d['trig'] == 'flip': ty = 'HTF CBC Flip'
        elif d['trig'] == 'ltf20':
            ty = 'LTF Pierce late' if d.get('late') else ('LTF Pierce beyond EMA9' if ((s.C[i] > e9[i]) if d['lg'] else (s.C[i] < e9[i])) else 'LTF Pierce not beyond EMA9')
        else: ty = {'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}[d['trig']]
        sig.append((i, d['lg'], ty, None))
    RT = ['HTF CBC Flip', 'LTF Pierce beyond EMA9', 'LTF Pierce not beyond EMA9', 'LTF Pierce late', 'HTF EMA9 Pierce', 'HTF EMA20 Pierce']
    lv = live_signals(s, sym, tf)
    li = [z[0] for z in lv]
    LT = [k for k, _ in collections.Counter(z[2] for z in lv).most_common()]
    out += ['', '# %s %dm (HTF %dm)' % (sym, tf, 5 * tf), '',
            'Replay %s -> %s, %d bars; cost %.2f pt / trade. Thirds by date. Live alerts since 10/19: %d signals%s.' % (
                s.date[300], s.date[-1], s.n, cost, len(lv), ' (%s -> %s)' % (s.date[min(li)], s.date[max(li)]) if li else '')]
    summ = []
    for mdl, ex in (('BOT exits', lambda i, lg: bot_exit(s, i, lg)), ('CHART exits', lambda i, lg: chart_exit(s, i, lg, q))):
        R = number(s, sig, ex); LV = number(s, lv, ex)
        for key, kn in (('sh', 'SHARED count (all setup types share one number)'), ('pt', 'PER-TYPE count (each setup type numbered on its own)')):
            out += ['', '## %s %dm -- %s -- %s' % (sym, tf, mdl, kn), '', '### A. Replay (all modelled setup types ticked)', '']
            out += order_tables(R, key, cost, s, cuts, t4, tf)
            out += ['', 'By setup type (trades / net (avg)):', ''] + type_table(R, key, cost, RT)
            vr = verdict(R, key, cost, s, cuts)
            out += ['', '**Replay verdict:** ' + vr, '', '### B. Live alerts since 10/19 (every directional alert type)', '']
            lt = [s.T[z['i']] for z in LV] or [T1]; L0, L1 = min(lt), max(lt) + 1
            out += order_tables(LV, key, cost, s, [L0 + (L1 - L0) / 3, L0 + 2 * (L1 - L0) / 3], T1 - 7 * 86400000, tf)
            out += ['', 'By alert type (trades / net (avg)):', ''] + type_table(LV, key, cost, LT)
            summ.append('%s / %s: replay -- %s' % (mdl, kn.split(' (')[0], vr))
            # live 1..N quick line
            al = [z for z in LV if z[key] > 0 and z['res'] is not None]
            if al:
                line = ', '.join('1-%d %+.2f' % (k, np.mean([z['res'] - cost for z in al if z[key] <= k])) for k in range(1, 6) if any(z[key] <= k for z in al))
                late = [z['res'] - cost for z in al if z[key] > 5]
                summ.append('    live avg/trade: %s; #6+ %s; all %+.2f (%d)' % (line, ('%+.2f (%d)' % (np.mean(late), len(late))) if late else '-', np.mean([z['res'] - cost for z in al]), len(al)))
    out += ['', '### %s %dm summary' % (sym, tf), ''] + ['- ' + x for x in summ]
    return summ


if __name__ == '__main__':
    out = ['# Setup order since the HTF CBC flip -- MES + MGC 2m / 3m / 5m -- %s' % D.datetime.now(TZ).strftime('%Y-%m-%d %H:%M ET'), '', __doc__]
    allsum = {}
    for sym, tf in CHARTS:
        try:
            allsum['%s %dm' % (sym, tf)] = run_chart(sym, tf, out)
        except Exception as e:
            out += ['', '# %s %dm FAILED: %r' % (sym, tf, e)]
        print('done', sym, tf, file=sys.stderr, flush=True)
    top = ['', '## Overview', '']
    for k, v in allsum.items(): top += ['**%s**' % k, ''] + ['- ' + x for x in v] + ['']
    name = 'flip_order_report.md' if len(sys.argv) == 1 else 'flip_order_%s.md' % '_'.join(a.replace(':', '') for a in sys.argv[1:])
    open(name, 'w').write('\n'.join(out[:3] + top + out[3:]))
    print('\n'.join(top))
