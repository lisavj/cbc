## Week of 11/09/2026 summary

- STUDY SETTINGS STALE: the 11/08 settings sync report lists 1 non-known MISMATCH (chop_sim GATE MGC 2m range gate R5=0) + late_study MES 3m tp=2.0 -- both already fixed in the project scripts used for this run, and neither affects these 3m studies.
- MGC 3m 'skip against VWAP': beyond random **+151** (thirds +54 / +34 / +63, last 4 wk +19.5) vs 11/08 +150 -> **HELD**.
- MNQ 3m 'skip against 5-day EMA + 2 losses in a row or 2 flip-outs': beyond random **+840** (thirds +266 / +408 / +166, last 4 wk +439) vs +910 -> **HELD** (total -8 %; third 3 down from +300 to +166 -- watch).
- M2K 3m 'skip against 5-day EMA (shorts only)': beyond random **+132** (thirds +38 / +54 / +40) vs +133 -> **HELD**.
- **Weeks held: MGC VWAP 1/3, MNQ guard 1/3, M2K short filter 1/3.** None ready to add to CBC yet.
- MES 3m: best = 5-day EMA shorts-only + 2 losses / 2 flip-outs, beyond random +333 (T); shorts-only filter alone +169 (beyond random thirds -1 / +141 / +29). Walk-forward third 3 (beyond random) still negative on all four charts: MES -208 / MGC -105 / MNQ -444 / M2K -14.

---

# Trend filter + session guard study — 3m charts — 11/09/2026 13:58

## Summary

- MES 3m: best skip against 5-day EMA (shorts only) + 2 losses in a row or 2 flip-outs → beyond random +333 (Δ +764, T); walk-forward third 3 beyond random -208
- MGC 3m: best skip against VWAP + 4 flip-outs → beyond random +167 (Δ +184, TTx4); walk-forward third 3 beyond random -105
- MNQ 3m: best skip against 5-day EMA + 2 losses in a row or 2 flip-outs → beyond random +840 (Δ +1769, TTx4); walk-forward third 3 beyond random -444
- M2K 3m: best skip against 5-day EMA (shorts only) + 4 losses in a row → beyond random +140 (Δ +269, TTx4); walk-forward third 3 beyond random -14


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

