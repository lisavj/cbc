# Evening session study — weekly check Wed 10/28/2026 18:20 ET (summary)

## Since last week (vs the first run 10/28 09:08 ET)

Note: this run fired the same day as the first run (Wed 10/28 evening, not a Friday), so it adds only the 10/28 session and **does not count as a new weekly check** — every candidate stays at 1 of the 3 required checks. MES 3m sim numbers moved because the simulator now applies the v10.42 base exits for MES 3m (set in evening_study.py); the other charts barely changed.

- **MGC 3m:** window +0.55/setup vs +0.12 rest of day (unchanged, 143 sim setups). Weak 19:15–19:30 (21 · −28.3) still flagged; strong 19:30–19:45 still. Live 8 window setups +6.9 (no new), rest 28 (was 24).
- **MES 3m:** window +0.75 vs −0.05 (was +0.53 vs −0.10). Strong cell moved from 19:45–20:00 to 18:30–18:45. **Candidate "skip HTF CBC Flip in the window" weakened:** 15 sim · −5.0, thirds −10 / +1 / +4 (was −31.6, negative in all thirds). Live 6 window setups −5.4 (no new), rest 57 (was 51).
- **MGC 2m:** window −0.23 vs +0.30 (unchanged). Weak 18:30–18:45 still (20 · −18.2). Candidate "skip LTF EMA20 Pierce in the window": sim 45 · −50.1, thirds −9 / −12 / −29 (still negative in all thirds); live 5 · +0.2 (not negative, < 10). Live window 10 (+3.5), rest 59.
- **MES 2m:** window −0.73 vs −0.10 (unchanged). Weak 19:45–20:00 still (16 · −22.9). Candidate "no new setups 18:45–20:00": sim 67 · −47.6, thirds −40 / −6 / −1 (all negative); live 6 · −17.6 (needs ≥ 10). Live rest 68 (was 65).
- **MGC 5m:** window +0.16 vs −0.06 (unchanged). Weak 18:45–19:00 still (13 · −27.4). Live 21 total, 2 in window (no new).
- **MES 5m:** window +0.30 vs −0.01 (unchanged). No weak cells; strong 19:30–19:45. Live 33 total (was 31), 5 in window (no new).

**Verdict:** nothing meets the rule (all-thirds-negative sim with ≥ 20 setups, 3 consecutive weekly checks, ≥ 10 live setups net negative). Closest: MES 2m 18:45–20:00 (sim fits, live only 6) and MGC 2m LTF EMA20 Pierce in the window (sim fits, live 5 and positive). A per-chart evening time block would need a CBC Pine change. No Pine or server change made.

---

# Evening session 18:00–20:30 ET in 15-minute buckets — Wed 10/28/2026 18:22 ET

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

## MGC 3m — sim 01/05 → 10/28 (1140 setups), live 36 setups since 10/19

Whole window 18:00–20:30: sim 143 · 44% · +79.1 (avg +0.55) vs rest of day avg +0.12 · live 8 · 50% · +6.9 vs rest 28 · 43% · -14.8

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 5 · 20% · -11.6 | +0 / -8 / -4 | – | 1 · 0% · -2.7 | 3 · 33% · -7.5 | – | 1 · 0% · -1.4 |
| 18:30–18:45 | 21 · 48% · +1.9 | -2 / +2 / +2 | – | 4 · 25% · -4.8 | 9 · 56% · +2.9 | 6 · 33% · -15.5 | 2 · 100% · +19.3 |
| 18:45–19:00 | 23 · 43% · -1.5 | -7 / +5 / +1 | 3 · 33% · -0.6 | 6 · 67% · +2.4 | 13 · 38% · +1.3 | 2 · 0% · -6.4 | 2 · 50% · +1.1 |
| 19:00–19:15 | 26 · 35% · +40.2 | +15 / +36 / -11 | – | 9 · 44% · +22.1 | 8 · 50% · +45.2 | 5 · 0% · -17.3 | 4 · 25% · -9.7 |
| 19:15–19:30 | 21 · 33% · -28.3 ⚠ weak | -1 / -21 / -6 | 2 · 50% · -0.1 | 4 · 50% · -2.5 | 10 · 30% · -16.0 | 3 · 67% · -0.0 | 4 · 0% · -9.8 |
| 19:30–19:45 | 21 · 67% · +40.2 ✓ strong | +2 / +31 / +7 | 1 · 0% · -2.1 | 6 · 67% · +14.8 | 13 · 69% · +31.1 | – | 2 · 50% · -5.7 |
| 19:45–20:00 | 26 · 46% · +38.2 | +37 / -12 / +13 | 2 · 100% · +9.7 | 5 · 40% · +5.7 | 13 · 38% · +27.2 | 5 · 60% · +5.9 | 3 · 67% · -0.5 |
| 20:00–20:15 | – | – | – | – | – | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 35 · 49% · +35.0 (+7 / +16 / +12) | live 1 · 100% · +3.1
- LTF EMA20 Pierce: sim 69 · 46% · +84.1 (+62 / +19 / +4) | live 7 · 43% · +3.8
- HTF EMA9 Pierce: sim 21 · 33% · -33.4 (-23 / +4 / -14) | live –
- HTF EMA20 Pierce: sim 18 · 39% · -6.7 (-1 / -5 / -1) | live –

