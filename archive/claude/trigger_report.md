# Setup Triggers study -- 2026-11-13 21:18 ET (weekly run 3)

**STUDY SETTINGS STALE:** settings_sync_report (11/13 16:47 ET, CBC v10.96) lists 3 non-"known" MISMATCHES -- mes3_ema_grid `LIVE` part 'tod' (MES 3m is now 100 % at TP1 all day), chop_sim `EXIT[('MES',3)]` part 'tod', chop_sim `EXIT[('MGC',3)]` 50 % / trail 3.5 (MGC 3m is now FLIP 0 %, no trail). This study replays every chart on the base exits (`stretch_study.QB`: SL1 1.7 ATR, TP1 1.7, 80 %, BE, trail 1.7), not chop_sim `EXIT`, so the trigger comparison itself is not affected; ran anyway, scripts as-is (no fixes).

Replay Jan 5 – Nov 13 (2m Jun – Nov 13), each chart on its live filter settings (filter_sweep.LIVE), base exits; Δ = turning that trigger OFF. The last third ("Jul–Oct" / "Sep–Oct" in the tables) now runs to 11/13. Live = alert store (Trade Setup → Setup Ended), 10/19 – 11/13. Previous report: 2026-11-07 09:50 ET (weekly run 2; run 1 = 11/01).

**Baseline jump on MGC 2m:** the 11/08 replay-script sync turned the MGC 2m range gate (24 / 20 % / 5 ATR, v10.77) ON in filter_sweep.LIVE, so MGC 2m replay setups fell 1499 → 1353 and the per-trigger mix changed (HTF CBC Flip 490 → 277 setups). That jump comes from the sync, not the market. Other charts only gained one week of bars.

**Live data caveats (DATA_NOTES):** stored alerts are still not de-duplicated (/health serverVersion 14, `lastDedupe` null). MGC 2m / 3m / 5m and MCL 2m alerts from 11/08 evening → 11/12 mostly arrived twice; the live table below is the script's raw output (double-counts those). A de-duplicated recount (same chart + Time line + alert names within 60 s = one alert) is given in the "Since last week" bullets where it matters. MGC 3m live results 11/09 – 11/12 are partly on the old exits (a second alert ran 80 % / trail 1.7). MES 3m chart exits changed to 100 % at TP1 on 11/13 (v10.95) and MGC 3m to FLIP 0 % (v10.96); only the last session is on those.

## Since last week

**Verdict: keep all triggers.** No "trigger OFF" is robust on any chart this run (0 consecutive robust runs everywhere, after 3 weekly runs), so rule (a) fails for every candidate.