## MES 3m — current: 1705 trades to 11/09, net -847 after costs (0.50 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 1272 | +157 | **-58**  | -6 / +43 / -95 | -50.4 |
| skip against 60m CBC (shorts only) | 1516 | +103 | **+9**  | +29 / -18 / -1 | -24.7 |
| skip against EMA200 slope 1 h | 1415 | +69 | **-75**  | -84 / +39 / -30 | -67.6 |
| skip against EMA200 slope 1 h (shorts only) | 1542 | +100 | **+19**  | -56 / +22 / +53 | -27.4 |
| skip against EMA200 slope 3 h | 1337 | +96 | **-87**  | -74 / +97 / -110 | -68.2 |
| skip against EMA200 slope 3 h (shorts only) | 1499 | +76 | **-27**  | -52 / +47 / -22 | -34.3 |
| skip against VWAP | 1519 | +66 | **-26**  | +5 / +39 / -70 | -37.7 |
| skip against VWAP (shorts only) | 1593 | +89 | **+34** T | +17 / +9 / +7 | -15.5 |
| skip against prev session close | 1330 | +261 | **+75**  | -81 / +118 / +37 | +12.6 |
| skip against prev session close (shorts only) | 1521 | +159 | **+68**  | -12 / +57 / +22 | +3.0 |
| skip against 5-day EMA | 1085 | +363 | **+55**  | -93 / +254 / -106 | -50.5 |
| skip against 5-day EMA (shorts only) | 1368 | +337 | **+169**  | -1 / +141 / +29 | -2.5 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 979 | +634 | **+274**  | +26 / +391 / -143 | -111.2 |
| 3 flip-outs | 1293 | +294 | **+89**  | -44 / +223 / -89 | -163.6 |
| 4 flip-outs | 1505 | +268 | **+169**  | -45 / +157 / +57 | -29.0 |
| 2 losses in a row | 1040 | +560 | **+230**  | -10 / +313 / -73 | -86.0 |
| 2 losses in a row or 2 flip-outs | 911 | +685 | **+291**  | +11 / +401 / -120 | -104.5 |
| 2 losses in a row or 3 flip-outs | 1021 | +517 | **+177**  | -28 / +306 / -101 | -98.3 |
| 2 losses in a row or 4 flip-outs | 1039 | +549 | **+218**  | -22 / +313 / -73 | -86.0 |
| 3 losses in a row | 1399 | +268 | **+116**  | -14 / +162 / -32 | -120.3 |
| 3 losses in a row or 2 flip-outs | 975 | +648 | **+285**  | +32 / +391 / -138 | -107.2 |
| 3 losses in a row or 3 flip-outs | 1251 | +297 | **+71**  | -60 / +218 / -86 | -162.2 |
| 3 losses in a row or 4 flip-outs | 1352 | +297 | **+122**  | -15 / +192 / -55 | -129.8 |
| 4 losses in a row | 1604 | -33 | **-84**  | -64 / +4 / -23 | -45.0 |
| 4 losses in a row or 2 flip-outs | 979 | +634 | **+274**  | +26 / +391 / -143 | -111.2 |
| 4 losses in a row or 3 flip-outs | 1282 | +308 | **+98**  | -44 / +232 / -89 | -166.2 |
| 4 losses in a row or 4 flip-outs | 1467 | +225 | **+107**  | -38 / +134 / +11 | -74.0 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against 5-day EMA (shorts only) + 2 losses in a row or 2 flip-outs: Δ **+764** after costs, beyond random **+333**, 838 trades (-867) T (thirds +135 / +572 / +57; beyond random +26 / +414 / -107; last 4 wk -117.9)
2. skip against prev session close + 2 losses in a row or 2 flip-outs: Δ **+766** after costs, beyond random **+333**, 833 trades (-872) T (thirds +120 / +556 / +89; beyond random +5 / +399 / -71; last 4 wk -50.4)
3. skip against 5-day EMA (shorts only) + 3 losses in a row or 2 flip-outs: Δ **+730** after costs, beyond random **+329**, 898 trades (-807) T (thirds +158 / +517 / +55; beyond random +61 / +367 / -98; last 4 wk -121.1)
4. skip against prev session close + 3 losses in a row or 2 flip-outs: Δ **+735** after costs, beyond random **+329**, 886 trades (-819) T (thirds +121 / +548 / +65; beyond random +15 / +401 / -87; last 4 wk -68.6)
5. skip against prev session close + 4 losses in a row or 2 flip-outs: Δ **+730** after costs, beyond random **+328**, 896 trades (-809) T (thirds +121 / +546 / +62; beyond random +15 / +400 / -87; last 4 wk -58.9)
6. skip against prev session close + 2 flip-outs: Δ **+727** after costs, beyond random **+325**, 897 trades (-808) T (thirds +121 / +546 / +59; beyond random +15 / +400 / -90; last 4 wk -58.9)
7. skip against 5-day EMA (shorts only) + 2 flip-outs: Δ **+712** after costs, beyond random **+315**, 905 trades (-800) T (thirds +151 / +513 / +48; beyond random +54 / +365 / -104; last 4 wk -125.1)
8. skip against 5-day EMA (shorts only) + 4 losses in a row or 2 flip-outs: Δ **+712** after costs, beyond random **+315**, 905 trades (-800) T (thirds +151 / +513 / +48; beyond random +54 / +365 / -104; last 4 wk -125.1)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against VWAP + 3 losses in a row or 2 flip-outs** (+478 in-sample) → third 3 beyond random **-208** (rank 193 of 207, median -101)
- by plain Δ after costs: **skip against VWAP + 3 losses in a row or 2 flip-outs** (+708 in-sample) → third 3 Δ **-65** (rank 200 of 207, median +9)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -108 | +89 | -24 | -41 | -180 | -412 | -76 | -262 | +27 | +72 | +69 |
| skip against 5-day EMA (shorts only) + 2 losses in a row or 2 flip-outs | -49 | +10 | +113 | +48 | -7 | -174 | +4 | -22 | -25 | -6 | +25 |
| skip against prev session close + 2 losses in a row or 2 flip-outs | -14 | +0 | +116 | -15 | +13 | -180 | +20 | -84 | -24 | +11 | +77 |
| skip against 5-day EMA (shorts only) + 3 losses in a row or 2 flip-outs | -83 | +60 | +114 | +55 | -27 | -210 | +22 | -30 | -23 | -23 | +29 |

