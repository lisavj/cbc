STUDY SETTINGS STALE: settings_sync_report (11/13) lists 3 non-"known" MISMATCHes -- mes3_ema_grid LIVE part 'tod' (live 100 %), chop_sim EXIT MES 3m part 'tod', chop_sim EXIT MGC 3m 50 % / trail 3.5 (live FLIP 0 %). This study is NOT affected: volflip_study.py passes its own X dict exits (MES 100 % at TP1; MGC 0 % + BE, no trail), which match CBC_SETTINGS v10.96.

# Volume strong flip + EMA200-vs-VWAP watch -- 2026-11-15 13:53 ET

Script: claude/volflip_study.py (full table in the chat delivery of volflip_report.md). Weekly, Sundays ~2 PM ET.

Data notes for this run:
- Bars end Fri 11/13 16:57 ET for both charts (market closed since) -- the SAME data as the 11/14 baseline, so MES 3m results are identical to run 1. This run adds no new evidence for MES; it still counts as a weekly run.
- MGC 3m baseline changed because of the 11/14 mes3_ema_grid X4 fix (stretch gate now applied): current 1136 setups / +615 (was 1602 / +547 in run 1). MGC rows are not comparable to run 1.

## Overview

| Chart | Variant | Setups | Δ | z | Δ thirds | Δ last 4 wk | Verdict |
|---|---|---|---|---|---|---|---|
| MES 3m | 5a. Volume > avg 20: 3m setup candle | 1003 | +328 | +1.4 | +159 / +158 / +11 | -82 | promising |
| MES 3m | 5a. Volume > avg 50: 3m setup candle | 971 | +243 | +1.1 | +12 / +315 / -85 | -141 | noise |
| MES 3m | 5a. Volume > avg 100: 3m setup candle | 868 | +285 | +1.2 | -9 / +351 / -56 | -134 | noise |
| MES 3m | 5b. Volume > avg 20: 15m flip candle (flip setups) | 1721 | +63 | +0.6 | +45 / +80 / -61 | -40 | noise |
| MES 3m | 5b. Volume > avg 50: 15m flip candle (flip setups) | 1705 | +54 | +0.5 | +56 / +48 / -49 | -36 | noise |
| MES 3m | 5b. Volume > avg 100: 15m flip candle (flip setups) | 1689 | +99 | +0.8 | +53 / +74 / -28 | -36 | noise |
| MES 3m | 5c. Volume > avg 50: setup candle or one of last 3 | 1324 | +13 | +0.1 | -90 / +92 / +11 | -71 | noise |
| MES 3m | 5d. Volume > avg 50 AND sweep-close strong candle | 57 | +671 | +2.2 | -78 / +668 / +81 | -103 | noise |
| MES 3m | 5e. Volume > avg 50 (3m) + EMA200 vs VWAP | 478 | +685 | +2.5 | +28 / +637 / +20 | -57 | robust except last 4 wk |
| MES 3m | W1. Watch: EMA200 vs VWAP | 856 | +560 | +2.5 | +88 / +440 / +31 | -20 | robust except last 4 wk |
| MES 3m | W2. Watch: 3m EMA20 vs VWAP | 1521 | +180 | +1.4 | +27 / +139 / +14 | -43 | promising |
| MGC 3m | 5a. Volume > avg 20: 3m setup candle | 593 | -103 | -0.3 | +184 / +103 / -390 | -258 | worse |
| MGC 3m | 5a. Volume > avg 50: 3m setup candle | 612 | +120 | +0.3 | +294 / +129 / -303 | -256 | noise |
| MGC 3m | 5a. Volume > avg 100: 3m setup candle | 582 | -251 | -0.7 | +53 / -27 / -277 | -252 | worse |
| MGC 3m | 5b. Volume > avg 20: 15m flip candle (flip setups) | 1078 | +84 | +0.5 | +129 / +22 / -66 | +27 | noise |
| MGC 3m | 5b. Volume > avg 50: 15m flip candle (flip setups) | 1074 | +99 | +0.5 | +150 / +52 / -102 | +27 | noise |
| MGC 3m | 5b. Volume > avg 100: 15m flip candle (flip setups) | 1072 | +67 | +0.3 | +142 / +45 / -120 | +27 | noise |
| MGC 3m | 5c. Volume > avg 50: setup candle or one of last 3 | 829 | -86 | -0.3 | +96 / +31 / -213 | -269 | worse |
| MGC 3m | 5d. Volume > avg 50 AND sweep-close strong candle | 39 | -684 | -1.4 | -377 / +8 / -314 | -269 | worse |
| MGC 3m | 5e. Volume > avg 50 (3m) + EMA200 vs VWAP | 254 | -332 | -0.8 | -165 / +101 / -267 | -248 | worse |
| MGC 3m | W1. Watch: EMA200 vs VWAP | 488 | -418 | -1.1 | -213 / +66 / -271 | -257 | worse |
| MGC 3m | W2. Watch: 3m EMA20 vs VWAP | 861 | -20 | -0.1 | -127 / +62 / +45 | -59 | worse |

