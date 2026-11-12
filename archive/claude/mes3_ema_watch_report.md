# MES watch: chart EMA / TP1 / 5m confirmation / per-trigger / exit rules / late + room -- 2026-11-12 09:44 ET

Daily scheduled study. Live = CBC v10.87 (MES 3m chart EMAs 9 / 20, TP1 1.75 ATR since v10.82; bot: Flip + LTF Pierce beyond EMA9, 5-day short filter, entry windows 18:30-22:00 / 03:00-13:00 / 15:00-15:30 ET). Newest run on top; history tables keep one line per run. Settings check (claude/settings_sync_report.md, last written 11/09 14:43 ET): 0 MISMATCH, 1 known -- study settings current. **This run: MES 3m alerts missing 11/08 20:45 → 11/12 09:30 ET (see data warnings).**

## History

### (A) Chart EMA — replay Jan 5 → now, live exits, Δ vs slow 20

TP1 in the replay: 2.0 until the 11/07 run, 1.75 from 11/09 (live v10.82+), so rows before 11/09 are not directly comparable.

| Run | TP1 | Slow 14: Δ / z / thirds | Slow 14 last 4 wk Δ | Slow 14 last 5 days Δ | Slow 16: Δ / z / thirds | Slow 16 last 4 wk Δ | Slow 16 last 5 days Δ | Last-4-wk beat count (of last 7 runs) 14 / 16 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-12 09:44 ET | 1.75 | +214 / 0.8 / +6 · +37 · +171 | +34 | -42 | +222 / 0.9 / -1 · +79 · +144 | +72 | -0 | 3 of 4 / 3 of 4 | keep 9 / 20 |
| 2026-11-09 17:38 ET | 1.75 | +204 / 0.7 / +6 · +45 · +153 | +35 | -85 | +201 / 0.8 / -1 · +78 · +124 | +59 | -28 | 2 of 3 / 2 of 3 | keep 9 / 20 |
| 2026-11-07 09:44 ET (11/06 Fri run) | 2.0 | +135 / 0.5 / -19 · +55 · +99 | -5 | -78 | +153 / 0.6 / +12 · +124 · +18 | -3 | -50 | 1 of 2 / 1 of 2 | keep 9 / 20 |
| 2026-11-05 17:37 ET | 2.0 | +184 / 0.6 / -28 · +64 · +148 | +34 | -34 | +178 / 0.7 / +10 · +132 · +36 | +15 | -26 | 1 of 1 / 1 of 1 | keep 9 / 20 |

### (B) TP1 on the real MES 3m setups since 10/19

| Run | Ended | 1.5 | 1.75 | 2.0 | Δ 1.5 − 1.75 (halves) | Δ 2.0 − 1.75 (halves) | Verdict |
|---|---|---|---|---|---|---|---|
| 2026-11-12 09:44 ET | 106 | +27.9 | +55.6 | +59.5 | -27.7 (-11.2 / -16.5) | +3.9 (-6.3 / +10.2) | keep 1.75 |
| 2026-11-09 17:38 ET | 105 | +46.6 | +74.3 | +78.2 | -27.7 (-10.7 / -17.0) | +3.9 (-6.8 / +10.7) | keep 1.75 |
| 2026-11-07 09:44 ET | 103 | +55.8 | +81.9 | +84.2 | -26.1 | +2.3 (-8.0 / +10.3) | keep 2.0 (was live) |

### (C) MES 5m confirmation — live since 10/19, avg pts per ended setup (confirmed vs unconfirmed)

| Run | MES 2m conf (n / avg) | MES 2m unconf (n / avg) | Δ | MES 3m conf (n / avg) | MES 3m unconf (n / avg) | Δ | Friday replay | Verdict 2m / 3m |
|---|---|---|---|---|---|---|---|---|
| 2026-11-12 09:44 ET | 84 / +0.30 | 54 / -1.69 | +1.99 | 76 / +0.03 | 30 / -0.63 | +0.66 | 11/06: 2m Δ -0.03 z -0.1; 3m Δ +0.16 z 0.4 | keep watching / keep watching |
| 2026-11-09 17:38 ET | 66 / +0.14 | 54 / -1.69 | +1.83 | 75 / +0.28 | 30 / -0.63 | +0.91 | 11/06: 2m Δ -0.03 z -0.1; 3m Δ +0.16 z 0.4 | keep watching / keep watching |
| 2026-11-07 09:44 ET (11/06 Fri run) | 62 / +0.13 | 54 / -1.69 | +1.82 | 73 / +0.39 | 30 / -0.63 | +1.02 | 2m Δ -0.03 z -0.1 (thirds -/-/+); 3m Δ +0.16 z 0.4 (thirds +/+/-) | keep watching / keep watching |
| 2026-11-05 17:37 ET | 56 / -0.26 | 54 / -1.69 | +1.44 | 70 / +0.72 | 30 / -0.63 | +1.35 | none yet (11/05 ad-hoc: 2m z 1.3, 3m z 1.1, all thirds) | ACT (provisional) / keep watching |

### (D) Per trigger — live since 10/19 (ended / net)

| Run | MES 2m LTF late | MES 3m LTF late | MES 5m LTF late | MES 3m bot set (Flip + LTF beyond EMA9) | MES 3m everything else | Friday replay (LTF late window 0 vs 1) | Verdict |
|---|---|---|---|---|---|---|---|
| 2026-11-12 09:44 ET | 18 / -24.0 | 20 / -21.1 | 15 / -7.5 | 31 / +25.7 (avg +0.83) | 75 / -42.6 | 11/06: 2m Δ -44 z -1.0 · 3m Δ -2 z 0.0 · 5m Δ -74 z -1.7 | keep watching |
| 2026-11-09 17:38 ET | 15 / -27.0 | 20 / -21.1 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | 75 / -42.6 | 11/06: 2m Δ -44 z -1.0 · 3m Δ -2 z 0.0 · 5m Δ -74 z -1.7 | keep watching |
| 2026-11-07 09:44 ET (11/06 Fri run) | 14 / -33.4 | 19 / -32.5 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | 73 / -35.0 | 2m Δ -44 z -1.0 · 3m Δ -2 z 0.0 · 5m Δ -74 z -1.7 (window 0 worse or equal everywhere) | keep watching (no trigger near 40 ended; replay disagrees with switch-off) |
| 2026-11-05 17:37 ET | 13 / -25.4 | 18 / -23.2 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | 70 / -12.8 | not run (Thursday) | keep watching (no trigger near 40 ended) |