## MGC 3m — current: 1707 trades to 11/09, net -129 after costs (0.22 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 1249 | +71 | **+37**  | +76 / -30 / -9 | -5.7 |
| skip against 60m CBC (shorts only) | 1490 | +32 | **+16**  | +37 / -70 / +49 | -9.2 |
| skip against EMA200 slope 1 h | 1390 | +113 | **+89** T | +59 / +24 / +5 | +28.5 |
| skip against EMA200 slope 1 h (shorts only) | 1554 | +98 | **+87**  | +35 / -17 / +68 | +26.2 |
| skip against EMA200 slope 3 h | 1313 | +126 | **+97**  | -42 / +122 / +17 | +28.5 |
| skip against EMA200 slope 3 h (shorts only) | 1517 | +122 | **+108**  | -12 / +64 / +55 | +20.8 |
| skip against VWAP | 1489 | +167 | **+151** T | +54 / +34 / +63 | +19.5 |
| skip against VWAP (shorts only) | 1593 | +71 | **+62**  | +35 / -25 / +53 | +9.0 |
| skip against prev session close | 1322 | +145 | **+116** T | +34 / +62 / +20 | -14.9 |
| skip against prev session close (shorts only) | 1503 | +39 | **+23**  | +14 / -15 / +24 | -15.4 |
| skip against 5-day EMA | 1066 | +51 | **+3**  | +12 / +93 / -102 | -20.1 |
| skip against 5-day EMA (shorts only) | 1388 | +74 | **+50** T | +11 / +26 / +13 | -13.1 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 1449 | +89 | **+70**  | +57 / +23 / -9 | -16.9 |
| 3 flip-outs | 1653 | +14 | **+10**  | -8 / +1 / +16 | +25.2 |
| 4 flip-outs | 1694 | -5 | **-6**  | +1 / -10 / +3 | +0.0 |
| 2 losses in a row | 991 | +63 | **+9**  | +55 / -125 / +79 | +26.1 |
| 2 losses in a row or 2 flip-outs | 950 | +74 | **+17**  | +63 / -121 / +75 | +7.2 |
| 2 losses in a row or 3 flip-outs | 988 | +64 | **+10**  | +55 / -128 / +83 | +26.1 |
| 2 losses in a row or 4 flip-outs | 991 | +63 | **+9**  | +55 / -125 / +79 | +26.1 |
| 3 losses in a row | 1420 | +37 | **+15**  | +47 / +3 / -35 | +4.4 |
| 3 losses in a row or 2 flip-outs | 1309 | +97 | **+67**  | +69 / +13 / -15 | -9.2 |
| 3 losses in a row or 3 flip-outs | 1406 | +32 | **+10**  | +47 / -0 / -38 | +4.4 |
| 3 losses in a row or 4 flip-outs | 1419 | +34 | **+12**  | +47 / +3 / -38 | +4.4 |
| 4 losses in a row | 1584 | -48 | **-57**  | -10 / -38 / -9 | +15.9 |
| 4 losses in a row or 2 flip-outs | 1406 | +23 | **+0**  | +27 / +3 / -30 | -21.8 |
| 4 losses in a row or 3 flip-outs | 1559 | -53 | **-64**  | -10 / -35 / -18 | +19.3 |
| 4 losses in a row or 4 flip-outs | 1583 | -50 | **-60**  | -10 / -38 / -11 | +15.9 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against VWAP + 4 flip-outs: Δ **+184** after costs, beyond random **+167**, 1481 trades (-226) TTx4 (thirds +70 / +40 / +74; beyond random +64 / +35 / +68; last 4 wk +19.5)
2. skip against EMA200 slope 3 h (shorts only) + 2 flip-outs: Δ **+191** after costs, beyond random **+161**, 1320 trades (-387) TTx4 (thirds +31 / +72 / +87; beyond random +21 / +65 / +76; last 4 wk +16.2)
3. skip against VWAP + 3 flip-outs: Δ **+175** after costs, beyond random **+157**, 1464 trades (-243) TTx4 (thirds +71 / +32 / +72; beyond random +64 / +26 / +66; last 4 wk +19.5)
4. skip against VWAP + no guard: Δ **+167** after costs, beyond random **+151**, 1489 trades (-218) TTx4 (thirds +60 / +39 / +68; beyond random +54 / +34 / +63; last 4 wk +19.5)
5. skip against EMA200 slope 1 h (shorts only) + 2 flip-outs: Δ **+170** after costs, beyond random **+143**, 1339 trades (-368) 4 (thirds +78 / -1 / +93; beyond random +68 / -8 / +83; last 4 wk +28.8)
6. skip against 5-day EMA (shorts only) + 2 flip-outs: Δ **+169** after costs, beyond random **+133**, 1230 trades (-477) TTx (thirds +83 / +45 / +40; beyond random +70 / +37 / +27; last 4 wk -15.4)
7. skip against VWAP + 2 flip-outs: Δ **+156** after costs, beyond random **+129**, 1344 trades (-363) TTx4 (thirds +44 / +15 / +97; beyond random +34 / +7 / +88; last 4 wk +23.0)
8. skip against VWAP (shorts only) + 2 flip-outs: Δ **+144** after costs, beyond random **+119**, 1377 trades (-330) (thirds +85 / -2 / +61; beyond random +76 / -9 / +53; last 4 wk -4.3)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against 5-day EMA + 2 flip-outs** (+149 in-sample) → third 3 beyond random **-105** (rank 202 of 207, median +17)
- by plain Δ after costs: **skip against 5-day EMA + 2 flip-outs** (+186 in-sample) → third 3 Δ **-86** (rank 202 of 207, median +29)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -120 | +85 | +32 | -29 | -39 | -10 | -17 | -68 | -16 | +4 | +50 |
| skip against VWAP + 4 flip-outs | -112 | +73 | +35 | +56 | +2 | -31 | -6 | -61 | +21 | +30 | +49 |
| skip against EMA200 slope 3 h (shorts only) + 2 flip-outs | -83 | +26 | +32 | +27 | -32 | +13 | +25 | -49 | +33 | +29 | +40 |
| skip against VWAP + 3 flip-outs | -111 | +73 | +35 | +55 | -4 | -25 | -14 | -61 | +19 | +30 | +49 |

