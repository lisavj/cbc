# MES watch: chart EMA / TP1 / 5m confirmation / per-trigger / exit rules / late + room -- 2026-11-12 17:37 ET

Daily scheduled study. Live = CBC v10.87 in the task text; newest Pine is v10.93 (11/12: v10.88 adds "LTF EMA20 Pierce (not beyond EMA9)" to the bot set, v10.92 flip-only bot exits 09:30-16:00 -- bot-only, no effect on these chart studies). Newest run on top; history tables keep one line per run. Settings check (claude/settings_sync_report.md, 11/12 16:47 ET): 0 MISMATCH, 1 known -- study settings current.

## History

### (A) Chart EMA — replay Jan 5 → now, live exits, Δ vs slow 20

TP1 in the replay: 2.0 until the 11/07 run, 1.75 from 11/09 (live v10.82+), so rows before 11/09 are not directly comparable.

| Run | TP1 | Slow 14: Δ / z / thirds | Slow 14 last 4 wk Δ | Slow 14 last 5 days Δ | Slow 16: Δ / z / thirds | Slow 16 last 4 wk Δ | Slow 16 last 5 days Δ | Last-4-wk beat count (of last 7 runs) 14 / 16 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-12 17:37 ET | 1.75 | +207 / 0.7 / +6 · +37 · +164 | +29 | -48 | +226 / 0.9 / -1 · +79 · +148 | +77 | +4 | 4 of 5 / 4 of 5 | keep 9 / 20 |
| 2026-11-12 09:44 ET | 1.75 | +214 / 0.8 / +6 · +37 · +171 | +34 | -42 | +222 / 0.9 / -1 · +79 · +144 | +72 | -0 | 3 of 4 / 3 of 4 | keep 9 / 20 |
| 2026-11-09 17:38 ET | 1.75 | +204 / 0.7 / +6 · +45 · +153 | +35 | -85 | +201 / 0.8 / -1 · +78 · +124 | +59 | -28 | 2 of 3 / 2 of 3 | keep 9 / 20 |
| 2026-11-07 09:44 ET (11/06 Fri run) | 2.0 | +135 / 0.5 / -19 · +55 · +99 | -5 | -78 | +153 / 0.6 / +12 · +124 · +18 | -3 | -50 | 1 of 2 / 1 of 2 | keep 9 / 20 |
| 2026-11-05 17:37 ET | 2.0 | +184 / 0.6 / -28 · +64 · +148 | +34 | -34 | +178 / 0.7 / +10 · +132 · +36 | +15 | -26 | 1 of 1 / 1 of 1 | keep 9 / 20 |

### (B) TP1 on the real MES 3m setups since 10/19

| Run | Ended | 1.5 | 1.75 | 2.0 | Δ 1.5 − 1.75 (halves) | Δ 2.0 − 1.75 (halves) | Verdict |
|---|---|---|---|---|---|---|---|
| 2026-11-12 17:37 ET | 107 | +33.1 | +60.8 | +64.7 | -27.7 (-11.2 / -16.5) | +3.9 (-6.3 / +10.2) | keep 1.75 |
| 2026-11-12 09:44 ET | 106 | +27.9 | +55.6 | +59.5 | -27.7 (-11.2 / -16.5) | +3.9 (-6.3 / +10.2) | keep 1.75 |
| 2026-11-09 17:38 ET | 105 | +46.6 | +74.3 | +78.2 | -27.7 (-10.7 / -17.0) | +3.9 (-6.8 / +10.7) | keep 1.75 |
| 2026-11-07 09:44 ET | 103 | +55.8 | +81.9 | +84.2 | -26.1 | +2.3 (-8.0 / +10.3) | keep 2.0 (was live) |

### (C) MES 5m confirmation — live since 10/19, avg pts per ended setup (confirmed vs unconfirmed)

| Run | MES 2m conf (n / avg) | MES 2m unconf (n / avg) | Δ | MES 3m conf (n / avg) | MES 3m unconf (n / avg) | Δ | Friday replay | Verdict 2m / 3m |
|---|---|---|---|---|---|---|---|---|
| 2026-11-12 17:37 ET | 88 / +0.10 | 54 / -1.69 | +1.79 | 77 / +0.09 | 30 / -0.63 | +0.72 | 11/06: 2m Δ -0.03 z -0.1; 3m Δ +0.16 z 0.4 | keep watching / keep watching |
| 2026-11-12 09:44 ET | 84 / +0.30 | 54 / -1.69 | +1.99 | 76 / +0.03 | 30 / -0.63 | +0.66 | same | keep watching / keep watching |
| 2026-11-09 17:38 ET | 66 / +0.14 | 54 / -1.69 | +1.83 | 75 / +0.28 | 30 / -0.63 | +0.91 | same | keep watching / keep watching |
| 2026-11-07 09:44 ET (11/06 Fri run) | 62 / +0.13 | 54 / -1.69 | +1.82 | 73 / +0.39 | 30 / -0.63 | +1.02 | 2m Δ -0.03 z -0.1 (thirds -/-/+); 3m Δ +0.16 z 0.4 (thirds +/+/-) | keep watching / keep watching |
| 2026-11-05 17:37 ET | 56 / -0.26 | 54 / -1.69 | +1.44 | 70 / +0.72 | 30 / -0.63 | +1.35 | none yet (11/05 ad-hoc: 2m z 1.3, 3m z 1.1, all thirds) | ACT (provisional) / keep watching |

