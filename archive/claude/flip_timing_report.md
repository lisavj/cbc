# Flip timing study — weekly check -- 2026-11-07 09:52 ET (rerun after data repair; replaces the 11/06 run)

## Since last week (vs the Fri 11/06 17:53 ET report)

**Note on this run:** manual rerun of the 11/06 check after the BarFeed bar data was repaired (MGC 3m had 5m candles mixed in; MES 2m/5m had gaps). It **replaces** the 11/06 run in the check history: the streak stays at 3 (10/28, 10/30, 11/06-rerun). Numbers compare the repaired data with the original 11/06 17:53 report (a 09:46 ET run today already used the repaired data and matched exactly). The repair also moved the confirmed HTF CBC flip for a few live MES 3m setups, which re-bucketed them. 5m results are identical.

- **MGC 3m:** median flip→entry 18 min (live 27). Weak HTF EMA20 Pierce at 2 candles still (30 · −49.1); **HTF EMA9 at 3–4 flagged again** (21 · −29.7). Flip-candle HTF CBC Flip still strong (210 · +106.3); 3–4 LTF EMA20 now ✓. London flip-candle entries still weak (153 · −233.0). Live 67.
- **MES 3m:** median 21 (live 27). **5–8 HTF candles still weak: 237 · −88.9, thirds −35 / −52 / −2** (was −106.3; HTF EMA9 sub-cell 57 · −47.4 still ⚠, LTF EMA20 sub-cell 150 · −54.4 no longer all-thirds negative). 9–16 candles now ✓ strong (140 · +32.7). **Live 5–8 bucket now 18 · 50% · −14.2** (was 15 · −33.7 — 3 live setups moved in after the archive revision; pierces only 17 · −20.8). Live flip-candle entries 32 · +58.7 vs later entries 71 · −49.2. London flip-candle weak still; NY 5–8 weak dropped.
- **MGC 2m:** median 6 (live 12). 3–4 candles ✓ strong again (153 · +75.2). Weak HTF EMA9 at 1 candle still (38 · −35.6). Live 144; live flip candle 60 · −39.5, 2 candles 16 · −38.5.
- **MES 2m:** median 10 (live 12). **9–16 HTF candles weak unchanged: 105 · −78.2, thirds −35 / −27 / −16** (LTF EMA20 68 · −52.0 ⚠). **Live 9–16: 14 · 29% · −27.8** (13 pierces · −24.6). Live 116.
- **MGC 5m:** unchanged (weak HTF EMA9 at 1 and 9–16, HTF EMA20 at 1, LTF EMA20 at 2). Live 49.
- **MES 5m:** unchanged — 3–4 HTF candles weak (118 · −102.1, −23 / −57 / −22), live 9 · +1.1 → still fails (c). Live 58.

**Verdict — the two rules from 11/06 still meet all three conditions** (sim ≥ 20 all thirds negative, held on the 3 weekly checks 10/28 · 10/30 · 11/06 (now the repaired-data rerun), ≥ 10 live net negative):

1. **MES 3m — no new pierce setups 5–8 HTF (15m) candles after the HTF CBC flip** (75–120 min). Sim 237 · −88.9 (−35 / −52 / −2 — last third now only just negative, watch it next Friday); live 18 · −14.2 (pierces 17 · −20.8). Caveat: live includes 10/19–10/27 setups before the v10.42 MES 3m exit change.
2. **MES 2m — no new setups 9–16 HTF (10m) candles after the HTF CBC flip** (90–160 min). Sim 105 · −78.2 (−35 / −27 / −16); live 14 · −27.8.

Not yet: MES 5m pierces 3–4 HTF candles (live 9 · +1.1). Both changes need a CBC Pine change (a per-chart "max HTF candles since the flip" window for new setups — CBC has no such rule today). No Pine or server change made. Hold-time buckets describe outcomes and are not filters.

---

# Flip timing — entry and exit relative to the HTF CBC flip -- 2026-11-07 09:52 ET (rerun after data repair)

CBC flip-timing study: how long after the HTF CBC flip are setups entered and exited, and does it matter?

For every setup: (1) time from the HTF CBC flip that started the current trend direction to the ENTRY candle,
(2) hold time ENTRY -> EXIT, (3) time from the flip to the EXIT. In minutes and in HTF candles (3m chart -> 15m HTF,
2m chart -> 10m HTF). Flip = the last chart candle where the confirmed HTF CBC (bar field hc) changed to the trade
direction, at or before the entry candle.
Cases: MGC 3m, MES 3m (HTF 15m), MGC 2m, MES 2m (HTF 10m), MGC 5m, MES 5m (HTF 25m; base exits, no gates -- set in evening_study.py). Sources:
  LIVE  real Trade Setup alerts matched to their Setup Ended results ("Lasted" and the exit time come from the alert).
  SIM   chop_sim.py replay (current CBC-style rules + exits, ~50 % exact match with real setups) on the BarFeed
        archive: 3m and 5m from 01/05, 2m from 06/01. Use it to compare buckets, not for exact totals.
Each chart also gets a table splitting entry timing by session (Asia 18:00–03:00, London 03:00–09:30, NY 09:30–16:00 ET).
Thirds = the case's sim setups split into three equal time blocks. A cell is "⚠ weak" with >= 20 sim setups
negative in all three thirds, "✓ strong" with >= 20 positive in all three thirds.
Usage: python3 flip_timing_study.py > flip_timing_report_new.md   (needs chop_sim.py and evening_study.py next to it)

Cells: setups · win % · net pts.

## MGC 3m (HTF 15m) — sim 01/05 → 11/06, 1183 setups · live 67 setups (67 matched to bars)

