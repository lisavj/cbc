## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09.
- MGC 3m "London stop after 1st loss" alone (— / stop / current exits): net +139, beyond random **+91** (thirds +66 / +24 / +1; last 4 wk +94 vs +101) -> **HELD, barely** (third 3 only +1, last 4 weeks slightly worse).
- MGC 3m "VWAP + London stop" (filter / stop / current exits): net +274, beyond random **+234** (thirds +95 / +50 / +88; last 4 wk +117 vs +101) ✓↑ -> **HELD**. With TP + SL rules: net +315 (beyond random +274) ✓↑.
- MES 3m balanced "filter / stop / SL rule": net **-36** (thirds +112 / -116 / -31; beyond random +54 / +474 / -82; last 4 wk +7 vs +124) -> **WEAKER** (third 3 beyond random negative, last 4 weeks far behind).
- **Weeks held: MGC London stop 2/3, MGC VWAP+London 2/3, MES balanced set 0/3.**
- MES 3m: only "filter / stop / current exits" is ✓ (beyond random +16 / +403 / +0), last 4 wk +75 vs +124.

---

Everything together, MES 3m and MGC 3m -- 11/08/2026.
Entry filter x session stop x exit rules, all in one replay (net after costs; gain beyond random skipping in brackets).
MES 3m: filter = skip shorts when price is below... above the 5-day EMA rule (shorts only when price is below the 5-day EMA of session closes);
        stop = 2 losses in a row or 2 flip-outs per 18-18 session, ONLY when the previous 5 sessions lost (regime switch);
        TP rule = TP1 -> 85 % after 18 min; SL rule = SL1 to half its distance if negative at 18 min.
MGC 3m: filter = skip setups against VWAP; stop = London (03:00-09:30 ET) stops after its first loss;
        TP rule = TP1 -> 65 % after 21 min; SL rule = close if under 25 % of TP1 at 18 min.
Costs: commission + 1 tick per trade (MES 0.50 / MGC 0.22), +1 tick for a rule exit at the candle close.

## MES 3m

Filter / session stop / exits. ✓ = beyond random positive in all three thirds; ↑ = last 4 weeks not worse than current exits.

| Filter / stop / exits | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| filter / stop / TP + SL rules | +140 (+92) | -108 (+489) | -63 (-107) | -26 (-161) | -31 (+474) | 1067 |  |
| filter / stop / SL rule | +112 (+54) | -116 (+474) | -31 (-82) | +7 (-132) | -36 (+447) | 1021 |  |
| filter / stop / TP rule | +97 (+48) | -157 (+437) | +18 (-26) | +27 (-110) | -41 (+458) | 1056 |  |
| filter / stop / current exits | +74 (+16) | -185 (+403) | +53 (+0) | +75 (-66) | -59 (+419) | 1011 | ✓ |
| — / stop / TP rule | +128 (+105) | -225 (+382) | +15 (-4) | +38 (-89) | -83 (+484) | 1198 |  |
| — / stop / TP + SL rules | +147 (+128) | -167 (+442) | -69 (-88) | -17 (-143) | -89 (+482) | 1207 |  |
| — / stop / SL rule | +94 (+66) | -144 (+456) | -71 (-98) | +23 (-107) | -121 (+425) | 1155 |  |
| — / stop / current exits | +75 (+44) | -246 (+352) | +16 (-10) | +94 (-38) | -155 (+386) | 1145 |  |
| filter / — / TP rule | +79 (+64) | -413 (+264) | -58 (-36) | +62 (-67) | -392 (+292) | 1448 |  |
| filter / — / TP + SL rules | +128 (+115) | -422 (+259) | -148 (-121) | +3 (-124) | -442 (+253) | 1470 |  |
| filter / — / current exits | +23 (+1) | -492 (+176) | -25 (-13) | +105 (-28) | -493 (+165) | 1391 |  |
| filter / — / SL rule | +63 (+42) | -469 (+203) | -122 (-104) | +39 (-92) | -528 (+141) | 1415 |  |
| — / — / TP rule | +55 (+84) | -658 (+87) | -59 (+24) | +73 (-46) | -662 (+194) | 1810 | ✓ |
| — / — / TP + SL rules | +94 (+126) | -622 (+128) | -140 (-52) | +11 (-107) | -668 (+202) | 1841 |  |
| — / — / SL rule | +15 (+37) | -663 (+76) | -143 (-68) | +56 (-66) | -791 (+46) | 1770 |  |
| — / — / current exits | -20 (+0) | -733 (+0) | -68 (+0) | +124 (+0) | -822 (+0) | 1738 | ↑ |

**Full stats** (after costs): trades / net / win %% / profit factor / max drawdown