### (D) Per trigger — live since 10/19 (ended / net)

| Run | MES 2m LTF late | MES 3m LTF late | MES 5m LTF late | MES 3m bot set (Flip + LTF beyond EMA9) | MES 3m everything else | Friday replay (LTF late window 0 vs 1) | Verdict |
|---|---|---|---|---|---|---|---|
| 2026-11-12 17:37 ET | 18 / -24.0 | 20 / -21.1 | 15 / -7.5 | 31 / +25.7 (avg +0.83); v10.88 3-trigger set 63 / +18.8 (avg +0.30) | 76 / -37.4 | 11/06: 2m Δ -44 z -1.0 · 3m Δ -2 z 0.0 · 5m Δ -74 z -1.7 | keep watching |
| 2026-11-12 09:44 ET | 18 / -24.0 | 20 / -21.1 | 15 / -7.5 | 31 / +25.7 (avg +0.83) | 75 / -42.6 | same | keep watching |
| 2026-11-09 17:38 ET | 15 / -27.0 | 20 / -21.1 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | 75 / -42.6 | same | keep watching |
| 2026-11-07 09:44 ET (11/06 Fri run) | 14 / -33.4 | 19 / -32.5 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | 73 / -35.0 | 2m Δ -44 z -1.0 · 3m Δ -2 z 0.0 · 5m Δ -74 z -1.7 | keep watching |
| 2026-11-05 17:37 ET | 13 / -25.4 | 18 / -23.2 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | 70 / -12.8 | not run | keep watching |

### (E) Exit rules (v10.79) — live hits and Friday replay

| Run | MES 3m TP cut live hits: rule vs CBC | MGC 3m profit lock live hits: rule vs CBC | Replay MES 3m TP cut (Δ / z / thirds / last 4 wk) | Replay MGC 3m lock (Δ / z / thirds / last 4 wk) | Verdict |
|---|---|---|---|---|---|
| 2026-11-12 17:37 ET | 1 hit (11/12 10:30): +11.44 vs +5.25 (+6.19) | 5 hits, 2 comparable: +5.10 vs -3.00 (+8.10; halves +1.20 / +6.90) | 11/06: +168 / 2.8 / all + / +0.3 | 11/06: +307 / 2.4 / all + / -45 | keep watching (MES 1 / MGC 2 of 15) |
| 2026-11-12 09:44 ET | 0 | 5 hits, 2 comparable: +5.10 vs -3.00 (+8.10) | same | same | keep watching |
| 2026-11-09 17:38 ET | 0 | 1: +3.2 vs +2.0 (+1.2) | same | same | keep watching |
| 2026-11-07 09:44 ET (11/06 Fri run) | 0 (no Exit Rule alerts yet) | 0 | +168 / 2.8 / +131 · +6 · +30 / +0.3 | +307 / 2.4 / +126 · +85 · +96 / -45 | keep watching |

### (F) Late trigger + room < 0.5 x TP1 — live (Room line exists from 10/29), ended / net / avg

| Run | MES 3m | MES 2m | MES 5m | MES 3m bot windows | Verdict |
|---|---|---|---|---|---|
| 2026-11-12 17:37 ET | 8 / +7.2 / +0.90 | 5 / -16.2 / -3.23 | 5 / +13.5 / +2.70 | 8 / +7.2 / +0.90 | too few yet (all charts) |
| 2026-11-12 09:44 ET | 8 / +7.2 / +0.90 | 5 / -16.2 / -3.23 | 5 / +13.5 / +2.70 | 8 / +7.2 / +0.90 | too few yet |
| 2026-11-09 17:38 ET | 8 / +7.2 / +0.90 | 3 / -8.4 / -2.80 | 2 / +7.0 / +3.51 | 8 / +7.2 / +0.90 | too few yet |

---

## Run 2026-11-12 17:37 ET (Thu)

Thursday run: Friday-only replays (step 3 per-trigger replay + LTF late-window test, (C) replay, (E) replay) not run; verdicts use the 11/06 Friday run (kept below). Live alerts through 11/12 17:01 ET (last MES setup 15:40); BarFeed MES 3m through 11/12 17:37 (102 285 candles from 01/05). Settings check: 0 MISMATCH.

**Data warnings this run**