### (E) Exit rules (v10.79) — live hits and Friday replay

| Run | MES 3m TP cut live hits: rule vs CBC | MGC 3m profit lock live hits: rule vs CBC | Replay MES 3m TP cut (Δ / z / thirds / last 4 wk) | Replay MGC 3m lock (Δ / z / thirds / last 4 wk) | Verdict |
|---|---|---|---|---|---|
| 2026-11-12 09:44 ET | 0 (MES 3m alerts silent 11/08 eve → 11/12) | 5 hits, 2 comparable: +5.10 vs -3.00 (+8.10; halves +1.20 / +6.90) | 11/06: +168 / 2.8 / all + / +0.3 | 11/06: +307 / 2.4 / all + / -45 | keep watching (MES 0 / MGC 2 of 15 comparable hits) |
| 2026-11-09 17:38 ET | 0 | 1 (from 11/08): +3.2 vs +2.0 (+1.2) | 11/06: +168 / 2.8 / all + / +0.3 | 11/06: +307 / 2.4 / all + / -45 | keep watching (MES 0 / MGC 1 of 15 hits) |
| 2026-11-07 09:44 ET (11/06 Fri run) | 0 (no Exit Rule alerts yet) | 0 (no Exit Rule alerts yet) | +168 / 2.8 / +131 · +6 · +30 / +0.3 (all 7 neighbours + , z ≥ 2.1) | +307 / 2.4 / +126 · +85 · +96 / -45 (all 4 neighbours +, z ≥ 1.9) | keep watching (0 of 15 live hits) |

### (F) Late trigger + room < 0.5 x TP1 — live (Room line exists from 10/29), ended / net / avg

| Run | MES 3m | MES 2m | MES 5m | MES 3m bot windows | Verdict |
|---|---|---|---|---|---|
| 2026-11-12 09:44 ET | 8 / +7.2 / +0.90 | 5 / -16.2 / -3.23 | 5 / +13.5 / +2.70 | 8 / +7.2 / +0.90 | too few yet (all charts) |
| 2026-11-09 17:38 ET | 8 / +7.2 / +0.90 | 3 / -8.4 / -2.80 | 2 / +7.0 / +3.51 | 8 / +7.2 / +0.90 | too few yet (all charts) |

---

## Run 2026-11-12 09:44 ET (Thu)

**Manual re-run 2026-11-12 09:50 ET (for the missed 11/11 Wed run, usage limit):** alerts re-fetched — no new setups since the 09:44 run (identical live tables), and the 09:44 run already contains every alert an 11/11 run would have seen, so it stands in for the 11/11 run; no separate history rows (so the (A) "beat count" is not double-counted). Settings sync report still dated 11/09 — used as-is. Server now v14 (/health: drops near-copy alerts on arrival); stored duplicates not yet cleaned (lastDedupe null), so the in-script dedupe stays on.

Thursday run: the Friday-only replays (step 3 per-trigger replay + LTF late-window test, (C) replay, (E) replay) were not run; the latest ones (11/06 Friday run, below) are used for the verdicts. Live data through 11/12 09:39 ET; BarFeed MES 3m through 11/12 (102 140 candles from 01/05). Settings check (claude/settings_sync_report.md, last written 11/09 14:43 ET — not refreshed since): 0 MISMATCH, 1 known — study settings current.

**Data warnings this run**

