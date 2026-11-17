# HTF EMA20 slope lookback (5 to 60 min) -- all 12 charts -- 11/15/2026

Today = 12 chart bars (24 min on 2m, 36 min on 3m, 60 min on 5m). Per lookback the threshold is rescaled (base x L/12) and gridded x0.8-1.35 (6 values). Replay on current settings (v1.16); 2m Jun 1 - Nov 13, 3m / 5m Jan 5 - Nov 13. Script slk_study.py (local). Each line: minutes: best net (vs today, z, verdict; threshold, max DD) and thresholds better than today out of 6.

- MES 2m (today 454 trades / +234, DD 49): 6 min +392 (+159, z +1.8, promising; th 0.253, DD 36) 4/6; 8 min +424 (+190, z +2.1, robust; th 0.225, DD 48) 6/6; 10 min +272 (+38, z +0.4, noise; th 0.281, DD 112) 4/6; 12 min +267 (+33, z +0.4, noise; th 0.450, DD 50) 3/6; 14 min +309 (+75, z +1.1, promising; th 0.394, DD 70) 3/6; 16 min +254 (+20, z +0.3, noise; th 0.550, DD 49) 2/6; 24 min +211 (-23, z -0.5, worse; th 0.675, DD 63) 0/5; 30 min +193 (-41, z -0.6, worse; th 0.750, DD 72) 0/6; 36 min +132 (-102, z -1.4, worse; th 1.238, DD 56) 0/6; 42 min +158 (-76, z -0.9, worse; th 1.772, DD 46) 0/6; 44 min +118 (-116, z -1.4, worse; th 1.856, DD 46) 0/6
- MGC 2m (today 863 trades / +329, DD 93): 6 min +673 (+344, z +2.9, robust; th 0.142, DD 43) 6/6; 8 min +737 (+409, z +3.7, robust; th 0.140, DD 43) 6/6; 10 min +659 (+331, z +3.5, robust; th 0.175, DD 91) 6/6; 12 min +622 (+294, z +3.2, robust except last 4 wk; th 0.252, DD 92) 6/6; 14 min +579 (+250, z +2.8, noise; th 0.196, DD 91) 6/6; 16 min +547 (+218, z +2.5, robust; th 0.224, DD 73) 6/6; 24 min +330 (+1, z +0.0, noise; th 0.378, DD 82) 1/5; 30 min +328 (+0, z -0.0, worse; th 0.420, DD 93) 0/6; 36 min +241 (-88, z -1.0, worse; th 0.756, DD 97) 0/6; 42 min +197 (-132, z -1.6, worse; th 0.735, DD 81) 0/6; 44 min +155 (-174, z -2.1, robustly worse; th 0.847, DD 90) 0/6
- MNQ 2m (today 732 trades / +3566, DD 844): 6 min +3934 (+368, z +0.3, noise; th 0.186, DD 500) 3/6; 8 min +4269 (+704, z +0.6, noise; th 0.248, DD 337) 5/6; 10 min +6000 (+2434, z +2.1, robust; th 0.275, DD 678) 6/6; 12 min +5515 (+1950, z +1.6, promising; th 0.248, DD 1068) 6/6; 14 min +5337 (+1771, z +1.7, promising; th 0.289, DD 1062) 6/6; 16 min +5355 (+1789, z +1.6, promising; th 0.293, DD 1080) 5/6; 24 min +3982 (+417, z +0.4, noise; th 0.440, DD 1449) 2/5; 30 min +3159 (-406, z -0.5, worse; th 0.756, DD 665) 0/6; 36 min +2483 (-1083, z -1.3, worse; th 0.743, DD 991) 0/6; 42 min +2716 (-850, z -0.9, worse; th 1.059, DD 767) 0/6; 44 min +2270 (-1296, z -1.3, worse; th 1.210, DD 1263) 0/6
- M2K 2m (today 198 trades / +33, DD 23): 6 min +158 (+126, z +4.0, robust; th 0.275, DD 12) 6/6; 8 min +151 (+118, z +3.4, robust; th 0.267, DD 16) 6/6; 10 min +98 (+65, z +2.3, robust; th 0.417, DD 11) 6/6; 12 min +94 (+61, z +2.2, robust; th 0.450, DD 19) 6/6; 14 min +85 (+52, z +2.7, robust; th 0.583, DD 14) 6/6; 16 min +84 (+51, z +2.0, noise; th 0.800, DD 12) 6/6; 24 min +43 (+11, z +0.6, noise; th 0.900, DD 22) 3/5; 30 min +28 (-5, z -0.2, worse; th 1.250, DD 29) 0/6; 36 min +41 (+8, z +0.4, noise; th 1.500, DD 22) 1/6; 42 min +29 (-4, z -0.2, worse; th 1.750, DD 27) 0/6; 44 min +33 (+0, z +0.0, noise; th 2.017, DD 21) 0/6
- MES 3m (today 739 trades / +809, DD 142): 6 min +441 (-367, z -1.6, worse; th 0.095, DD 133) 0/6; 9 min +606 (-203, z -1.0, worse; th 0.126, DD 76) 0/6; 12 min +586 (-223, z -1.1, worse; th 0.126, DD 98) 0/6; 15 min +856 (+47, z +0.3, noise; th 0.140, DD 181) 1/6; 24 min +740 (-69, z -0.5, worse; th 0.280, DD 115) 0/6; 30 min +773 (-36, z -0.3, worse; th 0.420, DD 98) 0/6; 36 min +742 (-67, z -0.8, worse; th 0.462, DD 122) 0/5; 42 min +684 (-124, z -1.1, worse; th 0.441, DD 145) 0/6; 45 min +649 (-159, z -1.3, worse; th 0.578, DD 149) 0/6
- MGC 3m (today 627 trades / +1164, DD 117): 6 min +1120 (-44, z -0.1, worse; th 0.068, DD 105) 0/6; 9 min +1374 (+210, z +0.6, noise; th 0.101, DD 68) 6/6; 12 min +1394 (+230, z +0.7, noise; th 0.135, DD 82) 6/6; 15 min +1575 (+411, z +1.3, promising; th 0.169, DD 106) 6/6; 24 min +1390 (+227, z +0.8, noise; th 0.180, DD 130) 6/6; 30 min +1313 (+149, z +0.8, noise; th 0.300, DD 88) 4/6; 36 min +1197 (+33, z +0.2, noise; th 0.330, DD 125) 1/5; 42 min +1125 (-38, z -0.2, worse; th 0.350, DD 95) 0/6; 45 min +1141 (-23, z -0.1, worse; th 0.506, DD 75) 0/6
- MNQ 3m (today 443 trades / +3944, DD 285): 6 min +3995 (+51, z +0.0, noise; th 0.138, DD 477) 1/6; 9 min +4036 (+92, z +0.1, noise; th 0.253, DD 362) 2/6; 12 min +5052 (+1108, z +0.8, noise; th 0.200, DD 499) 4/6; 15 min +4547 (+603, z +0.4, noise; th 0.250, DD 502) 3/6; 24 min +3668 (-276, z -0.2, worse; th 0.400, DD 293) 0/6; 30 min +3117 (-827, z -0.8, worse; th 0.562, DD 494) 0/6; 36 min +3868 (-76, z -0.1, worse; th 0.825, DD 333) 0/5; 42 min +3581 (-362, z -0.5, worse; th 0.787, DD 359) 0/6; 45 min +2350 (-1593, z -1.6, worse; th 1.125, DD 304) 0/6
- M2K 3m (today 365 trades / +87, DD 22): 6 min +124 (+37, z +0.7, noise; th 0.108, DD 26) 3/6; 9 min +162 (+75, z +1.6, promising; th 0.162, DD 21) 6/6; 12 min +176 (+90, z +2.0, promising; th 0.160, DD 21) 6/6; 15 min +116 (+29, z +0.7, noise; th 0.270, DD 19) 5/6; 24 min +120 (+34, z +0.9, noise; th 0.288, DD 22) 4/6; 30 min +98 (+11, z +0.4, noise; th 0.400, DD 23) 3/6; 36 min +86 (-1, z -0.0, worse; th 0.528, DD 21) 0/5; 42 min +76 (-11, z -0.4, worse; th 0.560, DD 20) 0/6; 45 min +77 (-9, z -0.3, worse; th 0.540, DD 20) 0/6
- MES 5m (today 228 trades / +248, DD 46): 5 min +85 (-164, z -1.6, worse; th 0.079, DD 52) 0/6; 10 min +475 (+227, z +2.5, noise; th 0.158, DD 48) 5/6; 15 min +564 (+316, z +3.6, robust; th 0.192, DD 40) 6/6; 30 min +327 (+79, z +1.0, noise; th 0.315, DD 45) 4/6; 35 min +376 (+128, z +2.0, robust except last 4 wk; th 0.367, DD 43) 5/6; 40 min +378 (+130, z +1.7, promising; th 0.373, DD 41) 3/6; 45 min +358 (+110, z +1.3, noise; th 0.420, DD 47) 2/6; 60 min +222 (-26, z -0.6, worse; th 0.770, DD 42) 0/5
- MGC 5m (today 624 trades / +672, DD 94): 5 min +320 (-352, z -2.0, robustly worse; th 0.054, DD 79) 0/6; 10 min +725 (+53, z +0.3, noise; th 0.108, DD 55) 1/6; 15 min +1096 (+424, z +2.7, robust; th 0.132, DD 55) 6/6; 30 min +1025 (+353, z +3.0, robust; th 0.264, DD 49) 6/6; 35 min +913 (+241, z +2.0, noise; th 0.224, DD 78) 6/6; 40 min +811 (+139, z +1.1, noise; th 0.256, DD 80) 3/6; 45 min +710 (+38, z +0.3, noise; th 0.432, DD 60) 5/6; 60 min +697 (+25, z +0.3, noise; th 0.432, DD 85) 1/5
- MNQ 5m (today 1484 trades / +2033, DD 777): 5 min +1085 (-948, z -0.8, worse; th 0.062, DD 413) 0/6; 10 min +2744 (+711, z +0.6, noise; th 0.124, DD 218) 6/6; 15 min +4511 (+2478, z +2.2, robust except last 4 wk; th 0.151, DD 181) 6/6; 30 min +4545 (+2511, z +2.6, robust except last 4 wk; th 0.220, DD 334) 6/6; 35 min +3867 (+1833, z +1.8, promising; th 0.257, DD 318) 6/6; 40 min +3585 (+1551, z +1.6, promising; th 0.293, DD 273) 5/6; 45 min +3380 (+1346, z +1.3, promising; th 0.330, DD 338) 6/6; 60 min +2631 (+598, z +0.6, noise; th 0.495, DD 346) 5/6
- M2K 5m (today 216 trades / +86, DD 36): 5 min +111 (+25, z +0.3, noise; th 0.100, DD 28) 4/6; 10 min +218 (+132, z +2.2, noise; th 0.200, DD 38) 6/6; 15 min +294 (+208, z +2.9, robust except last 4 wk; th 0.200, DD 34) 6/6; 30 min +265 (+179, z +3.6, robust; th 0.450, DD 17) 6/6; 35 min +187 (+101, z +2.1, robust; th 0.467, DD 33) 6/6; 40 min +139 (+53, z +1.1, promising; th 0.600, DD 24) 6/6; 45 min +158 (+72, z +1.6, promising; th 0.825, DD 15) 6/6; 60 min +90 (+4, z +0.1, noise; th 1.100, DD 37) 1/5

Verdict: 5m -> 15 min (3 bars) best on all four (30 min also good; 5 min bad). 2m -> 6-10 min (MGC / M2K robust plateau 6-16, MES 8, MNQ 10). 3m -> keep 36 min on MES / MNQ; MGC 3m 15 min and M2K 3m 9-12 min promising only. Heavy search (lookback x threshold, in-sample): implement plateau winners only.

## M2K 2m: slope lookback (base = 12 bars, slope 1.0)

Base: 198 trades, net +33, avg +0.17, thirds -6 / +5 / +33, last 4 wk +20, max DD 23

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 12 bars (24 min), slope >= 0.800 | 341 | +15 | -17 | -0.6 | -6 / -6 / -5 | -2 | 40 | worse |
| lookback 12 bars (24 min), slope >= 0.900 | 259 | +43 | +11 | +0.6 | +6 / -9 / +14 | -1 | 22 | noise |
| lookback 12 bars (24 min), slope >= 1.100 | 151 | +24 | -9 | -0.6 | -4 / -3 / -2 | -5 | 27 | worse |
| lookback 12 bars (24 min), slope >= 1.200 | 118 | +43 | +10 | +0.5 | +15 / -6 / +1 | -0 | 16 | noise |
| lookback 12 bars (24 min), slope >= 1.350 | 73 | +35 | +2 | +0.1 | +15 / -6 / -7 | -13 | 19 | noise |
| lookback 15 bars (30 min), slope >= 1.000 | 327 | +9 | -23 | -0.8 | +7 / -10 / -21 | -5 | 37 | worse |
| lookback 15 bars (30 min), slope >= 1.125 | 264 | +22 | -10 | -0.4 | +15 / -12 / -13 | -8 | 26 | worse |
| lookback 15 bars (30 min), slope >= 1.250 | 205 | +28 | -5 | -0.2 | +30 / -24 / -12 | -11 | 29 | worse |
| lookback 15 bars (30 min), slope >= 1.375 | 147 | +22 | -11 | -0.5 | +13 / -16 / -8 | -13 | 25 | worse |
| lookback 15 bars (30 min), slope >= 1.500 | 104 | +27 | -5 | -0.2 | +6 / -13 / +1 | +0 | 24 | worse |
| lookback 15 bars (30 min), slope >= 1.688 | 53 | -1 | -34 | -1.2 | -2 / -13 / -19 | -6 | 21 | worse |
| lookback 18 bars (36 min), slope >= 1.200 | 319 | -26 | -59 | -2.2 | -13 / -22 / -24 | -2 | 66 | robustly worse |
| lookback 18 bars (36 min), slope >= 1.350 | 248 | +16 | -17 | -0.8 | +13 / -10 / -21 | -6 | 26 | worse |
| lookback 18 bars (36 min), slope >= 1.500 | 189 | +41 | +8 | +0.4 | +18 / -10 / +0 | +2 | 22 | noise |
| lookback 18 bars (36 min), slope >= 1.650 | 132 | +25 | -7 | -0.3 | +8 / -13 / -2 | -1 | 23 | worse |
| lookback 18 bars (36 min), slope >= 1.800 | 99 | +22 | -11 | -0.4 | +9 / -7 / -13 | -7 | 20 | worse |
| lookback 18 bars (36 min), slope >= 2.025 | 63 | +12 | -21 | -0.7 | -1 / -7 / -13 | -13 | 16 | worse |
| lookback 21 bars (42 min), slope >= 1.400 | 314 | -31 | -64 | -2.3 | -24 / -12 / -28 | -3 | 69 | robustly worse |
| lookback 21 bars (42 min), slope >= 1.575 | 251 | +17 | -15 | -0.6 | +6 / -18 / -4 | -1 | 29 | worse |
| lookback 21 bars (42 min), slope >= 1.750 | 197 | +29 | -4 | -0.2 | +8 / -17 / +4 | +6 | 27 | worse |
| lookback 21 bars (42 min), slope >= 1.925 | 141 | +27 | -6 | -0.2 | +9 / -17 / +2 | -1 | 27 | worse |
| lookback 21 bars (42 min), slope >= 2.100 | 101 | +25 | -8 | -0.3 | +4 / -14 / +3 | -6 | 24 | worse |
| lookback 21 bars (42 min), slope >= 2.363 | 67 | +1 | -32 | -1.2 | -7 / -18 / -7 | -6 | 25 | worse |


## MES 2m: slope lookback (base = 12 bars, slope 0.75)