- **MES 3m alerts still thin.** The 11/08 20:45 → 11/12 09:30 ET gap is confirmed (no MES 3m alert of any kind 11/09-11/11). Since it came back: 59 MES 3m alerts on 11/12 (a normal day had 130-240), 2 setups, last MES 3m alert of any kind 14:21 ET. MES 2m / 5m flowed normally.
- **MGC 3m: no Trade Setup since 11/11 06:15 ET and no Setup Ended since 11/11 12:30 ET**, while other MGC 3m alerts ("Shadow …", A+ Setup, pierce alerts) keep arriving (998 since 11/09). MGC 3m live numbers are frozen at 85 setups. Possibly a side effect of deleting the duplicate MGC 3m alert on 11/12 (the alert left may not have Trade Setup / Setup Ended ticked) or every setup being gated to shadow -- worth checking in TradingView.
- Duplicates: server v14, stored alerts still not cleaned (lastDedupe null); the script dropped 1 504 near copies, 6 setups had two Setup Ended results (0.5×(TP1) version kept).

### Verdicts

- **(A) EMA: keep 9 / 20, keep watching.** TP1 1.75: slow 14 Δ +207 (z 0.7, thirds +6 / +37 / +164), slow 16 Δ +226 (z 0.9, thirds -1 / +79 / +148) -- not robust. Last 4 wk: 14 +29, 16 +77 (both beat 20 in 4 of the last 5 runs; need 5 of 7 AND z ≥ 2). Last 5 days: 14 -48, 16 +4. TP1 1.5 variant: slow 16 Δ +221, z 1.0, all thirds + (promising edge).
- **(B) TP1: keep 1.75.** 107 real setups: 2.0 +64.7 ≥ 1.75 +60.8 > 1.5 +33.1. 2.0 − 1.75 = +3.9 (halves -6.3 / +10.2; thirds +0.8 / -18.8 / +21.9); 1.5 − 1.75 = -27.7 (halves -11.2 / -16.5). Validation 106 / 107.
- **(C) keep watching (2m and 3m).** MES 2m 88 conf +0.10 vs 54 unconf -1.69 (+1.79/setup); h1 -1.10 vs -1.69, h2 has 0 unconfirmed; replay 11/06 Δ -0.03 z -0.1 fails. MES 3m 77 conf +0.09 vs 30 unconf -0.63 (+0.72); h2 has 1 unconfirmed (+3.75), replay z 0.4. Only 1 unconfirmed setup on either chart since 10/28, so the split hardly grows. Acting would need a new CBC filter / dashboard flag (not built).
- **(D) keep watching on every MES chart** (no trigger at 40 ended). LTF Pierce LATE: MES 2m 18 / -24.0 (avg -1.33, halves -12.6 / -11.4), MES 3m 20 / -21.1 (avg -1.05, halves -34.5 / +13.4), MES 5m 15 / -7.5 (avg -0.50, halves -22.1 / +14.6); latest replay disagrees with a switch-off (window 0 vs 1: 2m z -1.0, 3m z 0.0, 5m z -1.7). MES 3m bot set (Flip + LTF beyond) 31 / +25.7 (avg +0.83, halves +4.0 / +21.8); the v10.88 three-trigger bot set 63 / +18.8 (avg +0.30) -- LTF Pierce not beyond on MES 3m 32 / -6.9 (avg -0.22, halves +3.2 / -10.1) dilutes it. No ADD candidate (nothing at 40 ended with avg > +0.5).
- **(E) keep watching.** First MES 3m TP cut hit: 11/12 10:30 LONG, rule +11.44 vs CBC +5.25 (+6.19). MGC 3m profit lock: 5 hits, 2 comparable +5.10 vs -3.00 (+8.10). Far from 15 hits each.
- **(F) too few yet on every chart.** late & room < 0.5: MES 3m 8 / +7.2 (avg +0.90), MES 2m 5 / -16.2 (-3.23), MES 5m 5 / +13.5 (+2.70), MES 3m bot windows 8 / +7.2. No new combo setup today on MES 2m / 3m; MES 5m had two on 11/12 (-2.75, +4.43).

## Live (steps 1, 2, 4, 6b, 6c)

### Live per chart (10/19 → 11/12 15:40)

| Chart | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| MES 2m | 155 | 142 | 45% | -82.5 | -0.58 | -110.0 / +27.5 |
| MES 3m | 120 | 107 | 47% | -11.6 | -0.11 | -34.1 / +22.5 |
| MES 5m | 81 | 71 | 52% | -18.3 | -0.26 | -26.5 / +8.1 |
| MGC 2m | 211 | 193 | 47% | -72.8 | -0.38 | -37.8 / -35.0 |
| MGC 3m | 85 | 74 | 45% | -2.6 | -0.03 | -14.8 / +12.3 |
| MGC 5m | 69 | 63 | 48% | -14.9 | -0.24 | -7.7 / -7.1 |
| MNQ 2m | 207 | 192 | 40% | -386.2 | -2.01 | -416.3 / +30.2 |
| MNQ 3m | 119 | 110 | 31% | -970.3 | -8.82 | -481.6 / -488.7 |
| MNQ 5m | 75 | 63 | 54% | +583.2 | +9.26 | +271.6 / +311.5 |
| MES 3m 10/19–11/04 (9 / 20) | 107 | 95 | 47% | +6.7 | +0.07 | -49.0 / +55.7 |
| MES 3m 11/05 (7 / 14 build) | 5 | 5 | 60% | +24.9 | +4.99 | -1.7 / +26.6 |
| MES 3m 11/06–11/07 (9 / 20, TP1 2.0) | 4 | 3 | 0% | -22.2 | -7.42 | -9.2 / -13.0 |
| MES 3m from 11/08 (TP1 1.75, v10.82+) | 4 | 4 | 50% | -21.1 | -5.26 | -7.6 / -13.4 |
| MGC 3m before 11/08 | 77 | 67 | 42% | -34.2 | -0.51 | -6.1 / -28.1 |
| MGC 3m from 11/08 (50 % + trail 3.5; partly old exits to 11/12) | 8 | 7 | 71% | +31.7 | +4.52 | +32.9 / -1.2 |

