# Evening session study — weekly check -- 2026-11-07 09:52 ET (rerun after data repair; replaces the 11/06 run)

## Since last week (vs the Fri 11/06 17:53 ET report)

**Note on this run:** manual rerun of the 11/06 check after the BarFeed bar data was repaired (MGC 3m had 5m candles mixed in; MES 2m/5m had gaps). It **replaces** the 11/06 run in the check history: the streak stays at 3 (10/28, 10/30, 11/06-rerun). The numbers below compare the repaired data with the original 11/06 17:53 report. (A scheduled run at 09:46 ET today already picked up the repaired data and gave identical results.) Sim counts moved: MGC 3m 1204→1183, MES 3m 1713→1719, MGC 2m 1506→1499, MES 2m 1227→1226; 5m unchanged; live counts unchanged.

- **MGC 3m:** window +0.68/setup vs +0.19 rest of day (was +0.61 vs +0.04; sim 148). **Weak 19:15–19:30 dropped** (22 · −18.8, thirds −1 / −21 / +4); strong 19:30–19:45 still (21 · +40.2). Live window 11 · +15.8, rest 56 · −50.0 (unchanged).
- **MES 3m:** window +0.56 vs −0.03 (was +0.66 vs −0.06). Strong 18:30–18:45 and 19:00–19:15 LTF EMA20 ✓ still. "Skip HTF CBC Flip in the window" still not supported (15 · −5.0, thirds −10 / +1 / +4). Live window 10 · +12.0.
- **MGC 2m:** window −0.29 vs +0.27 (was −0.25 vs +0.28). Weak 18:30–18:45 still (21 · −25.2); strong 19:15–19:30 and 19:30–19:45 still (19:30–19:45 LTF EMA20 ✓ dropped to 9 setups). Candidate "skip LTF EMA20 Pierce in the window": sim 48 · −51.5, thirds −9 / −20 / −22 (all negative, same as 11/06), live 9 · −2.1 (< 10) → still fails (c).
- **MES 2m:** window −0.68 vs −0.12 (unchanged). Weak 18:30–18:45 and 18:45–19:00 still; 19:45–20:00 not weak. Candidate "no new setups 18:45–20:00" streak still broken (middle third positive). Live window 8 · −19.6.
- **MGC 5m / MES 5m:** identical to 11/06 (window +0.17 vs −0.12 / +0.32 vs −0.03; MES 5m strong 19:30–19:45 still). Live 49 / 58 total, 6 / 5 in window.

**Verdict:** nothing in the evening study meets the rule. MGC 2m skip LTF EMA20 Pierce 18:00–20:30 is closest (sim all-negative for 3 weekly checks) but has only 9 live setups. An evening per-chart/per-trigger block would need a CBC Pine change. No Pine or server change made.

---

# Evening session 18:00–20:30 ET in 15-minute buckets -- 2026-11-07 09:52 ET (rerun after data repair)

CBC evening-session study: setups entered 18:00-20:30 ET in 15-minute buckets, per chart and trigger type.

Cases: MGC 3m, MES 3m (HTF 15m), MGC 2m, MES 2m (HTF 10m), MGC 5m, MES 5m (HTF 25m; base exits, no gates). Two sources:
  LIVE  real Trade Setup alerts matched to their Setup Ended results (Alert Feed, /alerts?from=2000-01-01).
  SIM   chop_sim.py replay (current CBC-style rules + exits, ~50 % exact match with real setups) on the BarFeed
        archive: 3m and 5m from 01/05, 2m from 06/01. The sim's quiet window ends 18:30 (CBC: 18:45) and it skips the
        forming Asia opening range 20:00-20:30 (same as CBC), so those buckets are empty / thin by design.
Bucket = entry candle OPEN time (ET). Thirds = the case's sim setups split into three equal time blocks.
A bucket/trigger cell is flagged "weak" when it has >= 10 sim setups and is negative in all three thirds, and
"strong" when >= 10 sim setups and positive in all three thirds.
Usage: python3 evening_study.py > evening_session_report_new.md   (needs chop_sim.py in the same folder)

