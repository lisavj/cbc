# HTF EMA20 / EMA200 stretch study — run 7 -- 2026-11-12 09:58 ET

## Since last run (vs run 6, Sat 11/07 evening)

Archive now runs to 11/12 (11/09–11/12 added). Settings sync 11/12: no mismatch (v10.87). The scripts use the BASE exits (stretch_study QB), so the 11/08 chop_sim exit sync does not move these numbers; the MGC 2m sample did change (1499 → 1334 setups, Jun–Jul third +83 → +174) -- that comes from the 11/08 replay sync (MGC 2m range gate), not the market. Candidate streak count: this is run 7.

- **MGC 3m** — current (VWAP 4) **+312** (was +278; thirds +161 / +2 / +149).
  - Best with VWAP: **VWAP 4 + HTF EMA20 cap 3 ATR +62 (unchanged), z +1.1, thirds +33 / +8 / +20 = promising** (7th run promising, 0 robust; no change -- the new days did not touch it).
  - Best HTF EMA20 instead of VWAP: cap 3 ATR +75 (was +68), z +0.6, +60 / +79 / **-64** = noise (Jul–now still negative).
  - Best EMA200 instead of VWAP: cap 5 ATR +13 (was +21), z +0.1, Jul–now -41 = noise. With VWAP: VWAP 4 + EMA200 cap 8 -13 (unchanged), z -0.5 = worse.
- **MES 3m** — current (no cap) **-1** (was +16). Best HTF EMA20: cap 3 +18 (was -8), z +0.2, -46 / +60 / +4 = noise. Best EMA200: cap 5 +75 (was +53), z +0.7, **-15** / +52 / +38 = noise.
- **MGC 2m** — current **+390** (was +340, sample changed by the sync). Best HTF EMA20: cap 5 +15 (was +27), z +0.5, -5 / -2 / +22 = noise. EMA200: every cap worse now (best cap 12 -14; cap 3 was +32, now -51).
- **MES 2m** — current **-215** (was -194). Best HTF EMA20: cap 1 +253 (was +220), z +1.7, +88 / **-46** / +211 = noise (Aug still negative). **EMA200 cap 4 ATR +169 (was +125), z +1.5 (was +1.1), +17 / +1 / +151 = promising** (3rd run promising, 0 robust; Aug ≈ 0, gain is Sep–now). EMA200 cap 12 +39, z +1.6, +4 / +8 / +26 = promising (new, small).
- **Live shadow check** (MGC 3m only -- no stretch cap live on the other three): **16 shadows ended, 15 matched Blocked↔Ended** (8 new since run 6: 11/09 ×2, 11/10 ×4, 11/11 ×2; 11/03 02:33 still has no Blocked alert -- stretch / ER from bars). **Win 10/16 (62 %), net +13.8, avg +0.86** (was 4/8, +1.4).
  - From 11/10 each shadow often sends two or three "Shadow Ended" alerts (one at 0.8 × TP1 = base exits, one at 0.5 × TP1 = MGC 3m live exits -- looks like a second chart / alert); counted once, base-exit (0.8) version, first one. 11/10 11:03 had two 0.8 endings (HTF flip +9.36 at 12:15, Trail +9.47 at 12:48) -- +9.36 used.
  - By VWAP stretch: 4–5: 2, net -1.9 (1/2); 5–6: 2, net +5.0 (2/2); 6–8: 1 (-5.0); ≥ 8: 11, net +15.6 (7/11).
  - By ER: < 0.30: 7, net +13.7 (5/7); ≥ 0.30: 9, net +0.1 (5/9).
  - By HTF (15m) EMA20 distance (bars, live h20, ATR 14): ≤ 3 ATR: 6, net +4.5 (3/6); > 3 ATR: 10, net +9.3 (7/10) -- opposite to what the "VWAP 4 + HTF EMA20 cap 3" candidate assumes, but tiny samples.
  - By EMA200 distance: ≤ 4 ATR: 1 (+5.2); 4–8: 9, net +3.0 (5/9); > 8: 6, net +5.6 (4/6).
  - Far below 20 per group — no live evidence either way. The blocked setups made +13.8 over 16 live (the filter cost ~0.9 pt per blocked setup this week, mostly the 11/10 down-trend shorts), while the sim still says the filter pays (+83 vs no cap).

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

