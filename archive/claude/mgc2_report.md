# MGC 2m improvement battery -- 2026-11-13 21:49 ET (weekly run 3)

**STUDY SETTINGS STALE:** settings_sync_report (11/13 16:47 ET, v10.96) lists 3 non-"known" MISMATCHes -- MES 3m `LIVE` / chop_sim `EXIT[('MES',3)]` part 'tod' vs 100 % all day, and chop_sim `EXIT[('MGC',3)]` 0.5 / trail 3.5 vs FLIP 0 %. None touches MGC 2m (EXIT (MGC,2), GATE (MGC,2) and the 2m base exits all MATCH), so this battery runs on current MGC 2m settings.

## Since last week

First run with the **range gate 24 bars / 20 % / 5 ATR in the baseline** (v10.77, script sync 11/08). Last week's (run 2, 11/07) baseline had no range gate, so every Δ below is measured from a different base; the baseline jump and many row moves come from that sync, not the market. The flop gate (v10.77, non-flip setups while the HTF flip is a flop) is still not modelled.

- **Current:** 1353 setups, net **+384 pts** ($3,843 per micro), thirds **+174 / +68 / +142** (run 2 without gate: 1499, +340, +83 / +130 / +127; run 2's "range gate 5 ATR" row was +386, +91 / -62 / +17 vs that base -> consistent).
- **Robust / promising rows:** none. Consecutive robust runs: 0 for every row. **Verdict: no change yet.**
- **Range gate OFF (pre-v10.77):** Δ **-24**, z -0.2, thirds -91 / +62 / +5, last 4 wk -41.4 -> OFF is *not* better (run 1 +23 / run 2 +46 for the gate = OFF worse each run). Robust-better runs for OFF: 0 of 3.
- **Rows moved > 30 pts vs last week** (Δ vs Δ; base changed, see above):
  - Trigger OFF: HTF EMA9 Pierce +47 -> **+85** (z +1.1, -53 / +55 / +83, last 4 wk +16.6) -- noise, Jun-Jul still negative; live HTF EMA9 Pierce is the best live trigger (+16.2 / 16 ended).
  - Trigger OFF: HTF EMA9 + EMA20 +51 -> **+87** (z +0.9, -26 / +5 / +109, last 4 wk +19.0) -- noise.
  - Trigger OFF: LTF EMA20 Pierce -219 -> **-304** (z -2.4, -177 / +15 / -143) -- keep ON.
  - Trigger OFF: HTF CBC Flip -10 -> **-59** (z -0.6, -16 / -43 / -1) -- keep ON.
  - Close 100 % at TP1 -21 -> **+20** (z +0.1, -2 / -22 / +43, last 4 wk +26.8) -- noise.
  - Max SL cap 6 -14 -> **+25** (z +0.4, +16 / -1 / +9); cap 8 +29 -> **-8**; Min SL 4 +10 -> **-25**.
  - Trail 2.5 ATR -15 -> **+29** (z +0.3, +28 / +0 / +1) -- noise.
  - TP1 1.3 ATR -169 -> **-124** (still clearly worse).
  - VWAP stretch 3 ATR -66 -> **-103**; 4 ATR -41 -> **-110** -- keep OFF.
  - HTF flips >= 3 in 8 block -48 -> **+2** (noise).
  - NY session only -210 -> **-290** (z -1.9).
- **Small leans (noise):** Close 50 % at TP1 +40 (z +0.3, +38 / -6 / +7, last 4 wk -6.6); Trail 2.0 +24; No BE +13.
- **Confirmed current:** 1H MTF gate ON **-338** (z -3.6, -62 / -44 / -231; keep OFF); LTF EMA20 Pierce OFF -304 (z -2.4); TP1 1.3 -124 / 2.0 -98 / 2.5 -70; range gate 4 / 6 ATR / zone 30 % all worse than 5 ATR.
- **Session gaps** (setups the live alerts never send; neither robust-worse -> no session extension):
  - Block 22:30-03:00: Δ **-106**, z -1.3, thirds -15 / +7 / -98 (those setups +106: +15 / -7 / +98), last 4 wk -0.8. Run 1 -106, run 2 -86. Aug third negative and z > -2 -> robust-worse runs: 0.
  - Block 07:45-09:30: Δ **-59**, z -1.0, thirds +3 / -35 / -27 (those setups +59: -3 / +35 / +27), last 4 wk +10.5. Run 1 -86, run 2 -86. Jun-Jul negative -> robust-worse runs: 0.

### Live MGC 2m Trade Setups by first trigger (alert store, near-copies de-duplicated)

Per DATA_NOTES 1 the 11/08-11/12 MGC 2m alerts arrived twice (two CBC alerts) and the store is still not cleaned (`lastDedupe` null), so alerts with the same Chart / Time / "•" names within 60 s are counted once (1,504 near copies dropped store-wide). Raw `trigger_study.live()` (not de-duplicated) is shown below for reference.

| Chart | Trigger | Setups | Ended | Win % | Net | Avg |
|---|---|---|---|---|---|---|
| MGC 2m | HTF CBC Flip | 62 | 57 | 47% | -36.3 | -0.64 |
| MGC 2m | HTF EMA20 Pierce | 16 | 14 | 36% | -22.1 | -1.58 |
| MGC 2m | HTF EMA20 Pierce (late) | 5 | 4 | 25% | -9.4 | -2.35 |
| MGC 2m | HTF EMA9 Pierce | 19 | 16 | 62% | +16.2 | +1.01 |
| MGC 2m | HTF EMA9 Pierce (late) | 9 | 9 | 44% | +0.2 | +0.02 |
| MGC 2m | HTF Pullback Structure | 1 | 1 | 0% | -5.0 | -5.00 |
| MGC 2m | LTF EMA20 Pierce | 82 | 75 | 47% | +2.4 | +0.03 |
| MGC 2m | LTF EMA20 Pierce (late) | 33 | 32 | 41% | -43.6 | -1.36 |

Vs last week: LTF EMA20 Pierce plain + late 79 / 74 ended, -21.0 -> **115 / 107 ended, -41.2** (the late variant -33.1 -> -43.6). HTF CBC Flip -16.0 (38 ended) -> **-36.3 (57 ended)**. HTF EMA20 Pierce incl. late -24.5 -> -31.5 (18 ended). No replay row supports removing any of them (Flip OFF -59, LTF20 OFF -304, HTF EMA20 OFF -28); the only positive trigger-OFF row is HTF EMA9 Pierce, which is the best trigger live.

Raw (not de-duplicated) `trigger_study.live()` MGC 2m rows: Flip 66 / 60 -50.1; HTF EMA20 17 / 15 -24.3; HTF EMA20 late 5 / 4 -9.4; HTF EMA9 20 / 18 +7.5; HTF EMA9 late 10 / 10 -4.0; Pullback Structure 1 / 1 -5.0; LTF EMA20 94 / 88 -0.4; LTF EMA20 late 34 / 33 -40.9.

### Replay vs live (same dates, current replay settings incl. range gate 5 ATR)

```
first live MGC 2m setup 2026-10-19, last ended 2026-11-13
LIVE: 227 setups sent, 228 ended, net -67.7
REPLAY same dates: 238 setups, net +47.9
GAP (live - replay): -115.6
REPLAY same dates excl. 22:30-03:00 & 07:45-09:30 entries: 155 setups, net +52.3
| Week of | Live | Replay |
|---|---|---|
| 2026-10-19 | +7.9 | +20.2 |
| 2026-10-26 | -8.7 | +45.0 |
| 2026-11-02 | -31.3 | -15.4 |
| 2026-11-09 | -35.6 | -1.8 |
```

Live MGC 2m net **-67.7** vs replay **+47.9** over 10/19 -> 11/13: gap **-116 pts** (last week -32.1 vs -13.5, gap -19, on the no-gate replay). Part of the jump is the 11/08 sync: with the range gate in the replay, the replay weeks moved (10/19 -5.3 -> +20.2, 10/26 +29.8 -> +45.0, 11/02 -38.0 -> -15.4). The live flop gate is not in the replay. **MGC 2m LIVE GAP flag condition met this week (live < 0, replay > +30): 1 of 3 weeks running** (run 2 did not meet it) -> no flag yet. Week of 11/09: live -35.6 vs replay -1.8.

## Full output (run 3, 2026-11-13 21:49 ET)

Current (incl. range gate 5 ATR): 1353 setups, net +384 pts ($+3843), thirds +174 / +68 / +142

| Change | Setups | Net | Δ | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|
| Close 50 % at TP1 | 1353 | +424 | +40 | +0.3 | +38 / -6 / +7 | noise | -6.6 |
| Close 60 % at TP1 | 1353 | +411 | +26 | +0.2 | +25 / -4 / +5 | noise | -4.4 |
| Close 70 % at TP1 | 1353 | +398 | +13 | +0.1 | +13 / -2 / +2 | noise | -2.2 |
| Close 90 % at TP1 | 1353 | +371 | -13 | -0.1 | -13 / +2 / -2 | worse | +2.2 |
| Close 100 % at TP1 | 1441 | +404 | +20 | +0.1 | -2 / -22 / +43 | noise | +26.8 |
| SL1 1.3 ATR | 1357 | +368 | -16 | -0.2 | +7 / -7 / -16 | worse | +1.3 |
| SL1 1.5 ATR | 1356 | +379 | -5 | -0.1 | -2 / -9 / +6 | worse | +0.3 |
| SL1 2.0 ATR | 1349 | +376 | -8 | -0.1 | -10 / +10 / -9 | worse | +6.2 |
| Min SL 3 pts | 1360 | +344 | -40 | -0.6 | -16 / -27 / +3 | worse | -3.6 |
| Min SL 4 pts | 1358 | +360 | -25 | -0.4 | +3 / -17 / -11 | worse | -8.3 |
| Min SL 6 pts | 1345 | +395 | +11 | +0.2 | +8 / -12 / +15 | noise | +6.0 |
| Max SL cap 6 pts | 1355 | +409 | +25 | +0.4 | +16 / -1 / +9 | noise | +3.5 |
| Max SL cap 8 pts | 1352 | +376 | -8 | -0.2 | -12 / +19 / -16 | worse | -11.8 |
| Max SL cap 10 pts | 1351 | +356 | -28 | -0.6 | -40 / +31 / -20 | worse | -10.8 |
| TP1 1.3 ATR | 1380 | +261 | -124 | -1.0 | -71 / -20 / -33 | worse | -29.9 |
| TP1 2.0 ATR | 1345 | +286 | -98 | -1.0 | -34 / -23 / -41 | worse | -14.9 |
| TP1 2.5 ATR | 1338 | +315 | -70 | -0.7 | -16 / -12 / -42 | worse | -43.3 |
| Trail 1.3 ATR | 1395 | +393 | +9 | +0.1 | +12 / -29 / +26 | noise | -0.2 |
| Trail 2.0 ATR | 1321 | +408 | +24 | +0.2 | +2 / -1 / +23 | noise | +3.7 |
| Trail 2.5 ATR | 1286 | +414 | +29 | +0.3 | +28 / +0 / +1 | noise | +1.8 |
| No breakeven at TP1 | 1344 | +398 | +13 | +0.2 | -4 / +18 / -0 | noise | +5.4 |
| Trigger OFF: HTF CBC Flip | 1216 | +325 | -59 | -0.6 | -16 / -43 / -1 | worse | -6.6 |
| Trigger OFF: LTF EMA20 Pierce | 885 | +81 | -304 | -2.4 | -177 / +15 / -143 | worse | -30.8 |
| Trigger OFF: HTF EMA9 Pierce | 1201 | +470 | +85 | +1.1 | -53 / +55 / +83 | noise | +16.6 |
| Trigger OFF: HTF EMA20 Pierce | 1255 | +357 | -28 | -0.5 | +6 / -47 / +13 | worse | -13.3 |
| Trigger OFF: HTF EMA9 + EMA20 | 1058 | +472 | +87 | +0.9 | -26 / +5 / +109 | noise | +19.0 |
| Range gate OFF (pre-v10.77) | 1572 | +360 | -24 | -0.2 | -91 / +62 / +5 | worse | -41.4 |
| Range gate 4 ATR (24 bars, 20 %) | 1477 | +373 | -11 | -0.1 | -41 / +13 / +16 | worse | -17.6 |
| Range gate 6 ATR (24 bars, 20 %) | 1289 | +340 | -44 | -0.8 | -38 / +22 / -29 | worse | -10.5 |
| Range gate 4 ATR, zone 30 % | 1419 | +341 | -43 | -0.4 | -51 / +14 / -6 | worse | -18.0 |
| Range gate 5 ATR, zone 30 % | 1213 | +317 | -67 | -0.9 | -33 / +18 / -52 | worse | +4.0 |
| VWAP stretch 3 ATR | 675 | +281 | -103 | -0.8 | +18 / -79 / -42 | worse | -26.2 |
| VWAP stretch 4 ATR | 780 | +274 | -110 | -0.9 | -14 / -74 / -22 | worse | -21.9 |
| VWAP stretch 6 ATR | 961 | +335 | -49 | -0.5 | -25 / -44 / +20 | worse | -14.1 |
| 1H MTF gate (skip against 60m CBC) | 1005 | +47 | -338 | -3.6 | -62 / -44 / -231 | worse | -99.2 |
| HTF flips >= 3 in 8 block | 1082 | +386 | +2 | +0.0 | +60 / -35 / -23 | noise | -34.2 |
| HTF flips >= 4 in 8 block | 1302 | +392 | +8 | +0.2 | +13 / -5 / +0 | noise | +5.7 |
| Block 22:30-03:00 setups | 1080 | +279 | -106 | -1.3 | -15 / +7 / -98 | worse | -0.8 |
| Block 07:45-09:30 setups | 1208 | +326 | -59 | -1.0 | +3 / -35 / -27 | worse | +10.5 |
| Block 16:00-18:00 setups | 1353 | +384 | +0 | +0.0 | +0 / +0 / +0 | noise | +0.0 |
| NY session only (09:30-17:00) | 394 | +94 | -290 | -1.9 | -72 / -65 / -152 | worse | -8.7 |