Cells: setups · win % · net pts. Thirds: net in each third of the sim period. ⚠ weak = ≥ 10 sim setups and negative in all thirds; ✓ strong = ≥ 10 and positive in all thirds.

## MGC 3m — sim 01/05 → 11/06 (1183 setups), live 67 setups since 10/19

Whole window 18:00–20:30: sim 148 · 45% · +100.7 (avg +0.68) vs rest of day avg +0.19 · live 11 · 55% · +15.8 vs rest 56 · 39% · -50.0

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 5 · 20% · -11.6 | +0 / -8 / -4 | – | 1 · 0% · -2.7 | 3 · 33% · -7.5 | – | 1 · 0% · -1.4 |
| 18:30–18:45 | 21 · 48% · +1.9 | -2 / +2 / +2 | – | 4 · 25% · -4.8 | 9 · 56% · +2.9 | 6 · 33% · -15.5 | 2 · 100% · +19.3 |
| 18:45–19:00 | 25 · 44% · +3.2 | -9 / +10 / +2 | 3 · 33% · -0.6 | 7 · 71% · +9.0 | 14 · 36% · -0.5 | 2 · 0% · -6.4 | 2 · 50% · +1.1 |
| 19:00–19:15 | 26 · 35% · +40.2 | +15 / +32 / -7 | – | 9 · 44% · +22.1 | 8 · 50% · +45.2 | 5 · 0% · -17.3 | 4 · 25% · -9.7 |
| 19:15–19:30 | 22 · 36% · -18.8 | -1 / -21 / +4 | 3 · 67% · +6.9 | 4 · 50% · -2.5 | 10 · 30% · -16.0 | 4 · 75% · +9.5 | 4 · 0% · -9.8 |
| 19:30–19:45 | 21 · 67% · +40.2 ✓ strong | +2 / +31 / +7 | 1 · 0% · -2.1 | 6 · 67% · +14.8 | 13 · 69% · +31.1 | – | 2 · 50% · -5.7 |
| 19:45–20:00 | 28 · 46% · +45.6 | +36 / -10 / +20 | 4 · 75% · +11.7 | 5 · 40% · +5.7 | 15 · 40% · +34.5 | 5 · 60% · +5.9 | 3 · 67% · -0.5 |
| 20:00–20:15 | – | – | – | – | – | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 36 · 50% · +41.6 (+7 / +19 / +16) | live 1 · 100% · +3.1
- LTF EMA20 Pierce: sim 72 · 46% · +89.7 (+59 / +21 / +9) | live 9 · 44% · +5.7
- HTF EMA9 Pierce: sim 22 · 36% · -23.9 (-21 / -2 / -1) | live 1 · 100% · +7.0
- HTF EMA20 Pierce: sim 18 · 39% · -6.7 (-5 / -1 / -1) | live –

## MES 3m — sim 01/05 → 11/06 (1719 setups), live 103 setups since 10/19