- **MES 3m CBC alerts were silent from 11/08 20:45 ET to 11/12 09:30 ET** (no Trade Setup / Setup Ended / any MES 3m alert reached the store; MES 2m and MES 5m kept arriving). Only 1 new MES 3m setup since the 11/09 run (11/12 09:30 SHORT, HTF CBC Flip, -18.7 SL1). All MES 3m live numbers below are therefore essentially unchanged since 11/09. Worth checking the MES 3m CBC alert in TradingView (and whether the bot's own alert was affected).
- Duplicate alerts (claude/DATA_NOTES.md): the server has not de-duplicated yet (/health serverVersion 13, lastDedupe null). This run drops near copies itself (same chart + Time line + set of "•" names within 60 s, keep the longest): 1 504 dropped. 6 setups had two different Setup Ended results; the 0.5×(TP1) version was kept. MGC 3m live results 11/09–11/12 are partly on the old exits.
- MGC 3m: 3 of the 5 Profit-lock hits have no Trade Setup and no Setup Ended alert stored (11/09 23:21, 11/10 02:12, 11/10 22:33 setups), so they cannot be compared with CBC.

### Verdicts

- **(A) EMA: keep 9 / 20, keep watching.** Replay with live exits (TP1 1.75): slow 14 Δ +214 (z 0.8, thirds +6 / +37 / +171), slow 16 Δ +222 (z 0.9, thirds -1 / +79 / +144) — not robust (needs z ≥ 2 and all thirds +). Last 4 weeks: 14 +34, 16 +72 (beat 20 in 3 of the last 4 runs each; need 5 of 7). Last 5 trading days: 14 -42, 16 -0.3. TP1 1.5 variant: slow 16 Δ +218, z 0.98, all thirds + (on the edge of "promising").
- **(B) TP1: keep 1.75.** Real MES 3m setups (106 ended): 2.0 ATR +59.5 ≥ 1.75 +55.6 > 1.5 +27.9. 2.0 − 1.75 = +3.9 but halves -6.3 / +10.2 and thirds +0.8 / -18.8 / +21.9; 1.5 − 1.75 = -27.7 (halves -11.2 / -16.5). Validation 105 / 106 win/loss agreement.
- **(C) 5m confirmation — MES 2m: keep watching.** Live passes the live part: 84 confirmed ended avg +0.30 vs 54 unconfirmed -1.69 (+1.99/setup); date halves h1 -1.33 vs -1.71, h2 +0.68 vs -1.00 (h2 has only 1 unconfirmed). Fails the replay condition (11/06 Friday replay Δ -0.03, z -0.1). **MES 3m: keep watching** — 76 confirmed +0.03 vs 30 unconfirmed -0.63 (+0.66); halves disagree (h2: 1 unconfirmed, +3.75); replay Δ +0.16, z 0.4. Note: there has been only 1 unconfirmed MES 2m and 1 unconfirmed MES 3m setup since 10/28 — the split now barely grows. Acting would need a new CBC filter or dashboard flag (not built).
- **(D) Per trigger: keep watching on every MES chart** — no trigger has 40+ ended live setups. LTF Pierce LATE: MES 2m 18 / -24.0 (avg -1.33, halves -12.6 / -11.4), MES 3m 20 / -21.1 (avg -1.05, halves -34.5 / +13.4), MES 5m 15 / -7.5 (avg -0.50, halves -22.1 / +14.6). Latest Friday replay does not back a switch-off (window 0 vs 1: MES 2m -44 z -1.0, MES 3m -2 z 0.0, MES 5m -74 z -1.7). MES 3m bot set 31 / +25.7 (avg +0.83, halves +4.0 / +21.8) vs everything else 75 / -42.6 — no ADD candidate.
- **(E) Exit rules: keep watching.** MES 3m TP cut: 0 hits (MES 3m alerts silent 11/08 evening → 11/12). MGC 3m profit lock: 5 hits since 11/09; 2 with a stored Setup Ended: rule +5.10 vs CBC -3.00 (+8.10; halves +1.20 / +6.90); 3 hits (+0.90, +3.02, +1.70) without stored setup alerts. Far from 15 hits. Latest Friday replay (11/06): MES 3m +168, z 2.8; MGC 3m +307, z 2.4, but last 4 wk -45.
- **(F) Late + room < 0.5: too few yet on every chart.** MES 3m 8 ended / +7.2 (avg +0.90) — unchanged (alert gap); not late & room < 0.5 15 / -11.5, late & room ≥ 0.5 2 / +6.2. MES 2m 5 / -16.2 (avg -3.23; neighbours < 0.3 4 / -22.1, < 0.75 7 / -28.5 — the only chart where the combination looks bad, but n = 5 and "not late & room < 0.5" is +65.5, so it's the late trigger, not room). MES 5m 5 / +13.5 (avg +2.70, 1 open). MES 3m bot windows 8 / +7.2 (the bot does not take late triggers anyway).

## Live (steps 1, 2, 4, 6b, 6c)

### Live per chart (10/19 → 11/12 09:30)

| Chart | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| MES 2m | 151 | 138 | 45% | -66.5 | -0.48 | -111.6 / +45.1 |
| MES 3m | 119 | 106 | 46% | -16.9 | -0.16 | -34.1 / +17.2 |
| MES 5m | 77 | 67 | 51% | -30.2 | -0.45 | -23.5 / -6.7 |
| MGC 2m | 204 | 186 | 47% | -60.5 | -0.33 | -31.2 / -29.2 |
| MGC 3m | 85 | 74 | 45% | -2.6 | -0.03 | -14.8 / +12.3 |
| MGC 5m | 69 | 63 | 48% | -14.9 | -0.24 | -7.7 / -7.1 |
| MNQ 2m | 202 | 187 | 40% | -360.2 | -1.93 | -405.8 / +45.7 |
| MNQ 3m | 117 | 108 | 31% | -972.3 | -9.00 | -513.6 / -458.7 |
| MNQ 5m | 72 | 60 | 52% | +487.2 | +8.12 | +295.1 / +192.0 |
| MES 3m 10/19–11/04 (9 / 20) | 107 | 95 | 47% | +6.7 | +0.07 | -49.0 / +55.7 |
| MES 3m 11/05 (7 / 14 build) | 5 | 5 | 60% | +24.9 | +4.99 | -1.7 / +26.6 |
| MES 3m 11/06–11/07 (9 / 20, TP1 2.0) | 4 | 3 | 0% | -22.2 | -7.42 | -9.2 / -13.0 |
| MES 3m from 11/08 (TP1 1.75, v10.82+) | 3 | 3 | 33% | -26.3 | -8.77 | +11.4 / -37.7 |
| MGC 3m before 11/08 | 77 | 67 | 42% | -34.2 | -0.51 | -6.1 / -28.1 |
| MGC 3m from 11/08 (50 % + trail 3.5; partly old exits to 11/12) | 8 | 7 | 71% | +31.7 | +4.52 | +32.9 / -1.2 |

Matched: 1096 Trade Setup alerts, 989 ended; 95 Setup Ended alerts without a matching Trade Setup (not counted). Near-duplicate alerts dropped: 1504; setups with two Setup Ended results: 6 (0.5×(TP1) version kept).

### (D) Live per trigger — MES 2m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 40 | 37 | 51% | -6.2 | -0.17 | -15.2 / +9.0 |
| LTF Pierce beyond EMA9 | 39 | 34 | 50% | -2.2 | -0.06 | -56.8 / +54.6 |
| LTF Pierce not beyond | 29 | 26 | 38% | -21.3 | -0.82 | -19.3 / -2.0 |
| LTF Pierce LATE | 18 | 18 | 39% | -24.0 | -1.33 | -12.6 / -11.4 |
| HTF EMA9 Pierce | 7 | 7 | 57% | +4.9 | +0.70 | -2.7 / +7.6 |
| HTF EMA9 late | 3 | 2 | 0% | -6.1 | -3.06 | +0.0 / -6.1 |
| HTF EMA20 Pierce | 10 | 10 | 30% | -7.8 | -0.78 | +4.8 / -12.5 |
| HTF EMA20 late | 3 | 2 | 50% | -0.8 | -0.38 | +2.0 / -2.8 |
| HTF Pullback | 2 | 2 | 50% | -3.2 | -1.60 | -8.0 / +4.8 |

### (D) Live per trigger — MES 3m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 18 | 16 | 56% | +23.0 | +1.44 | +9.8 / +13.2 |
| LTF Pierce beyond EMA9 | 18 | 15 | 60% | +2.8 | +0.18 | -11.5 / +14.2 |
| LTF Pierce not beyond | 34 | 31 | 45% | -12.2 | -0.39 | +5.0 / -17.1 |
| LTF Pierce LATE | 22 | 20 | 40% | -21.1 | -1.05 | -34.5 / +13.4 |
| HTF EMA9 Pierce | 13 | 12 | 50% | +10.6 | +0.89 | +5.2 / +5.4 |
| HTF EMA9 late | 2 | 2 | 0% | -5.9 | -2.94 | -1.2 / -4.6 |
| HTF EMA20 Pierce | 7 | 5 | 20% | -5.8 | -1.17 | -8.8 / +3.0 |
| HTF EMA20 late | 3 | 3 | 67% | +0.8 | +0.26 | -5.2 / +6.0 |
| HTF Pullback | 2 | 2 | 0% | -9.1 | -4.54 | -5.6 / -3.5 |
| **Bot set (Flip + LTF Pierce beyond EMA9)** | 36 | 31 | 58% | +25.7 | +0.83 | +4.0 / +21.8 |
| Everything else | 83 | 75 | 41% | -42.6 | -0.57 | -48.8 / +6.2 |

### (D) Live per trigger — MES 5m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 17 | 15 | 67% | +11.0 | +0.74 | +9.4 / +1.6 |
| LTF Pierce beyond EMA9 | 14 | 13 | 38% | -23.1 | -1.78 | -27.8 / +4.7 |
| LTF Pierce not beyond | 14 | 13 | 54% | +3.7 | +0.28 | +2.3 / +1.4 |
| LTF Pierce LATE | 18 | 15 | 47% | -7.5 | -0.50 | -22.1 / +14.6 |
| HTF EMA9 Pierce | 3 | 1 | 0% | -8.0 | -8.00 | +0.0 / -8.0 |
| HTF EMA9 late | 1 | 1 | 0% | -5.5 | -5.50 | +0.0 / -5.5 |
| HTF EMA20 Pierce | 7 | 6 | 50% | -4.2 | -0.70 | +4.5 / -8.7 |
| HTF EMA20 late | 2 | 2 | 100% | +9.1 | +4.56 | +4.8 / +4.3 |
| HTF Pullback | 1 | 1 | 0% | -5.8 | -5.75 | +0.0 / -5.8 |

### (D) Live per trigger — MGC / MNQ, ended setups / net pts

| Trigger | MGC 2m | MGC 3m | MGC 5m | MNQ 2m | MNQ 3m | MNQ 5m |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 49 / -22.8 | 8 / +5.7 | 15 / +5.9 | 60 / +36.9 | 30 / -233.5 | 9 / -65.5 |
| LTF Pierce beyond EMA9 | 30 / -11.4 | 15 / -16.0 | 10 / +3.1 | 21 / -294.8 | 18 / -270.5 | 12 / +61.8 |
| LTF Pierce not beyond | 37 / +23.1 | 17 / +1.9 | 9 / +18.1 | 38 / +60.8 | 26 / -508.3 | 16 / +339.4 |
| LTF Pierce LATE | 28 / -34.1 | 11 / +17.3 | 13 / -68.2 | 19 / -148.9 | 9 / +33.7 | 4 / +32.4 |
| HTF EMA9 Pierce | 16 / +16.2 | 9 / +5.8 | 8 / +32.3 | 21 / +19.5 | 6 / +147.5 | 10 / +73.6 |
| HTF EMA9 late | 9 / +0.2 | 3 / -4.4 | 2 / -8.7 | 3 / +90.8 | 3 / -25.3 | 3 / -20.3 |
| HTF EMA20 Pierce | 13 / -22.3 | 10 / -5.9 | 5 / -2.1 | 19 / -45.2 | 15 / -86.0 | 5 / +33.6 |
| HTF EMA20 late | 3 / -4.4 | — | 1 / +4.8 | 3 / -21.9 | — | — |
| HTF Pullback | 1 / -5.0 | 1 / -6.9 | — | 3 / -57.5 | — | 1 / +32.0 |
| LTF EMA20 Touch | — | — | — | — | 1 / -30.0 | — |

### (C) Live MES 5m confirmation

| Chart / window | Group | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|---|
| MES 2m since 10/19 | confirmed | 96 | 84 | 52% | +24.8 | +0.30 | -23.7 / +48.5 |
| MES 2m since 10/19 | unconfirmed | 55 | 54 | 34% | -91.4 | -1.69 | -25.0 / -66.4 |
| MES 2m since 11/06 | confirmed | 29 | 26 | 62% | +42.4 | +1.63 | +25.4 / +16.9 |
| MES 2m since 11/06 | unconfirmed | 0 | 0 | 0% | +0.0 | +0.00 | +0.0 / +0.0 |
| MES 3m since 10/19 | confirmed | 84 | 76 | 50% | +2.0 | +0.03 | -46.4 / +48.4 |
| MES 3m since 10/19 | unconfirmed | 35 | 30 | 37% | -18.9 | -0.63 | -32.2 / +13.2 |
| MES 3m since 11/06 | confirmed | 7 | 6 | 17% | -48.6 | -8.09 | -22.2 / -26.3 |
| MES 3m since 11/06 | unconfirmed | 0 | 0 | 0% | +0.0 | +0.00 | +0.0 / +0.0 |

MES 2m common date halves (split 10/28 05:50): conf h1 16 / -21.2 (avg -1.33) · conf h2 68 / +46.1 (avg +0.68) · unconf h1 53 / -90.4 (avg -1.71) · unconf h2 1 / -1.0 (avg -1.00)
MES 3m common date halves (split 10/27 18:48): conf h1 24 / -11.4 (avg -0.48) · conf h2 52 / +13.5 (avg +0.26) · unconf h1 29 / -22.7 (avg -0.78) · unconf h2 1 / +3.8 (avg +3.75)

### (E) Exit Rule alerts (v10.79+)

Exit Rule alerts found (after dedupe): 12 (MGC 3m armed 7, MGC 3m hit 5); first 11/09 10:57.

| Chart | Rule | Time | Dir | Rule result | CBC result (Setup Ended) | Rule − CBC |
|---|---|---|---|---|---|---|
| MGC 3m | Profit lock | 11/09 11:00 | LONG | +3.20 | +2.00 | +1.20 |
| MGC 3m | Profit lock | 11/09 23:57 | SHORT | +0.90 | no matching setup | — |
| MGC 3m | Profit lock | 11/10 02:21 | SHORT | +3.02 | no matching setup | — |
| MGC 3m | Profit lock | 11/10 23:09 | LONG | +1.70 | no matching setup | — |
| MGC 3m | Profit lock | 11/11 06:21 | LONG | +1.90 | -5.00 | +6.90 |

| Chart (period) | Hits with ended setup | Sum rule | Sum CBC | Rule − CBC | Halves (rule − CBC) |
|---|---|---|---|---|---|
| MES 3m | 0 | +0.00 | +0.00 | +0.00 | +0.00 / +0.00 |
| MGC 3m before 11/08 | 0 | +0.00 | +0.00 | +0.00 | +0.00 / +0.00 |
| MGC 3m from 11/08 (50 % + trail 3.5) | 2 | +5.10 | -3.00 | +8.10 | +1.20 / +6.90 |

### (F) Late trigger × room (first trigger late; room = x TP1 from the "Room:" line)

#### MES 2m — 151 setups (138 ended), 83 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/05 06:38

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 5 | 5 | 20% | -16.2 | -3.23 | -0.4 / -15.8 |
| late & room ≥ 0.5 | 8 | 7 | 43% | +1.8 | +0.26 | -7.6 / +9.4 |
| not late & room < 0.5 | 27 | 22 | 73% | +65.5 | +2.98 | +13.6 / +51.9 |
| not late & room ≥ 0.5 | 28 | 27 | 56% | +9.0 | +0.33 | +17.9 / -8.9 |
| late & room < 0.3 | 4 | 4 | 0% | -22.1 | -5.52 | -6.3 / -15.8 |
| late & room < 0.75 | 8 | 7 | 14% | -28.5 | -4.07 | -12.8 / -15.8 |
| (no Room line) late | 11 | 10 | 44% | -16.5 | -1.65 | -16.5 / +0.0 |
| (no Room line) not late | 72 | 67 | 34% | -110.1 | -1.64 | -110.1 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): +16.2 pts on 5 ended setups — too few yet.

#### MES 3m — 119 setups (106 ended), 79 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/03 07:18

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 8 | 8 | 62% | +7.2 | +0.90 | +11.0 / -3.8 |
| late & room ≥ 0.5 | 2 | 2 | 50% | +6.2 | +3.12 | +15.8 / -9.6 |
| not late & room < 0.5 | 17 | 15 | 53% | -11.5 | -0.76 | +17.6 / -29.1 |
| not late & room ≥ 0.5 | 13 | 11 | 64% | +47.8 | +4.34 | +26.0 / +21.8 |
| late & room < 0.3 | 5 | 5 | 80% | +19.5 | +3.89 | +14.1 / +5.4 |
| late & room < 0.75 | 9 | 9 | 56% | -2.4 | -0.26 | +11.0 / -13.4 |
| (no Room line) late | 17 | 15 | 27% | -39.6 | -2.64 | -39.6 / +0.0 |
| (no Room line) not late | 62 | 55 | 44% | -27.1 | -0.49 | -27.1 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): -7.2 pts on 8 ended setups — too few yet.

