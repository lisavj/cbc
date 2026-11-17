# MES watch: chart EMA / TP1 / 5m confirmation / per-trigger / exit rules / late + room -- 2026-11-13 17:37 ET

Daily scheduled study. Newest run on top; history tables keep one line per run.

**STUDY SETTINGS STALE:** 3 MISMATCHes in claude/settings_sync_report.md (11/13 16:47 ET, Pine v10.96):
- mes3_ema_grid.py `LIVE` part 'tod' vs live MES 3m 100 % at TP1 all day (v10.95).
- chop_sim `EXIT[('MES',3)]` has the same 'tod' problem.
- chop_sim `EXIT[('MGC',3)]` 50 % + trail 3.5 vs live MGC 3m FLIP 0 % (v10.96).

The study ran anyway. Every replay was run twice: once as the task specifies (LIVE as stored, 'tod') and once with the current live exits (`dict(LIVE, part=1.0)`; for MGC 3m, FLIP 0 % = part 0, tr 0 with the `tr>0` trail guard). LIVE was not edited.

## History

### (A) Chart EMA — replay Jan 5 → now, live exits, Δ vs slow 20

TP1 in the replay was 2.0 until the 11/07 run and 1.75 from 11/09 (live v10.82+), so rows before 11/09 are not directly comparable. From 11/13 the first figures are 'tod' (as in the task). The current live exits (part 1.0) are in brackets.

| Run | TP1 | Slow 14: Δ / z / thirds | Slow 14 last 4 wk Δ | Slow 14 last 5 days Δ | Slow 16: Δ / z / thirds | Slow 16 last 4 wk Δ | Slow 16 last 5 days Δ | Last-4-wk beat count (of last 7 runs) 14 / 16 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-13 17:37 ET (Fri) | 1.75 | +197 / 0.7 / +6 · +37 · +154 [part 1.0: +129 / 0.4 / -23 · +67 · +85] | -14 [-31] | -52 [-50] | +226 / 0.9 / -1 · +79 · +148 [part 1.0: +141 / 0.6 / -16 · +49 · +107] | +58 [+27] | +6 [-10] | 4 of 6 / 5 of 6 | keep 9 / 20 |
| 2026-11-12 17:37 ET | 1.75 | +207 / 0.7 / +6 · +37 · +164 | +29 | -48 | +226 / 0.9 / -1 · +79 · +148 | +77 | +4 | 4 of 5 / 4 of 5 | keep 9 / 20 |
| 2026-11-12 09:44 ET | 1.75 | +214 / 0.8 / +6 · +37 · +171 | +34 | -42 | +222 / 0.9 / -1 · +79 · +144 | +72 | -0 | 3 of 4 / 3 of 4 | keep 9 / 20 |
| 2026-11-09 17:38 ET | 1.75 | +204 / 0.7 / +6 · +45 · +153 | +35 | -85 | +201 / 0.8 / -1 · +78 · +124 | +59 | -28 | 2 of 3 / 2 of 3 | keep 9 / 20 |
| 2026-11-07 09:44 ET (11/06 Fri run) | 2.0 | +135 / 0.5 / -19 · +55 · +99 | -5 | -78 | +153 / 0.6 / +12 · +124 · +18 | -3 | -50 | 1 of 2 / 1 of 2 | keep 9 / 20 |
| 2026-11-05 17:37 ET | 2.0 | +184 / 0.6 / -28 · +64 · +148 | +34 | -34 | +178 / 0.7 / +10 · +132 · +36 | +15 | -26 | 1 of 1 / 1 of 1 | keep 9 / 20 |

### (B) TP1 on the real MES 3m setups since 10/19

| Run | Ended | 1.5 | 1.75 | 2.0 | Δ 1.5 − 1.75 (halves) | Δ 2.0 − 1.75 (halves) | Verdict |
|---|---|---|---|---|---|---|---|
| 2026-11-13 17:37 ET — 'tod' model | 108 | +16.8 | +44.5 | +48.4 | -27.7 (-11.8 / -15.9) | +3.9 (-5.9 / +9.8) | keep 1.75 |
| 2026-11-13 17:37 ET — 100 % at TP1 (live v10.95) | 108 | -14.6 | +15.2 | +26.0 | -29.7 (-14.4 / -15.4) | +10.8 (-4.1 / +14.9) | keep 1.75 |
| 2026-11-12 17:37 ET | 107 | +33.1 | +60.8 | +64.7 | -27.7 (-11.2 / -16.5) | +3.9 (-6.3 / +10.2) | keep 1.75 |
| 2026-11-12 09:44 ET | 106 | +27.9 | +55.6 | +59.5 | -27.7 (-11.2 / -16.5) | +3.9 (-6.3 / +10.2) | keep 1.75 |
| 2026-11-09 17:38 ET | 105 | +46.6 | +74.3 | +78.2 | -27.7 (-10.7 / -17.0) | +3.9 (-6.8 / +10.7) | keep 1.75 |
| 2026-11-07 09:44 ET | 103 | +55.8 | +81.9 | +84.2 | -26.1 | +2.3 (-8.0 / +10.3) | keep 2.0 (was live) |

### (C) MES 5m confirmation — live since 10/19, avg pts per ended setup (confirmed vs unconfirmed)

**11/13 correction:** before this run, a MES 5m setup that never got a "Setup Ended" alert stayed "open" forever. There are 10 such setups, the first on 10/21 SHORT and 10/28 LONG. Because of that, almost every 2m / 3m setup after 10/28 counted as confirmed: that is why the earlier rows had "0 unconfirmed since 11/06". From this run, an unended 5m setup ends at the next MES 5m setup or at 16:00 ET, whichever comes first. Rows before 11/13 are therefore NOT comparable, and the earlier "confirmed better" reading on MES 3m was mostly this artefact.

| Run | MES 2m conf (n / avg) | MES 2m unconf (n / avg) | Δ | MES 3m conf (n / avg) | MES 3m unconf (n / avg) | Δ | Friday replay | Verdict 2m / 3m |
|---|---|---|---|---|---|---|---|---|
| 2026-11-13 17:37 ET (fixed rule) | 23 / +0.41 | 123 / -0.89 | +1.30 | 29 / -0.96 | 79 / -0.00 | -0.96 | 11/13: 2m Δ +0.01 z 0.0 (thirds + / - / -); 3m Δ +0.49 z 1.3 (thirds + / + / -) [part 1.0: +0.44 z 1.2, last third +0.02] | keep watching / keep watching |
| 2026-11-12 17:37 ET (old rule) | 88 / +0.10 | 54 / -1.69 | +1.79 | 77 / +0.09 | 30 / -0.63 | +0.72 | 11/06: 2m Δ -0.03 z -0.1; 3m Δ +0.16 z 0.4 | keep watching / keep watching |
| 2026-11-12 09:44 ET (old rule) | 84 / +0.30 | 54 / -1.69 | +1.99 | 76 / +0.03 | 30 / -0.63 | +0.66 | same | keep watching / keep watching |
| 2026-11-09 17:38 ET (old rule) | 66 / +0.14 | 54 / -1.69 | +1.83 | 75 / +0.28 | 30 / -0.63 | +0.91 | same | keep watching / keep watching |
| 2026-11-07 09:44 ET (old rule) | 62 / +0.13 | 54 / -1.69 | +1.82 | 73 / +0.39 | 30 / -0.63 | +1.02 | 2m Δ -0.03 z -0.1; 3m Δ +0.16 z 0.4 | keep watching / keep watching |
| 2026-11-05 17:37 ET (old rule) | 56 / -0.26 | 54 / -1.69 | +1.44 | 70 / +0.72 | 30 / -0.63 | +1.35 | none yet | ACT (provisional) / keep watching |