Matched: 1122 Trade Setup alerts, 1015 ended; 96 Setup Ended alerts without a matching Trade Setup (not counted). Near-duplicate alerts dropped: 1504; setups with two Setup Ended results: 6 (0.5×(TP1) version kept).

### (D) Live per trigger — MES 2m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 40 | 37 | 51% | -6.2 | -0.17 | -15.2 / +9.0 |
| LTF Pierce beyond EMA9 | 41 | 36 | 50% | -2.2 | -0.06 | -61.8 / +59.6 |
| LTF Pierce not beyond | 30 | 27 | 37% | -29.3 | -1.08 | -19.3 / -10.0 |
| LTF Pierce LATE | 18 | 18 | 39% | -24.0 | -1.33 | -12.6 / -11.4 |
| HTF EMA9 Pierce | 8 | 8 | 50% | -3.1 | -0.39 | +2.2 / -5.3 |
| HTF EMA9 late | 3 | 2 | 0% | -6.1 | -3.06 | +0.0 / -6.1 |
| HTF EMA20 Pierce | 10 | 10 | 30% | -7.8 | -0.78 | +4.8 / -12.5 |
| HTF EMA20 late | 3 | 2 | 50% | -0.8 | -0.38 | +2.0 / -2.8 |
| HTF Pullback | 2 | 2 | 50% | -3.2 | -1.60 | -8.0 / +4.8 |

### (D) Live per trigger — MES 3m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 18 | 16 | 56% | +23.0 | +1.44 | +9.8 / +13.2 |
| LTF Pierce beyond EMA9 | 18 | 15 | 60% | +2.8 | +0.18 | -11.5 / +14.2 |
| LTF Pierce not beyond | 35 | 32 | 47% | -6.9 | -0.22 | +3.2 / -10.1 |
| LTF Pierce LATE | 22 | 20 | 40% | -21.1 | -1.05 | -34.5 / +13.4 |
| HTF EMA9 Pierce | 13 | 12 | 50% | +10.6 | +0.89 | +5.2 / +5.4 |
| HTF EMA9 late | 2 | 2 | 0% | -5.9 | -2.94 | -1.2 / -4.6 |
| HTF EMA20 Pierce | 7 | 5 | 20% | -5.8 | -1.17 | -8.8 / +3.0 |
| HTF EMA20 late | 3 | 3 | 67% | +0.8 | +0.26 | -5.2 / +6.0 |
| HTF Pullback | 2 | 2 | 0% | -9.1 | -4.54 | -5.6 / -3.5 |
| **Bot set (Flip + LTF Pierce beyond EMA9)** | 36 | 31 | 58% | +25.7 | +0.83 | +4.0 / +21.8 |
| Bot set since v10.88 (+ LTF Pierce not beyond) | 71 | 63 | 52% | +18.8 | +0.30 | -2.8 / +21.6 |
| Everything else (vs 2-trigger set) | 84 | 76 | 42% | -37.4 | -0.49 | -38.1 / +0.7 |

### (D) Live per trigger — MES 5m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 17 | 15 | 67% | +11.0 | +0.74 | +9.4 / +1.6 |
| LTF Pierce beyond EMA9 | 15 | 14 | 36% | -31.1 | -2.22 | -21.8 / -9.3 |
| LTF Pierce not beyond | 16 | 15 | 60% | +18.8 | +1.25 | -5.7 / +24.5 |
| LTF Pierce LATE | 18 | 15 | 47% | -7.5 | -0.50 | -22.1 / +14.6 |
| HTF EMA9 Pierce | 4 | 2 | 50% | -3.2 | -1.60 | -8.0 / +4.8 |
| HTF EMA9 late | 1 | 1 | 0% | -5.5 | -5.50 | +0.0 / -5.5 |
| HTF EMA20 Pierce | 7 | 6 | 50% | -4.2 | -0.70 | +4.5 / -8.7 |
| HTF EMA20 late | 2 | 2 | 100% | +9.1 | +4.56 | +4.8 / +4.3 |
| HTF Pullback | 1 | 1 | 0% | -5.8 | -5.75 | +0.0 / -5.8 |

### (D) Live per trigger — MGC / MNQ, ended setups / net pts

