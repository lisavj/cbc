"""Engine = project claude/mes3_ema_grid.py MCase + claude/late_study.py LCase / load (unchanged logic, trimmed)."""
import gzip, json, time, os, urllib.request, numpy as np, pandas as pd
import chop_sim as cs
BASE = 'https://tv-webhook-dashboard.onrender.com'

def get(url):
    err = None
    for _ in range(4):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=300) as r:
                b = r.read()
                if r.headers.get('Content-Encoding') == 'gzip': b = gzip.decompress(b)
                return json.loads(b.decode())
        except Exception as e:
            err = e; time.sleep(20)
    raise err

def ema(x, n): return pd.Series(x).ewm(span=n, adjust=False).mean().values

class MCase(cs.Case):
    def gen(s):
        C, H, L = s.C, s.H, s.L; out = []; n = s.n; hk = 5
        e20, h9, h20 = s.e20, s.h9, s.h20
        flip_ok = np.zeros(n, bool); fev = np.zeros(n, int); fo = False
        for i in range(n):
            if s.hf[i] != 0:
                away = (C[i] > h20[i]) if s.hf[i] == 1 else (C[i] < h20[i])
                fo = away
                if away: fev[i] = s.hf[i]
            flip_ok[i] = fo
        om = (s.hm - s.tf) % 1440
        orf = ((om >= 570) & (om < 570 + getattr(s, 'NYW', 30))) | ((om >= 180) & (om < 210)) | ((om >= 1200) & (om < 1230))
        vwb = np.zeros(n, int); st = 0; lastb = -99; bdir = 0
        for i in range(1, n):
            xd = C[i] < s.vw[i] and C[i - 1] >= s.vw[i - 1]; xu = C[i] > s.vw[i] and C[i - 1] <= s.vw[i - 1]
            if (xu and st == -1) or (xd and st == 1): lastb = i; bdir = st
            st = 0 if s.hf[i] != 0 else (-1 if (xd and s.hdir[i] == 0) else 1 if (xu and s.hdir[i] == 1) else 0 if (xu or xd) else st)
            vwb[i] = bdir if i - lastb <= 5 else 0
        s.vwb = vwb
        lastp = -99
        def pierce(line, i, lg):
            if lg: return L[i - 1] > line[i - 1] and L[i] <= line[i] <= H[i]
            return H[i - 1] < line[i - 1] and L[i] <= line[i] <= H[i]
        for i in range(250, n - 1):
            if np.isnan(s.atr[i]) or s.hdir[i] < 0: continue
            hm = s.hm[i]
            if 16 * 60 <= hm < 18 * 60 + 30 or orf[i]: continue
            dirn = s.hdir[i] == 1
            if not flip_ok[i]: continue
            if fev[i] != 0:
                lg = fev[i] == 1; vw, e2 = s.vw[i], s.e200[i]
                side = (C[i] > max(vw, e2) + 1) if lg else (C[i] < min(vw, e2) - 1)
                vws = (s.vw[i] - s.vw[i - hk]) * (1 if lg else -1) > 0
                fd = abs(C[i] - e20[i]) <= max(2 * s.atr[i], 8)
                if side and vws and fd: out.append(dict(i=i, lg=lg, trig='flip'))
            for nm, line, mn in (('ltf20', e20, .08), ('h9', h9, .15), ('h20', h20, .15)):
                lg = dirn
                if nm == 'ltf20' and pierce(line, i, lg):
                    if i - lastp <= 3: continue
                    lastp = i
                if pierce(line, i, lg):
                    if (C[i] > line[i]) if lg else (C[i] < line[i]): out.append(dict(i=i, lg=lg, trig=nm, erm=mn))
                    elif i + 1 < n and s.hdir[i + 1] == s.hdir[i] and ((C[i + 1] > line[i + 1]) if lg else (C[i + 1] < line[i + 1])): out.append(dict(i=i + 1, lg=lg, trig=nm, erm=mn, late=1))
        out.sort(key=lambda d: (d['i'], d['trig'] != 'flip'))
        for d in out:
            i = d['i']; lg = d['lg']; A = s.atr[i]; gg = 1 if lg else -1
            hi = s.H[i - 23:i + 1].max(); lo = s.L[i - 23:i + 1].min(); pos = (C[i] - lo) / (hi - lo) if hi > lo else .5
            d['R5'] = (pos if lg else 1 - pos) >= .8 and (hi - lo) / A < 5
            d['xv'] = gg * (C[i] - s.vw[i]) / A; d['X4'] = d['xv'] > 4; d['M'] = False   # 11/14 fix: was X4 = False (MGC stretch gate never applied)
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={k: s.er[k][i] for k in s.er}, bo=bool(s.bo[i]), month=s.month[i])
        return out
    def sim1(s, i, lg, q, stop_at):
        C, H, L = s.C, s.H, s.L; en = C[i]; A = s.atr[i]; g = 1 if lg else -1
        sd = max(min(q['sl'] * A, q['cap']), q['mn']); tpd = min(q['tp'] * A, q['tcap'])
        part = q['part']
        if part == 'tod':
            m = (s.hm[i] - s.tf) % 1440
            part = .8 if (360 <= m < 960 or 1080 <= m < 1350) else 1.0
        sl = en - g * sd; t1 = en + g * tpd; hit = False
        for j in range(i + 1, s.n):
            if (L[j] <= sl if lg else H[j] >= sl):
                rem = g * (sl - en); return (part * tpd + (1 - part) * rem if hit else rem), j, ('trail' if hit else 'SL1')
            if not hit and (H[j] >= t1 if lg else L[j] <= t1):
                hit = True
                if part >= 1: return tpd, j, 'TP1'
                if q['be']: sl = max(sl, en) if lg else min(sl, en)
            if hit:
                ns = C[j] - g * q['tr'] * s.atr[j]; sl = max(sl, ns) if lg else min(sl, ns)
            why = None
            if s.hdir[j] == (0 if lg else 1): why = 'flip'
            elif s.hm[j] == 16 * 60: why = '16:00'
            elif j == stop_at: why = 'new'
            if why:
                rem = g * (C[j] - en); return (part * tpd + (1 - part) * rem if hit else rem), j, why
        return 0.0, s.n - 1, 'end'

