# Why the session-guard rule lags in the last 4 weeks — MES 3m and MGC 3m — 11/08/2026

## MES 3m — skip shorts above... below the 5-day EMA

Net after costs (beyond random skipping in brackets). Trades in the last column.

| Variant | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades |
|---|---|---|---|---|---|---|
| current exits | -23 (+0) | -714 (+0) | -94 (+0) | +176 (+0) | -831 (+0) | 1700 |
| filter only (no guard) | +21 (-0) | -505 (+142) | -10 (+30) | +175 (-9) | -495 (+172) | 1363 |
| A. guard per 18-18 session (the 11/08 rule) | +112 (+28) | -151 (+410) | -19 (-88) | +70 (-143) | -58 (+351) | 836 |
| B. looser: 3 losses or 3 flip-outs, per session | +44 (-2) | -327 (+275) | -38 (-59) | +44 (-154) | -321 (+214) | 1092 |
| C. guard resets at 03:00 and 09:30 (Asia / London / NY separately) | +46 (+9) | -439 (+188) | -31 (-24) | +145 (-46) | -423 (+173) | 1219 |
| D. pause 1 h after 2 losses / 2 flip-outs, then reset | -9 (-58) | -429 (+188) | -9 (-4) | +147 (-44) | -447 (+127) | 1172 |
| D. pause 2 h after 2 losses / 2 flip-outs, then reset | -23 (-76) | -405 (+204) | +3 (-2) | +140 (-55) | -425 (+126) | 1126 |
| E. guard only when the previous 3 sessions lost (else take all) | +106 (+50) | -254 (+326) | +46 (+15) | +148 (-43) | -101 (+392) | 1008 |
| E. guard only when the previous 5 sessions lost (else take all) | +71 (+13) | -208 (+361) | +76 (+46) | +145 (-47) | -61 (+420) | 983 |
| E. guard only when the previous 10 sessions lost (else take all) | +173 (+111) | -173 (+393) | +27 (+0) | +155 (-31) | +27 (+504) | 977 |
| F. = C + E5 (sub-session guard, only after 5 losing sessions) | +39 (+7) | -446 (+183) | +1 (+17) | +183 (-3) | -406 (+207) | 1254 |

## MES 3m — no trend filter

Net after costs (beyond random skipping in brackets). Trades in the last column.

| Variant | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades |
|---|---|---|---|---|---|---|
| current exits | -23 (+0) | -714 (+0) | -94 (+0) | +176 (+0) | -831 (+0) | 1700 |
| A. guard per 18-18 session (the 11/08 rule) | +88 (+16) | -172 (+393) | -52 (-101) | +81 (-125) | -136 (+308) | 909 |
| B. looser: 3 losses or 3 flip-outs, per session | -39 (-60) | -408 (+214) | -73 (-64) | +28 (-165) | -520 (+91) | 1248 |
| C. guard resets at 03:00 and 09:30 (Asia / London / NY separately) | +53 (+50) | -589 (+78) | -96 (-49) | +144 (-40) | -633 (+79) | 1455 |
| D. pause 1 h after 2 losses / 2 flip-outs, then reset | +6 (-7) | -541 (+127) | -89 (-41) | +153 (-33) | -624 (+78) | 1435 |
| D. pause 2 h after 2 losses / 2 flip-outs, then reset | +29 (+9) | -517 (+134) | -76 (-42) | +139 (-49) | -564 (+102) | 1362 |
| E. guard only when the previous 3 sessions lost (else take all) | +78 (+54) | -285 (+305) | +7 (+5) | +151 (-34) | -200 (+364) | 1153 |
| E. guard only when the previous 5 sessions lost (else take all) | +72 (+42) | -236 (+342) | -1 (-8) | +142 (-43) | -165 (+377) | 1107 |
| E. guard only when the previous 10 sessions lost (else take all) | +145 (+110) | -229 (+349) | -62 (-57) | +164 (-15) | -147 (+402) | 1122 |
| F. = C + E5 (sub-session guard, only after 5 losing sessions) | +22 (+29) | -608 (+62) | -59 (-1) | +183 (+6) | -646 (+90) | 1505 |

