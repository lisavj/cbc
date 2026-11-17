## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09.
- MGC 3m "skip against VWAP": beyond random **+190** (thirds +64 / +47 / +79, last 4 wk +24) vs 11/08 +150 (+27 %) -> **HELD** (note: base now includes the stretch gate, 972 vs 1193 trades).
- MNQ 3m "skip against 5-day EMA + 2 losses in a row or 2 flip-outs": beyond random **+875** (thirds +195 / +358 / +322, last 4 wk +761) vs +910 -> **HELD**.
- M2K 3m "skip against 5-day EMA (shorts only)": beyond random **+140** (thirds +39 / +60 / +42, last 4 wk +22) vs +133 -> **HELD**.
- **Weeks held: MGC VWAP 2/3, MNQ guard 2/3, M2K short filter 2/3.** None ready to add to CBC yet (one more HELD week needed).
- MES 3m: best = 5-day EMA shorts-only + 2 losses / 2 flip-outs, beyond random +272 (third 3 -168, no flags); shorts-only filter alone +165 (beyond random +1 / +176 / -13). Walk-forward third 3 (beyond random) still negative on all four charts: MES -257 / MGC -106 / MNQ -278 / M2K -4.

---

# Trend filter + session guard study — 3m charts — 11/14/2026 23:37

## Summary

- MES 3m: best skip against 5-day EMA (shorts only) + 2 losses in a row or 2 flip-outs → beyond random +272 (Δ +691, no flags); walk-forward third 3 beyond random -257
- MGC 3m: best skip against VWAP + 4 flip-outs → beyond random +190 (Δ +180, TTx4); walk-forward third 3 beyond random -106
- MNQ 3m: best skip against EMA200 slope 1 h + 3 losses in a row or 3 flip-outs → beyond random +899 (Δ +1601, TTx4); walk-forward third 3 beyond random -278
- M2K 3m: best skip against 5-day EMA (shorts only) + 4 losses in a row → beyond random +147 (Δ +275, TTx4); walk-forward third 3 beyond random -4


Trend filter + session guard study -- 3m charts MES, MGC, MNQ, M2K -- 11/08/2026.
Why: the MES 3m month split (11/08) showed the losing months were June (volatile, no direction, 37 % win) and August (quiet drift up,
shorts -159), with many more setups closed by an HTF flip against them (85-95 a month vs 61-71 in good months). Chop measures
(ER, flips per day) were the same in all thirds. Two kinds of fix are tested here:
 A. TREND FILTER (entry gate, re-simulated: a skipped setup does not end the open trade) -- skip setups against:
    mtf = the 60m CBC direction; e200-20 / e200-60 = the chart EMA200 slope over 20 / 60 candles (1 h / 3 h);
    vwap = session VWAP (long only above, short only below); pdc = the previous session close; d5 = a 5-day EMA of session closes
    (up to the previous session). Applied to both directions, or to shorts only ("S").
 B. SESSION GUARD (bot rule; session = 18:00-18:00 ET): stop taking setups for the rest of the session after K losing trades in a
    row (after costs) or after N trades closed by an HTF flip against them. Only trades that have already ENDED count.
Costs (as exit_lab): commission + 1 tick per trade, +1 tick for a rule exit; MES 0.50 / MGC 0.22 / MNQ 0.87 / M2K 0.35 pts per trade.
"Beyond random" = Δ after costs minus what dropping the same number of trades at random would give (current exits lose
money after costs, so ANY skipping looks good). Walk-forward = best rule picked on thirds 1-2 (beyond-random, after costs),
scored on third 3. Replay = chop_sim rules, live exits (MES 3m SL1 3 ATR / TP1 1.75 ATR / by time of day, MGC 3m MGCX,
MNQ / M2K CBC defaults), Jan 5 -> now. T = better in all three thirds, 4 = better in the last 4 weeks.

