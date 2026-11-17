# v10.97 vs CBC EMA Slope branch versions -- MES 3m / MGC 3m -- 11/14/2026

Replay Jan 5 -> Nov 13 (ats_inputs_study engine, TV EMA20), net after costs (MES 0.50, MGC 0.22). DD = max drawdown inside that period (points). Each branch setting was picked on this same data (in-sample), so the gains are an upper estimate. Script: claude/vcmp.py (needs ats_inputs_study.py, ema716_eng.py, chop_sim.py).

### MES 3m (thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/13; last 4 wk from 10/16)

| Version | Setups | Win % | Net | Third 1 net / DD | Third 2 net / DD | Third 3 net / DD | Last 4 wk net / DD | Max DD (whole) |
|---|---|---|---|---|---|---|---|---|
| v10.97 | 1799 | 48 % | -801 | -2 / 234 | -712 / 774 | -87 / 312 | +99 / 96 | 1069 |
| CBC-ES v1.04 (slope 0.30 + flip ride) | 1242 | 48 % | +138 | +249 / 87 | -409 / 457 | +297 / 165 | +155 / 60 | 476 |
| CBC-ES v1.05 (slope 0.42) | 1000 | 49 % | +350 | +235 / 74 | -232 / 296 | +347 / 74 | +164 / 47 | 296 |
| CBC-ES v1.06 (+ LTF pierce min ER 0.15) | 836 | 49 % | +533 | +308 / 54 | -158 / 252 | +384 / 75 | +173 / 52 | 252 |

Change CBC-ES v1.06 vs v10.97: net +1334; thirds +310 / +553 / +471; third drawdowns -179 / -522 / -237; last 4 wk +75; max DD -816.

### MGC 3m (thirds 01/05–04/19 / 04/19–08/01 / 08/01–11/13; last 4 wk from 10/16)

| Version | Setups | Win % | Net | Third 1 net / DD | Third 2 net / DD | Third 3 net / DD | Last 4 wk net / DD | Max DD (whole) |
|---|---|---|---|---|---|---|---|---|
| v10.97 | 1136 | 18 % | +615 | +329 / 217 | -10 / 183 | +297 / 123 | +262 / 53 | 245 |
| CBC-ES v1.04-v1.06 (slope 0.30) | 634 | 22 % | +1135 | +545 / 111 | +78 / 55 | +512 / 60 | +279 / 18 | 121 |

Change CBC-ES v1.04-v1.06 vs v10.97: net +520; thirds +217 / +89 / +215; third drawdowns -106 / -128 / -63; last 4 wk +16; max DD -124.