Median minutes — sim: flip→entry 18, hold 18, flip→exit 48 · live: flip→entry 27, hold 15, flip→exit 57

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 21, HTF EMA9 Pierce 36, HTF EMA20 Pierce 28

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 503 · 42% · +17.4 | +0.03 | +2 / +62 / -47 | 20 · 40% · -18.1 | 210 · 47% · +106.3 ✓ | 179 · 39% · -29.6 | 59 · 36% · -67.9 | 55 · 44% · +8.6 |
| 1 | 228 · 44% · +104.1 | +0.46 | +132 / -36 / +7 | 14 · 36% · -14.9 | – | 161 · 43% · +50.1 | 35 · 43% · +6.2 | 32 · 53% · +47.9 |
| 2 | 109 · 40% · +30.3 | +0.28 | +65 / +4 / -39 | 10 · 80% · +25.0 | – | 61 · 51% · +99.8 | 18 · 33% · -20.5 | 30 · 23% · -49.1 ⚠ |
| 3–4 | 130 · 48% · +100.1 | +0.77 | +57 / -15 / +59 | 12 · 17% · -29.9 | – | 86 · 48% · +100.3 ✓ | 21 · 33% · -29.7 ⚠ | 23 · 65% · +29.5 |
| 5–8 | 150 · 44% · +21.5 | +0.14 | -70 / +61 / +30 | 7 · 57% · +10.7 | – | 82 · 43% · +15.8 | 46 · 46% · -6.9 | 22 · 45% · +12.6 |
| 9–16 | 56 · 41% · +27.4 | +0.49 | -8 / +7 / +28 | 4 · 25% · -7.0 | – | 29 · 31% · -17.2 | 16 · 56% · +31.9 | 11 · 45% · +12.7 |
| 17–32 | 7 · 29% · -4.5 | -0.65 | +8 / -13 / +0 | – | – | 4 · 25% · +3.4 | 2 · 50% · -6.0 | 1 · 0% · -2.0 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 491 · 12% · -1751.9 ⚠ weak | -3.57 | -691 / -554 / -506 | 33 · 15% · -103.4 | 66 · 6% · -305.7 ⚠ | 240 · 8% · -941.2 ⚠ | 105 · 16% · -354.6 ⚠ | 80 · 26% · -150.4 ⚠ |
| 15–30 | 271 · 41% · -140.1 | -0.52 | +70 / -122 / -88 | 14 · 50% · -8.7 | 53 · 38% · -48.1 | 136 · 43% · -45.2 | 38 · 39% · -27.3 | 44 · 41% · -19.6 |
| 30–60 | 269 · 75% · +822.8 ✓ strong | +3.06 | +278 / +325 / +220 | 12 · 67% · +32.5 | 59 · 80% · +219.6 ✓ | 140 · 71% · +382.2 ✓ | 36 · 83% · +104.9 ✓ | 34 · 74% · +116.1 ✓ |
| 1–2 h | 130 · 89% · +1031.6 ✓ strong | +7.94 | +402 / +377 / +253 | 7 · 100% · +39.0 | 28 · 86% · +189.9 ✓ | 71 · 89% · +585.6 ✓ | 16 · 100% · +153.1 | 15 · 87% · +103.1 |
| 2–4 h | 20 · 100% · +282.5 ✓ strong | +14.12 | +95 / +27 / +161 | 1 · 100% · +6.4 | 4 · 100% · +50.5 | 13 · 100% · +189.8 | 2 · 100% · +31.1 | 1 · 100% · +11.0 |
| 4 h+ | 2 · 100% · +51.4 | +25.68 | +33 / +19 / +0 | – | – | 2 · 100% · +51.4 | – | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 503 | 47% | 42% | 8% | 2% | 21 |
| 1 | 228 | 39% | 40% | 19% | 2% | 18 |
| 2 | 109 | 31% | 36% | 33% | 0% | 15 |
| 3–4 | 130 | 35% | 41% | 22% | 2% | 16 |
| 5–8 | 150 | 34% | 37% | 29% | 0% | 15 |
| 9–16 | 56 | 41% | 34% | 25% | 0% | 9 |
| 17–32 | 7 | 29% | 29% | 43% | 0% | 9 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 582 · 46% · +362.3 · live 21 · 43% · -1.0 | 247 · 45% · +108.0 ✓ (+66 / +21 / +21) · live 4 · 75% · +12.9 | 224 · 48% · +195.9 ✓ (+136 / +33 / +27) · live 13 · 31% · -16.9 | 75 · 47% · +28.5 (-31 / +21 / +39) · live 2 · 50% · -0.1 | 36 · 42% · +29.8 (+29 / -9 / +10) · live 2 · 50% · +3.0 |
| London 03:00–09:30 | 358 · 36% · -192.7 · live 21 · 24% · -47.1 | 153 · 32% · -233.0 ⚠ (-93 / -81 / -59) · live 7 · 14% · -25.5 | 152 · 39% · +22.9 (+96 / -92 / +19) · live 12 · 33% · -15.6 | 35 · 43% · +11.8 (-20 / +30 / +1) · live 1 · 0% · -1.0 | 18 · 39% · +5.6 (-21 / +19 / +7) · live 1 · 0% · -5.0 |
| NY 09:30–16:00 | 243 · 46% · +126.6 · live 25 · 56% · +13.9 | 103 · 50% · +142.4 (+29 / +122 / -9) · live 9 · 44% · -5.5 | 91 · 45% · +15.6 (+22 / +13 / -19) · live 11 · 64% · +12.7 | 40 · 40% · -18.8 (-19 / +10 / -10) · live 4 · 75% · +11.7 | 9 · 33% · -12.6 (-8 / -16 / +11) · live 1 · 0% · -5.0 |

## MES 3m (HTF 15m) — sim 01/05 → 11/06, 1719 setups · live 103 setups (103 matched to bars)