## MES 3m — current: 1738 trades to 11/13, net -822 after costs (0.50 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 1296 | +140 | **-69**  | -3 / +43 / -109 | -53.3 |
| skip against 60m CBC (shorts only) | 1545 | +107 | **+16**  | +30 / +1 / -16 | -25.7 |
| skip against EMA200 slope 1 h | 1441 | +50 | **-90**  | -81 / +34 / -43 | -78.4 |
| skip against EMA200 slope 1 h (shorts only) | 1571 | +90 | **+11**  | -55 / +26 / +41 | -46.5 |
| skip against EMA200 slope 3 h | 1361 | +73 | **-105**  | -71 / +93 / -127 | -83.1 |
| skip against EMA200 slope 3 h (shorts only) | 1526 | +62 | **-38**  | -50 / +52 / -39 | -58.2 |
| skip against VWAP | 1548 | +46 | **-44**  | +6 / +33 / -84 | -54.6 |
| skip against VWAP (shorts only) | 1623 | +79 | **+24**  | +18 / +13 / -7 | -36.9 |
| skip against prev session close | 1356 | +243 | **+63**  | -78 / +134 / +7 | +6.4 |
| skip against prev session close (shorts only) | 1551 | +156 | **+67**  | -11 / +72 / +7 | -10.8 |
| skip against 5-day EMA | 1106 | +320 | **+22**  | -89 / +264 / -154 | -85.7 |
| skip against 5-day EMA (shorts only) | 1391 | +329 | **+165**  | +1 / +176 / -13 | -19.8 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 995 | +561 | **+210**  | +30 / +373 / -193 | -146.4 |
| 3 flip-outs | 1314 | +219 | **+18**  | -42 / +227 / -167 | -213.3 |
| 4 flip-outs | 1530 | +214 | **+115**  | -44 / +159 / +1 | -83.3 |
| 2 losses in a row | 1053 | +486 | **+162**  | -7 / +305 / -137 | -147.1 |
| 2 losses in a row or 2 flip-outs | 924 | +611 | **+226**  | +15 / +394 / -183 | -141.0 |
| 2 losses in a row or 3 flip-outs | 1034 | +443 | **+110**  | -24 / +299 / -164 | -147.1 |
| 2 losses in a row or 4 flip-outs | 1052 | +474 | **+150**  | -19 / +305 / -137 | -147.1 |
| 3 losses in a row | 1417 | +170 | **+19**  | -13 / +167 / -135 | -217.9 |
| 3 losses in a row or 2 flip-outs | 991 | +575 | **+221**  | +36 / +375 / -190 | -142.4 |
| 3 losses in a row or 3 flip-outs | 1269 | +199 | **-23**  | -58 / +224 / -188 | -234.4 |
| 3 losses in a row or 4 flip-outs | 1370 | +200 | **+26**  | -13 / +196 / -157 | -227.4 |
| 4 losses in a row | 1630 | -79 | **-130**  | -64 / +5 / -71 | -90.3 |
| 4 losses in a row or 2 flip-outs | 995 | +561 | **+210**  | +30 / +373 / -193 | -146.4 |
| 4 losses in a row or 3 flip-outs | 1303 | +233 | **+28**  | -42 / +236 / -166 | -215.9 |
| 4 losses in a row or 4 flip-outs | 1492 | +171 | **+54**  | -37 / +136 / -44 | -128.3 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against 5-day EMA (shorts only) + 2 losses in a row or 2 flip-outs: Δ **+691** after costs, beyond random **+272**, 850 trades (-888) (thirds +135 / +564 / -7; beyond random +31 / +408 / -168; last 4 wk -152.9)
2. skip against 5-day EMA (shorts only) + 3 losses in a row or 2 flip-outs: Δ **+659** after costs, beyond random **+269**, 913 trades (-825) (thirds +158 / +526 / -25; beyond random +65 / +381 / -177; last 4 wk -154.9)
3. skip against 5-day EMA (shorts only) + 2 flip-outs: Δ **+641** after costs, beyond random **+255**, 920 trades (-818) (thirds +151 / +522 / -32; beyond random +59 / +379 / -184; last 4 wk -158.9)
4. skip against 5-day EMA (shorts only) + 4 losses in a row or 2 flip-outs: Δ **+641** after costs, beyond random **+255**, 920 trades (-818) (thirds +151 / +522 / -32; beyond random +59 / +379 / -184; last 4 wk -158.9)
5. skip against prev session close + 3 losses in a row or 2 flip-outs: Δ **+649** after costs, beyond random **+254**, 902 trades (-836) (thirds +121 / +564 / -36; beyond random +20 / +421 / -187; last 4 wk -118.4)
6. skip against prev session close + 4 losses in a row or 2 flip-outs: Δ **+643** after costs, beyond random **+253**, 912 trades (-826) (thirds +121 / +562 / -40; beyond random +20 / +421 / -188; last 4 wk -108.7)
7. skip against prev session close + 2 flip-outs: Δ **+640** after costs, beyond random **+250**, 913 trades (-825) (thirds +121 / +562 / -43; beyond random +20 / +421 / -190; last 4 wk -108.7)
8. skip against prev session close + 2 losses in a row or 2 flip-outs: Δ **+671** after costs, beyond random **+248**, 845 trades (-893) (thirds +120 / +573 / -22; beyond random +10 / +421 / -183; last 4 wk -108.6)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against VWAP + 3 losses in a row or 2 flip-outs** (+457 in-sample) → third 3 beyond random **-257** (rank 192 of 207, median -172)
- by plain Δ after costs: **skip against 5-day EMA (shorts only) + 2 losses in a row or 2 flip-outs** (+698 in-sample) → third 3 Δ **-7** (rank 53 of 207, median -48)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -108 | +89 | -24 | -41 | -180 | -412 | -76 | -262 | +27 | +72 | +94 |
| skip against 5-day EMA (shorts only) + 2 losses in a row or 2 flip-outs | -49 | +10 | +113 | +48 | -7 | -174 | +4 | -22 | -25 | -6 | -22 |
| skip against 5-day EMA (shorts only) + 3 losses in a row or 2 flip-outs | -83 | +60 | +114 | +55 | -27 | -210 | +22 | -30 | -23 | -23 | -17 |
| skip against 5-day EMA (shorts only) + 2 flip-outs | -83 | +60 | +107 | +55 | -29 | -212 | +22 | -34 | -23 | -27 | -17 |

