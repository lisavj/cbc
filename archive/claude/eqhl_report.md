Equal highs / lows on 15m / 30m / 60m / 240m -- skip a long when an untaken EQH is close above the entry (short: EQL below) --
CBC EMA Slope current 3m settings (v1.19 logic = v1.22 / v1.23), MES / MGC / MNQ / M2K 3m -- 11/17/2026.
EQH / EQL: higher-timeframe candles built from the 3m bars (15m = CBC HTF candles; 30m / 60m / 240m from the 18:00 ET session start, so
240m = CME 4-hour candles). Swing high = a candle whose high is the highest of 3 candles each side (confirmed 3 candles later, no look-ahead).
Two consecutive swing highs within 0.10 x that timeframe's ATR(14) = EQH at the higher of the two (CBC's own EQH rule: ATR multiple 0.10);
it stays "untaken" until a later 3m high trades above it (swept). EQL mirrored. Only levels known at the setup candle's close count.
Gate: skip the long when the nearest untaken EQH above the entry is within x (x = 0.5 / 1 / 1.5 x TP1 distance, or 1 / 2 x 3m ATR);
short mirrored with EQL. TP1 distance = the chart's TP1 (ATR x mult, capped). Entry filter: skipping can change later setups.
Exits / filters = noflip_study.py CH bases (current settings, flip close ON). Net after costs. z = Δ / (SD x sqrt(trades changed));
robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds.

## Candidates (promising or better)

- none

## MES 3m (bars to 11/16)

Current: 705 trades, net +815, avg +1.16, thirds +372 / +1 / +442, last 4 wk +212, max DD 142. EQH / EQL found: 15m 463 / 412, 30m 192 / 170, 60m 82 / 67, 240m 22 / 14

| Change | Trades | Net | Avg | vs current | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Skip: 15m EQH/EQL within 0.5 x TP1 | 704 | +823 | +1.17 | +8 | +0.3 | +0 / +13 / -6 | -6 | 142 | noise |
| Skip: 15m EQH/EQL within 1 x TP1 | 683 | +758 | +1.11 | -58 | -1.1 | -6 / +9 / -61 | -6 | 130 | worse |
| Skip: 15m EQH/EQL within 1.5 x TP1 | 660 | +681 | +1.03 | -135 | -1.8 | -77 / +1 / -58 | -3 | 130 | worse |
| Skip: 15m EQH/EQL within 1 ATR | 702 | +768 | +1.09 | -48 | -1.5 | +0 / +9 / -57 | -6 | 142 | worse |
| Skip: 15m EQH/EQL within 2 ATR | 675 | +729 | +1.08 | -86 | -1.4 | -36 / +8 / -58 | -6 | 130 | worse |
| Skip: 30m EQH/EQL within 0.5 x TP1 | 704 | +811 | +1.15 | -4 | -0.1 | +0 / +7 / -12 | +0 | 148 | worse |
| Skip: 30m EQH/EQL within 1 x TP1 | 698 | +787 | +1.13 | -28 | -0.8 | -5 / -2 / -21 | +0 | 148 | worse |
| Skip: 30m EQH/EQL within 1.5 x TP1 | 684 | +698 | +1.02 | -117 | -2.1 | -37 / -49 / -31 | -4 | 148 | robustly worse |
| Skip: 30m EQH/EQL within 1 ATR | 704 | +811 | +1.15 | -4 | -0.1 | +0 / +7 / -12 | +0 | 148 | worse |
| Skip: 30m EQH/EQL within 2 ATR | 695 | +778 | +1.12 | -37 | -0.9 | -14 / -5 / -19 | +0 | 148 | worse |
| Skip: 60m EQH/EQL within 0.5 x TP1 | 705 | +815 | +1.16 | -1 | -0.0 | +0 / -6 / +5 | +0 | 148 | worse |
| Skip: 60m EQH/EQL within 1 x TP1 | 701 | +796 | +1.14 | -20 | -0.8 | +0 / -15 / -5 | +0 | 148 | worse |
| Skip: 60m EQH/EQL within 1.5 x TP1 | 697 | +796 | +1.14 | -20 | -0.6 | +0 / -17 / -3 | +0 | 148 | worse |
| Skip: 60m EQH/EQL within 1 ATR | 705 | +815 | +1.16 | -1 | -0.0 | +0 / -6 / +5 | +0 | 148 | worse |
| Skip: 60m EQH/EQL within 2 ATR | 699 | +804 | +1.15 | -11 | -0.4 | +0 / -15 / +4 | +0 | 148 | worse |
| Skip: 240m EQH/EQL within 0.5 x TP1 | 705 | +815 | +1.16 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| Skip: 240m EQH/EQL within 1 x TP1 | 704 | +813 | +1.15 | -3 | -0.3 | +0 / +0 / -3 | +0 | 142 | worse |
| Skip: 240m EQH/EQL within 1.5 x TP1 | 704 | +825 | +1.17 | +10 | +0.6 | +0 / +0 / +10 | +13 | 142 | noise |
| Skip: 240m EQH/EQL within 1 ATR | 705 | +815 | +1.16 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| Skip: 240m EQH/EQL within 2 ATR | 704 | +813 | +1.15 | -3 | -0.3 | +0 / +0 / -3 | +0 | 142 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 0.5 x TP1 | 703 | +805 | +1.15 | -10 | -0.3 | +0 / +7 / -18 | -6 | 148 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 1 x TP1 | 680 | +732 | +1.08 | -83 | -1.4 | -6 / +3 / -80 | -6 | 136 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 1.5 x TP1 | 651 | +628 | +0.96 | -188 | -2.2 | -76 / -44 / -68 | +5 | 136 | robustly worse |
| Skip: any of 15/30/60/240m EQH/EQL within 1 ATR | 701 | +750 | +1.07 | -65 | -1.8 | +0 / +3 / -69 | -6 | 148 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 2 ATR | 671 | +710 | +1.06 | -106 | -1.5 | -34 / -2 / -70 | -6 | 136 | worse |