Median minutes — sim: flip→entry 21, hold 21, flip→exit 60 · live: flip→entry 27, hold 18, flip→exit 63

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 33, HTF EMA9 Pierce 45, HTF EMA20 Pierce 38

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 677 · 52% · +2.9 | +0.00 | -101 / -49 / +153 | 32 · 59% · +58.7 | 313 · 56% · +83.9 | 239 · 52% · +13.3 | 69 · 41% · -73.8 ⚠ | 56 · 48% · -20.5 ⚠ |
| 1 | 273 · 45% · -34.8 | -0.13 | +104 / -135 / -4 | 20 · 35% · -11.9 | – | 199 · 47% · +26.4 | 45 · 40% · -66.8 ⚠ | 29 · 45% · +5.7 |
| 2 | 134 · 52% · +72.5 ✓ strong | +0.54 | +42 / +7 / +23 | 4 · 50% · -0.7 | – | 94 · 52% · +43.7 ✓ | 26 · 58% · +29.6 | 14 · 43% · -0.8 |
| 3–4 | 233 · 50% · +20.2 | +0.09 | +105 / -17 / -67 | 17 · 29% · -37.0 | – | 150 · 51% · +2.1 | 52 · 48% · +16.5 | 31 · 48% · +1.7 |
| 5–8 | 237 · 45% · -88.9 ⚠ weak | -0.38 | -35 / -52 / -2 | 18 · 50% · -14.2 | – | 150 · 43% · -54.4 | 57 · 44% · -47.4 ⚠ | 30 · 53% · +12.9 |
| 9–16 | 140 · 49% · +32.7 ✓ strong | +0.23 | +5 / +27 / +1 | 11 · 45% · +6.5 | – | 97 · 51% · +26.3 ✓ | 28 · 50% · +8.1 | 15 · 40% · -1.6 |
| 17–32 | 25 · 60% · +11.2 | +0.45 | +14 / +3 / -6 | 1 · 100% · +8.1 | – | 14 · 64% · +12.7 | 8 · 50% · -2.6 | 3 · 67% · +1.1 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 623 · 24% · -1635.6 ⚠ weak | -2.63 | -615 / -589 / -431 | 41 · 12% · -182.8 | 70 · 29% · -235.7 ⚠ | 330 · 19% · -952.7 ⚠ | 136 · 27% · -313.6 ⚠ | 87 · 33% · -133.6 ⚠ |
| 15–30 | 388 · 45% · -224.9 | -0.58 | +34 / -185 / -75 | 22 · 50% · -11.3 | 73 · 51% · -53.5 | 215 · 41% · -154.0 | 64 · 48% · -22.5 | 36 · 50% · +5.1 |
| 30–60 | 427 · 67% · +631.0 ✓ strong | +1.48 | +303 / +192 / +135 | 24 · 67% · +44.1 | 93 · 58% · +65.8 ✓ | 241 · 71% · +432.9 ✓ | 62 · 66% · +100.0 ✓ | 31 · 61% · +32.2 |
| 1–2 h | 257 · 87% · +1063.9 ✓ strong | +4.14 | +344 / +317 / +403 | 15 · 100% · +143.6 | 73 · 84% · +280.0 ✓ | 142 · 90% · +639.3 ✓ | 20 · 85% · +75.1 ✓ | 22 · 77% · +69.5 ✓ |
| 2–4 h | 23 · 96% · +170.8 ✓ strong | +7.43 | +66 / +38 / +67 | 1 · 100% · +15.8 | 4 · 100% · +27.3 | 15 · 93% · +104.4 | 3 · 100% · +24.4 | 1 · 100% · +14.8 |
| 4 h+ | 1 · 100% · +10.5 | +10.51 | +0 / +11 / +0 | – | – | – | – | 1 · 100% · +10.5 |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 677 | 34% | 50% | 14% | 2% | 27 |
| 1 | 273 | 26% | 40% | 32% | 2% | 18 |
| 2 | 134 | 16% | 47% | 35% | 1% | 21 |
| 3–4 | 233 | 24% | 41% | 33% | 2% | 15 |
| 5–8 | 237 | 24% | 37% | 38% | 1% | 15 |
| 9–16 | 140 | 21% | 41% | 34% | 3% | 18 |
| 17–32 | 25 | 16% | 48% | 36% | 0% | 30 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 628 · 51% · +129.7 · live 20 · 55% · +44.6 | 249 · 53% · -0.3 (-28 / -47 / +75) · live 6 · 67% · +10.6 | 218 · 51% · +110.4 (+115 / -18 / +13) · live 8 · 38% · +7.0 | 86 · 47% · -10.8 (-9 / +12 / -15) · live 4 · 50% · +0.7 | 75 · 51% · +30.4 (+15 / +28 / -12) · live 2 · 100% · +26.2 |
| London 03:00–09:30 | 560 · 46% · -156.7 · live 36 · 42% · -39.9 | 239 · 48% · -72.4 ⚠ (-17 / -29 / -26) · live 11 · 55% · +0.3 | 204 · 45% · -24.9 (+25 / -41 / -9) · live 18 · 39% · -19.4 | 73 · 42% · -23.9 (-5 / -25 / +6) · live 3 · 33% · -10.4 | 44 · 43% · -35.5 (-17 / -20 / +1) · live 4 · 25% · -10.4 |
| NY 09:30–16:00 | 531 · 53% · +42.8 · live 47 · 47% · +4.7 | 189 · 58% · +75.6 (-56 / +28 / +104) · live 15 · 60% · +47.8 | 218 · 50% · -27.5 (+110 / -86 / -52) · live 15 · 27% · -37.3 | 78 · 45% · -54.2 (-22 / -40 / +7) · live 11 · 55% · -4.5 | 46 · 59% · +49.0 ✓ (+21 / +22 / +6) · live 6 · 50% · -1.2 |

## MGC 2m (HTF 10m) — sim 06/01 → 11/06, 1499 setups · live 144 setups (144 matched to bars)