## MES 3m — sim 01/05 → 10/28 (1669 setups), live 63 setups since 10/19

Whole window 18:00–20:30: sim 102 · 55% · +76.4 (avg +0.75) vs rest of day avg -0.05 · live 6 · 33% · -5.4 vs rest 57 · 40% · -53.0

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 5 · 60% · +6.1 | -3 / +10 / -1 | – | 2 · 50% · +1.8 | 3 · 67% · +4.3 | – | – |
| 18:30–18:45 | 16 · 56% · +21.0 ✓ strong | +10 / +11 / +0 | – | 4 · 50% · -1.4 | 8 · 50% · +14.6 | 2 · 100% · +8.2 | 2 · 50% · -0.5 |
| 18:45–19:00 | 14 · 43% · -9.3 | +1 / -9 / -1 | 1 · 100% · +3.0 | 2 · 0% · -13.0 | 9 · 44% · -2.3 | 3 · 67% · +6.0 | – |
| 19:00–19:15 | 19 · 53% · +14.9 | +16 / -8 / +7 | 2 · 50% · +1.3 | 1 · 0% · -5.0 | 13 · 54% · +14.2 ✓ | 4 · 50% · +2.0 | 1 · 100% · +3.6 |
| 19:15–19:30 | 15 · 67% · +15.5 | +13 / -4 / +6 | 1 · 0% · -2.4 | 2 · 100% · +9.4 | 9 · 56% · -3.5 | 1 · 100% · +5.4 | 3 · 67% · +4.2 |
| 19:30–19:45 | 15 · 47% · +7.8 | +17 / -0 / -9 | 2 · 0% · -7.2 | 1 · 100% · +2.0 | 12 · 33% · -1.3 | 2 · 100% · +7.0 | – |
| 19:45–20:00 | 17 · 59% · +16.3 | -4 / +10 / +10 | – | 3 · 67% · +1.2 | 12 · 50% · +7.0 | 1 · 100% · +4.9 | 1 · 100% · +3.2 |
| 20:00–20:15 | 1 · 100% · +4.2 | +4 / +0 / +0 | – | – | 1 · 100% · +4.2 | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 15 · 53% · -5.0 (-10 / +1 / +4) | live 1 · 0% · -2.4
- LTF EMA20 Pierce: sim 67 · 49% · +37.4 (+41 / -7 / +4) | live 5 · 40% · -3.0
- HTF EMA9 Pierce: sim 13 · 77% · +33.6 (+20 / +9 / +5) | live –
- HTF EMA20 Pierce: sim 7 · 71% · +10.4 (+4 / +8 / -1) | live –

## MGC 2m — sim 06/01 → 10/28 (1409 setups), live 69 setups since 10/19

Whole window 18:00–20:30: sim 111 · 50% · -25.1 (avg -0.23) vs rest of day avg +0.30 · live 10 · 60% · +3.5 vs rest 59 · 51% · -2.6

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 7 · 57% · +1.6 | +2 / +4 / -5 | – | 6 · 67% · +6.6 | 1 · 0% · -5.0 | – | – |
| 18:30–18:45 | 20 · 40% · -18.2 ⚠ weak | -11 / -6 / -1 | – | 5 · 40% · -7.3 | 10 · 40% · -4.5 ⚠ | 3 · 33% · -4.3 | 2 · 50% · -2.1 |
| 18:45–19:00 | 18 · 44% · -15.9 | -4 / +2 / -14 | 3 · 33% · -2.5 | 5 · 40% · -7.1 | 9 · 22% · -22.2 | 3 · 100% · +8.7 | 1 · 100% · +4.8 |
| 19:00–19:15 | 14 · 50% · -10.2 | +1 / -16 / +5 | 2 · 50% · +1.9 | 4 · 50% · -5.6 | 6 · 50% · -3.0 | 3 · 33% · -3.6 | 1 · 100% · +1.9 |
| 19:15–19:30 | 11 · 64% · +11.3 | +7 / -2 / +6 | 2 · 100% · +4.7 | 6 · 83% · +13.0 | 2 · 0% · -3.8 | 2 · 100% · +4.6 | 1 · 0% · -2.5 |
| 19:30–19:45 | 16 · 75% · +33.4 ✓ strong | +19 / +10 / +4 | 1 · 100% · +2.5 | 3 · 100% · +7.9 | 9 · 67% · +17.6 | 3 · 67% · +3.9 | 1 · 100% · +4.0 |
| 19:45–20:00 | 24 · 42% · -22.1 | -17 / -8 / +2 | 2 · 50% · -3.1 | 10 · 50% · -1.4 | 7 · 29% · -24.2 | 6 · 50% · +4.4 | 1 · 0% · -0.9 |
| 20:00–20:15 | 1 · 0% · -5.0 | +0 / +0 / -5 | – | – | 1 · 0% · -5.0 | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 39 · 59% · +6.0 (-10 / +1 / +15) | live 1 · 0% · -5.0
- LTF EMA20 Pierce: sim 45 · 38% · -50.1 (-9 / -12 / -29) | live 5 · 40% · +0.2
- HTF EMA9 Pierce: sim 20 · 60% · +13.8 (+8 / -5 / +11) | live 2 · 100% · +4.8
- HTF EMA20 Pierce: sim 7 · 57% · +5.2 (+8 / +2 / -5) | live 2 · 100% · +3.5