| Timeframe | Trades with EQH/EQL within 1 x TP1: n / net / avg / win | Others: n / net / avg / win | Within 1 x TP1 by third |
|---|---|---|---|
| 15m | 27 / +59 / +2.19 / 59 % | 678 / +756 / +1.12 / 51 % | +8 / -12 / +62 |
| 30m | 10 / +24 / +2.38 / 80 % | 695 / +792 / +1.14 / 51 % | +5 / +2 / +17 |
| 60m | 5 / +22 / +4.31 / 80 % | 700 / +794 / +1.13 / 51 % | +0 / +15 / +6 |
| 240m | 1 / +3 / +2.70 / 100 % | 704 / +813 / +1.15 / 51 % | +0 / +0 / +3 |

## MGC 3m (bars to 11/16)

Current: 618 trades, net +1766, avg +2.86, thirds +1042 / +145 / +578, last 4 wk +187, max DD 114. EQH / EQL found: 15m 371 / 279, 30m 149 / 143, 60m 76 / 84, 240m 16 / 10

| Change | Trades | Net | Avg | vs current | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Skip: 15m EQH/EQL within 0.5 x TP1 | 617 | +1765 | +2.86 | -1 | -0.0 | -1 / +0 / +0 | +0 | 114 | worse |
| Skip: 15m EQH/EQL within 1 x TP1 | 605 | +1736 | +2.87 | -30 | -0.4 | -37 / +0 / +6 | +0 | 114 | worse |
| Skip: 15m EQH/EQL within 1.5 x TP1 | 592 | +1726 | +2.92 | -40 | -0.4 | -35 / +10 / -15 | +13 | 113 | worse |
| Skip: 15m EQH/EQL within 1 ATR | 615 | +1766 | +2.87 | -0 | -0.0 | -1 / +0 / +1 | +0 | 114 | worse |
| Skip: 15m EQH/EQL within 2 ATR | 598 | +1751 | +2.93 | -15 | -0.2 | -35 / +0 / +20 | +6 | 113 | worse |
| Skip: 30m EQH/EQL within 0.5 x TP1 | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 30m EQH/EQL within 1 x TP1 | 615 | +1763 | +2.87 | -3 | -0.1 | +8 / +0 / -11 | +0 | 114 | worse |
| Skip: 30m EQH/EQL within 1.5 x TP1 | 603 | +1597 | +2.65 | -169 | -2.4 | +9 / -14 / -164 | +7 | 114 | worse |
| Skip: 30m EQH/EQL within 1 ATR | 617 | +1746 | +2.83 | -19 | -0.6 | +0 / -19 / +0 | +0 | 114 | worse |
| Skip: 30m EQH/EQL within 2 ATR | 611 | +1738 | +2.84 | -28 | -0.5 | +1 / -12 / -16 | +0 | 114 | worse |
| Skip: 60m EQH/EQL within 0.5 x TP1 | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 60m EQH/EQL within 1 x TP1 | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 60m EQH/EQL within 1.5 x TP1 | 612 | +1635 | +2.67 | -131 | -3.0 | +5 / +7 / -144 | +0 | 114 | worse |
| Skip: 60m EQH/EQL within 1 ATR | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 60m EQH/EQL within 2 ATR | 613 | +1793 | +2.92 | +27 | +0.7 | +5 / +14 / +7 | +0 | 114 | noise |
| Skip: 240m EQH/EQL within 0.5 x TP1 | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 240m EQH/EQL within 1 x TP1 | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 240m EQH/EQL within 1.5 x TP1 | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 240m EQH/EQL within 1 ATR | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: 240m EQH/EQL within 2 ATR | 618 | +1766 | +2.86 | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 0.5 x TP1 | 617 | +1765 | +2.86 | -1 | -0.0 | -1 / +0 / +0 | +0 | 114 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 1 x TP1 | 604 | +1724 | +2.86 | -41 | -0.5 | -37 / +0 / -5 | +0 | 114 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 1.5 x TP1 | 584 | +1580 | +2.71 | -186 | -1.6 | -35 / +3 / -154 | +13 | 113 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 1 ATR | 614 | +1746 | +2.84 | -20 | -0.4 | -1 / -19 / +1 | +0 | 114 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 2 ATR | 592 | +1729 | +2.92 | -37 | -0.4 | -43 / -4 / +11 | +6 | 113 | worse |