Whole window 18:00–20:30: sim 106 · 54% · +58.9 (avg +0.56) vs rest of day avg -0.03 · live 10 · 50% · +12.0 vs rest 93 · 46% · -2.5

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 5 · 60% · +6.1 | -3 / +10 / -1 | – | 2 · 50% · +1.8 | 3 · 67% · +4.3 | – | – |
| 18:30–18:45 | 16 · 56% · +21.0 ✓ strong | +10 / +11 / +0 | – | 4 · 50% · -1.4 | 8 · 50% · +14.6 | 2 · 100% · +8.2 | 2 · 50% · -0.5 |
| 18:45–19:00 | 16 · 44% · -14.4 | +1 / -9 / -6 | 1 · 100% · +3.0 | 2 · 0% · -13.0 | 10 · 50% · +0.7 | 4 · 50% · -2.0 | – |
| 19:00–19:15 | 19 · 53% · +14.9 | +16 / -3 / +2 | 3 · 67% · +16.4 | 1 · 0% · -5.0 | 13 · 54% · +14.2 ✓ | 4 · 50% · +2.0 | 1 · 100% · +3.6 |
| 19:15–19:30 | 15 · 67% · +15.5 | +18 / -5 / +2 | 2 · 50% · +2.4 | 2 · 100% · +9.4 | 9 · 56% · -3.5 | 1 · 100% · +5.4 | 3 · 67% · +4.2 |
| 19:30–19:45 | 15 · 47% · +7.8 | +17 / -0 / -9 | 2 · 0% · -7.2 | 1 · 100% · +2.0 | 12 · 33% · -1.3 | 2 · 100% · +7.0 | – |
| 19:45–20:00 | 19 · 53% · +3.9 | -4 / +14 / -7 | 2 · 50% · -2.6 | 3 · 67% · +1.2 | 13 · 46% · -0.4 | 2 · 50% · -0.1 | 1 · 100% · +3.2 |
| 20:00–20:15 | 1 · 100% · +4.2 | +4 / +0 / +0 | – | – | 1 · 100% · +4.2 | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 15 · 53% · -5.0 (-10 / +1 / +4) | live 1 · 0% · -2.4
- LTF EMA20 Pierce: sim 69 · 49% · +32.9 (+46 / -3 / -10) | live 8 · 50% · -0.8
- HTF EMA9 Pierce: sim 15 · 67% · +20.6 (+20 / +9 / -8) | live 1 · 100% · +15.2
- HTF EMA20 Pierce: sim 7 · 71% · +10.4 (+4 / +11 / -4) | live –

## MGC 2m — sim 06/01 → 11/06 (1499 setups), live 144 setups since 10/19

Whole window 18:00–20:30: sim 119 · 50% · -34.5 (avg -0.29) vs rest of day avg +0.27 · live 20 · 55% · +6.1 vs rest 124 · 45% · -69.9

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 7 · 57% · +1.6 | +0 / +6 / -5 | – | 6 · 67% · +6.6 | 1 · 0% · -5.0 | – | – |
| 18:30–18:45 | 21 · 38% · -25.2 ⚠ weak | -11 / -5 / -10 | – | 5 · 40% · -7.3 | 10 · 40% · -4.5 ⚠ | 4 · 25% · -11.3 | 2 · 50% · -2.1 |
| 18:45–19:00 | 21 · 48% · -11.2 | -4 / +2 / -10 | 5 · 60% · +9.1 | 7 · 43% · -9.9 | 10 · 30% · -14.8 | 3 · 100% · +8.7 | 1 · 100% · +4.8 |
| 19:00–19:15 | 16 · 44% · -14.6 | -5 / -10 / +0 | 5 · 40% · -3.4 | 5 · 40% · -6.2 | 7 · 43% · -6.8 | 3 · 33% · -3.6 | 1 · 100% · +1.9 |
| 19:15–19:30 | 11 · 64% · +11.3 ✓ strong | +2 / +4 / +5 | 2 · 100% · +4.7 | 6 · 83% · +13.0 | 2 · 0% · -3.8 | 2 · 100% · +4.6 | 1 · 0% · -2.5 |
| 19:30–19:45 | 17 · 76% · +35.7 ✓ strong | +19 / +13 / +4 | 4 · 50% · +1.2 | 3 · 100% · +7.9 | 9 · 67% · +17.6 | 4 · 75% · +6.2 | 1 · 100% · +4.0 |
| 19:45–20:00 | 25 · 40% · -27.1 | -17 / -13 / +2 | 4 · 50% · -5.5 | 10 · 50% · -1.4 | 8 · 25% · -29.2 | 6 · 50% · +4.4 | 1 · 0% · -0.9 |
| 20:00–20:15 | 1 · 0% · -5.0 | +0 / +0 / -5 | – | – | 1 · 0% · -5.0 | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 42 · 57% · +2.7 (-23 / +18 / +8) | live 5 · 60% · +6.1
- LTF EMA20 Pierce: sim 48 · 38% · -51.5 (-9 / -20 / -22) | live 9 · 44% · -2.1
- HTF EMA9 Pierce: sim 22 · 59% · +9.1 (+8 / -1 / +2) | live 3 · 67% · -0.2
- HTF EMA20 Pierce: sim 7 · 57% · +5.2 (+8 / +2 / -5) | live 3 · 67% · +2.4

