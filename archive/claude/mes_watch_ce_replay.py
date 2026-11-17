#!/usr/bin/env python3
"""(C) 5m-confirmation replay and (E) exit-rule replay -- rc run 11/13/2026.
Engines: chop_sim / mes3_ema_grid / late_study (local copies, tr>0 trail guard added).
  MES 3m: mes3_ema_grid.MCase, slow 20, range gate R5, LIVE exits (as stored, part='tod') [+ part=1.0 variant]
  MES 2m: chop_sim.Case gen (1H MTF gate computed), slow 14, gates MTF=1, base exits MESX, bars from 06/01
  MES 5m: chop_sim.Case gen, slow 20, no gates, base exits MESX
  MGC 3m: chop_sim.Case gen (X4 + FD 10), slow 20, gates R5+X4, chop_sim EXIT[('MGC',3)] and FLIP 0 % (part 0, tr 0)
"""
import os, sys, pickle, numpy as np, pandas as pd, datetime as D
import chop_sim as cs, mes3_ema_grid as m, late_study as ls

CACHE = '/home/claude/w/rc/cache'; os.makedirs(CACHE, exist_ok=True)

def bars(sym, tf):
    p = '%s/%s_%d.pkl' % (CACHE, sym, tf)
    if os.path.exists(p): return pd.read_pickle(p)
    B = ls.load(sym, tf); B.to_pickle(p); return B

class Rule:
    TX = 0; TY = 0.0; AX = 0.0; LA = 0.0; LT = 0.0
    def sim1(s, i, lg, q, stop_at):
        C, H, L, O = s.C, s.H, s.L, s.O; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            mm = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= mm < 960 or 1080 <= mm < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        cut_on = s.TX > 0 and np.isfinite(s.atrrel[i]) and s.atrrel[i] >= s.AX
        tnb = int(np.ceil(s.TX / s.tf)) if cut_on else 10 ** 9; red = en + g * s.TY * tpd
        lock_on = s.LA > 0; locked = False; la = en + g * s.LA * tpd; lt = en + g * s.LT * tpd
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en)
                return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else ('LOCK' if locked else 'SL1'))
            if not hit and j - i > tnb:
                if (O[j] >= red) if lg else (O[j] <= red): return g * (O[j] - en), j, 'TPx'
                if (H[j] >= red) if lg else (L[j] <= red): return s.TY * tpd, j, 'TPx'
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if lock_on and not locked and ((H[j] >= la) if lg else (L[j] <= la)):
                locked = True; sl = max(sl, lt) if lg else min(sl, lt)
            if hit and q['tr'] > 0:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

class R3(Rule, m.MCase): pass          # MES 3m: strict toward flips, MCase gen
class RC(Rule, cs.Case): pass          # chop_sim gen (MTF / X4 / FD per symbol), Rule exits

def mk(cls, sym, tf, slow):
    B = bars(sym, tf).copy(); B['e20'] = m.ema(B.c.values.astype(float), slow)
    return cls(sym, tf, B)

def setrule(**k):
    for c in (Rule,):
        c.TX = k.get('TX', 0); c.TY = k.get('TY', 0.0); c.AX = k.get('AX', 0.0); c.LA = k.get('LA', 0.0); c.LT = k.get('LT', 0.0)

def run(s, q, G, **k):
    setrule(**k); r = s.run(lambda d: cs.cur_rule(d), q=q, gates=G); setrule(); return r

fmt = lambda t: D.datetime.utcfromtimestamp(t / 1000 - 5 * 3600).strftime('%m/%d')

def thirds(s):
    T0, T1 = s.T[300], s.T[-1]; cuts = [T0 + (T1 - T0) * k / 3 for k in (1, 2)]
    return cuts, (lambda i: 0 if s.T[i] < cuts[0] else 1 if s.T[i] < cuts[1] else 2)

# ---------------- (C)
def conf_split(s, res, s5, r5, win=10):
    tf = s.tf; ms = 60000
    S5 = np.array([s5.T[r['i']] + 5 * ms for r in r5]); E5 = np.array([s5.T[r['j']] + 5 * ms for r in r5]); L5 = np.array([r['lg'] for r in r5])
    out = []
    for r in res:
        if r['why'] == 'end': continue
        x = s.T[r['i']] + tf * ms; same = L5 == r['lg']
        op = same & (S5 <= x) & (E5 > x); near = same & (np.abs(S5 - x) <= win * ms)
        out.append((r, bool((op | near).any())))
    return out