**Replay, per chart (trigger's own net; OFF Δ / z / thirds / verdict -- this run vs run 2 (11/07) and run 1 (11/01))**
- **MES 3m:** HTF EMA9 Pierce 292 setups **−171** (run 2 −137, run 1 −116), negative in all thirds (−18 / −67 / −86). OFF **+164, z 1.7**, +25 / +55 / +83 — promising (run 2 +145 z 1.6; run 1 +111 z 1.2). Strongest candidate and slowly strengthening, but not robust (z < 2). Live HTF EMA9 Pierce unchanged at 12 ended +10.6 (< 20 and positive) → (c) fails too. HTF CBC Flip still carries the chart: +50 (was +84), OFF −133, z −1.2 (was −162, z −1.5). LTF EMA20 Pierce +119 (OFF −96, worse).
- **MGC 3m:** keep all. HTF EMA9 Pierce −84 (was −88), OFF +31, z 0.4, +58 / −19 / −8 — noise. HTF EMA20 Pierce +105, OFF −89, z −1.1 (was −76, z −0.9) — the most useful trigger here by OFF Δ. Flip +125 (OFF −21), LTF EMA20 +175 (OFF −54).
- **MES 2m:** LTF EMA20 Pierce 552 setups **−155** (was −147), negative in 2 of 3 thirds (−75 / +6 / −86). OFF **+129, z 1.2**, +32 / +20 / +77 — promising (run 2 +109 z 1.1; run 1 +132 z 1.3). Live 67 ended **−44.6** (was 51 −37.6). Criteria (b) and (c) met; (a) not (0 robust runs, z well short of 2). Others: Flip −64 (OFF +72 z 0.6, noise), HTF EMA9 −10 (OFF +34 noise), HTF EMA20 +11 (OFF −40 worse).
- **MGC 2m:** (range-gate baseline jump, see above) LTF EMA20 Pierce **carries the chart**: +439 on 717 setups (+237 / +7 / +195); OFF **−304, z −2.4**, −177 / +15 / −143 — robustly worse by z for the first time but not in all three thirds (Aug +15), so not "robust" by definition (run 2 −219 z −1.8 all thirds). HTF EMA9 Pierce −83 (+13 / −31 / −66), OFF +85, z 1.1, −53 / +55 / +83 — noise (first thirds worse). Keep all.
- **MES 5m:** LTF EMA20 Pierce −83 (−169 / +54 / +32), OFF +137, z 1.0, +126 / +14 / −3 — noise (run 2 +140 z 1.0 noise; run 1 promising z 1.1). Live 29 ended −12.4 (was 24 −29.7). The chart-EMA 16 / 34 / 120 candidate (weekly EMA check) addresses the same trigger — prefer whichever qualifies first; neither does yet. HTF EMA9 (+70, OFF −86) and HTF EMA20 (+66, OFF −42) remain the winners.
- **MGC 5m:** HTF EMA9 Pierce −90 (−64 / +51 / −77), OFF +124, z 1.4, +52 / −9 / +81 — noise (was +114 z 1.3). Live HTF EMA9 Pierce is the best live trigger on this chart: 9 ended +41.4 raw (de-dup 8 ended +32.3). Keep all.

**Live, per trigger (ended setups, net; raw script output, de-dup in brackets where duplicates matter; vs run 2)**
- LTF EMA20 Pierce: MES 2m 67 −44.6 (was −37.6); MES 3m 48 **−20.5** (was +9.6); MES 5m 29 −12.4 (was −29.7); MGC 3m 39 +19.2 [de-dup 36 +4.1] (was −18.6); MGC 2m 88 −0.4 [75 +2.4] (was +12.1); MGC 5m 25 +15.2 [21 +8.3] (was +0.5); MNQ 3m 46 −776.8 (was −748.8); MNQ 2m 69 −177.7 (was −78.0); MNQ 5m 31 +446.1; M2K 2m 43 +22.1; M2K 3m 30 −4.9; M2K 5m 21 −31.2.
- HTF CBC Flip: MES 3m 16 +23.0 (was +41.7); MES 2m −6.2 (was −1.2); MES 5m +11.0 (was +6.2); MGC 3m −14.7 [8 ended +5.7] (was +5.7); MGC 5m −1.2 (was +5.9); MGC 2m 60 −50.1 [57 −36.3] (was −16.0); MNQ 2m −21.1 (was +24.1); MNQ 3m −201.5; MNQ 5m −95.5; M2K 2m −32.6.
- HTF EMA9 Pierce: MES 3m +10.6 (12, no new); MGC 3m +15.4 [+7.5]; MGC 5m +41.4 [+32.3]; MGC 2m +7.5 [+16.2]; MNQ 3m +117.5; MNQ 2m +32.7; MNQ 5m +73.6.
- "LTF EMA20 Pierce (late)" still weak: MGC 5m 14 ended 0 % win −70.4; MGC 2m −40.9; MES 2m −32.0; MES 3m −16.3; MNQ 2m −238.9. Exception MGC 3m +35.7 raw [+4.8 de-dup].

**Candidates (consecutive robust runs: 0 for all, after 3 weekly runs):** MES 3m untick "Trigger: HTF EMA9 Pierce" (OFF z 1.2 → 1.6 → 1.7, promising, live < 20 and positive); MES 2m untick "Trigger: LTF EMA20 Pierce" (z 1.3 → 1.1 → 1.2, promising; replay and live both negative, only (a) missing); MES 5m LTF EMA20 Pierce (noise; 16 / 34 / 120 may qualify first); MGC 5m HTF EMA9 Pierce (noise, and live strongly positive). **Carrying:** LTF EMA20 Pierce on MGC 2m (OFF −304, z −2.4), HTF CBC Flip on MES 3m (OFF −133). No Pine or server changes.

Not in the replay: LTF EMA20 Touch, Momentum break, HTF Pullback Structure (live only, few setups).

---

## Live Trade Setups by first trigger (alert store, with Setup Ended results)

| Chart | Trigger | Setups | Ended | Win % | Net | Avg |
|---|---|---|---|---|---|---|
| M2K 2m | HTF CBC Flip | 25 | 25 | 36% | -32.6 | -1.30 |
| M2K 2m | HTF EMA20 Pierce | 8 | 8 | 75% | +10.5 | +1.32 |
| M2K 2m | HTF EMA20 Pierce (late) | 2 | 2 | 50% | -2.0 | -1.00 |
| M2K 2m | HTF EMA9 Pierce | 10 | 10 | 70% | +3.8 | +0.38 |
| M2K 2m | HTF EMA9 Pierce (late) | 5 | 4 | 100% | +8.1 | +2.04 |
| M2K 2m | HTF Pullback Structure | 1 | 1 | 0% | -0.6 | -0.60 |
| M2K 2m | LTF EMA20 Pierce | 45 | 43 | 60% | +22.1 | +0.51 |
| M2K 2m | LTF EMA20 Pierce (late) | 27 | 25 | 52% | +11.5 | +0.46 |
| M2K 3m | HTF CBC Flip | 14 | 13 | 54% | -4.7 | -0.36 |
| M2K 3m | HTF EMA20 Pierce | 12 | 12 | 33% | -10.2 | -0.85 |
| M2K 3m | HTF EMA20 Pierce (late) | 1 | 1 | 0% | -3.0 | -3.00 |
| M2K 3m | HTF EMA9 Pierce | 4 | 3 | 100% | +6.9 | +2.32 |
| M2K 3m | HTF Pullback Structure | 1 | 1 | 100% | +3.5 | +3.49 |
| M2K 3m | LTF EMA20 Pierce | 32 | 30 | 43% | -4.9 | -0.16 |
| M2K 3m | LTF EMA20 Pierce (late) | 18 | 16 | 62% | +4.3 | +0.27 |
| M2K 5m | HTF CBC Flip | 14 | 12 | 33% | -16.9 | -1.41 |
| M2K 5m | HTF EMA20 Pierce | 9 | 9 | 67% | +1.7 | +0.19 |
| M2K 5m | HTF EMA20 Pierce (late) | 3 | 3 | 67% | +2.8 | +0.93 |
| M2K 5m | HTF EMA9 Pierce | 6 | 5 | 40% | -6.0 | -1.21 |
| M2K 5m | HTF EMA9 Pierce (late) | 4 | 4 | 50% | -0.9 | -0.22 |
| M2K 5m | HTF Pullback Structure | 1 | 1 | 0% | -5.0 | -5.00 |
| M2K 5m | LTF EMA20 Pierce | 22 | 21 | 33% | -31.2 | -1.49 |
| M2K 5m | LTF EMA20 Pierce (late) | 9 | 7 | 43% | -1.8 | -0.26 |
| M2K 5m | LTF EMA20 Touch (mid-candle) | 1 | 1 | 0% | -2.1 | -2.10 |
| MCL 2m | HTF CBC Flip | 1 | 1 | 100% | +0.3 | +0.31 |
| MCL 2m | HTF EMA20 Pierce | 8 | 8 | 75% | +1.0 | +0.12 |
| MCL 2m | HTF EMA20 Pierce (late) | 1 | 1 | 0% | -0.1 | -0.10 |
| MCL 2m | HTF EMA9 Pierce | 20 | 19 | 61% | +1.9 | +0.10 |
| MCL 2m | HTF EMA9 Pierce (late) | 5 | 5 | 80% | +0.8 | +0.15 |
| MCL 2m | HTF Pullback Structure | 1 | 1 | 0% | -0.3 | -0.30 |
| MCL 2m | LTF EMA20 Pierce | 48 | 43 | 53% | +1.6 | +0.04 |
| MCL 2m | LTF EMA20 Pierce (late) | 30 | 24 | 54% | +1.3 | +0.06 |
| MCL 3m | HTF CBC Flip | 1 | 1 | 0% | -0.2 | -0.19 |
| MCL 3m | HTF EMA20 Pierce | 5 | 5 | 40% | -0.4 | -0.07 |
| MCL 3m | HTF EMA20 Pierce (late) | 1 | 1 | 100% | +0.3 | +0.26 |
| MCL 3m | HTF EMA9 Pierce | 4 | 3 | 0% | -0.5 | -0.16 |
| MCL 3m | HTF EMA9 Pierce (late) | 6 | 4 | 25% | -0.5 | -0.13 |
| MCL 3m | HTF Pullback Structure | 1 | 1 | 0% | -0.3 | -0.30 |
| MCL 3m | LTF EMA20 Pierce | 35 | 33 | 61% | +2.3 | +0.07 |
| MCL 3m | LTF EMA20 Pierce (late) | 15 | 14 | 43% | -0.8 | -0.06 |
| MCL 5m | HTF CBC Flip | 2 | 2 | 50% | -0.1 | -0.03 |
| MCL 5m | HTF EMA20 Pierce | 2 | 2 | 50% | -0.1 | -0.03 |
| MCL 5m | HTF EMA20 Pierce (late) | 1 | 1 | 100% | +0.3 | +0.35 |
| MCL 5m | HTF EMA9 Pierce | 3 | 2 | 50% | +0.0 | +0.00 |
| MCL 5m | HTF EMA9 Pierce (late) | 2 | 1 | 0% | -0.3 | -0.30 |
| MCL 5m | LTF EMA20 Pierce | 32 | 30 | 33% | -2.8 | -0.09 |
| MCL 5m | LTF EMA20 Pierce (late) | 10 | 9 | 56% | +0.7 | +0.07 |
| MES 2m | HTF CBC Flip | 40 | 37 | 51% | -6.2 | -0.17 |
| MES 2m | HTF EMA20 Pierce | 10 | 10 | 30% | -7.8 | -0.78 |
| MES 2m | HTF EMA20 Pierce (late) | 3 | 2 | 50% | -0.8 | -0.38 |
| MES 2m | HTF EMA9 Pierce | 8 | 8 | 50% | -3.1 | -0.39 |
| MES 2m | HTF EMA9 Pierce (late) | 3 | 2 | 0% | -6.1 | -3.06 |
| MES 2m | HTF Pullback Structure | 2 | 2 | 50% | -3.2 | -1.60 |
| MES 2m | LTF EMA20 Pierce | 74 | 67 | 43% | -44.6 | -0.67 |
| MES 2m | LTF EMA20 Pierce (late) | 19 | 19 | 37% | -32.0 | -1.68 |
| MES 3m | HTF CBC Flip | 18 | 16 | 56% | +23.0 | +1.44 |
| MES 3m | HTF EMA20 Pierce | 7 | 5 | 20% | -5.8 | -1.17 |
| MES 3m | HTF EMA20 Pierce (late) | 3 | 3 | 67% | +0.8 | +0.26 |
| MES 3m | HTF EMA9 Pierce | 13 | 12 | 50% | +10.6 | +0.89 |
| MES 3m | HTF EMA9 Pierce (late) | 2 | 2 | 0% | -5.9 | -2.94 |
| MES 3m | HTF Pullback Structure | 2 | 2 | 0% | -9.1 | -4.54 |
| MES 3m | LTF EMA20 Pierce | 54 | 48 | 50% | -20.5 | -0.43 |
| MES 3m | LTF EMA20 Pierce (late) | 22 | 21 | 43% | -16.3 | -0.77 |
| MES 5m | HTF CBC Flip | 17 | 15 | 67% | +11.0 | +0.74 |
| MES 5m | HTF EMA20 Pierce | 7 | 6 | 50% | -4.2 | -0.70 |
| MES 5m | HTF EMA20 Pierce (late) | 2 | 2 | 100% | +9.1 | +4.56 |
| MES 5m | HTF EMA9 Pierce | 4 | 2 | 50% | -3.2 | -1.60 |
| MES 5m | HTF EMA9 Pierce (late) | 1 | 1 | 0% | -5.5 | -5.50 |
| MES 5m | HTF Pullback Structure | 1 | 1 | 0% | -5.8 | -5.75 |
| MES 5m | LTF EMA20 Pierce | 31 | 29 | 48% | -12.4 | -0.43 |
| MES 5m | LTF EMA20 Pierce (late) | 18 | 15 | 47% | -7.5 | -0.50 |
| MGC 2m | HTF CBC Flip | 66 | 60 | 45% | -50.1 | -0.83 |
| MGC 2m | HTF EMA20 Pierce | 17 | 15 | 33% | -24.3 | -1.62 |
| MGC 2m | HTF EMA20 Pierce (late) | 5 | 4 | 25% | -9.4 | -2.35 |
| MGC 2m | HTF EMA9 Pierce | 20 | 18 | 56% | +7.5 | +0.42 |
| MGC 2m | HTF EMA9 Pierce (late) | 10 | 10 | 40% | -4.0 | -0.40 |
| MGC 2m | HTF Pullback Structure | 1 | 1 | 0% | -5.0 | -5.00 |
| MGC 2m | LTF EMA20 Pierce | 94 | 88 | 45% | -0.4 | -0.00 |
| MGC 2m | LTF EMA20 Pierce (late) | 34 | 33 | 42% | -40.9 | -1.24 |
| MGC 3m | HTF CBC Flip | 15 | 13 | 54% | -14.7 | -1.13 |
| MGC 3m | HTF EMA20 Pierce | 15 | 14 | 36% | -22.7 | -1.62 |
| MGC 3m | HTF EMA9 Pierce | 13 | 11 | 64% | +15.4 | +1.40 |
| MGC 3m | HTF EMA9 Pierce (late) | 4 | 4 | 50% | -1.6 | -0.40 |
| MGC 3m | HTF Pullback Structure | 1 | 1 | 0% | -6.9 | -6.91 |
| MGC 3m | LTF EMA20 Pierce | 43 | 39 | 46% | +19.2 | +0.49 |
| MGC 3m | LTF EMA20 Pierce (late) | 13 | 13 | 54% | +35.7 | +2.75 |
| MGC 5m | HTF CBC Flip | 18 | 18 | 56% | -1.2 | -0.07 |
| MGC 5m | HTF EMA20 Pierce | 8 | 7 | 43% | -2.7 | -0.39 |
| MGC 5m | HTF EMA20 Pierce (late) | 1 | 1 | 100% | +4.8 | +4.80 |
| MGC 5m | HTF EMA9 Pierce | 11 | 9 | 89% | +41.4 | +4.60 |
| MGC 5m | HTF EMA9 Pierce (late) | 3 | 3 | 0% | -13.9 | -4.65 |
| MGC 5m | HTF Pullback Structure | 1 | 1 | 0% | -2.7 | -2.70 |
| MGC 5m | LTF EMA20 Pierce | 30 | 25 | 56% | +15.2 | +0.61 |
| MGC 5m | LTF EMA20 Pierce (late) | 15 | 14 | 0% | -70.4 | -5.03 |
| MGC 5m | LTF EMA20 Touch (mid-candle) | 1 | 1 | 100% | +5.6 | +5.58 |
| MNQ 2m | HTF CBC Flip | 70 | 64 | 44% | -21.1 | -0.33 |
| MNQ 2m | HTF EMA20 Pierce | 19 | 19 | 42% | -45.2 | -2.38 |
| MNQ 2m | HTF EMA20 Pierce (late) | 3 | 3 | 33% | -21.9 | -7.30 |
| MNQ 2m | HTF EMA9 Pierce | 25 | 23 | 43% | +32.7 | +1.42 |
| MNQ 2m | HTF EMA9 Pierce (late) | 3 | 3 | 67% | +90.8 | +30.26 |
| MNQ 2m | HTF Pullback Structure | 3 | 3 | 33% | -57.5 | -19.17 |
| MNQ 2m | LTF EMA20 Pierce | 76 | 69 | 38% | -177.7 | -2.57 |
| MNQ 2m | LTF EMA20 Pierce (late) | 23 | 22 | 32% | -238.9 | -10.86 |
| MNQ 3m | HTF CBC Flip | 35 | 31 | 35% | -201.5 | -6.50 |
| MNQ 3m | HTF EMA20 Pierce | 16 | 15 | 40% | -86.0 | -5.73 |
| MNQ 3m | HTF EMA9 Pierce | 7 | 7 | 71% | +117.5 | +16.79 |
| MNQ 3m | HTF EMA9 Pierce (late) | 3 | 3 | 33% | -25.3 | -8.43 |
| MNQ 3m | LTF EMA20 Pierce | 50 | 46 | 17% | -776.8 | -16.89 |
| MNQ 3m | LTF EMA20 Pierce (late) | 11 | 11 | 36% | -23.1 | -2.10 |
| MNQ 3m | LTF EMA20 Touch (mid-candle) | 1 | 1 | 0% | -30.0 | -30.00 |
| MNQ 5m | HTF CBC Flip | 13 | 10 | 30% | -95.5 | -9.55 |
| MNQ 5m | HTF EMA20 Pierce | 8 | 6 | 67% | +65.7 | +10.94 |
| MNQ 5m | HTF EMA9 Pierce | 10 | 10 | 50% | +73.6 | +7.36 |
| MNQ 5m | HTF EMA9 Pierce (late) | 3 | 3 | 33% | -20.3 | -6.76 |
| MNQ 5m | HTF Pullback Structure | 1 | 1 | 100% | +32.0 | +32.00 |
| MNQ 5m | LTF EMA20 Pierce | 36 | 31 | 58% | +446.1 | +14.39 |
| MNQ 5m | LTF EMA20 Pierce (late) | 7 | 5 | 60% | +64.4 | +12.88 |

## MES 3m — current: 1756 setups, net -3

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 320 | 55% | +50 | +0.16 | -81 / +18 / +112 |
| LTF EMA20 Pierce | 962 | 50% | +119 | +0.12 | +188 / -132 / +62 |
| HTF EMA9 Pierce | 292 | 44% | -171 | -0.59 | -18 / -67 / -86 |
| HTF EMA20 Pierce | 182 | 48% | -0 | -0.00 | +34 / -33 / -1 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1592 | -136 | -133 | -1.2 | +33 / -49 / -117 | worse |
| LTF EMA20 Pierce | 1133 | -99 | -96 | -0.6 | -63 / +40 / -73 | worse |
| HTF EMA9 Pierce | 1566 | +161 | +164 | +1.7 | +25 / +55 / +83 | promising |
| HTF EMA20 Pierce | 1622 | -4 | -1 | -0.0 | +13 / -10 / -4 | worse |

## MGC 3m — current: 1199 setups, net +320

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 214 | 57% | +125 | +0.58 | +40 / +13 / +72 |
| LTF EMA20 Pierce | 614 | 49% | +175 | +0.28 | +128 / -3 / +50 |
| HTF EMA9 Pierce | 196 | 45% | -84 | -0.43 | -92 / +27 / -19 |
| HTF EMA20 Pierce | 175 | 52% | +105 | +0.60 | +85 / -35 / +55 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1084 | +299 | -21 | -0.2 | +12 / +8 / -41 | worse |
| LTF EMA20 Pierce | 837 | +267 | -54 | -0.4 | -10 / -11 / -33 | worse |
| HTF EMA9 Pierce | 1073 | +351 | +31 | +0.4 | +58 / -19 / -8 | noise |
| HTF EMA20 Pierce | 1062 | +231 | -89 | -1.1 | -75 / +15 / -30 | worse |

## MES 2m — current: 1224 setups, net -217

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jun–Jul / Aug / Sep–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 391 | 51% | -64 | -0.16 | -1 / +23 / -86 |
| LTF EMA20 Pierce | 552 | 47% | -155 | -0.28 | -75 / +6 / -86 |
| HTF EMA9 Pierce | 191 | 48% | -10 | -0.05 | +9 / +35 / -54 |
| HTF EMA20 Pierce | 90 | 48% | +11 | +0.13 | -20 / +13 / +18 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1039 | -145 | +72 | +0.6 | +12 / -40 / +100 | noise |
| LTF EMA20 Pierce | 853 | -88 | +129 | +1.2 | +32 / +20 / +77 | promising |
| HTF EMA9 Pierce | 1099 | -182 | +34 | +0.5 | +17 / -37 / +54 | noise |
| HTF EMA20 Pierce | 1149 | -257 | -40 | -0.8 | +7 / -7 / -40 | worse |

## MGC 2m — current: 1353 setups, net +384

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jun–Jul / Aug / Sep–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 277 | 53% | +30 | +0.11 | -56 / +67 / +18 |
| LTF EMA20 Pierce | 717 | 53% | +439 | +0.61 | +237 / +7 / +195 |
| HTF EMA9 Pierce | 230 | 46% | -83 | -0.36 | +13 / -31 / -66 |
| HTF EMA20 Pierce | 129 | 50% | -1 | -0.01 | -21 / +24 / -5 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1216 | +325 | -59 | -0.6 | -16 / -43 / -1 | worse |
| LTF EMA20 Pierce | 885 | +81 | -304 | -2.4 | -177 / +15 / -143 | worse |
| HTF EMA9 Pierce | 1201 | +470 | +85 | +1.1 | -53 / +55 / +83 | noise |
| HTF EMA20 Pierce | 1255 | +357 | -28 | -0.5 | +6 / -47 / +13 | worse |

## MES 5m — current: 1208 setups, net +18

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 317 | 53% | -34 | -0.11 | -29 / +40 / -45 |
| LTF EMA20 Pierce | 591 | 49% | -83 | -0.14 | -169 / +54 / +32 |
| HTF EMA9 Pierce | 191 | 52% | +70 | +0.37 | +3 / +5 / +62 |
| HTF EMA20 Pierce | 109 | 52% | +66 | +0.60 | +48 / -3 / +20 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1039 | -85 | -104 | -0.8 | +10 / -116 / +2 | worse |
| LTF EMA20 Pierce | 837 | +156 | +137 | +1.0 | +126 / +14 / -3 | noise |
| HTF EMA9 Pierce | 1086 | -68 | -86 | -1.0 | -28 / -9 / -50 | worse |
| HTF EMA20 Pierce | 1124 | -23 | -42 | -0.6 | -43 / -10 / +11 | worse |

## MGC 5m — current: 1194 setups, net -107

**Per trigger (current settings)**

| Trigger | Setups | Win % | Net | Avg | Net by third (Jan–Mar / Apr–Jun / Jul–Oct) |
|---|---|---|---|---|---|
| HTF CBC Flip | 326 | 55% | +71 | +0.22 | +70 / +75 / -74 |
| LTF EMA20 Pierce | 579 | 51% | -66 | -0.11 | -101 / -59 / +94 |
| HTF EMA9 Pierce | 177 | 45% | -90 | -0.51 | -64 / +51 / -77 |
| HTF EMA20 Pierce | 112 | 50% | -23 | -0.20 | -30 / +12 / -4 |

**Trigger turned OFF (one at a time)**

| Trigger OFF | Setups | Net | Δ vs current | z | Δ by third | Verdict |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 1024 | -51 | +56 | +0.4 | -55 / -41 / +152 | noise |
| LTF EMA20 Pierce | 827 | -31 | +76 | +0.5 | +44 / +90 / -57 | noise |
| HTF EMA9 Pierce | 1083 | +17 | +124 | +1.4 | +52 / -9 / +81 | noise |
| HTF EMA20 Pierce | 1116 | -98 | +9 | +0.1 | +22 / -18 / +5 | noise |

