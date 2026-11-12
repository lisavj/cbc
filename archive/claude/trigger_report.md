# Setup Triggers study -- 2026-11-07 09:50 ET (weekly run 2 — rerun after data repair, replaces the 11/06 run)

Replay Jan 5 – Nov 6 (2m Jun – Nov 6), each chart on its live settings, base exits; Δ = turning that trigger OFF. Live = alert store (Trade Setup → Setup Ended), ~10/19 – 11/06. Previous report: 2026-11-06 21:17 ET (pre-repair run 2, now replaced). Method unchanged (scripts ran as-is, no fixes).

**Rerun after data repair:** requested 11/07 after the BarFeed bar data was repaired (MGC 3m had 5m candles mixed in; MCL 2m / M2K 2m had wrong candles; MES 2m/5m, MNQ, M2K 3m had gaps). This run **replaces the 11/06 21:17 run as weekly run 2** (run history: run 1 = 11/01, run 2 = this run; consecutive-robust counts recomputed on that basis — still 0 everywhere). An earlier 11/07 09:46 pass produced byte-identical outputs, so the repaired data was already in place. Versus the pre-repair 11/06 numbers: MES 3m, MGC 3m, MES 2m and MGC 2m replays moved (biggest on MGC 3m: net +186 → +278); MES 5m and MGC 5m replays and the live table are unchanged. Comparisons below are to the 11/06 run (pre-repair) and run 1.

## Since last week

**Verdict: keep all triggers.** No "trigger OFF" is robust on any chart (0 consecutive robust runs everywhere), so rule (a) fails for every candidate.