**Verdict: keep as is for all four cases.** MGC 3m "...stretch x ATR per symbol" stays "MGC 3m 4". Nothing is robust on any run. MGC 3m candidate (VWAP 4 + HTF EMA20 cap 3 ATR — would need a new CBC input) promising for the 7th run, unchanged at +62 / z +1.1; live shadows (16) lean the other way (> 3 ATR from the 15m EMA20 did better) but are far short of 20 per group. MES 2m EMA200 cap 4 ATR (would need a new CBC input) promising for the 3rd run and up to z +1.5, but the gain is still almost all Sep–now (Aug +1). MES 3m / MGC 2m: no stretch cap helps.

---

# HTF EMA20 / EMA200 stretch study — full output -- 2026-11-12 09:58 ET

HTF EMA20 / EMA200 stretch study -- 10/30/2026.

Question: instead of (or on top of) the VWAP stretch cap (MGC 3m 4 ATR), would a cap on the distance from the HTF (15m;
10m on 2m charts) EMA20, or from the EMA200, keep the good setups and drop the bad ones? Distance = close - level in ATR,
signed in the trade direction (+ = stretched in the trade's favour, e.g. a short far below the line).
Simulator: chop_sim.py (CBC-style engine, ER/breakout rule, R5 range gate on 3m, MTF gate on MES 2m), BASE exits
(SL1 1.7 ATR + min 5, TP1 1.7 ATR capped 6, 80 % at TP1, BE, trail 1.7 ATR). HTF EMA20 = live value (forming candle).
~50 % exact match with live setups: compare variants, not totals. z = change / (SD x sqrt(setups changed));
robust = z >= 2 and better in all three thirds; promising = z >= 1 and better in all three thirds.
Usage: python3 ema_stretch_study.py  (needs chop_sim.py + stretch_study.py next to it).

## MGC 3m · current (VWAP cap 4 ATR): 1192 setups, net +312 (thirds +161 / +2 / +149)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 78 | 42% | -28 | -0.36 |
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
| < to 0 | 224 | 46% | -45 | -0.20 |
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
| < to 0 | 239 | 44% | -106 | -0.44 |
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
| No stretch cap at all | 1774 | +229 | -83 | -0.6 | -67 / +62 / -78 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| HTF EMA20 cap 1 ATR (instead of VWAP) | 729 | +7 | -305 | -1.9 | -123 / +8 / -190 | worse |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 968 | +186 | -125 | -0.9 | -73 / +29 / -82 | worse |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 1180 | +273 | -38 | -0.3 | -34 / +7 / -12 | worse | · 10/30 adds 02:27 +8.6
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 1349 | +352 | +40 | +0.3 | +36 / +51 / -47 | noise | · 10/30 adds 02:27 +8.6, 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 3 ATR (instead of VWAP) | 1485 | +387 | +75 | +0.6 | +60 / +79 / -64 | noise | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1660 | +352 | +40 | +0.3 | +34 / +76 / -70 | noise | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1729 | +223 | -89 | -0.6 | -36 / +43 / -96 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1754 | +175 | -136 | -1.0 | -57 / +30 / -110 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| EMA200 cap 3 ATR (instead of VWAP) | 1040 | +57 | -255 | -2.1 | -109 / -50 / -95 | worse |
| EMA200 cap 4 ATR (instead of VWAP) | 1265 | +225 | -87 | -0.8 | -46 / +23 / -65 | worse | · 10/30 adds 02:27 +8.6
| EMA200 cap 5 ATR (instead of VWAP) | 1441 | +324 | +13 | +0.1 | +24 / +30 / -41 | noise | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| EMA200 cap 6 ATR (instead of VWAP) | 1554 | +242 | -70 | -0.5 | -44 / +18 / -43 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| EMA200 cap 8 ATR (instead of VWAP) | 1688 | +255 | -57 | -0.4 | -38 / +54 / -73 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7
| EMA200 cap 10 ATR (instead of VWAP) | 1741 | +214 | -97 | -0.7 | -54 / +39 / -83 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| EMA200 cap 12 ATR (instead of VWAP) | 1757 | +220 | -92 | -0.6 | -47 / +53 / -98 | worse | · 10/30 adds 07:00 +5.0, 07:33 +6.7, 11:27 +9.8
| VWAP 4 + HTF EMA20 cap 2 ATR | 974 | +253 | -59 | -0.6 | -39 / -21 / +2 | worse | · 10/30 adds 02:27 +8.6
| VWAP 4 + HTF EMA20 cap 3 ATR | 1118 | +373 | +62 | +1.1 | +33 / +8 / +20 | promising |
| VWAP 4 + HTF EMA20 cap 4 ATR | 1163 | +334 | +23 | +0.7 | +34 / -17 / +6 | noise |
| VWAP 4 + EMA200 cap 4 ATR | 1058 | +239 | -73 | -1.0 | -41 / -14 / -18 | worse | · 10/30 adds 02:27 +8.6
| VWAP 4 + EMA200 cap 6 ATR | 1139 | +284 | -28 | -0.6 | +10 / -38 / +1 | worse |
| VWAP 4 + EMA200 cap 8 ATR | 1167 | +298 | -13 | -0.5 | +8 / -15 / -7 | worse |

## MES 3m · current (no stretch cap): 1751 setups, net -1 (thirds +123 / -214 / +89)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 89 | 49% | +14 | +0.16 |
| 0 to 1 | 504 | 49% | -0 | -0.00 |
| 1 to 2 | 450 | 50% | +24 | +0.05 |
| 2 to 3 | 337 | 50% | +24 | +0.07 |
| 3 to 4 | 193 | 46% | -95 | -0.49 |
| 4 to 5 | 101 | 52% | -34 | -0.33 |
| 5 to 6 | 41 | 54% | +36 | +0.87 |
| 6 to 8 | 30 | 57% | +26 | +0.86 |
| 8 to + | 6 | 50% | +3 | +0.42 |

**All setups (no stretch cap) by distance from EMA200 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| < to 0 | 233 | 50% | +26 | +0.11 |
| 0 to 2 | 442 | 50% | +48 | +0.11 |
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
| < to 0 | 210 | 48% | -8 | -0.04 |
| 0 to 2 | 579 | 51% | +147 | +0.25 |
| 2 to 3 | 261 | 49% | -79 | -0.30 |
| 3 to 4 | 220 | 46% | -122 | -0.55 |
| 4 to 5 | 160 | 54% | +59 | +0.37 |
| 5 to 6 | 85 | 45% | -14 | -0.17 |
| 6 to 8 | 114 | 45% | -55 | -0.49 |
| 8 to 10 | 65 | 69% | +103 | +1.58 |
| 10 to + | 57 | 42% | -32 | -0.56 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| No stretch cap at all | 1751 | -1 | +0 | +0.0 | +0 / +0 / +0 | noise |
| HTF EMA20 cap 1 ATR (instead of VWAP) | 683 | -31 | -29 | -0.2 | -104 / +129 / -54 | worse |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 896 | -60 | -59 | -0.4 | -64 / +102 / -96 | worse |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 1126 | -39 | -37 | -0.3 | -70 / +120 / -87 | worse |
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 1290 | -12 | -10 | -0.1 | -100 / +110 / -20 | worse |
| HTF EMA20 cap 3 ATR (instead of VWAP) | 1425 | +17 | +18 | +0.2 | -46 / +60 / +4 | noise |
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1596 | -43 | -42 | -0.6 | -38 / -65 / +62 | worse |
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1685 | -68 | -66 | -1.4 | -21 / -63 / +18 | worse |
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1720 | -31 | -30 | -0.9 | +9 / -31 / -8 | worse |
| EMA200 cap 3 ATR (instead of VWAP) | 988 | -28 | -27 | -0.2 | -78 / +123 / -72 | worse |
| EMA200 cap 4 ATR (instead of VWAP) | 1207 | -90 | -88 | -0.7 | -85 / +51 / -54 | worse |
| EMA200 cap 5 ATR (instead of VWAP) | 1386 | +74 | +75 | +0.7 | -15 / +52 / +38 | noise |
| EMA200 cap 6 ATR (instead of VWAP) | 1487 | +11 | +13 | +0.1 | +0 / -31 / +43 | noise |
| EMA200 cap 8 ATR (instead of VWAP) | 1610 | -8 | -6 | -0.1 | -11 / -40 / +45 | worse |
| EMA200 cap 10 ATR (instead of VWAP) | 1689 | -23 | -21 | -0.5 | -1 / -37 / +17 | worse |
| EMA200 cap 12 ATR (instead of VWAP) | 1722 | -36 | -35 | -1.3 | -3 / -35 / +3 | worse |

## MGC 2m · current (no stretch cap): 1334 setups, net +390 (thirds +174 / +68 / +148)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 73 | 55% | +18 | +0.25 |
| 0 to 1 | 413 | 52% | +103 | +0.25 |
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
| 2 to 4 | 382 | 49% | +44 | +0.12 |
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
| 10 to + | 169 | 57% | +140 | +0.83 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| No stretch cap at all | 1334 | +390 | +0 | +0.0 | +0 / +0 / +0 | noise |
| HTF EMA20 cap 1 ATR (instead of VWAP) | 561 | +84 | -306 | -2.1 | -201 / -87 / -19 | worse |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 702 | +135 | -255 | -1.9 | -203 / -37 / -15 | worse |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 854 | +234 | -156 | -1.3 | -94 / -42 / -20 | worse |
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 991 | +265 | -125 | -1.3 | -91 / +10 / -44 | worse |
| HTF EMA20 cap 3 ATR (instead of VWAP) | 1115 | +292 | -98 | -1.2 | -95 / +11 / -13 | worse |
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1244 | +285 | -105 | -2.0 | -67 / -27 / -11 | worse |
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1305 | +405 | +15 | +0.5 | -5 / -2 / +22 | noise |
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1319 | +390 | +0 | +0.0 | -6 / -6 / +12 | noise |
| EMA200 cap 3 ATR (instead of VWAP) | 772 | +339 | -51 | -0.4 | -74 / -3 / +27 | worse |
| EMA200 cap 4 ATR (instead of VWAP) | 927 | +295 | -95 | -0.9 | -59 / -25 / -11 | worse |
| EMA200 cap 5 ATR (instead of VWAP) | 1052 | +240 | -150 | -1.7 | -65 / -38 / -47 | worse |
| EMA200 cap 6 ATR (instead of VWAP) | 1159 | +284 | -106 | -1.5 | -48 / -49 / -9 | worse |
| EMA200 cap 8 ATR (instead of VWAP) | 1268 | +367 | -23 | -0.5 | -17 / +0 / -6 | worse |
| EMA200 cap 10 ATR (instead of VWAP) | 1311 | +372 | -18 | -0.7 | -11 / +3 / -10 | worse |
| EMA200 cap 12 ATR (instead of VWAP) | 1324 | +376 | -14 | -0.7 | -3 / -4 / -7 | worse |

## MES 2m · current (no stretch cap): 1274 setups, net -215 (thirds -103 / +80 / -191)

**All setups (no stretch cap) by distance from HTF EMA20 (ATR, + = in the trade direction)**

| Distance | N | Win % | Net | Avg |
|---|---|---|---|---|
| -9 to 0 | 17 | 59% | -6 | -0.34 |
| 0 to 1 | 241 | 50% | +9 | +0.04 |
| 1 to 2 | 321 | 46% | -48 | -0.15 |
| 2 to 3 | 307 | 48% | -81 | -0.26 |
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
| 4 to 6 | 288 | 49% | -36 | -0.13 |
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
| 5 to 6 | 116 | 52% | +15 | +0.13 |
| 6 to 8 | 167 | 47% | -32 | -0.19 |
| 8 to 10 | 68 | 44% | -47 | -0.69 |
| 10 to + | 113 | 45% | -55 | -0.49 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jun–Jul / Aug / Sep–now) | Verdict |
|---|---|---|---|---|---|---|
| No stretch cap at all | 1274 | -215 | +0 | +0.0 | +0 / +0 / +0 | noise |
| HTF EMA20 cap 1 ATR (instead of VWAP) | 361 | +38 | +253 | +1.7 | +88 / -46 / +211 | noise |
| HTF EMA20 cap 1.5 ATR (instead of VWAP) | 499 | -38 | +177 | +1.2 | +34 / -32 / +175 | noise |
| HTF EMA20 cap 2 ATR (instead of VWAP) | 671 | -73 | +142 | +1.1 | +30 / -37 / +150 | noise |
| HTF EMA20 cap 2.5 ATR (instead of VWAP) | 847 | -165 | +50 | +0.4 | -53 / -47 / +151 | noise |
| HTF EMA20 cap 3 ATR (instead of VWAP) | 954 | -151 | +65 | +0.7 | -61 / -19 / +145 | noise |
| HTF EMA20 cap 4 ATR (instead of VWAP) | 1115 | -167 | +48 | +0.7 | -38 / -1 / +87 | noise |
| HTF EMA20 cap 5 ATR (instead of VWAP) | 1202 | -179 | +36 | +0.8 | -7 / -0 / +43 | noise |
| HTF EMA20 cap 6 ATR (instead of VWAP) | 1255 | -200 | +15 | +0.6 | +3 / +3 / +9 | noise |
| EMA200 cap 3 ATR (instead of VWAP) | 585 | -93 | +123 | +1.0 | -8 / -44 / +175 | noise |
| EMA200 cap 4 ATR (instead of VWAP) | 782 | -46 | +169 | +1.5 | +17 / +1 / +151 | promising |
| EMA200 cap 5 ATR (instead of VWAP) | 913 | -140 | +75 | +0.8 | -31 / +14 / +92 | noise |
| EMA200 cap 6 ATR (instead of VWAP) | 1038 | -131 | +85 | +1.1 | -15 / -13 / +113 | noise |
| EMA200 cap 8 ATR (instead of VWAP) | 1175 | -180 | +36 | +0.7 | -5 / -17 / +58 | noise |
| EMA200 cap 10 ATR (instead of VWAP) | 1231 | -192 | +23 | +0.7 | -2 / -5 / +30 | noise |
| EMA200 cap 12 ATR (instead of VWAP) | 1252 | -177 | +39 | +1.6 | +4 / +8 / +26 | promising |

## Candidates (robust / promising)

- MGC 3m: VWAP 4 + HTF EMA20 cap 3 ATR → +62 pts, z +1.1, thirds +33 / +8 / +20 (promising)
- MES 2m: EMA200 cap 4 ATR (instead of VWAP) → +169 pts, z +1.5, thirds +17 / +1 / +151 (promising)
- MES 2m: EMA200 cap 12 ATR (instead of VWAP) → +39 pts, z +1.6, thirds +4 / +8 / +26 (promising)