## MNQ 3m — current: 1937 trades to 11/09, net -1627 after costs (0.87 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 1480 | +368 | **-16**  | +340 / +280 / -637 | -8.9 |
| skip against 60m CBC (shorts only) | 1699 | -165 | **-365**  | +379 / -162 / -582 | -73.1 |
| skip against EMA200 slope 1 h | 1623 | -250 | **-514**  | -224 / -52 / -237 | +66.7 |
| skip against EMA200 slope 1 h (shorts only) | 1776 | -348 | **-483**  | -150 / -178 / -155 | +127.1 |
| skip against EMA200 slope 3 h | 1552 | -525 | **-849**  | -162 / -336 / -350 | +0.2 |
| skip against EMA200 slope 3 h (shorts only) | 1753 | -788 | **-943**  | -303 / -352 / -288 | -14.7 |
| skip against VWAP | 1756 | -358 | **-510**  | -7 / -42 / -461 | +66.8 |
| skip against VWAP (shorts only) | 1834 | -60 | **-146**  | +159 / -70 / -235 | +60.2 |
| skip against prev session close | 1512 | -740 | **-1097**  | -596 / -190 / -312 | +75.3 |
| skip against prev session close (shorts only) | 1722 | -374 | **-555**  | -226 / +166 / -495 | +37.6 |
| skip against 5-day EMA | 1248 | +356 | **-222**  | -48 / +252 / -426 | +408.0 |
| skip against 5-day EMA (shorts only) | 1575 | -210 | **-514**  | +163 / +35 / -712 | +176.8 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 1521 | +228 | **-121**  | -111 / +206 / -216 | +90.4 |
| 3 flip-outs | 1814 | -73 | **-176**  | -191 / +96 / -81 | +14.7 |
| 4 flip-outs | 1915 | -28 | **-46**  | -112 / +29 / +36 | +0.0 |
| 2 losses in a row | 978 | +973 | **+168**  | +149 / -272 / +291 | +182.4 |
| 2 losses in a row or 2 flip-outs | 918 | +676 | **-179**  | -10 / -192 / +23 | +182.4 |
| 2 losses in a row or 3 flip-outs | 977 | +999 | **+193**  | +174 / -272 / +291 | +182.4 |
| 2 losses in a row or 4 flip-outs | 978 | +973 | **+168**  | +149 / -272 / +291 | +182.4 |
| 3 losses in a row | 1428 | +861 | **+433**  | -92 / +207 / +318 | +231.4 |
| 3 losses in a row or 2 flip-outs | 1238 | +1002 | **+414**  | -164 / +479 / +100 | +296.3 |
| 3 losses in a row or 3 flip-outs | 1388 | +942 | **+480**  | -86 / +246 / +320 | +246.1 |
| 3 losses in a row or 4 flip-outs | 1421 | +950 | **+516**  | -92 / +240 / +368 | +231.4 |
| 4 losses in a row | 1706 | +315 | **+121**  | -251 / +299 / +73 | +42.0 |
| 4 losses in a row or 2 flip-outs | 1409 | +665 | **+221**  | -96 / +486 / -169 | +132.4 |
| 4 losses in a row or 3 flip-outs | 1636 | +589 | **+336**  | -106 / +366 / +76 | +56.7 |
| 4 losses in a row or 4 flip-outs | 1698 | +401 | **+201**  | -251 / +328 / +123 | +42.0 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against 5-day EMA + 2 losses in a row or 2 flip-outs: Δ **+1769** after costs, beyond random **+840**, 831 trades (-1106) TTx4 (thirds +542 / +705 / +522; beyond random +266 / +408 / +166; last 4 wk +438.7)
2. skip against VWAP (shorts only) + 3 losses in a row or 2 flip-outs: Δ **+1398** after costs, beyond random **+811**, 1238 trades (-699) TTx4 (thirds +281 / +620 / +497; beyond random +97 / +444 / +270; last 4 wk +352.5)
3. skip against EMA200 slope 1 h + 3 losses in a row or 3 flip-outs: Δ **+1358** after costs, beyond random **+810**, 1285 trades (-652) TTx4 (thirds +494 / +422 / +441; beyond random +326 / +244 / +240; last 4 wk +216.2)
4. skip against 5-day EMA + 2 losses in a row: Δ **+1654** after costs, beyond random **+741**, 850 trades (-1087) TTx4 (thirds +441 / +572 / +641; beyond random +171 / +279 / +290; last 4 wk +438.7)
5. skip against 5-day EMA + 2 losses in a row or 3 flip-outs: Δ **+1654** after costs, beyond random **+741**, 850 trades (-1087) TTx4 (thirds +441 / +572 / +641; beyond random +171 / +279 / +290; last 4 wk +438.7)
6. skip against 5-day EMA + 2 losses in a row or 4 flip-outs: Δ **+1654** after costs, beyond random **+741**, 850 trades (-1087) TTx4 (thirds +441 / +572 / +641; beyond random +171 / +279 / +290; last 4 wk +438.7)
7. skip against EMA200 slope 1 h + 3 losses in a row: Δ **+1239** after costs, beyond random **+710**, 1307 trades (-630) TTx4 (thirds +516 / +366 / +358; beyond random +350 / +199 / +161; last 4 wk +201.5)
8. skip against EMA200 slope 1 h + 3 losses in a row or 4 flip-outs: Δ **+1237** after costs, beyond random **+706**, 1305 trades (-632) TTx4 (thirds +516 / +363 / +358; beyond random +350 / +195 / +161; last 4 wk +201.5)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against 60m CBC + 4 losses in a row or 2 flip-outs** (+938 in-sample) → third 3 beyond random **-444** (rank 176 of 207, median -166)
- by plain Δ after costs: **skip against 60m CBC + 4 losses in a row or 2 flip-outs** (+1323 in-sample) → third 3 Δ **-208** (rank 163 of 207, median +67)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -493 | +181 | +140 | -275 | +156 | -813 | +84 | -310 | -1 | -55 | -241 |
| skip against 5-day EMA + 2 losses in a row or 2 flip-outs | -175 | -63 | +333 | +190 | +337 | -358 | +2 | -148 | +67 | +79 | -123 |
| skip against VWAP (shorts only) + 3 losses in a row or 2 flip-outs | -265 | +21 | +244 | -40 | +483 | -574 | +29 | -205 | +75 | +66 | -63 |
| skip against EMA200 slope 1 h + 3 losses in a row or 3 flip-outs | -420 | +314 | +379 | -95 | +373 | -592 | -84 | +14 | -68 | +3 | -94 |