def cstats(s, sp, label):
    cuts, th = thirds(s)
    c = np.array([r['res'] for r, f in sp if f]); u = np.array([r['res'] for r, f in sp if not f])
    d = c.mean() - u.mean(); z = d / np.sqrt(c.var(ddof=1) / len(c) + u.var(ddof=1) / len(u))
    tt = []
    for k in range(3):
        ck = [r['res'] for r, f in sp if f and th(r['i']) == k]; uk = [r['res'] for r, f in sp if not f and th(r['i']) == k]
        tt.append((np.mean(ck) if ck else np.nan) - (np.mean(uk) if uk else np.nan))
    t4 = s.T[-1] - 28 * 86400000
    c4 = [r['res'] for r, f in sp if f and s.T[r['i']] >= t4]; u4 = [r['res'] for r, f in sp if not f and s.T[r['i']] >= t4]
    return dict(label=label, nc=len(c), ac=c.mean(), nu=len(u), au=u.mean(), d=d, z=z, th=tt,
                n4c=len(c4), a4c=np.mean(c4) if c4 else np.nan, n4u=len(u4), a4u=np.mean(u4) if u4 else np.nan,
                span='%s→%s' % (fmt(s.T[0]), fmt(s.T[-1])), cuts='%s / %s' % (fmt(cuts[0]), fmt(cuts[1])))

# ---------------- (E)
def estats(s, r, b):
    cuts, th = thirds(s); t4 = s.T[-1] - 28 * 86400000
    v = sum(t['res'] for t in r) - sum(t['res'] for t in b)
    tt = [sum(t['res'] for t in r if th(t['i']) == k) - sum(t['res'] for t in b if th(t['i']) == k) for k in range(3)]
    d4 = sum(t['res'] for t in r if s.T[t['i']] >= t4) - sum(t['res'] for t in b if s.T[t['i']] >= t4)
    bi = {t['i']: t['res'] for t in b}; ri = {t['i']: t['res'] for t in r}
    ch = sum(1 for i in set(bi) | set(ri) if abs(bi.get(i, 0) - ri.get(i, 0)) > 1e-9) or 1
    sd = float(np.std([t['res'] for t in b])) or 1
    hits = sum(1 for t in r if t['why'] in ('TPx', 'LOCK'))
    return dict(d=v, z=v / (sd * np.sqrt(ch)), th=tt, d4=d4, ch=ch, hits=hits, n=len(r), net=sum(t['res'] for t in r))