## MGC 3m — current: 1193 trades to 11/13, net +55 after costs (0.22 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 825 | +12 | **+29**  | +48 / -17 / -1 | +7.9 |
| skip against 60m CBC (shorts only) | 1024 | -5 | **+3**  | +45 / -62 / +20 | -14.8 |
| skip against EMA200 slope 1 h | 873 | +80 | **+95** T | +37 / +28 / +31 | +39.4 |
| skip against EMA200 slope 1 h (shorts only) | 1038 | +66 | **+73**  | +19 / -11 / +65 | +21.4 |
| skip against EMA200 slope 3 h | 801 | +116 | **+134**  | -37 / +124 / +47 | +37.7 |
| skip against EMA200 slope 3 h (shorts only) | 1004 | +103 | **+112**  | -2 / +55 / +58 | +16.1 |
| skip against VWAP | 972 | +179 | **+190** T | +64 / +47 / +79 | +23.9 |
| skip against VWAP (shorts only) | 1079 | +71 | **+76**  | +41 / -14 / +49 | +7.2 |
| skip against prev session close | 818 | +87 | **+105** T | +27 / +55 / +23 | -27.2 |
| skip against prev session close (shorts only) | 991 | +1 | **+10**  | +30 / -21 / +1 | -37.3 |
| skip against 5-day EMA | 675 | +2 | **+26**  | +1 / +119 / -95 | -34.2 |
| skip against 5-day EMA (shorts only) | 933 | +23 | **+35**  | +22 / +40 / -27 | -43.5 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 1059 | +73 | **+80**  | +80 / +43 / -43 | -40.2 |
| 3 flip-outs | 1164 | -24 | **-22**  | -4 / -20 / +1 | +5.1 |
| 4 flip-outs | 1181 | -3 | **-3**  | -5 / -3 / +5 | +11.4 |
| 2 losses in a row | 799 | -59 | **-41**  | +35 / -79 / +3 | -24.4 |
| 2 losses in a row or 2 flip-outs | 769 | -55 | **-36**  | +37 / -69 / -4 | -42.7 |
| 2 losses in a row or 3 flip-outs | 799 | -59 | **-41**  | +35 / -79 / +3 | -24.4 |
| 2 losses in a row or 4 flip-outs | 799 | -59 | **-41**  | +35 / -79 / +3 | -24.4 |
| 3 losses in a row | 1045 | +35 | **+42**  | +75 / +22 / -55 | -26.3 |
| 3 losses in a row or 2 flip-outs | 985 | +55 | **+65**  | +85 / +41 / -61 | -44.6 |
| 3 losses in a row or 3 flip-outs | 1041 | +31 | **+38**  | +75 / +15 / -51 | -26.3 |
| 3 losses in a row or 4 flip-outs | 1045 | +35 | **+42**  | +75 / +22 / -55 | -26.3 |
| 4 losses in a row | 1135 | +30 | **+32**  | +38 / -4 / -2 | +5.2 |
| 4 losses in a row or 2 flip-outs | 1041 | +57 | **+64**  | +80 / +32 / -48 | -40.2 |
| 4 losses in a row or 3 flip-outs | 1123 | +16 | **+19**  | +38 / -14 / -4 | +5.1 |
| 4 losses in a row or 4 flip-outs | 1131 | +30 | **+32**  | +38 / -4 / -2 | +11.4 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against VWAP + 4 flip-outs: Δ **+180** after costs, beyond random **+190**, 967 trades (-226) TTx4 (thirds +63 / +41 / +76; beyond random +67 / +44 / +79; last 4 wk +23.9)
2. skip against VWAP + no guard: Δ **+179** after costs, beyond random **+190**, 972 trades (-221) TTx4 (thirds +60 / +43 / +76; beyond random +64 / +47 / +79; last 4 wk +23.9)
3. skip against VWAP + 2 flip-outs: Δ **+172** after costs, beyond random **+185**, 907 trades (-286) TTx4 (thirds +64 / +49 / +59; beyond random +69 / +54 / +62; last 4 wk +4.9)
4. skip against VWAP + 3 flip-outs: Δ **+170** after costs, beyond random **+181**, 958 trades (-235) TTx4 (thirds +64 / +34 / +71; beyond random +68 / +38 / +75; last 4 wk +23.9)
5. skip against VWAP + 3 losses in a row or 2 flip-outs: Δ **+161** after costs, beyond random **+177**, 851 trades (-342) TTx4 (thirds +74 / +43 / +44; beyond random +80 / +48 / +49; last 4 wk +0.5)
6. skip against VWAP + 3 losses in a row: Δ **+157** after costs, beyond random **+171**, 886 trades (-307) TTx4 (thirds +72 / +49 / +35; beyond random +78 / +53 / +39; last 4 wk +0.5)
7. skip against VWAP + 3 losses in a row or 4 flip-outs: Δ **+157** after costs, beyond random **+171**, 886 trades (-307) TTx4 (thirds +72 / +49 / +35; beyond random +78 / +53 / +39; last 4 wk +0.5)
8. skip against VWAP + 4 losses in a row: Δ **+156** after costs, beyond random **+167**, 947 trades (-246) TTx4 (thirds +25 / +55 / +76; beyond random +29 / +59 / +79; last 4 wk +23.9)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against 5-day EMA + 2 flip-outs** (+169 in-sample) → third 3 beyond random **-106** (rank 202 of 207, median -0)
- by plain Δ after costs: **skip against 5-day EMA + 2 flip-outs** (+152 in-sample) → third 3 Δ **-114** (rank 202 of 207, median -6)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -88 | +104 | +52 | -40 | -95 | +48 | +2 | -30 | +5 | +9 | +89 |
| skip against VWAP + 4 flip-outs | -80 | +92 | +54 | +38 | -55 | +27 | +9 | -29 | +42 | +35 | +101 |
| skip against VWAP + no guard | -77 | +92 | +54 | +32 | -52 | +27 | +9 | -29 | +42 | +35 | +101 |
| skip against VWAP + 2 flip-outs | -65 | +84 | +54 | +32 | -43 | +36 | -2 | -22 | +37 | +16 | +101 |