| Trigger | MGC 2m | MGC 3m | MGC 5m | MNQ 2m | MNQ 3m | MNQ 5m |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 51 / -25.3 | 8 / +5.7 | 15 / +5.9 | 62 / +38.9 | 31 / -201.5 | 9 / -65.5 |
| LTF Pierce beyond EMA9 | 30 / -11.4 | 15 / -16.0 | 10 / +3.1 | 22 / -262.8 | 18 / -270.5 | 12 / +61.8 |
| LTF Pierce not beyond | 39 / +21.3 | 17 / +1.9 | 9 / +18.1 | 39 / +30.8 | 27 / -538.3 | 17 / +371.4 |
| LTF Pierce LATE | 30 / -37.1 | 11 / +17.3 | 13 / -68.2 | 20 / -178.9 | 9 / +33.7 | 5 / +64.4 |
| HTF EMA9 Pierce | 16 / +16.2 | 9 / +5.8 | 8 / +32.3 | 21 / +19.5 | 6 / +147.5 | 10 / +73.6 |
| HTF EMA9 late | 9 / +0.2 | 3 / -4.4 | 2 / -8.7 | 3 / +90.8 | 3 / -25.3 | 3 / -20.3 |
| HTF EMA20 Pierce | 13 / -22.3 | 10 / -5.9 | 5 / -2.1 | 19 / -45.2 | 15 / -86.0 | 6 / +65.7 |
| HTF EMA20 late | 4 / -9.4 | — | 1 / +4.8 | 3 / -21.9 | — | — |
| HTF Pullback | 1 / -5.0 | 1 / -6.9 | — | 3 / -57.5 | — | 1 / +32.0 |
| LTF EMA20 Touch | — | — | — | — | 1 / -30.0 | — |

### (C) Live MES 5m confirmation

| Chart / window | Group | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|---|
| MES 2m since 10/19 | confirmed | 100 | 88 | 51% | +8.8 | +0.10 | -20.1 / +28.9 |
| MES 2m since 10/19 | unconfirmed | 55 | 54 | 34% | -91.4 | -1.69 | -25.0 / -66.4 |
| MES 2m since 11/06 | confirmed | 33 | 30 | 57% | +26.3 | +0.88 | +37.3 / -10.9 |
| MES 2m since 11/06 | unconfirmed | 0 | 0 | 0% | +0.0 | +0.00 | +0.0 / +0.0 |
| MES 3m since 10/19 | confirmed | 85 | 77 | 51% | +7.3 | +0.09 | -46.4 / +53.7 |
| MES 3m since 10/19 | unconfirmed | 35 | 30 | 37% | -18.9 | -0.63 | -32.2 / +13.2 |
| MES 3m since 11/06 | confirmed | 8 | 7 | 29% | -43.3 | -6.19 | -22.2 / -21.1 |
| MES 3m since 11/06 | unconfirmed | 0 | 0 | 0% | +0.0 | +0.00 | +0.0 / +0.0 |

MES 2m common date halves (split 10/28 11:52): conf h1 17 / -18.6 (avg -1.10) · conf h2 71 / +27.5 (avg +0.39) · unconf h1 54 / -91.4 (avg -1.69) · unconf h2 0 / +0.0 (avg +0.00)
MES 3m common date halves (split 10/27 18:48): conf h1 24 / -11.4 (avg -0.48) · conf h2 53 / +18.7 (avg +0.35) · unconf h1 29 / -22.7 (avg -0.78) · unconf h2 1 / +3.8 (avg +3.75)

### (E) Exit Rule alerts (v10.79+)

Exit Rule alerts found (after dedupe): 13 (MES 3m hit 1, MGC 3m armed 7, MGC 3m hit 5); first 11/09 10:57.

| Chart | Rule | Time | Dir | Rule result | CBC result (Setup Ended) | Rule − CBC |
|---|---|---|---|---|---|---|
| MGC 3m | Profit lock | 11/09 11:00 | LONG | +3.20 | +2.00 | +1.20 |
| MGC 3m | Profit lock | 11/09 23:57 | SHORT | +0.90 | no matching setup | — |
| MGC 3m | Profit lock | 11/10 02:21 | SHORT | +3.02 | no matching setup | — |
| MGC 3m | Profit lock | 11/10 23:09 | LONG | +1.70 | no matching setup | — |
| MGC 3m | Profit lock | 11/11 06:21 | LONG | +1.90 | -5.00 | +6.90 |
| MES 3m | TP cut | 11/12 10:30 | LONG | +11.44 | +5.25 | +6.19 |

| Chart (period) | Hits with ended setup | Sum rule | Sum CBC | Rule − CBC | Halves (rule − CBC) |
|---|---|---|---|---|---|
| MES 3m | 1 | +11.44 | +5.25 | +6.19 | +0.00 / +6.19 |
| MGC 3m before 11/08 | 0 | +0.00 | +0.00 | +0.00 | +0.00 / +0.00 |
| MGC 3m from 11/08 (50 % + trail 3.5) | 2 | +5.10 | -3.00 | +8.10 | +1.20 / +6.90 |

### (F) Late trigger × room (first trigger late; room = x TP1 from the "Room:" line)

