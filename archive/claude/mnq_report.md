# MNQ 3m -- CBC EMA Slope branch studies -- 11/14/2026

Replay Jan 5 -> Nov 13 (BarFeed / Databento MNQ 3m, TV EMA20), net after 0.87 pts cost per trade. v10.97 MNQ 3m settings: ER 0.23 + breakout 3, no range gate, no VWAP stretch, toward late-away OFF (MNQ 3m 0), flip distance max(2 ATR, 50 pts), SL1 1.7 ATR min 25 cap 30, TP1 1.7 ATR cap 40, 80 % at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. One change at a time unless stated. In-sample: compare variants, not totals.

## 0. v10.97 baseline by trigger and session

Trades 2007, net -2317, avg -1.15, win 45 %, thirds -257 / -948 / -1112, last 4 wk -1085, max DD 2461

By trigger: flip 666 / -253 · ltf20 894 / -1588 · h9 288 / -423 · h20 159 / -52

By session: Asia 750 / -1052 · London 672 / +68 · NY AM 200 / -129 · NY PM 385 / -1204

## 1. HTF EMA20 slope filter threshold (vs v10.97 = off)

Base: 2007 trades, net -2317, avg -1.15, thirds -257 / -948 / -1112, last 4 wk -1085, max DD 2461

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1674 | -757 | +1560 | +2.2 | +640 / +25 / +896 | +297 | 1416 | robust |
| slope 0.24 | 1580 | +62 | +2379 | +3.1 | +1104 / +485 / +790 | +291 | 1356 | robust |
| slope 0.27 | 1499 | +35 | +2352 | +2.9 | +965 / +554 / +832 | +318 | 1308 | robust |
| slope 0.30 | 1420 | +496 | +2812 | +3.3 | +1242 / +722 / +849 | +305 | 1174 | robust |
| slope 0.33 | 1351 | +27 | +2344 | +2.7 | +882 / +852 / +611 | +339 | 1230 | robust |
| slope 0.36 | 1294 | +43 | +2359 | +2.6 | +849 / +922 / +589 | +389 | 1079 | robust |
| slope 0.39 | 1241 | -108 | +2209 | +2.4 | +950 / +779 / +481 | +344 | 1250 | robust |
| slope 0.42 | 1176 | +168 | +2485 | +2.6 | +954 / +877 / +653 | +460 | 927 | robust |
| slope 0.45 | 1102 | +496 | +2813 | +2.8 | +948 / +1054 / +810 | +580 | 739 | robust |
| slope 0.48 | 1031 | +614 | +2931 | +2.9 | +788 / +1169 / +974 | +610 | 635 | robust |
| slope 0.55 | 906 | +743 | +3060 | +2.9 | +732 / +1139 / +1189 | +902 | 399 | robust |
| slope 0.60 | 808 | +1265 | +3582 | +3.3 | +1036 / +1136 / +1410 | +889 | 394 | robust |

## 2a. Branch ideas, one at a time on v10.97