#### MES 5m — 77 setups (67 ended), 40 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/04 13:25

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 6 | 5 | 60% | +13.5 | +2.70 | +12.5 / +1.0 |
| late & room ≥ 0.5 | 4 | 4 | 50% | -4.4 | -1.10 | +4.8 / -9.2 |
| not late & room < 0.5 | 13 | 11 | 64% | +13.6 | +1.24 | +19.4 / -5.7 |
| not late & room ≥ 0.5 | 14 | 10 | 50% | -10.5 | -1.05 | +8.7 / -19.2 |
| late & room < 0.3 | 6 | 5 | 60% | +13.5 | +2.70 | +12.5 / +1.0 |
| late & room < 0.75 | 7 | 6 | 50% | +7.5 | +1.25 | +12.5 / -5.0 |
| (no Room line) late | 11 | 9 | 44% | -12.9 | -1.44 | -12.9 / +0.0 |
| (no Room line) not late | 29 | 28 | 46% | -29.5 | -1.06 | -29.5 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): -13.5 pts on 5 ended setups — too few yet.

#### MES 3m bot windows — 89 setups (80 ended), 57 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/03 03:45

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 8 | 8 | 62% | +7.2 | +0.90 | +5.0 / +2.2 |
| late & room ≥ 0.5 | 2 | 2 | 50% | +6.2 | +3.12 | +15.8 / -9.6 |
| not late & room < 0.5 | 11 | 9 | 67% | +15.7 | +1.75 | +18.3 / -2.6 |
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