### (D) Per trigger — live since 10/19 (ended / net)

| Run | MES 2m LTF late | MES 3m LTF late | MES 5m LTF late | MES 3m bot set (Flip + LTF beyond EMA9) | MES 3m current bot set (v10.88, + LTF not beyond) | MES 3m everything else | Friday replay (LTF late window 0 vs 1) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 2026-11-13 17:37 ET (Fri) | 19 / -32.0 | 20 / -21.1 | 15 / -7.5 | 32 / +9.4 (avg +0.29) | 64 / +2.5 (avg +0.04) | 76 / -37.4 | 11/13: 2m Δ -42 z -0.6 · 3m Δ -71 z -0.7 [part 1.0 -58] · 5m Δ -74 z -1.2 | keep watching |
| 2026-11-12 17:37 ET | 18 / -24.0 | 20 / -21.1 | 15 / -7.5 | 31 / +25.7 (avg +0.83) | 63 / +18.8 (avg +0.30) | 76 / -37.4 | 11/06: 2m Δ -44 z -1.0 · 3m Δ -2 z 0.0 · 5m Δ -74 z -1.7 | keep watching |
| 2026-11-12 09:44 ET | 18 / -24.0 | 20 / -21.1 | 15 / -7.5 | 31 / +25.7 (avg +0.83) | — | 75 / -42.6 | same | keep watching |
| 2026-11-09 17:38 ET | 15 / -27.0 | 20 / -21.1 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | — | 75 / -42.6 | same | keep watching |
| 2026-11-07 09:44 ET (11/06 Fri run) | 14 / -33.4 | 19 / -32.5 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | — | 73 / -35.0 | 2m Δ -44 z -1.0 · 3m Δ -2 z 0.0 · 5m Δ -74 z -1.7 | keep watching |
| 2026-11-05 17:37 ET | 13 / -25.4 | 18 / -23.2 | 9 / -4.7 | 30 / +44.4 (avg +1.48) | — | 70 / -12.8 | not run | keep watching |

### (E) Exit rules (v10.79) — live hits and Friday replay

| Run | MES 3m TP cut live hits: rule vs CBC | MGC 3m profit lock live hits: rule vs CBC | Replay MES 3m TP cut (Δ / z / thirds / last 4 wk) | Replay MGC 3m lock (Δ / z / thirds / last 4 wk) | Verdict |
|---|---|---|---|---|---|
| 2026-11-13 17:37 ET (Fri) | 1 hit: +11.44 vs +5.25 (+6.19) | 6 hits, 2 comparable: +5.10 vs -3.00 (+8.10) | 11/13 (new script): 'tod' +52 / 0.9 / + · + · + / -13; live 100 % +17 / 0.3 / + · + · + / -27 | 11/13: on 50 % / 3.5 +91 / 0.4 / + · + · - / -34; on live FLIP 0 % +28 / 0.1 / + · + · - / -35 | keep watching (MES 1 / MGC 2 of 15); replay edge mostly gone on the current exits |
| 2026-11-12 17:37 ET | 1 hit (11/12 10:30): +11.44 vs +5.25 (+6.19) | 5 hits, 2 comparable: +5.10 vs -3.00 (+8.10; halves +1.20 / +6.90) | 11/06: +168 / 2.8 / all + / +0.3 | 11/06: +307 / 2.4 / all + / -45 | keep watching |
| 2026-11-12 09:44 ET | 0 | 5 hits, 2 comparable: +5.10 vs -3.00 (+8.10) | same | same | keep watching |
| 2026-11-09 17:38 ET | 0 | 1: +3.2 vs +2.0 (+1.2) | same | same | keep watching |
| 2026-11-07 09:44 ET (11/06 Fri run) | 0 (no Exit Rule alerts yet) | 0 | +168 / 2.8 / +131 · +6 · +30 / +0.3 | +307 / 2.4 / +126 · +85 · +96 / -45 | keep watching |

### (F) Late trigger + room < 0.5 x TP1 — live (Room line exists from 10/29), ended / net / avg

| Run | MES 3m | MES 2m | MES 5m | MES 3m bot windows | Verdict |
|---|---|---|---|---|---|
| 2026-11-13 17:37 ET | 8 / +7.2 / +0.90 | 6 / -24.2 / -4.03 | 5 / +13.5 / +2.70 | 8 / +7.2 / +0.90 | too few yet (all charts) |
| 2026-11-12 17:37 ET | 8 / +7.2 / +0.90 | 5 / -16.2 / -3.23 | 5 / +13.5 / +2.70 | 8 / +7.2 / +0.90 | too few yet (all charts) |
| 2026-11-12 09:44 ET | 8 / +7.2 / +0.90 | 5 / -16.2 / -3.23 | 5 / +13.5 / +2.70 | 8 / +7.2 / +0.90 | too few yet |
| 2026-11-09 17:38 ET | 8 / +7.2 / +0.90 | 3 / -8.4 / -2.80 | 2 / +7.0 / +3.51 | 8 / +7.2 / +0.90 | too few yet |

---

## Run 2026-11-13 17:37 ET (Fri)

Friday run, so all the replays were run: (A), the (D) per-trigger replay and late-window test, the (C) replay and the (E) replay. Live alerts are through 11/13 (last MES setup 15:48). BarFeed MES 3m is current to 16:57. Replay data: MES 3m 102 745 candles from 01/05, MES 2m 82 259 from 06/01, MES 5m 61 647, MGC 3m 102 525. There are no gaps.

**Data warnings this run**

- **MES 5m: no alert of any kind since 11/12 18:40 ET** (0 alerts on 11/13; on a normal day there are 100-150). BarFeed MES 5m is current, so the CBC alert on the MES 5m chart has probably stopped or been deleted. Check it in TradingView. Live (C) 5m confirmation cannot work without it.
- **MES 3m alerts are still thin.** There were 79 MES 3m alerts on 11/13, the last at 14:24 ET, and 1 setup (08:33 LONG, -16.32). In the setup counts since 11/06 (11/06 4, 11/08 2, 11/12 2, 11/13 1), MES 3m has been near-silent since 11/08.
- **MGC 3m setups are flowing again:** 3 on 11/13 (FLIP 0 % exits, +7.4).
- **(C) live rule fix:** see the note in the (C) history. Unended 5m setups no longer count as open forever.
- **(C) and (E) replays rebuilt.** No (C) / (E) replay script existed in the project, so they were rebuilt today. The (E) rebuild with the old settings (TP1 2.0, 'tod') gives +114, z 1.7 vs +168, z 2.8 on 11/06, so compare variants within this run, not against 11/06 totals.
- **MES 2m MTF gate in the replay:** `late_study.LCase` (via `mes3_ema_grid.MCase`) hard-sets `d['M']=False`, so on that path the MES 2m 1H MTF gate is inert. (D) used `mes3_watch_a.MCase`, which computes the MTF flag.
- **Validation:** the TP1 replay with 100 % at TP1 reproduces the actual MES 3m results almost exactly (-28.5 vs -28.0, 107 / 108 agree), which confirms that the live chart now closes 100 % at TP1. The 'tod' model gives +1.1.
- Duplicates: the stored alerts are still not cleaned. 1 504 near copies were dropped, and 6 setups had two Setup Ended results.