Base: 2007 trades, net -2317, avg -1.15, thirds -257 / -948 / -1112, last 4 wk -1085, max DD 2461

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back (no TP1) | 2007 | -2229 | +88 | +0.2 | +932 / -152 / -692 | -585 | 3072 | noise |
| Range gate 24 / 20 % / 5 ATR | 1704 | -1043 | +1274 | +1.7 | +778 / +220 / +277 | -5 | 1628 | promising |
| VWAP stretch 4 ATR | 1335 | -1609 | +708 | +0.9 | -157 / +466 / +399 | +282 | 1673 | noise |
| LTF pierce min ER 0.12 | 1910 | -1979 | +338 | +0.9 | +116 / +255 / -33 | +109 | 2122 | noise |
| LTF pierce min ER 0.15 | 1844 | -1422 | +895 | +1.9 | +360 / +340 / +196 | +161 | 1731 | promising |
| LTF pierce min ER 0.20 | 1747 | -1568 | +749 | +1.3 | +242 / +254 / +253 | +217 | 1711 | promising |
| LTF pierce min ER 0.23 | 1704 | -1802 | +515 | +0.8 | +89 / +194 / +232 | +153 | 1939 | noise |
| 100 % at TP1 | 2136 | -2510 | -193 | -0.2 | -42 / -37 / -114 | +207 | 2672 | worse |
| 0 % at TP1, BE, closed by HTF flip (FLIP 0 %) | 1816 | -923 | +1394 | +1.6 | +1421 / -345 / +318 | +31 | 2450 | noise |
| 50 % at TP1 + BE + trail 1.7 | 2007 | -2290 | +27 | +0.0 | +126 / -130 / +31 | -273 | 2418 | noise |
| End setups at 16:00 OFF | 2007 | -2399 | -82 | -0.5 | +52 / -31 / -103 | -39 | 2543 | worse |
| Trigger HTF EMA9 Pierce OFF | 1812 | -1456 | +861 | +1.7 | +93 / +454 / +314 | +163 | 1593 | promising |
| Trigger HTF EMA20 Pierce OFF | 1901 | -1955 | +362 | +0.9 | +67 / +69 / +226 | +119 | 2134 | noise |
| Trigger HTF CBC Flip OFF | 1667 | -1102 | +1215 | +1.4 | +675 / -394 / +933 | +585 | 1660 | noise |
| Trigger LTF EMA20 Pierce OFF | 1426 | -865 | +1452 | +1.7 | -74 / +760 / +766 | +505 | 981 | noise |

## 2b. Same ideas on top of slope 0.60

Base: 808 trades, net +1265, avg +1.57, thirds +779 / +188 / +299, last 4 wk -196, max DD 394

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back (no TP1) | 808 | +997 | -269 | -1.1 | +260 / +19 / -548 | -148 | 586 | worse |
| Range gate 24 / 20 % / 5 ATR | 685 | +1352 | +86 | +0.2 | +249 / -103 / -60 | -28 | 351 | noise |
| VWAP stretch 4 ATR | 319 | +762 | -503 | -0.8 | -470 / +17 / -50 | +130 | 176 | worse |
| LTF pierce min ER 0.12 | 756 | +1439 | +174 | +0.7 | -42 / +155 / +61 | +25 | 327 | noise |
| LTF pierce min ER 0.15 | 710 | +1623 | +358 | +1.0 | -14 / +242 / +131 | +78 | 322 | noise |
| LTF pierce min ER 0.20 | 639 | +1457 | +192 | +0.5 | -50 / +201 / +41 | +86 | 364 | noise |
| LTF pierce min ER 0.23 | 602 | +1393 | +128 | +0.3 | -105 / +123 / +111 | +80 | 364 | noise |
| 100 % at TP1 | 861 | +1311 | +46 | +0.1 | +84 / +14 / -53 | +135 | 376 | noise |
| 0 % at TP1, BE, closed by HTF flip (FLIP 0 %) | 731 | +2318 | +1053 | +1.9 | +481 / -141 / +713 | +635 | 745 | noise |
| 50 % at TP1 + BE + trail 1.7 | 808 | +1466 | +201 | +0.4 | +101 / +13 / +86 | -56 | 481 | noise |
| End setups at 16:00 OFF | 808 | +1182 | -83 | -0.9 | +20 / -57 / -46 | -39 | 394 | worse |
| Trigger HTF EMA9 Pierce OFF | 709 | +776 | -489 | -1.5 | -302 / -53 / -134 | +21 | 368 | worse |
| Trigger HTF EMA20 Pierce OFF | 806 | +1229 | -36 | -0.6 | -1 / -31 / -4 | +0 | 394 | worse |
| Trigger HTF CBC Flip OFF | 704 | +1328 | +63 | +0.1 | +263 / -444 / +244 | +118 | 436 | noise |
| Trigger LTF EMA20 Pierce OFF | 373 | +662 | -603 | -1.0 | -564 / +133 / -173 | +88 | 248 | worse |