| Timeframe | Trades with EQH/EQL within 1 x TP1: n / net / avg / win | Others: n / net / avg / win | Within 1 x TP1 by third |
|---|---|---|---|
| 15m | 15 / +29 / +1.93 / 20 % | 603 / +1737 / +2.88 / 27 % | +36 / -0 / -6 |
| 30m | 3 / +3 / +0.95 / 33 % | 615 / +1763 / +2.87 / 27 % | -8 / +0 / +11 |
| 60m | 0 / +0 / +0.00 / 0 % | 618 / +1766 / +2.86 / 27 % | +0 / +0 / +0 |
| 240m | 0 / +0 / +0.00 / 0 % | 618 / +1766 / +2.86 / 27 % | +0 / +0 / +0 |

## MNQ 3m (bars to 11/16)

Current: 448 trades, net +6455, avg +14.41, thirds +2276 / +1711 / +2468, last 4 wk +1416, max DD 278. EQH / EQL found: 15m 319 / 274, 30m 144 / 113, 60m 65 / 52, 240m 22 / 16

| Change | Trades | Net | Avg | vs current | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Skip: 15m EQH/EQL within 0.5 x TP1 | 443 | +6563 | +14.82 | +108 | +0.6 | +0 / +47 / +62 | +0 | 278 | noise |
| Skip: 15m EQH/EQL within 1 x TP1 | 441 | +6538 | +14.82 | +83 | +0.4 | +0 / +53 / +31 | +0 | 289 | noise |
| Skip: 15m EQH/EQL within 1.5 x TP1 | 432 | +6572 | +15.21 | +118 | +0.3 | +22 / +64 / +32 | +0 | 285 | noise |
| Skip: 15m EQH/EQL within 1 ATR | 443 | +6563 | +14.82 | +108 | +0.6 | +0 / +47 / +62 | +0 | 278 | noise |
| Skip: 15m EQH/EQL within 2 ATR | 438 | +6570 | +15.00 | +115 | +0.4 | +26 / +58 / +31 | +0 | 289 | noise |
| Skip: 30m EQH/EQL within 0.5 x TP1 | 447 | +6500 | +14.54 | +45 | +0.6 | +0 / +45 / +0 | +0 | 278 | noise |
| Skip: 30m EQH/EQL within 1 x TP1 | 446 | +6525 | +14.63 | +71 | +0.7 | +0 / +71 / +0 | +0 | 278 | noise |
| Skip: 30m EQH/EQL within 1.5 x TP1 | 443 | +6533 | +14.75 | +78 | +0.5 | +0 / +76 / +2 | +1 | 278 | noise |
| Skip: 30m EQH/EQL within 1 ATR | 447 | +6500 | +14.54 | +45 | +0.6 | +0 / +45 / +0 | +0 | 278 | noise |
| Skip: 30m EQH/EQL within 2 ATR | 444 | +6532 | +14.71 | +77 | +0.5 | +0 / +76 / +1 | +1 | 278 | noise |
| Skip: 60m EQH/EQL within 0.5 x TP1 | 447 | +6500 | +14.54 | +45 | +0.6 | +0 / +45 / +0 | +0 | 278 | noise |
| Skip: 60m EQH/EQL within 1 x TP1 | 446 | +6541 | +14.67 | +86 | +0.8 | +41 / +45 / +0 | +0 | 278 | noise |
| Skip: 60m EQH/EQL within 1.5 x TP1 | 443 | +6547 | +14.78 | +92 | +0.5 | +45 / +45 / +2 | +1 | 278 | noise |
| Skip: 60m EQH/EQL within 1 ATR | 447 | +6500 | +14.54 | +45 | +0.6 | +0 / +45 / +0 | +0 | 278 | noise |
| Skip: 60m EQH/EQL within 2 ATR | 445 | +6542 | +14.70 | +87 | +0.7 | +41 / +45 / +1 | +1 | 278 | noise |
| Skip: 240m EQH/EQL within 0.5 x TP1 | 448 | +6455 | +14.41 | +0 | +0.0 | +0 / +0 / +0 | +0 | 278 | noise |
| Skip: 240m EQH/EQL within 1 x TP1 | 446 | +6362 | +14.26 | -93 | -0.9 | +41 / +0 / -134 | -134 | 278 | worse |
| Skip: 240m EQH/EQL within 1.5 x TP1 | 446 | +6362 | +14.26 | -93 | -0.9 | +41 / +0 / -134 | -134 | 278 | worse |
| Skip: 240m EQH/EQL within 1 ATR | 448 | +6455 | +14.41 | +0 | +0.0 | +0 / +0 / +0 | +0 | 278 | noise |
| Skip: 240m EQH/EQL within 2 ATR | 446 | +6362 | +14.26 | -93 | -0.9 | +41 / +0 / -134 | -134 | 278 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 0.5 x TP1 | 443 | +6563 | +14.82 | +108 | +0.6 | +0 / +47 / +62 | +0 | 278 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 1 x TP1 | 438 | +6471 | +14.77 | +16 | +0.1 | +41 / +78 / -104 | -134 | 289 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 1.5 x TP1 | 425 | +6512 | +15.32 | +57 | +0.1 | +67 / +89 / -99 | -134 | 285 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 1 ATR | 443 | +6563 | +14.82 | +108 | +0.6 | +0 / +47 / +62 | +0 | 278 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 2 ATR | 434 | +6504 | +14.99 | +49 | +0.2 | +67 / +84 / -102 | -134 | 289 | noise |