Median minutes — sim: flip→entry 6, hold 16, flip→exit 34 · live: flip→entry 12, hold 17, flip→exit 39

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 22, HTF EMA9 Pierce 24, HTF EMA20 Pierce 12

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 801 · 54% · +225.2 | +0.28 | -65 / +233 / +57 | 60 · 48% · -39.5 | 490 · 51% · -3.0 | 184 · 61% · +198.5 ✓ | 72 · 58% · +26.6 ✓ | 55 · 53% · +3.1 |
| 1 | 173 · 47% · +13.8 | +0.08 | +98 / -39 / -45 | 19 · 53% · +10.4 | – | 116 · 48% · +33.7 | 38 · 39% · -35.6 ⚠ | 19 · 58% · +15.7 |
| 2 | 104 · 50% · -7.1 | -0.07 | +5 / +4 / -16 | 16 · 25% · -38.5 | – | 72 · 51% · -3.5 | 19 · 42% · -1.6 | 13 · 54% · -1.9 |
| 3–4 | 153 · 53% · +75.2 ✓ strong | +0.49 | +41 / +25 / +9 | 10 · 50% · +0.8 | – | 89 · 55% · +55.4 ✓ | 37 · 54% · +29.6 | 27 · 44% · -9.9 |
| 5–8 | 159 · 50% · +44.0 | +0.28 | -24 / +20 / +49 | 25 · 52% · +6.1 | – | 104 · 50% · +60.2 | 48 · 50% · -9.5 | 7 · 43% · -6.7 |
| 9–16 | 92 · 46% · -10.7 | -0.12 | +1 / +2 / -14 | 8 · 50% · -2.1 | – | 62 · 48% · +1.6 | 24 · 42% · -10.4 | 6 · 33% · -1.9 |
| 17–32 | 16 · 31% · -5.0 | -0.31 | -5 / -7 / +8 | 6 · 33% · -0.9 | – | 13 · 31% · +1.3 | 1 · 100% · +0.3 | 2 · 0% · -6.6 |
| 33+ | 1 · 100% · +4.8 | +4.80 | +0 / +0 / +5 | – | – | 1 · 100% · +4.8 | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 677 · 30% · -1436.4 ⚠ weak | -2.12 | -601 / -363 / -473 | 63 · 27% · -151.1 | 161 · 27% · -481.4 ⚠ | 286 · 26% · -650.0 ⚠ | 146 · 34% · -205.5 ⚠ | 84 · 40% · -99.4 ⚠ |
| 15–30 | 404 · 57% · +274.2 ✓ strong | +0.68 | +94 / +92 / +89 | 44 · 59% · +20.9 | 161 · 48% · -20.9 | 183 · 64% · +259.2 ✓ | 40 · 60% · +9.1 | 20 · 60% · +26.8 ✓ |
| 30–60 | 335 · 79% · +995.3 ✓ strong | +2.97 | +363 / +363 / +269 | 28 · 57% · +27.1 | 134 · 73% · +308.1 ✓ | 135 · 84% · +486.7 ✓ | 45 · 84% · +149.3 ✓ | 21 · 71% · +51.2 ✓ |
| 1–2 h | 82 · 96% · +500.2 ✓ strong | +6.10 | +186 / +146 / +168 | 9 · 89% · +39.2 | 33 · 94% · +184.2 ✓ | 37 · 100% · +256.2 ✓ | 8 · 100% · +46.5 | 4 · 75% · +13.2 |
| 2–4 h | 1 · 100% · +7.1 | +7.07 | +7 / +0 / +0 | – | 1 · 100% · +7.1 | – | – | – |
| 4 h+ | – | – | – | – | – | – | – | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 801 | 34% | 52% | 12% | 2% | 20 |
| 1 | 173 | 26% | 41% | 31% | 2% | 12 |
| 2 | 104 | 29% | 42% | 27% | 2% | 14 |
| 3–4 | 153 | 18% | 41% | 39% | 1% | 12 |
| 5–8 | 159 | 18% | 42% | 40% | 1% | 12 |
| 9–16 | 92 | 26% | 42% | 29% | 2% | 12 |
| 17–32 | 16 | 19% | 19% | 56% | 6% | 7 |
| 33+ | 1 | 0% | 100% | 0% | 0% | 42 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 602 · 51% · +43.5 · live 39 · 44% · -30.2 | 323 · 56% · +115.3 (+2 / +118 / -5) · live 13 · 54% · -9.1 | 173 · 47% · -16.0 (+24 / -11 / -28) · live 14 · 29% · -23.7 | 66 · 44% · -13.9 (-29 / +3 / +12) · live 8 · 50% · +4.2 | 40 · 38% · -41.9 ⚠ (-21 / -6 / -15) · live 4 · 50% · -1.7 |
| London 03:00–09:30 | 489 · 54% · +201.6 · live 51 · 41% · -44.6 | 254 · 54% · +80.3 (-67 / +48 / +99) · live 24 · 33% · -42.2 | 144 · 53% · +52.9 (+48 / +43 / -38) · live 14 · 50% · -2.6 | 50 · 54% · +37.9 ✓ (+9 / +11 / +18) · live 9 · 56% · +5.1 | 41 · 54% · +30.5 ✓ (+7 / +5 / +19) · live 4 · 25% · -4.9 |
| NY 09:30–16:00 | 408 · 51% · +95.2 · live 54 · 54% · +11.1 | 224 · 52% · +29.6 (-0 / +67 / -38) · live 23 · 61% · +11.8 | 113 · 51% · +45.0 (+72 / -42 / +15) · live 17 · 47% · -1.0 | 43 · 53% · +20.0 (-4 / +6 / +18) · live 8 · 50% · -3.2 | 28 · 39% · +0.6 (+9 / -4 / -5) · live 6 · 50% · +3.5 |

## MES 2m (HTF 10m) — sim 06/01 → 11/06, 1226 setups · live 116 setups (116 matched to bars)