## M2K 3m — current: 1948 trades to 11/09, net -604 after costs (0.35 pts per trade)

**A. Trend filters alone** (no guard)

| Filter | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| skip against 60m CBC | 1433 | +110 | **-49**  | +3 / +18 / -70 | -1.5 |
| skip against 60m CBC (shorts only) | 1698 | +54 | **-24**  | +25 / -1 / -47 | -9.1 |
| skip against EMA200 slope 1 h | 1570 | +69 | **-48**  | -3 / -28 / -17 | +7.4 |
| skip against EMA200 slope 1 h (shorts only) | 1742 | +29 | **-35**  | -3 / -22 / -9 | +3.0 |
| skip against EMA200 slope 3 h | 1508 | +110 | **-26**  | -5 / +2 / -23 | +17.9 |
| skip against EMA200 slope 3 h (shorts only) | 1705 | +67 | **-8**  | -21 / +6 / +7 | +16.3 |
| skip against VWAP | 1757 | +78 | **+19**  | -1 / +23 / -3 | +9.2 |
| skip against VWAP (shorts only) | 1836 | +45 | **+11**  | +0 / -4 / +15 | +19.3 |
| skip against prev session close | 1534 | +92 | **-37**  | -8 / -27 / -1 | +24.1 |
| skip against prev session close (shorts only) | 1726 | +92 | **+23**  | +11 / -7 / +20 | +20.6 |
| skip against 5-day EMA | 1260 | +301 | **+87** T | +18 / +31 / +38 | +34.6 |
| skip against 5-day EMA (shorts only) | 1597 | +240 | **+132** T | +38 / +54 / +40 | +13.9 |

