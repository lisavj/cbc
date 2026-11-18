Untaken equal high / low (EQH / EQL) as the take-profit -- CBC EMA Slope current 3m settings -- MES (+ MGC / MNQ / M2K) -- 11/18/2026.
Follow-up to claude/eqhl_report.md (11/17): MES trades with a 15m EQH/EQL within 1 x TP1 averaged +2.19 vs +1.12 (27 trades).
EQH / EQL = claude/eqhl_study.py (15m / 30m / 60m candles from the 3m bars, swing R = 3 each side, two consecutive swings within
TOL x that timeframe's ATR, untaken until a later 3m high/low trades through; only levels known at the setup candle's close).
Exit change (entries unchanged): when the nearest untaken EQH above a long (EQL below a short) is within [lo, hi] x TP1 distance,
TP1 is moved to the level - 0.1 ATR ("front"), or level + 0.1 ATR ("through" = past the level, catching the sweep).
'ext' = only when the level is beyond TP1 (TP1 pushed out), 'tight' = only when inside TP1 (TP1 pulled in).
'ride' = MES flip-ride trades (no TP today) also get the level as a TP. Everything else = live exits (noflip_study.py CH).
Net after costs. z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, all thirds better, last 4 wk >= 0; promising = z >= 1 and all thirds.

## Candidates (promising or better)

- none

## MES 3m (bars to 11/18, tolerance 0.10)

Current exits: 711 trades, net +780, win 51 %, thirds +370 / +98 / +312, last 4 wk +202, max DD 142.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 711 | +791 | +11 | 17 | +0.3 | +7 / +2 / +3 | +3 | 51 % | 142 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 711 | +798 | +18 | 16 | +0.5 | +12 / +5 / +1 | +3 | 51 % | 142 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, front | 711 | +780 | -0 | 10 | -0.0 | -1 / -3 / +3 | +0 | 51 % | 142 (+0) | worse |
| 15m EQH/EQL tight 0.5-1, through | 711 | +780 | -0 | 9 | -0.0 | -0 / -1 / +1 | +0 | 51 % | 142 (+0) | worse |
| 15m EQH/EQL ext 1-1.5, front | 711 | +791 | +11 | 7 | +0.4 | +7 / +4 / -1 | +3 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 711 | +798 | +18 | 7 | +0.7 | +12 / +6 / +0 | +3 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL ext 1-2, front | 709 | +784 | +4 | 15 | +0.1 | +5 / -5 / +4 | +5 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 709 | +790 | +9 | 15 | +0.3 | +11 / -7 / +6 | +6 | 50 % | 142 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 711 | +784 | +4 | 6 | +0.2 | +1 / +4 / +0 | +0 | 51 % | 142 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 711 | +790 | +10 | 6 | +0.4 | +4 / +6 / +0 | +0 | 51 % | 142 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, front | 711 | +777 | -3 | 3 | -0.2 | -2 / -1 / +0 | +0 | 51 % | 142 (+0) | worse |
| 30m EQH/EQL tight 0.5-1, through | 711 | +779 | -1 | 3 | -0.1 | -2 / +0 / +0 | +0 | 51 % | 142 (+0) | worse |
| 30m EQH/EQL ext 1-1.5, front | 711 | +787 | +7 | 3 | +0.4 | +3 / +4 / +0 | +0 | 51 % | 142 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, through | 711 | +792 | +12 | 3 | +0.7 | +6 / +6 / +0 | +0 | 51 % | 142 (+0) | noise |
| 30m EQH/EQL ext 1-2, front | 710 | +779 | -1 | 11 | -0.0 | +6 / -16 / +9 | +6 | 50 % | 142 (+0) | worse |
| 30m EQH/EQL ext 1-2, through | 710 | +782 | +2 | 11 | +0.1 | +10 / -18 / +10 | +7 | 50 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 711 | +782 | +2 | 3 | +0.1 | +0 / +0 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 711 | +784 | +4 | 3 | +0.2 | +0 / +2 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, front | 711 | +779 | -1 | 1 | -0.1 | +0 / -1 / +0 | +0 | 51 % | 142 (+0) | worse |
| 60m EQH/EQL tight 0.5-1, through | 711 | +780 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, front | 711 | +783 | +3 | 2 | +0.2 | +0 / +1 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 711 | +784 | +4 | 2 | +0.3 | +0 / +1 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 710 | +763 | -17 | 6 | -0.7 | +0 / -19 / +2 | +0 | 50 % | 142 (+0) | worse |
| 60m EQH/EQL ext 1-2, through | 710 | +760 | -20 | 6 | -0.8 | +0 / -22 / +2 | +0 | 50 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 711 | +792 | +12 | 20 | +0.3 | +5 / +3 / +4 | +3 | 51 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 711 | +800 | +20 | 19 | +0.5 | +11 / +6 / +3 | +3 | 51 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, front | 711 | +778 | -2 | 11 | -0.1 | -3 / -3 / +3 | +0 | 51 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL tight 0.5-1, through | 711 | +778 | -2 | 10 | -0.1 | -2 / -1 / +1 | +0 | 51 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL ext 1-1.5, front | 711 | +794 | +14 | 9 | +0.5 | +7 / +5 / +1 | +3 | 50 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, through | 711 | +802 | +22 | 9 | +0.8 | +12 / +7 / +3 | +3 | 50 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, front | 709 | +776 | -4 | 20 | -0.1 | +8 / -22 / +10 | +8 | 50 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL ext 1-2, through | 709 | +784 | +3 | 20 | +0.1 | +15 / -24 / +13 | +10 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 713 | +800 | +20 | 21 | +0.5 | +16 / +2 / +3 | +3 | 51 % | 142 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 712 | +807 | +27 | 19 | +0.6 | +21 / +5 / +1 | +3 | 51 % | 142 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 711 | +784 | +4 | 6 | +0.2 | +1 / +4 / +0 | +0 | 51 % | 142 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 711 | +790 | +10 | 6 | +0.4 | +4 / +6 / +0 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 711 | +782 | +2 | 3 | +0.1 | +0 / +0 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 711 | +784 | +4 | 3 | +0.2 | +0 / +2 / +2 | +0 | 51 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 713 | +801 | +21 | 24 | +0.4 | +14 / +3 / +4 | +3 | 51 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 712 | +809 | +29 | 22 | +0.6 | +20 / +6 / +3 | +3 | 51 % | 142 (+0) | noise |

