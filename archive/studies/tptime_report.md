# Time-based TP1 reduction — Fri 11/06/2026 10:26

Time-based TP1 reduction study, MES 3m and MGC 3m -- 11/06/2026.
Question: once a setup has been open X minutes without reaching TP1, should TP1 be pulled in to Y % of its distance from
Entry (the trade then closes as soon as price touches that new level), instead of waiting for the full TP1 / stop / flip?
Variants: X = 9, 15, 30, 45, 60, 90, 120 min; Y = 25, 50, 75, 90 %. Mode A "modified TP" = new limit at Entry + Y % x TP1
distance from the candle after X minutes (fills intrabar when the high / low reaches it; if price is already past it, fills at
that candle's open). Mode B "close at candle" = close at the candle close once X minutes have passed and the close is at least
Y % of the way to TP1. Before TP1 only; the stop, flip, 16:00 and new-setup exits are unchanged.
Replay (chop_sim rules, late window 1, NY OR block 30) on live settings: MES 3m 9 / 20, range gate, SL1 3 x ATR min 5 /
TP1 2 x ATR / close at TP1 by time of day (80 % + BE + trail inside 06-16 and 18-22:30, else 100 %); MGC 3m range gate +
VWAP stretch 4 ATR, SL1 1.7 ATR min 5 cap 7 / TP1 1.7 ATR cap 6 / 80 % + BE + trail 1.7. A reduced TP closes 100 %.
Jan 5 -> now. ~50 % exact match with live setups: compare rows, not totals. z = change / (SD x sqrt(setups changed));
robust = z >= 2 and better in all three thirds; promising = z >= 1 and all three.
Usage: python3 tptime_study.py

## MES 3m — current exits: 1670 setups, net -8, win 46%, TP1 reached 658, median time in trade 27 min

**A. Modified TP (new limit at Y % after X min)** — Δ net vs current (✱ both halves better, T all three thirds better; z)

| X min \ Y | 25 % | 50 % | 75 % | 90 % |
|---|---|---|---|---|
| 9 | +30 (+0.1) | +164 ✱ (+0.5) | +189 ✱ T (+0.6) | +102 (+0.3) |
| 15 | +26 (+0.1) | +92 (+0.3) | +141 ✱ (+0.5) | +57 (+0.2) |
| 30 | +48 (+0.2) | +86 (+0.3) | +100 ✱ (+0.3) | +27 ✱ (+0.1) |
| 45 | -104 (-0.3) | -51 (-0.2) | +33 ✱ (+0.1) | +29 ✱ (+0.1) |
| 60 | -105 (-0.3) | -90 (-0.3) | -53 (-0.2) | -86 (-0.3) |
| 90 | +68 ✱ T (+0.2) | +59 ✱ T (+0.2) | +39 ✱ T (+0.2) | -12 (-0.1) |
| 120 | +38 ✱ (+0.1) | +45 ✱ (+0.2) | +40 (+0.2) | -8 (-0.0) |

Top 3: X 9 / Y 75 % → +189 (z +0.6, thirds +49 / +124 / +16, last 4 wk -36.3, win 52 %, 724 early exits); X 9 / Y 50 % → +164 (z +0.5, thirds -31 / +285 / -90, last 4 wk -114.9, win 58 %, 871 early exits); X 15 / Y 75 % → +141 (z +0.5, thirds +63 / +83 / -4, last 4 wk -58.1, win 51 %, 568 early exits)

**B. Close at the candle close (after X min, close >= Y % of TP1)** — Δ net vs current (✱ both halves better, T all three thirds better; z)

| X min \ Y | 25 % | 50 % | 75 % | 90 % |
|---|---|---|---|---|
| 9 | +109 ✱ (+0.4) | +148 ✱ (+0.5) | +20 (+0.1) | -19 (-0.1) |
| 15 | +38 (+0.1) | +74 (+0.2) | +8 (+0.0) | -4 (-0.0) |
| 30 | +93 (+0.3) | +141 (+0.5) | +43 (+0.1) | +12 (+0.0) |
| 45 | -61 (-0.2) | +14 (+0.0) | +15 ✱ (+0.1) | -8 (-0.0) |
| 60 | -70 (-0.2) | -52 (-0.2) | -21 (-0.1) | -7 (-0.0) |
| 90 | +62 ✱ T (+0.2) | +51 (+0.2) | +6 (+0.0) | +1 ✱ (+0.1) |
| 120 | +42 ✱ (+0.1) | +43 ✱ T (+0.2) | +16 ✱ (+0.1) | +0 (+0.0) |

Top 3: X 9 / Y 50 % → +148 (z +0.5, thirds +9 / +153 / -14, last 4 wk -49.6, win 53 %, 625 early exits); X 30 / Y 50 % → +141 (z +0.5, thirds +85 / +76 / -20, last 4 wk -37.8, win 50 %, 280 early exits); X 9 / Y 25 % → +109 (z +0.4, thirds -3 / +157 / -45, last 4 wk -123.7, win 61 %, 876 early exits)

## MGC 3m — current exits: 1704 setups, net +240, win 50%, TP1 reached 758, median time in trade 18 min

**A. Modified TP (new limit at Y % after X min)** — Δ net vs current (✱ both halves better, T all three thirds better; z)

| X min \ Y | 25 % | 50 % | 75 % | 90 % |
|---|---|---|---|---|
| 9 | -23 (-0.1) | +19 (+0.1) | +2 (+0.0) | -5 (-0.0) |
| 15 | -95 (-0.4) | -55 (-0.2) | +17 (+0.1) | -24 (-0.1) |
| 30 | +39 ✱ (+0.2) | +21 (+0.1) | -1 (-0.0) | -13 (-0.1) |
| 45 | -1 (-0.0) | +3 (+0.0) | +1 (+0.0) | +8 (+0.0) |
| 60 | +31 ✱ (+0.1) | +33 ✱ T (+0.1) | +21 (+0.1) | +17 (+0.1) |
| 90 | +1 (+0.0) | -1 (-0.0) | -2 (-0.2) | -0 (-0.0) |
| 120 | +0 (+0.0) | +0 (+0.0) | +0 (+0.0) | +0 (+0.0) |

Top 3: X 30 / Y 25 % → +39 (z +0.2, thirds +63 / -38 / +13, last 4 wk +3.3, win 53 %, 146 early exits); X 60 / Y 50 % → +33 (z +0.1, thirds +7 / +22 / +4, last 4 wk +4.0, win 50 %, 18 early exits); X 60 / Y 25 % → +31 (z +0.1, thirds +11 / +22 / -1, last 4 wk +6.5, win 51 %, 21 early exits)

**B. Close at the candle close (after X min, close >= Y % of TP1)** — Δ net vs current (✱ both halves better, T all three thirds better; z)

| X min \ Y | 25 % | 50 % | 75 % | 90 % |
|---|---|---|---|---|
| 9 | +30 (+0.1) | -43 (-0.2) | +0 (+0.0) | -2 (-0.0) |
| 15 | -25 (-0.1) | -8 (-0.0) | -32 (-0.1) | -8 (-0.0) |
| 30 | +40 (+0.2) | -12 (-0.1) | +2 (+0.0) | -9 (-0.0) |
| 45 | +14 ✱ (+0.1) | -9 (-0.1) | +24 (+0.1) | -4 (-0.0) |
| 60 | +35 ✱ T (+0.2) | +14 (+0.1) | +21 (+0.1) | +0 (+0.0) |
| 90 | +4 ✱ (+0.0) | +0 (+0.0) | +0 (+0.0) | +0 (+0.0) |
| 120 | +0 (+0.0) | +0 (+0.0) | +0 (+0.0) | +0 (+0.0) |

Top 3: X 30 / Y 25 % → +40 (z +0.2, thirds +62 / -22 / -1, last 4 wk -3.2, win 52 %, 125 early exits); X 60 / Y 25 % → +35 (z +0.2, thirds +7 / +25 / +4, last 4 wk +6.6, win 51 %, 20 early exits); X 9 / Y 25 % → +30 (z +0.1, thirds +69 / -31 / -8, last 4 wk +14.2, win 58 %, 519 early exits)

## Candidates (robust / promising)

- none