Base: 454 trades, net +234, avg +0.52, thirds +124 / +27 / +83, last 4 wk +4, max DD 49

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 12 bars (24 min), slope >= 0.600 | 604 | +172 | -62 | -0.9 | -33 / -42 / +12 | -27 | 70 | worse |
| lookback 12 bars (24 min), slope >= 0.675 | 521 | +211 | -23 | -0.5 | -3 / -29 / +10 | -22 | 63 | worse |
| lookback 12 bars (24 min), slope >= 0.825 | 381 | +196 | -38 | -0.8 | -20 / -29 / +11 | +3 | 49 | worse |
| lookback 12 bars (24 min), slope >= 0.900 | 308 | +181 | -53 | -0.8 | -18 / -34 / -1 | -6 | 50 | worse |
| lookback 12 bars (24 min), slope >= 1.013 | 234 | +141 | -93 | -1.2 | -46 / -37 / -9 | +10 | 47 | worse |
| lookback 15 bars (30 min), slope >= 0.750 | 586 | +193 | -41 | -0.6 | -8 / -42 / +9 | -38 | 72 | worse |
| lookback 15 bars (30 min), slope >= 0.844 | 502 | +146 | -88 | -1.3 | -9 / -65 / -14 | -19 | 68 | worse |
| lookback 15 bars (30 min), slope >= 0.938 | 425 | +63 | -171 | -2.6 | -27 / -67 / -78 | -65 | 73 | robustly worse |
| lookback 15 bars (30 min), slope >= 1.031 | 364 | +101 | -133 | -2.0 | -28 / -49 / -56 | -53 | 60 | robustly worse |
| lookback 15 bars (30 min), slope >= 1.125 | 293 | +101 | -133 | -1.9 | -27 / -35 / -72 | -53 | 53 | worse |
| lookback 15 bars (30 min), slope >= 1.266 | 214 | +90 | -144 | -1.8 | -51 / -20 / -73 | -46 | 53 | worse |
| lookback 18 bars (36 min), slope >= 0.900 | 558 | +25 | -209 | -3.1 | -75 / -57 / -77 | -69 | 71 | robustly worse |
| lookback 18 bars (36 min), slope >= 1.012 | 482 | +41 | -193 | -3.2 | -79 / -56 / -58 | -51 | 68 | robustly worse |
| lookback 18 bars (36 min), slope >= 1.125 | 404 | +92 | -142 | -2.2 | -21 / -75 / -46 | -30 | 80 | robustly worse |
| lookback 18 bars (36 min), slope >= 1.238 | 336 | +132 | -102 | -1.4 | -13 / -48 / -41 | -32 | 56 | worse |
| lookback 18 bars (36 min), slope >= 1.350 | 265 | +117 | -117 | -1.5 | -55 / -44 / -18 | -0 | 61 | worse |
| lookback 18 bars (36 min), slope >= 1.519 | 201 | +80 | -154 | -1.8 | -63 / -56 / -36 | -1 | 56 | worse |
| lookback 21 bars (42 min), slope >= 1.050 | 544 | +12 | -221 | -3.0 | -84 / -77 / -61 | -65 | 89 | robustly worse |
| lookback 21 bars (42 min), slope >= 1.181 | 473 | -48 | -282 | -4.2 | -117 / -72 / -93 | -72 | 87 | robustly worse |
| lookback 21 bars (42 min), slope >= 1.312 | 390 | +17 | -217 | -3.2 | -59 / -53 / -105 | -53 | 87 | robustly worse |
| lookback 21 bars (42 min), slope >= 1.444 | 315 | +24 | -210 | -3.0 | -63 / -51 / -97 | -54 | 85 | robustly worse |
| lookback 21 bars (42 min), slope >= 1.575 | 268 | +59 | -175 | -2.3 | -35 / -61 / -79 | -28 | 66 | robustly worse |
| lookback 21 bars (42 min), slope >= 1.772 | 191 | +158 | -76 | -0.9 | -25 / -29 / -22 | -14 | 46 | worse |


## MGC 2m: slope lookback (base = 12 bars, slope 0.42)

Base: 863 trades, net +329, avg +0.38, thirds +170 / +126 / +33, last 4 wk -24, max DD 93

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 12 bars (24 min), slope >= 0.336 | 1003 | +267 | -62 | -0.9 | +18 / -31 / -49 | -39 | 101 | worse |
| lookback 12 bars (24 min), slope >= 0.378 | 935 | +330 | +1 | +0.0 | +36 / -41 / +6 | +4 | 82 | noise |
| lookback 12 bars (24 min), slope >= 0.462 | 792 | +301 | -28 | -0.6 | -7 / -9 / -12 | -9 | 101 | worse |
| lookback 12 bars (24 min), slope >= 0.504 | 699 | +313 | -16 | -0.2 | -31 / +15 / -0 | -15 | 97 | worse |
| lookback 12 bars (24 min), slope >= 0.567 | 627 | +249 | -79 | -0.9 | -43 / +2 / -38 | -19 | 96 | worse |
| lookback 15 bars (30 min), slope >= 0.420 | 981 | +328 | -0 | -0.0 | +19 / -27 / +7 | -11 | 93 | worse |
| lookback 15 bars (30 min), slope >= 0.473 | 921 | +248 | -80 | -1.2 | +21 / -57 / -45 | -50 | 128 | worse |
| lookback 15 bars (30 min), slope >= 0.525 | 835 | +274 | -55 | -0.8 | +8 / -30 / -34 | -27 | 94 | worse |
| lookback 15 bars (30 min), slope >= 0.578 | 765 | +244 | -85 | -1.2 | -2 / -49 / -34 | -19 | 91 | worse |
| lookback 15 bars (30 min), slope >= 0.630 | 706 | +200 | -129 | -1.7 | -10 / -80 / -39 | -27 | 94 | worse |
| lookback 15 bars (30 min), slope >= 0.709 | 618 | +242 | -87 | -1.0 | -10 / -69 / -8 | -29 | 94 | worse |
| lookback 18 bars (36 min), slope >= 0.504 | 970 | +159 | -169 | -2.4 | -22 / -137 / -11 | -15 | 96 | robustly worse |
| lookback 18 bars (36 min), slope >= 0.567 | 899 | +108 | -221 | -3.2 | -55 / -126 / -39 | -56 | 122 | robustly worse |
| lookback 18 bars (36 min), slope >= 0.630 | 827 | +215 | -114 | -1.6 | -4 / -91 / -19 | -34 | 95 | worse |
| lookback 18 bars (36 min), slope >= 0.693 | 734 | +215 | -114 | -1.5 | -14 / -77 / -23 | -40 | 99 | worse |
| lookback 18 bars (36 min), slope >= 0.756 | 663 | +241 | -88 | -1.0 | -19 / -42 / -27 | -42 | 97 | worse |
| lookback 18 bars (36 min), slope >= 0.851 | 597 | +146 | -183 | -1.9 | -28 / -112 / -43 | -20 | 78 | worse |
| lookback 21 bars (42 min), slope >= 0.588 | 979 | +177 | -152 | -1.8 | -26 / -106 / -20 | -32 | 98 | worse |
| lookback 21 bars (42 min), slope >= 0.661 | 893 | +162 | -166 | -2.1 | -45 / -107 / -14 | -36 | 96 | robustly worse |
| lookback 21 bars (42 min), slope >= 0.735 | 811 | +197 | -132 | -1.6 | -32 / -64 / -36 | -16 | 81 | worse |
| lookback 21 bars (42 min), slope >= 0.808 | 746 | +162 | -166 | -2.0 | -24 / -101 / -42 | -2 | 87 | robustly worse |
| lookback 21 bars (42 min), slope >= 0.882 | 669 | +138 | -191 | -2.3 | -59 / -95 / -37 | -12 | 82 | robustly worse |
| lookback 21 bars (42 min), slope >= 0.992 | 570 | +80 | -249 | -2.7 | -84 / -108 / -57 | -16 | 81 | robustly worse |


## MNQ 2m: slope lookback (base = 12 bars, slope 0.55)

Base: 732 trades, net +3566, avg +4.87, thirds +1397 / +487 / +1681, last 4 wk +733, max DD 844

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 12 bars (24 min), slope >= 0.440 | 895 | +3982 | +417 | +0.4 | -104 / +22 / +498 | +513 | 1449 | noise |
| lookback 12 bars (24 min), slope >= 0.495 | 810 | +3598 | +32 | +0.1 | -167 / -171 / +370 | +407 | 1054 | noise |
| lookback 12 bars (24 min), slope >= 0.605 | 637 | +3559 | -7 | -0.0 | +134 / -8 / -134 | +128 | 806 | worse |
| lookback 12 bars (24 min), slope >= 0.660 | 567 | +2654 | -912 | -1.0 | +27 / -177 / -761 | -557 | 639 | worse |
| lookback 12 bars (24 min), slope >= 0.743 | 457 | +2115 | -1451 | -1.3 | +98 / -905 / -644 | -560 | 1096 | worse |
| lookback 15 bars (30 min), slope >= 0.550 | 906 | +2372 | -1194 | -1.3 | -639 / -481 / -74 | -57 | 1441 | worse |
| lookback 15 bars (30 min), slope >= 0.619 | 821 | +2297 | -1269 | -1.4 | -853 / -415 / -1 | +67 | 1285 | worse |
| lookback 15 bars (30 min), slope >= 0.688 | 714 | +2784 | -782 | -0.9 | -468 / -450 / +137 | +233 | 983 | worse |
| lookback 15 bars (30 min), slope >= 0.756 | 622 | +3159 | -406 | -0.5 | -107 / -213 / -87 | +61 | 665 | worse |
| lookback 15 bars (30 min), slope >= 0.825 | 550 | +2329 | -1236 | -1.3 | -106 / -907 / -223 | +160 | 1159 | worse |
| lookback 15 bars (30 min), slope >= 0.928 | 455 | +1774 | -1791 | -1.7 | +28 / -920 / -899 | -564 | 1196 | worse |
| lookback 18 bars (36 min), slope >= 0.660 | 862 | +1832 | -1734 | -2.0 | -988 / -483 / -263 | -148 | 1458 | worse |
| lookback 18 bars (36 min), slope >= 0.743 | 760 | +2483 | -1083 | -1.3 | -686 / -306 / -91 | -27 | 991 | worse |
| lookback 18 bars (36 min), slope >= 0.825 | 669 | +2251 | -1315 | -1.4 | -357 / -775 / -182 | -108 | 1224 | worse |
| lookback 18 bars (36 min), slope >= 0.908 | 599 | +1258 | -2308 | -2.4 | -286 / -964 / -1058 | -786 | 1324 | robustly worse |
| lookback 18 bars (36 min), slope >= 0.990 | 531 | +1344 | -2222 | -2.1 | -201 / -1059 / -961 | -683 | 1306 | robustly worse |
| lookback 18 bars (36 min), slope >= 1.114 | 431 | +1767 | -1799 | -1.6 | -165 / -754 / -880 | -635 | 913 | worse |
| lookback 21 bars (42 min), slope >= 0.770 | 868 | +1719 | -1847 | -1.8 | -1134 / -192 / -521 | -206 | 1621 | worse |
| lookback 21 bars (42 min), slope >= 0.866 | 770 | +1726 | -1840 | -1.9 | -704 / -739 / -397 | -188 | 1436 | worse |
| lookback 21 bars (42 min), slope >= 0.963 | 677 | +2027 | -1539 | -1.6 | -217 / -870 / -451 | +27 | 1086 | worse |
| lookback 21 bars (42 min), slope >= 1.059 | 600 | +2716 | -850 | -0.9 | -61 / -539 / -250 | +143 | 767 | worse |
| lookback 21 bars (42 min), slope >= 1.155 | 533 | +2378 | -1188 | -1.2 | +70 / -1041 / -217 | +178 | 1067 | worse |
| lookback 21 bars (42 min), slope >= 1.299 | 445 | +2001 | -1565 | -1.4 | +77 / -754 / -888 | -669 | 965 | worse |


## M2K 2m: slope lookback (base = 12 bars, slope 1.0)

Base: 198 trades, net +33, avg +0.17, thirds -6 / +5 / +33, last 4 wk +20, max DD 23

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 22 bars (44 min), slope >= 1.467 | 309 | -10 | -43 | -1.6 | -13 / -14 / -16 | -0 | 50 | worse |
| lookback 22 bars (44 min), slope >= 1.650 | 251 | +19 | -13 | -0.5 | +1 / -17 / +3 | +2 | 35 | worse |
| lookback 22 bars (44 min), slope >= 1.833 | 193 | +32 | -0 | -0.0 | +15 / -10 / -5 | -3 | 19 | worse |
| lookback 22 bars (44 min), slope >= 2.017 | 137 | +33 | +0 | +0.0 | +13 / -13 / +0 | -9 | 21 | noise |
| lookback 22 bars (44 min), slope >= 2.200 | 97 | +17 | -15 | -0.7 | +2 / -18 / +1 | -5 | 25 | worse |
| lookback 22 bars (44 min), slope >= 2.475 | 66 | +11 | -22 | -0.8 | -4 / -12 / -6 | -6 | 17 | worse |


## MES 2m: slope lookback (base = 12 bars, slope 0.75)

Base: 454 trades, net +234, avg +0.52, thirds +124 / +27 / +83, last 4 wk +4, max DD 49

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 22 bars (44 min), slope >= 1.100 | 541 | +24 | -210 | -2.9 | -93 / -69 / -48 | -47 | 74 | robustly worse |
| lookback 22 bars (44 min), slope >= 1.238 | 466 | -14 | -248 | -3.7 | -119 / -60 / -68 | -51 | 78 | robustly worse |
| lookback 22 bars (44 min), slope >= 1.375 | 386 | -15 | -248 | -3.8 | -112 / -51 / -85 | -41 | 88 | robustly worse |
| lookback 22 bars (44 min), slope >= 1.513 | 314 | +48 | -185 | -2.7 | -60 / -69 / -56 | -29 | 83 | robustly worse |
| lookback 22 bars (44 min), slope >= 1.650 | 254 | +95 | -139 | -1.8 | -33 / -51 / -54 | -15 | 52 | worse |
| lookback 22 bars (44 min), slope >= 1.856 | 189 | +118 | -116 | -1.4 | -64 / -26 / -26 | -7 | 46 | worse |


## MGC 2m: slope lookback (base = 12 bars, slope 0.42)

Base: 863 trades, net +329, avg +0.38, thirds +170 / +126 / +33, last 4 wk -24, max DD 93

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 22 bars (44 min), slope >= 0.616 | 978 | +152 | -177 | -2.1 | -29 / -148 / +1 | -16 | 100 | worse |
| lookback 22 bars (44 min), slope >= 0.693 | 879 | +143 | -186 | -2.3 | -28 / -139 / -18 | -19 | 93 | robustly worse |
| lookback 22 bars (44 min), slope >= 0.770 | 805 | +141 | -187 | -2.3 | -46 / -114 / -27 | -15 | 93 | robustly worse |
| lookback 22 bars (44 min), slope >= 0.847 | 741 | +155 | -174 | -2.1 | -64 / -91 / -19 | +1 | 90 | robustly worse |
| lookback 22 bars (44 min), slope >= 0.924 | 648 | +149 | -180 | -2.1 | -79 / -98 / -3 | +9 | 88 | robustly worse |
| lookback 22 bars (44 min), slope >= 1.040 | 573 | +126 | -203 | -2.2 | -92 / -83 / -27 | +2 | 89 | robustly worse |


## MNQ 2m: slope lookback (base = 12 bars, slope 0.55)

Base: 732 trades, net +3566, avg +4.87, thirds +1397 / +487 / +1681, last 4 wk +733, max DD 844

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 22 bars (44 min), slope >= 0.807 | 855 | +1816 | -1750 | -1.7 | -1065 / -266 / -419 | -184 | 1503 | worse |
| lookback 22 bars (44 min), slope >= 0.908 | 766 | +1569 | -1997 | -2.2 | -662 / -862 / -473 | -302 | 1518 | robustly worse |
| lookback 22 bars (44 min), slope >= 1.008 | 674 | +2065 | -1501 | -1.6 | -586 / -674 / -241 | +91 | 1073 | worse |
| lookback 22 bars (44 min), slope >= 1.109 | 596 | +2202 | -1363 | -1.4 | +102 / -1098 / -367 | -11 | 1161 | worse |
| lookback 22 bars (44 min), slope >= 1.210 | 526 | +2270 | -1296 | -1.3 | +30 / -1020 / -305 | +47 | 1263 | worse |
| lookback 22 bars (44 min), slope >= 1.361 | 433 | +1934 | -1632 | -1.4 | +21 / -821 / -832 | -618 | 1009 | worse |