## MGC 3m (bars to 11/18, tolerance 0.10)

Current exits: 624 trades, net +1740, win 26 %, thirds +1037 / +134 / +569, last 4 wk +161, max DD 114.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1733 | -7 | 1 | -0.4 | -7 / +0 / +0 | +0 | 26 % | 121 (+7) | worse |
| 15m EQH/EQL tight 0.5-1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 624 | +1733 | -7 | 1 | -0.4 | -7 / +0 / +0 | +0 | 26 % | 121 (+7) | worse |
| 15m EQH/EQL ext 1-2, front | 623 | +1757 | +17 | 2 | +0.7 | +17 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 623 | +1750 | +10 | 3 | +0.3 | +10 / +0 / +0 | +0 | 26 % | 121 (+7) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-2, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-2, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-2, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1733 | -7 | 1 | -0.4 | -7 / +0 / +0 | +0 | 26 % | 121 (+7) | worse |
| 15/30/60m EQH/EQL tight 0.5-1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, through | 624 | +1733 | -7 | 1 | -0.4 | -7 / +0 / +0 | +0 | 26 % | 121 (+7) | worse |
| 15/30/60m EQH/EQL ext 1-2, front | 623 | +1757 | +17 | 2 | +0.7 | +17 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, through | 623 | +1750 | +10 | 3 | +0.3 | +10 / +0 / +0 | +0 | 26 % | 121 (+7) | noise |

## MNQ 3m (bars to 11/18, tolerance 0.10)

Current exits: 448 trades, net +6455, win 33 %, thirds +2270 / +2386 / +1798, last 4 wk +1473, max DD 278.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-2, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL ext 1-2, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL ext 1-2, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-2, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |

## M2K 3m (bars to 11/18, tolerance 0.10)