### Verdicts

- **(A) EMA: keep 9 / 20, keep watching.**
  - TP1 1.75 'tod': slow 14 Δ +197 (z 0.7, thirds +6 / +37 / +154); slow 16 Δ +226 (z 0.9, thirds -1 / +79 / +148).
  - Current live exits (part 1.0): slow 14 +129 (z 0.4), slow 16 +141 (z 0.6), both with the first third negative.
  - Last 4 wk: slow 14 -14 (it now loses), slow 16 +58. Slow 16 has beaten 20 over the last 4 weeks in 5 of the last 6 runs, which meets the run-count condition, but z is far below 2. Slow 14 has 4 of 6.
  - Closest variant: slow 16 with TP1 1.5 is +221, z 1.0, all thirds positive.
- **(B) TP1: keep 1.75.**
  - 108 real setups.
  - 'tod' model: 2.0 +48.4 ≥ 1.75 +44.5 > 1.5 +16.8.
  - Live 100 % model: 2.0 +26.0 > 1.75 +15.2 > 1.5 -14.6.
  - 2.0 − 1.75 = +3.9 / +10.8, but the first half is negative in both models (-5.9 / -4.1) and the middle third is negative too, so "switch back to 2.0" fails.
  - 1.5 − 1.75 = -27.7 / -29.7, negative in both halves.
- **(C) keep watching (2m and 3m), with the corrected live rule.**
  - MES 2m: 23 confirmed +0.41 vs 123 unconfirmed -0.89 (+1.30 / setup). Both halves agree (h1 -0.65 vs -1.72, h2 +0.98 vs +0.05), but there are only 23 ended (need 40), and the Friday replay fails (Δ +0.01, z 0.0).
  - MES 3m: confirmed is now WORSE, 29 at -0.96 vs 79 at -0.00. The replay improved (Δ +0.49, z 1.3), but its last third is negative.
  - With MES 5m alerts missing since 11/12, no new live confirmations can be counted.
  - Acting would need a new CBC filter or dashboard flag (not built).