Median minutes — sim: flip→entry 10, hold 18, flip→exit 40 · live: flip→entry 12, hold 14, flip→exit 38

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 32, HTF EMA9 Pierce 38, HTF EMA20 Pierce 26

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 595 · 51% · -134.8 | -0.23 | -56 / +78 / -157 | 53 · 45% · -46.3 | 419 · 51% · -83.2 | 116 · 49% · -34.5 | 39 · 51% · -8.2 | 21 · 48% · -8.9 |
| 1 | 117 · 46% · +17.0 | +0.15 | -1 / -16 / +35 | 11 · 45% · -1.4 | – | 84 · 44% · +7.6 | 19 · 42% · -5.3 | 14 · 64% · +14.7 |
| 2 | 83 · 48% · -20.6 | -0.25 | -37 / +7 / +9 | 7 · 29% · -14.6 | – | 57 · 49% · -18.4 | 14 · 36% · -12.3 | 12 · 58% · +10.0 |
| 3–4 | 136 · 47% · +44.1 | +0.32 | -12 / +25 / +31 | 14 · 50% · +14.1 | – | 81 · 51% · +29.0 | 38 · 42% · +4.4 | 17 · 41% · +10.7 |
| 5–8 | 174 · 51% · +4.5 | +0.03 | +15 / +18 / -28 | 13 · 54% · +0.7 | – | 118 · 51% · -0.4 | 45 · 56% · +14.5 | 11 · 36% · -9.5 |
| 9–16 | 105 · 41% · -78.2 ⚠ weak | -0.74 | -35 / -27 / -16 | 14 · 29% · -27.8 | – | 68 · 40% · -52.0 ⚠ | 25 · 56% · +0.0 | 12 · 17% · -26.2 |
| 17–32 | 14 · 43% · -14.8 | -1.06 | -4 / +3 / -14 | 2 · 0% · -7.0 | – | 12 · 33% · -18.5 | 2 · 100% · +3.7 | – |
| 33+ | 2 · 0% · -11.0 | -5.48 | +0 / +0 / -11 | 2 · 50% · -0.7 | – | 1 · 0% · -5.0 | 1 · 0% · -6.0 | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 520 · 27% · -1139.3 ⚠ weak | -2.19 | -422 / -276 / -441 | 60 · 27% · -151.0 | 134 · 34% · -322.5 ⚠ | 234 · 23% · -555.4 ⚠ | 101 · 28% · -192.6 ⚠ | 51 · 29% · -68.8 ⚠ |
| 15–30 | 360 · 54% · +38.2 | +0.11 | -6 / +40 / +4 | 36 · 53% · +9.8 | 139 · 46% · -87.8 ⚠ | 152 · 55% · +46.6 ✓ | 45 · 64% · +36.2 ✓ | 24 · 71% · +43.2 ✓ |
| 30–60 | 263 · 73% · +587.0 ✓ strong | +2.23 | +194 / +206 / +187 | 18 · 78% · +55.6 | 110 · 68% · +197.9 ✓ | 113 · 76% · +284.3 ✓ | 29 · 86% · +86.4 ✓ | 11 · 64% · +18.4 |
| 1–2 h | 81 · 83% · +307.3 ✓ strong | +3.79 | +91 / +116 / +100 | 2 · 50% · +2.5 | 34 · 82% · +116.2 ✓ | 38 · 82% · +132.3 ✓ | 8 · 100% · +60.8 | 1 · 0% · -2.0 |
| 2–4 h | 2 · 100% · +13.1 | +6.55 | +13 / +0 / +0 | – | 2 · 100% · +13.1 | – | – | – |
| 4 h+ | – | – | – | – | – | – | – | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 595 | 31% | 48% | 20% | 1% | 20 |
| 1 | 117 | 21% | 42% | 36% | 1% | 18 |
| 2 | 83 | 18% | 40% | 42% | 0% | 14 |
| 3–4 | 136 | 16% | 44% | 40% | 0% | 16 |
| 5–8 | 174 | 21% | 43% | 36% | 0% | 14 |
| 9–16 | 105 | 25% | 37% | 38% | 0% | 12 |
| 17–32 | 14 | 29% | 29% | 36% | 7% | 17 |
| 33+ | 2 | 100% | 0% | 0% | 0% | 17 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 497 · 48% · -140.7 · live 23 · 26% · -54.5 | 242 · 51% · -63.6 (+20 / -3 / -81) · live 12 · 42% · -10.0 | 135 · 45% · -25.8 (-17 / -17 / +8) · live 7 · 14% · -24.1 | 75 · 48% · -23.4 (-11 / +6 / -19) · live 2 · 0% · -7.4 | 45 · 42% · -27.9 ⚠ (-8 / -6 / -14) · live 2 · 0% · -13.0 |
| London 03:00–09:30 | 383 · 47% · -114.7 · live 39 · 49% · -3.5 | 194 · 47% · -109.5 (-83 / +39 / -65) · live 17 · 53% · -4.9 | 102 · 43% · -19.9 (-8 / -19 / +7) · live 10 · 50% · +8.4 | 47 · 60% · +33.5 ✓ (+26 / +7 / +0) · live 1 · 100% · +2.4 | 40 · 42% · -18.8 (-11 / -12 / +4) · live 11 · 36% · -9.4 |
| NY 09:30–16:00 | 346 · 51% · +61.7 · live 54 · 46% · -25.1 | 159 · 54% · +38.4 (+8 / +42 / -11) · live 24 · 42% · -31.3 | 99 · 54% · +86.2 (-25 / +51 / +60) · live 15 · 53% · +13.7 | 52 · 48% · -5.6 (-1 / +5 / -9) · live 10 · 60% · +5.7 | 36 · 36% · -57.2 ⚠ (-20 / -7 / -31) · live 5 · 20% · -13.1 |

## MGC 5m (HTF 25m) — sim 01/05 → 11/06, 1173 setups · live 49 setups (49 matched to bars)

