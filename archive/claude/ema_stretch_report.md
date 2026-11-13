# HTF EMA20 / EMA200 stretch study — run 8 -- 2026-11-12 17:09 ET

## Since last run (vs run 7, 11/12 09:58 ET)

The archive now runs to 11/12 after the close, so only today's session was added. Settings sync 11/12 16:47: 0 MISMATCH (newest Pine v10.93; the changes since v10.87 are bot-only and do not touch these replays). The scripts use the BASE exits, so the numbers move only with new bars. Candidate streak count: this is run 8.

- **MGC 3m**: current (VWAP 4) is **+309** (was +312), thirds +161 / +2 / +145.
  - Best with VWAP: **VWAP 4 + HTF EMA20 cap 3 ATR is +62 (unchanged), z +1.1, thirds +33 / +8 / +20 = promising.** This is the 8th promising run in a row and it has never been robust.
  - Best HTF EMA20 instead of VWAP: cap 3 ATR is +75 (unchanged), z +0.6, thirds +60 / +79 / **-64** = noise.
  - Best EMA200 instead of VWAP: cap 5 ATR is +13 (unchanged), z +0.1, Jul–now -41 = noise. Best EMA200 with VWAP: VWAP 4 + EMA200 cap 8 is -13 (unchanged), z -0.5 = worse.
- **MES 3m**: current (no cap) is **+0** (was -1). Best HTF EMA20: cap 3 is +18 (unchanged), z +0.2, thirds -46 / +60 / +4 = noise. Best EMA200: cap 5 is +75 (unchanged), z +0.7, thirds **-15** / +52 / +38 = noise.
- **MGC 2m**: current is **+394** (was +390). Best HTF EMA20: cap 5 is +15 (unchanged), z +0.5, thirds -5 / -2 / +22 = noise. Every EMA200 cap is worse (best is cap 12 at -14; cap 3 is -55, was -51).
- **MES 2m**: current is **-231** (was -215).
  - Best HTF EMA20: cap 1 is +269 (was +253), z +1.8, thirds +88 / **-46** / +227 = noise (Aug still negative).
  - **EMA200 cap 4 ATR is +185 (was +169), z +1.6 (was +1.5), thirds +17 / +1 / +167 = promising.** This is its 4th promising run with 0 robust. Aug is still about flat, so the gain is nearly all Sep–now.
  - EMA200 cap 12 is +39, z +1.6, thirds +4 / +8 / +26 = promising (2nd run, small).
- **Live shadow check.** MGC 3m is the only case with a stretch cap live, so it is the only case with shadows. **17 shadows ended and 16 match a Blocked alert.** The 11/03 02:33 shadow still has no Blocked alert, so its stretch and ER come from the bars. There is 1 new shadow since run 7: 11/12 15:48 S, HTF EMA9 Pierce (late), stretch 18.7 ATR, ER 0.47, ended at 16:00. It arrived only as a 0.5 × TP1 ending (+4.48), which fits the deletion of the second, old-exit alert on 11/12 (data note 2). For consistency with the earlier 0.8 × TP1 rows it counts at the base-exit equivalent: 0.8 × 4.17 + 0.2 × 4.8 = **+4.30**.
  - **Totals: 11/17 wins (65 %), net +18.1, avg +1.06** (was 10/16, +13.8).
  - By VWAP stretch: 4–5 ATR: 2, net -1.9 (1/2). 5–6: 2, net +5.0 (2/2). 6–8: 1, net -5.0. ≥ 8: 12, net +19.9 (8/12).
  - By ER: < 0.30: 7, net +13.7 (5/7). ≥ 0.30: 10, net +4.4 (6/10).
  - By HTF (15m) EMA20 distance (bars, live h20, ATR 14): ≤ 3 ATR: 7, net +8.8 (4/7). > 3 ATR: 10, net +9.3 (7/10). Both groups are about even, so they give no support either way to the "VWAP 4 + HTF EMA20 cap 3" candidate.
  - By EMA200 distance: ≤ 4 ATR: 1, +5.2. 4–8: 10, net +7.3 (6/10). > 8: 6, net +5.6 (4/6).
  - Every group is far below 20. On live data the blocked setups have made +18.1 over 17 (about +1.1 per blocked setup), while the sim still says the filter pays (+83 vs no cap). Live MGC 3m results from 11/09 to 11/12 are partly on the old exits (data note 2).
  - In the sim, today's 06:30 and 07:03 shorts were stretched (9.5 / 8.4 ATR). Neither produced a live Blocked alert, so the live engine probably did not trigger them (the sim matches live only about 50 % of the time).

