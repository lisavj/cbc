# NY opening-range setup block length — Thu 11/05/2026 08:43

NY opening-range setup block length -- 11/05/2026.
CBC "No new setups during opening range (forming): NY" blocks every trigger 9:30-10:00 ET (the NY OR length, 30 min).
Would 15 min (9:30-9:45) be better? Windows tested: 0 (off), 10, 15, 20, 30 (current), 45 min. London / Asia blocks unchanged
(30 min). Also: setups that only exist with the block off, split by 15-min slot (9:30-9:45 / 9:45-10:00).
Engine: late_study LCase (mes3_ema_grid MCase + LTF late window 1). Charts on live settings (see late_study.py).
Usage: python3 orw_study.py   (needs chop_sim.py, mes3_ema_grid.py, late_study.py next to it)

## MES 3m slow 14 (live 7/14)

| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| off | 1922 | 47% | +12 | -87 | -1.1 | -123 / -28 / +63 | worse | +13.8 |
| 10 min | 1909 | 47% | +27 | -72 | -1.0 | -99 / -29 / +55 | worse | +5.6 |
| 15 min | 1901 | 47% | +34 | -65 | -1.1 | -87 / -32 / +53 | worse | +7.9 |
| 20 min | 1891 | 47% | +38 | -61 | -1.1 | -59 / -38 / +36 | worse | -2.6 |
| 30 min (current) | 1875 | 47% | +99 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 |
| 45 min | 1848 | 47% | +73 | -26 | -0.4 | -36 / +52 / -42 | worse | -32.3 |
With the block off, setups on candles opening 9:30-9:45 ET: 36, net +6.5, win 58%, avg +0.18.
With the block off, setups on candles opening 9:45-10:00 ET: 30, net -32.4, win 47%, avg -1.08.

## MES 3m slow 20 (9/20)

| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| off | 1704 | 46% | -167 | -50 | -0.8 | -94 / -4 / +49 | worse | +34.0 |
| 10 min | 1688 | 46% | -188 | -70 | -1.3 | -108 / +4 / +33 | worse | +7.0 |
| 15 min | 1679 | 46% | -164 | -47 | -1.0 | -85 / +9 / +29 | worse | +17.1 |
| 20 min | 1673 | 46% | -149 | -32 | -0.8 | -36 / -5 / +9 | worse | +7.0 |
| 30 min (current) | 1660 | 46% | -117 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 |
| 45 min | 1633 | 46% | -150 | -33 | -0.6 | -16 / -13 / -3 | worse | -14.1 |
With the block off, setups on candles opening 9:30-9:45 ET: 34, net -18.2, win 53%, avg -0.53.
With the block off, setups on candles opening 9:45-10:00 ET: 20, net -27.5, win 45%, avg -1.37.

## MGC 3m slow 20

| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| off | 1735 | 51% | +315 | +96 | +1.9 | -12 / +58 / +51 | noise | +28.7 |
| 10 min | 1719 | 51% | +343 | +124 | +2.9 | +26 / +54 / +44 | robust | +27.1 |
| 15 min | 1715 | 51% | +320 | +102 | +2.6 | +33 / +34 / +34 | robust | +27.1 |
| 20 min | 1705 | 50% | +292 | +74 | +2.3 | +35 / -4 / +42 | noise | +27.4 |
| 30 min (current) | 1691 | 50% | +218 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 |
| 45 min | 1670 | 50% | +168 | -51 | -1.6 | -24 / -23 / -5 | worse | -12.5 |
With the block off, setups on candles opening 9:30-9:45 ET: 28, net +16.0, win 61%, avg +0.57.
With the block off, setups on candles opening 9:45-10:00 ET: 29, net +61.7, win 69%, avg +2.13.

## MES 2m slow 14 (MTF gate)

| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| off | 1798 | 51% | -197 | -78 | -1.9 | -21 / -48 / -9 | worse | -0.4 |
| 10 min | 1776 | 51% | -153 | -34 | -0.9 | +13 / -33 / -14 | worse | -19.2 |
| 15 min | 1762 | 51% | -124 | -4 | -0.1 | +29 / -45 / +12 | worse | -3.2 |
| 20 min | 1754 | 51% | -78 | +41 | +1.4 | +26 / -7 / +23 | noise | +9.1 |
| 30 min (current) | 1744 | 51% | -119 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 |
| 45 min | 1717 | 51% | -147 | -27 | -0.8 | +49 / -13 / -63 | worse | -31.6 |
With the block off, setups on candles opening 9:30-9:45 ET: 45, net -50.1, win 42%, avg -1.11.
With the block off, setups on candles opening 9:45-10:00 ET: 24, net -42.9, win 42%, avg -1.79.

## MGC 2m slow 20

| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| off | 1503 | 52% | +394 | -3 | -0.1 | -2 / +11 / -11 | worse | -11.1 |
| 10 min | 1494 | 52% | +374 | -22 | -0.7 | +14 / -12 / -25 | worse | -24.4 |
| 15 min | 1487 | 52% | +402 | +6 | +0.2 | +16 / +1 / -11 | noise | -17.5 |
| 20 min | 1482 | 52% | +413 | +16 | +0.7 | +16 / +5 / -5 | noise | -11.8 |
| 30 min (current) | 1471 | 52% | +396 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 |
| 45 min | 1448 | 52% | +380 | -16 | -0.6 | -30 / -1 / +15 | worse | -13.0 |
With the block off, setups on candles opening 9:30-9:45 ET: 22, net +6.4, win 55%, avg +0.29.
With the block off, setups on candles opening 9:45-10:00 ET: 19, net +40.1, win 68%, avg +2.11.

## MES 5m slow 20

| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| off | 1226 | 52% | +111 | +98 | +1.9 | +40 / -11 / +69 | noise | +8.9 |
| 10 min | 1203 | 51% | +45 | +32 | +0.8 | -4 / -3 / +39 | noise | -4.4 |
| 15 min | 1199 | 51% | -6 | -18 | -0.5 | -1 / -44 / +26 | worse | -4.4 |
| 20 min | 1187 | 51% | +1 | -12 | -0.4 | +7 / -10 / -10 | worse | -1.7 |
| 30 min (current) | 1179 | 51% | +13 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 |
| 45 min | 1163 | 51% | -14 | -27 | -0.7 | -12 / -9 / -6 | worse | -8.9 |
With the block off, setups on candles opening 9:30-9:45 ET: 35, net +91.4, win 69%, avg +2.61.
With the block off, setups on candles opening 9:45-10:00 ET: 26, net -15.3, win 50%, avg -0.59.

## MGC 5m slow 20

| NY block | Setups | Win % | Net | Δ vs 30 min | z | Δ by third | Verdict | Last 4 wk Δ |
|---|---|---|---|---|---|---|---|---|
| off | 1195 | 51% | -78 | +8 | +0.2 | +15 / +25 / -32 | noise | +9.8 |
| 10 min | 1178 | 51% | -77 | +8 | +0.2 | +20 / +19 / -31 | noise | +9.8 |
| 15 min | 1176 | 51% | -75 | +10 | +0.3 | +15 / +19 / -24 | noise | +9.8 |
| 20 min | 1167 | 52% | -73 | +12 | +0.5 | -2 / +17 / -2 | noise | +4.8 |
| 30 min (current) | 1153 | 51% | -85 | +0 | +0.0 | +0 / +0 / +0 | baseline | +0.0 |
| 45 min | 1141 | 51% | -92 | -6 | -0.2 | +12 / -0 / -18 | worse | +0.0 |
With the block off, setups on candles opening 9:30-9:45 ET: 24, net +3.0, win 54%, avg +0.13.
With the block off, setups on candles opening 9:45-10:00 ET: 22, net +30.2, win 64%, avg +1.37.

## Candidates (robust / promising)

- MGC 3m slow 20: NY block 10 min → +124, z +2.9, thirds +26 / +54 / +44 (robust)
- MGC 3m slow 20: NY block 15 min → +102, z +2.6, thirds +33 / +34 / +34 (robust)