## MNQ 3m — current: 1969 trades to 11/13, net -2075 after costs (0.87 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 1501 | +583 | **+90**  | +314 / +255 / -479 | +241.0 |
| skip against 60m CBC (shorts only) | 1725 | -104 | **-361**  | +365 / -158 / -568 | +9.7 |
| skip against EMA200 slope 1 h | 1645 | -131 | **-472**  | -244 / -120 / -108 | +225.1 |
| skip against EMA200 slope 1 h (shorts only) | 1804 | -414 | **-588**  | -160 / -228 / -199 | +104.6 |
| skip against EMA200 slope 3 h | 1573 | -389 | **-806**  | -188 / -379 / -239 | +121.6 |
| skip against EMA200 slope 3 h (shorts only) | 1779 | -806 | **-1006**  | -315 / -373 / -318 | -43.4 |
| skip against VWAP | 1786 | -359 | **-552**  | -18 / -73 / -461 | +53.3 |
| skip against VWAP (shorts only) | 1865 | -91 | **-200**  | +153 / -86 / -267 | +46.7 |
| skip against prev session close | 1536 | -555 | **-1012**  | -626 / -208 / -178 | +290.4 |
| skip against prev session close (shorts only) | 1753 | -405 | **-633**  | -237 / +162 / -558 | +68.9 |
| skip against 5-day EMA | 1269 | +433 | **-305**  | -93 / +183 / -395 | +498.2 |
| skip against 5-day EMA (shorts only) | 1596 | -134 | **-527**  | +141 / +29 / -697 | +253.3 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 1553 | +228 | **-210**  | -143 / +180 / -247 | +111.2 |
| 3 flip-outs | 1846 | -73 | **-202**  | -201 / +88 / -89 | +14.7 |
| 4 flip-outs | 1947 | -28 | **-51**  | -114 / +28 / +35 | +0.0 |
| 2 losses in a row | 989 | +1240 | **+207**  | +92 / -306 / +420 | +569.5 |
| 2 losses in a row or 2 flip-outs | 929 | +943 | **-153**  | -72 / -229 / +147 | +569.5 |
| 2 losses in a row or 3 flip-outs | 988 | +1265 | **+231**  | +117 / -306 / +420 | +569.5 |
| 2 losses in a row or 4 flip-outs | 989 | +1240 | **+207**  | +92 / -306 / +420 | +569.5 |
| 3 losses in a row | 1452 | +1048 | **+503**  | -125 / +152 / +475 | +395.2 |
| 3 losses in a row or 2 flip-outs | 1262 | +1189 | **+443**  | -211 / +412 / +243 | +480.9 |
| 3 losses in a row or 3 flip-outs | 1412 | +1129 | **+541**  | -120 / +187 / +474 | +409.9 |
| 3 losses in a row or 4 flip-outs | 1445 | +1137 | **+584**  | -125 / +184 / +525 | +395.2 |
| 4 losses in a row | 1732 | +440 | **+191**  | -262 / +228 / +224 | +174.9 |
| 4 losses in a row or 2 flip-outs | 1435 | +790 | **+227**  | -132 / +396 / -37 | +286.1 |
| 4 losses in a row or 3 flip-outs | 1662 | +714 | **+391**  | -121 / +289 / +223 | +189.7 |
| 4 losses in a row or 4 flip-outs | 1724 | +527 | **+269**  | -262 / +256 / +274 | +174.9 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against EMA200 slope 1 h + 3 losses in a row or 3 flip-outs: Δ **+1601** after costs, beyond random **+899**, 1303 trades (-666) TTx4 (thirds +494 / +401 / +705; beyond random +283 / +167 / +449; last 4 wk +505.7)
2. skip against 5-day EMA + 2 losses in a row or 2 flip-outs: Δ **+2066** after costs, beyond random **+875**, 839 trades (-1130) TTx4 (thirds +542 / +745 / +779; beyond random +195 / +358 / +322; last 4 wk +760.8)
3. skip against VWAP (shorts only) + 3 losses in a row or 2 flip-outs: Δ **+1554** after costs, beyond random **+808**, 1261 trades (-708) TTx4 (thirds +281 / +637 / +636; beyond random +50 / +406 / +352; last 4 wk +523.6)
4. skip against EMA200 slope 1 h + 3 losses in a row: Δ **+1482** after costs, beyond random **+803**, 1325 trades (-644) TTx4 (thirds +516 / +344 / +622; beyond random +307 / +125 / +371; last 4 wk +490.9)
5. skip against EMA200 slope 1 h + 3 losses in a row or 4 flip-outs: Δ **+1480** after costs, beyond random **+799**, 1323 trades (-646) TTx4 (thirds +516 / +342 / +622; beyond random +307 / +121 / +371; last 4 wk +490.9)
6. skip against 5-day EMA + 2 losses in a row: Δ **+1951** after costs, beyond random **+780**, 858 trades (-1111) TTx4 (thirds +441 / +612 / +898; beyond random +103 / +230 / +447; last 4 wk +760.8)
7. skip against 5-day EMA + 2 losses in a row or 3 flip-outs: Δ **+1951** after costs, beyond random **+780**, 858 trades (-1111) TTx4 (thirds +441 / +612 / +898; beyond random +103 / +230 / +447; last 4 wk +760.8)
8. skip against 5-day EMA + 2 losses in a row or 4 flip-outs: Δ **+1951** after costs, beyond random **+780**, 858 trades (-1111) TTx4 (thirds +441 / +612 / +898; beyond random +103 / +230 / +447; last 4 wk +760.8)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against 60m CBC + 4 losses in a row or 2 flip-outs** (+817 in-sample) → third 3 beyond random **-278** (rank 162 of 207, median -37)
- by plain Δ after costs: **skip against 60m CBC + 4 losses in a row or 2 flip-outs** (+1310 in-sample) → third 3 Δ **+20** (rank 144 of 207, median +255)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -493 | +181 | +140 | -275 | +156 | -813 | +84 | -310 | -1 | -55 | -689 |
| skip against EMA200 slope 1 h + 3 losses in a row or 3 flip-outs | -420 | +314 | +379 | -95 | +373 | -592 | -84 | +14 | -68 | +3 | -300 |
| skip against 5-day EMA + 2 losses in a row or 2 flip-outs | -175 | -63 | +333 | +190 | +337 | -358 | +2 | -148 | +67 | +79 | -275 |
| skip against VWAP (shorts only) + 3 losses in a row or 2 flip-outs | -265 | +21 | +244 | -40 | +483 | -574 | +29 | -205 | +75 | +66 | -356 |