Median minutes — sim: flip→entry 30, hold 20, flip→exit 75 · live: flip→entry 30, hold 25, flip→exit 75

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 70, HTF EMA9 Pierce 70, HTF EMA20 Pierce 30

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 527 · 54% · +47.8 | +0.09 | +29 / +48 / -30 | 21 · 43% · -30.9 | 322 · 55% · +73.4 | 114 · 49% · -58.2 | 48 · 62% · +52.8 | 43 · 49% · -20.2 |
| 1 | 160 · 50% · +17.8 | +0.11 | -42 / +12 / +48 | 4 · 50% · -3.8 | – | 109 · 56% · +85.3 | 27 · 30% · -43.1 ⚠ | 24 · 46% · -24.4 ⚠ |
| 2 | 90 · 44% · -53.8 | -0.60 | -53 / +12 / -13 | 4 · 50% · +2.3 | – | 64 · 45% · -39.6 ⚠ | 15 · 27% · -39.5 | 11 · 64% · +25.3 |
| 3–4 | 149 · 50% · -39.6 | -0.27 | -85 / +60 / -15 | 9 · 56% · +4.5 | – | 105 · 50% · -38.2 | 28 · 57% · +22.4 | 16 · 38% · -23.7 |
| 5–8 | 143 · 47% · -38.7 | -0.27 | +46 / -36 / -49 | 10 · 40% · -5.8 | – | 102 · 46% · -34.0 | 29 · 48% · -10.2 | 12 · 50% · +5.5 |
| 9–16 | 92 · 50% · -33.1 | -0.36 | -45 / +28 / -16 | 1 · 0% · -1.7 | – | 61 · 57% · +12.8 | 26 · 27% · -52.7 ⚠ | 5 · 80% · +6.8 |
| 17–32 | 12 · 42% · -17.6 | -1.46 | -3 / +5 / -20 | – | – | 9 · 44% · -11.8 | 2 · 0% · -14.0 | 1 · 100% · +8.2 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 337 · 23% · -1238.4 ⚠ weak | -3.67 | -563 / -321 / -355 | 13 · 23% · -36.7 | 74 · 27% · -267.6 ⚠ | 157 · 22% · -645.0 ⚠ | 63 · 17% · -229.4 ⚠ | 43 · 33% · -96.4 ⚠ |
| 15–30 | 325 · 38% · -625.0 ⚠ weak | -1.92 | -144 / -230 / -250 | 14 · 29% · -36.0 | 84 · 40% · -164.2 ⚠ | 158 · 38% · -305.6 ⚠ | 46 · 33% · -110.6 ⚠ | 37 · 43% · -44.7 |
| 30–60 | 278 · 68% · +476.8 ✓ strong | +1.72 | +162 / +198 / +117 | 14 · 50% · -5.8 | 83 · 69% · +145.7 ✓ | 143 · 67% · +225.6 ✓ | 36 · 72% · +78.7 ✓ | 16 · 69% · +26.8 |
| 1–2 h | 173 · 84% · +799.2 ✓ strong | +4.62 | +250 / +304 / +245 | 7 · 100% · +38.0 | 56 · 77% · +186.1 ✓ | 77 · 86% · +398.3 ✓ | 26 · 88% · +138.3 ✓ | 14 · 93% · +76.5 |
| 2–4 h | 57 · 98% · +432.3 ✓ strong | +7.58 | +142 / +141 / +149 | 1 · 100% · +5.1 | 25 · 96% · +173.4 ✓ | 27 · 100% · +219.4 ✓ | 3 · 100% · +24.3 | 2 · 100% · +15.2 |
| 4 h+ | 3 · 100% · +37.9 | +12.63 | +0 / +38 / +0 | – | – | 2 · 100% · +23.4 | 1 · 100% · +14.4 | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 527 | 42% | 50% | 4% | 4% | 25 |
| 1 | 160 | 34% | 44% | 18% | 4% | 25 |
| 2 | 90 | 48% | 41% | 8% | 3% | 15 |
| 3–4 | 149 | 42% | 43% | 13% | 3% | 15 |
| 5–8 | 143 | 40% | 41% | 17% | 2% | 20 |
| 9–16 | 92 | 38% | 39% | 17% | 5% | 15 |
| 17–32 | 12 | 58% | 42% | 0% | 0% | 18 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 444 · 50% · -102.2 · live 14 · 43% · -23.7 | 205 · 55% · +55.7 (+66 / +37 / -47) · live 6 · 33% · -19.1 | 157 · 47% · -98.5 (-106 / +35 / -27) · live 4 · 75% · +7.8 | 45 · 44% · -19.0 (+5 / -7 / -17) · live 4 · 25% · -12.4 | 37 · 43% · -40.4 (-41 / -1 / +1) · live – |
| London 03:00–09:30 | 385 · 52% · +54.5 · live 14 · 29% · -31.4 | 167 · 54% · +19.3 (-25 / +37 / +7) · live 4 · 25% · -13.1 | 136 · 55% · +94.4 (-26 / +74 / +46) · live 6 · 33% · -16.8 | 44 · 45% · -4.3 (+15 / -17 / -2) · live 3 · 33% · +0.1 | 38 · 42% · -54.9 ⚠ (-23 / -11 / -21) · live 1 · 0% · -1.7 |
| NY 09:30–16:00 | 344 · 50% · -69.4 · live 21 · 57% · +19.7 | 155 · 52% · -27.2 (-12 / -26 / +11) · live 11 · 55% · +1.2 | 106 · 43% · -71.5 (-48 / -25 / +2) · live 7 · 57% · +12.0 | 54 · 50% · -15.4 (+26 / -12 / -30) · live 3 · 67% · +6.4 | 29 · 66% · +44.7 (+15 / +45 / -16) · live – |

## MES 5m (HTF 25m) — sim 01/05 → 11/06, 1183 setups · live 58 setups (58 matched to bars)