## 3. One-hour no-new-setup blocks on top of slope 0.60

Base: 808 trades, net +1265, avg +1.57, thirds +779 / +188 / +299, last 4 wk -196, max DD 394

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 797 | +1410 | +145 | +1.4 | +59 / +26 / +60 | +62 | 394 | promising |
| block 19:00-20:00 | 760 | +1504 | +239 | +1.2 | +122 / +128 / -12 | +23 | 378 | noise |
| block 20:00-21:00 | 789 | +1308 | +42 | +0.3 | +69 / +52 / -79 | -21 | 363 | noise |
| block 21:00-22:00 | 781 | +1271 | +5 | +0.0 | +15 / -38 / +28 | +16 | 411 | noise |
| block 22:00-23:00 | 776 | +1319 | +53 | +0.3 | +72 / -36 / +17 | +3 | 394 | noise |
| block 23:00-00:00 | 770 | +975 | -290 | -1.5 | -153 / -77 / -60 | +74 | 388 | worse |
| block 00:00-01:00 | 761 | +943 | -322 | -1.5 | -59 / -272 / +9 | -64 | 382 | worse |
| block 01:00-02:00 | 769 | +1043 | -222 | -1.1 | -77 / -168 / +23 | +39 | 396 | worse |
| block 02:00-03:00 | 761 | +1216 | -49 | -0.2 | -75 / -89 / +114 | +47 | 407 | worse |
| block 03:00-04:00 | 788 | +1169 | -96 | -0.7 | +9 / -99 / -6 | +0 | 357 | worse |
| block 04:00-05:00 | 775 | +1303 | +38 | +0.2 | -73 / +140 / -28 | +62 | 342 | noise |
| block 05:00-06:00 | 775 | +1197 | -68 | -0.4 | -7 / +53 / -114 | +22 | 396 | worse |
| block 06:00-07:00 | 769 | +1342 | +76 | +0.4 | -52 / +64 / +65 | +58 | 394 | noise |
| block 07:00-08:00 | 776 | +1250 | -15 | -0.1 | -22 / +52 / -45 | -73 | 377 | worse |
| block 08:00-09:00 | 760 | +1047 | -218 | -1.1 | -119 / +111 / -210 | -31 | 342 | worse |
| block 09:00-10:00 | 789 | +1069 | -196 | -1.6 | -19 / -30 / -148 | +7 | 363 | worse |
| block 10:00-11:00 | 788 | +1060 | -205 | -1.5 | -219 / -4 / +18 | +31 | 534 | worse |
| block 11:00-12:00 | 778 | +1140 | -126 | -0.7 | -112 / -41 / +27 | +50 | 369 | worse |
| block 12:00-13:00 | 771 | +1179 | -87 | -0.4 | +42 / +4 / -132 | +29 | 344 | worse |
| block 13:00-14:00 | 779 | +1413 | +148 | +0.8 | +140 / +52 / -45 | -44 | 456 | noise |
| block 14:00-15:00 | 776 | +1319 | +53 | +0.3 | +18 / +17 / +19 | +46 | 346 | noise |
| block 15:00-16:00 | 764 | +1158 | -108 | -0.6 | -166 / -29 / +88 | -39 | 362 | worse |

## 4. Sessions (slope 0.60 vs v10.97)

| Session | v10.97 trades / net | slope 0.60 trades / net |
|---|---|---|
| Asia | 750 / -1052 | 345 / +197 |
| London | 672 / +68 | 247 / +611 |
| NY AM | 200 / -129 | 58 / +268 |
| NY PM | 385 / -1204 | 158 / +189 |

## 1b. Slope threshold extended (vs v10.97)

