# MTF (60m) EMA20 slope combined with the HTF (15m) EMA20 slope -- MES / MGC 3m -- 11/15/2026

Replay Jan 5 -> Nov 13 on v1.14 settings (MES 3m slope 0.42 + 13-15 block + window to 19:00 + End 16:00 OFF; MGC 3m slope 0.30 + range gate 5 + stretch 4 + FLIP 0 %). MTF EMA20 = EMA20 of 60m closes, last COMPLETED hour (no lookahead); MTF slope = |EMA20 - EMA20 k hours earlier| / 3m ATR. Thresholds as percentiles of all bars. Script mtf_study.py / mtf_eng.py (local + chat zip).

## Verdict: keep the HTF slope alone. No combination helps on either chart.

- MTF slope instead of HTF: -830..-1200 (MES), -470..-1030 (MGC). AND (both must slope): -250..-520 / -330..-880 -- removes winners. OR (MTF rescues flat-HTF setups): every rescued group loses (-58..-320). Average / scaled combos: -90..-720. MTF direction agreement (rising for long): -130..-330; 'not against' ~0 MES, -200 MGC.
- Only near-neutral rows: HTF EMA20 sloping WITH the trade (MES +9, MGC +48, z 0.9, all thirds +, noise) and price on the trade side of the MTF EMA20 (MGC +12, MES -69). Not worth a code change.
- Why: the 60m EMA moves too slowly -- when the 15m line is flat the 60m line is usually still tilted from the last move, so it rescues chop; requiring both cuts the early part of new trends, which carries most of the profit.

## MES 3m: MTF (60m) EMA20 slope combined with the HTF (15m) EMA20 slope 0.42 (v1.14 settings)