Median minutes — sim: flip→entry 25, hold 30, flip→exit 80 · live: flip→entry 28, hold 28, flip→exit 78

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 55, HTF EMA9 Pierce 60, HTF EMA20 Pierce 35

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 567 · 54% · +70.2 | +0.12 | +70 / +55 / -55 | 28 · 57% · -3.7 | 314 · 53% · -41.7 | 166 · 52% · +6.7 | 45 · 53% · +28.1 | 42 · 67% · +77.1 ✓ |
| 1 | 151 · 55% · +106.9 | +0.71 | -14 / +92 / +29 | 4 · 0% · -22.5 | – | 100 · 55% · +47.6 | 37 · 54% · +39.3 ✓ | 14 · 57% · +20.0 |
| 2 | 93 · 51% · +27.2 | +0.29 | +39 / +5 / -17 | 4 · 50% · -1.5 | – | 64 · 53% · +44.5 | 17 · 41% · -30.5 | 12 · 50% · +13.2 |
| 3–4 | 118 · 41% · -102.1 ⚠ weak | -0.87 | -23 / -57 / -22 | 9 · 56% · +1.1 | – | 76 · 41% · -73.2 ⚠ | 29 · 41% · -21.5 ⚠ | 13 · 38% · -7.4 |
| 5–8 | 155 · 48% · -59.4 | -0.38 | -107 / +19 / +29 | 9 · 33% · -9.9 | – | 103 · 43% · -96.7 | 35 · 66% · +56.0 ✓ | 17 · 41% · -18.7 |
| 9–16 | 84 · 44% · -37.5 | -0.45 | -20 / +19 / -37 | 3 · 33% · -11.2 | – | 57 · 44% · -38.6 | 20 · 50% · +2.4 | 7 · 29% · -1.3 |
| 17–32 | 15 · 47% · -14.1 | -0.94 | -1 / -6 / -8 | 1 · 100% · +5.1 | – | 10 · 60% · +8.4 | 3 · 33% · -7.8 | 2 · 0% · -14.7 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 260 · 21% · -958.3 ⚠ weak | -3.69 | -372 / -311 / -275 | 13 · 0% · -84.4 | 38 · 13% · -227.0 ⚠ | 132 · 19% · -544.5 ⚠ | 64 · 31% · -114.2 ⚠ | 26 · 19% · -72.7 ⚠ |
| 15–30 | 315 · 37% · -519.4 ⚠ weak | -1.65 | -163 / -141 / -216 | 16 · 44% · -27.9 | 84 · 39% · -161.3 ⚠ | 161 · 34% · -309.6 ⚠ | 41 · 49% · -17.1 | 29 · 38% · -31.5 |
| 30–60 | 301 · 59% · +163.0 | +0.54 | -4 / +121 / +46 | 19 · 74% · +44.1 | 99 · 53% · -20.3 | 134 · 61% · +117.7 | 39 · 56% · +15.5 | 29 · 72% · +50.2 ✓ |
| 1–2 h | 211 · 75% · +685.1 ✓ strong | +3.25 | +269 / +237 / +179 | 10 · 70% · +25.6 | 58 · 76% · +178.7 ✓ | 106 · 74% · +314.2 ✓ | 31 · 77% · +117.7 ✓ | 16 · 81% · +74.5 |
| 2–4 h | 86 · 97% · +543.0 ✓ strong | +6.31 | +191 / +192 / +160 | – | 34 · 91% · +181.4 ✓ | 36 · 100% · +253.7 ✓ | 10 · 100% · +60.1 | 6 · 100% · +47.8 |
| 4 h+ | 10 · 90% · +77.8 | +7.78 | +24 / +29 / +25 | – | 1 · 100% · +6.7 | 7 · 100% · +67.3 | 1 · 100% · +4.0 | 1 · 0% · -0.2 |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 567 | 37% | 51% | 8% | 4% | 35 |
| 1 | 151 | 23% | 52% | 22% | 3% | 30 |
| 2 | 93 | 30% | 43% | 23% | 4% | 20 |
| 3–4 | 118 | 33% | 34% | 29% | 4% | 20 |
| 5–8 | 155 | 30% | 39% | 29% | 3% | 20 |
| 9–16 | 84 | 32% | 37% | 29% | 2% | 22 |
| 17–32 | 15 | 27% | 33% | 33% | 7% | 20 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 415 · 51% · +135.6 · live 13 · 38% · -25.9 | 200 · 54% · +54.8 (+58 / -0 / -3) · live 7 · 57% · -2.7 | 124 · 51% · +71.2 ✓ (+28 / +29 / +14) · live 4 · 25% · -12.7 | 53 · 49% · +26.3 (-16 / +11 / +31) · live 2 · 0% · -10.5 | 38 · 39% · -16.6 (-13 / +14 / -17) · live – |
| London 03:00–09:30 | 384 · 49% · -94.8 · live 21 · 43% · -27.8 | 193 · 53% · +28.7 (-29 / +20 / +38) · live 11 · 55% · +1.2 | 111 · 43% · -59.4 (-39 / +1 / -22) · live 5 · 40% · -11.0 | 52 · 44% · -56.8 (-50 / -13 / +6) · live 4 · 0% · -23.1 | 28 · 46% · -7.3 (+14 / -24 / +2) · live 1 · 100% · +5.1 |
| NY 09:30–16:00 | 384 · 53% · -49.6 · live 24 · 58% · +11.1 | 174 · 54% · -13.3 (+41 / +35 / -89) · live 10 · 60% · -2.2 | 127 · 53% · +20.2 (+13 / +10 / -3) · live 8 · 50% · +0.8 | 50 · 50% · -28.9 (-41 / +20 / -8) · live 3 · 100% · +23.7 | 33 · 48% · -27.7 (-22 / +23 / -29) · live 3 · 33% · -11.2 |

## Flags (weak cells: ≥ 20 sim setups, negative in all thirds)