### (B) TP1 on the real MES 3m setups (10/19 → 11/12, 106 ended setups with bars + SL1; 0 skipped: no bar / no SL1)

| TP1 | Net | Win % | Avg | Halves | Thirds |
|---|---|---|---|---|---|
| 1.50 ATR | +27.9 | 48% | +0.26 | -12.3 / +40.2 | -30.6 / -6.2 / +64.6 |
| 1.75 ATR (live) | +55.6 | 46% | +0.52 | -1.1 / +56.7 | -19.8 / -15.2 / +90.6 |
| 2.00 ATR | +59.5 | 43% | +0.56 | -7.5 / +66.9 | -19.0 / -34.1 / +112.6 |
| Δ 1.5 − 1.75 | -27.7 | | | -11.2 / -16.5 | -10.7 / +9.0 / -26.0 |
| Δ 2.0 − 1.75 | +3.9 | | | -6.3 / +10.2 | +0.8 / -18.8 / +21.9 |

Validation (own SL1 + own TP1 from the Trade Setup alert): replay +12.1 vs actual -16.9; win/loss agreement 105 / 106 (99%).
Note: live MES 3m TP1 was 1.75 (v10.54–10.66), 2.0 (v10.67–10.81) and 1.75 again from v10.82 (11/08), so actual results mix both targets.