Current exits: 367 trades, net +214, win 40 %, thirds +86 / +100 / +28, last 4 wk +8, max DD 47.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 367 | +245 | +31 | 4 | +3.1 | +34 / +0 / -3 | -2 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 367 | +246 | +33 | 3 | +3.8 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, front | 367 | +212 | -2 | 2 | -0.2 | +0 / +0 / -2 | -2 | 39 % | 47 (+0) | worse |
| 15m EQH/EQL tight 0.5-1, through | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 15m EQH/EQL ext 1-1.5, front | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL ext 1-2, front | 366 | +237 | +23 | 4 | +2.4 | +34 / +0 / -10 | +0 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 366 | +237 | +23 | 4 | +2.4 | +34 / +0 / -10 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL ext 1-2, front | 366 | +205 | -9 | 2 | -1.3 | +0 / +0 / -9 | +0 | 39 % | 47 (+0) | worse |
| 30m EQH/EQL ext 1-2, through | 366 | +205 | -9 | 2 | -1.3 | +0 / +0 / -9 | +0 | 39 % | 47 (+0) | worse |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL tight 0.5-1, front | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL tight 0.5-1, through | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL ext 1-1.5, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 60m EQH/EQL ext 1-2, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 367 | +245 | +31 | 3 | +3.6 | +34 / +0 / -3 | -2 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, front | 367 | +212 | -2 | 1 | -0.3 | +0 / +0 / -2 | -2 | 39 % | 47 (+0) | worse |
| 15/30/60m EQH/EQL tight 0.5-1, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, front | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, through | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, front | 366 | +237 | +23 | 4 | +2.4 | +34 / +0 / -10 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, through | 366 | +237 | +23 | 4 | +2.4 | +34 / +0 / -10 | +0 | 40 % | 47 (+0) | noise |


---

# Tolerance 0.25

## MES 3m (bars to 11/18, tolerance 0.25)

Current exits: 711 trades, net +780, win 51 %, thirds +370 / +98 / +312, last 4 wk +202, max DD 142.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 711 | +785 | +5 | 30 | +0.1 | +7 / -2 / +1 | +3 | 51 % | 142 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 711 | +800 | +20 | 30 | +0.4 | +18 / +1 / +1 | +3 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, front | 711 | +773 | -8 | 15 | -0.2 | -6 / -3 / +1 | +0 | 51 % | 142 (+0) | worse |
| 15m EQH/EQL tight 0.5-1, through | 711 | +781 | +0 | 15 | +0.0 | -3 / -1 / +4 | +0 | 51 % | 142 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, front | 711 | +793 | +13 | 15 | +0.3 | +12 / +0 / +0 | +3 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 711 | +800 | +20 | 15 | +0.5 | +21 / +2 / -3 | +3 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL ext 1-2, front | 709 | +798 | +18 | 26 | +0.4 | +12 / -2 / +9 | +8 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 709 | +806 | +25 | 26 | +0.5 | +22 / -4 / +7 | +10 | 50 % | 142 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 711 | +780 | -0 | 16 | -0.0 | +3 / -7 / +3 | +2 | 50 % | 142 (+0) | worse |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 711 | +792 | +12 | 16 | +0.3 | +8 / -3 / +6 | +2 | 50 % | 142 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, front | 711 | +776 | -4 | 5 | -0.2 | -2 / -1 / -1 | +0 | 51 % | 142 (+0) | worse |
| 30m EQH/EQL tight 0.5-1, through | 711 | +779 | -1 | 5 | -0.1 | -2 / +0 / -0 | +0 | 51 % | 142 (+0) | worse |
| 30m EQH/EQL ext 1-1.5, front | 711 | +784 | +4 | 11 | +0.1 | +6 / -6 / +4 | +2 | 50 % | 142 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, through | 711 | +793 | +13 | 11 | +0.4 | +10 / -3 / +6 | +2 | 50 % | 142 (+0) | noise |
| 30m EQH/EQL ext 1-2, front | 710 | +783 | +3 | 21 | +0.1 | +9 / -21 / +15 | +7 | 50 % | 142 (+0) | noise |
| 30m EQH/EQL ext 1-2, through | 710 | +792 | +12 | 21 | +0.3 | +14 / -21 / +18 | +9 | 50 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 711 | +781 | +1 | 5 | +0.0 | +0 / +0 / +1 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 711 | +784 | +4 | 5 | +0.2 | +0 / +2 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, front | 711 | +778 | -2 | 3 | -0.1 | +0 / -1 / -1 | +0 | 51 % | 142 (+0) | worse |
| 60m EQH/EQL tight 0.5-1, through | 711 | +780 | +0 | 3 | +0.0 | +0 / +0 / -0 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, front | 711 | +783 | +3 | 2 | +0.2 | +0 / +1 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 711 | +784 | +4 | 2 | +0.3 | +0 / +1 / +2 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 710 | +763 | -17 | 6 | -0.7 | +0 / -19 / +2 | +0 | 50 % | 142 (+0) | worse |
| 60m EQH/EQL ext 1-2, through | 710 | +760 | -20 | 6 | -0.8 | +0 / -22 / +2 | +0 | 50 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 711 | +777 | -3 | 38 | -0.0 | +7 / -13 / +3 | +5 | 50 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 711 | +796 | +16 | 38 | +0.3 | +19 / -8 / +6 | +6 | 50 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, front | 711 | +771 | -9 | 17 | -0.2 | -6 / -3 / -0 | +0 | 51 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL tight 0.5-1, through | 711 | +780 | +0 | 17 | +0.0 | -3 / -1 / +4 | +0 | 51 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, front | 711 | +786 | +6 | 21 | +0.1 | +12 / -10 / +4 | +5 | 50 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, through | 711 | +796 | +16 | 21 | +0.4 | +22 / -7 / +2 | +6 | 50 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, front | 709 | +784 | +4 | 36 | +0.1 | +15 / -25 / +14 | +10 | 50 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, through | 709 | +796 | +16 | 36 | +0.3 | +27 / -24 / +14 | +13 | 50 % | 142 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 714 | +763 | -17 | 38 | -0.3 | +16 / -2 / -31 | +4 | 51 % | 142 (+0) | worse |
| 15m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 713 | +780 | -0 | 37 | -0.0 | +27 / +1 / -28 | +5 | 51 % | 142 (+0) | worse |
| 30m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 713 | +775 | -6 | 21 | -0.1 | +4 / -22 / +12 | +2 | 50 % | 142 (+0) | worse |
| 30m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 713 | +789 | +8 | 21 | +0.2 | +10 / -17 / +16 | +2 | 50 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 711 | +781 | +1 | 5 | +0.0 | +0 / +0 / +1 | +0 | 51 % | 142 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 711 | +784 | +4 | 5 | +0.2 | +0 / +2 / +2 | +0 | 51 % | 142 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front + ride trades | 716 | +741 | -39 | 50 | -0.6 | +17 / -28 / -28 | +6 | 51 % | 142 (+0) | worse |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through + ride trades | 715 | +763 | -17 | 49 | -0.2 | +29 / -23 / -23 | +7 | 51 % | 142 (+0) | worse |