## M2K 2m: slope lookback (base = 12 bars, slope 1.0)

Base: 198 trades, net +33, avg +0.17, thirds -6 / +5 / +33, last 4 wk +20, max DD 23

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (16 min), slope >= 0.533 | 319 | +48 | +16 | +0.6 | +8 / +23 / -15 | +8 | 31 | noise |
| lookback 8 bars (16 min), slope >= 0.600 | 248 | +68 | +36 | +1.5 | +23 / +10 / +3 | +11 | 18 | promising |
| lookback 8 bars (16 min), slope >= 0.667 | 199 | +52 | +19 | +0.8 | +23 / +4 / -8 | -0 | 17 | noise |
| lookback 8 bars (16 min), slope >= 0.733 | 160 | +66 | +34 | +1.4 | +33 / +15 / -15 | -12 | 13 | noise |
| lookback 8 bars (16 min), slope >= 0.800 | 129 | +84 | +51 | +2.0 | +34 / +20 / -3 | -11 | 12 | noise |
| lookback 8 bars (16 min), slope >= 0.900 | 84 | +62 | +29 | +1.1 | +26 / +6 / -3 | -8 | 7 | noise |


## MES 2m: slope lookback (base = 12 bars, slope 0.75)

Base: 454 trades, net +234, avg +0.52, thirds +124 / +27 / +83, last 4 wk +4, max DD 49

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (16 min), slope >= 0.400 | 588 | +196 | -38 | -0.5 | -21 / -4 / -13 | -54 | 69 | worse |
| lookback 8 bars (16 min), slope >= 0.450 | 522 | +191 | -42 | -0.6 | -12 / -18 / -12 | -51 | 64 | worse |
| lookback 8 bars (16 min), slope >= 0.500 | 456 | +207 | -27 | -0.4 | -16 / -20 / +9 | -30 | 61 | worse |
| lookback 8 bars (16 min), slope >= 0.550 | 393 | +254 | +20 | +0.3 | -9 / -23 / +52 | +25 | 49 | noise |
| lookback 8 bars (16 min), slope >= 0.600 | 326 | +242 | +8 | +0.1 | +5 / -6 / +9 | +1 | 49 | noise |
| lookback 8 bars (16 min), slope >= 0.675 | 259 | +231 | -3 | -0.0 | -19 / -1 / +17 | +32 | 31 | worse |


## MGC 2m: slope lookback (base = 12 bars, slope 0.42)

Base: 863 trades, net +329, avg +0.38, thirds +170 / +126 / +33, last 4 wk -24, max DD 93

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (16 min), slope >= 0.224 | 986 | +547 | +218 | +2.5 | +113 / +41 / +64 | +46 | 73 | robust |
| lookback 8 bars (16 min), slope >= 0.252 | 900 | +503 | +174 | +2.1 | +55 / +53 / +66 | +10 | 75 | robust |
| lookback 8 bars (16 min), slope >= 0.280 | 836 | +539 | +210 | +2.6 | +75 / +89 / +46 | -3 | 66 | robust except last 4 wk |
| lookback 8 bars (16 min), slope >= 0.308 | 761 | +512 | +183 | +2.2 | +86 / +42 / +55 | -3 | 72 | robust except last 4 wk |
| lookback 8 bars (16 min), slope >= 0.336 | 702 | +493 | +164 | +1.9 | +40 / +42 / +83 | +25 | 58 | promising |
| lookback 8 bars (16 min), slope >= 0.378 | 616 | +494 | +165 | +1.7 | +38 / +66 / +61 | +12 | 58 | promising |


## MNQ 2m: slope lookback (base = 12 bars, slope 0.55)

Base: 732 trades, net +3566, avg +4.87, thirds +1397 / +487 / +1681, last 4 wk +733, max DD 844

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (16 min), slope >= 0.293 | 900 | +5355 | +1789 | +1.6 | +722 / +700 / +367 | +239 | 1080 | promising |
| lookback 8 bars (16 min), slope >= 0.330 | 792 | +4661 | +1095 | +1.0 | +108 / +447 / +541 | +388 | 1169 | promising |
| lookback 8 bars (16 min), slope >= 0.367 | 696 | +4968 | +1402 | +1.4 | +399 / +563 / +440 | +186 | 891 | promising |
| lookback 8 bars (16 min), slope >= 0.403 | 624 | +4385 | +819 | +0.8 | +379 / +717 / -278 | -530 | 637 | noise |
| lookback 8 bars (16 min), slope >= 0.440 | 542 | +3835 | +269 | +0.2 | +138 / +733 / -602 | -606 | 542 | noise |
| lookback 8 bars (16 min), slope >= 0.495 | 465 | +2193 | -1373 | -1.2 | -520 / -366 / -488 | -673 | 439 | worse |


## M2K 2m: slope lookback (base = 12 bars, slope 1.0)

Base: 198 trades, net +33, avg +0.17, thirds -6 / +5 / +33, last 4 wk +20, max DD 23

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (6 min), slope >= 0.200 | 398 | +45 | +13 | +0.3 | +3 / +35 / -26 | +10 | 44 | noise |
| lookback 3 bars (6 min), slope >= 0.225 | 345 | +65 | +32 | +0.9 | +15 / +29 / -12 | +6 | 30 | noise |
| lookback 3 bars (6 min), slope >= 0.250 | 296 | +126 | +93 | +2.9 | +25 / +42 / +26 | +14 | 23 | robust |
| lookback 3 bars (6 min), slope >= 0.275 | 262 | +158 | +126 | +4.0 | +46 / +46 / +34 | +18 | 12 | robust |
| lookback 3 bars (6 min), slope >= 0.300 | 224 | +136 | +103 | +3.5 | +49 / +37 / +17 | +3 | 10 | robust |
| lookback 3 bars (6 min), slope >= 0.338 | 180 | +139 | +106 | +3.8 | +48 / +41 / +18 | +8 | 10 | robust |
| lookback 4 bars (8 min), slope >= 0.267 | 343 | +151 | +118 | +3.4 | +47 / +32 / +40 | +3 | 16 | robust |
| lookback 4 bars (8 min), slope >= 0.300 | 286 | +141 | +108 | +3.4 | +48 / +28 / +32 | +2 | 14 | robust |
| lookback 4 bars (8 min), slope >= 0.333 | 234 | +140 | +107 | +3.6 | +52 / +28 / +27 | +0 | 15 | robust |
| lookback 4 bars (8 min), slope >= 0.367 | 189 | +125 | +93 | +3.3 | +52 / +31 / +10 | -7 | 10 | robust except last 4 wk |
| lookback 4 bars (8 min), slope >= 0.400 | 149 | +124 | +91 | +3.4 | +47 / +31 / +13 | -6 | 10 | robust except last 4 wk |
| lookback 4 bars (8 min), slope >= 0.450 | 105 | +111 | +79 | +3.0 | +42 / +24 / +12 | -4 | 5 | robust except last 4 wk |
| lookback 5 bars (10 min), slope >= 0.333 | 365 | +67 | +35 | +1.0 | +38 / -1 / -2 | -7 | 24 | noise |
| lookback 5 bars (10 min), slope >= 0.375 | 278 | +91 | +59 | +1.8 | +63 / +2 / -6 | -2 | 15 | noise |
| lookback 5 bars (10 min), slope >= 0.417 | 202 | +98 | +65 | +2.3 | +45 / +14 / +6 | +1 | 11 | robust |
| lookback 5 bars (10 min), slope >= 0.458 | 155 | +93 | +61 | +2.3 | +37 / +9 / +14 | +6 | 12 | robust |
| lookback 5 bars (10 min), slope >= 0.500 | 119 | +72 | +40 | +1.4 | +35 / -1 / +6 | +10 | 15 | noise |
| lookback 5 bars (10 min), slope >= 0.563 | 72 | +50 | +18 | +0.7 | +23 / +0 / -6 | +1 | 12 | noise |
| lookback 6 bars (12 min), slope >= 0.400 | 340 | +39 | +6 | +0.2 | +3 / +7 / -4 | +10 | 31 | noise |
| lookback 6 bars (12 min), slope >= 0.450 | 270 | +94 | +61 | +2.2 | +20 / +20 / +21 | +24 | 19 | robust |
| lookback 6 bars (12 min), slope >= 0.500 | 219 | +70 | +37 | +1.4 | +11 / +15 / +11 | +25 | 20 | promising |
| lookback 6 bars (12 min), slope >= 0.550 | 164 | +78 | +46 | +1.9 | +18 / +9 / +20 | +19 | 13 | promising |
| lookback 6 bars (12 min), slope >= 0.600 | 132 | +69 | +36 | +1.5 | +11 / +4 / +21 | +18 | 15 | promising |
| lookback 6 bars (12 min), slope >= 0.675 | 96 | +42 | +9 | +0.4 | +14 / -6 / +1 | +2 | 13 | noise |
| lookback 7 bars (14 min), slope >= 0.467 | 319 | +80 | +48 | +1.7 | +9 / +20 / +18 | +21 | 24 | promising |
| lookback 7 bars (14 min), slope >= 0.525 | 255 | +83 | +51 | +2.2 | +4 / +22 / +24 | +23 | 20 | robust |
| lookback 7 bars (14 min), slope >= 0.583 | 201 | +85 | +52 | +2.7 | +12 / +12 / +28 | +20 | 14 | robust |
| lookback 7 bars (14 min), slope >= 0.642 | 159 | +59 | +26 | +1.4 | +16 / +2 / +8 | +4 | 14 | promising |
| lookback 7 bars (14 min), slope >= 0.700 | 129 | +55 | +22 | +1.1 | +25 / -3 / +1 | -5 | 13 | noise |
| lookback 7 bars (14 min), slope >= 0.788 | 90 | +71 | +38 | +1.5 | +28 / +16 / -6 | -11 | 9 | noise |


## MES 2m: slope lookback (base = 12 bars, slope 0.75)

Base: 454 trades, net +234, avg +0.52, thirds +124 / +27 / +83, last 4 wk +4, max DD 49

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (6 min), slope >= 0.150 | 562 | +109 | -125 | -1.3 | -116 / +7 / -15 | -31 | 78 | worse |
| lookback 3 bars (6 min), slope >= 0.169 | 515 | +208 | -26 | -0.3 | -77 / +24 / +27 | +3 | 57 | worse |
| lookback 3 bars (6 min), slope >= 0.188 | 482 | +267 | +33 | +0.4 | -24 / +20 / +36 | +5 | 53 | noise |
| lookback 3 bars (6 min), slope >= 0.206 | 450 | +361 | +127 | +1.4 | -3 / +51 / +79 | +30 | 44 | noise |
| lookback 3 bars (6 min), slope >= 0.225 | 422 | +389 | +155 | +1.7 | +24 / +45 / +86 | +34 | 38 | promising |
| lookback 3 bars (6 min), slope >= 0.253 | 360 | +392 | +159 | +1.8 | +57 / +40 / +62 | +38 | 36 | promising |
| lookback 4 bars (8 min), slope >= 0.200 | 560 | +309 | +75 | +0.8 | +24 / -5 / +56 | -14 | 63 | noise |
| lookback 4 bars (8 min), slope >= 0.225 | 497 | +424 | +190 | +2.1 | +71 / +13 / +107 | +29 | 48 | robust |
| lookback 4 bars (8 min), slope >= 0.250 | 439 | +424 | +190 | +2.1 | +90 / +24 / +76 | +24 | 44 | robust |
| lookback 4 bars (8 min), slope >= 0.275 | 381 | +396 | +162 | +1.9 | +78 / +43 / +42 | -9 | 57 | promising |
| lookback 4 bars (8 min), slope >= 0.300 | 330 | +374 | +140 | +1.6 | +80 / +58 / +2 | -34 | 48 | promising |
| lookback 4 bars (8 min), slope >= 0.338 | 271 | +356 | +122 | +1.4 | +32 / +75 / +14 | -6 | 30 | promising |
| lookback 5 bars (10 min), slope >= 0.250 | 627 | +220 | -14 | -0.1 | +33 / -0 / -47 | -103 | 128 | worse |
| lookback 5 bars (10 min), slope >= 0.281 | 542 | +272 | +38 | +0.4 | +51 / +23 / -36 | -92 | 112 | noise |
| lookback 5 bars (10 min), slope >= 0.312 | 458 | +248 | +14 | +0.2 | +55 / +41 / -82 | -104 | 100 | noise |
| lookback 5 bars (10 min), slope >= 0.344 | 387 | +259 | +25 | +0.3 | +33 / +61 / -68 | -74 | 73 | noise |
| lookback 5 bars (10 min), slope >= 0.375 | 326 | +244 | +10 | +0.1 | +30 / +23 / -42 | -58 | 77 | noise |
| lookback 5 bars (10 min), slope >= 0.422 | 236 | +192 | -42 | -0.5 | +20 / +20 / -82 | -72 | 68 | worse |
| lookback 6 bars (12 min), slope >= 0.300 | 596 | +134 | -99 | -1.1 | +17 / -13 / -103 | -105 | 115 | worse |
| lookback 6 bars (12 min), slope >= 0.338 | 513 | +192 | -42 | -0.5 | +15 / +51 / -108 | -100 | 95 | worse |
| lookback 6 bars (12 min), slope >= 0.375 | 444 | +257 | +23 | +0.3 | +48 / +35 / -60 | -72 | 71 | noise |
| lookback 6 bars (12 min), slope >= 0.413 | 380 | +201 | -33 | -0.4 | +41 / +27 / -101 | -70 | 67 | worse |
| lookback 6 bars (12 min), slope >= 0.450 | 323 | +267 | +33 | +0.4 | +38 / +52 / -57 | -36 | 50 | noise |
| lookback 6 bars (12 min), slope >= 0.506 | 252 | +249 | +15 | +0.2 | +12 / +67 / -64 | -32 | 52 | noise |
| lookback 7 bars (14 min), slope >= 0.350 | 584 | +190 | -44 | -0.6 | -35 / +58 / -67 | -92 | 89 | worse |
| lookback 7 bars (14 min), slope >= 0.394 | 506 | +309 | +75 | +1.1 | +4 / +43 / +28 | -11 | 70 | promising |
| lookback 7 bars (14 min), slope >= 0.438 | 447 | +272 | +39 | +0.6 | -15 / +51 / +2 | -23 | 61 | noise |
| lookback 7 bars (14 min), slope >= 0.481 | 387 | +253 | +19 | +0.3 | -23 / +26 / +16 | -16 | 61 | noise |
| lookback 7 bars (14 min), slope >= 0.525 | 332 | +229 | -5 | -0.1 | -9 / +6 / -3 | -9 | 52 | worse |
| lookback 7 bars (14 min), slope >= 0.591 | 252 | +215 | -19 | -0.2 | -45 / +6 / +20 | +37 | 32 | worse |


## MGC 2m: slope lookback (base = 12 bars, slope 0.42)