## MES 2m — sim 06/01 → 10/28 (1149 setups), live 74 setups since 10/19

Whole window 18:00–20:30: sim 82 · 45% · -60.2 (avg -0.73) vs rest of day avg -0.10 · live 6 · 17% · -17.6 vs rest 68 · 37% · -104.3

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 6 · 50% · +3.6 | +7 / +0 / -4 | – | 6 · 50% · +3.6 | – | – | – |
| 18:30–18:45 | 9 · 33% · -16.2 | -5 / -1 / -10 | – | 3 · 0% · -10.1 | 4 · 25% · -9.4 | 1 · 100% · +1.5 | 1 · 100% · +1.8 |
| 18:45–19:00 | 12 · 42% · -13.5 | -8 / -7 / +1 | – | 5 · 20% · -17.4 | 5 · 40% · -0.1 | 1 · 100% · +1.4 | 1 · 100% · +2.6 |
| 19:00–19:15 | 11 · 45% · +2.8 | -0 / +1 / +2 | 1 · 0% · -5.0 | 4 · 50% · +0.1 | 5 · 40% · +0.9 | 2 · 50% · +1.8 | – |
| 19:15–19:30 | 18 · 56% · -4.6 | -16 / -0 / +11 | 3 · 33% · -2.6 | 7 · 71% · +2.1 | 9 · 44% · -7.0 | 1 · 100% · +2.2 | 1 · 0% · -2.0 |
| 19:30–19:45 | 10 · 50% · -9.3 | +0 / +5 / -14 | 1 · 0% · -5.0 | 2 · 100% · +6.1 | 6 · 50% · -6.0 | 1 · 0% · -4.5 | 1 · 0% · -5.0 |
| 19:45–20:00 | 16 · 38% · -22.9 ⚠ weak | -17 / -5 / -1 | 1 · 0% · -5.0 | 5 · 20% · -19.0 | 7 · 57% · +3.8 | 3 · 0% · -10.0 | 1 · 100% · +2.3 |
| 20:00–20:15 | – | – | – | – | – | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 32 · 44% · -34.6 (-17 / -12 / -6) | live 2 · 50% · -0.6
- LTF EMA20 Pierce: sim 36 · 44% · -17.8 (-13 / +1 / -6) | live 3 · 0% · -15.0
- HTF EMA9 Pierce: sim 9 · 44% · -7.5 (-5 / +1 / -4) | live –
- HTF EMA20 Pierce: sim 5 · 60% · -0.3 (-2 / +2 / -0) | live 1 · 0% · -2.0

## MGC 5m — sim 01/05 → 10/28 (1134 setups), live 21 setups since 10/20