### (A) Replay — slow chart EMA 20 vs 14 vs 16 (mes3_watch_a.py; LIVE exits, TP1 1.75 and dict(LIVE, tp=1.5))

"Last 5 trading days" = Globex sessions labelled by their 18:00 ET start date: 11/05 = Fri 11/06, 11/08 = Mon 11/09 … 11/11 = Thu 11/12 (partial).

Data: 102140 candles, 01/05 → 11/12. Thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/12. Last 4 weeks from 10/15; last 5 trading days: 11/05, 11/08, 11/09, 11/10, 11/11 (Globex sessions).

#### Live exits, TP1 1.75 (live)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1733 | 49% | +15 | +0.01 | +0 | +0.0 | +0 / +0 / +0 | baseline | +187.8 | +71.5 | Flip 318 / -213 (+0) · LTF20 983 / +214 (+0) · HTF9 268 / -77 (+0) · HTF20 164 / +91 (+0) |
| 7 / 14 | 1971 | 50% | +229 | +0.12 | +214 | +0.8 | +6 / +37 / +171 | noise | +34.2 | -41.6 | Flip 332 / -155 (+19) · LTF20 1224 / +363 (+7) · HTF9 260 / -66 (+6) · HTF20 155 / +87 (+2) |
| 7 / 16 | 1879 | 50% | +237 | +0.13 | +222 | +0.9 | -1 / +79 / +144 | noise | +72.2 | -0.3 | Flip 329 / -178 (+19) · LTF20 1118 / +395 (+25) · HTF9 271 / -73 (+17) · HTF20 161 / +95 (+11) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)

#### Live exits, TP1 1.5

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1766 | 53% | +142 | +0.08 | +0 | +0.0 | +0 / +0 / +0 | baseline | +166.2 | +64.1 | Flip 318 / -193 (+0) · LTF20 999 / +322 (+0) · HTF9 277 / -49 (+0) · HTF20 172 / +62 (+0) |
| 7 / 14 | 2004 | 54% | +250 | +0.12 | +108 | +0.4 | +92 / -40 / +56 | noise | -7.2 | -42.8 | Flip 332 / -122 (+17) · LTF20 1243 / +319 (-32) · HTF9 266 / -41 (+6) · HTF20 163 / +94 (+2) |
| 7 / 16 | 1914 | 55% | +360 | +0.19 | +218 | +1.0 | +115 / +38 / +65 | noise | +39.5 | -2.0 | Flip 329 / -142 (+17) · LTF20 1139 / +460 (-4) · HTF9 279 / -38 (+18) · HTF20 167 / +79 (+9) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)


---

## Run 2026-11-09 17:38 ET (Mon)

Monday run: Friday-only replays not run. Live data through 11/09 15:50 ET. Detailed live / (B) / (A) tables of this run are superseded by the 11/12 run above (MES 3m unchanged since then because of the alert gap); verdicts kept.

- **(A) keep 9 / 20.** TP1 1.75: slow 14 Δ +204 (z 0.7, thirds +6 / +45 / +153), slow 16 Δ +201 (z 0.8, thirds -1 / +78 / +124). Last 4 weeks 14 +35, 16 +59; last 5 days 14 -85, 16 -28. TP1 1.5: slow 16 Δ +198, z 0.9, all thirds +.
- **(B) keep 1.75.** 105 ended: 2.0 +78.2 ≥ 1.75 +74.3 > 1.5 +46.6; 2.0 − 1.75 halves -6.8 / +10.7. Validation 104 / 105.
- **(C) keep watching / keep watching.** MES 2m 66 conf +0.14 vs 54 unconf -1.69; MES 3m 75 conf +0.28 vs 30 unconf -0.63; replay 11/06 does not back either.
- **(D) keep watching.** LTF late MES 2m 15 / -27.0, MES 3m 20 / -21.1, MES 5m 9 / -4.7. Bot set 30 / +44.4 vs everything else 75 / -42.6.
- **(E) keep watching.** First Exit Rule alerts (MGC 3m profit lock 11/09 11:00: +3.2 vs CBC +2.0). MES 3m 0 hits.
- **(F) too few yet.** MES 3m 8 / +7.2, MES 2m 3 / -8.4, MES 5m 2 / +7.0, bot windows 8 / +7.2.

