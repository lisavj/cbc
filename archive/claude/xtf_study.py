"""1H (MTF) and 4H (XTF) CBC confirmation study -- MES / MGC / MNQ / M2K 2m / 3m / 5m -- 11/12/2026.
Question: are setups / alerts better when the 1-hour CBC (and the 4-hour CBC) points the same way as the trade, and would a gate
"skip when the 1H / 4H CBC is against" (or "only take when it agrees") help?
1H / 4H CBC: rebuilt from the chart's own candles with the CBC rule (bullish once a period closes above the previous period's high,
bearish once one closes below the previous period's low), using only COMPLETED periods (no look-ahead) -- same as chop_sim's 1H
MTF state that CBC's "1H MTF gate" uses. 1H = clock hours; 4H = CME 4-hour candles from 18:00 ET (18 / 22 / 02 / 06 / 10 / 14).
Groups: 1H agrees / 1H against; 4H agrees / 4H against; both agree; 1H agrees + 4H against; 1H against + 4H agrees; both against.
Signals: REPLAY (chop_sim, Jan 5 -> now; 2m Jun 1 -> now) every modelled Trade Setup trigger with the chart's live gates EXCEPT the
1H MTF gate (off everywhere here so the against setups can be scored -- MES 2m runs it live) + ER / breakout rule. LIVE = every
directional alert since 10/19 incl. Trade Setups (duplicates once; MES 2m live Trade Setups are already 1H-gated).
Same-type repeats within 7 candles skipped unless the earlier trade had closed. Every signal scored on its own.
Exits: BOT = SL 3 ATR / TP 1.75 ATR, else HTF CBC flip against or 15:57 flatten. CHART = each chart's CBC exits (MES / MGC 3m live;
others base 1.7 / 1.7 / 80 % / BE / trail 1.7 with per-symbol min / cap). Net after costs: MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35.
Gate verdict (per chart, per gate): CANDIDATE if the blocked group is net negative in all three replay thirds under BOTH exits,
the kept avg beats all under both exits, and live blocked (30+ trades) is net negative with a lower avg than live kept.
"""
import re, sys, json, collections, datetime as D
import numpy as np, pandas as pd
from zoneinfo import ZoneInfo
import chop_sim as cs, stretch_study as ss, flip_order_study as fo

TZ = ZoneInfo('America/New_York')
ss.FROM[5] = '2026-01-05'
COST = {'MES': .5, 'MGC': .22, 'MNQ': .87, 'M2K': .35}
BASEQ = {'MES': ss.QB['MES'], 'MGC': ss.QB['MGC'],
         'MNQ': dict(sl=1.7, mn=25, cap=30, tp=1.7, tcap=40, part=.8, be=True, ts=0, tr=1.7),
         'M2K': dict(sl=1.7, mn=3, cap=5, tp=1.7, tcap=3, part=.8, be=True, ts=0, tr=1.7)}


def dedup(s, sig, ex):
    """same-type repeats within 7 candles skipped unless that trade already closed."""
    out = []; last = {}
    for (i, lg, typ, x) in sorted(sig, key=lambda z: z[0]):
        r, j = ex(i, lg)
        k = (typ, lg)
        if k in last and i - last[k][0] < 7 and (last[k][1] is None or last[k][1] >= i): continue
        last[k] = (i, j); out.append((i, lg, typ, x, r))
    return out


def cbc_state(s, key):
    """CBC state (1 bull / 0 bear / -1 unknown) of the last COMPLETED period, per chart candle; key = period id per candle."""
    df = pd.DataFrame({'k': key, 'h': s.H, 'l': s.L, 'c': s.C})
    g = df.groupby('k', sort=False).agg(h=('h', 'max'), l=('l', 'min'), c=('c', 'last'))
    st = {}; prev = None; stt = -1
    for k2, row in g.iterrows():
        if prev is not None:
            if stt != 0 and row.c < prev.l: stt = 0
            elif stt != 1 and row.c > prev.h: stt = 1
        st[k2] = stt; prev = row
    keys = list(g.index); before = {keys[i]: keys[i - 1] for i in range(1, len(keys))}
    return np.array([st.get(before.get(k2), -1) for k2 in key])


