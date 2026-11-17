## Week of 11/14/2026 summary

- STUDY SETTINGS STALE: the 11/13 settings sync (v10.96) lists 3 non-known MISMATCHes, NOT yet fixed in the project scripts, and they touch the 3m studies -- mes3_ema_grid LIVE still closes MES 3m 80/100 % by time of day (live since v10.95: 100 % at TP1 all day), and MGC 3m live is now FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip) while these replays use 80 % / trail 1.7 (MGCX) or 50 % / 3.5. Bot replay (H) is unaffected (part 1.0). Also new: the 11/14 X4 fix in mes3_ema_grid.py makes the MGC 3m VWAP-stretch gate actually block setups (MGC 3m 1193 setups vs 1707 last week), so MGC 3m numbers are not like-for-like with 11/09. The X4 fix changes this study most: last week the stretch gate was not really applied, so 11/09 stretch-gate rows were meaningless and the range-gate rows ran without stretch blocking.
- "range gate only, OFF in NY": live-label exits (50 % / 3.5) **Δ +43** (Δ thirds +31 / -2 / +14, last 4 wk +3) -> **FAILED** (third 2 negative, total < +50); old 80 % / 1.7 exits +47 ✓ (+27 / +9 / +12). vs 11/09 +154. **MGC 3m NY range-gate exemption: weeks held 0/3** (reset from 1/3).
- NY range-gated setups on their own (NYR5): 108 trades +108, z 1.27, thirds +85 / +21 / +2, last 4 wk +17 (13 trades) -- still positive alone, but most of them are now also stretch-blocked, so lifting only the range gate adds little.
- Other rows: no combination is ✓ with both exit sets. "Both gates OFF in NY" +151 (live-label) but third 3 -31. Stretch gate OFF loses in every session with both exit sets (NY -16 / -41) -> keep it on. Range gate OFF in Asia / London loses -> keep.
- Note: 50 % / 3.5 is no longer the live MGC 3m exit (FLIP 0 % since v10.96); not modelled here.

---

# MGC 3m — entry gate off by session (11/14/2026)

Replay Jan 5 -> now, chop_sim rules, net after costs (0.22 pts/trade). Live gates = range gate (24 bars, top/bottom 20 %, < 5 ATR) + VWAP stretch (> 4 ATR). "Off in X" = setups starting in that sub-session (ET: Asia 18:00-03:00, London 03:00-09:30, NY 09:30-16:00) are NOT gated; elsewhere the gate stays on. Δ vs gate on everywhere. ✓ = better in all three thirds.

## both gates (range + stretch) — exits live 50 % / trail 3.5: gate on everywhere = 1142 trades, net +299

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +187 | -30 | -48 | -8 | -46 | **-86** | -88 / +2 / +0 |  |
| London | +294 | -14 | -104 | +70 | +16 | **-48** | +0 / -46 / -3 |  |
| NY | +290 | +174 | +8 | -31 | +22 | **+151** | +0 / +0 / +151 |  |
| Asia + London | +471 | -43 | -155 | +57 | -24 | **-142** | -88 / -51 / -3 |  |
| Asia + NY | +477 | +143 | -40 | -39 | -24 | **+65** | -88 / +2 / +151 |  |
| London + NY | +579 | +160 | -94 | +43 | +38 | **+109** | +0 / -46 / +154 |  |
| Asia + London + NY | +756 | +130 | -145 | +30 | -2 | **+15** | -88 / -51 / +154 |  |

## range gate only (stretch stays on) — exits live 50 % / trail 3.5: gate on everywhere = 1142 trades, net +299

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +72 | +60 | -39 | -39 | -50 | **-18** | -18 / +0 / +0 |  |
| London | +51 | +4 | -43 | +0 | -4 | **-38** | +0 / -35 / -3 |  |
| NY | +24 | +31 | -2 | +14 | +3 | **+43** | +0 / +0 / +43 |  |
| Asia + London | +123 | +64 | -81 | -38 | -53 | **-56** | -18 / -35 / -3 |  |
| Asia + NY | +96 | +90 | -41 | -25 | -47 | **+25** | -18 / +0 / +43 |  |
| London + NY | +75 | +35 | -44 | +14 | -1 | **+5** | +0 / -35 / +40 |  |
| Asia + London + NY | +147 | +95 | -83 | -25 | -51 | **-13** | -18 / -35 / +40 |  |