| Period | Current exits | All four (filter + stop + TP + SL) | Best row (filter / stop / TP + SL rules) |
|---|---|---|---|
| Third 1 | 520 / -20 / 51 % / 0.99 / 222 | 375 / +140 / 53 % / 1.13 / 102 | 375 / +140 / 53 % / 1.13 / 102 |
| Third 2 | 587 / -733 / 42 % / 0.64 / 808 | 297 / -108 / 45 % / 0.85 / 219 | 297 / -108 / 45 % / 0.85 / 219 |
| Third 3 | 631 / -68 / 51 % / 0.96 / 308 | 395 / -63 / 50 % / 0.94 / 117 | 395 / -63 / 50 % / 0.94 / 117 |
| Last 4 wk | 149 / +124 / 56 % / 1.24 / 80 | 126 / -26 / 49 % / 0.95 / 97 | 126 / -26 / 49 % / 0.95 / 97 |
| Whole | 1738 / -822 / 48 % / 0.85 / 1088 | 1067 / -31 / 50 % / 0.99 / 249 | 1067 / -31 / 50 % / 0.99 / 249 |

## MGC 3m

Filter / session stop / exits. ✓ = beyond random positive in all three thirds; ↑ = last 4 weeks not worse than current exits.

| Filter / stop / exits | Third 1 | Third 2 | Third 3 | Last 4 wk | Whole | Trades | |
|---|---|---|---|---|---|---|---|
| filter / stop / TP + SL rules | +143 (+159) | +28 (+39) | +144 (+75) | +116 (+16) | +315 (+274) | 901 | ✓↑ |
| filter / stop / SL rule | +136 (+151) | +21 (+33) | +157 (+88) | +123 (+22) | +314 (+273) | 892 | ✓↑ |
| filter / stop / TP rule | +107 (+123) | +21 (+33) | +154 (+86) | +113 (+13) | +283 (+242) | 891 | ✓↑ |
| filter / stop / current exits | +79 (+95) | +38 (+50) | +157 (+88) | +117 (+17) | +274 (+234) | 873 | ✓↑ |
| filter / — / TP rule | +89 (+102) | +31 (+41) | +144 (+74) | +116 (+15) | +263 (+217) | 996 | ✓↑ |
| filter / — / SL rule | +86 (+99) | +21 (+31) | +146 (+76) | +119 (+18) | +253 (+207) | 1000 | ✓↑ |
| filter / — / TP + SL rules | +98 (+111) | +22 (+33) | +130 (+61) | +112 (+11) | +251 (+204) | 1010 | ✓↑ |
| filter / — / current exits | +50 (+64) | +36 (+47) | +148 (+79) | +125 (+24) | +234 (+190) | 972 | ✓↑ |
| — / stop / SL rule | +118 (+130) | -15 (-6) | +93 (+22) | +116 (+15) | +196 (+147) | 1062 | ↑ |
| — / stop / TP + SL rules | +123 (+136) | -22 (-13) | +89 (+18) | +112 (+11) | +191 (+141) | 1072 | ↑ |
| — / stop / TP rule | +73 (+86) | -7 (+2) | +92 (+21) | +101 (-0) | +157 (+108) | 1063 | ✓ |
| — / stop / current exits | +53 (+66) | +14 (+24) | +72 (+1) | +94 (-7) | +139 (+91) | 1043 | ✓ |
| — / — / SL rule | +45 (+55) | -24 (-17) | +91 (+18) | +111 (+10) | +113 (+56) | 1226 | ↑ |
| — / — / TP rule | +25 (+35) | -7 (-0) | +90 (+17) | +102 (+0) | +108 (+51) | 1220 | ↑ |
| — / — / TP + SL rules | +52 (+62) | -29 (-22) | +84 (+11) | +107 (+5) | +107 (+50) | 1237 | ↑ |
| — / — / current exits | -10 (+0) | -7 (+0) | +72 (+0) | +101 (+0) | +55 (+0) | 1193 | ↑ |

**Full stats** (after costs): trades / net / win %% / profit factor / max drawdown

| Period | Current exits | All four (filter + stop + TP + SL) | Best row (filter / stop / TP + SL rules) |
|---|---|---|---|
| Third 1 | 447 / -10 / 51 % / 0.99 / 137 | 325 / +143 / 53 % / 1.19 / 51 | 325 / +143 / 53 % / 1.19 / 51 |
| Third 2 | 378 / -7 / 49 % / 0.99 / 131 | 283 / +28 / 48 % / 1.05 / 74 | 283 / +28 / 48 % / 1.05 / 74 |
| Third 3 | 368 / +72 / 50 % / 1.08 / 82 | 293 / +144 / 53 % / 1.26 / 52 | 293 / +144 / 53 % / 1.26 / 52 |
| Last 4 wk | 102 / +101 / 54 % / 1.48 / 34 | 85 / +116 / 61 % / 1.93 / 21 | 85 / +116 / 61 % / 1.93 / 21 |
| Whole | 1193 / +55 / 50 % / 1.02 / 189 | 901 / +315 / 51 % / 1.17 / 86 | 901 / +315 / 51 % / 1.17 / 86 |