def periods(s):
    et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    h1 = (s.T // 3600000)
    sess = (et - pd.Timedelta(hours=18))
    day = sess.dt.normalize().dt.strftime('%Y%m%d').values
    h4 = np.array(['%s_%d' % (d, h // 4) for d, h in zip(day, sess.dt.hour.values)])
    return cbc_state(s, h1), cbc_state(s, h4)


def grp(m1, m4, i, lg):
    w = 1 if lg else 0
    a1 = None if m1[i] < 0 else bool(m1[i] == w); a4 = None if m4[i] < 0 else bool(m4[i] == w)
    return a1, a4


def stat(v, cost, cuts, T):
    v = [z for z in v if z['res'] is not None]
    if not v: return None
    x = np.array([z['res'] - cost for z in v])
    th = [sum(z['res'] - cost for z in v if (0 if T[z['i']] < cuts[0] else 1 if T[z['i']] < cuts[1] else 2) == k) for k in range(3)]
    return dict(n=len(x), w=100 * (x > 0).mean(), net=x.sum(), avg=x.mean(), th=th)


def row(lb, st):
    if not st: return '| %s | 0 | | | | |' % lb
    return '| %s | %d | %.0f %% | %+.1f | %+.2f | %+.0f / %+.0f / %+.0f |' % (lb, st['n'], st['w'], st['net'], st['avg'], *st['th'])


GROUPS = [('All', lambda a1, a4: True), ('1H agrees', lambda a1, a4: a1 is True), ('1H against', lambda a1, a4: a1 is False),
          ('4H agrees', lambda a1, a4: a4 is True), ('4H against', lambda a1, a4: a4 is False),
          ('Both agree', lambda a1, a4: a1 is True and a4 is True), ('1H agrees, 4H against', lambda a1, a4: a1 is True and a4 is False),
          ('1H against, 4H agrees', lambda a1, a4: a1 is False and a4 is True), ('Both against', lambda a1, a4: a1 is False and a4 is False),
          ('Either against', lambda a1, a4: a1 is False or a4 is False)]
GATES = [('skip 1H against', '1H against'), ('skip 4H against', '4H against'), ('skip either against (= take only both agree)', 'Either against'),
         ('skip both against', 'Both against')]


def run_chart(sym, tf, out):
    B = ss.load(sym, tf); s = cs.Case(sym, tf, B); cost = COST[sym]
    G = dict(cs.GATE.get((sym, tf), dict(R5=0, X4=0, MTF=0)), MTF=0)
    q = cs.EXIT.get((sym, tf), BASEQ[sym]); q = dict(q, ts=q.get('ts', 0), tcap=q.get('tcap', 6))
    e9 = B.e9.values.astype(float); m1, m4 = periods(s)
    T0, T1 = s.T[300], s.T[-1]
    sig = []
    for d in s.cands:
        if G['R5'] and d['R5']: continue
        if G['X4'] and d['X4']: continue
        if d['VB']: continue
        if d['trig'] != 'flip' and d['er'][12] < d['erm']: continue
        if not cs.cur_rule(d): continue
        i = d['i']
        ty = 'HTF CBC Flip' if d['trig'] == 'flip' else ('LTF Pierce late' if d.get('late') else ('LTF Pierce beyond EMA9' if ((s.C[i] > e9[i]) if d['lg'] else (s.C[i] < e9[i])) else 'LTF Pierce not beyond EMA9')) if d['trig'] == 'ltf20' else {'h9': 'HTF EMA9 Pierce', 'h20': 'HTF EMA20 Pierce'}[d['trig']]
        sig.append((i, d['lg'], ty, None))
    lv = fo.live_signals(s, sym, tf)
    # cross-check rebuilt 1H vs CBC's own "MTF CBC (1H)" line on live Trade Setups
    chk = [0, 0]
    tix = {int(t): k for k, t in enumerate(s.T)}
    for a in fo.ALERTS:
        r = a['raw'] if isinstance(a['raw'], str) else json.dumps(a['raw'])
        if not r.startswith(sym) or 'Trade Setup:' not in r: continue
        mm = re.search(r'Chart: \S+\s+(\d+)m', r)
        if not mm or int(mm[1]) != tf: continue
        mt = re.search(r'Time: (\d+)/(\d+) (\d+):(\d+)', r); x = re.search(r'MTF CBC \(1H\): (\w+)', r)
        if not mt or not x: continue
        ct = D.datetime(int(a['receivedAt'][:4]), int(mt[1]), int(mt[2]), int(mt[3]), int(mt[4]), tzinfo=TZ)
        i = tix.get(int(ct.timestamp() * 1000) - tf * 60000)
        if i is None or m1[i] < 0 or x[1] not in ('Bullish', 'Bearish'): continue
        chk[0] += 1; chk[1] += (m1[i] == 1) == (x[1] == 'Bullish')
    out += ['', '# %s %dm' % (sym, tf), '', 'Replay %s -> %s; cost %.2f pt / trade; live alerts since 10/19: %d signals. Rebuilt 1H CBC matches CBC\'s own "MTF CBC (1H)" line on %d of %d live Trade Setups.' % (
        s.date[300], s.date[-1], cost, len(lv), chk[1], chk[0])]
    res = {}
    for src, SG in (('REPLAY', sig), ('LIVE', lv)):
        for mdl, ex in (('BOT', lambda i, lg: fo.bot_exit(s, i, lg)), ('CHART', lambda i, lg: fo.chart_exit(s, i, lg, q))):
            R = dedup(s, SG, ex)
            rows = []
            for (i, lg, t, x, r) in R:
                a1, a4 = grp(m1, m4, i, lg); rows.append(dict(i=i, lg=lg, typ=t, res=r, a1=a1, a4=a4))
            if src == 'LIVE':
                lt = [s.T[z['i']] for z in rows] or [T1]; a0, b0 = min(lt), max(lt) + 1; cuts = [a0 + (b0 - a0) / 3, a0 + 2 * (b0 - a0) / 3]
            else: cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
            S = {g: stat([z for z in rows if f(z['a1'], z['a4'])], cost, cuts, s.T) for g, f in GROUPS}
            res[(src, mdl)] = S
            out += ['', '## %s %dm -- %s -- %s exits' % (sym, tf, src, mdl), '', '| Group | Trades | Win % | Net | Avg / trade | Thirds (by date) |', '|---|---|---|---|---|---|']
            out += [row(g, S[g]) for g, _ in GROUPS]
            if mdl == 'BOT':
                types = [t for t, _ in collections.Counter(z['typ'] for z in rows).most_common()]
                out += ['', 'By type (trades / net / avg), bot exits:', '', '| Type | 1H agrees | 1H against | 4H agrees | 4H against | Both agree | Either against |', '|---|---|---|---|---|---|---|']
                for t in types:
                    v = [z for z in rows if z['typ'] == t and z['res'] is not None]
                    if len(v) < 15: continue
                    cell = lambda f: (lambda w: '%d / %+.0f / %+.2f' % (len(w), sum(w), np.mean(w)) if w else '-')([z['res'] - cost for z in v if f(z['a1'], z['a4'])])
                    out.append('| %s | %s |' % (t, ' | '.join(cell(dict(GROUPS)[g]) for g in ('1H agrees', '1H against', '4H agrees', '4H against', 'Both agree', 'Either against'))))
    # gate verdicts
    summ = []
    for gname, blk in GATES:
        rb, rc = res[('REPLAY', 'BOT')], res[('REPLAY', 'CHART')]; lb, lc = res[('LIVE', 'BOT')], res[('LIVE', 'CHART')]
        def kept(S):
            a, b = S['All'], S[blk]
            if not a: return None
            nb = b['n'] if b else 0; netb = b['net'] if b else 0
            return (a['net'] - netb) / max(1, a['n'] - nb)
        ok_rep = all(S[blk] and all(t < 0 for t in S[blk]['th']) and kept(S) > S['All']['avg'] for S in (rb, rc))
        ok_live = lb[blk] is not None and lb[blk]['n'] >= 30 and lb[blk]['net'] < 0 and lb[blk]['avg'] < kept(lb)
        v = 'CANDIDATE' if ok_rep and ok_live else 'replay yes, live no' if ok_rep else 'live yes, replay no' if ok_live else 'no'
        f = lambda S: ('%d / %+.0f (%s)' % (S[blk]['n'], S[blk]['net'], ' / '.join('%+.0f' % t for t in S[blk]['th']))) if S[blk] else '0'
        summ.append('%s: **%s** -- blocked replay bot %s, chart %s; live bot %s (kept avg %+.2f vs all %+.2f)' % (
            gname, v, f(rb), f(rc), f(lb), kept(lb) or 0, lb['All']['avg'] if lb['All'] else 0))
    out += ['', '### %s %dm gate verdicts' % (sym, tf), ''] + ['- ' + x for x in summ]
    return summ, res


if __name__ == '__main__':
    ch = [(a.split(':')[0], int(a.split(':')[1])) for a in sys.argv[1:]] or [(s, t) for s in ('MES', 'MGC', 'MNQ', 'M2K') for t in (3, 2, 5)]
    out = ['# 1H (MTF) and 4H (XTF) CBC confirmation -- MES / MGC / MNQ / M2K 2m / 3m / 5m -- %s' % D.datetime.now(TZ).strftime('%Y-%m-%d %H:%M ET'), '', __doc__]
    top = ['', '## Overview (avg pts / trade after costs; replay bot | replay chart | live bot)', '',
           '| Chart | All | 1H agrees | 1H against | 4H agrees | 4H against | Both agree | Both against |', '|---|---|---|---|---|---|---|---|']
    ver = ['', '## Gate verdicts', '']
    for sym, tf in ch:
        try:
            sm, R = run_chart(sym, tf, out)
            c = lambda g: ' / '.join(('%+.2f' % R[k][g]['avg']) if R[k][g] else '-' for k in (('REPLAY', 'BOT'), ('REPLAY', 'CHART'), ('LIVE', 'BOT')))
            top.append('| %s %dm | %s |' % (sym, tf, ' | '.join(c(g) for g in ('All', '1H agrees', '1H against', '4H agrees', '4H against', 'Both agree', 'Both against'))))
            ver += ['**%s %dm**' % (sym, tf), ''] + ['- ' + x for x in sm] + ['']
        except Exception as e:
            import traceback; traceback.print_exc(); out += ['', '# %s %dm FAILED: %r' % (sym, tf, e)]
        print('done', sym, tf, file=sys.stderr, flush=True)
    open('xtf_report.md', 'w').write('\n'.join(out[:3] + top + ver + out[3:])); print('\n'.join(top + ver))