Base: 739 trades, net +809, avg +1.09, thirds +354 / -8 / +462, last 4 wk +217, max DD 142

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| MTF slope only, 1h, >= 0.18 ATR (p20) | 1068 | -19 | -828 | -3.3 | -212 / -351 / -265 | -113 | 479 | robustly worse |
| MTF slope only, 1h, >= 0.31 ATR (p35) | 858 | -380 | -1189 | -4.9 | -571 / -291 / -327 | -105 | 578 | robustly worse |
| MTF slope only, 1h, >= 0.46 ATR (p50) | 641 | -60 | -869 | -3.8 | -449 / -129 / -291 | -69 | 266 | robustly worse |
| MTF slope only, 2h, >= 0.34 ATR (p20) | 1073 | -221 | -1030 | -4.1 | -459 / -335 / -236 | -91 | 540 | robustly worse |
| MTF slope only, 2h, >= 0.59 ATR (p35) | 889 | -392 | -1201 | -4.9 | -555 / -354 / -292 | -89 | 631 | robustly worse |
| MTF slope only, 2h, >= 0.88 ATR (p50) | 667 | -60 | -869 | -3.6 | -415 / -149 / -305 | -111 | 285 | robustly worse |
| HTF base AND MTF 1h >= 0.13 (p15) | 620 | +556 | -253 | -2.4 | -83 / -79 / -91 | -5 | 157 | robustly worse |
| HTF base AND MTF 1h >= 0.23 (p25) | 565 | +421 | -388 | -3.0 | -130 / -98 / -159 | -30 | 165 | robustly worse |
| HTF base AND MTF 1h >= 0.31 (p35) | 495 | +288 | -521 | -3.5 | -209 / -96 / -216 | -20 | 136 | robustly worse |
| HTF base AND MTF 1h >= 0.46 (p50) | 408 | +305 | -504 | -2.9 | -308 / -32 / -164 | +4 | 91 | robustly worse |
| HTF base AND MTF 2h >= 0.26 (p15) | 622 | +501 | -308 | -2.8 | -128 / -26 / -154 | -50 | 117 | robustly worse |
| HTF base AND MTF 2h >= 0.42 (p25) | 563 | +490 | -319 | -2.5 | -138 / -55 / -127 | +8 | 120 | robustly worse |
| HTF base AND MTF 2h >= 0.59 (p35) | 498 | +335 | -473 | -3.1 | -201 / -80 / -193 | -29 | 125 | robustly worse |
| HTF base AND MTF 2h >= 0.88 (p50) | 398 | +380 | -429 | -2.4 | -246 / +11 / -194 | -41 | 89 | worse |
| HTF base OR MTF 1h >= 0.58 (p60) [MTF rescues] | 915 | +523 | -286 | -2.2 | -75 / -137 / -73 | -33 | 228 | robustly worse |
| HTF base OR MTF 1h >= 0.83 (p75) [MTF rescues] | 819 | +631 | -178 | -2.0 | -63 / -57 / -57 | -19 | 171 | worse |
| HTF base OR MTF 1h >= 1.34 (p90) [MTF rescues] | 766 | +751 | -58 | -1.1 | -27 / -17 / -14 | -2 | 142 | worse |
| HTF base OR MTF 2h >= 1.12 (p60) [MTF rescues] | 926 | +490 | -318 | -2.3 | -112 / -99 / -107 | -57 | 210 | robustly worse |
| HTF base OR MTF 2h >= 1.61 (p75) [MTF rescues] | 842 | +582 | -227 | -2.3 | -80 / -76 / -71 | -23 | 178 | robustly worse |
| HTF base OR MTF 2h >= 2.62 (p90) [MTF rescues] | 771 | +729 | -80 | -1.4 | -33 / -27 / -19 | -8 | 142 | worse |
| HTF base + MTF 1h EMA20 rising for long / falling for short | 613 | +679 | -130 | -1.2 | -40 / -12 / -78 | -1 | 126 | worse |
| HTF base + MTF 1h EMA20 NOT against the trade (> -0.25 ATR) | 661 | +803 | -5 | -0.1 | -21 / +27 / -11 | +14 | 115 | worse |
| HTF base + MTF 2h EMA20 rising for long / falling for short | 609 | +644 | -165 | -1.5 | -57 / +7 / -115 | -53 | 142 | worse |
| HTF base + MTF 2h EMA20 NOT against the trade (> -0.25 ATR) | 647 | +716 | -93 | -1.0 | -29 / -3 / -61 | -13 | 127 | worse |
| HTF base + MTF 3h EMA20 rising for long / falling for short | 556 | +483 | -326 | -2.5 | -76 / -62 / -188 | -72 | 135 | robustly worse |
| HTF base + MTF 3h EMA20 NOT against the trade (> -0.25 ATR) | 592 | +583 | -225 | -1.9 | -21 / -28 / -177 | -47 | 152 | worse |
| HTF base + HTF EMA20 sloping with the trade | 735 | +817 | +9 | +0.5 | +0 / +8 / +1 | +12 | 134 | noise |
| HTF base + HTF and MTF 1h both with the trade | 612 | +690 | -118 | -1.1 | -40 / -12 / -66 | +10 | 126 | worse |
| HTF base + price on the trade side of MTF EMA20 | 662 | +740 | -69 | -0.8 | -40 / -2 / -27 | -14 | 138 | worse |
| Average of HTF and MTF 1h slope (MTF scaled to HTF) >= 0.34 | 916 | +246 | -563 | -2.9 | -293 / -167 / -103 | -30 | 267 | robustly worse |
| Average of HTF and MTF 1h slope (MTF scaled to HTF) >= 0.42 | 760 | +125 | -684 | -3.8 | -233 / -214 / -236 | -33 | 281 | robustly worse |
| Average of HTF and MTF 1h slope (MTF scaled to HTF) >= 0.50 | 626 | +179 | -630 | -3.4 | -291 / -145 / -194 | +2 | 191 | robustly worse |
| HTF >= 0.34 AND MTF 1h scaled >= 0.34 (both lower) | 573 | +183 | -626 | -3.5 | -222 / -165 / -239 | -15 | 207 | robustly worse |
| HTF >= 0.50 OR MTF 1h scaled >= 0.50 | 901 | +350 | -458 | -2.7 | -245 / -78 / -136 | -62 | 204 | robustly worse |
| Average of HTF and MTF 2h slope (MTF scaled to HTF) >= 0.34 | 969 | +124 | -685 | -3.5 | -368 / -163 / -154 | -72 | 331 | robustly worse |
| Average of HTF and MTF 2h slope (MTF scaled to HTF) >= 0.42 | 791 | +90 | -719 | -3.9 | -298 / -176 / -245 | -61 | 242 | robustly worse |
| Average of HTF and MTF 2h slope (MTF scaled to HTF) >= 0.50 | 662 | +228 | -580 | -3.1 | -204 / -109 / -268 | -53 | 175 | robustly worse |
| HTF >= 0.34 AND MTF 2h scaled >= 0.34 (both lower) | 582 | +230 | -579 | -3.2 | -248 / -113 / -217 | -23 | 158 | robustly worse |
| HTF >= 0.50 OR MTF 2h scaled >= 0.50 | 934 | +327 | -482 | -2.7 | -221 / -119 / -142 | -72 | 239 | robustly worse |