Base: 863 trades, net +329, avg +0.38, thirds +170 / +126 / +33, last 4 wk -24, max DD 93

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (6 min), slope >= 0.084 | 910 | +451 | +122 | +0.9 | -13 / +82 / +53 | +43 | 56 | noise |
| lookback 3 bars (6 min), slope >= 0.095 | 856 | +449 | +120 | +0.9 | -31 / +80 / +71 | +50 | 56 | noise |
| lookback 3 bars (6 min), slope >= 0.105 | 805 | +548 | +220 | +1.7 | +8 / +98 / +113 | +86 | 48 | promising |
| lookback 3 bars (6 min), slope >= 0.116 | 753 | +595 | +266 | +2.1 | +6 / +137 / +124 | +83 | 47 | robust |
| lookback 3 bars (6 min), slope >= 0.126 | 707 | +615 | +287 | +2.4 | +37 / +143 / +107 | +72 | 39 | robust |
| lookback 3 bars (6 min), slope >= 0.142 | 646 | +673 | +344 | +2.9 | +68 / +150 / +126 | +84 | 43 | robust |
| lookback 4 bars (8 min), slope >= 0.112 | 915 | +655 | +327 | +2.8 | +59 / +190 / +78 | +87 | 46 | robust |
| lookback 4 bars (8 min), slope >= 0.126 | 853 | +667 | +339 | +3.0 | +69 / +204 / +66 | +78 | 43 | robust |
| lookback 4 bars (8 min), slope >= 0.140 | 791 | +737 | +409 | +3.7 | +100 / +213 / +96 | +88 | 43 | robust |
| lookback 4 bars (8 min), slope >= 0.154 | 728 | +707 | +378 | +3.5 | +125 / +182 / +71 | +63 | 42 | robust |
| lookback 4 bars (8 min), slope >= 0.168 | 679 | +685 | +356 | +3.3 | +122 / +153 / +82 | +60 | 44 | robust |
| lookback 4 bars (8 min), slope >= 0.189 | 605 | +685 | +356 | +3.3 | +152 / +155 / +49 | +30 | 41 | robust |
| lookback 5 bars (10 min), slope >= 0.140 | 1033 | +654 | +326 | +3.1 | +116 / +182 / +27 | +42 | 62 | robust |
| lookback 5 bars (10 min), slope >= 0.158 | 937 | +596 | +268 | +2.7 | +150 / +126 / -8 | -2 | 89 | noise |
| lookback 5 bars (10 min), slope >= 0.175 | 852 | +659 | +331 | +3.5 | +179 / +132 / +19 | +1 | 91 | robust |
| lookback 5 bars (10 min), slope >= 0.193 | 775 | +652 | +323 | +3.4 | +158 / +137 / +28 | +14 | 83 | robust |
| lookback 5 bars (10 min), slope >= 0.210 | 702 | +593 | +264 | +2.8 | +126 / +131 / +8 | +2 | 72 | robust |
| lookback 5 bars (10 min), slope >= 0.236 | 613 | +562 | +233 | +2.4 | +88 / +130 / +14 | +8 | 64 | robust |
| lookback 6 bars (12 min), slope >= 0.168 | 1000 | +590 | +261 | +2.7 | +164 / +122 / -25 | -20 | 96 | noise |
| lookback 6 bars (12 min), slope >= 0.189 | 912 | +619 | +290 | +3.1 | +180 / +126 / -16 | -21 | 97 | noise |
| lookback 6 bars (12 min), slope >= 0.210 | 815 | +590 | +262 | +2.9 | +146 / +147 / -31 | -32 | 108 | noise |
| lookback 6 bars (12 min), slope >= 0.231 | 754 | +534 | +206 | +2.3 | +131 / +116 / -41 | -50 | 116 | noise |
| lookback 6 bars (12 min), slope >= 0.252 | 672 | +622 | +294 | +3.2 | +116 / +158 / +19 | -26 | 92 | robust except last 4 wk |
| lookback 6 bars (12 min), slope >= 0.284 | 579 | +556 | +227 | +2.4 | +83 / +128 / +16 | -17 | 71 | robust except last 4 wk |
| lookback 7 bars (14 min), slope >= 0.196 | 987 | +579 | +250 | +2.8 | +135 / +122 / -8 | -14 | 91 | noise |
| lookback 7 bars (14 min), slope >= 0.221 | 896 | +516 | +187 | +2.2 | +109 / +92 / -14 | -6 | 74 | noise |
| lookback 7 bars (14 min), slope >= 0.245 | 811 | +531 | +203 | +2.4 | +70 / +96 / +38 | +16 | 72 | robust |
| lookback 7 bars (14 min), slope >= 0.270 | 731 | +551 | +222 | +2.7 | +48 / +95 / +78 | +40 | 67 | robust |
| lookback 7 bars (14 min), slope >= 0.294 | 672 | +544 | +215 | +2.5 | +24 / +106 / +86 | +38 | 52 | robust |
| lookback 7 bars (14 min), slope >= 0.331 | 588 | +440 | +111 | +1.2 | -8 / +65 / +54 | +5 | 52 | noise |


## MNQ 2m: slope lookback (base = 12 bars, slope 0.55)

Base: 732 trades, net +3566, avg +4.87, thirds +1397 / +487 / +1681, last 4 wk +733, max DD 844

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (6 min), slope >= 0.110 | 864 | +2166 | -1400 | -0.9 | -506 / +245 / -1139 | -845 | 748 | worse |
| lookback 3 bars (6 min), slope >= 0.124 | 795 | +2832 | -734 | -0.5 | -160 / +186 / -760 | -581 | 779 | worse |
| lookback 3 bars (6 min), slope >= 0.138 | 732 | +3530 | -35 | -0.0 | +72 / +332 / -439 | -394 | 630 | worse |
| lookback 3 bars (6 min), slope >= 0.151 | 687 | +3766 | +200 | +0.1 | +107 / +486 / -393 | -387 | 582 | noise |
| lookback 3 bars (6 min), slope >= 0.165 | 648 | +3644 | +78 | +0.1 | +38 / +450 / -410 | -478 | 572 | noise |
| lookback 3 bars (6 min), slope >= 0.186 | 586 | +3934 | +368 | +0.3 | +290 / +536 / -458 | -597 | 500 | noise |
| lookback 4 bars (8 min), slope >= 0.147 | 837 | +3301 | -265 | -0.2 | -15 / +478 / -728 | -749 | 664 | worse |
| lookback 4 bars (8 min), slope >= 0.165 | 769 | +3716 | +150 | +0.1 | +23 / +528 / -400 | -497 | 641 | noise |
| lookback 4 bars (8 min), slope >= 0.183 | 706 | +4112 | +546 | +0.4 | +432 / +581 / -468 | -591 | 507 | noise |
| lookback 4 bars (8 min), slope >= 0.202 | 627 | +4028 | +462 | +0.4 | -177 / +844 / -204 | -413 | 384 | noise |
| lookback 4 bars (8 min), slope >= 0.220 | 564 | +4115 | +549 | +0.4 | -314 / +1039 / -176 | -350 | 353 | noise |
| lookback 4 bars (8 min), slope >= 0.248 | 480 | +4269 | +704 | +0.6 | +179 / +665 / -141 | -381 | 337 | noise |
| lookback 5 bars (10 min), slope >= 0.183 | 1008 | +5909 | +2343 | +1.7 | +1222 / +877 / +243 | -71 | 913 | promising |
| lookback 5 bars (10 min), slope >= 0.206 | 905 | +5285 | +1719 | +1.3 | +744 / +924 / +50 | -180 | 930 | promising |
| lookback 5 bars (10 min), slope >= 0.229 | 802 | +5832 | +2266 | +1.8 | +686 / +1243 / +337 | +70 | 748 | promising |
| lookback 5 bars (10 min), slope >= 0.252 | 708 | +5883 | +2317 | +2.0 | +954 / +953 / +411 | -35 | 695 | promising |
| lookback 5 bars (10 min), slope >= 0.275 | 616 | +6000 | +2434 | +2.1 | +948 / +996 / +491 | +223 | 678 | robust |
| lookback 5 bars (10 min), slope >= 0.309 | 500 | +4575 | +1009 | +0.9 | +758 / -103 / +353 | +340 | 703 | noise |
| lookback 6 bars (12 min), slope >= 0.220 | 948 | +5202 | +1636 | +1.2 | +781 / +763 / +92 | +66 | 1112 | promising |
| lookback 6 bars (12 min), slope >= 0.248 | 844 | +5515 | +1950 | +1.6 | +1257 / +547 / +146 | -50 | 1068 | promising |
| lookback 6 bars (12 min), slope >= 0.275 | 751 | +5435 | +1870 | +1.6 | +1075 / +643 / +152 | +40 | 1088 | promising |
| lookback 6 bars (12 min), slope >= 0.303 | 656 | +4742 | +1176 | +1.1 | +1052 / +15 / +109 | +214 | 888 | promising |
| lookback 6 bars (12 min), slope >= 0.330 | 580 | +4402 | +836 | +0.8 | +639 / -303 / +500 | +482 | 973 | noise |
| lookback 6 bars (12 min), slope >= 0.371 | 475 | +4378 | +812 | +0.7 | +692 / -79 / +200 | +75 | 557 | noise |
| lookback 7 bars (14 min), slope >= 0.257 | 904 | +5152 | +1586 | +1.4 | +848 / +515 / +224 | +62 | 1122 | promising |
| lookback 7 bars (14 min), slope >= 0.289 | 813 | +5337 | +1771 | +1.7 | +658 / +677 / +436 | +266 | 1062 | promising |
| lookback 7 bars (14 min), slope >= 0.321 | 714 | +5222 | +1656 | +1.7 | +750 / +244 / +662 | +464 | 1053 | promising |
| lookback 7 bars (14 min), slope >= 0.353 | 640 | +5273 | +1707 | +1.8 | +585 / +402 / +719 | +495 | 852 | promising |
| lookback 7 bars (14 min), slope >= 0.385 | 546 | +4515 | +949 | +0.9 | +594 / +633 / -278 | -467 | 596 | noise |
| lookback 7 bars (14 min), slope >= 0.433 | 441 | +4311 | +745 | +0.7 | +376 / +745 / -376 | -529 | 355 | noise |


## M2K 3m: slope lookback (base = 12 bars, slope 0.48)

Base: 365 trades, net +87, avg +0.24, thirds +47 / +26 / +14, last 4 wk +8, max DD 22

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (24 min), slope >= 0.256 | 506 | +84 | -3 | -0.1 | +2 / -19 / +15 | -3 | 34 | worse |
| lookback 8 bars (24 min), slope >= 0.288 | 426 | +120 | +34 | +0.9 | +22 / +2 / +9 | -7 | 22 | noise |
| lookback 8 bars (24 min), slope >= 0.320 | 366 | +104 | +17 | +0.5 | +13 / +5 / -1 | -1 | 22 | noise |
| lookback 8 bars (24 min), slope >= 0.352 | 320 | +92 | +5 | +0.1 | +9 / +1 / -6 | +3 | 22 | noise |
| lookback 8 bars (24 min), slope >= 0.384 | 269 | +89 | +2 | +0.1 | -9 / +21 / -9 | +4 | 22 | noise |
| lookback 8 bars (24 min), slope >= 0.432 | 213 | +78 | -9 | -0.2 | -8 / +11 / -12 | -2 | 15 | worse |
| lookback 10 bars (30 min), slope >= 0.320 | 506 | +65 | -22 | -0.6 | -5 / -11 / -7 | -3 | 33 | worse |
| lookback 10 bars (30 min), slope >= 0.360 | 440 | +88 | +2 | +0.0 | +12 / +4 / -14 | +0 | 25 | noise |
| lookback 10 bars (30 min), slope >= 0.400 | 387 | +98 | +11 | +0.4 | -12 / +30 / -7 | -2 | 23 | noise |
| lookback 10 bars (30 min), slope >= 0.440 | 331 | +91 | +4 | +0.1 | -2 / +10 / -4 | -3 | 20 | noise |
| lookback 10 bars (30 min), slope >= 0.480 | 281 | +76 | -11 | -0.5 | -10 / +12 / -14 | -4 | 19 | worse |
| lookback 10 bars (30 min), slope >= 0.540 | 210 | +55 | -32 | -0.9 | -27 / +20 / -25 | -7 | 19 | worse |
| lookback 12 bars (36 min), slope >= 0.384 | 484 | +58 | -29 | -0.9 | -2 / -23 / -4 | +1 | 40 | worse |
| lookback 12 bars (36 min), slope >= 0.432 | 427 | +69 | -18 | -0.8 | -11 / -5 / -1 | +0 | 34 | worse |
| lookback 12 bars (36 min), slope >= 0.528 | 310 | +86 | -1 | -0.0 | +1 / +9 / -11 | -2 | 21 | worse |
| lookback 12 bars (36 min), slope >= 0.576 | 265 | +81 | -5 | -0.2 | +4 / +11 / -21 | -4 | 20 | worse |
| lookback 12 bars (36 min), slope >= 0.648 | 210 | +62 | -25 | -0.7 | -17 / +7 / -15 | -2 | 16 | worse |
| lookback 14 bars (42 min), slope >= 0.448 | 472 | +26 | -61 | -2.1 | -20 / -27 / -14 | +2 | 40 | robustly worse |
| lookback 14 bars (42 min), slope >= 0.504 | 408 | +66 | -21 | -0.9 | -21 / +4 / -4 | +3 | 21 | worse |
| lookback 14 bars (42 min), slope >= 0.560 | 353 | +76 | -11 | -0.4 | -13 / +12 / -10 | +1 | 20 | worse |
| lookback 14 bars (42 min), slope >= 0.616 | 308 | +63 | -24 | -0.7 | -8 / +0 / -16 | -2 | 19 | worse |
| lookback 14 bars (42 min), slope >= 0.672 | 272 | +57 | -30 | -0.9 | -25 / +8 / -13 | -6 | 20 | worse |
| lookback 14 bars (42 min), slope >= 0.756 | 210 | +51 | -36 | -0.9 | -20 / -3 / -12 | -13 | 18 | worse |


## MES 3m: slope lookback (base = 12 bars, slope 0.42)

Base: 739 trades, net +809, avg +1.09, thirds +354 / -8 / +462, last 4 wk +217, max DD 142

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (24 min), slope >= 0.224 | 874 | +715 | -94 | -0.6 | +10 / -138 / +35 | +3 | 227 | worse |
| lookback 8 bars (24 min), slope >= 0.252 | 807 | +640 | -169 | -1.1 | -54 / -86 / -29 | -12 | 176 | worse |
| lookback 8 bars (24 min), slope >= 0.280 | 742 | +740 | -69 | -0.5 | -87 / +35 / -17 | -24 | 115 | worse |
| lookback 8 bars (24 min), slope >= 0.308 | 679 | +630 | -179 | -1.2 | -63 / +20 / -135 | -5 | 119 | worse |
| lookback 8 bars (24 min), slope >= 0.336 | 615 | +614 | -195 | -1.2 | -70 / +62 / -187 | -53 | 122 | worse |
| lookback 8 bars (24 min), slope >= 0.378 | 515 | +449 | -360 | -2.2 | -207 / +89 / -242 | -97 | 86 | worse |
| lookback 10 bars (30 min), slope >= 0.280 | 908 | +599 | -210 | -1.3 | -136 / -97 / +24 | -10 | 198 | worse |
| lookback 10 bars (30 min), slope >= 0.315 | 842 | +624 | -185 | -1.3 | -63 / -109 / -13 | +3 | 186 | worse |
| lookback 10 bars (30 min), slope >= 0.350 | 764 | +617 | -192 | -1.5 | -62 / -83 / -47 | -5 | 164 | worse |
| lookback 10 bars (30 min), slope >= 0.385 | 679 | +692 | -117 | -1.0 | -106 / +13 / -24 | -13 | 147 | worse |
| lookback 10 bars (30 min), slope >= 0.420 | 613 | +773 | -36 | -0.3 | -126 / +99 / -9 | -36 | 98 | worse |
| lookback 10 bars (30 min), slope >= 0.473 | 541 | +718 | -91 | -0.7 | -139 / +92 / -44 | -60 | 81 | worse |
| lookback 12 bars (36 min), slope >= 0.336 | 885 | +617 | -191 | -1.5 | +22 / -169 / -44 | +7 | 231 | worse |
| lookback 12 bars (36 min), slope >= 0.378 | 812 | +729 | -80 | -0.9 | +29 / -91 / -18 | +1 | 176 | worse |
| lookback 12 bars (36 min), slope >= 0.462 | 687 | +742 | -67 | -0.8 | -42 / +36 / -62 | -56 | 122 | worse |
| lookback 12 bars (36 min), slope >= 0.504 | 642 | +668 | -140 | -1.3 | -120 / +47 / -68 | -41 | 109 | worse |
| lookback 12 bars (36 min), slope >= 0.567 | 572 | +516 | -293 | -2.1 | -162 / +70 / -202 | -11 | 177 | worse |
| lookback 14 bars (42 min), slope >= 0.392 | 870 | +578 | -231 | -1.9 | -45 / -135 / -52 | -4 | 202 | worse |
| lookback 14 bars (42 min), slope >= 0.441 | 806 | +684 | -124 | -1.1 | -41 / -43 / -40 | -18 | 145 | worse |
| lookback 14 bars (42 min), slope >= 0.490 | 758 | +585 | -224 | -1.8 | -75 / -29 / -121 | -52 | 145 | worse |
| lookback 14 bars (42 min), slope >= 0.539 | 704 | +346 | -463 | -3.4 | -181 / -28 / -254 | -21 | 189 | robustly worse |
| lookback 14 bars (42 min), slope >= 0.588 | 632 | +312 | -496 | -3.3 | -195 / -8 / -294 | -31 | 186 | robustly worse |
| lookback 14 bars (42 min), slope >= 0.661 | 524 | +208 | -601 | -3.6 | -260 / -66 / -275 | -20 | 170 | robustly worse |