- **(D) keep watching on every MES chart.** No trigger has 40 ended setups.
  - LTF Pierce LATE: MES 2m 19 / -32.0 (avg -1.68, halves -12.6 / -19.4), MES 3m 20 / -21.1 (avg -1.05, halves -34.5 / +13.4), MES 5m 15 / -7.5.
  - The Friday replay disagrees with a switch-off. Window 0 is worse than window 1 on every chart: 2m -42 (z -0.6), 3m -71 (z -0.7; part 1.0 -58), 5m -74 (z -1.2). LTF20 late is net positive in the replay on all three charts.
  - MES 3m bot set (Flip + LTF beyond): 32 / +9.4 (avg +0.29; today's 08:33 LTF-beyond LONG was -16.32).
  - Current v10.88 three-trigger set: 64 / +2.5 (avg +0.04). LTF Pierce not beyond on MES 3m: 32 / -6.9 (avg -0.22, halves +3.2 / -10.1).
  - No ADD candidate.
  - In the replay, Flip is the largest drag on MES 3m (-227 'tod' / -229 part 1.0; thirds -98 / -189 / +60).
- **(E) keep watching.**
  - Live: MES 3m TP cut 1 hit (+6.19 vs CBC); MGC 3m profit lock 6 hits, 2 comparable (+8.10). Both are far from 15.
  - The replay edge has mostly gone on the current live exits:
    - MES 3m TP cut on 100 % at TP1: +17, z 0.3, last 4 wk -27. The neighbours range from +0 to +43, all with z < 1.
    - MGC 3m lock on FLIP 0 %: +28, z 0.1, last third -45, last 4 wk -35. Every neighbour's last third is negative.
  - If live hits confirm this, the likely outcome is DROP, so be strict about "Bot: flatten when an exit rule closes the trade".
- **(F) too few yet on every chart.** late & room < 0.5:
  - MES 3m 8 / +7.2 (avg +0.90)
  - MES 2m 6 / -24.2 (avg -4.03; its neighbours < 0.3: 5 / -30.1, < 0.75: 8 / -36.5, the most consistent negative so far)
  - MES 5m 5 / +13.5
  - MES 3m bot windows 8 / +7.2
  - New today: MES 2m 11/13 14:04 LONG, late LTF, room 0.16 (EMA200), -8.00.

## Live (steps 1, 2, 4, 6b, 6c)

### Live per chart (10/19 → 11/13 15:48)

| Chart | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| MES 2m | 159 | 146 | 44% | -99.7 | -0.68 | -116.9 / +17.3 |
| MES 3m | 121 | 108 | 46% | -28.0 | -0.26 | -31.1 / +3.2 |
| MES 5m | 81 | 71 | 52% | -18.3 | -0.26 | -26.5 / +8.1 |
| MGC 2m | 227 | 208 | 46% | -97.5 | -0.47 | -53.7 / -43.8 |
| MGC 3m | 90 | 79 | 47% | +10.0 | +0.13 | -6.0 / +16.0 |
| MGC 5m | 75 | 69 | 45% | -37.2 | -0.54 | -3.6 / -33.6 |
| MNQ 2m | 222 | 206 | 40% | -438.7 | -2.13 | -312.1 / -126.7 |
| MNQ 3m | 123 | 114 | 31% | -1025.1 | -8.99 | -541.6 / -483.4 |
| MNQ 5m | 78 | 66 | 53% | +566.1 | +8.58 | +273.6 / +292.5 |
| MES 3m 10/19–11/04 (9 / 20) | 107 | 95 | 47% | +6.7 | +0.07 | -49.0 / +55.7 |
| MES 3m 11/05 (7 / 14 build) | 5 | 5 | 60% | +24.9 | +4.99 | -1.7 / +26.6 |
| MES 3m 11/06–11/07 (9 / 20, TP1 2.0) | 4 | 3 | 0% | -22.2 | -7.42 | -9.2 / -13.0 |
| MES 3m from 11/08 (TP1 1.75, v10.82+) | 5 | 5 | 40% | -37.4 | -7.48 | -7.6 / -29.8 |
| MES 3m from 11/13 (v10.95+, 100 % at TP1 all day) | 1 | 1 | 0% | -16.3 | -16.32 | +0.0 / -16.3 |
| MGC 3m before 11/08 | 77 | 67 | 42% | -34.2 | -0.51 | -6.1 / -28.1 |
| MGC 3m 11/08–11/12 (50 % + trail 3.5; partly old exits) | 10 | 9 | 78% | +36.8 | +4.09 | +39.5 / -2.7 |
| MGC 3m from 11/13 (v10.96 FLIP 0 %) | 3 | 3 | 67% | +7.4 | +2.48 | +2.1 / +5.4 |

Matched: 1176 Trade Setup alerts, 1067 ended; 96 Setup Ended alerts without a matching Trade Setup (not counted). Near-duplicate alerts dropped: 1504; setups with two Setup Ended results: 6 (0.5×(TP1) version kept).

### (D) Live per trigger — MES 2m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 40 | 37 | 51% | -6.2 | -0.17 | -15.2 / +9.0 |
| LTF Pierce beyond EMA9 | 42 | 37 | 51% | +1.8 | +0.05 | -61.8 / +63.5 |
| LTF Pierce not beyond | 32 | 29 | 34% | -42.4 | -1.46 | -14.5 / -27.9 |
| LTF Pierce LATE | 19 | 19 | 37% | -32.0 | -1.68 | -12.6 / -19.4 |
| HTF EMA9 Pierce | 8 | 8 | 50% | -3.1 | -0.39 | +2.2 / -5.3 |
| HTF EMA9 late | 3 | 2 | 0% | -6.1 | -3.06 | +0.0 / -6.1 |
| HTF EMA20 Pierce | 10 | 10 | 30% | -7.8 | -0.78 | +4.8 / -12.5 |
| HTF EMA20 late | 3 | 2 | 50% | -0.8 | -0.38 | +2.0 / -2.8 |
| HTF Pullback | 2 | 2 | 50% | -3.2 | -1.60 | -8.0 / +4.8 |

### (D) Live per trigger — MES 3m (first listed trigger)

| Trigger | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|
| HTF CBC Flip | 18 | 16 | 56% | +23.0 | +1.44 | +9.8 / +13.2 |
| LTF Pierce beyond EMA9 | 19 | 16 | 56% | -13.6 | -0.85 | -18.9 / +5.4 |
| LTF Pierce not beyond | 35 | 32 | 47% | -6.9 | -0.22 | +3.2 / -10.1 |
| LTF Pierce LATE | 22 | 20 | 40% | -21.1 | -1.05 | -34.5 / +13.4 |
| HTF EMA9 Pierce | 13 | 12 | 50% | +10.6 | +0.89 | +5.2 / +5.4 |
| HTF EMA9 late | 2 | 2 | 0% | -5.9 | -2.94 | -1.2 / -4.6 |
| HTF EMA20 Pierce | 7 | 5 | 20% | -5.8 | -1.17 | -8.8 / +3.0 |
| HTF EMA20 late | 3 | 3 | 67% | +0.8 | +0.26 | -5.2 / +6.0 |
| HTF Pullback | 2 | 2 | 0% | -9.1 | -4.54 | -5.6 / -3.5 |
| Bot set (Flip + LTF Pierce beyond EMA9; task definition) | 37 | 32 | 56% | +9.4 | +0.29 | -1.0 / +10.5 |
| **Current bot set since v10.88 (+ LTF Pierce not beyond)** | 72 | 64 | 52% | +2.5 | +0.04 | -7.0 / +9.5 |
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
| HTF CBC Flip | 57 / -36.3 | 8 / +5.7 | 16 / -1.1 | 64 / -21.1 | 31 / -201.5 | 10 / -95.5 |
| LTF Pierce beyond EMA9 | 33 / -17.7 | 17 / -6.5 | 12 / -9.9 | 23 / -279.0 | 18 / -270.5 | 12 / +61.8 |
| LTF Pierce not beyond | 42 / +20.1 | 18 / +4.0 | 9 / +18.1 | 46 / +101.3 | 28 / -506.3 | 19 / +384.4 |
| LTF Pierce LATE | 32 / -43.6 | 11 / +17.3 | 13 / -68.2 | 22 / -238.9 | 11 / -23.1 | 5 / +64.4 |
| HTF EMA9 Pierce | 16 / +16.2 | 9 / +5.8 | 8 / +32.3 | 23 / +32.7 | 7 / +117.5 | 10 / +73.6 |
| HTF EMA9 late | 9 / +0.2 | 4 / -1.6 | 3 / -13.9 | 3 / +90.8 | 3 / -25.3 | 3 / -20.3 |
| HTF EMA20 Pierce | 14 / -22.1 | 11 / -7.7 | 5 / -2.1 | 19 / -45.2 | 15 / -86.0 | 6 / +65.7 |
| HTF EMA20 late | 4 / -9.4 | — | 1 / +4.8 | 3 / -21.9 | — | — |
| HTF Pullback | 1 / -5.0 | 1 / -6.9 | 1 / -2.7 | 3 / -57.5 | — | 1 / +32.0 |
| LTF EMA20 Touch | — | — | 1 / +5.6 | — | 1 / -30.0 | — |

### (C) Live MES 5m confirmation

| Chart / window | Group | Setups | Ended | Win % | Net | Avg | Halves |
|---|---|---|---|---|---|---|---|
| MES 2m since 10/19 | confirmed | 30 | 23 | 52% | +9.4 | +0.41 | +16.1 / -6.7 |
| MES 2m since 10/19 | unconfirmed | 129 | 123 | 43% | -109.1 | -0.89 | -111.0 / +1.9 |
| MES 2m since 11/06 | confirmed | 6 | 5 | 20% | -17.5 | -3.50 | -13.0 / -4.5 |
| MES 2m since 11/06 | unconfirmed | 31 | 29 | 59% | +26.7 | +0.92 | +45.3 / -18.5 |
| MES 3m since 10/19 | confirmed | 32 | 29 | 45% | -27.8 | -0.96 | -7.1 / -20.7 |
| MES 3m since 10/19 | unconfirmed | 89 | 79 | 47% | -0.2 | -0.00 | -46.4 / +46.3 |
| MES 3m since 11/06 | confirmed | 2 | 2 | 50% | +1.8 | +0.88 | -3.5 / +5.2 |
| MES 3m since 11/06 | unconfirmed | 7 | 6 | 17% | -61.4 | -10.23 | -7.4 / -54.0 |

MES 2m common date halves (split 10/28 14:00): conf h1 8 / -5.2 (avg -0.65) · conf h2 15 / +14.6 (avg +0.98) · unconf h1 65 / -111.7 (avg -1.72) · unconf h2 58 / +2.6 (avg +0.05)
MES 3m common date halves (split 10/27 19:39): conf h1 13 / -2.1 (avg -0.16) · conf h2 16 / -25.7 (avg -1.60) · unconf h1 41 / -29.0 (avg -0.71) · unconf h2 38 / +28.9 (avg +0.76)

### (E) Exit Rule alerts (v10.79+)

Exit Rule alerts found (after dedupe): 16 (MES 3m hit 1, MGC 3m armed 9, MGC 3m hit 6); first 11/09 10:57.

| Chart | Rule | Time | Dir | Rule result | CBC result (Setup Ended) | Rule − CBC |
|---|---|---|---|---|---|---|
| MGC 3m | Profit lock | 11/09 11:00 | LONG | +3.20 | +2.00 | +1.20 |
| MGC 3m | Profit lock | 11/09 23:57 | SHORT | +0.90 | no matching setup | — |
| MGC 3m | Profit lock | 11/10 02:21 | SHORT | +3.02 | no matching setup | — |
| MGC 3m | Profit lock | 11/10 23:09 | LONG | +1.70 | no matching setup | — |
| MGC 3m | Profit lock | 11/11 06:21 | LONG | +1.90 | -5.00 | +6.90 |
| MES 3m | TP cut | 11/12 10:30 | LONG | +11.44 | +5.25 | +6.19 |
| MGC 3m | Profit lock | 11/13 00:12 | LONG | +2.49 | no matching setup | — |

| Chart (period) | Hits with ended setup | Sum rule | Sum CBC | Rule − CBC | Halves (rule − CBC) |
|---|---|---|---|---|---|
| MES 3m | 1 | +11.44 | +5.25 | +6.19 | +0.00 / +6.19 |
| MGC 3m before 11/08 | 0 | +0.00 | +0.00 | +0.00 | +0.00 / +0.00 |
| MGC 3m from 11/08 (50 % + trail 3.5; FLIP 0 % from 11/13) | 2 | +5.10 | -3.00 | +8.10 | +1.20 / +6.90 |

### (F) Late trigger × room (first trigger late; room = x TP1 from the "Room:" line)

#### MES 2m — 159 setups (146 ended), 83 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/05 21:38

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 6 | 6 | 17% | -24.2 | -4.03 | -0.4 / -23.8 |
| late & room ≥ 0.5 | 8 | 7 | 43% | +1.8 | +0.26 | -12.6 / +14.4 |
| not late & room < 0.5 | 28 | 23 | 74% | +70.7 | +3.07 | +21.4 / +49.3 |
| not late & room ≥ 0.5 | 34 | 33 | 48% | -21.4 | -0.65 | +17.4 / -38.8 |
| late & room < 0.3 | 5 | 5 | 0% | -30.1 | -6.02 | -6.3 / -23.8 |
| late & room < 0.75 | 9 | 8 | 12% | -36.5 | -4.56 | -12.8 / -23.8 |
| (no Room line) late | 11 | 10 | 44% | -16.5 | -1.65 | -16.5 / +0.0 |
| (no Room line) not late | 72 | 67 | 34% | -110.1 | -1.64 | -110.1 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): +24.2 pts on 6 ended setups — too few yet.