Base: 2007 trades, net -2317, avg -1.15, thirds -257 / -948 / -1112, last 4 wk -1085, max DD 2461

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.30 | 1420 | +496 | +2812 | +3.3 | +1242 / +722 / +849 | +305 | 1174 | robust |
| slope 0.45 | 1102 | +496 | +2813 | +2.8 | +948 / +1054 / +810 | +580 | 739 | robust |
| slope 0.50 | 996 | +568 | +2885 | +2.8 | +719 / +1040 / +1126 | +822 | 585 | robust |
| slope 0.55 | 906 | +743 | +3060 | +2.9 | +732 / +1139 / +1189 | +902 | 399 | robust |
| slope 0.60 | 808 | +1265 | +3582 | +3.3 | +1036 / +1136 / +1410 | +889 | 394 | robust |
| slope 0.65 | 723 | +1762 | +4079 | +3.7 | +1200 / +1255 / +1623 | +1032 | 359 | robust |
| slope 0.70 | 625 | +2131 | +4448 | +3.9 | +1104 / +1391 / +1953 | +1011 | 330 | robust |
| slope 0.75 | 558 | +2220 | +4537 | +4.0 | +1270 / +1453 / +1814 | +1034 | 295 | robust |
| slope 0.80 | 499 | +2135 | +4452 | +3.8 | +1287 / +1517 / +1648 | +1137 | 234 | robust |
| slope 0.90 | 392 | +1532 | +3849 | +3.2 | +1028 / +1548 / +1273 | +922 | 279 | robust |
| slope 1.00 | 314 | +828 | +3145 | +2.6 | +852 / +1148 / +1145 | +898 | 340 | robust |

## 1c. Same, vs slope 0.30

Base: 1420 trades, net +496, avg +0.35, thirds +985 / -227 / -263, last 4 wk -781, max DD 1174

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.45 | 1102 | +496 | +0 | +0.0 | -294 / +332 / -39 | +276 | 739 | noise |
| slope 0.50 | 996 | +568 | +73 | +0.1 | -523 / +318 / +277 | +518 | 585 | noise |
| slope 0.55 | 906 | +743 | +248 | +0.3 | -510 / +417 / +340 | +597 | 399 | noise |
| slope 0.60 | 808 | +1265 | +770 | +1.0 | -206 / +415 / +561 | +584 | 394 | noise |
| slope 0.65 | 723 | +1762 | +1266 | +1.5 | -42 / +534 / +774 | +727 | 359 | noise |
| slope 0.70 | 625 | +2131 | +1636 | +1.8 | -138 / +670 / +1104 | +707 | 330 | noise |
| slope 0.75 | 558 | +2220 | +1725 | +1.9 | +28 / +732 / +965 | +730 | 295 | promising |
| slope 0.80 | 499 | +2135 | +1639 | +1.7 | +45 / +795 / +799 | +832 | 234 | promising |
| slope 0.90 | 392 | +1532 | +1037 | +1.1 | -213 / +826 / +424 | +618 | 279 | noise |
| slope 1.00 | 314 | +828 | +332 | +0.3 | -390 / +426 / +296 | +593 | 340 | noise |

## 2c. FLIP 0 % exit + 0.15 ER on slope 0.30 / 0.60

Base: 1420 trades, net +496, avg +0.35, thirds +985 / -227 / -263, last 4 wk -781, max DD 1174

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.30 + FLIP 0 % | 1281 | +1240 | +745 | +1.0 | +428 / -282 / +599 | +947 | 1660 | noise |
| slope 0.30 + LTF ER 0.15 | 1286 | +843 | +347 | +0.8 | +103 / +216 / +28 | +135 | 951 | noise |
| slope 0.30 + FLIP 0 % + LTF ER 0.15 | 1172 | +1727 | +1231 | +1.5 | +568 / +126 / +537 | +1081 | 1396 | promising |
| slope 0.60 + FLIP 0 % | 731 | +2318 | +1822 | +1.9 | +275 / +274 / +1274 | +1219 | 745 | promising |
| slope 0.60 + FLIP 0 % + LTF ER 0.15 | 648 | +2730 | +2234 | +2.3 | +114 / +692 / +1428 | +1295 | 622 | robust |