## MGC 3m: slope lookback (base = 12 bars, slope 0.3)

Base: 627 trades, net +1164, avg +1.86, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (24 min), slope >= 0.160 | 726 | +1351 | +187 | +0.6 | +210 / +22 / -45 | -5 | 135 | noise |
| lookback 8 bars (24 min), slope >= 0.180 | 686 | +1390 | +227 | +0.8 | +183 / +44 / -0 | +16 | 130 | noise |
| lookback 8 bars (24 min), slope >= 0.200 | 632 | +1319 | +155 | +0.6 | +159 / +1 / -5 | -5 | 103 | noise |
| lookback 8 bars (24 min), slope >= 0.220 | 585 | +1234 | +70 | +0.3 | +172 / -57 / -45 | -25 | 85 | noise |
| lookback 8 bars (24 min), slope >= 0.240 | 546 | +1244 | +81 | +0.3 | +153 / -56 / -16 | -24 | 90 | noise |
| lookback 8 bars (24 min), slope >= 0.270 | 474 | +1271 | +108 | +0.4 | +216 / -70 / -38 | -46 | 84 | noise |
| lookback 10 bars (30 min), slope >= 0.200 | 744 | +1180 | +16 | +0.1 | +52 / -21 / -15 | +22 | 143 | noise |
| lookback 10 bars (30 min), slope >= 0.225 | 697 | +1137 | -27 | -0.1 | +102 / -39 / -91 | -13 | 127 | worse |
| lookback 10 bars (30 min), slope >= 0.250 | 649 | +1141 | -23 | -0.1 | +89 / -37 / -75 | -18 | 122 | worse |
| lookback 10 bars (30 min), slope >= 0.275 | 591 | +1277 | +113 | +0.6 | +138 / +5 / -30 | -7 | 96 | noise |
| lookback 10 bars (30 min), slope >= 0.300 | 550 | +1313 | +149 | +0.8 | +94 / +40 / +15 | +7 | 88 | noise |
| lookback 10 bars (30 min), slope >= 0.338 | 477 | +1272 | +108 | +0.5 | +36 / +113 / -41 | -51 | 94 | noise |
| lookback 12 bars (36 min), slope >= 0.240 | 712 | +968 | -196 | -1.0 | -77 / -56 / -63 | -13 | 154 | worse |
| lookback 12 bars (36 min), slope >= 0.270 | 674 | +1043 | -121 | -0.8 | -40 / -33 / -48 | -2 | 124 | worse |
| lookback 12 bars (36 min), slope >= 0.330 | 576 | +1197 | +33 | +0.2 | +18 / -21 / +37 | +8 | 125 | noise |
| lookback 12 bars (36 min), slope >= 0.360 | 513 | +982 | -181 | -0.9 | -63 / -89 / -29 | -37 | 126 | worse |
| lookback 12 bars (36 min), slope >= 0.405 | 460 | +1027 | -136 | -0.5 | -78 / -55 / -3 | -30 | 114 | worse |
| lookback 14 bars (42 min), slope >= 0.280 | 702 | +968 | -196 | -1.1 | -33 / -75 / -88 | -61 | 155 | worse |
| lookback 14 bars (42 min), slope >= 0.315 | 660 | +1102 | -61 | -0.4 | +2 / -24 / -39 | -45 | 95 | worse |
| lookback 14 bars (42 min), slope >= 0.350 | 603 | +1125 | -38 | -0.2 | +14 / -52 / -1 | -30 | 95 | worse |
| lookback 14 bars (42 min), slope >= 0.385 | 556 | +979 | -184 | -0.8 | -28 / -137 / -20 | -30 | 152 | worse |
| lookback 14 bars (42 min), slope >= 0.420 | 521 | +996 | -168 | -0.7 | -29 / -68 / -71 | -41 | 113 | worse |
| lookback 14 bars (42 min), slope >= 0.473 | 453 | +1095 | -69 | -0.2 | +4 / -19 / -54 | -35 | 88 | worse |


## MNQ 3m: slope lookback (base = 12 bars, slope 0.75)

Base: 443 trades, net +3944, avg +8.90, thirds +1208 / +929 / +1807, last 4 wk +800, max DD 285

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 8 bars (24 min), slope >= 0.400 | 635 | +3668 | -276 | -0.2 | -124 / -57 / -95 | -44 | 293 | worse |
| lookback 8 bars (24 min), slope >= 0.450 | 538 | +3361 | -583 | -0.6 | -365 / +79 / -297 | -370 | 474 | worse |
| lookback 8 bars (24 min), slope >= 0.500 | 446 | +3157 | -786 | -0.8 | -145 / -205 / -437 | -377 | 451 | worse |
| lookback 8 bars (24 min), slope >= 0.550 | 385 | +2914 | -1030 | -1.0 | -211 / -511 / -308 | -412 | 469 | worse |
| lookback 8 bars (24 min), slope >= 0.600 | 326 | +2329 | -1615 | -1.5 | -300 / -393 / -921 | -1003 | 319 | worse |
| lookback 8 bars (24 min), slope >= 0.675 | 250 | +1860 | -2084 | -1.8 | -451 / -489 / -1143 | -1076 | 378 | worse |
| lookback 10 bars (30 min), slope >= 0.500 | 670 | +2497 | -1446 | -1.2 | -497 / -286 / -663 | -329 | 508 | worse |
| lookback 10 bars (30 min), slope >= 0.562 | 564 | +3117 | -827 | -0.8 | -225 / -55 / -547 | -274 | 494 | worse |
| lookback 10 bars (30 min), slope >= 0.625 | 465 | +2521 | -1423 | -1.4 | -192 / +5 / -1236 | -787 | 439 | worse |
| lookback 10 bars (30 min), slope >= 0.688 | 381 | +2971 | -973 | -1.0 | -128 / +38 / -882 | -663 | 314 | worse |
| lookback 10 bars (30 min), slope >= 0.750 | 315 | +2635 | -1309 | -1.6 | -378 / -241 / -690 | -630 | 283 | worse |
| lookback 10 bars (30 min), slope >= 0.844 | 216 | +1974 | -1970 | -1.9 | -738 / -245 / -987 | -932 | 273 | worse |
| lookback 12 bars (36 min), slope >= 0.600 | 648 | +2730 | -1214 | -1.1 | -109 / -463 / -641 | -285 | 622 | worse |
| lookback 12 bars (36 min), slope >= 0.675 | 539 | +3336 | -608 | -0.8 | -36 / -249 / -323 | -135 | 413 | worse |
| lookback 12 bars (36 min), slope >= 0.825 | 375 | +3868 | -76 | -0.1 | -210 / +131 / +2 | +114 | 333 | worse |
| lookback 12 bars (36 min), slope >= 0.900 | 305 | +2488 | -1456 | -1.6 | -337 / +18 / -1136 | -1095 | 376 | worse |
| lookback 12 bars (36 min), slope >= 1.013 | 238 | +1420 | -2523 | -2.3 | -553 / -714 / -1256 | -1031 | 354 | robustly worse |
| lookback 14 bars (42 min), slope >= 0.700 | 604 | +2902 | -1042 | -1.1 | -383 / -341 / -318 | +2 | 519 | worse |
| lookback 14 bars (42 min), slope >= 0.787 | 509 | +3581 | -362 | -0.5 | -84 / -80 / -198 | +94 | 359 | worse |
| lookback 14 bars (42 min), slope >= 0.875 | 445 | +2756 | -1188 | -1.3 | -498 / +145 / -835 | -664 | 381 | worse |
| lookback 14 bars (42 min), slope >= 0.963 | 364 | +2510 | -1434 | -1.4 | -441 / -145 / -848 | -555 | 327 | worse |
| lookback 14 bars (42 min), slope >= 1.050 | 296 | +1703 | -2241 | -2.0 | -343 / -1040 / -858 | -652 | 393 | robustly worse |
| lookback 14 bars (42 min), slope >= 1.181 | 219 | +2001 | -1943 | -1.7 | -514 / -981 / -448 | -556 | 303 | worse |


## M2K 3m: slope lookback (base = 12 bars, slope 0.48)

Base: 365 trades, net +87, avg +0.24, thirds +47 / +26 / +14, last 4 wk +8, max DD 22

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 15 bars (45 min), slope >= 0.480 | 471 | +45 | -42 | -1.4 | -27 / -8 / -7 | +3 | 27 | worse |
| lookback 15 bars (45 min), slope >= 0.540 | 419 | +77 | -9 | -0.3 | -3 / -4 / -2 | +0 | 20 | worse |
| lookback 15 bars (45 min), slope >= 0.600 | 362 | +60 | -27 | -0.9 | -16 / +1 / -12 | -2 | 19 | worse |
| lookback 15 bars (45 min), slope >= 0.660 | 313 | +41 | -46 | -1.6 | -26 / +4 / -23 | -7 | 20 | worse |
| lookback 15 bars (45 min), slope >= 0.720 | 272 | +43 | -44 | -1.4 | -26 / +14 / -32 | -10 | 24 | worse |
| lookback 15 bars (45 min), slope >= 0.810 | 203 | +54 | -33 | -0.9 | -20 / +3 / -15 | -17 | 22 | worse |


## MES 3m: slope lookback (base = 12 bars, slope 0.42)

Base: 739 trades, net +809, avg +1.09, thirds +354 / -8 / +462, last 4 wk +217, max DD 142

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 15 bars (45 min), slope >= 0.420 | 865 | +564 | -244 | -2.0 | -25 / -180 / -39 | -18 | 230 | robustly worse |
| lookback 15 bars (45 min), slope >= 0.473 | 806 | +618 | -190 | -1.6 | -50 / -93 / -48 | -35 | 192 | worse |
| lookback 15 bars (45 min), slope >= 0.525 | 756 | +600 | -209 | -1.8 | -125 / -43 / -41 | -21 | 156 | worse |
| lookback 15 bars (45 min), slope >= 0.578 | 696 | +649 | -159 | -1.3 | -113 / +1 / -47 | -3 | 149 | worse |
| lookback 15 bars (45 min), slope >= 0.630 | 625 | +485 | -324 | -2.4 | -177 / -33 / -114 | -48 | 141 | robustly worse |
| lookback 15 bars (45 min), slope >= 0.709 | 543 | +267 | -542 | -3.6 | -247 / -54 / -241 | -12 | 164 | robustly worse |


## MGC 3m: slope lookback (base = 12 bars, slope 0.3)

Base: 627 trades, net +1164, avg +1.86, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 15 bars (45 min), slope >= 0.300 | 705 | +980 | -184 | -0.9 | -38 / -83 / -63 | -57 | 156 | worse |
| lookback 15 bars (45 min), slope >= 0.338 | 653 | +971 | -193 | -0.9 | -41 / -88 / -64 | -52 | 149 | worse |
| lookback 15 bars (45 min), slope >= 0.375 | 597 | +977 | -187 | -0.8 | -65 / -80 / -42 | -33 | 133 | worse |
| lookback 15 bars (45 min), slope >= 0.413 | 561 | +1022 | -142 | -0.6 | -93 / -26 / -23 | -38 | 121 | worse |
| lookback 15 bars (45 min), slope >= 0.450 | 499 | +1106 | -58 | -0.2 | -29 / +38 / -67 | -41 | 90 | worse |
| lookback 15 bars (45 min), slope >= 0.506 | 433 | +1141 | -23 | -0.1 | -9 / +18 / -32 | -30 | 75 | worse |


## MNQ 3m: slope lookback (base = 12 bars, slope 0.75)

Base: 443 trades, net +3944, avg +8.90, thirds +1208 / +929 / +1807, last 4 wk +800, max DD 285

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 15 bars (45 min), slope >= 0.750 | 640 | +2077 | -1867 | -1.7 | -494 / -508 / -865 | -185 | 685 | worse |
| lookback 15 bars (45 min), slope >= 0.844 | 549 | +2099 | -1845 | -1.9 | -254 / -125 / -1466 | -888 | 534 | worse |
| lookback 15 bars (45 min), slope >= 0.938 | 460 | +2131 | -1813 | -1.9 | -267 / -229 / -1318 | -858 | 410 | worse |
| lookback 15 bars (45 min), slope >= 1.031 | 378 | +2006 | -1938 | -2.1 | -114 / -691 / -1134 | -725 | 389 | robustly worse |
| lookback 15 bars (45 min), slope >= 1.125 | 301 | +2350 | -1593 | -1.6 | -251 / -662 / -680 | -520 | 304 | worse |
| lookback 15 bars (45 min), slope >= 1.266 | 209 | +1516 | -2428 | -2.3 | -786 / -679 / -963 | -878 | 241 | robustly worse |


## M2K 3m: slope lookback (base = 12 bars, slope 0.48)

Base: 365 trades, net +87, avg +0.24, thirds +47 / +26 / +14, last 4 wk +8, max DD 22

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 5 bars (15 min), slope >= 0.160 | 562 | +114 | +27 | +0.6 | +8 / -21 / +41 | -4 | 35 | noise |
| lookback 5 bars (15 min), slope >= 0.180 | 494 | +115 | +29 | +0.6 | +30 / -22 / +20 | +2 | 37 | noise |
| lookback 5 bars (15 min), slope >= 0.200 | 439 | +76 | -11 | -0.3 | +6 / -19 / +2 | -0 | 30 | worse |
| lookback 5 bars (15 min), slope >= 0.220 | 376 | +111 | +24 | +0.6 | +13 / -4 / +14 | +0 | 25 | noise |
| lookback 5 bars (15 min), slope >= 0.240 | 333 | +103 | +16 | +0.4 | +1 / +16 / -2 | -7 | 20 | noise |
| lookback 5 bars (15 min), slope >= 0.270 | 257 | +116 | +29 | +0.7 | +1 / +22 / +6 | -7 | 19 | noise |


## MES 3m: slope lookback (base = 12 bars, slope 0.42)

Base: 739 trades, net +809, avg +1.09, thirds +354 / -8 / +462, last 4 wk +217, max DD 142

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 5 bars (15 min), slope >= 0.140 | 874 | +856 | +47 | +0.3 | +42 / +50 / -45 | -56 | 181 | noise |
| lookback 5 bars (15 min), slope >= 0.158 | 810 | +720 | -89 | -0.5 | -147 / +85 / -27 | -51 | 165 | worse |
| lookback 5 bars (15 min), slope >= 0.175 | 740 | +726 | -83 | -0.5 | -87 / +63 / -59 | -71 | 140 | worse |
| lookback 5 bars (15 min), slope >= 0.193 | 668 | +759 | -50 | -0.3 | -126 / +81 / -5 | -75 | 130 | worse |
| lookback 5 bars (15 min), slope >= 0.210 | 615 | +784 | -25 | -0.1 | -168 / +56 / +87 | -14 | 130 | worse |
| lookback 5 bars (15 min), slope >= 0.236 | 543 | +796 | -13 | -0.1 | -107 / +68 / +25 | -6 | 119 | worse |


## MGC 3m: slope lookback (base = 12 bars, slope 0.3)

