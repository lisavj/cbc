"""Databento ohlcv-1m (parent symbols) -> TradingView-style front-month continuous 2m/3m/5m bars with BarFeed fields.
Roll: front = contract with the highest volume in that session (18:00 ET day; matches TradingView MNQ1! on 9/15), never moving back to an earlier
expiry; unadjusted prices (same as TradingView MES1!/MGC1!). Calendar spreads dropped."""
import pandas as pd, numpy as np, sys
MON = 'FGHJKMNQUVXZ'
def rank(sym):  # MESZ6 -> sortable expiry
    return int(sym[-1]) * 12 + MON.index(sym[-2])

def front_map(d, root):
    x = d[d.root == root]
    v = x.groupby(['sday', 'symbol']).volume.sum().reset_index()
    lead = v.loc[v.groupby('sday').volume.idxmax()].set_index('sday').symbol.sort_index()
    out = {}; cur = None
    for dd in sorted(x.sday.unique()):
        if cur is None or rank(lead[dd]) > rank(cur): cur = lead[dd]
        out[dd] = cur
    return out

def ema(a, n):
    out = np.full(len(a), np.nan); k = 2 / (n + 1); s = np.nan
    for i, x in enumerate(a):
        if i < n - 1: continue
        s = np.mean(a[:n]) if np.isnan(s) else x * k + s * (1 - k)  # Pine: seeded with SMA
        out[i] = s
    return out

SETTLE = {'MGC': ('America/New_York', '13:29'), 'BTC': ('Europe/London', '15:59')}  # others: 15:59 ET (equity index)

def settlements(x, root):
    tz, hhmm = SETTLE.get(root, ('America/New_York', '15:59'))
    loc = pd.to_datetime(x.t, unit='ms', utc=True).dt.tz_convert(tz).dt.strftime('%H:%M')
    last = x.groupby('sday').close.last()
    st = x[loc <= hhmm].groupby('sday').close.last() if True else None
    # only use the settlement-minute close when that minute belongs to the same session's day session
    return st.reindex(last.index).fillna(last)

def build(d, root, tf, fm):
    x = d[(d.root == root) & (d.symbol == d.sday.map(fm))].sort_values('t')
    settle = settlements(x, root)
    ms = tf * 60000
    x = x.assign(b=x.t // ms * ms)
    B = x.groupby('b').agg(o=('open', 'first'), h=('high', 'max'), l=('low', 'min'), c=('close', 'last'), v=('volume', 'sum'), sday=('sday', 'first')).reset_index().rename(columns={'b': 't'})
    B['contract'] = B.sday.map(fm)
    c = B.c.values
    B['e9'], B['e20'], B['e200'] = ema(c, 9), ema(c, 20), ema(c, 200)
    hlc3 = (B.h + B.l + B.c) / 3
    pv = (hlc3 * B.v).groupby(B.sday).cumsum(); vv = B.v.groupby(B.sday).cumsum()
    B['vw'] = np.where(vv > 0, pv / vv.replace(0, np.nan), hlc3)
    # HTF = 5x, buckets anchored to the 18:00 ET session start
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)  # 18:00 ET previous calendar day
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = B.sday + '_' + (mins // (5 * tf)).astype(str)
    H = B.groupby('hk', sort=False).agg(h=('h', 'max'), l=('l', 'min'), c=('c', 'last'), last=('t', 'max')).reset_index()
    H['h9'], H['h20'] = ema(H.c.values, 9), ema(H.c.values, 20)
    st = []; s = False
    for i in range(len(H)):
        if i:
            if s and H.c[i] < H.l[i - 1]: s = False
            if not s and H.c[i] > H.h[i - 1]: s = True
        st.append(1.0 if s else 0.0)
    H['state'] = st
    B = B.merge(H[['hk', 'h9', 'h20', 'state', 'last']], on='hk', how='left')
    hc = np.full(len(B), np.nan); hf = np.zeros(len(B)); cur = np.nan
    for i, (t, last, stt) in enumerate(zip(B.t.values, B['last'].values, B.state.values)):
        if t == last:
            if not np.isnan(cur) and stt != cur: hf[i] = 1.0 if stt == 1 else -1.0
            cur = stt
        hc[i] = cur
    B['hc'], B['hf'] = hc, hf
    # daily pivots from the previous session
    D = B.groupby('sday').agg(H=('h', 'max'), L=('l', 'min'))
    D['C'] = settle.reindex(D.index)  # TradingView daily close for futures = settlement (approximated: close of the settlement minute)
    D = D.shift(1)
    pp = (D.H + D.L + D.C) / 3
    B['pp'] = B.sday.map(pp); B['r1'] = B.sday.map(2 * pp - D.L); B['s1'] = B.sday.map(2 * pp - D.H)
    # prior NY RTH high/low, opening ranges (30 min after 9:30 / 3:00 / 20:00 ET)
    hm = et.dt.hour * 60 + et.dt.minute
    rth = (hm >= 570) & (hm < 960); cal = et.dt.date.astype(str)
    R = B[rth].groupby(cal[rth]).agg(H=('h', 'max'), L=('l', 'min'))
    days = sorted(R.index)
    prevmap = {d2: days[i - 1] for i, d2 in enumerate(days) if i}
    # ydh set when RTH ends -> value = most recent completed RTH before this bar
    ydh = np.full(len(B), np.nan); ydl = ydh.copy(); lastH = lastL = np.nan; curd = None; cH = cL = np.nan
    for i, (r, dd, h, l) in enumerate(zip(rth.values, cal.values, B.h.values, B.l.values)):
        if r:
            if curd != dd: curd, cH, cL = dd, h, l
            else: cH, cL = max(cH, h), min(cL, l)
        elif curd is not None and not np.isnan(cH):
            lastH, lastL = cH, cL; cH = cL = np.nan; curd = None
        ydh[i], ydl[i] = lastH, lastL
    B['ydh'], B['ydl'] = ydh, ydl
    for name, startm in (('ny', 570), ('ln', 180), ('as', 1200)):
        act = (hm >= startm) & (hm < startm + 30)
        hi = np.full(len(B), np.nan); lo = hi.copy(); a_prev = False; ch = cl = np.nan
        for i, (a, h, l) in enumerate(zip(act.values, B.h.values, B.l.values)):
            if a: ch, cl = (max(ch, h), min(cl, l)) if a_prev else (h, l)
            a_prev = a; hi[i], lo[i] = ch, cl
        B[name + 'h'], B[name + 'l'] = hi, lo
    B['fl'] = 0
    return B

COLS = ['e9', 'e20', 'h9', 'h20', 'e200', 'vw', 'pp', 'r1', 's1', 'ydh', 'ydl', 'nyh', 'nyl', 'lnh', 'lnl', 'ash', 'asl', 'hc', 'hf', 'fl']
def to_csv(B, path, lo=None, hi=None):
    o = B if lo is None else B[(B.t >= lo) & (B.t < hi)]
    o = o.assign(time=o.t // 1000, open=o.o, high=o.h, low=o.l, close=o.c, Volume=o.v)
    o[['time', 'open', 'high', 'low', 'close', 'Volume'] + COLS].round(5).to_csv(path, index=False)
