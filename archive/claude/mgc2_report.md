# MGC 2m improvement battery -- 2026-11-07 09:50 ET (weekly run 2 -- rerun after data repair; replaces the 11/06 run)

## Since last week

Manual rerun of the 11/06 run, after the BarFeed bar data was repaired on 11/07. It **replaces** the 11/06 21:49 ET run as weekly run 2 in the run history (not a new run 3), so the consecutive-run counts are unchanged. The repaired MGC 2m bars moved the replay even though nothing traded since Friday. The 11/07 09:46 ET check, already on the repaired bars, gave identical output.

- **Current:** 1499 setups, net **+340 pts** ($3,403 per micro), thirds +83 / +130 / +127 (11/06 run before the repair: 1506, +365, +83 / +130 / +152; run 1 11/02: 1446, +370, +83 / +130 / +158). The data repair cut the Sep-Nov third by 25 pts.
- **Robust / promising rows:** none (0 consecutive robust runs for every row). **Verdict: no change yet.**
- **Rows moved > 30 pts vs last week (run 1, 11/02):** none moved > 30 pts vs the 11/06 pre-repair run. Vs run 1: HTF EMA9 + EMA20 OFF +16 -> **+51** (z +0.5, -5 / -5 / +62, last 4 wk +9.1); NY session only -241 -> **-210** (z -1.3, +35 / -106 / -138, last 4 wk +23.2); VWAP stretch 3 ATR -97 -> **-66** (z -0.5, +89 / -119 / -36); VWAP stretch 6 ATR -68 -> **-34**.
- **Small leans (noise):** range gate 5 ATR +24 -> **+46** (z +0.4, +91 / -62 / +17, last 4 wk +46.6; Aug still -62); HTF EMA9 Pierce OFF +40 -> **+47** (z +0.6, -49 / +58 / +39, last 4 wk +23.2); close 50 % at TP1 +32 (+28 / +3 / +1); max SL cap 8 +29 (z +0.6, -15 / +17 / +27, last 4 wk -2.7).
- **Confirmed current:** 1H MTF gate ON -311 (z -3.1, keep OFF); LTF EMA20 Pierce OFF -219 (z -1.8); TP1 1.3 ATR -169 / 2.0 -83.
- **Session gaps** (setups the live alerts never send; neither robust-worse -> no session extension):
  - Block 22:30-03:00: Δ -86, z -1.0, thirds +34 / -27 / -94 (those setups +86: -34 / +27 / +94), last 4 wk -8.1. Run 2 -88, run 1 -106. Jun-Jul third negative -> fails the all-thirds rule. Robust-worse runs: 0.
  - Block 07:45-09:30: Δ -86, z -1.4, thirds -0 / -11 / -74 (those setups +86: 0 / +11 / +74), last 4 wk -7.7. Run 2 -83, run 1 -86. Jun-Jul ~0 -> fails. Robust-worse runs: 0.

### Live MGC 2m Trade Setups by first trigger (alert store)

| Chart | Trigger | Setups | Ended | Win % | Net | Avg |
|---|---|---|---|---|---|---|
| MGC 2m | HTF CBC Flip | 41 | 38 | 50% | -16.0 | -0.42 |
| MGC 2m | HTF EMA20 Pierce | 14 | 12 | 33% | -20.1 | -1.68 |
| MGC 2m | HTF EMA20 Pierce (late) | 4 | 3 | 33% | -4.4 | -1.47 |
| MGC 2m | HTF EMA9 Pierce | 13 | 11 | 64% | +5.9 | +0.54 |
| MGC 2m | HTF EMA9 Pierce (late) | 5 | 5 | 40% | -3.2 | -0.63 |
| MGC 2m | HTF Pullback Structure | 1 | 1 | 0% | -5.0 | -5.00 |
| MGC 2m | LTF EMA20 Pierce | 56 | 51 | 49% | +12.1 | +0.24 |
| MGC 2m | LTF EMA20 Pierce (late) | 23 | 23 | 39% | -33.1 | -1.44 |

Unchanged from the 11/06 run (no trading since). LTF EMA20 Pierce plain + late: 79 setups / 74 ended, **-21.0** (run 1 ~61 / 58, -28.4). Weakest live: HTF EMA20 Pierce (incl. late) -24.5 over 15 ended, HTF CBC Flip -16.0 over 38 ended; no replay row supports removing either.

### Replay vs live (same dates, current replay settings)

```
first live MGC 2m setup 2026-10-19, last ended 2026-11-06
LIVE: 157 setups sent, 158 ended, net -32.1
REPLAY same dates: 198 setups, net -13.5
GAP (live - replay): -18.6
REPLAY same dates excl. 22:30-03:00 & 07:45-09:30 entries: 127 setups, net -19.3
| Week of | Live | Replay |
|---|---|---|
| 2026-10-19 | +7.9 | -5.3 |
| 2026-10-26 | -8.7 | +29.8 |
| 2026-11-02 | -31.3 | -38.0 |
```