## MGC 3m (bars to 11/18, tolerance 0.25)

Current exits: 624 trades, net +1740, win 26 %, thirds +1037 / +134 / +569, last 4 wk +161, max DD 114.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1747 | +7 | 2 | +0.3 | +3 / +0 / +4 | +4 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1737 | -3 | 2 | -0.1 | -7 / +0 / +4 | +4 | 26 % | 121 (+7) | worse |
| 15m EQH/EQL tight 0.5-1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, front | 624 | +1744 | +4 | 1 | +0.2 | +0 / +0 / +4 | +4 | 26 % | 114 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 624 | +1737 | -3 | 2 | -0.1 | -7 / +0 / +4 | +4 | 26 % | 121 (+7) | worse |
| 15m EQH/EQL ext 1-2, front | 623 | +1761 | +22 | 3 | +0.7 | +17 / +0 / +4 | +4 | 27 % | 114 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 623 | +1754 | +15 | 4 | +0.4 | +10 / +0 / +4 | +4 | 27 % | 121 (+7) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-2, front | 623 | +1745 | +5 | 2 | +0.2 | +0 / +0 / +5 | +0 | 26 % | 114 (+0) | noise |
| 30m EQH/EQL ext 1-2, through | 623 | +1745 | +5 | 2 | +0.2 | +0 / +0 / +5 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 60m EQH/EQL ext 1-2, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 624 | +1747 | +7 | 2 | +0.3 | +3 / +0 / +4 | +4 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 624 | +1737 | -3 | 2 | -0.1 | -7 / +0 / +4 | +4 | 26 % | 121 (+7) | worse |
| 15/30/60m EQH/EQL tight 0.5-1, front | 624 | +1743 | +3 | 1 | +0.2 | +3 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, through | 624 | +1740 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, front | 624 | +1744 | +4 | 1 | +0.2 | +0 / +0 / +4 | +4 | 26 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, through | 624 | +1737 | -3 | 2 | -0.1 | -7 / +0 / +4 | +4 | 26 % | 121 (+7) | worse |
| 15/30/60m EQH/EQL ext 1-2, front | 622 | +1766 | +27 | 5 | +0.7 | +17 / +0 / +9 | +4 | 27 % | 114 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, through | 622 | +1759 | +20 | 6 | +0.4 | +10 / +0 / +9 | +4 | 27 % | 121 (+7) | noise |

## MNQ 3m (bars to 11/18, tolerance 0.25)