#### MES 2m — 155 setups (142 ended), 83 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/05 07:24

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 5 | 5 | 20% | -16.2 | -3.23 | -0.4 / -15.8 |
| late & room ≥ 0.5 | 8 | 7 | 43% | +1.8 | +0.26 | -12.6 / +14.4 |
| not late & room < 0.5 | 28 | 23 | 74% | +70.7 | +3.07 | +16.6 / +54.1 |
| not late & room ≥ 0.5 | 31 | 30 | 50% | -12.3 | -0.41 | +17.9 / -30.1 |
| late & room < 0.3 | 4 | 4 | 0% | -22.1 | -5.52 | -6.3 / -15.8 |
| late & room < 0.75 | 8 | 7 | 14% | -28.5 | -4.07 | -12.8 / -15.8 |
| (no Room line) late | 11 | 10 | 44% | -16.5 | -1.65 | -16.5 / +0.0 |
| (no Room line) not late | 72 | 67 | 34% | -110.1 | -1.64 | -110.1 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): +16.2 pts on 5 ended setups — too few yet.

#### MES 3m — 120 setups (107 ended), 79 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/03 07:18

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 8 | 8 | 62% | +7.2 | +0.90 | +11.0 / -3.8 |
| late & room ≥ 0.5 | 2 | 2 | 50% | +6.2 | +3.12 | +15.8 / -9.6 |
| not late & room < 0.5 | 18 | 16 | 56% | -6.2 | -0.39 | +17.6 / -23.8 |
| not late & room ≥ 0.5 | 13 | 11 | 64% | +47.8 | +4.34 | +26.0 / +21.8 |
| late & room < 0.3 | 5 | 5 | 80% | +19.5 | +3.89 | +14.1 / +5.4 |
| late & room < 0.75 | 9 | 9 | 56% | -2.4 | -0.26 | +11.0 / -13.4 |
| (no Room line) late | 17 | 15 | 27% | -39.6 | -2.64 | -39.6 / +0.0 |
| (no Room line) not late | 62 | 55 | 44% | -27.1 | -0.49 | -27.1 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): -7.2 pts on 8 ended setups — too few yet.

#### MES 5m — 81 setups (71 ended), 40 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/04 21:45

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 6 | 5 | 60% | +13.5 | +2.70 | +7.0 / +6.5 |
| late & room ≥ 0.5 | 4 | 4 | 50% | -4.4 | -1.10 | +4.8 / -9.2 |
| not late & room < 0.5 | 14 | 12 | 58% | +5.6 | +0.47 | +19.4 / -13.7 |
| not late & room ≥ 0.5 | 17 | 13 | 62% | +9.4 | +0.72 | +0.7 / +8.7 |
| late & room < 0.3 | 6 | 5 | 60% | +13.5 | +2.70 | +7.0 / +6.5 |
| late & room < 0.75 | 7 | 6 | 50% | +7.5 | +1.25 | +7.0 / +0.5 |
| (no Room line) late | 11 | 9 | 44% | -12.9 | -1.44 | -12.9 / +0.0 |
| (no Room line) not late | 29 | 28 | 46% | -29.5 | -1.06 | -29.5 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): -13.5 pts on 5 ended setups — too few yet.

#### MES 3m bot windows — 90 setups (81 ended), 57 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/03 04:39

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 8 | 8 | 62% | +7.2 | +0.90 | +5.0 / +2.2 |
| late & room ≥ 0.5 | 2 | 2 | 50% | +6.2 | +3.12 | +15.8 / -9.6 |
| not late & room < 0.5 | 12 | 10 | 70% | +21.0 | +2.10 | +8.1 / +12.9 |
| not late & room ≥ 0.5 | 11 | 10 | 70% | +54.8 | +5.48 | +26.0 / +28.8 |
| late & room < 0.3 | 5 | 5 | 80% | +19.5 | +3.89 | +8.1 / +11.4 |
| late & room < 0.75 | 9 | 9 | 56% | -2.4 | -0.26 | +5.0 / -7.4 |
| (no Room line) late | 13 | 12 | 33% | -23.1 | -1.92 | -23.1 / +0.0 |
| (no Room line) not late | 44 | 39 | 46% | -1.9 | -0.05 | -1.9 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): -7.2 pts on 8 ended setups — too few yet.

#### Late & room < 0.5 setups, last 5 trading days (11/06, 11/09, 11/10, 11/11, 11/12)