def main():
    out = []
    G3 = dict(R5=1, X4=0, MTF=0)
    s3 = mk(R3, 'MES', 3, 20); print('MES3', s3.n, fmt(s3.T[0]), fmt(s3.T[-1]), flush=True)
    s2 = mk(RC, 'MES', 2, 14); print('MES2', s2.n, fmt(s2.T[0]), fmt(s2.T[-1]), flush=True)
    s5 = mk(RC, 'MES', 5, 20); print('MES5', s5.n, fmt(s5.T[0]), fmt(s5.T[-1]), flush=True)
    sg = mk(RC, 'MGC', 3, 20); print('MGC3', sg.n, fmt(sg.T[0]), fmt(sg.T[-1]), flush=True)
    for nm, s in (('MES 3m', s3), ('MES 2m', s2), ('MES 5m', s5), ('MGC 3m', sg)):
        dt = np.diff(s.T) / 60000; gaps = (dt > 3 * s.tf * 20)  # > 20 candles * 3 (rough) excluding weekends checked below
        big = [(fmt(s.T[k]), round(dt[k] / 60)) for k in np.where(dt > 6 * 60)[0] if not (pd.Timestamp(s.T[k], unit='ms').dayofweek in (4, 5))]
        out.append('DATA %s: %d candles %s→%s; non-weekend gaps > 6 h: %s' % (nm, s.n, fmt(s.T[0]), fmt(s.T[-1]), big[:12]))
    # (C)
    r5 = run(s5, ls.MESX, dict(R5=0, X4=0, MTF=0))
    r2 = run(s2, ls.MESX, dict(R5=0, X4=0, MTF=1))
    r3 = run(s3, m.LIVE, G3)
    r3b = run(s3, dict(m.LIVE, part=1.0), G3)
    C = [cstats(s2, conf_split(s2, r2, s5, r5), 'MES 2m by 5m'), cstats(s3, conf_split(s3, r3, s5, r5), 'MES 3m by 5m (LIVE tod)'),
         cstats(s3, conf_split(s3, r3b, s5, r5), 'MES 3m by 5m (part 1.0)')]
    out.append('C engine nets: MES5 %d / %+.0f; MES2 %d / %+.0f; MES3 tod %d / %+.0f; MES3 p1 %d / %+.0f' % (
        len(r5), sum(r['res'] for r in r5), len(r2), sum(r['res'] for r in r2), len(r3), sum(r['res'] for r in r3), len(r3b), sum(r['res'] for r in r3b)))
    out.append('| Chart | Span | Conf n / avg | Unconf n / avg | Δ avg | z | Δ by third | Last 4 wk conf / unconf |')
    out.append('|---|---|---|---|---|---|---|---|')
    for c in C:
        out.append('| %s | %s (thirds cut %s) | %d / %+.2f | %d / %+.2f | %+.2f | %+.1f | %+.2f / %+.2f / %+.2f | %d / %+.2f · %d / %+.2f |' % (
            c['label'], c['span'], c['cuts'], c['nc'], c['ac'], c['nu'], c['au'], c['d'], c['z'], *c['th'], c['n4c'], c['a4c'], c['n4u'], c['a4u']))
    # (E a) MES 3m TP cut
    out.append('\n(E a) MES 3m TP cut')
    VA = [('21 min / 70 % / 1.5x (rule)', 21, .70, 1.5), ('15 min', 15, .70, 1.5), ('18 min', 18, .70, 1.5), ('24 min', 24, .70, 1.5),
          ('65 %', 21, .65, 1.5), ('75 %', 21, .75, 1.5), ('ATR 1.4x', 21, .70, 1.4), ('ATR 1.6x', 21, .70, 1.6)]
    for bn, q in (('LIVE as stored (tod)', m.LIVE), ('LIVE part=1.0 (v10.95 live)', dict(m.LIVE, part=1.0))):
        b = run(s3, q, G3)
        out.append('Base %s: %d setups, net %+.1f' % (bn, len(b), sum(t['res'] for t in b)))
        out.append('| Variant | Δ | z | Δ by third | Last 4 wk Δ | Rule exits | Setups changed |'); out.append('|---|---|---|---|---|---|---|')
        for vn, tx, ty, ax in VA:
            r = run(s3, q, G3, TX=tx, TY=ty, AX=ax); st = estats(s3, r, b)
            out.append('| %s | %+.1f | %+.1f | %+.0f / %+.0f / %+.0f | %+.1f | %d | %d |' % (vn, st['d'], st['z'], *st['th'], st['d4'], st['hits'], st['ch']))
    # (E b) MGC 3m profit lock
    out.append('\n(E b) MGC 3m profit lock')
    GG = cs.GATE[('MGC', 3)]
    VB = [('75 % → +55 % (rule)', .75, .55), ('70 % → +55 %', .70, .55), ('80 % → +55 %', .80, .55), ('75 % → +50 %', .75, .50), ('75 % → +60 %', .75, .60)]
    for bn, q in (('chop_sim EXIT MGC 3m (50 % + BE + trail 3.5, v10.84)', cs.EXIT[('MGC', 3)]),
                  ('FLIP 0 % (part 0, BE at TP1, no trail, v10.96 live)', dict(cs.EXIT[('MGC', 3)], part=0, tr=0))):
        b = run(sg, q, GG)
        out.append('Base %s: %d setups, net %+.1f' % (bn, len(b), sum(t['res'] for t in b)))
        out.append('| Variant | Δ | z | Δ by third | Last 4 wk Δ | Lock exits | Setups changed |'); out.append('|---|---|---|---|---|---|---|')
        for vn, la, lt in VB:
            r = run(sg, q, GG, LA=la, LT=lt); st = estats(sg, r, b)
            out.append('| %s | %+.1f | %+.1f | %+.0f / %+.0f / %+.0f | %+.1f | %d | %d |' % (vn, st['d'], st['z'], *st['th'], st['d4'], st['hits'], st['ch']))
    cuts3, _ = thirds(s3); cutsg, _ = thirds(sg)
    out.append('\nThirds MES 3m: %s→%s / %s / %s→%s; MGC 3m cuts %s / %s; last 4 wk from %s (MES 3m) / %s (MGC 3m)' % (
        fmt(s3.T[300]), fmt(cuts3[0]), fmt(cuts3[1]), fmt(cuts3[1]), fmt(s3.T[-1]), fmt(cutsg[0]), fmt(cutsg[1]),
        fmt(s3.T[-1] - 28 * 86400000), fmt(sg.T[-1] - 28 * 86400000)))
    txt = '\n'.join(out); print(txt); open('/home/claude/w/rc/rc_out.md', 'w').write(txt)

if __name__ == '__main__':
    main()