Current (live): MES 3m 1799 setups, net -801 (thirds -2 / -712 / -87, last 4 wk +99). MGC 3m 1136 setups, net +615 (thirds +329 / -10 / +297, last 4 wk +262).

## Verdict

- MES 3m W1 EMA200 vs VWAP: +560, z 2.5, all thirds better, but last 4 wk -20 -> does not qualify. Keeps 48 % of setups (856 / 1799).
- MES 3m W2 3m EMA20 vs VWAP: +180, z 1.4 -> promising only; last 4 wk -43. Keeps 85 %.
- MES 3m 5a volume > avg 20: +328, z 1.4 -> promising only; last 4 wk -82. Keeps 56 %.
- MES 3m 5e volume > avg 50 + EMA200 vs VWAP: +685, z 2.5, all thirds better, last 4 wk -57 -> does not qualify; keeps only 27 % of setups (478 / 1799), below the 40 % floor, so it could not qualify even with a positive last 4 weeks.
- MES 3m 5d: +671 but only 57 setups (3 %) and first third worse -> noise.
- MGC 3m: nothing helps; EMA200 vs VWAP -418, volume gates noise or worse (only 5b, flip-candle volume, is slightly positive with last 4 wk +27, z 0.5 -- noise). No MGC variant promising.
- **No change recommended.** If W1 ever qualifies, it needs a CBC Pine change: a new per-symbol/timeframe input such as "Environment: slow EMA vs VWAP" (list, e.g. "MES 3m 200" = longs only while EMA200 > VWAP, shorts only while EMA200 < VWAP; "MES 3m 20" for the 3m EMA20 version), applied as an entry gate on all triggers. 5a/5e would need a "Volume > average of N candles" per symbol/timeframe input (e.g. "MES 3m 20"). Not built.

## Tallies (runs qualifying, need 3 consecutive)

| Variant (MES 3m) | Runs qualifying |
|---|---|
| W1 EMA200 vs VWAP | 0/3 |
| W2 3m EMA20 vs VWAP | 0/3 |
| 5a volume > avg 20 | 0/3 |
| 5e volume > avg 50 + EMA200 vs VWAP | 0/3 (also under the 40 % setup floor) |
| MGC 3m (any) | none promising -- not tracked |

## History

| Run | MES W1 EMA200 vs VWAP | MES W2 3m EMA20 vs VWAP | MES 5a vol > avg 20 | MES 5e vol50 + EMA200 | MGC | Verdict |
|---|---|---|---|---|---|---|
| 11/14 (baseline) | +560, z 2.5, +88/+440/+31, l4 -20 | +180, z 1.4, +27/+139/+14, l4 -43 | +328, z 1.4, +159/+158/+11, l4 -82 | +685, z 2.5, +28/+637/+20, l4 -57 | nothing helps (EMA200 -377) | no change; tallies 0/3 (last 4 wk negative) |
| 11/15 | +560, z 2.5, +88/+440/+31, l4 -20 | +180, z 1.4, +27/+139/+14, l4 -43 | +328, z 1.4, +159/+158/+11, l4 -82 | +685, z 2.5, +28/+637/+20, l4 -57 (27 % kept) | nothing helps (EMA200 -418; X4 fix, base 1136 / +615) | no change; tallies 0/3; same bars as baseline (to 11/13) |
