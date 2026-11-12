# MGC 3m VWAP stretch cap: ER exemption check -- 2026-11-12

Question: should high-ER (strong-trend) setups be exempt from the MGC 3m VWAP stretch cap (4 ATR)? Trigger: 11/12 08:09 short blocked at 8.8 ATR, ER 0.33, would have reached TP1.

## Live shadows (Setup Blocked + Shadow Ended, MGC 3m, 11/03-11/11; 50 % version used where two chart instances reported)

| Group | Shadows | Wins | Net (pts, before costs) |
|---|---|---|---|
| ER >= 0.30 | 9 | 5 | -3.1 |
| ER < 0.30 | 6 | 4 | +12.9 |
| All | 15 | 9 | +9.8 |

11/12 08:09 (ER 0.33) not yet in the store. Too few to judge; high-ER shadows are not better than low-ER ones.

## Replay (Jan 5 -> now, chop_sim, live MGC 3m exits 50 % / trail 3.5, range gate on, after 0.32 pt cost per trade)

Current (cap 4): 1141 setups, net +166, last 4 wk +131.

| Variant | Setups | Net | Δ | z | Δ thirds (gross) | Last 4 wk Δ | Added setups n / net / win % |
|---|---|---|---|---|---|---|---|
| Exempt ER >= 0.25 | 1479 | +136 | -31 | -0.2 | -48 / +137 / -11 | -24.5 | 355 / -38 / 52 % |
| Exempt ER >= 0.30 | 1403 | +87 | -79 | -0.5 | -37 / +42 / -1 | -37.6 | 278 / -84 / 51 % |
| Exempt ER >= 0.35 | 1319 | +160 | -7 | -0.1 | +7 / +19 / +24 | -25.0 | 188 / -14 / 52 % |
| Exempt ER >= 0.40 | 1275 | +90 | -77 | -0.8 | -33 / +32 / -33 | -19.4 | 139 / -77 / 51 % |
| Exempt ER >= 0.50 | 1191 | +121 | -46 | -0.8 | -1 / +2 / -31 | -1.1 | 50 / -46 / 50 % |
| Stretch filter OFF | 1641 | -44 | -211 | -1.1 | -57 / +75 / -68 | -5.2 | 526 / -229 / 47 % |

Verdict: no ER exemption. Every threshold is worse after costs and in the last 4 weeks; the setups it would add are a coin flip (50-52 % win, net negative). Same result as the 10/30 stretch study. Keep "MGC 3m 4". The every-3-days stretch check keeps tracking the live shadows.

Side note: two MGC 3m chart instances send Shadow Ended (one at 50 % / v10.84, one at 80 % / older settings).