| Shadow (MGC 3m) | Dir | Trigger | VWAP stretch | ER | HTF EMA20 | EMA200 | Ended | Result |
|---|---|---|---|---|---|---|---|---|
| 11/03 02:33 | S | (no Blocked alert) | 9.1 (bars) | 0.23 (bars) | 4.4 | 7.2 | Breakeven | +4.14 |
| 11/03 04:09 | S | LTF EMA20 Pierce | 9.7 | 0.35 | 4.0 | 7.3 | SL1 | -5.39 |
| 11/04 03:33 | L | LTF EMA20 Pierce | 13.3 | 0.33 | 6.8 | 12.1 | HTF flip | +6.46 |
| 11/04 07:30 | L | HTF CBC Flip | 20.5 | 0.31 | 4.3 | 11.2 | SL1 | -5.41 |
| 11/04 10:45 | L | HTF CBC Flip | 9.5 | 0.38 | 0.4 | 3.2 | Trail | +5.17 |
| 11/04 15:15 | L | HTF CBC Flip | 23.3 | 0.40 | 2.7 | 7.4 | HTF flip | -3.20 |
| 11/05 05:45 | L | HTF CBC Flip | 4.6 | 0.28 | 1.3 | 4.2 | Trail | +4.64 |
| 11/05 06:54 | L | LTF EMA20 Pierce (late) | 6.3 | 0.17 | 2.0 | 5.0 | SL1 | -5.00 |
| 11/09 11:15 | L | HTF CBC Flip | 4.9 | 0.57 | 2.6 | 4.0 | SL1 | -6.51 |
| 11/09 15:48 | L | LTF EMA20 Pierce (late) | 5.9 | 0.17 | 3.7 | 5.1 | 16:00 | +0.20 |
| 11/10 04:03 | S | HTF EMA9 Pierce | 5.1 | 0.68 | 3.8 | 4.5 | Breakeven | +4.80 |
| 11/10 06:18 | S | LTF EMA20 Pierce (late) | 11.7 | 0.19 | 6.0 | 9.4 | HTF flip | -4.30 |
| 11/10 11:03 | S | LTF EMA20 Pierce | 8.5 | 0.10 | 2.8 | 6.0 | HTF flip | +9.36 |
| 11/10 12:48 | S | LTF EMA20 Pierce | 17.5 | 0.11 | 5.5 | 11.6 | Breakeven | +4.65 |
| 11/11 12:27 | S | HTF EMA9 Pierce | 10.9 | 0.30 | 4.2 | 8.4 | HTF flip | +0.50 |
| 11/11 13:00 | S | HTF CBC Flip | 15.5 | 0.85 | 7.4 | 12.2 | Breakeven | +3.66 |
| **11/12 15:48** | S | HTF EMA9 Pierce (late) | 18.7 | 0.47 | 1.5 | 7.1 | 16:00 | +4.30 (0.5× alert: +4.48) |

**Verdict: keep as is for all four cases.** For MGC 3m, "...stretch x ATR per symbol" stays "MGC 3m 4". No variant has been robust on any run.
- MGC 3m candidate: VWAP 4 + HTF EMA20 cap 3 ATR (would need a new CBC input). Promising for the 8th run, unchanged at +62 / z +1.1. The live shadows (17) split about evenly by HTF EMA20 distance and are far short of 20 per group.
- MES 2m candidate: EMA200 cap 4 ATR (would need a new CBC input). Promising for the 4th run, now +185 / z +1.6, but Aug is still +1, so the gain is nearly all Sep–now. There is no live shadow data for it.
- MES 3m and MGC 2m: no stretch cap helps.

---

# HTF EMA20 / EMA200 stretch study — full output -- 2026-11-12 17:09 ET

HTF EMA20 / EMA200 stretch study -- 10/30/2026.