#### MES 3m — 121 setups (108 ended), 79 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/03 11:27

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 8 | 8 | 62% | +7.2 | +0.90 | +11.0 / -3.8 |
| late & room ≥ 0.5 | 2 | 2 | 50% | +6.2 | +3.12 | +6.2 / +0.0 |
| not late & room < 0.5 | 18 | 16 | 56% | -6.2 | -0.39 | +17.6 / -23.8 |
| not late & room ≥ 0.5 | 14 | 12 | 58% | +31.5 | +2.62 | +26.0 / +5.5 |
| late & room < 0.3 | 5 | 5 | 80% | +19.5 | +3.89 | +14.1 / +5.4 |
| late & room < 0.75 | 9 | 9 | 56% | -2.4 | -0.26 | +1.5 / -3.8 |
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

#### MES 3m bot windows — 91 setups (82 ended), 57 without a Room line (kept out of the room cells); halves = date split of the Room-line setups at 11/03 04:39

| Cell | Setups | Ended | Win % | Net | Avg | Halves (date split) |
|---|---|---|---|---|---|---|
| late & room < 0.5 | 8 | 8 | 62% | +7.2 | +0.90 | +5.0 / +2.2 |
| late & room ≥ 0.5 | 2 | 2 | 50% | +6.2 | +3.12 | +15.8 / -9.6 |
| not late & room < 0.5 | 12 | 10 | 70% | +21.0 | +2.10 | +8.1 / +12.9 |
| not late & room ≥ 0.5 | 12 | 11 | 64% | +38.5 | +3.50 | +26.0 / +12.5 |
| late & room < 0.3 | 5 | 5 | 80% | +19.5 | +3.89 | +8.1 / +11.4 |
| late & room < 0.75 | 9 | 9 | 56% | -2.4 | -0.26 | +5.0 / -7.4 |
| (no Room line) late | 13 | 12 | 33% | -23.1 | -1.92 | -23.1 / +0.0 |
| (no Room line) not late | 44 | 39 | 46% | -1.9 | -0.05 | -1.9 / +0.0 |

Combo skip effect (minus the late & room < 0.5 net): -7.2 pts on 8 ended setups — too few yet.

#### Late & room < 0.5 setups, last 5 trading days (11/09, 11/10, 11/11, 11/12, 11/13)

| Chart | Time | Dir | First trigger | Room | Room x TP1 | VWAP ext | Result |
|---|---|---|---|---|---|---|---|
| MES 3m | 11/08 18:48 | SHORT | LTF EMA20 Pierce (late, 1 bars after) | AS OR-H 7400.50 at 1.5 pts | 0.11 | +0.2 ATR | +11.39 |
| MES 5m | 11/09 20:40 | LONG | LTF EMA20 Pierce (late, 1 bars after) | OB- 7585.75-7580.50 at 0 pts | 0.00 | +1.2 ATR | open |
| MES 5m | 11/11 03:55 | LONG | LTF EMA20 Pierce (late, 1 bars after) | HTF Piv-H 7595.50 at 1 pts | 0.17 | +4.0 ATR | +4.80 |
| MES 2m | 11/11 07:02 | LONG | LTF EMA20 Pierce (late, 1 bars after) | HTF EQH 7613.50 at 0.5 pts | 0.12 | +11.5 ATR | -5.00 |
| MES 2m | 11/11 14:44 | LONG | HTF EMA20 Pierce (late) | R2 7651.00 at 0.33 pts | 0.06 | +8.4 ATR | -2.75 |
| MES 5m | 11/12 05:55 | LONG | LTF EMA20 Pierce (late, 1 bars after) | LTF Piv-L 7615.00 at 0.25 pts | 0.04 | +0.9 ATR | -2.75 |
| MES 5m | 11/12 06:15 | SHORT | LTF EMA20 Pierce (late, 1 bars after) | AS OR-H 7612.50 at 0.25 pts | 0.05 | -0.3 ATR | +4.43 |
| MES 2m | 11/13 14:04 | LONG | LTF EMA20 Pierce (late, 1 bars after) | EMA200 7576.25 at 0.96 pts | 0.16 | -0.5 ATR | -8.00 |

First MES setup with a Room line: 10/29 20:36.


### (B) TP1 on the real MES 3m setups — exit model task text: 80 % + BE + trail 1.7 inside 06:00-16:00 / 18:00-22:30, 100 % outside (10/19 → 11/13, 108 ended setups with bars + SL1; 0 skipped: no bar / no SL1)

| TP1 | Net | Win % | Avg | Halves | Thirds |
|---|---|---|---|---|---|
| 1.50 ATR | +16.8 | 48% | +0.16 | -9.7 / +26.5 | -26.9 / +2.5 / +41.1 |
| 1.75 ATR (live) | +44.5 | 46% | +0.41 | +2.0 / +42.5 | -15.6 / -5.8 / +65.9 |
| 2.00 ATR | +48.4 | 43% | +0.45 | -3.9 / +52.3 | -14.1 / -24.0 / +86.5 |
| Δ 1.5 − 1.75 | -27.7 | | | -11.8 / -15.9 | -11.3 / +8.3 / -24.7 |
| Δ 2.0 − 1.75 | +3.9 | | | -5.9 / +9.8 | +1.4 / -18.2 / +20.6 |

Validation (own SL1 + own TP1 from the Trade Setup alert): replay +1.1 vs actual -28.0; win/loss agreement 107 / 108 (99%).


### (B) TP1 on the real MES 3m setups — exit model v10.95+ live: 100 % at TP1 all day (10/19 → 11/13, 108 ended setups with bars + SL1; 0 skipped: no bar / no SL1)