## MGC 3m — skip shorts above... below the 5-day EMA

Net after costs (beyond random skipping in brackets). Trades in the last column.

| Variant | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades |
|---|---|---|---|---|---|---|
| current exits | -63 (+0) | +3 (+0) | -77 (+0) | +30 (+0) | -138 (+0) | 1705 |
| filter only (no guard) | -42 (+10) | +37 (+29) | -65 (+2) | +15 (-18) | -70 (+42) | 1387 |
| A. guard per 18-18 session (the 11/08 rule) | -39 (-1) | -75 (-99) | -17 (+39) | +26 (-10) | -131 (-61) | 863 |
| B. looser: 3 losses or 3 flip-outs, per session | -25 (+22) | +42 (+30) | -107 (-44) | +5 (-30) | -90 (+8) | 1211 |
| C. guard resets at 03:00 and 09:30 (Asia / London / NY separately) | -77 (-28) | -24 (-36) | -104 (-41) | +12 (-22) | -204 (-105) | 1225 |
| D. pause 1 h after 2 losses / 2 flip-outs, then reset | +8 (+55) | -39 (-52) | -69 (-6) | +40 (+6) | -100 (-3) | 1198 |
| D. pause 2 h after 2 losses / 2 flip-outs, then reset | -37 (+9) | -32 (-46) | -75 (-14) | +28 (-6) | -143 (-50) | 1149 |
| E. guard only when the previous 3 sessions lost (else take all) | -35 (+10) | -78 (-94) | -27 (+35) | +46 (+12) | -140 (-48) | 1141 |
| E. guard only when the previous 5 sessions lost (else take all) | -50 (-5) | -75 (-89) | -9 (+52) | +41 (+6) | -133 (-43) | 1117 |
| E. guard only when the previous 10 sessions lost (else take all) | -62 (-17) | -60 (-77) | +11 (+71) | +39 (+5) | -110 (-23) | 1078 |
| F. = C + E5 (sub-session guard, only after 5 losing sessions) | -49 (+1) | +2 (-8) | -77 (-12) | +31 (-2) | -124 (-19) | 1304 |

## MGC 3m — no trend filter

Net after costs (beyond random skipping in brackets). Trades in the last column.

| Variant | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades |
|---|---|---|---|---|---|---|
| current exits | -63 (+0) | +3 (+0) | -77 (+0) | +30 (+0) | -138 (+0) | 1705 |
| A. guard per 18-18 session (the 11/08 rule) | +15 (+57) | -93 (-116) | +15 (+73) | +37 (+2) | -63 (+13) | 948 |
| B. looser: 3 losses or 3 flip-outs, per session | -8 (+47) | +9 (-1) | -106 (-38) | +35 (+1) | -105 (+8) | 1404 |
| C. guard resets at 03:00 and 09:30 (Asia / London / NY separately) | -110 (-53) | -54 (-64) | -98 (-28) | +31 (-1) | -262 (-145) | 1457 |
| D. pause 1 h after 2 losses / 2 flip-outs, then reset | -51 (+5) | -49 (-59) | -65 (+6) | +78 (+45) | -165 (-48) | 1452 |
| D. pause 2 h after 2 losses / 2 flip-outs, then reset | -49 (+5) | -54 (-65) | -73 (-4) | +48 (+15) | -176 (-64) | 1389 |
| E. guard only when the previous 3 sessions lost (else take all) | -19 (+34) | -75 (-88) | -7 (+61) | +59 (+27) | -101 (+7) | 1332 |
| E. guard only when the previous 5 sessions lost (else take all) | -29 (+22) | -81 (-93) | +17 (+82) | +50 (+17) | -93 (+11) | 1294 |
| E. guard only when the previous 10 sessions lost (else take all) | -39 (+12) | -76 (-91) | +54 (+118) | +55 (+23) | -62 (+39) | 1248 |
| F. = C + E5 (sub-session guard, only after 5 losing sessions) | -99 (-39) | -35 (-41) | -61 (+11) | +47 (+15) | -195 (-69) | 1568 |
