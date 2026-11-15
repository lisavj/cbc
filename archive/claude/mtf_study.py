# MES / MGC 3m: MTF (60m) EMA20 slope in combination with the HTF (15m) EMA20 slope filter -- 11/15/2026
import sys
exec(open('mtf_eng.py').read())
log = lambda m: print(m, file=sys.stderr, flush=True)
sym = sys.argv[1]; setup(sym)
if sym == 'MES': CFGX['base'] = dict(CFGX['base'], P=dict(qwin=(960, 1140), eod=False))   # v1.14 MES 3m time rules
T_ = B.t.values.astype(np.int64); Cl = B.c.values.astype(float); hr = T_ // 3600000
# 60m closes: last 3m close in each clock hour; EMA20 over completed hours; bar i sees the last COMPLETED hour (no lookahead)
dfh = pd.DataFrame(dict(h=hr, c=Cl)).groupby('h').c.last(); m20h = dfh.ewm(span=20, adjust=False).mean()
prev = pd.Series(m20h.values, index=m20h.index + 1)          # value usable from the next hour on
M20 = prev.reindex(hr).values
def mdiff(k):   # m20 (last completed hour) minus k hours earlier
    p = pd.Series(m20h.values, index=m20h.index + 1 + k); return M20 - p.reindex(hr).values
MD = {k: mdiff(k) for k in (1, 2, 3)}
HD = h20raw - np.roll(h20raw, 12)
b = run({}); base_sl = CFGX['base']['slope']
A0 = case(dict(TDEF, fdp=CFGX['fdp'], tw=CFGX['tw'], erl=CFGX['base'].get('erl', .08), **CFGX['base'].get('P', {}))).atr
def q(k, p): x = np.abs(MD[k]) / A0; return float(np.nanpercentile(x[300:], p))
rows = []
def add(nm, f): a = run(dict(cmb=f)); rows.append((nm, a)); log(nm)
nb = lambda i, A, SLP: SLP[i] >= base_sl
for k in (1, 2):
    for p in (20, 35, 50):
        t = q(k, p); add('MTF slope only, %dh, >= %.2f ATR (p%d)' % (k, t, p), lambda i, g, SLP, A, k=k, t=t: abs(MD[k][i]) / A[i] >= t)
for k in (1, 2):
    for p in (15, 25, 35, 50):
        t = q(k, p); add('HTF base AND MTF %dh >= %.2f (p%d)' % (k, t, p), lambda i, g, SLP, A, k=k, t=t: SLP[i] >= base_sl and abs(MD[k][i]) / A[i] >= t)
for k in (1, 2):
    for p in (60, 75, 90):
        t = q(k, p); add('HTF base OR MTF %dh >= %.2f (p%d) [MTF rescues]' % (k, t, p), lambda i, g, SLP, A, k=k, t=t: SLP[i] >= base_sl or abs(MD[k][i]) / A[i] >= t)
for k in (1, 2, 3):
    add('HTF base + MTF %dh EMA20 rising for long / falling for short' % k, lambda i, g, SLP, A, k=k: SLP[i] >= base_sl and g * MD[k][i] > 0)
    add('HTF base + MTF %dh EMA20 NOT against the trade (> -0.25 ATR)' % k, lambda i, g, SLP, A, k=k: SLP[i] >= base_sl and g * MD[k][i] / A[i] > -.25)
add('HTF base + HTF EMA20 sloping with the trade', lambda i, g, SLP, A: SLP[i] >= base_sl and g * HD[i] > 0)
add('HTF base + HTF and MTF 1h both with the trade', lambda i, g, SLP, A: SLP[i] >= base_sl and g * HD[i] > 0 and g * MD[1][i] > 0)
add('HTF base + price on the trade side of MTF EMA20', lambda i, g, SLP, A: SLP[i] >= base_sl and g * (Cl[i] - M20[i]) > 0)
for k in (1, 2):
    sc = np.nanmedian(np.abs(HD[300:]) / A0[300:]) / np.nanmedian(np.abs(MD[k][300:]) / A0[300:])
    for f in (.8, 1.0, 1.2):
        add('Average of HTF and MTF %dh slope (MTF scaled to HTF) >= %.2f' % (k, f * base_sl), lambda i, g, SLP, A, k=k, sc=sc, f=f: (SLP[i] + sc * abs(MD[k][i]) / A[i]) / 2 >= f * base_sl)
    for f in (.8, 1.2):
        add('HTF >= %.2f AND MTF %dh scaled >= %.2f (both lower)' % (f * base_sl, k, f * base_sl) if f < 1 else 'HTF >= %.2f OR MTF %dh scaled >= %.2f' % (f * base_sl, k, f * base_sl),
            (lambda i, g, SLP, A, k=k, sc=sc, f=f: SLP[i] >= f * base_sl and sc * abs(MD[k][i]) / A[i] >= f * base_sl) if f < 1 else (lambda i, g, SLP, A, k=k, sc=sc, f=f: SLP[i] >= f * base_sl or sc * abs(MD[k][i]) / A[i] >= f * base_sl))
out = table('%s 3m: MTF (60m) EMA20 slope combined with the HTF (15m) EMA20 slope %.2f (v1.14 settings)' % (sym, base_sl), b, rows)
open('mtf_%s.md' % sym.lower(), 'w').write('\n'.join(out)); print('\n'.join(out))