**B. Session guards alone** (no trend filter)

| Guard | Trades | Δ after costs | Beyond random | Thirds (beyond random) | Last 4 wk |
|---|---|---|---|---|---|
| 2 flip-outs | 1307 | +135 | **-64**  | -2 / +27 / -88 | -5.1 |
| 3 flip-outs | 1710 | +51 | **-23**  | -17 / +38 / -44 | +7.4 |
| 4 flip-outs | 1854 | +64 | **+34** T | +18 / +16 / +1 | +12.0 |
| 2 losses in a row | 1058 | +206 | **-70**  | -23 / +17 / -64 | +18.1 |
| 2 losses in a row or 2 flip-outs | 946 | +234 | **-76**  | -41 / +48 / -83 | +17.5 |
| 2 losses in a row or 3 flip-outs | 1033 | +195 | **-89**  | -40 / +28 / -76 | +18.1 |
| 2 losses in a row or 4 flip-outs | 1054 | +211 | **-66**  | -26 / +24 / -64 | +18.1 |
| 3 losses in a row | 1614 | +116 | **+12**  | -7 / +51 / -31 | +7.7 |
| 3 losses in a row or 2 flip-outs | 1188 | +190 | **-46**  | -23 / +57 / -80 | -1.4 |
| 3 losses in a row or 3 flip-outs | 1504 | +112 | **-25**  | -28 / +66 / -63 | +7.7 |
| 3 losses in a row or 4 flip-outs | 1583 | +116 | **+3**  | -21 / +57 / -33 | +7.7 |
| 4 losses in a row | 1823 | +99 | **+60**  | +26 / +46 / -12 | +6.8 |
| 4 losses in a row or 2 flip-outs | 1282 | +159 | **-47**  | +0 / +46 / -93 | -6.7 |
| 4 losses in a row or 3 flip-outs | 1647 | +100 | **+7**  | +0 / +58 / -52 | +15.2 |
| 4 losses in a row or 4 flip-outs | 1760 | +121 | **+63**  | +26 / +48 / -12 | +15.5 |