Base: 627 trades, net +1164, avg +1.86, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 5 bars (15 min), slope >= 0.100 | 741 | +1291 | +127 | +0.4 | +146 / +24 / -43 | +5 | 135 | noise |
| lookback 5 bars (15 min), slope >= 0.113 | 687 | +1328 | +165 | +0.5 | +126 / +45 / -6 | +26 | 135 | noise |
| lookback 5 bars (15 min), slope >= 0.125 | 641 | +1295 | +131 | +0.4 | +121 / +37 / -26 | -7 | 128 | noise |
| lookback 5 bars (15 min), slope >= 0.138 | 591 | +1363 | +199 | +0.6 | +174 / +30 / -4 | -26 | 124 | noise |
| lookback 5 bars (15 min), slope >= 0.150 | 551 | +1422 | +258 | +0.8 | +234 / +57 / -32 | -74 | 123 | noise |
| lookback 5 bars (15 min), slope >= 0.169 | 463 | +1575 | +411 | +1.3 | +289 / +93 / +29 | -64 | 106 | promising |


## MNQ 3m: slope lookback (base = 12 bars, slope 0.75)

Base: 443 trades, net +3944, avg +8.90, thirds +1208 / +929 / +1807, last 4 wk +800, max DD 285

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 5 bars (15 min), slope >= 0.250 | 755 | +4547 | +603 | +0.4 | +424 / +72 / +107 | -228 | 502 | noise |
| lookback 5 bars (15 min), slope >= 0.281 | 630 | +4067 | +123 | +0.1 | -21 / +259 / -115 | -212 | 351 | noise |
| lookback 5 bars (15 min), slope >= 0.312 | 526 | +4004 | +60 | +0.0 | +230 / +567 / -737 | -793 | 385 | noise |
| lookback 5 bars (15 min), slope >= 0.344 | 452 | +3753 | -191 | -0.2 | +122 / +640 / -954 | -1091 | 355 | worse |
| lookback 5 bars (15 min), slope >= 0.375 | 376 | +3612 | -331 | -0.3 | -58 / +573 / -846 | -963 | 268 | worse |
| lookback 5 bars (15 min), slope >= 0.422 | 256 | +3382 | -562 | -0.5 | +205 / +40 / -807 | -861 | 176 | worse |


## M2K 3m: slope lookback (base = 12 bars, slope 0.48)

Base: 365 trades, net +87, avg +0.24, thirds +47 / +26 / +14, last 4 wk +8, max DD 22

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 2 bars (6 min), slope >= 0.064 | 406 | +60 | -27 | -0.5 | -26 / -31 / +30 | +3 | 42 | worse |
| lookback 2 bars (6 min), slope >= 0.072 | 391 | +68 | -19 | -0.3 | -21 / -35 / +38 | +1 | 40 | worse |
| lookback 2 bars (6 min), slope >= 0.080 | 378 | +82 | -5 | -0.1 | -13 / -33 / +41 | +5 | 40 | worse |
| lookback 2 bars (6 min), slope >= 0.088 | 359 | +102 | +15 | +0.3 | -8 / -22 / +45 | +2 | 36 | noise |
| lookback 2 bars (6 min), slope >= 0.096 | 344 | +111 | +24 | +0.5 | -10 / -3 / +37 | -1 | 29 | noise |
| lookback 2 bars (6 min), slope >= 0.108 | 327 | +124 | +37 | +0.7 | -9 / +8 / +38 | -2 | 26 | noise |
| lookback 3 bars (9 min), slope >= 0.096 | 438 | +112 | +25 | +0.5 | +4 / +4 / +17 | -9 | 23 | noise |
| lookback 3 bars (9 min), slope >= 0.108 | 413 | +134 | +47 | +0.9 | +6 / +17 / +24 | -6 | 23 | noise |
| lookback 3 bars (9 min), slope >= 0.120 | 387 | +130 | +43 | +0.9 | +8 / +18 / +18 | -13 | 21 | noise |
| lookback 3 bars (9 min), slope >= 0.132 | 369 | +138 | +51 | +1.0 | +16 / +21 / +14 | -14 | 21 | promising |
| lookback 3 bars (9 min), slope >= 0.144 | 338 | +156 | +69 | +1.4 | +15 / +25 / +29 | -4 | 21 | promising |
| lookback 3 bars (9 min), slope >= 0.162 | 302 | +162 | +75 | +1.6 | +23 / +26 / +25 | -5 | 21 | promising |
| lookback 4 bars (12 min), slope >= 0.128 | 445 | +152 | +65 | +1.3 | +27 / +15 / +24 | -16 | 27 | promising |
| lookback 4 bars (12 min), slope >= 0.144 | 403 | +163 | +76 | +1.6 | +21 / +21 / +33 | -6 | 21 | promising |
| lookback 4 bars (12 min), slope >= 0.160 | 362 | +176 | +90 | +2.0 | +32 / +21 / +36 | -6 | 21 | promising |
| lookback 4 bars (12 min), slope >= 0.176 | 327 | +171 | +84 | +1.9 | +46 / +15 / +23 | -11 | 21 | promising |
| lookback 4 bars (12 min), slope >= 0.192 | 294 | +175 | +88 | +2.0 | +45 / +28 / +15 | -11 | 15 | robust except last 4 wk |
| lookback 4 bars (12 min), slope >= 0.216 | 249 | +160 | +73 | +1.7 | +26 / +35 / +12 | -7 | 12 | promising |


## MES 3m: slope lookback (base = 12 bars, slope 0.42)

Base: 739 trades, net +809, avg +1.09, thirds +354 / -8 / +462, last 4 wk +217, max DD 142

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 2 bars (6 min), slope >= 0.056 | 608 | +141 | -668 | -2.9 | -140 / -117 / -411 | -95 | 269 | robustly worse |
| lookback 2 bars (6 min), slope >= 0.063 | 583 | +184 | -625 | -2.7 | -131 / -84 / -410 | -96 | 236 | robustly worse |
| lookback 2 bars (6 min), slope >= 0.070 | 562 | +248 | -561 | -2.4 | -102 / -79 / -380 | -64 | 208 | robustly worse |
| lookback 2 bars (6 min), slope >= 0.077 | 541 | +313 | -496 | -2.2 | -83 / -52 / -361 | -55 | 178 | robustly worse |
| lookback 2 bars (6 min), slope >= 0.084 | 522 | +407 | -402 | -1.8 | -63 / -29 / -310 | -32 | 155 | worse |
| lookback 2 bars (6 min), slope >= 0.095 | 500 | +441 | -367 | -1.6 | -67 / +3 / -304 | -28 | 133 | worse |
| lookback 3 bars (9 min), slope >= 0.084 | 711 | +387 | -421 | -1.9 | -80 / -54 / -288 | -54 | 197 | worse |
| lookback 3 bars (9 min), slope >= 0.095 | 674 | +462 | -347 | -1.6 | -53 / +4 / -298 | -56 | 149 | worse |
| lookback 3 bars (9 min), slope >= 0.105 | 648 | +444 | -365 | -1.7 | -84 / +14 / -295 | -65 | 152 | worse |
| lookback 3 bars (9 min), slope >= 0.116 | 609 | +571 | -238 | -1.1 | -32 / +66 / -272 | -54 | 114 | worse |
| lookback 3 bars (9 min), slope >= 0.126 | 581 | +606 | -203 | -1.0 | -54 / +111 / -260 | -39 | 76 | worse |
| lookback 3 bars (9 min), slope >= 0.142 | 523 | +541 | -268 | -1.3 | -67 / +68 / -269 | -46 | 88 | worse |
| lookback 4 bars (12 min), slope >= 0.112 | 753 | +524 | -285 | -1.4 | +35 / -2 / -318 | -109 | 165 | worse |
| lookback 4 bars (12 min), slope >= 0.126 | 708 | +586 | -223 | -1.1 | +17 / +68 / -307 | -103 | 98 | worse |
| lookback 4 bars (12 min), slope >= 0.140 | 645 | +564 | -245 | -1.2 | +33 / +44 / -323 | -108 | 95 | worse |
| lookback 4 bars (12 min), slope >= 0.154 | 602 | +508 | -300 | -1.6 | -16 / +84 / -369 | -115 | 88 | worse |
| lookback 4 bars (12 min), slope >= 0.168 | 557 | +511 | -297 | -1.5 | -46 / +89 / -340 | -104 | 94 | worse |
| lookback 4 bars (12 min), slope >= 0.189 | 481 | +513 | -296 | -1.5 | -69 / +124 / -351 | -136 | 69 | worse |


## MGC 3m: slope lookback (base = 12 bars, slope 0.3)

Base: 627 trades, net +1164, avg +1.86, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 2 bars (6 min), slope >= 0.040 | 513 | +954 | -210 | -0.5 | +119 / +0 / -329 | -101 | 129 | worse |
| lookback 2 bars (6 min), slope >= 0.045 | 503 | +964 | -199 | -0.5 | +125 / -7 / -317 | -108 | 129 | worse |
| lookback 2 bars (6 min), slope >= 0.050 | 485 | +983 | -181 | -0.5 | +132 / -19 / -294 | -102 | 129 | worse |
| lookback 2 bars (6 min), slope >= 0.055 | 469 | +1029 | -134 | -0.4 | +149 / -6 / -278 | -108 | 121 | worse |
| lookback 2 bars (6 min), slope >= 0.060 | 461 | +1053 | -111 | -0.3 | +157 / +4 / -272 | -108 | 121 | worse |
| lookback 2 bars (6 min), slope >= 0.068 | 442 | +1120 | -44 | -0.1 | +173 / +24 / -240 | -108 | 105 | worse |
| lookback 3 bars (9 min), slope >= 0.060 | 633 | +1178 | +14 | +0.0 | +147 / -28 / -105 | +7 | 113 | noise |
| lookback 3 bars (9 min), slope >= 0.068 | 601 | +1262 | +99 | +0.3 | +168 / +6 / -75 | -9 | 101 | noise |
| lookback 3 bars (9 min), slope >= 0.075 | 586 | +1283 | +120 | +0.3 | +171 / +26 / -77 | -6 | 96 | noise |
| lookback 3 bars (9 min), slope >= 0.083 | 557 | +1351 | +187 | +0.5 | +229 / +41 / -82 | -10 | 81 | noise |
| lookback 3 bars (9 min), slope >= 0.090 | 538 | +1345 | +181 | +0.5 | +248 / +27 / -94 | -20 | 82 | noise |
| lookback 3 bars (9 min), slope >= 0.101 | 515 | +1374 | +210 | +0.6 | +272 / +13 / -75 | -12 | 68 | noise |
| lookback 4 bars (12 min), slope >= 0.080 | 658 | +1241 | +77 | +0.2 | +177 / -14 / -85 | +31 | 103 | noise |
| lookback 4 bars (12 min), slope >= 0.090 | 623 | +1236 | +73 | +0.2 | +212 / -27 / -113 | +12 | 102 | noise |
| lookback 4 bars (12 min), slope >= 0.100 | 597 | +1265 | +101 | +0.3 | +235 / -36 / -99 | +18 | 103 | noise |
| lookback 4 bars (12 min), slope >= 0.110 | 562 | +1304 | +141 | +0.4 | +257 / -48 / -68 | +33 | 96 | noise |
| lookback 4 bars (12 min), slope >= 0.120 | 526 | +1345 | +181 | +0.5 | +255 / +14 / -87 | -3 | 87 | noise |
| lookback 4 bars (12 min), slope >= 0.135 | 466 | +1394 | +230 | +0.7 | +282 / +5 / -57 | -26 | 82 | noise |


## MNQ 3m: slope lookback (base = 12 bars, slope 0.75)

Base: 443 trades, net +3944, avg +8.90, thirds +1208 / +929 / +1807, last 4 wk +800, max DD 285

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 2 bars (6 min), slope >= 0.100 | 581 | +3077 | -867 | -0.6 | +260 / -352 / -775 | -1010 | 821 | worse |
| lookback 2 bars (6 min), slope >= 0.113 | 554 | +3518 | -426 | -0.3 | +307 / -350 / -383 | -755 | 614 | worse |
| lookback 2 bars (6 min), slope >= 0.125 | 525 | +3752 | -192 | -0.1 | +290 / -234 / -248 | -543 | 547 | worse |
| lookback 2 bars (6 min), slope >= 0.138 | 496 | +3995 | +51 | +0.0 | +309 / -189 / -70 | -464 | 477 | noise |
| lookback 2 bars (6 min), slope >= 0.150 | 467 | +3661 | -283 | -0.2 | -52 / -45 / -186 | -622 | 441 | worse |
| lookback 2 bars (6 min), slope >= 0.169 | 427 | +3573 | -371 | -0.3 | +19 / -262 / -127 | -631 | 395 | worse |
| lookback 3 bars (9 min), slope >= 0.150 | 627 | +3720 | -224 | -0.1 | -3 / -282 / +61 | -387 | 532 | worse |
| lookback 3 bars (9 min), slope >= 0.169 | 577 | +3950 | +6 | +0.0 | +129 / -381 / +258 | -294 | 571 | noise |
| lookback 3 bars (9 min), slope >= 0.188 | 526 | +3798 | -145 | -0.1 | -263 / -182 / +300 | -247 | 498 | worse |
| lookback 3 bars (9 min), slope >= 0.206 | 472 | +3413 | -531 | -0.4 | -197 / -105 / -229 | -739 | 457 | worse |
| lookback 3 bars (9 min), slope >= 0.225 | 431 | +3625 | -319 | -0.2 | -172 / -173 / +26 | -635 | 434 | worse |
| lookback 3 bars (9 min), slope >= 0.253 | 376 | +4036 | +92 | +0.1 | -34 / +29 / +97 | -519 | 362 | noise |
| lookback 4 bars (12 min), slope >= 0.200 | 579 | +5052 | +1108 | +0.8 | +280 / -49 / +877 | +128 | 499 | noise |
| lookback 4 bars (12 min), slope >= 0.225 | 507 | +4925 | +981 | +0.7 | +4 / -39 / +1016 | +153 | 437 | noise |
| lookback 4 bars (12 min), slope >= 0.250 | 447 | +4637 | +693 | +0.5 | +144 / +194 / +354 | -412 | 334 | noise |
| lookback 4 bars (12 min), slope >= 0.275 | 380 | +3890 | -54 | -0.0 | -176 / +157 / -35 | -548 | 293 | worse |
| lookback 4 bars (12 min), slope >= 0.300 | 332 | +4102 | +159 | +0.1 | -93 / +250 / +2 | -517 | 293 | noise |
| lookback 4 bars (12 min), slope >= 0.338 | 271 | +3660 | -284 | -0.2 | -98 / +195 / -381 | -952 | 321 | worse |


## M2K 5m: slope lookback (base = 12 bars, slope 1.0)