## MGC 3m: MTF (60m) EMA20 slope combined with the HTF (15m) EMA20 slope 0.30 (v1.14 settings)

Base: 627 trades, net +1164, avg +1.86, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| MTF slope only, 1h, >= 0.17 ATR (p20) | 731 | +396 | -768 | -1.8 | -310 / -46 / -411 | -141 | 246 | worse |
| MTF slope only, 1h, >= 0.30 ATR (p35) | 516 | +269 | -895 | -2.1 | -342 / -68 / -485 | -168 | 212 | robustly worse |
| MTF slope only, 1h, >= 0.45 ATR (p50) | 325 | +137 | -1026 | -2.5 | -337 / -148 / -542 | -271 | 188 | robustly worse |
| MTF slope only, 2h, >= 0.31 ATR (p20) | 768 | +690 | -474 | -1.1 | -159 / -12 / -303 | -49 | 148 | worse |
| MTF slope only, 2h, >= 0.58 ATR (p35) | 559 | +402 | -762 | -1.8 | -306 / +15 / -471 | -199 | 156 | worse |
| MTF slope only, 2h, >= 0.85 ATR (p50) | 357 | +158 | -1006 | -2.4 | -379 / -97 / -530 | -193 | 191 | robustly worse |
| HTF base AND MTF 1h >= 0.13 (p15) | 454 | +670 | -494 | -2.0 | -218 / +27 / -303 | -153 | 118 | worse |
| HTF base AND MTF 1h >= 0.21 (p25) | 390 | +611 | -553 | -2.0 | -202 / -1 / -350 | -142 | 92 | robustly worse |
| HTF base AND MTF 1h >= 0.30 (p35) | 311 | +480 | -684 | -2.2 | -268 / -38 / -377 | -183 | 97 | robustly worse |
| HTF base AND MTF 1h >= 0.45 (p50) | 201 | +284 | -879 | -2.4 | -307 / -78 / -494 | -266 | 56 | robustly worse |
| HTF base AND MTF 2h >= 0.24 (p15) | 453 | +836 | -328 | -1.4 | -164 / +51 / -215 | -83 | 78 | worse |
| HTF base AND MTF 2h >= 0.40 (p25) | 388 | +735 | -429 | -1.5 | -246 / +1 / -184 | -81 | 81 | worse |
| HTF base AND MTF 2h >= 0.58 (p35) | 321 | +402 | -762 | -2.5 | -326 / -49 / -387 | -218 | 69 | robustly worse |
| HTF base AND MTF 2h >= 0.85 (p50) | 212 | +339 | -825 | -2.3 | -296 / -44 / -485 | -224 | 67 | robustly worse |
| HTF base OR MTF 1h >= 0.56 (p60) [MTF rescues] | 696 | +1060 | -104 | -0.7 | -38 / -45 / -21 | +2 | 111 | worse |
| HTF base OR MTF 1h >= 0.78 (p75) [MTF rescues] | 658 | +1070 | -94 | -0.9 | -31 / -40 / -22 | -4 | 137 | worse |
| HTF base OR MTF 1h >= 1.13 (p90) [MTF rescues] | 633 | +1164 | -0 | -0.0 | -0 / -5 / +5 | -3 | 117 | worse |
| HTF base OR MTF 2h >= 1.08 (p60) [MTF rescues] | 711 | +1050 | -114 | -0.7 | -33 / -56 / -25 | +2 | 131 | worse |
| HTF base OR MTF 2h >= 1.52 (p75) [MTF rescues] | 658 | +1110 | -54 | -0.5 | +5 / -48 / -11 | -5 | 104 | worse |
| HTF base OR MTF 2h >= 2.24 (p90) [MTF rescues] | 635 | +1157 | -7 | -0.1 | -7 / -5 / +5 | -3 | 117 | worse |
| HTF base + MTF 1h EMA20 rising for long / falling for short | 434 | +874 | -290 | -1.1 | -89 / +46 / -247 | -103 | 83 | worse |
| HTF base + MTF 1h EMA20 NOT against the trade (> -0.25 ATR) | 495 | +844 | -320 | -1.5 | -89 / +28 / -258 | -94 | 94 | worse |
| HTF base + MTF 2h EMA20 rising for long / falling for short | 417 | +895 | -268 | -1.0 | -55 / +11 / -224 | -91 | 80 | worse |
| HTF base + MTF 2h EMA20 NOT against the trade (> -0.25 ATR) | 485 | +959 | -205 | -0.9 | -67 / +32 / -170 | -40 | 81 | worse |
| HTF base + MTF 3h EMA20 rising for long / falling for short | 363 | +955 | -209 | -0.7 | -37 / +37 / -209 | -80 | 75 | worse |
| HTF base + MTF 3h EMA20 NOT against the trade (> -0.25 ATR) | 410 | +916 | -248 | -0.9 | -21 / +16 / -244 | -90 | 98 | worse |
| HTF base + HTF EMA20 sloping with the trade | 618 | +1212 | +48 | +0.9 | +22 / +20 / +7 | +0 | 102 | noise |
| HTF base + HTF and MTF 1h both with the trade | 431 | +894 | -270 | -1.1 | -75 / +51 / -247 | -103 | 83 | worse |
| HTF base + price on the trade side of MTF EMA20 | 512 | +1176 | +12 | +0.1 | +4 / +0 / +8 | +10 | 92 | noise |
| Average of HTF and MTF 1h slope (MTF scaled to HTF) >= 0.24 | 706 | +524 | -639 | -1.9 | -169 / -52 / -419 | -134 | 163 | worse |
| Average of HTF and MTF 1h slope (MTF scaled to HTF) >= 0.30 | 568 | +700 | -464 | -1.4 | -84 / -43 / -336 | -164 | 95 | worse |
| Average of HTF and MTF 1h slope (MTF scaled to HTF) >= 0.36 | 467 | +537 | -627 | -1.9 | -149 / -84 / -394 | -168 | 107 | worse |
| HTF >= 0.24 AND MTF 1h scaled >= 0.24 (both lower) | 409 | +537 | -627 | -2.0 | -244 / -33 / -350 | -143 | 87 | worse |
| HTF >= 0.36 OR MTF 1h scaled >= 0.36 | 732 | +727 | -436 | -1.4 | -122 / -167 / -147 | -41 | 262 | worse |
| Average of HTF and MTF 2h slope (MTF scaled to HTF) >= 0.24 | 749 | +790 | -374 | -1.1 | -181 / +71 / -263 | -35 | 163 | worse |
| Average of HTF and MTF 2h slope (MTF scaled to HTF) >= 0.30 | 616 | +831 | -333 | -1.0 | -108 / -8 / -217 | -56 | 97 | worse |
| Average of HTF and MTF 2h slope (MTF scaled to HTF) >= 0.36 | 508 | +692 | -472 | -1.4 | -167 / -60 / -245 | -87 | 91 | worse |
| HTF >= 0.24 AND MTF 2h scaled >= 0.24 (both lower) | 421 | +683 | -481 | -1.5 | -249 / -53 / -179 | -90 | 113 | worse |
| HTF >= 0.36 OR MTF 2h scaled >= 0.36 | 766 | +869 | -295 | -0.9 | -116 / -49 / -129 | -29 | 181 | worse |