class LCase(MCase):
    LATE = 1; NYW = 30
    def gen(s):
        late = s.LATE
        out = MCase.gen(s)
        out = [d for d in out if not (d['trig'] == 'ltf20' and d.get('late'))]
        C, H, L = s.C, s.H, s.L; e20 = s.e20; n = s.n
        lastp = -99; extra = []
        flip_ok = np.zeros(n, bool); fo = False
        for i in range(n):
            if s.hf[i] != 0: fo = (C[i] > s.h20[i]) if s.hf[i] == 1 else (C[i] < s.h20[i])
            flip_ok[i] = fo
        om = (s.hm - s.tf) % 1440
        orf = ((om >= 570) & (om < 570 + getattr(s, 'NYW', 30))) | ((om >= 180) & (om < 210)) | ((om >= 1200) & (om < 1230))
        for i in range(250, n - 1):
            if np.isnan(s.atr[i]) or s.hdir[i] < 0 or (16 * 60 <= s.hm[i] < 18 * 60 + 30) or orf[i] or not flip_ok[i]: continue
            lg = s.hdir[i] == 1
            pier = (L[i - 1] > e20[i - 1] and L[i] <= e20[i] <= H[i]) if lg else (H[i - 1] < e20[i - 1] and L[i] <= e20[i] <= H[i])
            if not pier: continue
            if i - lastp <= 3: continue
            lastp = i
            if (C[i] > e20[i]) if lg else (C[i] < e20[i]): continue
            for k in range(1, late + 1):
                j = i + k
                if j >= n or s.hdir[j] != s.hdir[i]: break
                if (C[j] > e20[j]) if lg else (C[j] < e20[j]):
                    extra.append(dict(i=j, lg=lg, trig='ltf20', erm=.08, late=k)); break
        for d in extra:
            i = d['i']; A = s.atr[i]; lg = d['lg']; gg = 1 if lg else -1
            hi = s.H[i - 23:i + 1].max(); lo = s.L[i - 23:i + 1].min(); pos = (C[i] - lo) / (hi - lo) if hi > lo else .5
            d['R5'] = (pos if lg else 1 - pos) >= .8 and (hi - lo) / A < 5
            d['xv'] = gg * (C[i] - s.vw[i]) / A; d['X4'] = d['xv'] > 4; d['M'] = False
            d['VB'] = s.vwb[i] == (1 if lg else -1)
            d.update(er={kk: s.er[kk][i] for kk in s.er}, bo=bool(s.bo[i]), month=s.month[i])
        out += extra
        out.sort(key=lambda d: (d['i'], d['trig'] != 'flip'))
        return out

def load(sym, tf=3, cache=None):
    if cache and os.path.exists(cache): return pd.read_pickle(cache)
    key = sym if tf == 3 else '%s_%d' % (sym, tf)
    B = pd.DataFrame(get(BASE + '/bars?sym=%s&days=400&from=%s' % (key, '2026-06-01' if tf == 2 else '2026-01-05'))['bars'])
    if 'live' in B: B = B[B['live'].isna() | (B['live'] == 0)]
    B = B.sort_values('t').drop_duplicates('t', keep='last').reset_index(drop=True)
    for c in B.columns:
        if c != 'fl': B[c] = pd.to_numeric(B[c], errors='coerce')
    for c in ('nyh','nyl','lnh','lnl','ash','asl','e200','vw','e20','h9','h20','hc','hf'):
        if c not in B: B[c] = np.nan
    et = pd.to_datetime(B.t, unit='ms', utc=True).dt.tz_convert('America/New_York')
    start = (et + pd.Timedelta(hours=6)).dt.normalize() - pd.Timedelta(hours=6)
    mins = ((et - start).dt.total_seconds() // 60).astype(int)
    B['hk'] = start.dt.strftime('%Y-%m-%d') + '_' + (mins // (5 * tf)).astype(str); B['last'] = B.groupby('hk').t.transform('max'); B['hf'] = B['hf'].fillna(0)
    if cache: B.to_pickle(cache)
    return B