Whole window 18:00–20:30: sim 83 · 52% · +13.2 (avg +0.16) vs rest of day avg -0.06 · live 2 · 50% · -1.0 vs rest 19 · 47% · -1.8

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 4 · 50% · -1.1 | +10 / -4 / -6 | – | – | 4 · 50% · -1.1 | – | – |
| 18:30–18:45 | 8 · 62% · +15.6 | -5 / +17 / +4 | – | – | 4 · 75% · +10.1 | 3 · 33% · -3.4 | 1 · 100% · +8.9 |
| 18:45–19:00 | 13 · 31% · -27.4 ⚠ weak | -14 / -12 / -1 | 1 · 100% · +4.0 | 4 · 25% · -10.4 | 7 · 29% · -16.1 | 1 · 100% · +6.1 | 1 · 0% · -7.0 |
| 19:00–19:15 | 26 · 50% · +6.7 | +14 / -3 / -4 | 1 · 0% · -5.0 | 14 · 57% · +15.2 | 9 · 44% · -6.1 | – | 3 · 33% · -2.3 |
| 19:15–19:30 | 5 · 40% · -11.4 | -14 / -2 / +5 | – | – | 3 · 33% · -9.5 | 2 · 50% · -1.9 | – |
| 19:30–19:45 | 17 · 59% · +14.7 ✓ strong | +5 / +8 / +1 | – | 11 · 73% · +28.3 ✓ | 4 · 50% · -2.4 | 1 · 0% · -6.1 | 1 · 0% · -5.0 |
| 19:45–20:00 | 8 · 75% · +18.2 | +0 / +9 / +9 | – | – | 5 · 60% · +4.4 | 2 · 100% · +9.6 | 1 · 100% · +4.2 |
| 20:00–20:15 | 2 · 50% · -2.2 | -7 / +0 / +5 | – | – | 1 · 0% · -7.0 | – | 1 · 100% · +4.8 |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 29 · 59% · +33.0 (+21 / +19 / -7) | live –
- LTF EMA20 Pierce: sim 37 · 46% · -27.7 (-20 / -10 / +2) | live 2 · 50% · -1.0
- HTF EMA9 Pierce: sim 9 · 56% · +4.3 (-14 / +9 / +10) | live –
- HTF EMA20 Pierce: sim 8 · 50% · +3.6 (+2 / -6 / +7) | live –

## MES 5m — sim 01/05 → 10/28 (1154 setups), live 33 setups since 10/20

Whole window 18:00–20:30: sim 70 · 51% · +21.2 (avg +0.30) vs rest of day avg -0.01 · live 5 · 40% · -4.5 vs rest 28 · 50% · -19.0

| Bucket (ET) | Sim all | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|
| 18:00–18:15 | – | – | – | – | – | – | – |
| 18:15–18:30 | 3 · 67% · +4.1 | +10 / +0 / -6 | – | – | 2 · 50% · -0.8 | 1 · 100% · +4.9 | – |
| 18:30–18:45 | 13 · 54% · +15.1 | +22 / -14 / +8 | – | – | 9 · 56% · +15.1 | 2 · 100% · +8.7 | 2 · 0% · -8.8 |
| 18:45–19:00 | 13 · 31% · -20.7 | -10 / +1 / -12 | 2 · 0% · -8.8 | 4 · 50% · +2.4 | 6 · 17% · -17.7 | 2 · 50% · -2.1 | 1 · 0% · -3.2 |
| 19:00–19:15 | 19 · 42% · -10.4 | -19 / +19 / -10 | – | 8 · 50% · -0.8 | 9 · 44% · -2.9 | 1 · 0% · -1.8 | 1 · 0% · -5.0 |
| 19:15–19:30 | 6 · 33% · -18.3 | +0 / -20 / +2 | 3 · 67% · +4.2 | – | 2 · 50% · -5.3 | 2 · 50% · -0.5 | 2 · 0% · -12.5 |
| 19:30–19:45 | 12 · 75% · +32.0 ✓ strong | +10 / +9 / +13 | – | 5 · 80% · +11.0 | 3 · 67% · +10.3 | 1 · 100% · +5.0 | 3 · 67% · +5.7 |
| 19:45–20:00 | 3 · 100% · +14.5 | +0 / +12 / +3 | – | – | 3 · 100% · +14.5 | – | – |
| 20:00–20:15 | 1 · 100% · +4.8 | +5 / +0 / +0 | – | – | 1 · 100% · +4.8 | – | – |
| 20:15–20:30 | – | – | – | – | – | – | – |

**Whole window by trigger** (sim N · win · net, thirds | live)

- HTF CBC Flip: sim 17 · 59% · +12.6 (-3 / +16 / +0) | live 2 · 100% · +9.9
- LTF EMA20 Pierce: sim 35 · 51% · +18.0 (+12 / +5 / +0) | live 2 · 0% · -8.8
- HTF EMA9 Pierce: sim 9 · 67% · +14.3 (+9 / -5 / +11) | live –
- HTF EMA20 Pierce: sim 9 · 22% · -23.8 (+0 / -10 / -14) | live 1 · 0% · -5.7

## Flags (weak cells: ≥ 10 sim setups, negative in all thirds)

- MGC 3m 19:15–19:30 all triggers: 21 · 33% · -28.3, thirds -1 / -21 / -6
- MGC 2m 18:30–18:45 all triggers: 20 · 40% · -18.2, thirds -11 / -6 / -1
- MGC 2m 18:30–18:45 LTF EMA20 Pierce: 10 · 40% · -4.5, thirds -1 / -4 / -0
- MES 2m 19:45–20:00 all triggers: 16 · 38% · -22.9, thirds -17 / -5 / -1
- MGC 5m 18:45–19:00 all triggers: 13 · 31% · -27.4, thirds -14 / -12 / -1
