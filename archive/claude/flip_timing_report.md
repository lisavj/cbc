# Flip timing study — weekly check Wed 10/28/2026 18:20 ET (summary)

## Since last week (vs the first run 10/28 09:20 ET)

Note: this run fired the same day as the first run (Wed 10/28 evening), so it **does not count as a new weekly check** — candidates stay at 1 of 3. MES 3m sim now uses the v10.42 base exits (the first run used the older 1.3 / 2.0 exits), so its numbers shifted for that reason; other charts only gained the 10/28 session.

- **MGC 3m:** median flip→entry 18 min (live 30). Weak HTF EMA20 Pierce at 2 candles (27 · −52.0) and HTF EMA9 Pierce at 3–4 (20 · −26.0) still flagged. Live 36 setups (was 32).
- **MES 3m:** median flip→entry 21. **5–8 HTF candles after the flip still weak: 224 · −88.0, thirds −27 / −52 / −8** (was 228 · −99.7); the weak part moved from LTF EMA20 (now 140 · −61.4, mixed thirds) to HTF EMA9 Pierce (54 · −39.6, all thirds). HTF EMA9 Pierce 1 candle after the flip still weak (44 · −71.6); new weak: HTF EMA9 and HTF EMA20 Pierce on the flip candle (68 · −63.0; 55 · −17.0). 2 candles now strong (131 · +76.8). Flip candle −0.11 → +0.01/setup. **Live:** flip-candle entries 24 · +10.7 vs later entries 39 · −69.1 (was 20 · +38.3 vs 37 · −75.6; tonight's 4 flip-candle setups lost −27.6). Live in the 5–8 bucket: 7 · +3.0 — not negative, < 10.
- **MGC 2m:** median 6 min (live 14). Flip candle +267.8 (thirds −26 / +138 / +155, not "strong"); 3–4 candles strong (+83.4). Live 69 (was 60).
- **MES 2m:** median 10 min. **9–16 HTF candles still weak: 97 · −64.4, thirds −35 / −27 / −3**; live 7 · −13.9 (needs ≥ 10). 1 candle still weak (106 · −10.2). Live flip-candle entries 36 · −83.1. Live 74 (was 71).
- **MGC 5m:** median 30 min. Flip candle no longer "strong" (508 · +78.6, thirds +10 / +89 / −21). HTF EMA9 Pierce at 1 and 9–16 candles still weak; new weak HTF EMA20 Pierce at 1 candle (21 · −18.1). Live 21 (no new).
- **MES 5m:** median 25 min (live 15). **3–4 HTF candles still weak: 111 · −95.7, thirds −23 / −53 / −21** (mostly LTF EMA20, 71 · −71.3); live 3 · +8.4. Live 33 (was 31).

**Candidates:** MES 3m no new pierce setups 5–8 HTF candles after the flip (sim holds, live 7 · +3.0); MES 2m no new setups 9–16 HTF candles after the flip (sim holds, live 7 · −13.9); MES 5m no new pierce setups 3–4 HTF candles after the flip (sim holds, live 3 · +8.4). **Verdict: no change.** None has 3 weekly checks or ≥ 10 live setups. A "max HTF candles since the flip" rule would need a CBC Pine change. Hold-time buckets describe outcomes and are not filters. No Pine or server change made.

---

# Flip timing — entry and exit relative to the HTF CBC flip — Wed 10/28/2026 18:22 ET

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

## MGC 3m (HTF 15m) — sim 01/05 → 10/28, 1140 setups · live 36 setups (36 matched to bars)

Median minutes — sim: flip→entry 18, hold 18, flip→exit 48 · live: flip→entry 30, hold 12, flip→exit 57

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 21, HTF EMA9 Pierce 36, HTF EMA20 Pierce 28

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 485 · 43% · +25.5 | +0.05 | +22 / -36 / +39 | 11 · 64% · +13.8 | 202 · 47% · +90.3 ✓ | 172 · 40% · -18.8 | 59 · 37% · -63.7 | 52 · 46% · +17.6 |
| 1 | 221 · 43% · +70.7 | +0.32 | +138 / -29 / -38 | 7 · 29% · -4.8 | – | 157 · 43% · +47.0 | 32 · 38% · -19.0 | 32 · 50% · +42.7 |
| 2 | 103 · 40% · +27.8 | +0.27 | +74 / +8 / -54 | 4 · 100% · +8.0 | – | 58 · 52% · +100.2 | 18 · 33% · -20.5 | 27 · 19% · -52.0 ⚠ |
| 3–4 | 124 · 48% · +53.4 | +0.43 | +57 / -21 / +18 | 6 · 0% · -19.1 | – | 81 · 46% · +49.9 ✓ | 20 · 35% · -26.0 ⚠ | 23 · 65% · +29.5 |
| 5–8 | 147 · 44% · +8.7 | +0.06 | -72 / +67 / +14 | 5 · 60% · +6.0 | – | 80 · 42% · +5.8 | 45 · 44% · -9.6 | 22 · 45% · +12.6 |
| 9–16 | 53 · 40% · +18.4 | +0.35 | -8 / +8 / +19 | 3 · 0% · -11.8 | – | 26 · 27% · -26.2 | 16 · 56% · +31.9 | 11 · 45% · +12.7 |
| 17–32 | 7 · 29% · -4.5 | -0.65 | +8 / -13 / +0 | – | – | 4 · 25% · +3.4 | 2 · 50% · -6.0 | 1 · 0% · -2.0 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 475 · 12% · -1693.3 ⚠ weak | -3.56 | -661 / -554 / -478 | 19 · 16% · -52.0 | 64 · 6% · -292.7 ⚠ | 231 · 8% · -900.5 ⚠ | 103 · 17% · -346.8 ⚠ | 77 · 25% · -153.3 ⚠ |
| 15–30 | 264 · 41% · -142.2 | -0.54 | +77 / -128 / -91 | 6 · 67% · -0.8 | 52 · 37% · -50.0 | 135 · 44% · -41.8 | 36 · 36% · -39.6 | 41 · 44% · -10.9 |
| 30–60 | 258 · 75% · +776.5 ✓ strong | +3.01 | +278 / +275 / +223 | 7 · 71% · +22.7 | 56 · 79% · +203.2 ✓ | 133 · 72% · +363.0 ✓ | 35 · 83% · +99.3 ✓ | 34 · 71% · +110.9 ✓ |
| 1–2 h | 124 · 90% · +989.1 ✓ strong | +7.98 | +397 / +345 / +247 | 3 · 100% · +15.7 | 27 · 89% · +191.5 ✓ | 66 · 88% · +551.2 ✓ | 16 · 100% · +143.0 | 15 · 87% · +103.4 |
| 2–4 h | 17 · 100% · +218.4 | +12.85 | +95 / +27 / +97 | 1 · 100% · +6.4 | 3 · 100% · +38.3 | 11 · 100% · +138.0 | 2 · 100% · +31.1 | 1 · 100% · +11.0 |
| 4 h+ | 2 · 100% · +51.4 | +25.68 | +33 / +19 / +0 | – | – | 2 · 100% · +51.4 | – | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 485 | 48% | 43% | 7% | 2% | 21 |
| 1 | 221 | 39% | 39% | 20% | 1% | 18 |
| 2 | 103 | 32% | 37% | 31% | 0% | 18 |
| 3–4 | 124 | 35% | 40% | 23% | 2% | 15 |
| 5–8 | 147 | 34% | 36% | 30% | 0% | 15 |
| 9–16 | 53 | 42% | 32% | 26% | 0% | 9 |
| 17–32 | 7 | 29% | 29% | 43% | 0% | 9 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 563 · 46% · +282.6 · live 10 · 50% · +13.4 | 240 · 45% · +85.9 (+70 / -6 / +22) · live 4 · 75% · +12.9 | 216 · 48% · +152.9 (+137 / +29 / -14) · live 4 · 25% · -4.2 | 73 · 47% · +18.4 (-34 / +23 / +29) · live 1 · 100% · +6.6 | 34 · 41% · +25.5 (+29 / -9 / +6) · live 1 · 0% · -1.8 |
| London 03:00–09:30 | 348 · 36% · -202.2 · live 11 · 27% · -19.9 | 149 · 33% · -218.5 ⚠ (-73 / -130 / -15) · live 3 · 33% · -6.8 | 147 · 37% · +3.5 (+103 / -78 / -21) · live 7 · 29% · -8.0 | 35 · 43% · +11.8 (-20 / +34 / -3) · live – | 17 · 35% · +1.0 (-21 / +20 / +2) · live 1 · 0% · -5.0 |
| NY 09:30–16:00 | 229 · 46% · +119.4 · live 15 · 53% · -1.5 | 96 · 53% · +158.1 ✓ (+25 / +101 / +32) · live 4 · 75% · +7.8 | 85 · 42% · -4.6 (+29 / +6 / -39) · live 6 · 50% · -3.6 | 39 · 38% · -21.5 (-19 / +10 / -12) · live 4 · 50% · -0.6 | 9 · 33% · -12.6 (-8 / -16 / +11) · live 1 · 0% · -5.0 |

## MES 3m (HTF 15m) — sim 01/05 → 10/28, 1669 setups · live 63 setups (63 matched to bars)

Median minutes — sim: flip→entry 21, hold 21, flip→exit 60 · live: flip→entry 21, hold 18, flip→exit 51

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 33, HTF EMA9 Pierce 45, HTF EMA20 Pierce 38

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 662 · 53% · +9.9 | +0.01 | -90 / -65 / +165 | 24 · 54% · +10.7 | 306 · 57% · +82.5 | 233 · 52% · +7.3 | 68 · 41% · -63.0 ⚠ | 55 · 49% · -17.0 ⚠ |
| 1 | 266 · 44% · -61.4 | -0.23 | +100 / -153 / -9 | 13 · 23% · -26.8 | – | 193 · 46% · +4.5 | 44 · 39% · -71.6 ⚠ | 29 · 45% · +5.7 |
| 2 | 131 · 53% · +76.8 ✓ strong | +0.59 | +42 / +9 / +26 | 3 · 33% · -5.9 | – | 93 · 53% · +49.3 ✓ | 25 · 56% · +25.6 ✓ | 13 · 46% · +1.9 |
| 3–4 | 225 · 51% · +35.0 | +0.16 | +96 / -12 / -49 | 12 · 17% · -38.8 | – | 144 · 51% · +10.2 | 50 · 50% · +23.1 | 31 · 48% · +1.7 |
| 5–8 | 224 · 45% · -88.0 ⚠ weak | -0.39 | -27 / -52 / -8 | 7 · 57% · +3.0 | – | 140 · 44% · -61.4 | 54 · 44% · -39.6 ⚠ | 30 · 53% · +13.0 |
| 9–16 | 136 · 49% · +11.7 | +0.09 | +10 / +33 / -31 | 4 · 50% · -0.6 | – | 93 · 49% · +5.2 | 28 · 50% · +8.1 | 15 · 40% · -1.6 |
| 17–32 | 25 · 60% · +11.2 | +0.45 | +14 / -2 / -1 | – | – | 14 · 64% · +12.7 | 8 · 50% · -2.6 | 3 · 67% · +1.1 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 602 · 24% · -1559.3 ⚠ weak | -2.59 | -580 / -598 / -382 | 28 · 7% · -121.6 | 67 · 30% · -216.0 ⚠ | 317 · 19% · -907.3 ⚠ | 132 · 27% · -305.1 ⚠ | 86 · 34% · -130.9 ⚠ |
| 15–30 | 378 · 45% · -224.7 | -0.59 | +38 / -181 / -81 | 13 · 54% · +7.1 | 72 · 51% · -47.7 | 208 · 40% · -167.6 | 62 · 48% · -14.5 | 36 · 50% · +5.1 |
| 30–60 | 418 · 67% · +618.0 ✓ strong | +1.48 | +304 / +157 / +157 | 16 · 62% · +11.0 | 93 · 58% · +65.8 ✓ | 234 · 71% · +411.5 ✓ | 61 · 67% · +105.0 ✓ | 30 · 63% · +35.7 ✓ |
| 1–2 h | 249 · 86% · +1001.9 ✓ strong | +4.02 | +317 / +331 / +354 | 6 · 100% · +45.1 | 70 · 83% · +253.1 ✓ | 138 · 90% · +609.1 ✓ | 19 · 84% · +70.2 | 22 · 77% · +69.5 ✓ |
| 2–4 h | 21 · 95% · +148.7 ✓ strong | +7.08 | +66 / +38 / +45 | – | 4 · 100% · +27.3 | 13 · 92% · +82.2 | 3 · 100% · +24.4 | 1 · 100% · +14.8 |
| 4 h+ | 1 · 100% · +10.5 | +10.51 | +0 / +11 / +0 | – | – | – | – | 1 · 100% · +10.5 |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 662 | 33% | 50% | 15% | 2% | 27 |
| 1 | 266 | 26% | 39% | 33% | 2% | 18 |
| 2 | 131 | 16% | 48% | 34% | 2% | 24 |
| 3–4 | 225 | 23% | 41% | 34% | 2% | 15 |
| 5–8 | 224 | 23% | 37% | 39% | 1% | 15 |
| 9–16 | 136 | 22% | 40% | 35% | 3% | 18 |
| 17–32 | 25 | 16% | 48% | 36% | 0% | 30 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 611 · 52% · +145.9 · live 13 · 38% · -8.3 | 242 · 53% · +7.9 (-32 / -48 / +88) · live 3 · 67% · +4.2 | 214 · 51% · +117.1 (+110 / -25 / +32) · live 6 · 17% · -13.3 | 82 · 49% · +2.2 (-9 / +11 / -0) · live 4 · 50% · +0.7 | 73 · 51% · +18.7 (+20 / +27 / -28) · live – |
| London 03:00–09:30 | 541 · 46% · -137.6 · live 21 · 38% · -18.3 | 233 · 48% · -52.1 ⚠ (-18 / -31 / -3) · live 8 · 50% · +0.1 | 194 · 45% · -21.7 (+26 / -47 / -0) · live 11 · 27% · -17.5 | 71 · 42% · -23.8 (+1 / -31 / +6) · live – | 43 · 42% · -40.0 ⚠ (-17 / -20 / -3) · live 2 · 50% · -0.9 |
| NY 09:30–16:00 | 517 · 52% · -13.1 · live 29 · 41% · -31.8 | 187 · 57% · +54.1 (-40 / +15 / +79) · live 13 · 54% · +6.3 | 214 · 49% · -45.0 (+102 / -83 / -64) · live 11 · 18% · -40.8 | 71 · 44% · -66.4 ⚠ (-20 / -33 / -14) · live 3 · 67% · +2.3 | 45 · 58% · +44.2 (+21 / +24 / -1) · live 2 · 50% · +0.3 |

## MGC 2m (HTF 10m) — sim 06/01 → 10/28, 1409 setups · live 69 setups (69 matched to bars)

Median minutes — sim: flip→entry 6, hold 16, flip→exit 34 · live: flip→entry 14, hold 22, flip→exit 44

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 22, HTF EMA9 Pierce 28, HTF EMA20 Pierce 12

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 751 · 55% · +267.8 | +0.36 | -26 / +138 / +155 | 30 · 60% · -4.6 | 460 · 52% · +19.8 | 174 · 61% · +193.3 ✓ | 67 · 61% · +44.9 | 50 · 54% · +9.9 |
| 1 | 164 · 47% · +7.6 | +0.05 | +87 / -20 / -60 | 9 · 33% · -9.1 | – | 111 · 48% · +26.2 | 35 · 40% · -29.5 | 18 · 56% · +10.9 |
| 2 | 100 · 49% · -16.9 | -0.17 | +5 / +1 / -23 | 4 · 25% · -4.5 | – | 71 · 52% · +1.5 | 18 · 39% · -6.4 | 11 · 45% · -11.9 |
| 3–4 | 142 · 53% · +83.4 ✓ strong | +0.59 | +37 / +19 / +28 | 7 · 43% · +0.6 | – | 81 · 54% · +60.0 ✓ | 36 · 56% · +30.6 ✓ | 25 · 44% · -7.3 |
| 5–8 | 149 · 48% · +24.6 | +0.16 | -17 / -16 / +58 | 13 · 62% · +10.8 | – | 98 · 49% · +41.0 | 44 · 48% · -9.8 | 7 · 43% · -6.7 |
| 9–16 | 86 · 48% · +4.1 | +0.05 | +2 / -3 / +5 | 2 · 50% · -0.6 | – | 56 · 52% · +16.4 | 24 · 42% · -10.4 ⚠ | 6 · 33% · -1.9 |
| 17–32 | 16 · 31% · -5.0 | -0.31 | -5 / -7 / +8 | 4 · 50% · +8.3 | – | 13 · 31% · +1.3 | 1 · 100% · +0.3 | 2 · 0% · -6.6 |
| 33+ | 1 · 100% · +4.8 | +4.80 | +0 / +0 / +5 | – | – | 1 · 100% · +4.8 | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 635 · 30% · -1335.8 ⚠ weak | -2.10 | -576 / -375 / -385 | 23 · 26% · -51.0 | 154 · 27% · -450.4 ⚠ | 267 · 25% · -621.0 ⚠ | 136 · 35% · -178.1 ⚠ | 78 · 41% · -86.3 ⚠ |
| 15–30 | 381 · 57% · +254.1 ✓ strong | +0.67 | +92 / +67 / +95 | 25 · 60% · +9.9 | 149 · 48% · -36.7 | 175 · 65% · +255.1 ✓ | 38 · 61% · +13.4 | 19 · 58% · +22.3 |
| 30–60 | 313 · 80% · +962.6 ✓ strong | +3.08 | +379 / +298 / +286 | 14 · 64% · +12.2 | 123 · 76% · +315.6 ✓ | 128 · 84% · +468.4 ✓ | 43 · 84% · +138.0 ✓ | 19 · 68% · +40.6 |
| 1–2 h | 79 · 96% · +482.4 ✓ strong | +6.11 | +179 / +123 / +180 | 7 · 86% · +29.8 | 33 · 94% · +184.2 ✓ | 35 · 100% · +241.9 ✓ | 8 · 100% · +46.5 | 3 · 67% · +9.8 |
| 2–4 h | 1 · 100% · +7.1 | +7.07 | +7 / +0 / +0 | – | 1 · 100% · +7.1 | – | – | – |
| 4 h+ | – | – | – | – | – | – | – | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 751 | 33% | 53% | 12% | 2% | 20 |
| 1 | 164 | 26% | 41% | 32% | 1% | 12 |
| 2 | 100 | 29% | 42% | 28% | 1% | 14 |
| 3–4 | 142 | 17% | 42% | 42% | 0% | 10 |
| 5–8 | 149 | 19% | 41% | 40% | 1% | 12 |
| 9–16 | 86 | 26% | 44% | 28% | 2% | 14 |
| 17–32 | 16 | 19% | 19% | 56% | 6% | 7 |
| 33+ | 1 | 0% | 100% | 0% | 0% | 42 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 573 · 51% · +63.9 · live 20 · 50% · -9.3 | 306 · 57% · +141.0 ✓ (+25 / +78 / +39) · live 8 · 62% · -6.0 | 166 · 47% · -12.2 (+17 / -20 / -9) · live 8 · 25% · -10.3 | 62 · 42% · -28.2 (-29 / -7 / +8) · live 3 · 67% · +3.0 | 39 · 38% · -36.7 ⚠ (-21 / -6 / -10) · live 1 · 100% · +4.0 |
| London 03:00–09:30 | 454 · 54% · +221.2 · live 20 · 45% · -8.4 | 235 · 55% · +99.1 (-45 / +14 / +131) · live 9 · 44% · -7.5 | 136 · 53% · +57.6 (+40 / +41 / -24) · live 5 · 40% · -1.3 | 45 · 53% · +32.9 ✓ (+14 / +1 / +18) · live 5 · 60% · +4.8 | 38 · 55% · +31.6 (+8 / -1 / +24) · live 1 · 0% · -4.3 |
| NY 09:30–16:00 | 382 · 51% · +85.2 · live 29 · 59% · +18.5 | 210 · 52% · +27.7 (-5 / +47 / -14) · live 13 · 69% · +8.9 | 104 · 49% · +28.6 (+72 / -22 / -22) · live 7 · 43% · -1.4 | 42 · 52% · +19.8 (-2 / -10 / +32) · live 5 · 60% · +3.0 | 26 · 42% · +9.0 (+9 / -3 / +3) · live 4 · 50% · +8.0 |

## MES 2m (HTF 10m) — sim 06/01 → 10/28, 1149 setups · live 74 setups (74 matched to bars)

Median minutes — sim: flip→entry 10, hold 18, flip→exit 40 · live: flip→entry 11, hold 13, flip→exit 30

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 32, HTF EMA9 Pierce 38, HTF EMA20 Pierce 26

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 566 · 51% · -115.9 | -0.20 | -37 / +70 / -149 | 36 · 33% · -83.1 | 396 · 51% · -78.5 | 110 · 50% · -20.3 | 39 · 51% · -8.2 | 21 · 48% · -8.9 |
| 1 | 106 · 44% · -10.2 ⚠ weak | -0.10 | -1 / -7 / -2 | 9 · 44% · -6.8 | – | 76 · 41% · -24.8 ⚠ | 17 · 41% · -8.1 | 13 · 69% · +22.7 |
| 2 | 79 · 48% · -22.4 | -0.28 | -37 / -1 / +15 | 3 · 33% · -4.4 | – | 53 · 49% · -20.2 | 14 · 36% · -12.3 | 12 · 58% · +10.0 |
| 3–4 | 128 · 47% · +31.4 | +0.25 | -19 / +22 / +28 | 10 · 30% · -8.5 | – | 76 · 50% · +20.8 | 36 · 44% · +5.4 | 16 · 38% · +5.2 |
| 5–8 | 158 · 53% · +31.3 | +0.20 | +15 / +23 / -6 | 8 · 50% · -4.0 | – | 108 · 52% · +9.5 | 39 · 62% · +31.3 | 11 · 36% · -9.5 |
| 9–16 | 97 · 41% · -64.4 ⚠ weak | -0.66 | -35 / -27 / -3 | 7 · 29% · -13.9 | – | 62 · 39% · -46.3 | 24 · 58% · +7.6 | 11 · 18% · -25.7 |
| 17–32 | 14 · 43% · -14.8 | -1.06 | -4 / +8 / -19 | 1 · 0% · -1.2 | – | 12 · 33% · -18.5 | 2 · 100% · +3.7 | – |
| 33+ | 1 · 0% · -5.0 | -5.00 | +0 / +0 / -5 | – | – | 1 · 0% · -5.0 | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 484 · 28% · -1013.8 ⚠ weak | -2.09 | -397 / -247 / -370 | 39 · 13% · -155.2 | 126 · 33% · -304.1 ⚠ | 217 · 24% · -478.0 ⚠ | 92 · 29% · -171.4 ⚠ | 49 · 31% · -60.3 |
| 15–30 | 339 · 53% · +9.9 | +0.03 | -3 / +34 / -21 | 23 · 48% · -4.7 | 131 · 45% · -93.5 ⚠ | 143 · 53% · +22.1 | 42 · 67% · +43.6 ✓ | 23 · 70% · +37.7 ✓ |
| 30–60 | 244 · 73% · +519.2 ✓ strong | +2.13 | +181 / +188 / +151 | 10 · 90% · +35.5 | 103 · 69% · +189.9 ✓ | 101 · 75% · +224.6 ✓ | 29 · 86% · +86.4 ✓ | 11 · 64% · +18.4 |
| 1–2 h | 80 · 82% · +301.5 ✓ strong | +3.77 | +94 / +109 / +99 | 2 · 50% · +2.5 | 34 · 82% · +116.2 ✓ | 37 · 81% · +126.5 ✓ | 8 · 100% · +60.8 | 1 · 0% · -2.0 |
| 2–4 h | 2 · 100% · +13.1 | +6.55 | +7 / +6 / +0 | – | 2 · 100% · +13.1 | – | – | – |
| 4 h+ | – | – | – | – | – | – | – | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 566 | 30% | 48% | 21% | 1% | 20 |
| 1 | 106 | 22% | 41% | 37% | 1% | 18 |
| 2 | 79 | 18% | 39% | 43% | 0% | 14 |
| 3–4 | 128 | 16% | 44% | 40% | 0% | 16 |
| 5–8 | 158 | 18% | 44% | 37% | 0% | 14 |
| 9–16 | 97 | 23% | 37% | 40% | 0% | 12 |
| 17–32 | 14 | 29% | 29% | 36% | 7% | 17 |
| 33+ | 1 | 100% | 0% | 0% | 0% | 30 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 468 · 49% · -121.4 · live 17 · 18% · -50.7 | 235 · 51% · -70.1 (+19 / -7 / -82) · live 9 · 22% · -27.6 | 123 · 45% · -30.0 (-16 / -19 / +5) · live 6 · 17% · -16.1 | 69 · 52% · +5.6 (-11 / -1 / +17) · live 1 · 0% · -2.0 | 41 · 41% · -27.0 ⚠ (-8 / -3 / -16) · live 1 · 0% · -5.0 |
| London 03:00–09:30 | 362 · 48% · -100.8 · live 25 · 52% · +0.5 | 183 · 48% · -88.0 (-62 / +22 / -48) · live 12 · 50% · -9.4 | 97 · 43% · -27.6 (-12 / -21 / +5) · live 7 · 57% · +7.9 | 45 · 60% · +30.3 (+26 / +10 / -6) · live 1 · 100% · +2.4 | 37 · 43% · -15.6 (-11 / -9 / +5) · live 5 · 40% · -0.4 |
| NY 09:30–16:00 | 319 · 51% · +52.2 · live 32 · 31% · -71.7 | 148 · 54% · +42.2 (+7 / +56 / -20) · live 15 · 27% · -46.1 | 93 · 52% · +56.4 (-29 / +55 / +31) · live 9 · 33% · -11.6 | 44 · 48% · -4.7 (-1 / +13 / -16) · live 6 · 50% · -4.3 | 34 · 38% · -41.6 ⚠ (-20 / -7 / -15) · live 2 · 0% · -9.8 |

## MGC 5m (HTF 25m) — sim 01/05 → 10/28, 1134 setups · live 21 setups (21 matched to bars)

Median minutes — sim: flip→entry 30, hold 22, flip→exit 75 · live: flip→entry 30, hold 30, flip→exit 95

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 70, HTF EMA9 Pierce 70, HTF EMA20 Pierce 30

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 508 · 55% · +78.6 | +0.15 | +10 / +89 / -21 | 8 · 50% · -3.9 | 310 · 56% · +93.9 | 110 · 49% · -50.8 | 47 · 64% · +53.4 | 41 · 49% · -18.0 |
| 1 | 154 · 51% · +30.4 | +0.20 | -47 / +9 / +68 | 3 · 67% · +3.2 | – | 106 · 57% · +91.6 | 27 · 30% · -43.1 ⚠ | 21 · 48% · -18.1 ⚠ |
| 2 | 87 · 46% · -39.5 | -0.45 | -53 / +19 / -6 | 1 · 100% · +4.8 | – | 63 · 46% · -32.6 | 14 · 29% · -32.5 | 10 · 70% · +25.6 |
| 3–4 | 145 · 50% · -37.1 | -0.26 | -87 / +58 / -7 | 5 · 40% · -3.7 | – | 103 · 50% · -36.8 | 26 · 58% · +23.5 | 16 · 38% · -23.7 |
| 5–8 | 139 · 47% · -49.4 | -0.36 | +55 / -31 / -74 | 3 · 33% · -1.6 | – | 98 · 46% · -44.7 | 29 · 48% · -10.2 | 12 · 50% · +5.5 |
| 9–16 | 90 · 51% · -19.1 | -0.21 | -43 / +26 / -2 | 1 · 0% · -1.7 | – | 60 · 58% · +19.8 | 25 · 28% · -45.7 ⚠ | 5 · 80% · +6.8 |
| 17–32 | 11 · 45% · -11.2 | -1.01 | -11 / +14 / -13 | – | – | 8 · 50% · -5.3 | 2 · 0% · -14.0 | 1 · 100% · +8.2 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 328 · 24% · -1199.3 ⚠ weak | -3.66 | -556 / -295 / -348 | 7 · 29% · -14.3 | 72 · 26% · -265.6 ⚠ | 153 · 22% · -620.8 ⚠ | 61 · 18% · -216.8 ⚠ | 42 · 33% · -96.1 ⚠ |
| 15–30 | 308 · 39% · -575.5 ⚠ weak | -1.87 | -172 / -162 / -241 | 3 · 33% · -3.3 | 79 · 43% · -130.5 ⚠ | 151 · 38% · -298.2 ⚠ | 46 · 33% · -110.6 ⚠ | 32 · 44% · -36.2 |
| 30–60 | 271 · 68% · +470.3 ✓ strong | +1.74 | +152 / +202 / +116 | 5 · 20% · -18.0 | 80 · 68% · +130.6 ✓ | 140 · 68% · +238.7 ✓ | 35 · 71% · +74.1 | 16 · 69% · +26.8 |
| 1–2 h | 168 · 85% · +801.4 ✓ strong | +4.77 | +257 / +261 / +283 | 6 · 100% · +32.6 | 54 · 78% · +186.0 ✓ | 76 · 86% · +393.0 ✓ | 24 · 96% · +145.9 ✓ | 14 · 93% · +76.5 |
| 2–4 h | 56 · 98% · +417.9 ✓ strong | +7.46 | +142 / +141 / +135 | – | 25 · 96% · +173.4 ✓ | 26 · 100% · +205.0 ✓ | 3 · 100% · +24.3 | 2 · 100% · +15.2 |
| 4 h+ | 3 · 100% · +37.9 | +12.63 | +0 / +38 / +0 | – | – | 2 · 100% · +23.4 | 1 · 100% · +14.4 | – |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 508 | 42% | 51% | 4% | 4% | 25 |
| 1 | 154 | 34% | 44% | 18% | 4% | 25 |
| 2 | 87 | 47% | 43% | 7% | 3% | 15 |
| 3–4 | 145 | 41% | 43% | 13% | 3% | 15 |
| 5–8 | 139 | 41% | 40% | 17% | 2% | 20 |
| 9–16 | 90 | 37% | 40% | 18% | 6% | 15 |
| 17–32 | 11 | 55% | 45% | 0% | 0% | 15 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 434 · 50% · -97.1 · live 6 · 33% · -15.7 | 200 · 55% · +53.8 (+58 / +57 / -61) · live 2 · 0% · -13.9 | 154 · 47% · -103.8 (-99 / +20 / -24) · live 3 · 67% · +3.2 | 44 · 45% · -13.7 (+0 / -2 / -12) · live 1 · 0% · -5.0 | 36 · 44% · -33.4 (-54 / +12 / +8) · live – |
| London 03:00–09:30 | 369 · 53% · +85.0 · live 7 · 29% · -13.4 | 160 · 56% · +46.9 (-30 / +36 / +40) · live 2 · 50% · -1.3 | 130 · 56% · +110.6 (-35 / +87 / +59) · live 3 · 33% · -8.4 | 42 · 43% · -24.1 (+29 / -31 / -22) · live 1 · 0% · -2.0 | 37 · 43% · -48.5 ⚠ (-16 / -18 / -14) · live 1 · 0% · -1.7 |
| NY 09:30–16:00 | 331 · 51% · -35.1 · live 8 · 75% · +26.1 | 148 · 52% · -22.1 ⚠ (-18 / -4 / -0) · live 4 · 75% · +11.2 | 102 · 45% · -53.1 (-53 / -21 / +21) · live 3 · 67% · +9.5 | 53 · 51% · -11.6 (+26 / +2 / -41) · live 1 · 100% · +5.4 | 28 · 68% · +51.7 (+15 / +45 / -9) · live – |

## MES 5m (HTF 25m) — sim 01/05 → 10/28, 1154 setups · live 33 setups (33 matched to bars)

Median minutes — sim: flip→entry 25, hold 30, flip→exit 80 · live: flip→entry 15, hold 30, flip→exit 60

Median flip→entry by trigger (sim, minutes): HTF CBC Flip 0, LTF EMA20 Pierce 55, HTF EMA9 Pierce 60, HTF EMA20 Pierce 30

**Entry: HTF candles since the flip**

| HTF candles flip→entry | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| flip candle (0) | 553 · 54% · +81.2 | +0.15 | +65 / +26 / -10 | 20 · 60% · +8.2 | 303 · 53% · -40.5 | 163 · 53% · +16.5 | 45 · 53% · +28.1 | 42 · 67% · +77.1 ✓ |
| 1 | 149 · 55% · +104.1 | +0.70 | -14 / +90 / +28 | 4 · 0% · -22.5 | – | 99 · 55% · +42.8 | 36 · 56% · +41.3 ✓ | 14 · 57% · +20.0 |
| 2 | 92 · 50% · +18.3 | +0.20 | +39 / +5 / -26 | 2 · 0% · -15.3 | – | 63 · 52% · +35.6 | 17 · 41% · -30.5 | 12 · 50% · +13.2 |
| 3–4 | 111 · 41% · -95.7 ⚠ weak | -0.86 | -23 / -53 / -21 | 3 · 67% · +8.4 | – | 71 · 41% · -71.3 ⚠ | 28 · 43% · -15.2 | 12 · 33% · -9.2 |
| 5–8 | 152 · 47% · -64.4 | -0.42 | -107 / +17 / +25 | 3 · 33% · -7.3 | – | 101 · 43% · -96.5 | 35 · 66% · +56.0 ✓ | 16 · 38% · -24.0 |
| 9–16 | 82 · 45% · -21.5 | -0.26 | -24 / +34 / -31 | – | – | 56 · 45% · -30.6 | 19 · 53% · +10.4 | 7 · 29% · -1.3 |
| 17–32 | 15 · 47% · -14.1 | -0.94 | +7 / -14 / -8 | 1 · 100% · +5.1 | – | 10 · 60% · +8.4 | 3 · 33% · -7.8 | 2 · 0% · -14.7 |
| 33+ | – | – | – | – | – | – | – | – |

**Exit: hold time entry→exit**

| Hold time | Sim all | Sim avg | Sim thirds | Live all | Sim HTF CBC Flip | Sim LTF EMA20 Pierce | Sim HTF EMA9 Pierce | Sim HTF EMA20 Pierce |
|---|---|---|---|---|---|---|---|---|
| < 15 min | 251 · 22% · -913.5 ⚠ weak | -3.64 | -377 / -310 / -226 | 7 · 0% · -39.4 | 35 · 14% · -203.0 ⚠ | 130 · 19% · -538.2 ⚠ | 61 · 33% · -98.0 ⚠ | 25 · 16% · -74.4 ⚠ |
| 15–30 | 308 · 37% · -507.3 ⚠ weak | -1.65 | -150 / -142 / -215 | 8 · 38% · -18.0 | 84 · 39% · -161.3 ⚠ | 154 · 33% · -297.5 ⚠ | 41 · 49% · -17.1 | 29 · 38% · -31.5 |
| 30–60 | 292 · 59% · +147.4 | +0.50 | -7 / +121 / +33 | 11 · 82% · +32.0 | 94 · 52% · -24.7 | 131 · 61% · +111.7 | 39 · 56% · +15.5 | 28 · 71% · +44.9 ✓ |
| 1–2 h | 208 · 75% · +666.0 ✓ strong | +3.20 | +267 / +225 / +174 | 7 · 57% · +1.9 | 56 · 75% · +165.7 ✓ | 105 · 73% · +308.0 ✓ | 31 · 77% · +117.7 ✓ | 16 · 81% · +74.5 |
| 2–4 h | 85 · 96% · +537.6 ✓ strong | +6.32 | +186 / +184 / +168 | – | 33 · 91% · +176.0 ✓ | 36 · 100% · +253.7 ✓ | 10 · 100% · +60.1 | 6 · 100% · +47.8 |
| 4 h+ | 10 · 90% · +77.8 | +7.78 | +24 / +29 / +25 | – | 1 · 100% · +6.7 | 7 · 100% · +67.3 | 1 · 100% · +4.0 | 1 · 0% · -0.2 |

**How setups end, by entry timing (sim)**

| HTF candles flip→entry | N | SL1 | trail (TP1 hit) | HTF flip | 16:00 / other | median hold (min) |
|---|---|---|---|---|---|---|
| flip candle (0) | 553 | 37% | 51% | 8% | 4% | 35 |
| 1 | 149 | 23% | 52% | 21% | 3% | 30 |
| 2 | 92 | 30% | 42% | 23% | 4% | 20 |
| 3–4 | 111 | 33% | 34% | 28% | 5% | 20 |
| 5–8 | 152 | 30% | 38% | 30% | 3% | 20 |
| 9–16 | 82 | 30% | 38% | 29% | 2% | 25 |
| 17–32 | 15 | 27% | 33% | 33% | 7% | 20 |

**Entry timing by session** (sim N · win · net, thirds · live N · win · net)

| Session | All | flip candle HTF candles | 1–4 HTF candles | 5–8 HTF candles | 9+ HTF candles |
|---|---|---|---|---|---|
| Asia 18:00–03:00 | 405 · 51% · +142.1 · live 10 · 50% · -4.4 | 194 · 54% · +53.5 (+57 / -10 / +7) · live 6 · 67% · +5.3 | 120 · 52% · +78.9 ✓ (+32 / +20 / +27) · live 3 · 33% · -4.7 | 53 · 49% · +26.3 (-16 / +19 / +23) · live 1 · 0% · -5.0 | 38 · 39% · -16.6 (-13 / +14 / -17) · live – |
| London 03:00–09:30 | 373 · 48% · -119.0 · live 13 · 38% · -24.7 | 188 · 53% · +16.9 (-36 / +22 / +31) · live 7 · 43% · -6.2 | 108 · 43% · -66.8 (-43 / +5 / -29) · live 4 · 25% · -16.0 | 49 · 43% · -61.8 (-50 / -13 / +1) · live 1 · 0% · -7.6 | 28 · 46% · -7.3 (+14 / -24 / +2) · live 1 · 100% · +5.1 |
| NY 09:30–16:00 | 376 · 53% · -15.3 · live 10 · 60% · +5.6 | 171 · 55% · +10.7 (+44 / +14 / -47) · live 7 · 71% · +9.1 | 124 · 52% · +14.5 (+13 / +18 / -17) · live 2 · 0% · -8.8 | 50 · 50% · -28.9 (-41 / +11 / +1) · live 1 · 100% · +5.3 | 31 · 52% · -11.7 (-18 / +30 / -23) · live – |

## Flags (weak cells: ≥ 20 sim setups, negative in all thirds)

- MGC 3m · HTF candles flip→entry 2 HTF EMA20 Pierce: 27 · 19% · -52.0, thirds -18 / -17 / -17
- MGC 3m · HTF candles flip→entry 3–4 HTF EMA9 Pierce: 20 · 35% · -26.0, thirds -23 / -3 / -0
- MGC 3m · London 03:00–09:30 flip candle HTF candles after the flip: 149 · 33% · -218.5, thirds -73 / -130 / -15
- MGC 3m · Hold time < 15 min: 475 · 12% · -1693.3, thirds -661 / -554 / -478
- MGC 3m · Hold time < 15 min HTF CBC Flip: 64 · 6% · -292.7, thirds -144 / -91 / -58
- MGC 3m · Hold time < 15 min LTF EMA20 Pierce: 231 · 8% · -900.5, thirds -312 / -294 / -295
- MGC 3m · Hold time < 15 min HTF EMA9 Pierce: 103 · 17% · -346.8, thirds -188 / -62 / -97
- MGC 3m · Hold time < 15 min HTF EMA20 Pierce: 77 · 25% · -153.3, thirds -18 / -107 / -28
- MES 3m · HTF candles flip→entry flip candle (0) HTF EMA9 Pierce: 68 · 41% · -63.0, thirds -25 / -32 / -6
- MES 3m · HTF candles flip→entry flip candle (0) HTF EMA20 Pierce: 55 · 49% · -17.0, thirds -10 / -5 / -2
- MES 3m · HTF candles flip→entry 1 HTF EMA9 Pierce: 44 · 39% · -71.6, thirds -35 / -17 / -20
- MES 3m · HTF candles flip→entry 5–8: 224 · 45% · -88.0, thirds -27 / -52 / -8
- MES 3m · HTF candles flip→entry 5–8 HTF EMA9 Pierce: 54 · 44% · -39.6, thirds -19 / -11 / -10
- MES 3m · London 03:00–09:30 flip candle HTF candles after the flip: 233 · 48% · -52.1, thirds -18 / -31 / -3
- MES 3m · London 03:00–09:30 9+ HTF candles after the flip: 43 · 42% · -40.0, thirds -17 / -20 / -3
- MES 3m · NY 09:30–16:00 5–8 HTF candles after the flip: 71 · 44% · -66.4, thirds -20 / -33 / -14
- MES 3m · Hold time < 15 min: 602 · 24% · -1559.3, thirds -580 / -598 / -382
- MES 3m · Hold time < 15 min HTF CBC Flip: 67 · 30% · -216.0, thirds -100 / -53 / -63
- MES 3m · Hold time < 15 min LTF EMA20 Pierce: 317 · 19% · -907.3, thirds -304 / -382 / -221
- MES 3m · Hold time < 15 min HTF EMA9 Pierce: 132 · 27% · -305.1, thirds -133 / -102 / -71
- MES 3m · Hold time < 15 min HTF EMA20 Pierce: 86 · 34% · -130.9, thirds -43 / -61 / -27
- MGC 2m · HTF candles flip→entry 9–16 HTF EMA9 Pierce: 24 · 42% · -10.4, thirds -8 / -0 / -2
- MGC 2m · Asia 18:00–03:00 9+ HTF candles after the flip: 39 · 38% · -36.7, thirds -21 / -6 / -10
- MGC 2m · Hold time < 15 min: 635 · 30% · -1335.8, thirds -576 / -375 / -385
- MGC 2m · Hold time < 15 min HTF CBC Flip: 154 · 27% · -450.4, thirds -217 / -118 / -115
- MGC 2m · Hold time < 15 min LTF EMA20 Pierce: 267 · 25% · -621.0, thirds -257 / -190 / -174
- MGC 2m · Hold time < 15 min HTF EMA9 Pierce: 136 · 35% · -178.1, thirds -49 / -63 / -66
- MGC 2m · Hold time < 15 min HTF EMA20 Pierce: 78 · 41% · -86.3, thirds -52 / -4 / -29
- MES 2m · HTF candles flip→entry 1: 106 · 44% · -10.2, thirds -1 / -7 / -2
- MES 2m · HTF candles flip→entry 1 LTF EMA20 Pierce: 76 · 41% · -24.8, thirds -0 / -10 / -15
- MES 2m · HTF candles flip→entry 9–16: 97 · 41% · -64.4, thirds -35 / -27 / -3
- MES 2m · Asia 18:00–03:00 9+ HTF candles after the flip: 41 · 41% · -27.0, thirds -8 / -3 / -16
- MES 2m · NY 09:30–16:00 9+ HTF candles after the flip: 34 · 38% · -41.6, thirds -20 / -7 / -15
- MES 2m · Hold time < 15 min: 484 · 28% · -1013.8, thirds -397 / -247 / -370
- MES 2m · Hold time < 15 min HTF CBC Flip: 126 · 33% · -304.1, thirds -68 / -104 / -131
- MES 2m · Hold time < 15 min LTF EMA20 Pierce: 217 · 24% · -478.0, thirds -220 / -97 / -161
- MES 2m · Hold time < 15 min HTF EMA9 Pierce: 92 · 29% · -171.4, thirds -54 / -47 / -71
- MES 2m · Hold time 15–30 HTF CBC Flip: 131 · 45% · -93.5, thirds -50 / -9 / -35
- MGC 5m · HTF candles flip→entry 1 HTF EMA9 Pierce: 27 · 30% · -43.1, thirds -4 / -18 / -21
- MGC 5m · HTF candles flip→entry 1 HTF EMA20 Pierce: 21 · 48% · -18.1, thirds -9 / -3 / -6
- MGC 5m · HTF candles flip→entry 9–16 HTF EMA9 Pierce: 25 · 28% · -45.7, thirds -27 / -12 / -6
- MGC 5m · London 03:00–09:30 9+ HTF candles after the flip: 37 · 43% · -48.5, thirds -16 / -18 / -14
- MGC 5m · NY 09:30–16:00 flip candle HTF candles after the flip: 148 · 52% · -22.1, thirds -18 / -4 / -0
- MGC 5m · Hold time < 15 min: 328 · 24% · -1199.3, thirds -556 / -295 / -348
- MGC 5m · Hold time < 15 min HTF CBC Flip: 72 · 26% · -265.6, thirds -71 / -24 / -171
- MGC 5m · Hold time < 15 min LTF EMA20 Pierce: 153 · 22% · -620.8, thirds -341 / -169 / -111
- MGC 5m · Hold time < 15 min HTF EMA9 Pierce: 61 · 18% · -216.8, thirds -86 / -73 / -58
- MGC 5m · Hold time < 15 min HTF EMA20 Pierce: 42 · 33% · -96.1, thirds -58 / -30 / -8
- MGC 5m · Hold time 15–30: 308 · 39% · -575.5, thirds -172 / -162 / -241
- MGC 5m · Hold time 15–30 HTF CBC Flip: 79 · 43% · -130.5, thirds -44 / -54 / -32
- MGC 5m · Hold time 15–30 LTF EMA20 Pierce: 151 · 38% · -298.2, thirds -77 / -102 / -119
- MGC 5m · Hold time 15–30 HTF EMA9 Pierce: 46 · 33% · -110.6, thirds -49 / -13 / -49
- MES 5m · HTF candles flip→entry 3–4: 111 · 41% · -95.7, thirds -23 / -53 / -21
- MES 5m · HTF candles flip→entry 3–4 LTF EMA20 Pierce: 71 · 41% · -71.3, thirds -13 / -31 / -27
- MES 5m · Hold time < 15 min: 251 · 22% · -913.5, thirds -377 / -310 / -226
- MES 5m · Hold time < 15 min HTF CBC Flip: 35 · 14% · -203.0, thirds -84 / -54 / -65
- MES 5m · Hold time < 15 min LTF EMA20 Pierce: 130 · 19% · -538.2, thirds -247 / -176 / -115
- MES 5m · Hold time < 15 min HTF EMA9 Pierce: 61 · 33% · -98.0, thirds -26 / -53 / -19
- MES 5m · Hold time < 15 min HTF EMA20 Pierce: 25 · 16% · -74.4, thirds -20 / -27 / -28
- MES 5m · Hold time 15–30: 308 · 37% · -507.3, thirds -150 / -142 / -215
- MES 5m · Hold time 15–30 HTF CBC Flip: 84 · 39% · -161.3, thirds -79 / -11 / -71
- MES 5m · Hold time 15–30 LTF EMA20 Pierce: 154 · 33% · -297.5, thirds -75 / -89 / -133
