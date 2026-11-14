# M2K 3m -- CBC EMA Slope branch studies -- 11/14/2026

Replay Jan 5 -> Nov 13 (BarFeed / Databento M2K 3m, TV EMA20), net after 0.35 pts cost per trade. v10.97 M2K 3m settings: ER 0.23 + breakout 3, no range gate, no VWAP stretch, toward late-away 1 pt (global; M2K not in the per-symbol list), flip distance 2 ATR (M2K not in the pts list), SL1 1.7 ATR min 3 cap 5, TP1 1.7 ATR cap 3, 80 % at TP1 + BE + trail 1.7, no setups 16:00-18:45 + OR forming blocks, end at 16:00. One change at a time unless stated. In-sample: compare variants, not totals.

## 0. v10.97 baseline by trigger and session

Trades 2299, net -756, avg -0.33, win 53 %, thirds -245 / -332 / -179, last 4 wk -94, max DD 783

By trigger: flip 559 / -160 · ltf20 1133 / -525 · h9 348 / -46 · h20 259 / -25

By session: Asia 836 / -361 · London 732 / -214 · NY AM 262 / +3 · NY PM 468 / -180

## 1. HTF EMA20 slope filter threshold (vs v10.97 = off)

Base: 2299 trades, net -756, avg -0.33, thirds -245 / -332 / -179, last 4 wk -94, max DD 783

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.20 | 1800 | -481 | +276 | +3.7 | +135 / +68 / +73 | +43 | 503 | robust |
| slope 0.24 | 1696 | -444 | +312 | +3.8 | +125 / +106 / +81 | +50 | 468 | robust |
| slope 0.30 | 1554 | -402 | +354 | +4.1 | +147 / +125 / +82 | +52 | 423 | robust |
| slope 0.36 | 1396 | -315 | +441 | +4.7 | +173 / +177 / +91 | +70 | 337 | robust |
| slope 0.42 | 1276 | -284 | +472 | +4.8 | +190 / +204 / +77 | +52 | 305 | robust |
| slope 0.48 | 1152 | -206 | +550 | +5.3 | +218 / +224 / +109 | +85 | 236 | robust |
| slope 0.55 | 1000 | -198 | +559 | +5.2 | +213 / +231 / +115 | +90 | 228 | robust |
| slope 0.60 | 897 | -187 | +570 | +5.1 | +200 / +229 / +140 | +103 | 225 | robust |
| slope 0.65 | 815 | -168 | +588 | +5.2 | +196 / +245 / +147 | +105 | 202 | robust |
| slope 0.70 | 742 | -155 | +601 | +5.2 | +203 / +261 / +138 | +98 | 191 | robust |
| slope 0.75 | 654 | -126 | +630 | +5.3 | +220 / +255 / +155 | +96 | 160 | robust |
| slope 0.80 | 584 | -104 | +652 | +5.4 | +213 / +273 / +166 | +102 | 151 | robust |
| slope 0.90 | 462 | -70 | +686 | +5.6 | +237 / +287 / +162 | +99 | 108 | robust |
| slope 1.00 | 368 | -81 | +675 | +5.4 | +226 / +292 / +157 | +97 | 108 | robust |

## 2a. Branch ideas, one at a time on v10.97

Base: 2299 trades, net -756, avg -0.33, thirds -245 / -332 / -179, last 4 wk -94, max DD 783

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back (no TP1) | 2299 | -887 | -131 | -2.6 | -94 / -19 / -18 | -36 | 934 | robustly worse |
| Range gate 24 / 20 % / 5 ATR | 2022 | -771 | -15 | -0.2 | -50 / -9 / +44 | +35 | 795 | worse |
| Toward late-away OFF (strict away) | 1857 | -598 | +158 | +2.7 | +77 / +57 / +25 | +41 | 633 | robust |
| VWAP stretch 4 ATR | 1675 | -459 | +297 | +4.1 | +91 / +129 / +77 | +24 | 481 | robust |
| LTF pierce min ER 0.12 | 2183 | -611 | +146 | +3.7 | +82 / +53 / +11 | +12 | 636 | robust |
| LTF pierce min ER 0.15 | 2080 | -573 | +183 | +3.5 | +114 / +54 / +15 | +25 | 601 | robust |
| LTF pierce min ER 0.20 | 1970 | -555 | +201 | +3.1 | +96 / +78 / +26 | +30 | 589 | robust |
| LTF pierce min ER 0.23 | 1912 | -545 | +211 | +3.1 | +92 / +87 / +31 | +37 | 578 | robust |
| 100 % at TP1 | 2416 | -759 | -2 | -0.0 | -8 / +13 / -8 | -11 | 783 | worse |
| 0 % at TP1, BE, closed by HTF flip (FLIP 0 %) | 2104 | -863 | -107 | -1.1 | -47 / -50 / -9 | +0 | 923 | worse |
| 50 % at TP1 + BE + trail 1.7 | 2299 | -774 | -18 | -0.2 | -18 / -5 / +5 | -0 | 811 | worse |
| End setups at 16:00 OFF | 2299 | -758 | -2 | -0.1 | +3 / -3 / -2 | -2 | 783 | worse |
| Trigger HTF EMA9 Pierce OFF | 2081 | -724 | +32 | +0.6 | +13 / +10 / +9 | +3 | 750 | noise |
| Trigger HTF EMA20 Pierce OFF | 2127 | -699 | +57 | +1.1 | +23 / +15 / +19 | +15 | 732 | promising |
| Trigger HTF CBC Flip OFF | 2007 | -729 | +27 | +0.3 | +14 / -9 / +22 | +29 | 748 | noise |
| Trigger LTF EMA20 Pierce OFF | 1559 | -420 | +336 | +3.7 | +95 / +128 / +114 | +45 | 435 | robust |