Base: 216 trades, net +86, avg +0.40, thirds +42 / +1 / +43, last 4 wk -7, max DD 36

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 6 bars (30 min), slope >= 0.400 | 342 | +262 | +176 | +3.0 | +17 / +108 / +51 | +12 | 21 | robust |
| lookback 6 bars (30 min), slope >= 0.450 | 256 | +265 | +179 | +3.6 | +35 / +101 / +42 | +8 | 17 | robust |
| lookback 6 bars (30 min), slope >= 0.500 | 204 | +189 | +103 | +2.2 | +4 / +67 / +32 | +2 | 16 | robust |
| lookback 6 bars (30 min), slope >= 0.550 | 153 | +141 | +55 | +1.3 | +10 / +51 / -6 | +4 | 18 | noise |
| lookback 6 bars (30 min), slope >= 0.600 | 133 | +132 | +46 | +1.1 | +14 / +32 / +0 | +3 | 15 | promising |
| lookback 6 bars (30 min), slope >= 0.675 | 98 | +112 | +26 | +0.6 | +19 / +26 / -19 | -1 | 19 | noise |
| lookback 7 bars (35 min), slope >= 0.467 | 337 | +187 | +101 | +2.1 | +13 / +76 / +13 | +11 | 33 | robust |
| lookback 7 bars (35 min), slope >= 0.525 | 269 | +119 | +33 | +0.8 | +15 / +28 / -11 | +2 | 34 | noise |
| lookback 7 bars (35 min), slope >= 0.583 | 216 | +120 | +34 | +0.9 | +11 / +26 / -4 | +1 | 30 | noise |
| lookback 7 bars (35 min), slope >= 0.642 | 176 | +135 | +48 | +1.4 | +14 / +23 / +11 | -1 | 23 | promising |
| lookback 7 bars (35 min), slope >= 0.700 | 143 | +103 | +17 | +0.5 | -1 / +20 / -2 | -4 | 23 | noise |
| lookback 7 bars (35 min), slope >= 0.788 | 109 | +111 | +25 | +0.6 | +4 / +27 / -5 | -1 | 13 | noise |
| lookback 8 bars (40 min), slope >= 0.533 | 348 | +123 | +37 | +0.7 | -1 / +30 / +8 | +1 | 28 | noise |
| lookback 8 bars (40 min), slope >= 0.600 | 285 | +139 | +53 | +1.1 | +1 / +28 / +25 | +2 | 24 | promising |
| lookback 8 bars (40 min), slope >= 0.667 | 233 | +132 | +46 | +1.1 | +7 / +22 / +17 | -1 | 22 | promising |
| lookback 8 bars (40 min), slope >= 0.733 | 188 | +123 | +37 | +0.8 | +6 / +27 / +4 | -6 | 19 | noise |
| lookback 8 bars (40 min), slope >= 0.800 | 152 | +115 | +28 | +0.6 | +5 / +28 / -4 | +1 | 19 | noise |
| lookback 8 bars (40 min), slope >= 0.900 | 106 | +106 | +20 | +0.4 | -11 / +27 / +4 | +1 | 16 | noise |
| lookback 12 bars (60 min), slope >= 0.800 | 358 | +55 | -31 | -0.6 | -10 / +10 / -31 | -12 | 32 | worse |
| lookback 12 bars (60 min), slope >= 0.900 | 273 | +73 | -13 | -0.4 | -8 / +4 / -9 | -0 | 31 | worse |
| lookback 12 bars (60 min), slope >= 1.100 | 160 | +90 | +4 | +0.1 | +6 / +9 / -10 | +3 | 37 | noise |
| lookback 12 bars (60 min), slope >= 1.200 | 129 | +84 | -3 | -0.1 | -1 / +23 / -24 | -2 | 20 | worse |
| lookback 12 bars (60 min), slope >= 1.350 | 93 | +59 | -28 | -0.6 | -26 / +21 / -23 | -5 | 19 | worse |


## MES 5m: slope lookback (base = 12 bars, slope 0.7)

Base: 228 trades, net +248, avg +1.09, thirds +54 / +99 / +96, last 4 wk +17, max DD 46

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 6 bars (30 min), slope >= 0.280 | 365 | +298 | +49 | +0.6 | +61 / +18 / -29 | -48 | 52 | noise |
| lookback 6 bars (30 min), slope >= 0.315 | 283 | +327 | +79 | +1.0 | +61 / +22 / -4 | -39 | 45 | noise |
| lookback 6 bars (30 min), slope >= 0.350 | 218 | +272 | +24 | +0.3 | +38 / -3 / -11 | -12 | 36 | noise |
| lookback 6 bars (30 min), slope >= 0.385 | 186 | +277 | +28 | +0.4 | +38 / -5 / -5 | -6 | 27 | noise |
| lookback 6 bars (30 min), slope >= 0.420 | 149 | +240 | -9 | -0.1 | +34 / -4 / -39 | +9 | 19 | worse |
| lookback 6 bars (30 min), slope >= 0.472 | 111 | +231 | -17 | -0.2 | +53 / -2 / -67 | -9 | 24 | worse |
| lookback 7 bars (35 min), slope >= 0.327 | 360 | +321 | +72 | +1.0 | +34 / +67 / -29 | -37 | 49 | noise |
| lookback 7 bars (35 min), slope >= 0.367 | 294 | +376 | +128 | +2.0 | +72 / +52 / +3 | -27 | 43 | robust except last 4 wk |
| lookback 7 bars (35 min), slope >= 0.408 | 237 | +312 | +64 | +1.1 | +33 / +35 / -4 | -13 | 36 | noise |
| lookback 7 bars (35 min), slope >= 0.449 | 192 | +351 | +103 | +1.8 | +58 / +48 / -2 | -2 | 24 | noise |
| lookback 7 bars (35 min), slope >= 0.490 | 152 | +319 | +70 | +1.2 | +33 / +41 / -3 | -3 | 28 | noise |
| lookback 7 bars (35 min), slope >= 0.551 | 109 | +203 | -45 | -0.7 | +7 / -16 / -36 | -8 | 26 | worse |
| lookback 8 bars (40 min), slope >= 0.373 | 361 | +378 | +130 | +1.7 | +37 / +29 / +64 | +13 | 41 | promising |
| lookback 8 bars (40 min), slope >= 0.420 | 295 | +312 | +64 | +0.9 | +9 / +23 / +32 | +17 | 40 | noise |
| lookback 8 bars (40 min), slope >= 0.467 | 239 | +312 | +64 | +0.9 | +6 / +43 / +14 | +14 | 31 | noise |
| lookback 8 bars (40 min), slope >= 0.513 | 192 | +207 | -41 | -0.6 | -16 / +1 / -26 | -14 | 31 | worse |
| lookback 8 bars (40 min), slope >= 0.560 | 154 | +197 | -51 | -0.7 | -27 / -5 / -19 | -15 | 32 | worse |
| lookback 8 bars (40 min), slope >= 0.630 | 106 | +156 | -93 | -1.3 | -24 / -25 / -44 | -6 | 23 | worse |
| lookback 12 bars (60 min), slope >= 0.560 | 383 | +208 | -40 | -0.5 | +17 / -75 / +17 | -18 | 64 | worse |
| lookback 12 bars (60 min), slope >= 0.630 | 303 | +171 | -78 | -1.5 | -21 / -42 / -15 | -5 | 41 | worse |
| lookback 12 bars (60 min), slope >= 0.770 | 175 | +222 | -26 | -0.6 | +0 / -9 / -17 | -4 | 42 | worse |
| lookback 12 bars (60 min), slope >= 0.840 | 126 | +211 | -37 | -0.6 | -7 / -15 / -16 | -3 | 33 | worse |
| lookback 12 bars (60 min), slope >= 0.945 | 82 | +137 | -112 | -1.6 | -29 / -44 / -39 | +4 | 24 | worse |


## MGC 5m: slope lookback (base = 12 bars, slope 0.48)

Base: 624 trades, net +672, avg +1.08, thirds +199 / +234 / +239, last 4 wk +12, max DD 94

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 6 bars (30 min), slope >= 0.192 | 799 | +868 | +196 | +1.5 | +90 / +94 / +13 | -23 | 87 | promising |
| lookback 6 bars (30 min), slope >= 0.216 | 729 | +951 | +279 | +2.2 | +117 / +133 / +29 | -23 | 74 | robust except last 4 wk |
| lookback 6 bars (30 min), slope >= 0.240 | 656 | +1001 | +329 | +2.8 | +111 / +196 / +22 | -20 | 66 | robust except last 4 wk |
| lookback 6 bars (30 min), slope >= 0.264 | 577 | +1025 | +353 | +3.0 | +158 / +163 / +32 | +5 | 49 | robust |
| lookback 6 bars (30 min), slope >= 0.288 | 502 | +874 | +202 | +1.8 | +87 / +100 / +15 | +14 | 62 | promising |
| lookback 6 bars (30 min), slope >= 0.324 | 423 | +783 | +111 | +0.9 | +46 / +80 / -15 | -8 | 43 | noise |
| lookback 7 bars (35 min), slope >= 0.224 | 787 | +913 | +241 | +2.0 | +113 / +149 / -20 | -19 | 78 | noise |
| lookback 7 bars (35 min), slope >= 0.252 | 696 | +848 | +176 | +1.6 | +32 / +140 / +3 | -24 | 70 | promising |
| lookback 7 bars (35 min), slope >= 0.280 | 613 | +841 | +169 | +1.7 | +64 / +111 / -6 | +10 | 67 | noise |
| lookback 7 bars (35 min), slope >= 0.308 | 550 | +763 | +91 | +0.9 | +13 / +116 / -38 | -20 | 59 | noise |
| lookback 7 bars (35 min), slope >= 0.336 | 499 | +737 | +65 | +0.6 | +18 / +118 / -71 | -18 | 52 | noise |
| lookback 7 bars (35 min), slope >= 0.378 | 416 | +674 | +2 | +0.0 | +62 / +51 / -110 | -25 | 44 | noise |
| lookback 8 bars (40 min), slope >= 0.256 | 774 | +811 | +139 | +1.1 | +27 / +118 / -7 | -10 | 80 | noise |
| lookback 8 bars (40 min), slope >= 0.288 | 698 | +758 | +86 | +0.8 | +16 / +76 / -5 | -9 | 67 | noise |
| lookback 8 bars (40 min), slope >= 0.320 | 626 | +780 | +108 | +1.0 | +2 / +133 / -27 | -26 | 76 | noise |
| lookback 8 bars (40 min), slope >= 0.352 | 564 | +630 | -42 | -0.4 | -34 / +61 / -70 | -39 | 78 | worse |
| lookback 8 bars (40 min), slope >= 0.384 | 495 | +647 | -25 | -0.2 | +15 / +42 / -82 | -50 | 73 | worse |
| lookback 8 bars (40 min), slope >= 0.432 | 406 | +663 | -9 | -0.1 | +19 / -3 / -25 | +3 | 48 | worse |
| lookback 12 bars (60 min), slope >= 0.384 | 774 | +611 | -61 | -0.6 | -94 / +54 / -20 | +17 | 148 | worse |
| lookback 12 bars (60 min), slope >= 0.432 | 707 | +697 | +25 | +0.3 | +6 / +31 / -13 | +2 | 85 | noise |
| lookback 12 bars (60 min), slope >= 0.528 | 550 | +599 | -73 | -1.1 | -56 / +38 / -54 | -33 | 86 | worse |
| lookback 12 bars (60 min), slope >= 0.576 | 486 | +455 | -217 | -2.4 | -89 / -0 / -128 | -34 | 82 | robustly worse |
| lookback 12 bars (60 min), slope >= 0.648 | 415 | +423 | -249 | -2.2 | -91 / -44 / -114 | -33 | 85 | robustly worse |


## MNQ 5m: slope lookback (base = 12 bars, slope off)

Base: 1484 trades, net +2033, avg +1.37, thirds +615 / +913 / +505, last 4 wk +491, max DD 777

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 6 bars (30 min), slope >= 0.220 | 697 | +4545 | +2511 | +2.6 | +1151 / +641 / +720 | -52 | 334 | robust except last 4 wk |
| lookback 6 bars (30 min), slope >= 0.248 | 592 | +3770 | +1737 | +1.7 | +999 / +421 / +317 | -367 | 262 | promising |
| lookback 6 bars (30 min), slope >= 0.275 | 517 | +3651 | +1617 | +1.5 | +1185 / +270 / +162 | -338 | 225 | promising |
| lookback 6 bars (30 min), slope >= 0.303 | 454 | +3483 | +1449 | +1.4 | +1021 / +216 / +212 | -247 | 219 | promising |
| lookback 6 bars (30 min), slope >= 0.330 | 381 | +3277 | +1243 | +1.1 | +967 / +126 / +150 | -284 | 255 | promising |
| lookback 6 bars (30 min), slope >= 0.371 | 310 | +2622 | +589 | +0.5 | +565 / -81 / +106 | -352 | 192 | noise |
| lookback 7 bars (35 min), slope >= 0.257 | 667 | +3867 | +1833 | +1.8 | +1270 / +274 / +289 | -311 | 318 | promising |
| lookback 7 bars (35 min), slope >= 0.289 | 578 | +3589 | +1556 | +1.5 | +1151 / +106 / +299 | -325 | 318 | promising |
| lookback 7 bars (35 min), slope >= 0.321 | 519 | +3250 | +1216 | +1.1 | +901 / +91 / +224 | -302 | 230 | promising |
| lookback 7 bars (35 min), slope >= 0.353 | 443 | +3251 | +1217 | +1.1 | +838 / -52 / +432 | -202 | 250 | noise |
| lookback 7 bars (35 min), slope >= 0.385 | 395 | +2452 | +419 | +0.4 | +508 / -285 / +196 | -360 | 281 | noise |
| lookback 7 bars (35 min), slope >= 0.433 | 304 | +2074 | +40 | +0.0 | +273 / -479 / +246 | -432 | 216 | noise |
| lookback 8 bars (40 min), slope >= 0.293 | 665 | +3585 | +1551 | +1.6 | +953 / +394 / +205 | -401 | 273 | promising |
| lookback 8 bars (40 min), slope >= 0.330 | 583 | +3233 | +1200 | +1.1 | +800 / +164 / +237 | -370 | 276 | promising |
| lookback 8 bars (40 min), slope >= 0.367 | 521 | +3092 | +1058 | +1.0 | +708 / +37 / +313 | -391 | 269 | noise |
| lookback 8 bars (40 min), slope >= 0.403 | 460 | +2354 | +320 | +0.3 | +150 / -62 / +233 | -478 | 292 | noise |
| lookback 8 bars (40 min), slope >= 0.440 | 380 | +2114 | +81 | +0.1 | +265 / -489 / +305 | -499 | 272 | noise |
| lookback 8 bars (40 min), slope >= 0.495 | 304 | +1774 | -260 | -0.2 | -84 / -471 / +296 | -270 | 260 | worse |
| lookback 12 bars (60 min), slope >= 0.440 | 692 | +2553 | +519 | +0.5 | +842 / -264 / -59 | -408 | 300 | noise |
| lookback 12 bars (60 min), slope >= 0.495 | 610 | +2631 | +598 | +0.6 | +807 / -192 / -18 | -335 | 346 | noise |
| lookback 12 bars (60 min), slope >= 0.550 | 541 | +2345 | +311 | +0.3 | +516 / -90 / -115 | -337 | 353 | noise |
| lookback 12 bars (60 min), slope >= 0.605 | 452 | +2036 | +3 | +0.0 | +362 / -357 / -2 | -319 | 446 | noise |
| lookback 12 bars (60 min), slope >= 0.660 | 388 | +2345 | +312 | +0.3 | +582 / -479 / +209 | -286 | 384 | noise |
| lookback 12 bars (60 min), slope >= 0.743 | 322 | +1693 | -341 | -0.3 | +180 / -488 / -32 | -336 | 384 | worse |


## M2K 5m: slope lookback (base = 12 bars, slope 1.0)

Base: 216 trades, net +86, avg +0.40, thirds +42 / +1 / +43, last 4 wk -7, max DD 36

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 9 bars (45 min), slope >= 0.600 | 343 | +132 | +46 | +0.9 | -21 / +38 / +30 | +5 | 34 | noise |
| lookback 9 bars (45 min), slope >= 0.675 | 281 | +144 | +58 | +1.2 | -8 / +41 / +25 | +6 | 30 | noise |
| lookback 9 bars (45 min), slope >= 0.750 | 222 | +145 | +59 | +1.2 | +12 / +28 / +19 | +3 | 18 | promising |
| lookback 9 bars (45 min), slope >= 0.825 | 168 | +158 | +72 | +1.6 | +32 / +26 / +14 | +1 | 15 | promising |
| lookback 9 bars (45 min), slope >= 0.900 | 127 | +127 | +41 | +0.9 | -12 / +25 / +28 | +8 | 15 | noise |
| lookback 9 bars (45 min), slope >= 1.013 | 93 | +97 | +11 | +0.2 | -45 / +32 / +24 | +3 | 23 | noise |


## MES 5m: slope lookback (base = 12 bars, slope 0.7)