## 2d. On top of slope 0.75

Base: 558 trades, net +2220, avg +3.98, thirds +1013 / +505 / +703, last 4 wk -51, max DD 295

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.75 + FLIP 0 % | 506 | +3724 | +1504 | +3.1 | +315 / +213 / +975 | +805 | 386 | robust |
| slope 0.75 + LTF ER 0.15 | 487 | +2331 | +110 | +0.4 | -84 / +78 / +116 | +47 | 159 | noise |
| slope 0.75 + FLIP 0 % + LTF ER 0.15 | 443 | +3944 | +1724 | +3.3 | +195 / +424 / +1104 | +851 | 285 | robust |
| slope 0.75 + 100 % at TP1 | 593 | +2238 | +18 | +0.0 | +105 / -68 / -20 | +92 | 291 | noise |
| slope 0.75 + range gate 5 | 477 | +2003 | -217 | -0.7 | +109 / -147 / -179 | -37 | 283 | worse |
| slope 0.75 + flip ride | 558 | +1988 | -232 | -1.1 | +100 / +57 / -389 | -141 | 309 | worse |

## 2e. Final candidates vs v10.97

Base: 2007 trades, net -2317, avg -1.15, thirds -257 / -948 / -1112, last 4 wk -1085, max DD 2461

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.75 | 558 | +2220 | +4537 | +4.0 | +1270 / +1453 / +1814 | +1034 | 295 | robust |
| slope 0.75 + FLIP 0 % | 506 | +3724 | +6041 | +4.9 | +1585 / +1667 / +2790 | +1840 | 386 | robust |
| slope 0.75 + LTF ER 0.15 | 487 | +2331 | +4648 | +4.0 | +1185 / +1532 / +1931 | +1081 | 159 | robust |
| slope 0.75 + FLIP 0 % + LTF ER 0.15 | 443 | +3944 | +6261 | +5.1 | +1465 / +1878 / +2918 | +1885 | 285 | robust |

## Verdict (11/14/2026)

- MNQ 3m on v10.97 settings loses badly in the replay: 2007 trades, -2317 pts, every third negative, last 4 wk -1085 (live 10/19-11/13 was also -1025).
- HTF EMA20 slope filter: robust at EVERY threshold 0.20-1.00 vs v10.97. Plateau 0.65-0.80; best 0.75: 558 trades, +2220, z 4.0 vs v10.97, thirds +1013 / +505 / +703, max DD 295 (vs 2461). vs slope 0.30, 0.75 / 0.80 are promising (z 1.9 / 1.7).
- Exit on top of slope 0.75: FLIP 0 % (0 % at TP1, BE, closed by the HTF flip -- the MGC 3m exit) robust: +1504, z 3.1, all thirds, last 4 wk +805. 100 % at TP1 / range gate / flip ride / VWAP stretch: noise or worse. LTF pierce min ER 0.15: +110 (noise) but max DD 159.
- Candidate MNQ 3m set (input-only, lists already exist): ats_c_sl_sym += "MNQ 3m 0.75"; ats_part_sym += "MNQ 3m 0"; ats_trl_sym += "MNQ 3m 0" (FLIP 0 %). Optional: ats_erl_sym += "MNQ 3m 0.15". Replay: +3724 (FLIP 0 %) / +3944 (with ER 0.15) vs -2317.
- Caveats: in-sample (threshold picked from 23 values; the plateau is the reason to trust it); MNQ replay-vs-live match has never been validated (MES ~50 %); trade count drops 72 %. Time blocks: no hour is robust; 18:00-19:00 promising (+145, z 1.4) only.