**Replay, per chart (net of the trigger's own setups; OFF Δ / z / thirds / verdict — this run vs the pre-repair 11/06 run; run 1 = 11/01)**
- **MES 3m:** HTF EMA9 Pierce 285 setups −137 (11/06 −142, run 1 −116), negative in all thirds (−18 / −67 / −51). OFF +145, z 1.6, +25 / +55 / +65 — promising (11/06 +158 z 1.7; run 1 +111 z 1.2). Still the strongest candidate but not robust; live HTF EMA9 Pierce +10.6 on 12 ended (< 20 and positive) → (c) fails. HTF CBC Flip carries the chart: +84, OFF −162, z −1.5 (worse in 2 of 3 thirds).
- **MGC 3m:** keep all. HTF EMA9 Pierce −88 (was −97), OFF +35, z 0.4, +58 / −19 / −4 — noise. HTF EMA20 Pierce +91 (OFF −76, z −0.9); Flip +127 (OFF −18); LTF EMA20 +147 (OFF −41).
- **MES 2m:** LTF EMA20 Pierce 527 setups −147 (was −161), negative in 2 of 3 thirds (−75 / +6 / −79). OFF +109, z 1.1, +32 / +20 / +58 — promising (11/06 +123 z 1.2; run 1 +132 z 1.3). Live 51 ended −37.6 (unchanged). (b) and (c) met; (a) not (0 robust runs). Others: Flip −38 (OFF +39 noise), EMA9 +2 (OFF +24 noise), EMA20 −3 (OFF −22 worse).
- **MGC 2m:** LTF EMA20 Pierce carries the chart: +352, positive all thirds; OFF −219, z −1.8, −131 / −9 / −79 (worse in all thirds, short of z −2). HTF EMA9 OFF +47 noise. Keep all.
- **MES 5m:** identical to 11/06. LTF EMA20 Pierce −101 (−169 / +54 / +14), OFF +140, z 1.0, +126 / +14 / −1 — noise (run 1 promising, z 1.1). Live 24 ended −29.7. The chart-EMA 16 / 34 / 120 candidate (weekly EMA check) addresses the same trigger — prefer whichever qualifies first; neither does yet. HTF EMA9 (+66, OFF −84) and HTF EMA20 (+68, OFF −44) remain the winners.
- **MGC 5m:** identical to 11/06. HTF EMA9 Pierce −84 (−64 / +51 / −71), OFF +114, z 1.3, +52 / −9 / +71 — noise. Live HTF EMA9 Pierce +18.4 on 6. Keep all.

**Live, per trigger (ended setups, net) — unchanged vs the 11/06 run (no new session; alert store not affected by the bar repair)**
- LTF EMA20 Pierce: MES 2m 51 −37.6; MES 5m 24 −29.7; MGC 3m 32 −18.6; MES 3m 45 +9.6; MGC 2m 51 +12.1; MGC 5m 14 +0.5; MNQ 3m 43 −748.8; MNQ 2m 42 −78.0; MNQ 5m 23 +362.6; M2K 2m 28 +26.4; M2K 3m 21 +0.3; M2K 5m 19 −23.0.
- HTF CBC Flip: MES 3m +41.7; MES 2m −1.2; MES 5m +6.2; MGC 3m +5.7; MGC 5m +5.9; MGC 2m −16.0; MNQ 2m +24.1; MNQ 3m −265.5; MNQ 5m −65.5; M2K 2m −29.1.
- HTF EMA9 Pierce: MES 3m +10.6 (12); MGC 3m +3.6; MGC 5m +18.4; MNQ 3m +147.5; MNQ 2m +49.5.
- "LTF EMA20 Pierce (late)" still weak: MGC 5m 10 ended 0 % win −54.8; MGC 2m −33.1; MES 2m −33.4; MES 3m −27.7; MGC 3m −10.6.

**Candidates (consecutive robust runs: 0 for all):** MES 3m untick "Trigger: HTF EMA9 Pierce" (z 1.2 → 1.7 → 1.6, promising); MES 2m untick "Trigger: LTF EMA20 Pierce" (z 1.3 → 1.2 → 1.1, promising, slowly fading); MES 5m LTF EMA20 Pierce (noise; 16 / 34 / 120 may qualify first). **Carrying:** HTF CBC Flip on MES 3m, LTF EMA20 Pierce on MGC 2m (near-robustly worse when off). No Pine or server changes.

Not in the replay: LTF EMA20 Touch, Momentum break, HTF Pullback Structure (only live, few setups).

---

## Live Trade Setups by first trigger (alert store, with Setup Ended results)

| Chart | Trigger | Setups | Ended | Win % | Net | Avg |
|---|---|---|---|---|---|---|
| M2K 2m | HTF CBC Flip | 16 | 16 | 31% | -29.1 | -1.82 |
| M2K 2m | HTF EMA20 Pierce | 5 | 5 | 80% | +9.3 | +1.86 |
| M2K 2m | HTF EMA20 Pierce (late) | 2 | 2 | 50% | -2.0 | -1.00 |
| M2K 2m | HTF EMA9 Pierce | 7 | 7 | 86% | +11.3 | +1.62 |
| M2K 2m | HTF EMA9 Pierce (late) | 2 | 2 | 100% | +5.5 | +2.77 |
| M2K 2m | HTF Pullback Structure | 1 | 1 | 0% | -0.6 | -0.60 |
| M2K 2m | LTF EMA20 Pierce | 30 | 28 | 68% | +26.4 | +0.94 |
| M2K 2m | LTF EMA20 Pierce (late) | 12 | 11 | 45% | +3.4 | +0.31 |
| M2K 3m | HTF CBC Flip | 9 | 8 | 50% | -7.3 | -0.92 |
| M2K 3m | HTF EMA20 Pierce | 8 | 8 | 25% | -12.1 | -1.51 |
| M2K 3m | HTF EMA9 Pierce | 2 | 2 | 100% | +5.7 | +2.84 |
| M2K 3m | HTF Pullback Structure | 1 | 1 | 100% | +3.5 | +3.49 |
| M2K 3m | LTF EMA20 Pierce | 21 | 21 | 48% | +0.3 | +0.01 |
| M2K 3m | LTF EMA20 Pierce (late) | 16 | 15 | 67% | +7.3 | +0.49 |
| M2K 5m | HTF CBC Flip | 9 | 7 | 29% | -12.9 | -1.84 |
| M2K 5m | HTF EMA20 Pierce | 6 | 6 | 50% | -3.9 | -0.65 |
| M2K 5m | HTF EMA20 Pierce (late) | 3 | 3 | 67% | +2.8 | +0.93 |
| M2K 5m | HTF EMA9 Pierce | 4 | 4 | 50% | -3.3 | -0.83 |
| M2K 5m | HTF EMA9 Pierce (late) | 2 | 2 | 50% | -1.4 | -0.68 |
| M2K 5m | HTF Pullback Structure | 1 | 1 | 0% | -5.0 | -5.00 |
| M2K 5m | LTF EMA20 Pierce | 19 | 19 | 37% | -23.0 | -1.21 |
| M2K 5m | LTF EMA20 Pierce (late) | 5 | 5 | 60% | +2.9 | +0.58 |
| M2K 5m | LTF EMA20 Touch (mid-candle) | 1 | 1 | 0% | -2.1 | -2.10 |
| MCL 2m | HTF CBC Flip | 1 | 1 | 100% | +0.3 | +0.31 |
| MCL 2m | HTF EMA20 Pierce | 5 | 5 | 60% | +0.5 | +0.11 |
| MCL 2m | HTF EMA20 Pierce (late) | 1 | 1 | 0% | -0.1 | -0.10 |
| MCL 2m | HTF EMA9 Pierce | 15 | 14 | 54% | +1.2 | +0.09 |
| MCL 2m | HTF EMA9 Pierce (late) | 4 | 4 | 75% | +0.6 | +0.14 |
| MCL 2m | HTF Pullback Structure | 1 | 1 | 0% | -0.3 | -0.30 |
| MCL 2m | LTF EMA20 Pierce | 31 | 27 | 52% | +0.6 | +0.02 |
| MCL 2m | LTF EMA20 Pierce (late) | 19 | 15 | 60% | +1.0 | +0.07 |
| MCL 3m | HTF CBC Flip | 1 | 1 | 0% | -0.2 | -0.19 |
| MCL 3m | HTF EMA20 Pierce | 4 | 4 | 50% | -0.1 | -0.02 |
| MCL 3m | HTF EMA20 Pierce (late) | 1 | 1 | 100% | +0.3 | +0.26 |
| MCL 3m | HTF EMA9 Pierce | 4 | 3 | 0% | -0.5 | -0.16 |
| MCL 3m | HTF EMA9 Pierce (late) | 6 | 4 | 25% | -0.5 | -0.13 |
| MCL 3m | LTF EMA20 Pierce | 32 | 30 | 60% | +1.7 | +0.06 |
| MCL 3m | LTF EMA20 Pierce (late) | 14 | 13 | 46% | -0.5 | -0.04 |
| MCL 5m | HTF CBC Flip | 2 | 2 | 50% | -0.1 | -0.03 |
| MCL 5m | HTF EMA20 Pierce | 2 | 2 | 50% | -0.1 | -0.03 |
| MCL 5m | HTF EMA20 Pierce (late) | 1 | 1 | 100% | +0.3 | +0.35 |
| MCL 5m | HTF EMA9 Pierce | 1 | 1 | 100% | +0.3 | +0.30 |
| MCL 5m | HTF EMA9 Pierce (late) | 2 | 1 | 0% | -0.3 | -0.30 |
| MCL 5m | LTF EMA20 Pierce | 25 | 23 | 35% | -2.2 | -0.10 |
| MCL 5m | LTF EMA20 Pierce (late) | 2 | 2 | 0% | -0.6 | -0.30 |
| MES 2m | HTF CBC Flip | 34 | 31 | 52% | -1.2 | -0.04 |
| MES 2m | HTF EMA20 Pierce | 10 | 10 | 30% | -7.8 | -0.78 |
| MES 2m | HTF EMA20 Pierce (late) | 2 | 1 | 100% | +2.0 | +2.00 |
| MES 2m | HTF EMA9 Pierce | 7 | 7 | 57% | +4.9 | +0.70 |
| MES 2m | HTF EMA9 Pierce (late) | 3 | 2 | 0% | -6.1 | -3.06 |
| MES 2m | HTF Pullback Structure | 1 | 1 | 0% | -8.0 | -8.00 |
| MES 2m | LTF EMA20 Pierce | 55 | 51 | 41% | -37.6 | -0.74 |
| MES 2m | LTF EMA20 Pierce (late) | 14 | 14 | 36% | -33.4 | -2.38 |
| MES 3m | HTF CBC Flip | 17 | 15 | 60% | +41.7 | +2.78 |
| MES 3m | HTF EMA20 Pierce | 7 | 5 | 20% | -5.8 | -1.17 |
| MES 3m | HTF EMA20 Pierce (late) | 3 | 3 | 67% | +0.8 | +0.26 |
| MES 3m | HTF EMA9 Pierce | 13 | 12 | 50% | +10.6 | +0.89 |
| MES 3m | HTF EMA9 Pierce (late) | 2 | 2 | 0% | -5.9 | -2.94 |
| MES 3m | HTF Pullback Structure | 2 | 2 | 0% | -9.1 | -4.54 |
| MES 3m | LTF EMA20 Pierce | 51 | 45 | 51% | +9.6 | +0.21 |
| MES 3m | LTF EMA20 Pierce (late) | 21 | 20 | 40% | -27.7 | -1.38 |
| MES 5m | HTF CBC Flip | 16 | 14 | 64% | +6.2 | +0.45 |
| MES 5m | HTF EMA20 Pierce | 6 | 6 | 50% | -4.2 | -0.70 |
| MES 5m | HTF EMA20 Pierce (late) | 2 | 2 | 100% | +9.1 | +4.56 |
| MES 5m | HTF EMA9 Pierce | 2 | 1 | 0% | -8.0 | -8.00 |
| MES 5m | HTF EMA9 Pierce (late) | 1 | 1 | 0% | -5.5 | -5.50 |
| MES 5m | HTF Pullback Structure | 1 | 1 | 0% | -5.8 | -5.75 |
| MES 5m | LTF EMA20 Pierce | 25 | 24 | 42% | -29.7 | -1.24 |
| MES 5m | LTF EMA20 Pierce (late) | 11 | 9 | 44% | -4.7 | -0.53 |
| MGC 2m | HTF CBC Flip | 41 | 38 | 50% | -16.0 | -0.42 |
| MGC 2m | HTF EMA20 Pierce | 14 | 12 | 33% | -20.1 | -1.68 |
| MGC 2m | HTF EMA20 Pierce (late) | 4 | 3 | 33% | -4.4 | -1.47 |
| MGC 2m | HTF EMA9 Pierce | 13 | 11 | 64% | +5.9 | +0.54 |
| MGC 2m | HTF EMA9 Pierce (late) | 5 | 5 | 40% | -3.2 | -0.63 |
| MGC 2m | HTF Pullback Structure | 1 | 1 | 0% | -5.0 | -5.00 |
| MGC 2m | LTF EMA20 Pierce | 56 | 51 | 49% | +12.1 | +0.24 |
| MGC 2m | LTF EMA20 Pierce (late) | 23 | 23 | 39% | -33.1 | -1.44 |
| MGC 3m | HTF CBC Flip | 7 | 5 | 80% | +5.7 | +1.13 |
| MGC 3m | HTF EMA20 Pierce | 11 | 10 | 50% | -5.9 | -0.59 |
| MGC 3m | HTF EMA9 Pierce | 10 | 8 | 50% | +3.6 | +0.45 |
| MGC 3m | HTF EMA9 Pierce (late) | 3 | 3 | 33% | -4.4 | -1.46 |
| MGC 3m | HTF Pullback Structure | 1 | 1 | 0% | -6.9 | -6.91 |
| MGC 3m | LTF EMA20 Pierce | 37 | 32 | 34% | -18.6 | -0.58 |
| MGC 3m | LTF EMA20 Pierce (late) | 10 | 10 | 40% | -10.6 | -1.06 |
| MGC 5m | HTF CBC Flip | 13 | 13 | 62% | +5.9 | +0.45 |
| MGC 5m | HTF EMA20 Pierce | 4 | 3 | 33% | -1.5 | -0.50 |
| MGC 5m | HTF EMA20 Pierce (late) | 1 | 1 | 100% | +4.8 | +4.80 |
| MGC 5m | HTF EMA9 Pierce | 6 | 6 | 83% | +18.4 | +3.06 |
| MGC 5m | HTF EMA9 Pierce (late) | 2 | 2 | 0% | -8.7 | -4.36 |
| MGC 5m | LTF EMA20 Pierce | 15 | 14 | 50% | +0.5 | +0.04 |
| MGC 5m | LTF EMA20 Pierce (late) | 11 | 10 | 0% | -54.8 | -5.48 |
| MNQ 2m | HTF CBC Flip | 52 | 47 | 45% | +24.1 | +0.51 |
| MNQ 2m | HTF EMA20 Pierce | 15 | 15 | 33% | -93.2 | -6.22 |
| MNQ 2m | HTF EMA20 Pierce (late) | 3 | 3 | 33% | -21.9 | -7.30 |
| MNQ 2m | HTF EMA9 Pierce | 21 | 20 | 45% | +49.5 | +2.48 |
| MNQ 2m | HTF EMA9 Pierce (late) | 3 | 3 | 67% | +90.8 | +30.26 |
| MNQ 2m | HTF Pullback Structure | 3 | 3 | 33% | -57.5 | -19.17 |
| MNQ 2m | LTF EMA20 Pierce | 46 | 42 | 36% | -78.0 | -1.86 |
| MNQ 2m | LTF EMA20 Pierce (late) | 13 | 13 | 46% | -41.5 | -3.19 |
| MNQ 3m | HTF CBC Flip | 33 | 29 | 31% | -265.5 | -9.15 |
| MNQ 3m | HTF EMA20 Pierce | 15 | 14 | 43% | -56.0 | -4.00 |
| MNQ 3m | HTF EMA9 Pierce | 6 | 6 | 83% | +147.5 | +24.59 |
| MNQ 3m | HTF EMA9 Pierce (late) | 3 | 3 | 33% | -25.3 | -8.43 |
| MNQ 3m | LTF EMA20 Pierce | 47 | 43 | 16% | -748.8 | -17.41 |
| MNQ 3m | LTF EMA20 Pierce (late) | 9 | 9 | 44% | +33.7 | +3.74 |
| MNQ 3m | LTF EMA20 Touch (mid-candle) | 1 | 1 | 0% | -30.0 | -30.00 |
| MNQ 5m | HTF CBC Flip | 11 | 9 | 33% | -65.5 | -7.27 |
| MNQ 5m | HTF EMA20 Pierce | 7 | 5 | 60% | +33.6 | +6.73 |
| MNQ 5m | HTF EMA9 Pierce | 10 | 10 | 50% | +73.6 | +7.36 |
| MNQ 5m | HTF EMA9 Pierce (late) | 2 | 2 | 50% | +9.7 | +4.86 |
| MNQ 5m | HTF Pullback Structure | 1 | 1 | 100% | +32.0 | +32.00 |
| MNQ 5m | LTF EMA20 Pierce | 27 | 23 | 57% | +362.6 | +15.76 |
| MNQ 5m | LTF EMA20 Pierce (late) | 5 | 3 | 33% | +0.4 | +0.14 |

## MES 3m — current: 1719 setups, net +16

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 313 | 56% | +84 | +0.27 | -81 / +18 / +146 |
| LTF EMA20 Pierce | 943 | 49% | +70 | +0.07 | +188 / -132 / +14 |
| HTF EMA9 Pierce | 285 | 45% | -137 | -0.48 | -18 / -67 / -51 |
| HTF EMA20 Pierce | 178 | 48% | -1 | -0.01 | +34 / -33 / -2 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1559 | -146 | -162 | -1.5 | +33 / -49 / -146 | worse |
| LTF EMA20 Pierce | 1105 | -38 | -54 | -0.4 | -63 / +40 / -31 | worse |
| HTF EMA9 Pierce | 1533 | +161 | +145 | +1.6 | +25 / +55 / +65 | promising |
| HTF EMA20 Pierce | 1588 | +10 | -6 | -0.1 | +13 / -10 / -9 | worse |

## MGC 3m — current: 1180 setups, net +278

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 210 | 58% | +127 | +0.61 | +40 / +13 / +74 |
| LTF EMA20 Pierce | 603 | 49% | +147 | +0.24 | +128 / -3 / +22 |
| HTF EMA9 Pierce | 194 | 45% | -88 | -0.46 | -92 / +27 / -23 |
| HTF EMA20 Pierce | 173 | 52% | +91 | +0.53 | +85 / -35 / +41 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1066 | +259 | -18 | -0.2 | +12 / +8 / -38 | worse |
| LTF EMA20 Pierce | 822 | +237 | -41 | -0.3 | -10 / -11 / -20 | worse |
| HTF EMA9 Pierce | 1056 | +313 | +35 | +0.4 | +58 / -19 / -4 | noise |
| HTF EMA20 Pierce | 1045 | +202 | -76 | -0.9 | -75 / +15 / -16 | worse |

## MES 2m — current: 1173 setups, net -186

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jun–Jul / Aug / Sep–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 377 | 52% | -38 | -0.10 | -1 / +23 / -60 |
| LTF EMA20 Pierce | 527 | 46% | -147 | -0.28 | -75 / +6 / -79 |
| HTF EMA9 Pierce | 183 | 50% | +2 | +0.01 | +9 / +35 / -42 |
| HTF EMA20 Pierce | 86 | 45% | -3 | -0.04 | -20 / +13 / +4 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 993 | -146 | +39 | +0.4 | +12 / -40 / +67 | noise |
| LTF EMA20 Pierce | 820 | -76 | +109 | +1.1 | +32 / +20 / +58 | promising |
| HTF EMA9 Pierce | 1055 | -162 | +24 | +0.4 | +17 / -37 / +44 | noise |
| HTF EMA20 Pierce | 1100 | -208 | -22 | -0.5 | +7 / -7 / -22 | worse |

## MGC 2m — current: 1499 setups, net +340

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jun–Jul / Aug / Sep–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 490 | 51% | -3 | -0.01 | -110 / +94 / +13 |
| LTF EMA20 Pierce | 641 | 53% | +352 | +0.55 | +196 / +40 / +117 |
| HTF EMA9 Pierce | 239 | 50% | -1 | -0.00 | +25 / -21 / -4 |
| HTF EMA20 Pierce | 129 | 50% | -8 | -0.06 | -28 / +18 / +2 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1265 | +331 | -10 | -0.1 | +53 / -63 / +0 | worse |
| LTF EMA20 Pierce | 1090 | +121 | -219 | -1.8 | -131 / -9 / -79 | worse |
| HTF EMA9 Pierce | 1350 | +388 | +47 | +0.6 | -49 / +58 / +39 | noise |
| HTF EMA20 Pierce | 1404 | +332 | -8 | -0.1 | +28 / -47 / +11 | worse |

## MES 5m — current: 1183 setups, net -9

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 314 | 53% | -42 | -0.13 | -29 / +40 / -53 |
| LTF EMA20 Pierce | 576 | 49% | -101 | -0.18 | -169 / +54 / +14 |
| HTF EMA9 Pierce | 186 | 52% | +66 | +0.36 | +3 / +5 / +59 |
| HTF EMA20 Pierce | 107 | 52% | +68 | +0.64 | +48 / -3 / +23 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1015 | -101 | -93 | -0.7 | +10 / -116 / +13 | worse |
| LTF EMA20 Pierce | 821 | +131 | +140 | +1.0 | +126 / +14 / -1 | noise |
| HTF EMA9 Pierce | 1064 | -92 | -84 | -1.0 | -28 / -9 / -47 | worse |
| HTF EMA20 Pierce | 1101 | -53 | -44 | -0.6 | -43 / -10 / +9 | worse |

## MGC 5m — current: 1173 setups, net -117

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 322 | 55% | +73 | +0.23 | +70 / +75 / -71 |
| LTF EMA20 Pierce | 564 | 51% | -84 | -0.15 | -101 / -59 / +76 |
| HTF EMA9 Pierce | 175 | 45% | -84 | -0.48 | -64 / +51 / -71 |
| HTF EMA20 Pierce | 112 | 50% | -23 | -0.20 | -30 / +12 / -4 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1006 | -59 | +59 | +0.4 | -55 / -41 / +155 | noise |
| LTF EMA20 Pierce | 814 | -17 | +100 | +0.7 | +44 / +90 / -33 | noise |
| HTF EMA9 Pierce | 1063 | -4 | +114 | +1.3 | +52 / -9 / +71 | noise |
| HTF EMA20 Pierce | 1095 | -108 | +9 | +0.1 | +22 / -18 / +5 | noise |