| TP1 | Net | Win % | Avg | Halves | Thirds |
|---|---|---|---|---|---|
| 1.50 ATR | -14.6 | 48% | -0.13 | -9.3 / -5.2 | -21.0 / -4.2 / +10.7 |
| 1.75 ATR (live) | +15.2 | 46% | +0.14 | +5.0 / +10.1 | -8.3 / -12.3 / +35.7 |
| 2.00 ATR | +26.0 | 43% | +0.24 | +0.9 / +25.1 | -5.9 / -28.8 / +60.7 |
| Δ 1.5 − 1.75 | -29.7 | | | -14.4 / -15.4 | -12.8 / +8.0 / -25.0 |
| Δ 2.0 − 1.75 | +10.8 | | | -4.1 / +14.9 | +2.4 / -16.5 / +25.0 |

Validation (own SL1 + own TP1 from the Trade Setup alert): replay -28.5 vs actual -28.0; win/loss agreement 107 / 108 (99%).


### (A) Replay — slow chart EMA 20 vs 14 vs 16 (mes3_watch_a.py; LIVE 'tod', dict(LIVE, tp=1.5), dict(LIVE, part=1.0))

Data: 102745 candles, 01/05 → 11/13. Thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/13. Last 4 weeks from 10/16; last 5 trading days: 11/08, 11/09, 11/10, 11/11, 11/12 (Globex sessions).

#### Live exits, LIVE as stored, TP1 1.75, part tod

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1738 | 49% | +9 | +0.01 | +0 | +0.0 | +0 / +0 / +0 | baseline | +173.4 | +28.8 | Flip 319 / -227 (+0) · LTF20 986 / +211 (+0) · HTF9 269 / -66 (+0) · HTF20 164 / +91 (+0) |
| 7 / 14 | 1976 | 50% | +206 | +0.10 | +197 | +0.7 | +6 / +37 / +154 | noise | -14.3 | -52.4 | Flip 333 / -169 (+6) · LTF20 1228 / +354 (-17) · HTF9 260 / -66 (-5) · HTF20 155 / +87 (+2) |
| 7 / 16 | 1884 | 50% | +235 | +0.12 | +226 | +0.9 | -1 / +79 / +148 | noise | +57.8 | +6.4 | Flip 330 / -192 (+6) · LTF20 1122 / +406 (+37) · HTF9 271 / -73 (+5) · HTF20 161 / +95 (+11) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)

#### Live exits, dict(LIVE, tp=1.5)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1771 | 53% | +133 | +0.08 | +0 | +0.0 | +0 / +0 / +0 | baseline | +151.2 | +26.2 | Flip 319 / -207 (+0) · LTF20 1002 / +318 (+0) · HTF9 278 / -40 (+0) · HTF20 172 / +62 (+0) |
| 7 / 14 | 2009 | 54% | +225 | +0.11 | +92 | +0.3 | +92 / -40 / +39 | noise | -52.1 | -53.0 | Flip 333 / -136 (+5) · LTF20 1247 / +308 (-56) · HTF9 266 / -41 (-4) · HTF20 163 / +94 (+2) |
| 7 / 16 | 1919 | 55% | +355 | +0.18 | +221 | +1.0 | +115 / +38 / +68 | noise | +27.2 | +4.1 | Flip 330 / -156 (+5) · LTF20 1143 / +469 (+6) · HTF9 279 / -38 (+6) · HTF20 167 / +79 (+9) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)

#### Live exits, dict(LIVE, part=1.0) (current live v10.95)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1799 | 49% | +60 | +0.03 | +0 | +0.0 | +0 / +0 / +0 | baseline | +149.2 | +25.9 | Flip 319 / -229 (+0) · LTF20 1042 / +245 (+0) · HTF9 274 / -48 (+0) · HTF20 164 / +92 (+0) |
| 7 / 14 | 2140 | 50% | +189 | +0.09 | +129 | +0.4 | -23 / +67 / +85 | noise | -30.7 | -50.4 | Flip 333 / -162 (+6) · LTF20 1389 / +307 (-33) · HTF9 264 / -47 (-8) · HTF20 154 / +92 (+4) |
| 7 / 16 | 1998 | 50% | +201 | +0.10 | +141 | +0.6 | -16 / +49 / +107 | noise | +27.4 | -9.6 | Flip 330 / -188 (+6) · LTF20 1237 / +351 (+7) · HTF9 271 / -66 (+2) · HTF20 160 / +104 (+12) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)

#### Live exits, dict(LIVE, tp=1.5, part=1.0)