## M2K 3m — current: 1970 trades to 11/13, net -598 after costs (0.35 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 1450 | +113 | **-44**  | +4 / +23 / -71 | +0.2 |
| skip against 60m CBC (shorts only) | 1718 | +55 | **-21**  | +26 / +9 / -56 | -4.0 |
| skip against EMA200 slope 1 h | 1591 | +62 | **-53**  | -2 / -28 / -23 | -5.5 |
| skip against EMA200 slope 1 h (shorts only) | 1764 | +27 | **-36**  | -3 / -23 / -10 | -1.4 |
| skip against EMA200 slope 3 h | 1528 | +104 | **-30**  | -4 / +10 / -36 | +6.3 |
| skip against EMA200 slope 3 h (shorts only) | 1726 | +63 | **-11**  | -20 / +11 / -2 | +9.9 |
| skip against VWAP | 1778 | +65 | **+7**  | -0 / +33 / -26 | -9.1 |
| skip against VWAP (shorts only) | 1857 | +36 | **+1**  | +0 / +6 / -5 | +5.1 |
| skip against prev session close | 1555 | +84 | **-42**  | -7 / -13 / -22 | +13.2 |
| skip against prev session close (shorts only) | 1747 | +88 | **+20** T | +11 / +7 / +2 | +14.9 |
| skip against 5-day EMA | 1275 | +314 | **+103** T | +20 / +32 / +51 | +42.5 |
| skip against 5-day EMA (shorts only) | 1615 | +248 | **+140** T | +39 / +60 / +42 | +21.5 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 1318 | +149 | **-48**  | -1 / +19 / -66 | +10.2 |
| 3 flip-outs | 1729 | +63 | **-11**  | -17 / +38 / -32 | +10.8 |
| 4 flip-outs | 1874 | +74 | **+45** T | +18 / +16 / +11 | +14.0 |
| 2 losses in a row | 1073 | +215 | **-57**  | -21 / +15 / -50 | +31.3 |
| 2 losses in a row or 2 flip-outs | 961 | +244 | **-62**  | -39 / +46 / -69 | +31.3 |
| 2 losses in a row or 3 flip-outs | 1048 | +205 | **-75**  | -38 / +25 / -63 | +31.3 |
| 2 losses in a row or 4 flip-outs | 1069 | +221 | **-52**  | -24 / +22 / -50 | +31.3 |
| 3 losses in a row | 1633 | +119 | **+17**  | -6 / +43 / -20 | +15.5 |
| 3 losses in a row or 2 flip-outs | 1202 | +203 | **-30**  | -22 / +51 / -59 | +12.8 |
| 3 losses in a row or 3 flip-outs | 1521 | +122 | **-14**  | -27 / +59 / -46 | +22.0 |
| 3 losses in a row or 4 flip-outs | 1601 | +124 | **+12**  | -20 / +49 / -17 | +20.9 |
| 4 losses in a row | 1843 | +98 | **+59**  | +27 / +38 / -5 | +5.5 |
| 4 losses in a row or 2 flip-outs | 1295 | +177 | **-28**  | +2 / +38 / -68 | +11.4 |
| 4 losses in a row or 3 flip-outs | 1664 | +111 | **+18**  | +1 / +50 / -33 | +17.3 |
| 4 losses in a row or 4 flip-outs | 1778 | +130 | **+72** T | +27 / +40 / +5 | +16.2 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against 5-day EMA (shorts only) + 4 losses in a row: Δ **+275** after costs, beyond random **+147**, 1547 trades (-423) TTx4 (thirds +101 / +109 / +65; beyond random +62 / +56 / +30; last 4 wk +26.1)
2. skip against 5-day EMA (shorts only) + 4 flip-outs: Δ **+263** after costs, beyond random **+143**, 1576 trades (-394) TTx4 (thirds +85 / +108 / +70; beyond random +48 / +60 / +34; last 4 wk +21.5)
3. skip against 5-day EMA (shorts only) + 4 losses in a row or 4 flip-outs: Δ **+278** after costs, beyond random **+141**, 1517 trades (-453) TTx4 (thirds +108 / +105 / +65; beyond random +65 / +51 / +24; last 4 wk +26.1)
4. skip against 5-day EMA (shorts only) + no guard: Δ **+248** after costs, beyond random **+140**, 1615 trades (-355) TTx4 (thirds +71 / +106 / +71; beyond random +39 / +60 / +42; last 4 wk +21.5)
5. skip against 5-day EMA + 3 losses in a row: Δ **+383** after costs, beyond random **+136**, 1153 trades (-817) TTx4 (thirds +125 / +130 / +129; beyond random +45 / +43 / +48; last 4 wk +50.6)
6. skip against 5-day EMA + 3 losses in a row or 3 flip-outs: Δ **+386** after costs, beyond random **+134**, 1138 trades (-832) TTx4 (thirds +126 / +133 / +127; beyond random +44 / +46 / +43; last 4 wk +50.6)
7. skip against 5-day EMA + 3 losses in a row or 4 flip-outs: Δ **+375** after costs, beyond random **+126**, 1151 trades (-819) TTx4 (thirds +125 / +130 / +120; beyond random +45 / +43 / +39; last 4 wk +50.6)
8. skip against 5-day EMA (shorts only) + 4 losses in a row or 3 flip-outs: Δ **+281** after costs, beyond random **+121**, 1444 trades (-526) T4 (thirds +119 / +113 / +49; beyond random +72 / +54 / -4; last 4 wk +26.1)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against 5-day EMA (shorts only) + 4 losses in a row or 3 flip-outs** (+126 in-sample) → third 3 beyond random **-4** (rank 30 of 207, median -44)
- by plain Δ after costs: **skip against 5-day EMA + 2 losses in a row or 2 flip-outs** (+303 in-sample) → third 3 Δ **+102** (rank 14 of 207, median +27)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -28 | -79 | -4 | -114 | -62 | -42 | -98 | -35 | -53 | -43 | -38 |
| skip against 5-day EMA (shorts only) + 4 losses in a row | -2 | -28 | +1 | -52 | -26 | -12 | -99 | -6 | -49 | -17 | -32 |
| skip against 5-day EMA (shorts only) + 4 flip-outs | -4 | -53 | -1 | -40 | -24 | -12 | -102 | -18 | -36 | -9 | -37 |
| skip against 5-day EMA (shorts only) + 4 losses in a row or 4 flip-outs | -7 | -29 | +1 | -40 | -26 | -12 | -103 | -18 | -46 | -9 | -32 |

