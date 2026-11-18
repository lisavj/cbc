MGC 3m BOT settings for CBC v10.98 (main line) -- triggers, entry windows, 5-day filter, exit style, flatten time -- 11/17/2026.
Chart setups = CBC v10.98 MGC 3m (no slope filter): ER 0.23 + breakout, range gate 24 / 20 % / 5 ATR, VWAP stretch 4 ATR (applied), late-away
1 pt; chart exits FLIP 0 % (decide the one-setup-at-a-time sequence). Engine = claude/noflip_study.py TCase (all_eng gen).
The bot takes a chart setup when its FIRST trigger is ticked, its candle closes inside an entry window and before the no-new-entry time,
and the 5-day filter passes. Bot exits: BRACKET = SL1 / TP1 (the setup's, 100 % at TP1, broker side) or CBC ends the setup (HTF flip
against, next setup) or the flatten time; FLIP = SL1 kept, no TP, same other exits. 1 contract, net after 0.22 pt (1 pt = $10).
Thirds by date; z = Δ / (SD x sqrt(trades changed)) vs the reference row; robust = z >= 2 + all thirds + last 4 wk >= 0.

Chart: 1632 setups 01/05 -> 11/16

## 1. Each trigger alone (all hours, bracket, no 5-day filter)

| Variant | Trades | Win % | Net | Avg | Thirds | Last 4 wk | Max DD |
|---|---|---|---|---|---|---|---|
| HTF CBC Flip | 224 | 58 % | +83 | +0.37 | -31 / +80 / +34 | +7 | 88 |
| LTF EMA20 Pierce (beyond EMA9) | 260 | 53 % | +22 | +0.08 | +46 / +18 / -42 | -13 | 108 |
| LTF EMA20 Pierce (not beyond EMA9) | 445 | 49 % | +1 | +0.00 | +22 / -6 / -14 | -2 | 116 |
| LTF EMA20 Pierce (late) | 121 | 45 % | -20 | -0.16 | -32 / +11 / +1 | -12 | 80 |
| HTF EMA9 Pierce | 270 | 47 % | -101 | -0.37 | -111 / +1 / +9 | +3 | 152 |
| HTF EMA20 Pierce | 299 | 47 % | -109 | -0.36 | -17 / -65 / -27 | -15 | 150 |

## 2. Trigger sets (all hours, bracket)

| Variant | Trades | Win % | Net | Avg | Thirds | Last 4 wk | Max DD |
|---|---|---|---|---|---|---|---|
| MES bot default: Flip + LTF beyond + LTF not beyond | 929 | 52 % | +106 | +0.11 | +37 / +92 / -22 | -7 | 135 |
| Flip only | 224 | 58 % | +83 | +0.37 | -31 / +80 / +34 | +7 | 88 |
| Flip + HTF EMA20 | 523 | 51 % | -26 | -0.05 | -47 / +15 / +7 | -7 | 93 |
| Flip + LTF beyond | 484 | 55 % | +105 | +0.22 | +15 / +98 / -8 | -5 | 116 |
| Flip + LTF beyond + HTF EMA20 | 783 | 52 % | -4 | -0.00 | -2 / +33 / -35 | -20 | 166 |
| HTF EMA20 only | 299 | 47 % | -109 | -0.36 | -17 / -65 / -27 | -15 | 150 |
| All six | 1619 | 50 % | -124 | -0.08 | -123 / +39 / -40 | -30 | 279 |

## 3. By session (candle close ET; bracket; no 5-day filter)

| Trigger set | Asia 18:00-03:00 | London 03:00-09:30 | NY 09:30-15:45 |
|---|---|---|---|
| MES bot default: Flip + LTF beyond + LTF not beyond | 432 / +188 (+110 / +64 / +14) | 290 / -65 (-27 / -24 / -14) | 207 / -17 (-46 / +52 / -23) |
| Flip only | 110 / +67 (+16 / +42 / +10) | 60 / -37 (-27 / -17 / +7) | 54 / +53 (-20 / +54 / +18) |
| Flip + HTF EMA20 | 240 / -19 (+5 / +13 / -37) | 148 / -100 (-50 / -69 / +19) | 135 / +94 (-2 / +72 / +25) |
| Flip + LTF beyond | 228 / +93 (+31 / +60 / +2) | 152 / +0 (+18 / -10 / -8) | 104 / +12 (-34 / +48 / -2) |
| Flip + LTF beyond + HTF EMA20 | 358 / +7 (+21 / +31 / -45) | 240 / -64 (-6 / -63 / +5) | 185 / +53 (-17 / +65 / +5) |
| HTF EMA20 only | 130 / -87 (-10 / -29 / -47) | 88 / -64 (-24 / -53 / +13) | 81 / +42 (+17 / +17 / +7) |
| All six | 743 / +92 (+41 / +47 / +4) | 490 / -297 (-141 / -137 / -19) | 386 / +81 (-23 / +129 / -25) |

