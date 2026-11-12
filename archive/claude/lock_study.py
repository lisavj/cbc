"""Time + progress profit lock -- MES 3m and MGC 3m -- 11/08/2026.
Rule (before TP1): from the first candle close at least T min after entry, once the best price since entry has reached R x TP1 distance,
move SL1 to Entry + L (locked profit). L = fixed share of the TP1 distance, or 'mv' = 25 % of the best move so far (re-checked each candle,
the stop only ratchets up). If the close is already past the new stop, exit at that close. After TP1 the normal BE / trail take over
(the lock stays if it is higher). User example: T 8 min (= 9 min on 3m), R 30 %, L 25 % of TP1.
Exits: MES 3m live (SL1 3 ATR, TP1 1.75 ATR, 80/100 % by time of day); MES 3m BOT (100 % at TP1, v10.87 windows + short filter);
MGC 3m live since v10.84 (50 % at TP1, trail 3.5). Net after costs (MES 0.50 / MGC 0.22 per trade, rule exits are stop orders = no extra)."""
import numpy as np, pandas as pd, itertools, combo_study as cb, chop_sim as cs, late_study as ls, trend_guard_study as tg, mes3_ema_grid as m
class K(cb.CCase):
    TM = 0; RR = 0; LK = 0
    def sim1(s, i, lg, q, stop_at):
        C, H, Lo = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap']); part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440; part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False; best = 0.0; nb = int(np.ceil(s.TM / s.tf)) if s.TM else 10**9
        for j in range(i + 1, s.n):
            if (Lo[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); w = 'trail' if hit else ('lock' if rem > 0 else 'SL1'); return (part * tpd + (1 - part) * rem if hit else rem), j, w
            if not hit and (H[j] >= t1 if lg else Lo[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            best = max(best, g * ((H[j] if lg else Lo[j]) - en))
            if s.TM and not hit and j - i >= nb and best >= s.RR * tpd:
                lk = (0.25 * best) if s.LK == "mv" else s.LK * tpd
                nsl = en + g * lk
                if g * (C[j] - nsl) <= 0: return g * (C[j] - en), j, 'lock'
                sl = max(sl, nsl) if lg else min(sl, nsl)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'
TS = [0, 6, 9, 12, 15]; RS = [.2, .3, .4, .5]; LS = [.1, .15, .25, 'mv']
OUT = [__doc__, '']
for name, sym, q, cost, bot in (('MES 3m (chart exits)', 'MES', m.LIVE, .5, False), ('MES 3m BOT (100 % at TP1, bot windows + short filter)', 'MES', dict(m.LIVE, part=1.0), .5, True),
                                ('MGC 3m (live 50 % / trail 3.5)', 'MGC', dict(ls.MGCX, part=.5, tr=3.5), .22, False)):
    B = ls.load(sym, 3); ls.LCase.LATE = 1; ls.LCase.NYW = 30; s = K(sym, 3, B); TR, ss = tg.trend_arrays(s); G = cb.CH[sym][2]
    et = pd.to_datetime(s.B.t, unit='ms', utc=True).dt.tz_convert('America/New_York'); cm = ((et.dt.hour * 60 + et.dt.minute).values + 3) % 1440
    W = lambda c: (1110 <= c <= 1320) or (180 <= c <= 780) or (900 <= c <= 930)
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]; t4 = T1 - 28 * 86400000
    def run(t, r, l):
        K.TM, K.RR, K.LK = t, r, l; s.TX, s.TY = (0, 0.0); s.ACT = None
        def ok(d):
            if not cs.cur_rule(d): return False
            if not bot: return True
            if not W(cm[d['i']]): return False
            if d['lg']: return True
            v = TR['d5'][d['i']]; return v == 0 or v == -1
        return [dict(n=t_['res'] - cost, w=t_['why'], th=0 if s.T[t_['i']] < cuts[0] else 1 if s.T[t_['i']] < cuts[1] else 2, l4=bool(s.T[t_['i']] >= t4)) for t_ in s.run(ok, q=q, gates=G)]
    b = run(0, 0, 0); bt = [sum(x['n'] for x in b if x['th'] == k) for k in range(3)]; b4 = sum(x['n'] for x in b if x['l4']); bn = sum(x['n'] for x in b)
    res = {}
    for t, r, l in itertools.product(TS[1:], RS, LS):
        v = run(t, r, l); th = [sum(x['n'] for x in v if x['th'] == k) - bt[k] for k in range(3)]
        res[(t, r, l)] = dict(d=sum(x['n'] for x in v) - bn, th=th, d4=sum(x['n'] for x in v if x['l4']) - b4, lk=sum(1 for x in v if x['w'] == 'lock'), n=len(v))
    ln = lambda l: '25 % of the move' if l == 'mv' else '%d %% of TP1' % round(l * 100)
    fl = lambda c: ('T' if all(x > 0 for x in c['th']) else '') + ('4' if c['d4'] > 0 else '')
    OUT += ['## %s — current: %d trades, net %+.0f after costs (thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f)' % (name, len(b), bn, *bt, b4), '']
    u = res[(9, .3, .25)]
    OUT += ['**Your example (after 8 min = 9 min on 3m, at 30 %% of TP1, lock 25 %% of TP1):** Δ %+.0f (thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f, %d lock exits) %s' % (u['d'], *u['th'], u['d4'], u['lk'], fl(u)), '',
            '| Time | Reach | ' + ' | '.join('lock ' + ln(l) for l in LS) + ' |', '|---|---|' + '---|' * len(LS)]
    for t, r in itertools.product(TS[1:], RS):
        OUT.append('| %d min | %d %% | %s |' % (t, round(r * 100), ' | '.join(('%+.0f %s' % (res[(t, r, l)]['d'], fl(res[(t, r, l)]))).strip() for l in LS)))
    good = sorted([k for k in res if all(x > 0 for x in res[k]['th'])], key=lambda k: -res[k]['d'])
    pk = max(res, key=lambda k: res[k]['th'][0] + res[k]['th'][1]); l3 = sorted(res[k]['th'][2] for k in res)
    OUT += ['', 'Better in all three thirds: %d of %d. Top 3: %s' % (len(good), len(res), '; '.join('%d min / %d %% / %s %+.0f (thirds %+.0f / %+.0f / %+.0f, last 4 wk %+.0f)' % (k[0], round(k[1] * 100), ln(k[2]), res[k]['d'], *res[k]['th'], res[k]['d4']) for k in good[:3]) or 'none'),
            'Walk-forward: picked on thirds 1-2 = %d min / %d %% / %s -> third 3 Δ %+.0f (rank %d of %d).' % (pk[0], round(pk[1] * 100), ln(pk[2]), res[pk]['th'][2], sum(1 for v in l3 if v > res[pk]['th'][2]) + 1, len(l3)), '']
    print(name, 'done', flush=True)
open('lock_report.md', 'w').write('\n'.join(OUT))