# 4h EMA20 (added 11/15)

4h bars aligned to the CME day (18/22/02/06/10/14 ET), EMA20 of 4h closes, last COMPLETED 4h bar; lookback k = 1-3 4h bars. Script h4_study.py. Verdict: same as 60m -- nothing helps; every 4h combination worse on both charts (only the 15m-direction row is neutral).

## MES 3m: 4h EMA20 slope combined with the HTF (15m) EMA20 slope 0.42 (v1.14 settings)

Base: 739 trades, net +809, avg +1.09, thirds +354 / -8 / +462, last 4 wk +217, max DD 142

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| 4h slope only, 1 bar, >= 0.33 ATR (p20) | 1053 | -61 | -870 | -3.3 | -350 / -287 / -233 | -65 | 424 | robustly worse |
| 4h slope only, 1 bar, >= 0.60 ATR (p35) | 844 | +59 | -750 | -2.9 | -386 / -103 / -262 | -73 | 223 | robustly worse |
| 4h slope only, 1 bar, >= 0.92 ATR (p50) | 661 | +33 | -775 | -3.0 | -374 / -120 / -281 | -146 | 223 | robustly worse |
| 4h slope only, 2 bar, >= 0.64 ATR (p20) | 1020 | +51 | -758 | -2.9 | -248 / -257 / -253 | -116 | 415 | robustly worse |
| 4h slope only, 2 bar, >= 1.14 ATR (p35) | 840 | +107 | -701 | -2.7 | -255 / -178 / -268 | -111 | 276 | robustly worse |
| 4h slope only, 2 bar, >= 1.76 ATR (p50) | 669 | +182 | -627 | -2.4 | -182 / -122 / -322 | -170 | 244 | robustly worse |
| HTF base AND 4h 1 bar >= 0.25 (p15) | 585 | +562 | -247 | -2.1 | -146 / -33 / -68 | -4 | 139 | robustly worse |
| HTF base AND 4h 1 bar >= 0.41 (p25) | 512 | +428 | -381 | -2.6 | -185 / +34 / -229 | -104 | 85 | worse |
| HTF base AND 4h 1 bar >= 0.60 (p35) | 437 | +503 | -306 | -1.9 | -203 / +108 / -211 | -74 | 59 | worse |
| HTF base AND 4h 1 bar >= 0.92 (p50) | 343 | +388 | -421 | -2.2 | -211 / +49 / -259 | -149 | 49 | worse |
| HTF base AND 4h 2 bar >= 0.49 (p15) | 557 | +566 | -243 | -1.9 | -60 / -12 / -170 | -99 | 109 | worse |
| HTF base AND 4h 2 bar >= 0.80 (p25) | 482 | +492 | -316 | -2.1 | -116 / +23 / -223 | -107 | 100 | worse |
| HTF base AND 4h 2 bar >= 1.14 (p35) | 425 | +562 | -247 | -1.5 | -86 / +61 / -223 | -112 | 75 | worse |
| HTF base AND 4h 2 bar >= 1.76 (p50) | 337 | +484 | -325 | -1.7 | -71 / +50 / -304 | -179 | 47 | worse |
| HTF base OR 4h 1 bar >= 1.19 (p60) [4h rescues] | 994 | +482 | -327 | -2.0 | -140 / -169 / -18 | -14 | 254 | robustly worse |
| HTF base OR 4h 1 bar >= 1.75 (p75) [4h rescues] | 910 | +618 | -190 | -1.5 | -46 / -103 / -41 | -22 | 181 | worse |
| HTF base OR 4h 1 bar >= 2.83 (p90) [4h rescues] | 809 | +684 | -125 | -1.5 | -42 / -35 / -48 | -14 | 142 | worse |
| HTF base OR 4h 2 bar >= 2.30 (p60) [4h rescues] | 1005 | +461 | -348 | -2.1 | -113 / -212 / -23 | -12 | 288 | robustly worse |
| HTF base OR 4h 2 bar >= 3.45 (p75) [4h rescues] | 922 | +587 | -222 | -1.7 | -77 / -99 / -45 | -40 | 185 | worse |
| HTF base OR 4h 2 bar >= 5.69 (p90) [4h rescues] | 812 | +759 | -50 | -0.6 | -2 / -36 / -12 | -12 | 145 | worse |
| HTF base + 4h 1-bar EMA20 rising for long / falling for short | 455 | +533 | -276 | -1.7 | -170 / -3 / -102 | -45 | 77 | worse |
| HTF base + 4h 1-bar EMA20 NOT against the trade (> -0.25 ATR) | 504 | +601 | -208 | -1.4 | -109 / -5 / -94 | -40 | 87 | worse |
| HTF base + 4h 2-bar EMA20 rising for long / falling for short | 393 | +655 | -154 | -0.9 | -76 / +42 / -120 | -64 | 66 | worse |
| HTF base + 4h 2-bar EMA20 NOT against the trade (> -0.25 ATR) | 418 | +615 | -193 | -1.1 | -96 / +31 / -129 | -67 | 67 | worse |
| HTF base + 4h 3-bar EMA20 rising for long / falling for short | 358 | +579 | -229 | -1.3 | -115 / +85 / -200 | -156 | 46 | worse |
| HTF base + 4h 3-bar EMA20 NOT against the trade (> -0.25 ATR) | 370 | +634 | -175 | -1.0 | -115 / +95 / -155 | -103 | 49 | worse |
| HTF base + HTF EMA20 sloping with the trade | 735 | +817 | +9 | +0.5 | +0 / +8 / +1 | +12 | 134 | noise |
| HTF base + HTF and 4h 1-bar both with the trade | 454 | +545 | -264 | -1.7 | -170 / -3 / -90 | -33 | 77 | worse |
| HTF base + price on the trade side of 4h EMA20 | 542 | +674 | -135 | -1.0 | -64 / -15 / -56 | -27 | 119 | worse |
| Average of HTF and 4h 1-bar slope (4h scaled to HTF) >= 0.34 | 988 | +324 | -484 | -2.3 | -221 / -240 / -24 | -6 | 336 | robustly worse |
| Average of HTF and 4h 1-bar slope (4h scaled to HTF) >= 0.42 | 845 | +276 | -533 | -2.6 | -249 / -142 / -142 | -32 | 214 | robustly worse |
| Average of HTF and 4h 1-bar slope (4h scaled to HTF) >= 0.50 | 704 | +191 | -618 | -2.9 | -279 / -95 / -244 | -94 | 151 | robustly worse |
| HTF >= 0.34 AND 4h 1-bar scaled >= 0.34 (both lower) | 520 | +550 | -259 | -1.3 | -108 / +53 / -204 | -65 | 95 | worse |
| HTF >= 0.50 OR 4h 1-bar scaled >= 0.50 | 990 | +412 | -397 | -2.0 | -183 / -116 / -99 | -47 | 242 | robustly worse |
| Average of HTF and 4h 2-bar slope (4h scaled to HTF) >= 0.34 | 978 | +347 | -462 | -2.1 | -154 / -217 / -90 | +1 | 360 | robustly worse |
| Average of HTF and 4h 2-bar slope (4h scaled to HTF) >= 0.42 | 833 | +396 | -413 | -1.9 | -92 / -239 / -82 | -20 | 285 | worse |
| Average of HTF and 4h 2-bar slope (4h scaled to HTF) >= 0.50 | 697 | +324 | -485 | -2.2 | -152 / -90 / -242 | -110 | 155 | robustly worse |
| HTF >= 0.34 AND 4h 2-bar scaled >= 0.34 (both lower) | 503 | +551 | -258 | -1.3 | -28 / -4 / -226 | -101 | 118 | worse |
| HTF >= 0.50 OR 4h 2-bar scaled >= 0.50 | 1008 | +541 | -268 | -1.4 | -50 / -125 / -93 | -50 | 276 | worse |


