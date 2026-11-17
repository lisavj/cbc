HTF EMA20 slope filter threshold grid 0.24-0.36 (step 0.03) -- MES 3m and MGC 3m, CBC EMA Slope branch -- 11/14/2026.
Slope = |15m EMA20 now - 12 chart bars ago| / ATR; block when below the threshold (all triggers). Branch default 0.3 on both charts.
MES 3m: ER 0.23 + breakout, range gate 24 / 20 % / 5 ATR; SL1 3 ATR min 5, TP1 1.75, 100 % at TP1; HTF CBC Flip setups ride to the
HTF flip back / SL1 / 16:00 / next setup. MGC 3m: same filters + VWAP stretch 4 ATR (fixed engine); SL1 1.7 ATR min 5 cap 7, TP1 1.7
cap 6, 0 % at TP1 + BE, closed by the HTF flip (FLIP 0 %). TV EMA20 from the bar feed (= project baselines). Replay Jan 5 -> now,
net after costs (MES 0.50, MGC 0.22). Δ vs 0.30. z = Δ / (SD x sqrt(setups changed)); robust = z >= 2, all thirds better, last 4 wk >= 0;
promising = z >= 1 and all thirds.

## MES 3m

| Slope threshold | Setups | Win % | Net | Avg | Δ vs 0.30 | z | Thirds | Δ by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| off (v10.97) | 1799 | 45 % | -612 | -0.34 | -749 | -3.3 | +2 / -720 / +106 | -247 / -311 / -191 | +120 | 943 | worse |
| 0.24 | 1363 | 47 % | +5 | +0.00 | -133 | -1.2 | +245 / -477 / +236 | -4 / -68 / -61 | +132 | 550 | worse |
| 0.27 | 1306 | 47 % | -27 | -0.02 | -165 | -2.0 | +159 / -461 / +274 | -90 / -52 / -23 | +136 | 529 | worse |
| 0.30 (branch) | 1242 | 48 % | +138 | +0.11 | +0 | +0.0 | +249 / -409 / +297 | +0 / +0 / +0 | +155 | 476 | current |
| 0.33 | 1180 | 47 % | +99 | +0.08 | -38 | -0.5 | +222 / -403 / +281 | -27 / +5 / -17 | +175 | 461 | worse |
| 0.36 | 1122 | 48 % | +203 | +0.18 | +65 | +0.6 | +263 / -392 / +332 | +14 / +17 / +34 | +176 | 430 | noise |

## MGC 3m

| Slope threshold | Setups | Win % | Net | Avg | Δ vs 0.30 | z | Thirds | Δ by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| off (v10.97) | 1136 | 18 % | +615 | +0.54 | -520 | -1.2 | +329 / -10 / +297 | -217 / -89 / -215 | +262 | 245 | worse |
| 0.24 | 719 | 20 % | +936 | +1.30 | -199 | -1.0 | +469 / +19 / +449 | -77 / -59 / -63 | +266 | 167 | worse |
| 0.27 | 681 | 22 % | +1014 | +1.49 | -121 | -0.8 | +506 / +45 / +463 | -40 / -33 / -48 | +277 | 128 | worse |
| 0.30 (branch) | 634 | 22 % | +1135 | +1.79 | +0 | +0.0 | +545 / +78 / +512 | +0 / +0 / +0 | +279 | 121 | current |
| 0.33 | 583 | 23 % | +1168 | +2.00 | +33 | +0.2 | +563 / +57 / +548 | +18 / -21 / +37 | +286 | 129 | noise |
| 0.36 | 520 | 22 % | +954 | +1.83 | -181 | -0.9 | +482 / -11 / +482 | -63 / -89 / -29 | +242 | 131 | worse |

## Candidates (robust / promising vs 0.30)

- none
# Follow-up 11/14: 0.39-0.48 (python3 slope_grid.py 0,0.30,0.36,0.39,0.42,0.45,0.48)

## MES 3m

| Slope threshold | Setups | Win % | Net | Avg | Δ vs 0.30 | z | Thirds | Δ by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| off (v10.97) | 1799 | 45 % | -612 | -0.34 | -749 | -3.3 | +2 / -720 / +106 | -247 / -311 / -191 | +120 | 943 | worse |
| 0.30 (branch) | 1242 | 48 % | +138 | +0.11 | +0 | +0.0 | +249 / -409 / +297 | +0 / +0 / +0 | +155 | 476 | current |
| 0.36 | 1122 | 48 % | +203 | +0.18 | +65 | +0.6 | +263 / -392 / +332 | +14 / +17 / +34 | +176 | 430 | noise |
| 0.39 | 1058 | 48 % | +271 | +0.26 | +133 | +1.0 | +233 / -312 / +351 | -16 / +96 / +53 | +178 | 381 | noise |
| 0.42 | 1000 | 49 % | +350 | +0.35 | +212 | +1.4 | +235 / -232 / +347 | -14 / +177 / +50 | +164 | 296 | noise |
| 0.45 | 950 | 49 % | +292 | +0.31 | +154 | +0.9 | +168 / -213 / +337 | -82 / +196 / +40 | +155 | 277 | noise |
| 0.48 | 907 | 49 % | +293 | +0.32 | +155 | +0.9 | +163 / -201 / +331 | -86 / +208 / +33 | +130 | 265 | noise |

## MGC 3m

| Slope threshold | Setups | Win % | Net | Avg | Δ vs 0.30 | z | Thirds | Δ by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| off (v10.97) | 1136 | 18 % | +615 | +0.54 | -520 | -1.2 | +329 / -10 / +297 | -217 / -89 / -215 | +262 | 245 | worse |
| 0.30 (branch) | 634 | 22 % | +1135 | +1.79 | +0 | +0.0 | +545 / +78 / +512 | +0 / +0 / +0 | +279 | 121 | current |
| 0.36 | 520 | 22 % | +954 | +1.83 | -181 | -0.9 | +482 / -11 / +482 | -63 / -89 / -29 | +242 | 131 | worse |
| 0.39 | 478 | 23 % | +1007 | +2.11 | -128 | -0.5 | +504 / +2 / +501 | -41 / -76 / -11 | +250 | 125 | worse |
| 0.42 | 449 | 23 % | +989 | +2.20 | -147 | -0.5 | +496 / +45 / +448 | -50 / -34 / -64 | +235 | 108 | worse |
| 0.45 | 413 | 24 % | +1050 | +2.54 | -85 | -0.3 | +544 / +57 / +449 | -1 / -22 / -62 | +235 | 78 | worse |
| 0.48 | 379 | 24 % | +1064 | +2.81 | -72 | -0.2 | +563 / +76 / +424 | +18 / -2 / -87 | +197 | 77 | worse |

## Candidates (robust / promising vs 0.30)

- none
## Verdict (follow-up)

- MES 3m: every threshold from 0.36 to 0.48 beats 0.30 (+65 to +212) -- a plateau, not a single spike. Best 0.42: +212, z 1.4, thirds -14 / +177 / +50, last 4 wk +9, max DD 296 vs 476. Misses "promising" only on the first third (-14). The gain is mostly the Apr-Jul third (fewer trades in the bad stretch); the first third gets worse from 0.39 and the last 4 wk peaks at 0.36-0.39. Candidate, not a change yet: re-run weekly; switch MES 3m to 0.42 (or 0.39) if it turns promising (z >= 1 and all thirds better).
- MGC 3m: 0.36-0.48 all worse than 0.30 (-72 to -181); avg per setup rises but too many winners are lost. Lower drawdown at 0.45-0.48 (77-78 vs 121) but last 4 wk worse. Keep 0.30.