## 2b. Same ideas on top of slope 0.90

Base: 462 trades, net -70, avg -0.15, thirds -8 / -44 / -17, last 4 wk +5, max DD 108

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Flip setups ride to HTF flip back (no TP1) | 462 | -92 | -22 | -1.8 | -29 / +1 / +6 | -1 | 121 | worse |
| Range gate 24 / 20 % / 5 ATR | 415 | -107 | -38 | -1.8 | -35 / -13 / +11 | +3 | 126 | worse |
| Toward late-away OFF (strict away) | 406 | -70 | -0 | -0.0 | -9 / +10 / -1 | -0 | 95 | worse |
| VWAP stretch 4 ATR | 158 | +31 | +101 | +2.2 | +41 / +50 / +9 | -2 | 29 | robust except last 4 wk |
| LTF pierce min ER 0.12 | 416 | -33 | +37 | +1.9 | +22 / +12 / +3 | -1 | 79 | promising |
| LTF pierce min ER 0.15 | 377 | -29 | +41 | +1.5 | +40 / +11 / -10 | -4 | 80 | noise |
| LTF pierce min ER 0.20 | 324 | -23 | +47 | +1.4 | +42 / +16 / -12 | -4 | 78 | noise |
| LTF pierce min ER 0.23 | 296 | +15 | +85 | +2.3 | +56 / +33 / -4 | -4 | 56 | noise |
| 100 % at TP1 | 482 | -58 | +12 | +0.3 | +6 / +1 / +5 | -3 | 98 | noise |
| 0 % at TP1, BE, closed by HTF flip (FLIP 0 %) | 434 | -183 | -113 | -2.7 | -39 / -57 / -16 | +7 | 220 | robustly worse |
| 50 % at TP1 + BE + trail 1.7 | 462 | -88 | -18 | -0.5 | -4 / -7 / -8 | +2 | 122 | worse |
| End setups at 16:00 OFF | 462 | -65 | +5 | +0.8 | +4 / +1 / -0 | +0 | 106 | noise |
| Trigger HTF EMA9 Pierce OFF | 427 | -79 | -9 | -0.5 | -13 / -2 / +6 | +3 | 110 | worse |
| Trigger HTF EMA20 Pierce OFF | 460 | -73 | -3 | -0.9 | -1 / +0 / -2 | -2 | 108 | worse |
| Trigger HTF CBC Flip OFF | 429 | -42 | +27 | +1.3 | +10 / +1 / +16 | +1 | 82 | promising |
| Trigger LTF EMA20 Pierce OFF | 125 | +9 | +79 | +1.6 | +25 / +41 / +12 | -3 | 19 | promising |

## 3. One-hour no-new-setup blocks on top of slope 0.90