Question: instead of (or on top of) the VWAP stretch cap (MGC 3m 4 ATR), would a cap on the distance from the HTF (15m;
10m on 2m charts) EMA20, or from the EMA200, keep the good setups and drop the bad ones? Distance = close - level in ATR,
signed in the trade direction (+ = stretched in the trade's favour, e.g. a short far below the line).
Simulator: chop_sim.py (CBC-style engine, ER/breakout rule, R5 range gate on 3m, MTF gate on MES 2m), BASE exits
(SL1 1.7 ATR + min 5, TP1 1.7 ATR capped 6, 80 % at TP1, BE, trail 1.7 ATR). HTF EMA20 = live value (forming candle).
~50 % exact match with live setups: compare variants, not totals. z = change / (SD x sqrt(setups changed));
robust = z >= 2 and better in all three thirds; promising = z >= 1 and better in all three thirds.
Usage: python3 ema_stretch_study.py  (needs chop_sim.py + stretch_study.py next to it).

## MGC 3m · current (VWAP cap 4 ATR): 1193 setups, net +309 (thirds +161 / +2 / +145)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 79 | 42% | -32 | -0.40 |
| 0 to 1 | 537 | 50% | +28 | +0.05 |
| 1 to 2 | 493 | 52% | +232 | +0.47 |
| 2 to 3 | 336 | 51% | +144 | +0.43 |
| 3 to 4 | 190 | 49% | -32 | -0.17 |
| 4 to 5 | 86 | 41% | -128 | -1.49 |
| 5 to 6 | 33 | 36% | -40 | -1.21 |
| 6 to 8 | 16 | 75% | +55 | +3.45 |
| 8 to + | 5 | 40% | -2 | -0.47 |

**All setups (no stretch cap) by distance from EMA200 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 225 | 45% | -48 | -0.21 |
| 0 to 2 | 495 | 51% | +153 | +0.31 |
| 2 to 4 | 515 | 50% | +138 | +0.27 |
| 4 to 6 | 299 | 51% | -8 | -0.03 |
| 6 to 8 | 148 | 49% | +1 | +0.00 |
| 8 to 10 | 60 | 43% | -25 | -0.42 |
| 10 to 12 | 15 | 47% | -2 | -0.11 |
| 12 to 15 | 17 | 53% | +11 | +0.66 |
| 15 to + | 1 | 100% | +5 | +4.62 |

**All setups (no stretch cap) by distance from VWAP (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 240 | 43% | -109 | -0.45 |
| 0 to 2 | 501 | 54% | +321 | +0.64 |
| 2 to 3 | 235 | 50% | +31 | +0.13 |
| 3 to 4 | 191 | 52% | +70 | +0.37 |
| 4 to 5 | 168 | 48% | -50 | -0.30 |
| 5 to 6 | 123 | 49% | -60 | -0.49 |
| 6 to 8 | 151 | 50% | +57 | +0.37 |
| 8 to 10 | 85 | 51% | +3 | +0.04 |
| 10 to + | 81 | 41% | -38 | -0.47 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| No stretch cap at all | 1775 | +225 | -83 | -0.6 | -67 / +62 / -78 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| HTF EMA20 cap 1 ATR (instead of VWAP) | 730 | +4 | -305 | -1.9 | -123 / +8 / -190 | worse |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 969 | +183 | -125 | -0.9 | -73 / +29 / -82 | worse |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 1181 | +270 | -38 | -0.3 | -34 / +7 / -12 | worse | · 10/30 adds 02:27 +8.6
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 1350 | +348 | +40 | +0.3 | +36 / +51 / -47 | noise | · 10/30 adds 02:27 +8.6, 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 3 ATR (instead of VWAP) | 1486 | +384 | +75 | +0.6 | +60 / +79 / -64 | noise | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1661 | +349 | +40 | +0.3 | +34 / +76 / -70 | noise | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1730 | +219 | -89 | -0.6 | -36 / +43 / -96 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1755 | +172 | -136 | -1.0 | -57 / +30 / -110 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| EMA200 cap 3 ATR (instead of VWAP) | 1041 | +54 | -255 | -2.1 | -109 / -50 / -95 | worse |
| EMA200 cap 4 ATR (instead of VWAP) | 1266 | +221 | -87 | -0.8 | -46 / +23 / -65 | worse | · 10/30 adds 02:27 +8.6
| EMA200 cap 5 ATR (instead of VWAP) | 1442 | +321 | +13 | +0.1 | +24 / +30 / -41 | noise | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| EMA200 cap 6 ATR (instead of VWAP) | 1555 | +238 | -70 | -0.5 | -44 / +18 / -43 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| EMA200 cap 8 ATR (instead of VWAP) | 1689 | +251 | -57 | -0.4 | -38 / +54 / -73 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| EMA200 cap 10 ATR (instead of VWAP) | 1742 | +211 | -97 | -0.7 | -54 / +39 / -83 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| EMA200 cap 12 ATR (instead of VWAP) | 1758 | +217 | -92 | -0.6 | -47 / +53 / -98 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| VWAP 4 + HTF EMA20 cap 2 ATR | 975 | +250 | -59 | -0.6 | -39 / -21 / +2 | worse | · 10/30 adds 02:27 +8.6
| VWAP 4 + HTF EMA20 cap 3 ATR | 1119 | +370 | +62 | +1.1 | +33 / +8 / +20 | promising |
| VWAP 4 + HTF EMA20 cap 4 ATR | 1164 | +331 | +23 | +0.7 | +34 / -17 / +6 | noise |
| VWAP 4 + EMA200 cap 4 ATR | 1059 | +236 | -73 | -1.0 | -41 / -14 / -18 | worse | · 10/30 adds 02:27 +8.6
| VWAP 4 + EMA200 cap 6 ATR | 1140 | +281 | -28 | -0.6 | +10 / -38 / +1 | worse |
| VWAP 4 + EMA200 cap 8 ATR | 1168 | +295 | -13 | -0.5 | +8 / -15 / -7 | worse |

## MES 3m · current (no stretch cap): 1754 setups, net +0 (thirds +123 / -214 / +91)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 90 | 49% | +6 | +0.07 |
| 0 to 1 | 505 | 49% | +5 | +0.01 |
| 1 to 2 | 450 | 50% | +24 | +0.05 |
| 2 to 3 | 338 | 50% | +29 | +0.09 |
| 3 to 4 | 193 | 46% | -95 | -0.49 |
| 4 to 5 | 101 | 52% | -34 | -0.33 |
| 5 to 6 | 41 | 54% | +36 | +0.87 |
| 6 to 8 | 30 | 57% | +26 | +0.86 |
| 8 to + | 6 | 50% | +3 | +0.42 |

**All setups (no stretch cap) by distance from EMA200 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 235 | 50% | +23 | +0.10 |
| 0 to 2 | 443 | 50% | +53 | +0.12 |
| 2 to 4 | 497 | 49% | -135 | -0.27 |
| 4 to 6 | 295 | 51% | +69 | +0.23 |
| 6 to 8 | 137 | 47% | -12 | -0.08 |
| 8 to 10 | 77 | 48% | -6 | -0.08 |
| 10 to 12 | 41 | 46% | -27 | -0.65 |
| 12 to 15 | 18 | 72% | +32 | +1.78 |
| 15 to + | 11 | 55% | +3 | +0.24 |

**All setups (no stretch cap) by distance from VWAP (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 211 | 48% | -16 | -0.08 |
| 0 to 2 | 581 | 51% | +157 | +0.27 |
| 2 to 3 | 261 | 49% | -79 | -0.30 |
| 3 to 4 | 220 | 46% | -122 | -0.55 |
| 4 to 5 | 160 | 54% | +59 | +0.37 |
| 5 to 6 | 85 | 45% | -14 | -0.17 |
| 6 to 8 | 114 | 45% | -55 | -0.49 |
| 8 to 10 | 65 | 69% | +103 | +1.58 |
| 10 to + | 57 | 42% | -32 | -0.56 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| No stretch cap at all | 1754 | +0 | +0 | +0.0 | +0 / +0 / +0 | noise |
| HTF EMA20 cap 1 ATR (instead of VWAP) | 685 | -34 | -34 | -0.2 | -104 / +129 / -59 | worse |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 898 | -63 | -63 | -0.4 | -64 / +102 / -101 | worse |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 1128 | -42 | -42 | -0.3 | -70 / +120 / -92 | worse |
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 1292 | -15 | -15 | -0.1 | -100 / +110 / -25 | worse |
| HTF EMA20 cap 3 ATR (instead of VWAP) | 1428 | +18 | +18 | +0.2 | -46 / +60 / +4 | noise |
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1599 | -42 | -42 | -0.6 | -38 / -65 / +62 | worse |
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1688 | -66 | -66 | -1.4 | -21 / -63 / +18 | worse |
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1723 | -29 | -30 | -0.9 | +9 / -31 / -8 | worse |
| EMA200 cap 3 ATR (instead of VWAP) | 991 | -27 | -27 | -0.2 | -78 / +123 / -72 | worse |
| EMA200 cap 4 ATR (instead of VWAP) | 1210 | -88 | -88 | -0.7 | -85 / +51 / -54 | worse |
| EMA200 cap 5 ATR (instead of VWAP) | 1389 | +75 | +75 | +0.7 | -15 / +52 / +38 | noise |
| EMA200 cap 6 ATR (instead of VWAP) | 1490 | +13 | +13 | +0.1 | +0 / -31 / +43 | noise |
| EMA200 cap 8 ATR (instead of VWAP) | 1613 | -6 | -6 | -0.1 | -11 / -40 / +45 | worse |
| EMA200 cap 10 ATR (instead of VWAP) | 1692 | -21 | -21 | -0.5 | -1 / -37 / +17 | worse |
| EMA200 cap 12 ATR (instead of VWAP) | 1725 | -34 | -35 | -1.3 | -3 / -35 / +3 | worse |

## MGC 2m · current (no stretch cap): 1335 setups, net +394 (thirds +174 / +68 / +152)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 73 | 55% | +18 | +0.25 |
| 0 to 1 | 414 | 52% | +107 | +0.26 |
| 1 to 2 | 322 | 50% | +68 | +0.21 |
| 2 to 3 | 270 | 51% | +89 | +0.33 |
| 3 to 4 | 153 | 46% | +9 | +0.06 |
| 4 to 5 | 68 | 68% | +113 | +1.67 |
| 5 to 6 | 18 | 50% | -11 | -0.61 |
| 6 to 8 | 15 | 53% | +0 | +0.01 |
| 8 to + | 2 | 50% | +1 | +0.40 |

**All setups (no stretch cap) by distance from EMA200 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 191 | 55% | +131 | +0.68 |
| 0 to 2 | 330 | 52% | +87 | +0.26 |
| 2 to 4 | 383 | 49% | +48 | +0.13 |
| 4 to 6 | 240 | 51% | +29 | +0.12 |
| 6 to 8 | 119 | 54% | +75 | +0.63 |
| 8 to 10 | 46 | 50% | +3 | +0.06 |
| 10 to 12 | 14 | 64% | +13 | +0.90 |
| 12 to 15 | 10 | 60% | +9 | +0.87 |
| 15 to + | 2 | 50% | +0 | +0.08 |

**All setups (no stretch cap) by distance from VWAP (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 217 | 53% | +95 | +0.44 |
| 0 to 2 | 305 | 51% | +106 | +0.35 |
| 2 to 3 | 117 | 53% | +78 | +0.67 |
| 3 to 4 | 110 | 50% | +20 | +0.18 |
| 4 to 5 | 100 | 53% | +33 | +0.33 |
| 5 to 6 | 80 | 48% | +5 | +0.07 |
| 6 to 8 | 155 | 46% | -57 | -0.37 |
| 8 to 10 | 81 | 48% | -29 | -0.36 |
| 10 to + | 170 | 57% | +144 | +0.85 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| No stretch cap at all | 1335 | +394 | +0 | +0.0 | +0 / +0 / +0 | noise |
| HTF EMA20 cap 1 ATR (instead of VWAP) | 562 | +88 | -306 | -2.1 | -201 / -87 / -19 | worse |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 703 | +139 | -255 | -1.9 | -203 / -37 / -15 | worse |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 855 | +238 | -156 | -1.3 | -94 / -42 / -20 | worse |
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 992 | +269 | -125 | -1.3 | -91 / +10 / -44 | worse |
| HTF EMA20 cap 3 ATR (instead of VWAP) | 1116 | +296 | -98 | -1.2 | -95 / +11 / -13 | worse |
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1245 | +289 | -105 | -2.0 | -67 / -27 / -11 | worse |
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1306 | +409 | +15 | +0.5 | -5 / -2 / +22 | noise |
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1320 | +394 | +0 | +0.0 | -6 / -6 / +12 | noise |
| EMA200 cap 3 ATR (instead of VWAP) | 772 | +339 | -55 | -0.4 | -74 / -3 / +23 | worse |
| EMA200 cap 4 ATR (instead of VWAP) | 928 | +299 | -95 | -0.9 | -59 / -25 / -11 | worse |
| EMA200 cap 5 ATR (instead of VWAP) | 1053 | +244 | -150 | -1.7 | -65 / -38 / -47 | worse |
| EMA200 cap 6 ATR (instead of VWAP) | 1160 | +288 | -106 | -1.5 | -48 / -49 / -9 | worse |
| EMA200 cap 8 ATR (instead of VWAP) | 1269 | +371 | -23 | -0.5 | -17 / +0 / -6 | worse |
| EMA200 cap 10 ATR (instead of VWAP) | 1312 | +376 | -18 | -0.7 | -11 / +3 / -10 | worse |
| EMA200 cap 12 ATR (instead of VWAP) | 1325 | +380 | -14 | -0.7 | -3 / -4 / -7 | worse |

## MES 2m · current (no stretch cap): 1276 setups, net -231 (thirds -103 / +80 / -207)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 17 | 59% | -6 | -0.34 |
| 0 to 1 | 241 | 50% | +9 | +0.04 |
| 1 to 2 | 321 | 46% | -48 | -0.15 |
| 2 to 3 | 309 | 48% | -97 | -0.31 |
| 3 to 4 | 192 | 52% | -44 | -0.23 |
| 4 to 5 | 108 | 45% | -28 | -0.26 |
| 5 to 6 | 63 | 46% | -8 | -0.13 |
| 6 to 8 | 21 | 57% | -0 | -0.02 |
| 8 to + | 4 | 50% | -9 | -2.21 |

**All setups (no stretch cap) by distance from EMA200 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 68 | 46% | -9 | -0.13 |
| 0 to 2 | 246 | 50% | +26 | +0.11 |
| 2 to 4 | 412 | 49% | -88 | -0.21 |
| 4 to 6 | 290 | 49% | -52 | -0.18 |
| 6 to 8 | 152 | 45% | -81 | -0.53 |
| 8 to 10 | 62 | 50% | -3 | -0.04 |
| 10 to 12 | 20 | 55% | +10 | +0.48 |
| 12 to 15 | 19 | 32% | -45 | -2.37 |
| 15 to + | 7 | 86% | +11 | +1.55 |

**All setups (no stretch cap) by distance from VWAP (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 79 | 51% | +9 | +0.11 |
| 0 to 2 | 291 | 45% | -135 | -0.47 |
| 2 to 3 | 173 | 53% | +22 | +0.13 |
| 3 to 4 | 140 | 53% | +14 | +0.10 |
| 4 to 5 | 127 | 49% | -6 | -0.05 |
| 5 to 6 | 117 | 51% | +7 | +0.06 |
| 6 to 8 | 168 | 47% | -40 | -0.24 |
| 8 to 10 | 68 | 44% | -47 | -0.69 |
| 10 to + | 113 | 45% | -55 | -0.49 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| No stretch cap at all | 1276 | -231 | +0 | +0.0 | +0 / +0 / +0 | noise |
| HTF EMA20 cap 1 ATR (instead of VWAP) | 361 | +38 | +269 | +1.8 | +88 / -46 / +227 | noise |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 499 | -38 | +193 | +1.3 | +34 / -32 / +191 | noise |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 671 | -73 | +158 | +1.2 | +30 / -37 / +165 | noise |
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 847 | -165 | +66 | +0.6 | -53 / -47 / +167 | noise |
| HTF EMA20 cap 3 ATR (instead of VWAP) | 956 | -166 | +65 | +0.7 | -61 / -19 / +145 | noise |
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1117 | -183 | +48 | +0.7 | -38 / -1 / +87 | noise |
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1204 | -195 | +36 | +0.8 | -7 / -0 / +43 | noise |
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1257 | -216 | +15 | +0.6 | +3 / +3 / +9 | noise |
| EMA200 cap 3 ATR (instead of VWAP) | 585 | -93 | +138 | +1.1 | -8 / -44 / +190 | noise |
| EMA200 cap 4 ATR (instead of VWAP) | 782 | -46 | +185 | +1.6 | +17 / +1 / +167 | promising |
| EMA200 cap 5 ATR (instead of VWAP) | 914 | -148 | +83 | +0.9 | -31 / +14 / +100 | noise |
| EMA200 cap 6 ATR (instead of VWAP) | 1040 | -146 | +85 | +1.1 | -15 / -13 / +113 | noise |
| EMA200 cap 8 ATR (instead of VWAP) | 1177 | -195 | +36 | +0.7 | -5 / -17 / +58 | noise |
| EMA200 cap 10 ATR (instead of VWAP) | 1233 | -208 | +23 | +0.7 | -2 / -5 / +30 | noise |
| EMA200 cap 12 ATR (instead of VWAP) | 1254 | -192 | +39 | +1.6 | +4 / +8 / +26 | promising |

## Candidates (robust / promising)

- MGC 3m: VWAP 4 + HTF EMA20 cap 3 ATR → +62 pts, z +1.1, thirds +33 / +8 / +20 (promising)
- MES 2m: EMA200 cap 4 ATR (instead of VWAP) → +185 pts, z +1.6, thirds +17 / +1 / +167 (promising)
- MES 2m: EMA200 cap 12 ATR (instead of VWAP) → +39 pts, z +1.6, thirds +4 / +8 / +26 (promising)