Live per chart 10/19 → 11/09 15:50: MES 2m 120 ended -82.2 · MES 3m 105 +1.8 · MES 5m 59 -37.1 · MGC 2m 154 -79.8 · MGC 3m 71 -20.0 · MGC 5m 52 -20.6 · MNQ 2m 156 -160.3 · MNQ 3m 108 -972.3 · MNQ 5m 54 +416.5 (no duplicate-alert handling in that run).

---

## Run 2026-11-07 09:44 ET (delayed 11/06 Friday run)

Delayed 24 h so BarFeed candles could be fixed; treated as the Friday run (all Friday-only replays done). Live data through 11/06 17:00 ET. Replays used live TP1 2.0 (v10.67–10.81). Live per-trigger / confirmation / TP1 tables of this run are superseded; verdicts and Friday replay tables kept.

**Data check (BarFeed, last 10 days):** MES 3m, MES_2, MES_5: no gaps. MGC 3m: one missing candle (11/02 14:24 ET).

### Verdicts

- **(A) EMA: keep 9 / 20.** Replay TP1 2.0: slow 14 Δ +135 (z 0.5, thirds -19 / +55 / +99), slow 16 Δ +153 (z 0.6, thirds +12 / +124 / +18). Last 4 weeks: 14 -5, 16 -3; last 5 days 14 -78, 16 -50. TP1 1.5: slow 16 Δ +217, z 1.0, all thirds +.
- **(B) TP1: keep 2.0** (then live). Real MES 3m setups (103 ended): 2.0 +84.2 ≥ 1.75 +81.9 > 1.5 +55.8. Validation 102 / 103.
- **(C) MES 2m: keep watching** (downgraded from "ACT provisional"): live 62 conf +0.13 vs 54 unconf -1.69, but Friday replay Δ -0.03, z -0.1 (replay rebuilt from the rule text on MES 2m slow 14 + 1H MTF gate). **MES 3m: keep watching** — 73 conf +0.39 vs 30 unconf -0.63, halves disagree; replay Δ +0.16, z 0.4.
- **(D) keep watching on every MES chart** — LTF late MES 2m 14 / -33.4, MES 3m 19 / -32.5, MES 5m 9 / -4.7; replay does not back a switch-off. Bot set 30 / +44.4 vs everything else 73 / -35.0.
- **(E) keep watching (no live data).** No Exit Rule alerts through 11/06. Replay supports both rules (below).

### Friday replays (steps 3, 4, 6b)

#### (D) Replay per trigger (chop_sim engine; MES 3m 9 / 20 + range gate + live exits TP1 2.0; MES 2m slow 14 + 1H MTF gate + base exits, from 06/01; MES 5m 9 / 20 no gates + base exits)

MES 2m — 06/01 → 11/06, thirds split 07/24 / 09/15

| Trigger | Setups | Win % | Net | Avg | Thirds |
|---|---|---|---|---|---|
| Flip | 443 | 51% | -77.1 | -0.17 | -39.3 / +6.4 / -44.2 |
| LTF20 on-candle | 633 | 53% | +174.8 | +0.28 | +28.0 / +106.2 / +40.6 |
| LTF20 late | 155 | 51% | -3.4 | -0.02 | +44.0 / -33.5 / -13.9 |
| HTF EMA9 (incl late) | 212 | 47% | -19.8 | -0.09 | -23.1 / +6.3 / -3.0 |
| HTF EMA20 (incl late) | 101 | 54% | +37.4 | +0.37 | +1.9 / +26.4 / +9.1 |
| **All** | 1544 | 52% | +111.9 | +0.07 | +11.5 / +111.9 / -11.4 |

| MES 2m LTF late window | Setups | Net | Δ vs window 1 | z | Δ thirds | Last 4 wk Δ |
|---|---|---|---|---|---|---|
| 0 | 1458 | +67.9 | -44.1 | -1.0 | -56.0 / +29.6 / -17.7 | -23.8 |
| 1 (live) | 1544 | +111.9 | +0.0 | +0.0 | — | +0.0 |
| 2 | 1572 | +132.8 | +20.8 | +0.7 | +23.7 / -9.3 / +6.4 | +0.0 |
| 3 | 1581 | +133.3 | +21.4 | +0.7 | +28.8 / -11.0 / +3.7 | -5.0 |

MES 3m — 01/05 → 11/06, thirds split 04/17 / 07/28

| Trigger | Setups | Win % | Net | Avg | Thirds |
|---|---|---|---|---|---|
| Flip | 312 | 52% | -133.1 | -0.43 | -47.6 / -146.3 / +60.9 |
| LTF20 on-candle | 767 | 44% | +104.8 | +0.14 | +177.7 / -227.4 / +154.5 |
| LTF20 late | 176 | 47% | +8.4 | +0.05 | +14.8 / -38.8 / +32.5 |
| HTF EMA9 (incl late) | 257 | 44% | -32.7 | -0.13 | +52.3 / -78.8 / -6.1 |
| HTF EMA20 (incl late) | 157 | 46% | +41.1 | +0.26 | +41.1 / +2.5 / -2.5 |
| **All** | 1669 | 46% | -11.4 | -0.01 | +238.2 / -488.8 / +239.3 |

| MES 3m LTF late window | Setups | Net | Δ vs window 1 | z | Δ thirds | Last 4 wk Δ |
|---|---|---|---|---|---|---|
| 0 | 1573 | -13.8 | -2.4 | -0.0 | +9.2 / +36.4 / -48.0 | -32.7 |
| 1 (live) | 1669 | -11.4 | +0.0 | +0.0 | — | +0.0 |
| 2 | 1713 | -3.3 | +8.1 | +0.2 | +31.4 / -34.6 / +11.3 | -4.0 |
| 3 | 1720 | -12.3 | -1.0 | -0.0 | +44.1 / -44.1 / -0.9 | -4.0 |

MES 5m — 01/05 → 11/06, thirds split 04/17 / 07/28