Base: 462 trades, net -70, avg -0.15, thirds -8 / -44 / -17, last 4 wk +5, max DD 108

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| block 18:00-19:00 | 456 | -76 | -6 | -0.8 | -3 / -5 / +2 | +0 | 111 | worse |
| block 19:00-20:00 | 428 | -65 | +4 | +0.3 | -0 / -2 / +7 | +1 | 108 | noise |
| block 20:00-21:00 | 451 | -66 | +4 | +0.5 | +1 / +2 / +1 | +0 | 103 | noise |
| block 21:00-22:00 | 430 | -64 | +6 | +0.4 | +6 / -3 / +2 | -0 | 104 | noise |
| block 22:00-23:00 | 437 | -51 | +19 | +1.3 | +9 / +1 / +9 | +6 | 92 | promising |
| block 23:00-00:00 | 429 | -50 | +20 | +1.2 | +12 / +9 / -1 | +1 | 99 | noise |
| block 00:00-01:00 | 435 | -67 | +3 | +0.2 | +2 / -3 / +4 | +3 | 115 | noise |
| block 01:00-02:00 | 431 | -52 | +18 | +1.3 | -7 / +17 / +8 | +1 | 91 | noise |
| block 02:00-03:00 | 446 | -64 | +6 | +0.6 | +3 / +2 / +1 | +2 | 102 | noise |
| block 03:00-04:00 | 455 | -70 | +0 | +0.0 | +4 / +1 / -5 | -5 | 103 | noise |
| block 04:00-05:00 | 451 | -61 | +9 | +0.9 | -5 / +6 / +8 | -1 | 102 | noise |
| block 05:00-06:00 | 451 | -71 | -2 | -0.2 | -2 / +1 / -0 | +1 | 110 | worse |
| block 06:00-07:00 | 450 | -73 | -3 | -0.3 | -4 / +5 / -4 | +0 | 106 | worse |
| block 07:00-08:00 | 447 | -52 | +18 | +1.8 | +9 / -4 / +12 | +3 | 91 | noise |
| block 08:00-09:00 | 437 | -79 | -9 | -0.7 | +2 / -3 / -8 | -1 | 110 | worse |
| block 09:00-10:00 | 450 | -58 | +12 | +1.3 | -1 / +5 / +8 | -2 | 101 | noise |
| block 10:00-11:00 | 449 | -79 | -10 | -1.0 | -2 / +1 / -9 | -7 | 102 | worse |
| block 11:00-12:00 | 445 | -62 | +8 | +0.7 | +17 / -5 / -3 | +0 | 102 | noise |
| block 12:00-13:00 | 444 | -94 | -24 | -1.8 | -27 / +1 / +2 | -2 | 114 | worse |
| block 13:00-14:00 | 433 | -69 | +1 | +0.1 | +10 / +10 / -19 | -7 | 116 | noise |
| block 14:00-15:00 | 444 | -63 | +7 | +0.7 | +1 / +4 / +2 | -3 | 92 | noise |
| block 15:00-16:00 | 427 | -74 | -4 | -0.3 | -13 / +5 / +4 | +2 | 102 | worse |

## 4. Sessions (slope 0.90 vs v10.97)

| Session | v10.97 trades / net | slope 0.90 trades / net |
|---|---|---|
| Asia | 836 / -361 | 227 / -70 |
| London | 732 / -214 | 97 / -31 |
| NY AM | 262 / +3 | 33 / -2 |
| NY PM | 468 / -180 | 105 / +32 |

## 2c. M2K 3m combinations vs v10.97

Base: 2299 trades, net -756, avg -0.33, thirds -245 / -332 / -179, last 4 wk -94, max DD 783

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| slope 0.60 + stretch 4 + LTF ER 0.23 | 293 | +52 | +809 | +6.3 | +287 / +349 / +172 | +104 | 30 | robust |
| slope 0.60 + stretch 4 + LTF ER 0.23 + strict away | 241 | +63 | +820 | +6.4 | +289 / +357 / +174 | +103 | 21 | robust |
| slope 0.90 + stretch 4 | 158 | +31 | +787 | +6.1 | +278 / +338 / +171 | +97 | 29 | robust |
| slope 0.90 + stretch 4 + LTF ER 0.23 | 111 | +39 | +795 | +6.1 | +278 / +338 / +179 | +94 | 21 | robust |
| slope 0.90 + stretch 4 + LTF ER 0.23 + flip OFF | 105 | +47 | +804 | +6.1 | +286 / +337 / +181 | +94 | 19 | robust |
| slope 0.48 + stretch 4 + LTF ER 0.23 + strict away | 365 | +87 | +843 | +6.7 | +292 / +358 / +193 | +102 | 22 | robust |
| slope 0.75 + stretch 4 + LTF ER 0.23 + strict away | 152 | +31 | +787 | +6.0 | +274 / +343 / +170 | +83 | 24 | robust |
| slope 0.75 + stretch 3 + LTF ER 0.23 + strict away | 106 | +53 | +809 | +6.2 | +269 / +353 / +187 | +95 | 12 | robust |
| slope 0.75 + stretch 4 + LTF ER 0.23 + strict + 100 % at TP1 | 152 | +27 | +783 | +5.9 | +268 / +342 / +173 | +84 | 18 | robust |

## Verdict (11/14/2026)

- M2K 3m on v10.97 settings: 2299 trades, -756, every third negative (-245 / -332 / -179), every session negative except NY AM (+3).
- Slope filter robust at every threshold 0.20-1.00 (z 3.7-5.6) but alone never turns M2K positive (best 0.90: 462 trades, -70). Also robust on v10.97: VWAP stretch 4 (+297), LTF pierce min ER 0.12-0.23 (+146 to +211), toward late-away OFF / strict away (+158), LTF EMA20 Pierce trigger OFF (+336). Flip ride and FLIP 0 % exits are worse (unlike MES / MNQ / MGC).
- Combined (2c), only a thin edge: best slope 0.48 + VWAP stretch 4 + LTF ER 0.23 + strict away = 365 trades, +87 pts (thirds about +47 / +26 / +14), max DD 22. Avg +0.24 pts / trade after 0.35 cost -- most of the "gain" vs v10.97 is not trading.
- Recommendation: treat M2K 3m as no-edge. If it stays on, use the combo (input-only: ats_c_sl_sym "M2K 3m 0.48", ats_f_ext_sym "M2K 3m 4", ats_erl_sym "M2K 3m 0.23", ats_tw_sym "M2K 3m 0"); do not put it on the bot.