## MGC 3m: 4h EMA20 slope combined with the HTF (15m) EMA20 slope 0.30 (v1.14 settings)

Base: 627 trades, net +1164, avg +1.86, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| 4h slope only, 1 bar, >= 0.34 ATR (p20) | 837 | +212 | -951 | -2.2 | -497 / -102 / -352 | -110 | 258 | robustly worse |
| 4h slope only, 1 bar, >= 0.62 ATR (p35) | 661 | +293 | -871 | -2.0 | -374 / -102 / -394 | -160 | 223 | robustly worse |
| 4h slope only, 1 bar, >= 0.93 ATR (p50) | 484 | +291 | -873 | -2.0 | -314 / -134 / -425 | -225 | 162 | robustly worse |
| 4h slope only, 2 bar, >= 0.66 ATR (p20) | 803 | +199 | -965 | -2.2 | -502 / -72 / -390 | -121 | 266 | robustly worse |
| 4h slope only, 2 bar, >= 1.22 ATR (p35) | 625 | +340 | -824 | -1.9 | -351 / -108 / -365 | -147 | 224 | worse |
| 4h slope only, 2 bar, >= 1.82 ATR (p50) | 481 | +341 | -822 | -1.9 | -370 / -93 / -359 | -171 | 173 | worse |
| HTF base AND 4h 1 bar >= 0.25 (p15) | 494 | +675 | -489 | -2.4 | -247 / +4 / -245 | -148 | 103 | worse |
| HTF base AND 4h 1 bar >= 0.43 (p25) | 437 | +481 | -683 | -2.8 | -325 / -116 / -242 | -129 | 160 | robustly worse |
| HTF base AND 4h 1 bar >= 0.62 (p35) | 375 | +371 | -792 | -2.9 | -408 / -80 / -303 | -176 | 124 | robustly worse |
| HTF base AND 4h 1 bar >= 0.93 (p50) | 274 | +365 | -799 | -2.4 | -396 / -71 / -331 | -230 | 104 | robustly worse |
| HTF base AND 4h 2 bar >= 0.50 (p15) | 470 | +690 | -474 | -2.2 | -290 / -33 / -150 | -36 | 101 | robustly worse |
| HTF base AND 4h 2 bar >= 0.84 (p25) | 419 | +506 | -658 | -2.6 | -313 / -90 / -255 | -151 | 103 | robustly worse |
| HTF base AND 4h 2 bar >= 1.22 (p35) | 349 | +461 | -702 | -2.5 | -349 / -72 / -281 | -171 | 98 | robustly worse |
| HTF base AND 4h 2 bar >= 1.82 (p50) | 264 | +381 | -782 | -2.4 | -384 / -71 / -327 | -221 | 82 | robustly worse |
| HTF base OR 4h 1 bar >= 1.15 (p60) [4h rescues] | 781 | +1070 | -94 | -0.4 | -9 / -23 / -62 | +8 | 133 | worse |
| HTF base OR 4h 1 bar >= 1.62 (p75) [4h rescues] | 701 | +993 | -171 | -1.1 | -67 / -50 / -54 | -10 | 160 | worse |
| HTF base OR 4h 1 bar >= 2.43 (p90) [4h rescues] | 651 | +1111 | -52 | -0.5 | -20 / -22 / -10 | -6 | 124 | worse |
| HTF base OR 4h 2 bar >= 2.26 (p60) [4h rescues] | 789 | +966 | -198 | -0.8 | -82 / -47 / -68 | +4 | 130 | worse |
| HTF base OR 4h 2 bar >= 3.18 (p75) [4h rescues] | 715 | +992 | -172 | -1.0 | -53 / -62 / -57 | -10 | 167 | worse |
| HTF base OR 4h 2 bar >= 4.74 (p90) [4h rescues] | 658 | +1105 | -58 | -0.5 | -20 / -25 / -14 | -2 | 125 | worse |
| HTF base + 4h 1-bar EMA20 rising for long / falling for short | 324 | +532 | -632 | -2.1 | -241 / -56 / -335 | -210 | 98 | robustly worse |
| HTF base + 4h 1-bar EMA20 NOT against the trade (> -0.25 ATR) | 358 | +805 | -359 | -1.3 | -123 / -28 / -208 | -102 | 86 | worse |
| HTF base + 4h 2-bar EMA20 rising for long / falling for short | 296 | +507 | -657 | -2.1 | -247 / -47 / -364 | -210 | 97 | robustly worse |
| HTF base + 4h 2-bar EMA20 NOT against the trade (> -0.25 ATR) | 315 | +531 | -633 | -2.1 | -259 / -55 / -319 | -210 | 103 | robustly worse |
| HTF base + 4h 3-bar EMA20 rising for long / falling for short | 277 | +546 | -617 | -1.9 | -241 / -12 / -365 | -206 | 105 | worse |
| HTF base + 4h 3-bar EMA20 NOT against the trade (> -0.25 ATR) | 284 | +557 | -606 | -1.9 | -239 / -18 / -350 | -206 | 105 | worse |
| HTF base + HTF EMA20 sloping with the trade | 618 | +1212 | +48 | +0.9 | +22 / +20 / +7 | +0 | 102 | noise |
| HTF base + HTF and 4h 1-bar both with the trade | 319 | +564 | -599 | -2.0 | -227 / -43 / -329 | -210 | 91 | worse |
| HTF base + price on the trade side of 4h EMA20 | 377 | +705 | -459 | -1.7 | -168 / -19 / -272 | -119 | 69 | worse |
| Average of HTF and 4h 1-bar slope (4h scaled to HTF) >= 0.24 | 812 | +690 | -473 | -1.3 | -240 / -39 / -194 | -33 | 185 | worse |
| Average of HTF and 4h 1-bar slope (4h scaled to HTF) >= 0.30 | 720 | +714 | -450 | -1.3 | -208 / -81 / -161 | -34 | 196 | worse |
| Average of HTF and 4h 1-bar slope (4h scaled to HTF) >= 0.36 | 615 | +708 | -455 | -1.3 | -173 / -60 / -222 | -52 | 183 | worse |
| HTF >= 0.24 AND 4h 1-bar scaled >= 0.24 (both lower) | 478 | +410 | -754 | -2.6 | -368 / -123 / -263 | -137 | 169 | robustly worse |
| HTF >= 0.36 OR 4h 1-bar scaled >= 0.36 | 841 | +780 | -384 | -1.1 | -95 / -130 / -160 | -37 | 237 | worse |
| Average of HTF and 4h 2-bar slope (4h scaled to HTF) >= 0.24 | 786 | +687 | -476 | -1.3 | -243 / -42 / -191 | -14 | 212 | worse |
| Average of HTF and 4h 2-bar slope (4h scaled to HTF) >= 0.30 | 710 | +746 | -418 | -1.2 | -260 / -36 / -121 | -8 | 182 | worse |
| Average of HTF and 4h 2-bar slope (4h scaled to HTF) >= 0.36 | 594 | +688 | -476 | -1.3 | -255 / -60 / -161 | -21 | 172 | worse |
| HTF >= 0.24 AND 4h 2-bar scaled >= 0.24 (both lower) | 454 | +414 | -750 | -2.5 | -344 / -112 / -293 | -179 | 152 | robustly worse |
| HTF >= 0.36 OR 4h 2-bar scaled >= 0.36 | 822 | +786 | -378 | -1.1 | -124 / -130 / -124 | -14 | 217 | worse |

