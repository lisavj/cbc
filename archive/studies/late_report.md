# LTF EMA20 Pierce late-confirm window — Thu 11/05/2026 08:01

LTF EMA20 Pierce late-confirm window study -- 11/05/2026.
Question: CBC "LTF pierce late-confirm window (bars)" = 1 (one setting for every chart). If the pierce candle does not close back
beyond the slow chart EMA, the next N candles may (first close back beyond the line, HTF direction unchanged). Best N per chart?
Engine: mes3_ema_grid MCase (chop_sim rules), LTF late window = N (0 = pierce candle only). Charts on live settings:
MES 3m slow 14 and slow 20 (live exits SL 3 / TP1 2.0 / time-of-day close), MGC 3m slow 20 (range gate + VWAP stretch 4 ATR,
base exits). Jan 5 -> now. z / robust / promising as in the other studies (thirds = equal time).
Usage: python3 late_study.py   (needs chop_sim.py + mes3_ema_grid.py next to it)

## MES 3m slow 14 (live 7/14) — 99825 candles

| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1762 | 47% | +56 | +0.03 | -55 | -0.5 | -28 / +38 / -64 | worse | 992 / +120 (late 0 / +0) | -10.5 |
| 1 (current) | 1875 | 47% | +110 | +0.06 | +0 | +0.0 | +0 / +0 / +0 | baseline | 1128 / +162 (late 163 / +35) | +0.0 |
| 2 | 1927 | 47% | -5 | -0.00 | -115 | -1.5 | -3 / -65 / -48 | worse | 1192 / +45 (late 232 / -53) | -5.8 |
| 3 | 1936 | 47% | +23 | +0.01 | -87 | -1.0 | +44 / -77 / -54 | worse | 1208 / +114 (late 250 / +14) | -5.8 |
| 4 | 1944 | 47% | -18 | -0.01 | -128 | -1.3 | +50 / -115 / -63 | worse | 1219 / +70 (late 264 / -13) | -0.4 |
| 5 | 1952 | 47% | -17 | -0.01 | -127 | -1.3 | +52 / -118 / -61 | worse | 1228 / +90 (late 273 / +8) | -0.4 |

## MES 3m slow 20 (9/20) — 99825 candles

| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1567 | 46% | -85 | -0.05 | +21 | +0.2 | +9 / +36 / -24 | noise | 776 / +81 (late 0 / +0) | -9.0 |
| 1 (current) | 1660 | 46% | -106 | -0.06 | +0 | +0.0 | +0 / +0 / +0 | baseline | 895 / +58 (late 133 / -1) | +0.0 |
| 2 | 1704 | 46% | -98 | -0.06 | +8 | +0.1 | +31 / -35 / +11 | noise | 952 / +77 (late 195 / -14) | -4.0 |
| 3 | 1711 | 46% | -107 | -0.06 | -1 | -0.0 | +44 / -30 / -15 | worse | 962 / +73 (late 206 / -14) | -4.0 |
| 4 | 1719 | 46% | -157 | -0.09 | -51 | -0.7 | +28 / -59 / -20 | worse | 970 / +23 (late 216 / -69) | -4.0 |
| 5 | 1725 | 46% | -154 | -0.09 | -48 | -0.6 | +27 / -58 / -16 | worse | 976 / +26 (late 223 / -63) | -0.6 |

## MGC 3m slow 20 — 99605 candles

| Window | Setups | Win % | Net | Avg | Δ vs 1 (current) | z | Δ by third | Verdict | LTF20 setups / net (late ones) | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1649 | 50% | +214 | +0.13 | -5 | -0.1 | +5 / +13 / -22 | worse | 755 / +36 (late 0 / +0) | -1.5 |
| 1 (current) | 1691 | 50% | +218 | +0.13 | +0 | +0.0 | +0 / +0 / +0 | baseline | 806 / +34 (late 56 / -7) | +0.0 |
| 2 | 1717 | 50% | +268 | +0.16 | +50 | +1.2 | +34 / +14 / +2 | promising | 836 / +66 (late 94 / +7) | -2.9 |
| 3 | 1728 | 50% | +297 | +0.17 | +78 | +1.7 | +36 / +37 / +5 | promising | 848 / +89 (late 108 / +23) | -5.1 |
| 4 | 1735 | 50% | +270 | +0.16 | +51 | +1.0 | +22 / +31 / -1 | noise | 857 / +75 (late 118 / +16) | -5.9 |
| 5 | 1740 | 50% | +269 | +0.15 | +50 | +0.9 | +22 / +32 / -3 | noise | 863 / +71 (late 124 / +12) | -12.9 |

## Candidates (robust / promising)

- MGC 3m slow 20: window 2 → +50, z +1.2, thirds +34 / +14 / +2 (promising)
- MGC 3m slow 20: window 3 → +78, z +1.7, thirds +36 / +37 / +5 (promising)