## MES 2m — sim 06/01 → 11/06 (1226 setups), live 116 setups since 10/19

Whole window 18:00–20:30: sim 85 · 46% · -57.7 (avg -0.68) vs rest of day avg -0.12 · live 8 · 25% · -19.6 vs rest 108 · 44% · -63.5

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 6 · 50% · +3.6 | +7 / +0 / -4 | – | 6 · 50% · +3.6 | – | – | – |
| 18:30–18:45 | 10 · 40% · -11.7 ⚠ weak | -3 / -5 / -4 | – | 3 · 0% · -10.1 | 5 · 40% · -4.9 | 1 · 100% · +1.5 | 1 · 100% · +1.8 |
| 18:45–19:00 | 12 · 42% · -13.5 ⚠ weak | -8 / -4 / -2 | – | 5 · 20% · -17.4 | 5 · 40% · -0.1 | 1 · 100% · +1.4 | 1 · 100% · +2.6 |
| 19:00–19:15 | 12 · 42% · -2.6 | -2 / +7 / -7 | 2 · 0% · -10.4 | 4 · 50% · +0.1 | 5 · 40% · +0.9 | 3 · 33% · -3.6 | – |
| 19:15–19:30 | 18 · 56% · -4.6 | -16 / +2 / +9 | 3 · 33% · -2.6 | 7 · 71% · +2.1 | 9 · 44% · -7.0 | 1 · 100% · +2.2 | 1 · 0% · -2.0 |
| 19:30–19:45 | 10 · 50% · -9.3 | +0 / +5 / -14 | 1 · 0% · -5.0 | 2 · 100% · +6.1 | 6 · 50% · -6.0 | 1 · 0% · -4.5 | 1 · 0% · -5.0 |
| 19:45–20:00 | 17 · 41% · -19.5 | -17 / -4 / +2 | 2 · 50% · -1.6 | 6 · 33% · -15.6 | 7 · 57% · +3.8 | 3 · 0% · -10.0 | 1 · 100% · +2.3 |
| 20:00–20:15 | – | – | – | – | – | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 33 · 45% · -31.2 (-17 / -13 / -0) | live 3 · 67% · +2.8
- LTF EMA20 Pierce: sim 37 · 46% · -13.4 (-11 / +6 / -8) | live 4 · 0% · -20.4
- HTF EMA9 Pierce: sim 10 · 40% · -12.9 (-7 / +5 / -11) | live –
- HTF EMA20 Pierce: sim 5 · 60% · -0.3 (-2 / +2 / -0) | live 1 · 0% · -2.0

## MGC 5m — sim 01/05 → 11/06 (1173 setups), live 49 setups since 10/20

Whole window 18:00–20:30: sim 86 · 52% · +14.8 (avg +0.17) vs rest of day avg -0.12 · live 6 · 50% · -5.5 vs rest 43 · 44% · -30.0

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 4 · 50% · -1.1 | +10 / -4 / -6 | – | – | 4 · 50% · -1.1 | – | – |
| 18:30–18:45 | 8 · 62% · +15.6 | -5 / +22 / -1 | – | – | 4 · 75% · +10.1 | 3 · 33% · -3.4 | 1 · 100% · +8.9 |
| 18:45–19:00 | 14 · 36% · -23.4 | -14 / -12 / +2 | 2 · 100% · +8.0 | 5 · 40% · -6.4 | 7 · 29% · -16.1 | 1 · 100% · +6.1 | 1 · 0% · -7.0 |
| 19:00–19:15 | 27 · 52% · +11.3 | +14 / -3 / +1 | 3 · 33% · -6.4 | 14 · 57% · +15.2 | 9 · 44% · -6.1 | 1 · 100% · +4.6 | 3 · 33% · -2.3 |
| 19:15–19:30 | 5 · 40% · -11.4 | -14 / -2 / +5 | – | – | 3 · 33% · -9.5 | 2 · 50% · -1.9 | – |
| 19:30–19:45 | 18 · 56% · +7.7 | +5 / +8 / -6 | 1 · 0% · -7.0 | 12 · 67% · +21.3 | 4 · 50% · -2.4 | 1 · 0% · -6.1 | 1 · 0% · -5.0 |
| 19:45–20:00 | 8 · 75% · +18.2 | +0 / +9 / +9 | – | – | 5 · 60% · +4.4 | 2 · 100% · +9.6 | 1 · 100% · +4.2 |
| 20:00–20:15 | 2 · 50% · -2.2 | -7 / +0 / +5 | – | – | 1 · 0% · -7.0 | – | 1 · 100% · +4.8 |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 31 · 58% · +30.0 (+21 / +14 / -5) | live 2 · 50% · -3.0
- LTF EMA20 Pierce: sim 37 · 46% · -27.7 (-20 / -5 / -3) | live 2 · 50% · -1.0
- HTF EMA9 Pierce: sim 10 · 60% · +8.9 (-14 / +15 / +8) | live 1 · 100% · +4.6
- HTF EMA20 Pierce: sim 8 · 50% · +3.6 (+2 / -6 / +7) | live 1 · 0% · -6.0