| Chart | Time | Dir | First trigger | Room | Room x TP1 | VWAP ext | Result |
|---|---|---|---|---|---|---|---|
| MES 2m | 11/05 21:38 | LONG | LTF EMA20 Pierce (late, 1 bars after) | OB- 7413.75-7403.00 at 0 pts | 0.00 | +5.9 ATR | -8.00 |
| MES 3m | 11/06 06:54 | LONG | LTF EMA20 Pierce (late, 1 bars after) | HTF Piv-H 7411.00 at 4 pts | 0.38 | +4.4 ATR | -9.25 |
| MES 3m | 11/08 18:48 | SHORT | LTF EMA20 Pierce (late, 1 bars after) | AS OR-H 7400.50 at 1.5 pts | 0.11 | +0.2 ATR | +11.39 |
| MES 5m | 11/09 20:40 | LONG | LTF EMA20 Pierce (late, 1 bars after) | OB- 7585.75-7580.50 at 0 pts | 0.00 | +1.2 ATR | open |
| MES 5m | 11/11 03:55 | LONG | LTF EMA20 Pierce (late, 1 bars after) | HTF Piv-H 7595.50 at 1 pts | 0.17 | +4.0 ATR | +4.80 |
| MES 2m | 11/11 07:02 | LONG | LTF EMA20 Pierce (late, 1 bars after) | HTF EQH 7613.50 at 0.5 pts | 0.12 | +11.5 ATR | -5.00 |
| MES 2m | 11/11 14:44 | LONG | HTF EMA20 Pierce (late) | R2 7651.00 at 0.33 pts | 0.06 | +8.4 ATR | -2.75 |
| MES 5m | 11/12 05:55 | LONG | LTF EMA20 Pierce (late, 1 bars after) | LTF Piv-L 7615.00 at 0.25 pts | 0.04 | +0.9 ATR | -2.75 |
| MES 5m | 11/12 06:15 | SHORT | LTF EMA20 Pierce (late, 1 bars after) | AS OR-H 7612.50 at 0.25 pts | 0.05 | -0.3 ATR | +4.43 |

First MES setup with a Room line: 10/29 20:36.


### (B) TP1 on the real MES 3m setups (10/19 → 11/12, 107 ended setups with bars + SL1; 0 skipped: no bar / no SL1)

| TP1 | Net | Win % | Avg | Halves | Thirds |
|---|---|---|---|---|---|
| 1.50 ATR | +33.1 | 49% | +0.31 | -12.3 / +45.5 | -30.6 / -6.2 / +69.9 |
| 1.75 ATR (live) | +60.8 | 47% | +0.57 | -1.1 / +62.0 | -19.8 / -15.2 / +95.9 |
| 2.00 ATR | +64.7 | 43% | +0.61 | -7.5 / +72.2 | -19.0 / -34.1 / +117.8 |
| Δ 1.5 − 1.75 | -27.7 | | | -11.2 / -16.5 | -10.7 / +9.0 / -26.0 |
| Δ 2.0 − 1.75 | +3.9 | | | -6.3 / +10.2 | +0.8 / -18.8 / +21.9 |

Validation (own SL1 + own TP1 from the Trade Setup alert): replay +17.4 vs actual -11.6; win/loss agreement 106 / 107 (99%).
Note: live MES 3m TP1 was 1.75 (v10.54–10.66), 2.0 (v10.67–10.81) and 1.75 again from v10.82 (11/08), so actual results mix both targets.


### (A) Replay — slow chart EMA 20 vs 14 vs 16 (mes3_watch_a.py; LIVE exits, TP1 1.75 and dict(LIVE, tp=1.5))

Data: 102285 candles, 01/05 → 11/12. Thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/12. Last 4 weeks from 10/15; last 5 trading days: 11/05, 11/08, 11/09, 11/10, 11/11 (Globex sessions).

#### Live exits, TP1 1.75 (live)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1736 | 49% | +39 | +0.02 | +0 | +0.0 | +0 / +0 / +0 | baseline | +206.0 | +95.5 | Flip 318 / -213 (+0) · LTF20 985 / +227 (+0) · HTF9 269 / -66 (+0) · HTF20 164 / +91 (+0) |
| 7 / 14 | 1973 | 50% | +247 | +0.13 | +207 | +0.7 | +6 / +37 / +164 | noise | +28.6 | -48.2 | Flip 332 / -155 (+19) · LTF20 1226 / +381 (+13) · HTF9 260 / -66 (-5) · HTF20 155 / +87 (+2) |
| 7 / 16 | 1882 | 50% | +266 | +0.14 | +226 | +0.9 | -1 / +79 / +148 | noise | +77.3 | +3.9 | Flip 329 / -178 (+19) · LTF20 1121 / +423 (+41) · HTF9 271 / -73 (+6) · HTF20 161 / +95 (+11) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)

#### Live exits, TP1 1.5

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1769 | 54% | +164 | +0.09 | +0 | +0.0 | +0 / +0 / +0 | baseline | +182.7 | +85.7 | Flip 318 / -193 (+0) · LTF20 1001 / +334 (+0) · HTF9 278 / -40 (+0) · HTF20 172 / +62 (+0) |
| 7 / 14 | 2006 | 54% | +266 | +0.13 | +102 | +0.4 | +92 / -40 / +50 | noise | -12.1 | -48.8 | Flip 332 / -122 (+17) · LTF20 1245 / +335 (-27) · HTF9 266 / -41 (-4) · HTF20 163 / +94 (+2) |
| 7 / 16 | 1917 | 55% | +385 | +0.20 | +221 | +1.0 | +115 / +38 / +68 | noise | +44.1 | +1.5 | Flip 329 / -142 (+17) · LTF20 1142 / +485 (+10) · HTF9 279 / -38 (+8) · HTF20 167 / +79 (+9) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)


---

## Run 2026-11-12 09:44 ET (Thu, also stands in for the missed 11/11 run)