Live MGC 2m net **-32.1** vs replay **-13.5** over 10/19 -> 11/06: gap **-19 pts** (the 11/06 run before the repair showed replay +11.2, gap -43; the data repair turned the replay's week of 11/02 from +2.9 to -38.0). Replay is not positive by > 30 pts, so the **MGC 2m LIVE GAP flag does not fire** (0 of 3 weeks).

## Full output (run 2, rerun after data repair, 2026-11-07 09:50 ET)

Current: 1499 setups, net +340 pts ($+3403), thirds +83 / +130 / +127

| Change | Setups | Net | Δ | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|
| Close 50 % at TP1 | 1499 | +372 | +32 | +0.2 | +28 / +3 / +1 | noise | -0.5 |
| Close 60 % at TP1 | 1499 | +362 | +21 | +0.2 | +19 / +2 / +0 | noise | -0.4 |
| Close 70 % at TP1 | 1499 | +351 | +11 | +0.1 | +9 / +1 / +0 | noise | -0.2 |
| Close 90 % at TP1 | 1499 | +330 | -11 | -0.1 | -9 / -1 / -0 | worse | +0.2 |
| Close 100 % at TP1 | 1499 | +319 | -21 | -0.2 | -19 / -2 / -0 | worse | +0.4 |
| SL1 1.3 ATR | 1506 | +294 | -46 | -0.6 | -0 / -24 / -22 | worse | +3.2 |
| SL1 1.5 ATR | 1502 | +332 | -9 | -0.1 | +3 / -5 / -7 | worse | -5.3 |
| SL1 2.0 ATR | 1493 | +313 | -27 | -0.4 | -19 / +10 / -19 | worse | -2.1 |
| Min SL 3 pts | 1512 | +328 | -12 | -0.1 | -17 / -32 / +36 | worse | +26.8 |
| Min SL 4 pts | 1507 | +350 | +10 | +0.1 | +9 / -19 / +19 | noise | +13.7 |
| Min SL 6 pts | 1486 | +351 | +11 | +0.1 | -6 / +3 / +14 | noise | +6.8 |
| Max SL cap 6 pts | 1504 | +326 | -14 | -0.2 | +21 / -18 / -18 | worse | +3.5 |
| Max SL cap 8 pts | 1497 | +369 | +29 | +0.6 | -15 / +17 / +27 | noise | -2.7 |
| Max SL cap 10 pts | 1497 | +327 | -13 | -0.3 | -51 / +26 / +11 | worse | -14.4 |
| TP1 1.3 ATR | 1535 | +171 | -169 | -1.3 | -92 / -43 / -34 | worse | -15.0 |
| TP1 2.0 ATR | 1485 | +257 | -83 | -0.7 | -15 / -26 / -42 | worse | -39.6 |
| TP1 2.5 ATR | 1476 | +287 | -53 | -0.5 | +11 / -20 / -44 | worse | -51.1 |
| Trail 1.3 ATR | 1550 | +369 | +29 | +0.2 | +28 / -32 / +33 | noise | +1.4 |
| Trail 2.0 ATR | 1462 | +337 | -4 | -0.0 | -8 / -4 / +9 | worse | +3.4 |
| Trail 2.5 ATR | 1417 | +325 | -15 | -0.1 | +7 / -22 / -0 | worse | +9.5 |
| No breakeven at TP1 | 1486 | +339 | -1 | -0.0 | +4 / -5 / +0 | worse | +9.8 |
| Trigger OFF: HTF CBC Flip | 1265 | +331 | -10 | -0.1 | +53 / -63 / +0 | worse | -7.8 |
| Trigger OFF: LTF EMA20 Pierce | 1090 | +121 | -219 | -1.8 | -131 / -9 / -79 | worse | -47.8 |
| Trigger OFF: HTF EMA9 Pierce | 1350 | +388 | +47 | +0.6 | -49 / +58 / +39 | noise | +23.2 |
| Trigger OFF: HTF EMA20 Pierce | 1404 | +332 | -8 | -0.1 | +28 / -47 / +11 | worse | -22.7 |
| Trigger OFF: HTF EMA9 + EMA20 | 1217 | +391 | +51 | +0.5 | -5 / -5 / +62 | noise | +9.1 |
| Range gate 4 ATR (24 bars, 20 %) | 1408 | +352 | +11 | +0.2 | +50 / -49 / +9 | noise | +29.1 |
| Range gate 5 ATR (24 bars, 20 %) | 1291 | +386 | +46 | +0.4 | +91 / -62 / +17 | noise | +46.6 |
| Range gate 4 ATR, zone 30 % | 1352 | +319 | -22 | -0.3 | +40 / -48 / -14 | worse | +26.7 |
| VWAP stretch 3 ATR | 731 | +275 | -66 | -0.5 | +89 / -119 / -36 | worse | +8.7 |
| VWAP stretch 4 ATR | 857 | +300 | -41 | -0.3 | +69 / -91 / -18 | worse | +0.4 |
| VWAP stretch 6 ATR | 1058 | +306 | -34 | -0.3 | +9 / -60 / +16 | worse | +14.2 |
| 1H MTF gate (skip against 60m CBC) | 1120 | +29 | -311 | -3.1 | -50 / -48 / -213 | worse | -82.3 |
| HTF flips >= 3 in 8 block | 1179 | +292 | -48 | -0.5 | +62 / -65 / -45 | worse | -43.3 |
| HTF flips >= 4 in 8 block | 1438 | +325 | -15 | -0.3 | +15 / -12 / -19 | worse | -8.6 |
| Block 22:30-03:00 setups | 1186 | +254 | -86 | -1.0 | +34 / -27 / -94 | worse | -8.1 |
| Block 07:45-09:30 setups | 1342 | +255 | -86 | -1.4 | -0 / -11 / -74 | worse | -7.7 |
| Block 16:00-18:00 setups | 1499 | +340 | +0 | +0.0 | +0 / +0 / +0 | noise | +0.0 |
| NY session only (09:30-17:00) | 421 | +130 | -210 | -1.3 | +35 / -106 / -138 | worse | +23.2 |