Current exits: 448 trades, net +6455, win 33 %, thirds +2270 / +2386 / +1798, last 4 wk +1473, max DD 278.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6461 | +6 | 1 | +0.1 | +0 / +0 / +6 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 448 | +6461 | +6 | 1 | +0.1 | +0 / +0 / +6 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-2, front | 448 | +6456 | +1 | 1 | +0.0 | +1 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 448 | +6462 | +7 | 2 | +0.1 | +1 / +0 / +6 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 30m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, front | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 30m EQH/EQL ext 1-1.5, through | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 30m EQH/EQL ext 1-2, front | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 30m EQH/EQL ext 1-2, through | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 60m EQH/EQL ext 1-2, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 448 | +6436 | -19 | 2 | -0.2 | +0 / +0 / -19 | +0 | 33 % | 278 (+0) | worse |
| 15/30/60m EQH/EQL tight 0.5-1, front | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, through | 448 | +6455 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 33 % | 278 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, front | 448 | +6430 | -25 | 1 | -0.3 | +0 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 15/30/60m EQH/EQL ext 1-1.5, through | 448 | +6436 | -19 | 2 | -0.2 | +0 / +0 / -19 | +0 | 33 % | 278 (+0) | worse |
| 15/30/60m EQH/EQL ext 1-2, front | 448 | +6431 | -24 | 2 | -0.2 | +1 / +0 / -25 | +0 | 33 % | 278 (+0) | worse |
| 15/30/60m EQH/EQL ext 1-2, through | 448 | +6437 | -18 | 3 | -0.1 | +1 / +0 / -19 | +0 | 33 % | 278 (+0) | worse |

## M2K 3m (bars to 11/18, tolerance 0.25)

Current exits: 367 trades, net +214, win 40 %, thirds +86 / +100 / +28, last 4 wk +8, max DD 47.

| TP1 at EQH/EQL | Trades | Net | vs current | Changed | z | Change by third | Last 4 wk | Win % | Max DD (vs current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m EQH/EQL 0.5-1.5 x TP1, front | 367 | +245 | +31 | 4 | +3.1 | +34 / +0 / -3 | -2 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL 0.5-1.5 x TP1, through | 367 | +246 | +33 | 3 | +3.8 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL tight 0.5-1, front | 367 | +212 | -2 | 2 | -0.2 | +0 / +0 / -2 | -2 | 39 % | 47 (+0) | worse |
| 15m EQH/EQL tight 0.5-1, through | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 15m EQH/EQL ext 1-1.5, front | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL ext 1-1.5, through | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15m EQH/EQL ext 1-2, front | 366 | +235 | +22 | 5 | +1.9 | +32 / +0 / -10 | +0 | 39 % | 47 (+0) | noise |
| 15m EQH/EQL ext 1-2, through | 366 | +235 | +22 | 5 | +1.9 | +32 / +0 / -10 | +0 | 39 % | 47 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL 0.5-1.5 x TP1, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL tight 0.5-1, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL ext 1-1.5, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 30m EQH/EQL ext 1-2, front | 366 | +205 | -9 | 2 | -1.3 | +0 / +0 / -9 | +0 | 39 % | 47 (+0) | worse |
| 30m EQH/EQL ext 1-2, through | 366 | +205 | -9 | 2 | -1.3 | +0 / +0 / -9 | +0 | 39 % | 47 (+0) | worse |
| 60m EQH/EQL 0.5-1.5 x TP1, front | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL 0.5-1.5 x TP1, through | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL tight 0.5-1, front | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL tight 0.5-1, through | 367 | +214 | -0 | 1 | -0.0 | +0 / +0 / -0 | +0 | 40 % | 47 (+0) | worse |
| 60m EQH/EQL ext 1-1.5, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 60m EQH/EQL ext 1-1.5, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 60m EQH/EQL ext 1-2, front | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 60m EQH/EQL ext 1-2, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, front | 367 | +245 | +31 | 3 | +3.6 | +34 / +0 / -3 | -2 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL 0.5-1.5 x TP1, through | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL tight 0.5-1, front | 367 | +212 | -2 | 1 | -0.3 | +0 / +0 / -2 | -2 | 39 % | 47 (+0) | worse |
| 15/30/60m EQH/EQL tight 0.5-1, through | 367 | +214 | +0 | 1 | +0.0 | +0 / +0 / +0 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, front | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-1.5, through | 367 | +246 | +33 | 2 | +4.7 | +34 / +0 / -1 | +0 | 40 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, front | 366 | +235 | +22 | 5 | +1.9 | +32 / +0 / -10 | +0 | 39 % | 47 (+0) | noise |
| 15/30/60m EQH/EQL ext 1-2, through | 366 | +235 | +22 | 5 | +1.9 | +32 / +0 / -10 | +0 | 39 % | 47 (+0) | noise |