| Chart EMA | Setups | Win % | Net | Avg | Δ vs 20 | z | Δ by third | Verdict | Last 4 wk Δ | Last 5 days Δ | By trigger setups / net (Δ last 4 wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 / 20 (live) | 1836 | 53% | +146 | +0.08 | +0 | +0.0 | +0 / +0 / +0 | baseline | +121.4 | +23.3 | Flip 319 / -210 (+0) · LTF20 1063 / +330 (+0) · HTF9 282 / -35 (+0) · HTF20 172 / +61 (+0) |
| 7 / 14 | 2178 | 54% | +226 | +0.10 | +79 | +0.3 | +83 / +18 / -22 | noise | -64.9 | -42.4 | Flip 333 / -130 (+5) · LTF20 1413 / +300 (-68) · HTF9 270 / -43 (-6) · HTF20 162 / +99 (+3) |
| 7 / 16 | 2037 | 55% | +361 | +0.18 | +215 | +0.9 | +133 / +42 / +39 | noise | +1.9 | -3.1 | Flip 330 / -152 (+5) · LTF20 1262 / +484 (-18) · HTF9 279 / -59 (+4) · HTF20 166 / +88 (+10) |

(9 / 20 row: "Last 4 wk" and "Last 5 days" columns show its own net, not a Δ.)


### (D) Replay per trigger + LTF late-window test (chop_sim / mes3_watch_a.MCase engine)

#### MES 3m 9/20 + range gate, LIVE as stored (TP1 1.75, part tod) — 102745 candles 01/05 → 11/13; thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/13

| Trigger (window 1) | Setups | Win % | Net | Avg | Thirds |
|---|---|---|---|---|---|
| Flip | 319 | 54% | -226.8 | -0.71 | -98 / -189 / +60 |
| LTF20 on-candle | 806 | 47% | +135.4 | +0.17 | +227 / -218 / +127 |
| LTF20 late | 180 | 54% | +75.5 | +0.42 | +34 / -3 / +45 |
| HTF EMA9 (incl late) | 269 | 46% | -66.2 | -0.25 | +33 / -49 / -51 |
| HTF EMA20 (incl late) | 164 | 50% | +91.1 | +0.56 | +44 / +19 / +28 |
| All | 1738 | 49% | +9.1 | +0.01 | +240 / -440 / +209 |

| LTF late window | Setups | Net | Δ vs 1 | z | Δ by third | Verdict | LTF20 late setups / net |
|---|---|---|---|---|---|---|---|
| 0 | 1637 | -62.3 | -71.4 | -0.7 | -10 / +4 / -65 | worse | 0 / +0.0 |
| 1 (current) | 1738 | +9.1 | +0.0 | +0.0 | +0 / +0 / +0 | baseline | 180 / +75.5 |
| 2 | 1785 | -18.7 | -27.7 | -0.4 | +7 / -43 / +8 | worse | 247 / +60.2 |
| 3 | 1795 | -30.0 | -39.0 | -0.5 | +19 / -48 / -10 | worse | 263 / +60.6 |

#### MES 3m 9/20 + range gate, dict(LIVE, part=1.0) (current live) — 102745 candles 01/05 → 11/13; thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/13

| Trigger (window 1) | Setups | Win % | Net | Avg | Thirds |
|---|---|---|---|---|---|
| Flip | 319 | 54% | -229.0 | -0.72 | -89 / -189 / +50 |
| LTF20 on-candle | 859 | 48% | +165.0 | +0.19 | +232 / -189 / +122 |
| LTF20 late | 183 | 53% | +79.5 | +0.43 | +42 / +3 / +35 |
| HTF EMA9 (incl late) | 274 | 46% | -47.6 | -0.17 | +34 / -43 / -39 |
| HTF EMA20 (incl late) | 164 | 50% | +92.2 | +0.56 | +47 / +10 / +35 |
| All | 1799 | 49% | +60.1 | +0.03 | +266 / -408 / +202 |

| LTF late window | Setups | Net | Δ vs 1 | z | Δ by third | Verdict | LTF20 late setups / net |
|---|---|---|---|---|---|---|---|
| 0 | 1690 | +2.0 | -58.2 | -0.6 | -25 / +14 / -47 | worse | 0 / +0.0 |
| 1 (current) | 1799 | +60.1 | +0.0 | +0.0 | +0 / +0 / +0 | baseline | 183 / +79.5 |
| 2 | 1847 | +43.2 | -17.0 | -0.3 | +12 / -43 / +14 | worse | 249 / +68.4 |
| 3 | 1857 | +15.9 | -44.3 | -0.6 | +11 / -50 / -5 | worse | 265 / +55.3 |

#### MES 2m slow 14 + 1H MTF gate, base exits (late-away 1 pt) — 82259 candles 06/01 → 11/13; thirds 06/01–07/26 / 07/26–09/19 / 09/19–11/13

| Trigger (window 1) | Setups | Win % | Net | Avg | Thirds |
|---|---|---|---|---|---|
| Flip | 458 | 51% | -108.5 | -0.24 | -50 / +5 / -64 |
| LTF20 on-candle | 664 | 53% | +128.3 | +0.19 | +36 / +109 / -17 |
| LTF20 late | 166 | 52% | +8.8 | +0.05 | +40 / -29 / -2 |
| HTF EMA9 (incl late) | 221 | 46% | -29.6 | -0.13 | -30 / +12 / -11 |
| HTF EMA20 (incl late) | 104 | 55% | +51.5 | +0.50 | +2 / +24 / +25 |
| All | 1613 | 51% | +50.7 | +0.03 | -2 / +121 / -69 |

| LTF late window | Setups | Net | Δ vs 1 | z | Δ by third | Verdict | LTF20 late setups / net |
|---|---|---|---|---|---|---|---|
| 0 | 1519 | +8.9 | -41.8 | -0.6 | -48 / +22 / -16 | worse | 0 / +0.0 |
| 1 (current) | 1613 | +50.7 | +0.0 | +0.0 | +0 / +0 / +0 | baseline | 166 / +8.8 |
| 2 | 1643 | +67.2 | +16.5 | +0.4 | +24 / -9 / +2 | noise | 219 / +20.2 |
| 3 | 1652 | +67.8 | +17.1 | +0.4 | +29 / -9 / -3 | noise | 231 / +12.7 |

#### MES 5m 9/20 no gates, base exits (late-away 1 pt) — 61647 candles 01/05 → 11/13; thirds 01/06–04/20 / 04/20–08/02 / 08/02–11/13

| Trigger (window 1) | Setups | Win % | Net | Avg | Thirds |
|---|---|---|---|---|---|
| Flip | 344 | 53% | -27.5 | -0.08 | -2 / +44 / -70 |
| LTF20 on-candle | 644 | 49% | -151.4 | -0.24 | -198 / +82 / -35 |
| LTF20 late | 124 | 52% | +54.4 | +0.44 | +67 / -30 / +18 |
| HTF EMA9 (incl late) | 248 | 50% | -11.7 | -0.05 | -28 / +14 / +2 |
| HTF EMA20 (incl late) | 189 | 50% | +24.6 | +0.13 | +59 / -34 / +0 |
| All | 1549 | 50% | -111.6 | -0.07 | -103 / +76 / -85 |

| LTF late window | Setups | Net | Δ vs 1 | z | Δ by third | Verdict | LTF20 late setups / net |
|---|---|---|---|---|---|---|---|
| 0 | 1482 | -185.3 | -73.7 | -1.2 | -73 / +27 / -28 | worse | 0 / +0.0 |
| 1 (current) | 1549 | -111.6 | +0.0 | +0.0 | +0 / +0 / +0 | baseline | 124 / +54.4 |
| 2 | 1574 | -173.2 | -61.6 | -1.4 | -34 / -13 / -15 | worse | 170 / +11.3 |
| 3 | 1587 | -200.8 | -89.2 | -1.7 | -19 / -42 / -29 | worse | 188 / -3.8 |


### (C) and (E) Friday replays (new script rc.py, rebuilt 11/13)

DATA MES 3m: 102745 candles 01/05→11/13; non-weekend gaps > 6 h: []
DATA MES 2m: 82259 candles 05/31→11/13; non-weekend gaps > 6 h: []
DATA MES 5m: 61647 candles 01/05→11/13; non-weekend gaps > 6 h: []
DATA MGC 3m: 102525 candles 01/05→11/13; non-weekend gaps > 6 h: [('04/02', 73)]
C engine nets: MES5 1208 / +18; MES2 1415 / +33; MES3 tod 1738 / +9; MES3 p1 1799 / +60
| Chart | Span | Conf n / avg | Unconf n / avg | Δ avg | z | Δ by third | Last 4 wk conf / unconf |
|---|---|---|---|---|---|---|---|
| MES 2m by 5m | 05/31→11/13 (thirds cut 07/26 / 09/19) | 339 / +0.03 | 1076 / +0.02 | +0.01 | +0.0 | +0.52 / -0.27 / -0.18 | 49 / -1.32 · 195 / -0.39 |
| MES 3m by 5m (LIVE tod) | 01/05→11/13 (thirds cut 04/19 / 08/01) | 490 / +0.36 | 1248 / -0.13 | +0.49 | +1.3 | +0.89 / +0.83 / -0.14 | 34 / +1.69 · 116 / +1.00 |
| MES 3m by 5m (part 1.0) | 01/05→11/13 (thirds cut 04/19 / 08/01) | 517 / +0.35 | 1282 / -0.09 | +0.44 | +1.2 | +0.65 / +0.73 / +0.02 | 37 / +1.52 · 121 / +0.77 |

(E a) MES 3m TP cut
Base LIVE as stored (tod): 1738 setups, net +9.1
| Variant | Δ | z | Δ by third | Last 4 wk Δ | Rule exits | Setups changed |
|---|---|---|---|---|---|---|
| 21 min / 70 % / 1.5x (rule) | +51.6 | +0.9 | +32 / +4 / +16 | -12.9 | 48 | 67 |
| 15 min | +44.4 | +0.7 | +17 / -0 / +27 | -12.9 | 58 | 81 |
| 18 min | +75.9 | +1.3 | +45 / +4 / +27 | -12.9 | 51 | 71 |
| 24 min | +58.9 | +1.0 | +41 / +3 / +15 | -12.8 | 46 | 65 |
| 65 % | +34.6 | +0.6 | +22 / -4 / +16 | -17.5 | 49 | 68 |
| 75 % | +76.9 | +1.3 | +41 / +11 / +25 | -8.4 | 48 | 67 |
| ATR 1.4x | +82.8 | +1.2 | +48 / +25 / +9 | -12.9 | 68 | 92 |
| ATR 1.6x | +33.1 | +0.7 | +29 / +10 / -7 | -5.1 | 32 | 47 |
Base LIVE part=1.0 (v10.95 live): 1799 setups, net +60.1
| Variant | Δ | z | Δ by third | Last 4 wk Δ | Rule exits | Setups changed |
|---|---|---|---|---|---|---|
| 21 min / 70 % / 1.5x (rule) | +17.4 | +0.3 | +8 / +8 / +1 | -27.3 | 49 | 56 |
| 15 min | +13.4 | +0.2 | +1 / +0 / +13 | -27.3 | 59 | 67 |
| 18 min | +40.6 | +0.7 | +20 / +8 / +13 | -27.3 | 51 | 59 |
| 24 min | +24.7 | +0.5 | +17 / +8 / -0 | -27.1 | 47 | 54 |
| 65 % | +0.0 | +0.0 | -3 / +1 / +2 | -31.8 | 50 | 57 |
| 75 % | +43.0 | +0.8 | +17 / +16 / +10 | -22.7 | 49 | 56 |
| ATR 1.4x | +29.3 | +0.5 | +16 / +20 / -7 | -27.3 | 69 | 80 |
| ATR 1.6x | +17.3 | +0.4 | +16 / +18 / -16 | -15.9 | 32 | 38 |

(E b) MGC 3m profit lock
Base chop_sim EXIT MGC 3m (50 % + BE + trail 3.5, v10.84): 1147 setups, net +550.5
| Variant | Δ | z | Δ by third | Last 4 wk Δ | Lock exits | Setups changed |
|---|---|---|---|---|---|---|
| 75 % → +55 % (rule) | +91.3 | +0.4 | +73 / +26 / -8 | -34.2 | 286 | 647 |
| 70 % → +55 % | +146.0 | +0.7 | +119 / +69 / -43 | -47.5 | 351 | 673 |
| 80 % → +55 % | +75.0 | +0.4 | +73 / +26 / -24 | -41.3 | 228 | 610 |
| 75 % → +50 % | +24.2 | +0.1 | +46 / +6 / -28 | -38.3 | 275 | 518 |
| 75 % → +60 % | +95.7 | +0.4 | +99 / +53 / -56 | -73.1 | 307 | 660 |
Base FLIP 0 % (part 0, BE at TP1, no trail, v10.96 live): 1141 setups, net +855.2
| Variant | Δ | z | Δ by third | Last 4 wk Δ | Lock exits | Setups changed |
|---|---|---|---|---|---|---|
| 75 % → +55 % (rule) | +28.4 | +0.1 | +28 / +45 / -45 | -34.7 | 286 | 650 |
| 70 % → +55 % | +96.1 | +0.3 | +85 / +105 / -94 | -73.1 | 351 | 675 |
| 80 % → +55 % | +48.1 | +0.1 | +64 / +40 / -56 | -41.8 | 228 | 614 |
| 75 % → +50 % | -57.2 | -0.2 | +9 / +13 / -80 | -41.9 | 275 | 632 |
| 75 % → +60 % | +21.1 | +0.1 | +71 / +77 / -127 | -112.8 | 307 | 664 |

Thirds MES 3m: 01/05→04/19 / 08/01 / 08/01→11/13; MGC 3m cuts 04/19 / 08/01; last 4 wk from 10/16 (MES 3m) / 10/16 (MGC 3m)
---

## Run 2026-11-12 17:37 ET (Thu)

Thursday run, so no Friday replays were run.
- (A) keep 9 / 20: slow 14 +207 (z 0.7), slow 16 +226 (z 0.9); last 4 wk +29 / +77.
- (B) keep 1.75: 107 setups, 1.5 +33.1 / 1.75 +60.8 / 2.0 +64.7 ('tod' model).
- (C) keep watching, using the old confirmation rule (see the 11/13 correction): 2m 88 conf +0.10 vs 54 unconf -1.69; 3m 77 conf +0.09 vs 30 unconf -0.63.
- (D) keep watching: LTF late 2m 18 / -24.0, 3m 20 / -21.1, 5m 15 / -7.5; bot set 31 / +25.7.
- (E) keep watching: first MES 3m TP cut hit +11.44 vs +5.25; MGC 3m lock 5 hits, 2 comparable +8.10.
- (F) too few yet: MES 3m 8 / +7.2, 2m 5 / -16.2, 5m 5 / +13.5.

Data: MES 3m alerts gap 11/08 20:45 → 11/12 09:30. MGC 3m had no Trade Setup 11/11 06:15 → 11/12.

---

## Run 2026-11-12 09:44 ET (Thu, also stands in for the missed 11/11 run)

- (A) keep 9 / 20: slow 14 Δ +214 z 0.8, slow 16 Δ +222 z 0.9.
- (B) keep 1.75: 106 setups, 1.5 +27.9 / 1.75 +55.6 / 2.0 +59.5.
- (C) keep watching.
- (D) keep watching.
- (E) keep watching.
- (F) too few yet.

---

## Run 2026-11-09 17:38 ET (Mon)

- (A) keep 9 / 20: slow 14 +204 z 0.7, slow 16 +201 z 0.8.
- (B) keep 1.75: 105 setups, 1.5 +46.6 / 1.75 +74.3 / 2.0 +78.2.
- (C) keep watching.
- (D) keep watching: LTF late 2m 15 / -27.0, 3m 20 / -21.1, 5m 9 / -4.7.
- (E) keep watching.
- (F) too few yet.

---

## Run 2026-11-07 09:44 ET (delayed 11/06 Friday run)

Replays used live TP1 2.0 (v10.67–10.81).

(D) replay totals: MES 2m 1544 setups / +111.9, MES 3m 1669 / -11.4, MES 5m 1515 / -122.5.

LTF late window 0 vs 1: MES 2m -44.1 (z -1.0), MES 3m -2.4 (z -0.0), MES 5m -74.1 (z -1.7).

(C) replay:
- MES 2m by 5m: Δ -0.03, z -0.1.
- MES 3m by 5m: Δ +0.16, z 0.4.

(E) replay, 11/06 script:
- MES 3m TP cut: +167.5, z 2.8, thirds +131 / +6 / +30.
- MGC 3m lock on the 80 % / 1.7 base: +306.9, z 2.4, last 4 wk -45.

---

## Run 2026-11-05 17:37 ET (Thu)

- (A) keep 9 / 20, at TP1 2.0: slow 14 +184 z 0.6, slow 16 +178 z 0.7.
- (B) keep 2.0: 100 setups, 2.0 +100.9 > 1.75 +93.9 > 1.5 +68.7.
- (C) MES 2m ACT (provisional), but under the old confirmation rule. MES 3m keep watching.
- (D) keep watching.