| Trigger | Setups | Win % | Net | Avg | Thirds |
|---|---|---|---|---|---|
| Flip | 341 | 53% | -35.4 | -0.10 | -2.0 / +34.9 / -68.3 |
| LTF20 on-candle | 628 | 49% | -142.9 | -0.23 | -198.4 / +79.1 / -23.6 |
| LTF20 late | 118 | 51% | +41.2 | +0.35 | +67.2 / -28.9 / +2.9 |
| HTF EMA9 (incl late) | 241 | 50% | -12.3 | -0.05 | -28.1 / +6.4 / +9.3 |
| HTF EMA20 (incl late) | 187 | 50% | +26.9 | +0.14 | +58.6 / -41.4 / +9.7 |
| **All** | 1515 | 50% | -122.5 | -0.08 | -102.7 / +50.1 / -70.0 |

| MES 5m LTF late window | Setups | Net | Δ vs window 1 | z | Δ thirds | Last 4 wk Δ |
|---|---|---|---|---|---|---|
| 0 | 1450 | -196.6 | -74.1 | -1.7 | -73.1 / +19.3 / -20.3 | -12.8 |
| 1 (live) | 1515 | -122.5 | +0.0 | +0.0 | — | +0.0 |
| 2 | 1539 | -191.3 | -68.8 | -2.2 | -33.9 / +0.8 / -35.7 | -17.4 |
| 3 | 1552 | -218.9 | -96.3 | -2.6 | -18.9 / -27.8 / -49.7 | -20.6 |

#### (C) Replay — MES 5m confirmation

| Chart | Confirmed n / avg | Unconfirmed n / avg | Δ avg | z | Δ avg by third |
|---|---|---|---|---|---|
| MES 2m by 5m | 463 / +0.05 | 1081 / +0.08 | -0.03 | -0.1 | -0.27 / -0.08 / +0.25 |
| MES 3m by 5m | 550 / +0.10 | 1114 / -0.06 | +0.16 | +0.4 | +1.11 / +0.01 / -0.48 |

#### (E) Replay — exit rules vs current exits

| Chart | Rule | Δ vs current | z | Δ thirds | Last 4 wk Δ | Setups changed |
|---|---|---|---|---|---|---|
| MES 3m | TP cut 21 min / 70 % / ATR ≥ 1.5x (live rule) | +167.5 | +2.8 | +131.3 / +6.2 / +30.0 | +0.3 | 63 |
| MES 3m | 15 min | +131.4 | +2.1 | +110.1 / -0.8 / +22.1 | -8.3 | 71 |
| MES 3m | 18 min | +141.1 | +2.3 | +104.1 / +7.0 / +30.0 | +0.3 | 67 |
| MES 3m | 24 min | +125.6 | +2.2 | +102.8 / +6.2 / +16.6 | +0.3 | 56 |
| MES 3m | 65 % | +144.0 | +2.4 | +117.1 / -3.2 / +30.1 | -5.5 | 64 |
| MES 3m | 75 % | +115.1 | +2.1 | +122.1 / -20.3 / +13.3 | +6.0 | 55 |
| MES 3m | ATR ≥ 1.4x | +196.3 | +2.8 | +148.5 / +17.4 / +30.5 | +0.3 | 87 |
| MES 3m | ATR ≥ 1.6x | +143.7 | +2.8 | +114.5 / +15.7 / +13.6 | +0.7 | 46 |
| MGC 3m | Profit lock 75 % → +55 % (live rule) | +306.9 | +2.4 | +126.0 / +84.5 / +96.4 | -45.4 | 504 |
| MGC 3m | 70 % → +55 % | +358.1 | +2.6 | +157.0 / +137.3 / +63.8 | -32.4 | 574 |
| MGC 3m | 80 % → +55 % | +230.9 | +2.0 | +74.6 / +89.7 / +66.6 | -42.3 | 415 |
| MGC 3m | 75 % → +50 % | +234.4 | +1.9 | +98.0 / +60.8 / +75.6 | -53.6 | 495 |
| MGC 3m | 75 % → +60 % | +347.0 | +2.7 | +146.6 / +107.2 / +93.3 | -57.4 | 519 |

MGC 3m exits assumed in that replay: SL1 1.7 ATR (min 5, cap 7), TP1 1.7 ATR (cap 6), 80 % + BE + trail 1.7 (pre-v10.84 base; live is 50 % + trail 3.5 since 11/08 — the next Friday replay should use chop_sim EXIT (MGC,3)). TP cut fill: first candle at/after the time limit whose range reaches the cut target. z = Δ / (SD × √(setups changed)).

---

## Run 2026-11-05 17:37 ET (Thu)

Thursday run: Friday-only replays not run.

- **(A) keep 9 / 20.** Replay TP1 2.0: slow 14 Δ +184 (z 0.6, thirds -28 / +64 / +148), slow 16 Δ +178 (z 0.7, thirds +10 / +132 / +36). Last 4 weeks: 14 +34, 16 +15; last 5 days 14 -34, 16 -26.
- **(B) keep 2.0.** Real MES 3m setups (100 ended): 2.0 +100.9 > 1.75 +93.9 > 1.5 +68.7. Validation 98 / 100.
- **(C) MES 2m: ACT (provisional)** — 56 conf -0.26 vs 54 unconf -1.69. **MES 3m: keep watching.**
- **(D) keep watching on all MES charts** — LTF late MES 2m 13 / -25.4, MES 3m 18 / -23.2, MES 5m 9 / -4.7.

Live per chart 10/19 → 11/05: MES 2m 110 ended -105.7 · MES 3m 100 +31.7 · MES 5m 55 -18.6 · MGC 2m 138 -55.8 · MGC 3m 60 -34.2 · MGC 5m 44 -32.2 · MNQ 2m 146 -127.8 · MNQ 3m 100 -918.3 · MNQ 5m 49 +414.6.