Detailed tables superseded by the 17:37 run (MES 3m was silent 11/08 20:45 → 11/12 09:30). Verdicts: (A) keep 9 / 20 -- slow 14 Δ +214 z 0.8, slow 16 Δ +222 z 0.9; last 4 wk +34 / +72. (B) keep 1.75 -- 106 setups: 1.5 +27.9 / 1.75 +55.6 / 2.0 +59.5. (C) keep watching -- 2m 84 conf +0.30 vs 54 unconf -1.69; 3m 76 conf +0.03 vs 30 unconf -0.63. (D) keep watching -- LTF late 2m 18 / -24.0, 3m 20 / -21.1, 5m 15 / -7.5; bot set 31 / +25.7. (E) keep watching -- MGC 3m lock 5 hits (2 comparable, +8.10 vs CBC). (F) too few yet -- MES 3m 8 / +7.2, MES 2m 5 / -16.2, MES 5m 5 / +13.5.

---

## Run 2026-11-09 17:38 ET (Mon)

(A) keep 9 / 20 (slow 14 +204 z 0.7, slow 16 +201 z 0.8). (B) keep 1.75 (105: 1.5 +46.6 / 1.75 +74.3 / 2.0 +78.2). (C) keep watching both. (D) keep watching (LTF late 2m 15 / -27.0, 3m 20 / -21.1, 5m 9 / -4.7). (E) keep watching (first MGC 3m lock hit +3.2 vs +2.0). (F) too few yet.

---

## Run 2026-11-07 09:44 ET (delayed 11/06 Friday run) -- latest Friday replays (used for this week's verdicts)

Replays used live TP1 2.0 (v10.67–10.81); MES 3m 9 / 20 + range gate + live exits; MES 2m slow 14 + 1H MTF gate + base exits (from 06/01); MES 5m 9 / 20 no gates + base exits.

#### (D) Replay per trigger -- net pts (thirds)

| Trigger | MES 2m (06/01 →) | MES 3m (01/05 →) | MES 5m (01/05 →) |
|---|---|---|---|
| Flip | 443 / -77.1 (-39 / +6 / -44) | 312 / -133.1 (-48 / -146 / +61) | 341 / -35.4 (-2 / +35 / -68) |
| LTF20 on-candle | 633 / +174.8 (+28 / +106 / +41) | 767 / +104.8 (+178 / -227 / +155) | 628 / -142.9 (-198 / +79 / -24) |
| LTF20 late | 155 / -3.4 (+44 / -34 / -14) | 176 / +8.4 (+15 / -39 / +33) | 118 / +41.2 (+67 / -29 / +3) |
| HTF EMA9 (incl late) | 212 / -19.8 (-23 / +6 / -3) | 257 / -32.7 (+52 / -79 / -6) | 241 / -12.3 (-28 / +6 / +9) |
| HTF EMA20 (incl late) | 101 / +37.4 (+2 / +26 / +9) | 157 / +41.1 (+41 / +3 / -3) | 187 / +26.9 (+59 / -41 / +10) |
| All | 1544 / +111.9 | 1669 / -11.4 | 1515 / -122.5 |

LTF late window 0 / 2 / 3 vs 1 (Δ, z): MES 2m -44.1 z -1.0 / +20.8 z 0.7 / +21.4 z 0.7; MES 3m -2.4 z -0.0 / +8.1 z 0.2 / -1.0 z -0.0; MES 5m -74.1 z -1.7 / -68.8 z -2.2 / -96.3 z -2.6. Window 0 never better.

#### (C) Replay -- MES 5m confirmation

MES 2m by 5m: 463 conf +0.05 vs 1081 unconf +0.08, Δ -0.03, z -0.1, thirds -0.27 / -0.08 / +0.25. MES 3m by 5m: 550 conf +0.10 vs 1114 unconf -0.06, Δ +0.16, z 0.4, thirds +1.11 / +0.01 / -0.48.

#### (E) Replay -- exit rules vs current exits (Δ / z / thirds / last 4 wk)

MES 3m TP cut 21 min / 70 % / ATR ≥ 1.5x: +167.5 / 2.8 / +131 · +6 · +30 / +0.3 (neighbours 15 / 18 / 24 min, 65 / 75 %, 1.4x / 1.6x all +115…+196, z 2.1–2.8; middle third -1 / -3 / -20 on 15 min / 65 % / 75 %).
MGC 3m lock 75 % → +55 %: +306.9 / 2.4 / +126 · +85 · +96 / -45 (neighbours 70 / 80 %, +50 / +60 % all +231…+358, z 1.9–2.7, every last 4 wk negative). That replay used the pre-v10.84 MGC 3m exits (80 % + trail 1.7); the next Friday replay should use chop_sim EXIT (MGC,3) (50 % + trail 3.5).

---

## Run 2026-11-05 17:37 ET (Thu)

(A) keep 9 / 20 (TP1 2.0: slow 14 +184 z 0.6, slow 16 +178 z 0.7). (B) keep 2.0 (100: 2.0 +100.9 > 1.75 +93.9 > 1.5 +68.7). (C) MES 2m ACT (provisional), MES 3m keep watching. (D) keep watching.