## 4. MES bot configuration on MGC (reference) and the best combinations

Reference = the MES bot settings unchanged (Flip + LTF beyond + not beyond, MES windows, no shorts above 5-day EMA, flip-only 09:30-16:00):

| Variant | Trades | Win % | Net | Avg | Thirds | Last 4 wk | Max DD | Δ vs ref | z | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| Reference: MES settings on MGC | 492 | 49 % | +43 | +0.09 | -19 / +136 / -74 | +12 | 125 | +30 | +0.7 | noise |

Top 15 of 441 combinations (all thirds positive and last 4 wk >= 0 first, then net / max DD):

| Variant | Trades | Win % | Net | Avg | Thirds | Last 4 wk | Max DD | Δ vs ref | z | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| MES bot default: Flip + LTF beyond + LTF not beyond; Asia + London 1800-0930; 5-day no shorts above; flip-only all | 564 | 29 % | +699 | +1.24 | +348 / +71 / +279 | +112 | 221 | +656 | +4.1 | noise |
| MES bot default: Flip + LTF beyond + LTF not beyond; all hours; 5-day no shorts above; flip-only all | 725 | 30 % | +669 | +0.92 | +321 / +161 / +187 | +117 | 242 | +627 | +4.2 | robust |
| HTF EMA20 only; NY only 0930-1545; 5-day both sides; flip-only none | 44 | 66 % | +54 | +1.22 | +14 / +17 / +23 | +9 | 20 | +11 | +0.1 | noise |
| Flip + LTF beyond + HTF EMA20; MES windows 1830-2200, 0300-1300, 1500-1530; 5-day both sides; flip-only all | 273 | 34 % | +396 | +1.45 | +151 / +129 / +116 | +7 | 146 | +353 | +2.2 | noise |
| Flip + LTF beyond; MES windows 1830-2200, 0300-1300, 1500-1530; 5-day off; flip-only all | 330 | 33 % | +547 | +1.66 | +277 / +175 / +95 | +4 | 222 | +505 | +3.4 | promising |
| Flip + LTF beyond; MES windows 1830-2200, 0300-1300, 1500-1530; 5-day off; flip-only NY | 330 | 52 % | +259 | +0.79 | +151 / +93 / +16 | +12 | 105 | +217 | +1.7 | noise |
| Flip + LTF beyond + HTF EMA20; NY only 0930-1545; 5-day both sides; flip-only none | 99 | 63 % | +99 | +0.99 | +3 / +62 / +33 | +5 | 45 | +56 | +0.3 | noise |
| Flip + LTF beyond; MES windows 1830-2200, 0300-1300, 1500-1530; 5-day no shorts above; flip-only NY | 256 | 53 % | +154 | +0.60 | +51 / +98 / +5 | +10 | 71 | +112 | +1.0 | noise |
| Flip + LTF beyond + HTF EMA20; London + NY 0300-1545; 5-day both sides; flip-only none | 216 | 58 % | +137 | +0.63 | +10 / +90 / +37 | +29 | 63 | +94 | +0.6 | noise |
| Flip only; Asia only; 5-day off; flip-only none | 110 | 60 % | +67 | +0.61 | +16 / +42 / +10 | +13 | 37 | +25 | +0.2 | noise |
| Flip only; Asia only; 5-day off; flip-only NY | 110 | 60 % | +67 | +0.61 | +16 / +42 / +10 | +13 | 37 | +25 | +0.2 | noise |
| Flip only; Asia only; 5-day no shorts above; flip-only none | 97 | 61 % | +67 | +0.69 | +9 / +42 / +16 | +19 | 37 | +25 | +0.2 | noise |
| Flip only; Asia only; 5-day no shorts above; flip-only NY | 97 | 61 % | +67 | +0.69 | +9 / +42 / +16 | +19 | 37 | +25 | +0.2 | noise |
| MES bot default: Flip + LTF beyond + LTF not beyond; all hours; 5-day off; flip-only all | 929 | 30 % | +543 | +0.58 | +244 / +142 / +157 | +161 | 303 | +500 | +2.7 | robust |
| Flip + LTF beyond; Asia only; 5-day off; flip-only none | 228 | 57 % | +93 | +0.41 | +31 / +60 / +2 | +8 | 55 | +51 | +0.3 | noise |

## 5. Flatten / no-new-entry time for the top combination

| Variant | Trades | Win % | Net | Avg | Thirds | Last 4 wk | Max DD |
|---|---|---|---|---|---|---|---|
| flatten 15:57, no new 15:45-18:00 | 564 | 29 % | +699 | +1.24 | +348 / +71 / +279 | +112 | 221 |
| flatten 16:57, no new 16:45-18:00 | 564 | 29 % | +699 | +1.24 | +348 / +71 / +279 | +112 | 221 |
| flatten never, no new - | 564 | 29 % | +699 | +1.24 | +348 / +71 / +279 | +112 | 221 |