- MGC 3m · HTF candles flip→entry 2 HTF EMA20 Pierce: 30 · 23% · -49.1, thirds -18 / -22 / -9
- MGC 3m · HTF candles flip→entry 3–4 HTF EMA9 Pierce: 21 · 33% · -29.7, thirds -24 / -2 / -4
- MGC 3m · London 03:00–09:30 flip candle HTF candles after the flip: 153 · 32% · -233.0, thirds -93 / -81 / -59
- MGC 3m · Hold time < 15 min: 491 · 12% · -1751.9, thirds -691 / -554 / -506
- MGC 3m · Hold time < 15 min HTF CBC Flip: 66 · 6% · -305.7, thirds -144 / -101 / -61
- MGC 3m · Hold time < 15 min LTF EMA20 Pierce: 240 · 8% · -941.2, thirds -329 / -285 / -327
- MGC 3m · Hold time < 15 min HTF EMA9 Pierce: 105 · 16% · -354.6, thirds -183 / -78 / -94
- MGC 3m · Hold time < 15 min HTF EMA20 Pierce: 80 · 26% · -150.4, thirds -36 / -90 / -25
- MES 3m · HTF candles flip→entry flip candle (0) HTF EMA9 Pierce: 69 · 41% · -73.8, thirds -22 / -31 / -21
- MES 3m · HTF candles flip→entry flip candle (0) HTF EMA20 Pierce: 56 · 48% · -20.5, thirds -10 / -7 / -4
- MES 3m · HTF candles flip→entry 1 HTF EMA9 Pierce: 45 · 40% · -66.8, thirds -22 / -24 / -21
- MES 3m · HTF candles flip→entry 5–8: 237 · 45% · -88.9, thirds -35 / -52 / -2
- MES 3m · HTF candles flip→entry 5–8 HTF EMA9 Pierce: 57 · 44% · -47.4, thirds -21 / -10 / -17
- MES 3m · London 03:00–09:30 flip candle HTF candles after the flip: 239 · 48% · -72.4, thirds -17 / -29 / -26
- MES 3m · Hold time < 15 min: 623 · 24% · -1635.6, thirds -615 / -589 / -431
- MES 3m · Hold time < 15 min HTF CBC Flip: 70 · 29% · -235.7, thirds -108 / -65 / -63
- MES 3m · Hold time < 15 min LTF EMA20 Pierce: 330 · 19% · -952.7, thirds -332 / -354 / -267
- MES 3m · Hold time < 15 min HTF EMA9 Pierce: 136 · 27% · -313.6, thirds -134 / -103 / -77
- MES 3m · Hold time < 15 min HTF EMA20 Pierce: 87 · 33% · -133.6, thirds -42 / -67 / -25
- MGC 2m · HTF candles flip→entry 1 HTF EMA9 Pierce: 38 · 39% · -35.6, thirds -18 / -12 / -6
- MGC 2m · Asia 18:00–03:00 9+ HTF candles after the flip: 40 · 38% · -41.9, thirds -21 / -6 / -15
- MGC 2m · Hold time < 15 min: 677 · 30% · -1436.4, thirds -601 / -363 / -473
- MGC 2m · Hold time < 15 min HTF CBC Flip: 161 · 27% · -481.4, thirds -231 / -126 / -125
- MGC 2m · Hold time < 15 min LTF EMA20 Pierce: 286 · 26% · -650.0, thirds -268 / -188 / -194
- MGC 2m · Hold time < 15 min HTF EMA9 Pierce: 146 · 34% · -205.5, thirds -51 / -48 / -107
- MGC 2m · Hold time < 15 min HTF EMA20 Pierce: 84 · 40% · -99.4, thirds -52 / -2 / -46
- MES 2m · HTF candles flip→entry 9–16: 105 · 41% · -78.2, thirds -35 / -27 / -16
- MES 2m · HTF candles flip→entry 9–16 LTF EMA20 Pierce: 68 · 40% · -52.0, thirds -27 / -23 / -2
- MES 2m · Asia 18:00–03:00 9+ HTF candles after the flip: 45 · 42% · -27.9, thirds -8 / -6 / -14
- MES 2m · NY 09:30–16:00 9+ HTF candles after the flip: 36 · 36% · -57.2, thirds -20 / -7 / -31
- MES 2m · Hold time < 15 min: 520 · 27% · -1139.3, thirds -422 / -276 / -441
- MES 2m · Hold time < 15 min HTF CBC Flip: 134 · 34% · -322.5, thirds -76 / -119 / -127
- MES 2m · Hold time < 15 min LTF EMA20 Pierce: 234 · 23% · -555.4, thirds -234 / -96 / -226
- MES 2m · Hold time < 15 min HTF EMA9 Pierce: 101 · 28% · -192.6, thirds -58 / -57 / -78
- MES 2m · Hold time < 15 min HTF EMA20 Pierce: 51 · 29% · -68.8, thirds -55 / -5 / -10
- MES 2m · Hold time 15–30 HTF CBC Flip: 139 · 46% · -87.8, thirds -58 / -8 / -22
- MGC 5m · HTF candles flip→entry 1 HTF EMA9 Pierce: 27 · 30% · -43.1, thirds -4 / -11 / -27
- MGC 5m · HTF candles flip→entry 1 HTF EMA20 Pierce: 24 · 46% · -24.4, thirds -9 / -15 / -1
- MGC 5m · HTF candles flip→entry 2 LTF EMA20 Pierce: 64 · 45% · -39.6, thirds -21 / -2 / -16
- MGC 5m · HTF candles flip→entry 9–16 HTF EMA9 Pierce: 26 · 27% · -52.7, thirds -34 / -5 / -13
- MGC 5m · London 03:00–09:30 9+ HTF candles after the flip: 38 · 42% · -54.9, thirds -23 / -11 / -21
- MGC 5m · Hold time < 15 min: 337 · 23% · -1238.4, thirds -563 / -321 / -355
- MGC 5m · Hold time < 15 min HTF CBC Flip: 74 · 27% · -267.6, thirds -71 / -31 / -166
- MGC 5m · Hold time < 15 min LTF EMA20 Pierce: 157 · 22% · -645.0, thirds -341 / -181 / -123
- MGC 5m · Hold time < 15 min HTF EMA9 Pierce: 63 · 17% · -229.4, thirds -93 / -79 / -58
- MGC 5m · Hold time < 15 min HTF EMA20 Pierce: 43 · 33% · -96.4, thirds -58 / -30 / -8
- MGC 5m · Hold time 15–30: 325 · 38% · -625.0, thirds -144 / -230 / -250
- MGC 5m · Hold time 15–30 HTF CBC Flip: 84 · 40% · -164.2, thirds -44 / -61 / -58
- MGC 5m · Hold time 15–30 LTF EMA20 Pierce: 158 · 38% · -305.6, thirds -63 / -134 / -109
- MGC 5m · Hold time 15–30 HTF EMA9 Pierce: 46 · 33% · -110.6, thirds -44 / -17 / -49
- MES 5m · HTF candles flip→entry 3–4: 118 · 41% · -102.1, thirds -23 / -57 / -22
- MES 5m · HTF candles flip→entry 3–4 LTF EMA20 Pierce: 76 · 41% · -73.2, thirds -13 / -36 / -24
- MES 5m · HTF candles flip→entry 3–4 HTF EMA9 Pierce: 29 · 41% · -21.5, thirds -13 / -8 / -1
- MES 5m · Hold time < 15 min: 260 · 21% · -958.3, thirds -372 / -311 / -275
- MES 5m · Hold time < 15 min HTF CBC Flip: 38 · 13% · -227.0, thirds -84 / -54 / -89
- MES 5m · Hold time < 15 min LTF EMA20 Pierce: 132 · 19% · -544.5, thirds -243 / -173 / -128
- MES 5m · Hold time < 15 min HTF EMA9 Pierce: 64 · 31% · -114.2, thirds -26 / -56 / -32
- MES 5m · Hold time < 15 min HTF EMA20 Pierce: 26 · 19% · -72.7, thirds -20 / -27 / -26
- MES 5m · Hold time 15–30: 315 · 37% · -519.4, thirds -163 / -141 / -216
- MES 5m · Hold time 15–30 HTF CBC Flip: 84 · 39% · -161.3, thirds -79 / -7 / -75
- MES 5m · Hold time 15–30 LTF EMA20 Pierce: 161 · 34% · -309.6, thirds -86 / -94 / -130