## MES 5m — sim 01/05 → 11/06 (1183 setups), live 58 setups since 10/20

Whole window 18:00–20:30: sim 71 · 52% · +22.9 (avg +0.32) vs rest of day avg -0.03 · live 5 · 40% · -4.5 vs rest 53 · 49% · -38.0

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 3 · 67% · +4.1 | +10 / +0 / -6 | – | – | 2 · 50% · -0.8 | 1 · 100% · +4.9 | – |
| 18:30–18:45 | 14 · 57% · +16.8 | +22 / -9 / +5 | – | – | 9 · 56% · +15.1 | 2 · 100% · +8.7 | 3 · 33% · -7.0 |
| 18:45–19:00 | 13 · 31% · -20.7 | -10 / +6 / -16 | 2 · 0% · -8.8 | 4 · 50% · +2.4 | 6 · 17% · -17.7 | 2 · 50% · -2.1 | 1 · 0% · -3.2 |
| 19:00–19:15 | 19 · 42% · -10.4 | -19 / +19 / -10 | – | 8 · 50% · -0.8 | 9 · 44% · -2.9 | 1 · 0% · -1.8 | 1 · 0% · -5.0 |
| 19:15–19:30 | 6 · 33% · -18.3 | +0 / -20 / +2 | 3 · 67% · +4.2 | – | 2 · 50% · -5.3 | 2 · 50% · -0.5 | 2 · 0% · -12.5 |
| 19:30–19:45 | 12 · 75% · +32.0 ✓ strong | +10 / +14 / +8 | – | 5 · 80% · +11.0 | 3 · 67% · +10.3 | 1 · 100% · +5.0 | 3 · 67% · +5.7 |
| 19:45–20:00 | 3 · 100% · +14.5 | +0 / +12 / +3 | – | – | 3 · 100% · +14.5 | – | – |
| 20:00–20:15 | 1 · 100% · +4.8 | +5 / +0 / +0 | – | – | 1 · 100% · +4.8 | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 17 · 59% · +12.6 (-3 / +21 / -5) | live 2 · 100% · +9.9
- LTF EMA20 Pierce: sim 35 · 51% · +18.0 (+12 / +10 / -4) | live 2 · 0% · -8.8
- HTF EMA9 Pierce: sim 9 · 67% · +14.3 (+9 / -0 / +6) | live –
- HTF EMA20 Pierce: sim 10 · 30% · -22.0 (+0 / -10 / -12) | live 1 · 0% · -5.7

## Flags (weak cells: ≥ 10 sim setups, negative in all thirds)

- MGC 2m 18:30–18:45 all triggers: 21 · 38% · -25.2, thirds -11 / -5 / -10
- MGC 2m 18:30–18:45 LTF EMA20 Pierce: 10 · 40% · -4.5, thirds -1 / -4 / -0
- MES 2m 18:30–18:45 all triggers: 10 · 40% · -11.7, thirds -3 / -5 / -4
- MES 2m 18:45–19:00 all triggers: 12 · 42% · -13.5, thirds -8 / -4 / -2