## stretch gate only (range stays on) — exits live 50 % / trail 3.5: gate on everywhere = 1142 trades, net +299

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +86 | -72 | -8 | +44 | +8 | **-36** | -36 / +0 / +0 |  |
| London | +207 | -75 | -17 | +17 | +7 | **-75** | +0 / -75 / +0 |  |
| NY | +220 | +74 | -22 | -68 | -2 | **-16** | +0 / +0 / -16 |  |
| Asia + London | +286 | -147 | -25 | +51 | +14 | **-121** | -36 / -84 / +0 |  |
| Asia + NY | +306 | +1 | -30 | -24 | +6 | **-53** | -36 / +0 / -16 |  |
| London + NY | +422 | -2 | -37 | -47 | +5 | **-85** | +0 / -75 / -10 |  |
| Asia + London + NY | +501 | -73 | -45 | -13 | +13 | **-131** | -36 / -84 / -10 |  |

**Setups the gates block (gates off everywhere, exits live 50 % / trail 3.5)** — trades / net / avg by session

| Session | Range-gated | Stretch-gated | Not gated |
|---|---|---|---|
| Asia | 172 / +9 / +0.05 | 82 / -41 / -0.50 | 497 / +430 / +0.87 |
| London | 157 / -25 / -0.16 | 175 / -78 / -0.45 | 298 / -140 / -0.47 |
| NY | 108 / +108 / +1.00 | 198 / +24 / +0.12 | 211 / +27 / +0.13 |

## both gates (range + stretch) — exits old 80 % / trail 1.7: gate on everywhere = 1193 trades, net +55

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +226 | -38 | -67 | +32 | -36 | **-74** | -76 / +2 / +0 |  |
| London | +333 | +37 | -125 | +9 | -4 | **-79** | +0 / -79 / +0 |  |
| NY | +310 | +84 | +43 | -28 | +35 | **+99** | +0 / +0 / +99 |  |
| Asia + London | +557 | -2 | -192 | +35 | -40 | **-159** | -76 / -83 / +0 |  |
| Asia + NY | +536 | +45 | -24 | +4 | -1 | **+25** | -76 / +2 / +99 |  |
| London + NY | +643 | +120 | -82 | -19 | +31 | **+20** | +0 / -79 / +99 |  |
| Asia + London + NY | +867 | +82 | -149 | +7 | -5 | **-60** | -76 / -83 / +99 |  |

## range gate only (stretch stays on) — exits old 80 % / trail 1.7: gate on everywhere = 1193 trades, net +55

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +82 | +45 | -63 | -3 | -30 | **-21** | -21 / +0 / +0 |  |
| London | +53 | +21 | -34 | -2 | -11 | **-16** | +0 / -16 / +0 |  |
| NY | +27 | +27 | +9 | +12 | +5 | **+47** | +0 / +0 / +47 | ✓ |
| Asia + London | +135 | +66 | -97 | -5 | -41 | **-37** | -21 / -16 / +0 |  |
| Asia + NY | +109 | +71 | -54 | +9 | -25 | **+26** | -21 / +0 / +47 |  |
| London + NY | +80 | +48 | -26 | +10 | -6 | **+32** | +0 / -16 / +47 |  |
| Asia + London + NY | +162 | +92 | -89 | +7 | -36 | **+11** | -21 / -16 / +47 |  |

## stretch gate only (range stays on) — exits old 80 % / trail 1.7: gate on everywhere = 1193 trades, net +55

| Gate OFF in | Extra trades | Δ Third 1 | Δ Third 2 | Δ Third 3 | Δ Last 4 wk | Δ Whole | Δ in Asia / London / NY | |
|---|---|---|---|---|---|---|---|---|
| Asia | +112 | -72 | -7 | +36 | +1 | **-42** | -42 / +0 / +0 |  |
| London | +236 | -42 | -26 | -43 | -9 | **-110** | +0 / -110 / +0 |  |
| NY | +236 | +31 | -1 | -71 | +3 | **-41** | +0 / +0 / -41 |  |
| Asia + London | +347 | -113 | -33 | -7 | -7 | **-153** | -42 / -111 / +0 |  |
| Asia + NY | +348 | -40 | -8 | -35 | +4 | **-83** | -42 / +0 / -41 |  |
| London + NY | +472 | -11 | -26 | -114 | -6 | **-151** | +0 / -110 / -41 |  |
| Asia + London + NY | +583 | -82 | -33 | -78 | -5 | **-194** | -42 / -111 / -41 |  |

**Setups the gates block (gates off everywhere, exits old 80 % / trail 1.7)** — trades / net / avg by session

| Session | Range-gated | Stretch-gated | Not gated |
|---|---|---|---|
| Asia | 176 / +27 / +0.15 | 108 / -37 / -0.34 | 532 / +158 / +0.30 |
| London | 158 / -4 / -0.02 | 220 / -140 / -0.64 | 310 / -159 / -0.51 |
| NY | 109 / +76 / +0.70 | 222 / -10 / -0.04 | 225 / +84 / +0.37 |
