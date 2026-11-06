# MES 3m — exits on the 5m ATR vs the 3m ATR — Thu 11/05/2026 10:34

MES 3m setups with the 5m ATR for SL / TP1 / trail -- 11/05/2026.
Setups: replay of MES 3m on live settings (v10.70: 9 / 20, range gate, late window 1, NY OR block 30). Gates keep the 3m ATR
(as CBC). Exits: SL1 = m x ATR (min 5, no cap), TP1 = k x ATR, close at TP1 by time of day (100 % / 80 % + BE + trail 1.7 x ATR),
opposite 15m flip, 16:00. ATR = 3m ATR(14) (live) or the 5m ATR(14) of the last CLOSED 5m candle (no look-ahead).
Usage: python3 atr5_study.py

Data 01/04 → 11/05. 5m ATR / 3m ATR: median 1.31 (25–75 %: 1.24–1.39). Thirds 01/05–04/16 / –07/27 / –11/05.

## A. Same multipliers (SL 3.0 / TP1 2.0), 3m vs 5m ATR

| Exits | Setups | Win % | Net | Halves | Thirds | Δ vs live | z | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|
| 3m ATR (live) | 1660 | 46% | -77 | -50 / -28 | +234 / -522 / +211 | +0 | +0.0 | baseline | +0.0 |
| 5m ATR | 1563 | 42% | +51 | +32 / +19 | +214 / -315 / +152 | +128 | +1.6 | noise | -43.5 |
| 5m ATR, same median distance (SL 2.28 / TP1 1.52) | 1630 | 46% | -96 | -3 / -93 | +250 / -475 / +130 | -19 | -0.3 | worse | -41.6 |

## B. Grid on the 5m ATR (net; ✱ both halves +, T all three thirds +; Δ vs live 3m-ATR -77)

| SL \ TP1 (x 5m ATR) | 1.00 | 1.25 | 1.50 | 1.75 | 2.00 |
|---|---|---|---|---|---|
| 1.5 | +5 | -63 | -89 | -159 | -35 |
| 2.0 | +85 ✱ | +36 | -19 | -156 | -30 |
| 2.5 | +47 ✱ | +15 ✱ | -42 | -157 | -55 |
| 3.0 | +102 | +70 | +55 ✱ | -55 | +51 ✱ |

Same grid on the 3m ATR for reference:

| SL \ TP1 (x 3m ATR) | 1.00 | 1.25 | 1.50 | 1.75 | 2.00 |
|---|---|---|---|---|---|
| 2.0 | +21 | +72 | +94 | -59 | +11 |
| 2.5 | +11 | +68 | +70 | -92 | -51 |
| 3.0 | -15 | +59 | +47 | -102 | -77 |
| 3.5 | +102 | +168 | +142 | +8 | +46 |

## C. Best 5m-ATR cells vs live

| Exits | Setups | Win % | Net | Halves | Thirds | Δ vs live | z | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|---|
| 5m ATR SL 3.0 / TP1 1.00 | 1714 | 57% | +102 | -1 / +103 | +141 / -186 / +147 | +179 | +2.0 | noise | -52.4 |
| 5m ATR SL 2.0 / TP1 1.00 | 1721 | 56% | +85 | +3 / +81 | +152 / -214 / +146 | +162 | +1.9 | noise | -56.2 |
| 5m ATR SL 3.0 / TP1 1.25 | 1660 | 52% | +70 | -5 / +75 | +233 / -362 / +199 | +147 | +2.0 | noise | -27.0 |
| 5m ATR SL 3.0 / TP1 1.50 | 1627 | 48% | +55 | +53 / +1 | +270 / -368 / +153 | +132 | +2.1 | noise | -3.0 |
| 5m ATR SL 3.0 / TP1 2.00 | 1563 | 42% | +51 | +32 / +19 | +214 / -315 / +152 | +128 | +1.6 | noise | -43.5 |

## Candidates

- none