Base: 228 trades, net +248, avg +1.09, thirds +54 / +99 / +96, last 4 wk +17, max DD 46

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 9 bars (45 min), slope >= 0.420 | 380 | +358 | +110 | +1.3 | -0 / +36 / +75 | +20 | 47 | noise |
| lookback 9 bars (45 min), slope >= 0.473 | 298 | +334 | +86 | +1.1 | -18 / +23 / +80 | +22 | 48 | noise |
| lookback 9 bars (45 min), slope >= 0.525 | 238 | +232 | -16 | -0.2 | -36 / -15 / +35 | +13 | 55 | worse |
| lookback 9 bars (45 min), slope >= 0.578 | 177 | +232 | -17 | -0.2 | -30 / -2 / +15 | -7 | 44 | worse |
| lookback 9 bars (45 min), slope >= 0.630 | 137 | +175 | -73 | -1.1 | -29 / -20 / -24 | -11 | 31 | worse |
| lookback 9 bars (45 min), slope >= 0.709 | 90 | +192 | -56 | -0.8 | +19 / -54 / -22 | -12 | 23 | worse |


## MGC 5m: slope lookback (base = 12 bars, slope 0.48)

Base: 624 trades, net +672, avg +1.08, thirds +199 / +234 / +239, last 4 wk +12, max DD 94

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 9 bars (45 min), slope >= 0.288 | 772 | +708 | +37 | +0.3 | -4 / +42 / -2 | -6 | 95 | noise |
| lookback 9 bars (45 min), slope >= 0.324 | 691 | +706 | +35 | +0.3 | -15 / +96 / -46 | -29 | 103 | noise |
| lookback 9 bars (45 min), slope >= 0.360 | 628 | +619 | -53 | -0.5 | -29 / +15 / -38 | -29 | 71 | worse |
| lookback 9 bars (45 min), slope >= 0.396 | 543 | +692 | +20 | +0.2 | +16 / +26 / -22 | -9 | 68 | noise |
| lookback 9 bars (45 min), slope >= 0.432 | 480 | +710 | +38 | +0.3 | +31 / +24 / -18 | +12 | 60 | noise |
| lookback 9 bars (45 min), slope >= 0.486 | 394 | +684 | +12 | +0.1 | +25 / +1 / -14 | +20 | 61 | noise |


## MNQ 5m: slope lookback (base = 12 bars, slope off)

Base: 1484 trades, net +2033, avg +1.37, thirds +615 / +913 / +505, last 4 wk +491, max DD 777

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 9 bars (45 min), slope >= 0.330 | 668 | +3380 | +1346 | +1.3 | +751 / +306 / +289 | -261 | 338 | promising |
| lookback 9 bars (45 min), slope >= 0.371 | 608 | +3008 | +974 | +0.9 | +397 / +244 / +333 | -314 | 363 | noise |
| lookback 9 bars (45 min), slope >= 0.413 | 523 | +2538 | +505 | +0.5 | +238 / -29 / +295 | -431 | 276 | noise |
| lookback 9 bars (45 min), slope >= 0.454 | 442 | +2688 | +655 | +0.6 | +340 / -9 / +324 | -473 | 227 | noise |
| lookback 9 bars (45 min), slope >= 0.495 | 375 | +2441 | +408 | +0.4 | +42 / -76 / +442 | -213 | 268 | noise |
| lookback 9 bars (45 min), slope >= 0.557 | 303 | +2146 | +112 | +0.1 | -44 / -23 / +179 | -147 | 289 | noise |


## M2K 5m: slope lookback (base = 12 bars, slope 1.0)

Base: 216 trades, net +86, avg +0.40, thirds +42 / +1 / +43, last 4 wk -7, max DD 36

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (15 min), slope >= 0.200 | 437 | +294 | +208 | +2.9 | +61 / +116 / +31 | -9 | 34 | robust except last 4 wk |
| lookback 3 bars (15 min), slope >= 0.225 | 392 | +279 | +192 | +2.9 | +40 / +112 / +41 | +1 | 26 | robust |
| lookback 3 bars (15 min), slope >= 0.250 | 346 | +265 | +179 | +2.9 | +39 / +102 / +38 | -2 | 24 | robust except last 4 wk |
| lookback 3 bars (15 min), slope >= 0.275 | 305 | +257 | +171 | +2.9 | +38 / +78 / +55 | -0 | 25 | robust except last 4 wk |
| lookback 3 bars (15 min), slope >= 0.300 | 262 | +243 | +156 | +2.9 | +34 / +61 / +61 | +2 | 20 | robust |
| lookback 3 bars (15 min), slope >= 0.338 | 218 | +202 | +115 | +2.2 | +32 / +40 / +43 | -2 | 25 | robust except last 4 wk |


## MES 5m: slope lookback (base = 12 bars, slope 0.7)

Base: 228 trades, net +248, avg +1.09, thirds +54 / +99 / +96, last 4 wk +17, max DD 46

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (15 min), slope >= 0.140 | 455 | +445 | +197 | +1.9 | +133 / +108 / -45 | -5 | 86 | noise |
| lookback 3 bars (15 min), slope >= 0.157 | 410 | +504 | +255 | +2.5 | +116 / +149 / -10 | +9 | 60 | noise |
| lookback 3 bars (15 min), slope >= 0.175 | 352 | +562 | +313 | +3.3 | +129 / +144 / +40 | +38 | 40 | robust |
| lookback 3 bars (15 min), slope >= 0.192 | 303 | +564 | +316 | +3.6 | +100 / +156 / +61 | +29 | 40 | robust |
| lookback 3 bars (15 min), slope >= 0.210 | 272 | +509 | +260 | +3.0 | +84 / +136 / +41 | +14 | 36 | robust |
| lookback 3 bars (15 min), slope >= 0.236 | 222 | +474 | +225 | +2.7 | +92 / +110 / +23 | -0 | 25 | robust except last 4 wk |


## MGC 5m: slope lookback (base = 12 bars, slope 0.48)

Base: 624 trades, net +672, avg +1.08, thirds +199 / +234 / +239, last 4 wk +12, max DD 94

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (15 min), slope >= 0.096 | 709 | +876 | +204 | +1.2 | +46 / +117 / +41 | +23 | 68 | promising |
| lookback 3 bars (15 min), slope >= 0.108 | 665 | +974 | +302 | +1.8 | +80 / +153 / +68 | +24 | 63 | promising |
| lookback 3 bars (15 min), slope >= 0.120 | 618 | +1058 | +386 | +2.3 | +113 / +153 / +120 | +49 | 61 | robust |
| lookback 3 bars (15 min), slope >= 0.132 | 576 | +1096 | +424 | +2.7 | +104 / +179 / +142 | +85 | 55 | robust |
| lookback 3 bars (15 min), slope >= 0.144 | 535 | +1069 | +397 | +2.6 | +66 / +189 / +142 | +79 | 46 | robust |
| lookback 3 bars (15 min), slope >= 0.162 | 484 | +1010 | +338 | +2.3 | +31 / +179 / +128 | +61 | 44 | robust |


## MNQ 5m: slope lookback (base = 12 bars, slope off)

Base: 1484 trades, net +2033, avg +1.37, thirds +615 / +913 / +505, last 4 wk +491, max DD 777

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 3 bars (15 min), slope >= 0.110 | 651 | +3327 | +1294 | +1.2 | +101 / +854 / +339 | -353 | 237 | promising |
| lookback 3 bars (15 min), slope >= 0.124 | 597 | +3719 | +1686 | +1.5 | +113 / +1124 / +448 | -404 | 210 | promising |
| lookback 3 bars (15 min), slope >= 0.138 | 556 | +4075 | +2041 | +1.9 | +238 / +1196 / +608 | -328 | 210 | promising |
| lookback 3 bars (15 min), slope >= 0.151 | 516 | +4511 | +2478 | +2.2 | +480 / +1305 / +693 | -237 | 181 | robust except last 4 wk |
| lookback 3 bars (15 min), slope >= 0.165 | 474 | +4314 | +2281 | +2.0 | +610 / +1139 / +532 | -302 | 195 | robust except last 4 wk |
| lookback 3 bars (15 min), slope >= 0.186 | 428 | +4097 | +2064 | +1.8 | +365 / +1051 / +648 | -253 | 170 | promising |


## M2K 5m: slope lookback (base = 12 bars, slope 1.0)

Base: 216 trades, net +86, avg +0.40, thirds +42 / +1 / +43, last 4 wk -7, max DD 36

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 1 bars (5 min), slope >= 0.067 | 321 | +90 | +3 | +0.0 | +1 / +55 / -53 | -1 | 45 | noise |
| lookback 1 bars (5 min), slope >= 0.075 | 312 | +79 | -7 | -0.1 | -11 / +64 / -60 | -8 | 41 | worse |
| lookback 1 bars (5 min), slope >= 0.083 | 306 | +85 | -2 | -0.0 | -8 / +62 / -55 | -8 | 41 | worse |
| lookback 1 bars (5 min), slope >= 0.092 | 289 | +105 | +18 | +0.3 | -3 / +75 / -53 | -9 | 33 | noise |
| lookback 1 bars (5 min), slope >= 0.100 | 280 | +111 | +25 | +0.3 | -3 / +76 / -48 | -3 | 28 | noise |
| lookback 1 bars (5 min), slope >= 0.113 | 261 | +107 | +20 | +0.3 | -4 / +70 / -45 | -13 | 27 | noise |
| lookback 2 bars (10 min), slope >= 0.133 | 434 | +118 | +32 | +0.4 | -10 / +62 / -20 | +6 | 38 | noise |
| lookback 2 bars (10 min), slope >= 0.150 | 405 | +147 | +61 | +0.9 | -0 / +90 / -29 | +1 | 38 | noise |
| lookback 2 bars (10 min), slope >= 0.167 | 370 | +173 | +87 | +1.3 | +30 / +77 / -21 | -2 | 38 | noise |
| lookback 2 bars (10 min), slope >= 0.183 | 341 | +204 | +117 | +1.8 | +34 / +90 / -7 | -1 | 38 | noise |
| lookback 2 bars (10 min), slope >= 0.200 | 310 | +218 | +132 | +2.2 | +43 / +93 / -4 | -13 | 38 | noise |
| lookback 2 bars (10 min), slope >= 0.225 | 274 | +218 | +132 | +2.3 | +37 / +92 / +3 | -6 | 26 | robust except last 4 wk |


## MES 5m: slope lookback (base = 12 bars, slope 0.7)

Base: 228 trades, net +248, avg +1.09, thirds +54 / +99 / +96, last 4 wk +17, max DD 46

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 1 bars (5 min), slope >= 0.047 | 323 | -38 | -286 | -2.6 | -63 / -112 / -112 | -48 | 82 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.052 | 312 | -13 | -261 | -2.4 | -57 / -94 / -110 | -47 | 75 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.058 | 299 | +22 | -226 | -2.1 | -37 / -91 / -98 | -42 | 70 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.064 | 292 | +41 | -208 | -1.9 | -37 / -77 / -94 | -38 | 61 | worse |
| lookback 1 bars (5 min), slope >= 0.070 | 283 | +59 | -189 | -1.8 | -24 / -68 / -97 | -39 | 66 | worse |
| lookback 1 bars (5 min), slope >= 0.079 | 267 | +85 | -164 | -1.6 | -23 / -60 / -81 | -31 | 52 | worse |
| lookback 2 bars (10 min), slope >= 0.093 | 435 | +205 | -43 | -0.4 | +46 / +7 / -96 | -39 | 66 | worse |
| lookback 2 bars (10 min), slope >= 0.105 | 403 | +314 | +66 | +0.6 | +108 / +33 / -75 | -25 | 60 | noise |
| lookback 2 bars (10 min), slope >= 0.117 | 377 | +321 | +72 | +0.7 | +98 / +55 / -81 | -14 | 60 | noise |
| lookback 2 bars (10 min), slope >= 0.128 | 351 | +373 | +124 | +1.3 | +95 / +77 / -48 | +8 | 57 | noise |
| lookback 2 bars (10 min), slope >= 0.140 | 328 | +401 | +152 | +1.6 | +106 / +87 / -41 | +2 | 71 | noise |
| lookback 2 bars (10 min), slope >= 0.158 | 292 | +475 | +227 | +2.5 | +109 / +120 / -2 | +5 | 48 | noise |


## MGC 5m: slope lookback (base = 12 bars, slope 0.48)

Base: 624 trades, net +672, avg +1.08, thirds +199 / +234 / +239, last 4 wk +12, max DD 94

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 1 bars (5 min), slope >= 0.032 | 379 | +213 | -459 | -2.6 | -209 / -113 / -136 | +25 | 87 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.036 | 366 | +247 | -425 | -2.4 | -183 / -104 / -138 | +17 | 87 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.040 | 360 | +243 | -429 | -2.4 | -187 / -109 / -132 | +19 | 87 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.044 | 349 | +310 | -362 | -2.0 | -154 / -103 / -105 | +27 | 76 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.048 | 344 | +316 | -356 | -2.0 | -158 / -97 / -101 | +33 | 76 | robustly worse |
| lookback 1 bars (5 min), slope >= 0.054 | 339 | +320 | -352 | -2.0 | -145 / -97 / -110 | +24 | 79 | robustly worse |
| lookback 2 bars (10 min), slope >= 0.064 | 584 | +588 | -84 | -0.5 | -55 / -26 / -3 | +64 | 66 | worse |
| lookback 2 bars (10 min), slope >= 0.072 | 573 | +628 | -44 | -0.3 | -35 / -1 / -8 | +59 | 66 | worse |
| lookback 2 bars (10 min), slope >= 0.080 | 555 | +583 | -89 | -0.5 | -29 / -14 / -46 | +27 | 66 | worse |
| lookback 2 bars (10 min), slope >= 0.088 | 528 | +635 | -37 | -0.2 | -7 / +20 / -49 | +7 | 63 | worse |
| lookback 2 bars (10 min), slope >= 0.096 | 507 | +635 | -37 | -0.2 | +28 / +6 / -70 | +9 | 67 | worse |
| lookback 2 bars (10 min), slope >= 0.108 | 475 | +725 | +53 | +0.3 | +67 / +43 / -57 | +4 | 55 | noise |


## MNQ 5m: slope lookback (base = 12 bars, slope off)

Base: 1484 trades, net +2033, avg +1.37, thirds +615 / +913 / +505, last 4 wk +491, max DD 777

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| lookback 1 bars (5 min), slope >= 0.037 | 387 | +804 | -1230 | -1.1 | -360 / -396 / -474 | -501 | 421 | worse |
| lookback 1 bars (5 min), slope >= 0.041 | 380 | +808 | -1225 | -1.1 | -315 / -365 / -546 | -545 | 390 | worse |
| lookback 1 bars (5 min), slope >= 0.046 | 361 | +840 | -1193 | -1.0 | -284 / -356 / -553 | -533 | 363 | worse |
| lookback 1 bars (5 min), slope >= 0.050 | 355 | +750 | -1284 | -1.1 | -264 / -324 / -695 | -675 | 426 | worse |
| lookback 1 bars (5 min), slope >= 0.055 | 344 | +914 | -1119 | -1.0 | -269 / -293 / -557 | -599 | 425 | worse |
| lookback 1 bars (5 min), slope >= 0.062 | 334 | +1085 | -948 | -0.8 | -172 / -293 / -483 | -507 | 413 | worse |
| lookback 2 bars (10 min), slope >= 0.073 | 566 | +2221 | +188 | +0.2 | -68 / +214 / +41 | -401 | 280 | noise |
| lookback 2 bars (10 min), slope >= 0.083 | 537 | +2350 | +316 | +0.3 | -57 / +174 / +199 | -341 | 249 | noise |
| lookback 2 bars (10 min), slope >= 0.092 | 512 | +2496 | +463 | +0.4 | -64 / +263 / +265 | -311 | 262 | noise |
| lookback 2 bars (10 min), slope >= 0.101 | 495 | +2414 | +380 | +0.3 | -8 / +334 / +54 | -361 | 272 | noise |
| lookback 2 bars (10 min), slope >= 0.110 | 475 | +2654 | +621 | +0.5 | +100 / +388 / +132 | -331 | 272 | noise |
| lookback 2 bars (10 min), slope >= 0.124 | 434 | +2744 | +711 | +0.6 | +99 / +431 / +180 | -410 | 218 | noise |