**Top 8 (filter + guard) by beyond-random gain**

1. skip against 5-day EMA (shorts only) + 4 losses in a row: Δ **+269** after costs, beyond random **+140**, 1531 trades (-417) TTx4 (thirds +101 / +111 / +57; beyond random +61 / +59 / +20; last 4 wk +19.8)
2. skip against 5-day EMA (shorts only) + 4 flip-outs: Δ **+255** after costs, beyond random **+134**, 1558 trades (-390) TTx4 (thirds +85 / +103 / +67; beyond random +48 / +55 / +32; last 4 wk +22.5)
3. skip against 5-day EMA (shorts only) + 4 losses in a row or 4 flip-outs: Δ **+272** after costs, beyond random **+133**, 1501 trades (-447) TTx4 (thirds +108 / +107 / +57; beyond random +64 / +54 / +14; last 4 wk +28.5)
4. skip against 5-day EMA (shorts only) + no guard: Δ **+240** after costs, beyond random **+132**, 1597 trades (-351) TTx4 (thirds +71 / +101 / +69; beyond random +38 / +54 / +40; last 4 wk +13.9)
5. skip against 5-day EMA + 3 losses in a row: Δ **+367** after costs, beyond random **+115**, 1136 trades (-812) TTx4 (thirds +125 / +128 / +114; beyond random +43 / +42 / +31; last 4 wk +39.9)
6. skip against 5-day EMA (shorts only) + 4 losses in a row or 3 flip-outs: Δ **+275** after costs, beyond random **+113**, 1428 trades (-520) T4 (thirds +119 / +114 / +41; beyond random +71 / +57 / -14; last 4 wk +28.2)
7. skip against 5-day EMA + 3 losses in a row or 3 flip-outs: Δ **+370** after costs, beyond random **+113**, 1121 trades (-827) TTx4 (thirds +126 / +131 / +113; beyond random +43 / +45 / +26; last 4 wk +46.9)
8. skip against 5-day EMA + 3 losses in a row or 4 flip-outs: Δ **+358** after costs, beyond random **+106**, 1134 trades (-814) TTx4 (thirds +125 / +128 / +106; beyond random +43 / +42 / +21; last 4 wk +39.9)

**Walk-forward** (pick on thirds 1-2, score on third 3)

- by beyond-random: **skip against 5-day EMA (shorts only) + 4 losses in a row or 3 flip-outs** (+128 in-sample) → third 3 beyond random **-14** (rank 47 of 207, median -39)
- by plain Δ after costs: **skip against 5-day EMA + 2 losses in a row or 2 flip-outs** (+301 in-sample) → third 3 Δ **+100** (rank 9 of 207, median +33)

**By month, net after costs** (current exits vs top 3 rules)

| Rule | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| current | -28 | -79 | -4 | -114 | -62 | -42 | -98 | -35 | -53 | -43 | -44 |
| skip against 5-day EMA (shorts only) + 4 losses in a row | -2 | -28 | +1 | -52 | -26 | -12 | -99 | -6 | -49 | -17 | -44 |
| skip against 5-day EMA (shorts only) + 4 flip-outs | -4 | -53 | -1 | -40 | -24 | -12 | -102 | -18 | -36 | -9 | -50 |
| skip against 5-day EMA (shorts only) + 4 losses in a row or 4 flip-outs | -7 | -29 | +1 | -40 | -26 | -12 | -103 | -18 | -46 | -9 | -44 |