| Timeframe | Trades with EQH/EQL within 1 x TP1: n / net / avg / win | Others: n / net / avg / win | Within 1 x TP1 by third |
|---|---|---|---|
| 15m | 8 / -101 / -12.62 / 25 % | 440 / +6556 / +14.90 / 33 % | +0 / -70 / -31 |
| 30m | 2 / -71 / -35.39 / 0 % | 446 / +6525 / +14.63 / 33 % | +0 / -71 / +0 |
| 60m | 2 / -86 / -43.18 / 0 % | 446 / +6541 / +14.67 / 33 % | -41 / -45 / +0 |
| 240m | 2 / +93 / +46.46 / 50 % | 446 / +6362 / +14.26 / 33 % | -41 / +0 / +134 |

## M2K 3m (bars to 11/16)

Current: 362 trades, net +221, avg +0.61, thirds +86 / +87 / +48, last 4 wk +14, max DD 47. EQH / EQL found: 15m 404 / 364, 30m 165 / 150, 60m 73 / 67, 240m 36 / 17

| Change | Trades | Net | Avg | vs current | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Skip: 15m EQH/EQL within 0.5 x TP1 | 360 | +224 | +0.62 | +3 | +0.4 | +3 / +0 / +0 | +0 | 47 | noise |
| Skip: 15m EQH/EQL within 1 x TP1 | 351 | +223 | +0.63 | +2 | +0.1 | +5 / -1 / -3 | -3 | 48 | noise |
| Skip: 15m EQH/EQL within 1.5 x TP1 | 342 | +225 | +0.66 | +4 | +0.2 | +3 / +2 / -1 | -3 | 46 | noise |
| Skip: 15m EQH/EQL within 1 ATR | 359 | +224 | +0.62 | +3 | +0.3 | +4 / -1 / +0 | +0 | 48 | noise |
| Skip: 15m EQH/EQL within 2 ATR | 347 | +219 | +0.63 | -2 | -0.1 | +1 / -1 / -2 | -3 | 48 | worse |
| Skip: 30m EQH/EQL within 0.5 x TP1 | 361 | +221 | +0.61 | +0 | +0.1 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 30m EQH/EQL within 1 x TP1 | 360 | +221 | +0.61 | +0 | +0.1 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 30m EQH/EQL within 1.5 x TP1 | 356 | +208 | +0.58 | -13 | -1.1 | -1 / -5 / -8 | -1 | 47 | worse |
| Skip: 30m EQH/EQL within 1 ATR | 361 | +221 | +0.61 | +0 | +0.1 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 30m EQH/EQL within 2 ATR | 356 | +215 | +0.60 | -5 | -0.4 | +0 / +0 / -6 | +0 | 47 | worse |
| Skip: 60m EQH/EQL within 0.5 x TP1 | 362 | +221 | +0.61 | +0 | +0.0 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 60m EQH/EQL within 1 x TP1 | 361 | +221 | +0.61 | +0 | +0.1 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 60m EQH/EQL within 1.5 x TP1 | 360 | +220 | +0.61 | -1 | -0.1 | +0 / +0 / -1 | -1 | 47 | worse |
| Skip: 60m EQH/EQL within 1 ATR | 362 | +221 | +0.61 | +0 | +0.0 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 60m EQH/EQL within 2 ATR | 358 | +218 | +0.61 | -3 | -0.3 | -4 / +0 / +0 | +0 | 47 | worse |
| Skip: 240m EQH/EQL within 0.5 x TP1 | 362 | +221 | +0.61 | +0 | +0.0 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 240m EQH/EQL within 1 x TP1 | 362 | +221 | +0.61 | +0 | +0.0 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 240m EQH/EQL within 1.5 x TP1 | 362 | +221 | +0.61 | +0 | +0.0 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 240m EQH/EQL within 1 ATR | 362 | +221 | +0.61 | +0 | +0.0 | +0 / +0 / +0 | +0 | 47 | noise |
| Skip: 240m EQH/EQL within 2 ATR | 361 | +215 | +0.60 | -6 | -1.2 | +0 / +0 / -6 | +0 | 47 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 0.5 x TP1 | 359 | +224 | +0.62 | +3 | +0.4 | +3 / +0 / +0 | +0 | 47 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 1 x TP1 | 351 | +223 | +0.63 | +2 | +0.1 | +5 / -1 / -3 | -3 | 48 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 1.5 x TP1 | 339 | +212 | +0.62 | -9 | -0.4 | +3 / -3 / -9 | -4 | 46 | worse |
| Skip: any of 15/30/60/240m EQH/EQL within 1 ATR | 358 | +224 | +0.63 | +3 | +0.3 | +4 / -1 / +0 | +0 | 48 | noise |
| Skip: any of 15/30/60/240m EQH/EQL within 2 ATR | 343 | +202 | +0.59 | -18 | -0.8 | -2 / -1 / -15 | -3 | 48 | worse |

| Timeframe | Trades with EQH/EQL within 1 x TP1: n / net / avg / win | Others: n / net / avg / win | Within 1 x TP1 by third |
|---|---|---|---|
| 15m | 11 / -2 / -0.16 / 36 % | 351 / +223 / +0.63 / 40 % | -5 / +1 / +3 |
| 30m | 2 / -0 / -0.25 / 0 % | 360 / +221 / +0.61 / 40 % | +0 / +0 / -0 |
| 60m | 1 / -0 / -0.29 / 0 % | 361 / +221 / +0.61 / 40 % | +0 / +0 / -0 |
| 240m | 0 / +0 / +0.00 / 0 % | 362 / +221 / +0.61 / 40 % | +0 / +0 / +0 |
