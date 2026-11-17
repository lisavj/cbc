# MGC 5m runner exit watch -- 2026-11-14 14:13 ET

STUDY SETTINGS STALE: settings sync 11/13 lists 3 non-"known" MISMATCHes (mes3_ema_grid LIVE part, chop_sim EXIT MES 3m part, chop_sim EXIT MGC 3m part/trail). None touches this study: MGC 5m runs on stretch_study QB['MGC'] base exits (SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6, 80 %, BE, trail 1.7), which MATCH. BarFeed MGC 5m current (no gaps listed for 5m).

**Verdict: no change yet.** Weeks robust: 80/2.5 **0**, 50/3.5 **0**. No cell is robust (best z +1.4). MGC 5m is **still net negative under every exit tested** (-320 .. -564 pts after cost).

## Replay (Jan 5 -> 11/14, chop_sim, net after 0.32 pt cost)

Current 80 % / trail 1.7: 1194 trades, net **-489**, thirds -20 / -66 / -319 (script labels; see caveat), last 4 wk -132.4

| Close at TP1 | Trail | Net | Δ | z | Δ by third | Δ last 4 wk | Verdict |
|---|---|---|---|---|---|---|---|
| 80 % | 2.5 | -378 | +111 | +1.0 | +27 / +53 / +7 | -2.1 | promising |
| 80 % | 3.5 | -330 | +160 | +1.4 | +26 / +61 / -7 | +2.8 | noise |
| 80 % | 4.5 | -324 | +165 | +1.4 | +24 / +69 / -7 | +2.4 | noise |
| 60 % | 1.7 | -526 | -37 | -0.2 | -16 / +14 / -30 | -6.0 | worse |
| 60 % | 2.5 | -397 | +92 | +0.6 | +12 / +89 / -25 | -12.4 | noise |
| 60 % | 3.5 | -331 | +159 | +1.0 | +9 / +93 / -43 | -10.0 | noise |
| 60 % | 4.5 | -322 | +167 | +1.1 | +10 / +102 / -43 | -10.7 | noise |
| 50 % | 1.7 | -545 | -56 | -0.4 | -24 / +21 / -44 | -9.0 | worse |
| 50 % | 2.5 | -406 | +83 | +0.5 | +5 / +106 / -42 | -17.6 | noise |
| 50 % | 3.5 | -331 | +158 | +1.0 | +1 / +109 / -60 | -16.4 | noise |
| 50 % | 4.5 | -321 | +168 | +1.1 | +4 / +118 / -60 | -17.3 | noise |
| 40 % | 1.7 | -564 | -74 | -0.5 | -33 / +28 / -59 | -12.0 | worse |
| 40 % | 2.5 | -416 | +73 | +0.5 | -2 / +124 / -58 | -22.8 | noise |
| 40 % | 3.5 | -331 | +158 | +1.0 | -7 / +125 / -78 | -22.8 | noise |
| 40 % | 4.5 | -320 | +169 | +1.1 | -3 / +134 / -78 | -23.9 | noise |

Movement vs 11/12: 80/2.5 Δ +112 -> +111, z 1.0 -> 1.0, thirds +27/+53/+8 -> +27/+53/+7, last 4 wk Δ -3 -> -2.1 (still promising, unchanged). 50/3.5 Δ +162 -> +158, z 1.0 -> 1.0, thirds +1/+109/-56 -> +1/+109/-60, last 4 wk Δ -18 -> -16.4 (noise). Wider trails still help everywhere (+158..+169 at 3.5-4.5); a smaller close % still hurts the latest third and last 4 wk.

**Caveat -- thirds labelling.** `ss.thirds(R, s.month, 5)` uses the non-3m cuts (Jun-Jul / Aug / Sep-now) for gross P&L, while the cost is subtracted per Jan-Mar / Apr-Jun / Jul-now trade counts, so the script's "thirds" are not Jan-Mar / Apr-Jun / Jul-now and do not sum to the net (-405 vs -489). The 11/12 baseline had the same quirk, so week-to-week numbers stay comparable. Script left unchanged (it runs); suggested fix: `ss.thirds(R, s.month, 3)`. Side check with true Jan-Mar / Apr-Jun / Jul-now thirds:
- 80 / 1.7: -236 / -35 / -218
- 80 / 2.5: -202 / -34 / -142 -> Δ +34 / +1 / +76 (still better in all three)
- 50 / 3.5: -80 / -63 / -188 -> Δ +156 / -28 / +30 (worse Apr-Jun)

## Live runner give-back (MGC 5m "Setup Ended", de-duplicated per Data note 1)

- /alerts?from=2026-11-13 (Fri 11/13): 5 Setup Ended, 1 hit TP1: 11/13 15:35 SHORT +5.58 = 0.8×6(TP1) + 0.2×3.89(Trail), Best +10.2 -> runner kept 3.89 of 10.2 (gave back 6.3 pts on the 20 %).
- Whole week 11/09-11/13 (from=2026-11-09, de-duped): 22 Setup Ended, net +12.8; 11 hit TP1, net +71.9 (TP1 legs 0.8 × 64.7 = +51.8, runners 0.2 × 100.3 = +20.1). Sum of Best on those 11: +192.2 -> runners exited at 100.3 of 192.2 available (gave back ~92 pts per full contract, ~18 pts at the 20 % runner size). 5 of 11 runners trailed out at 0 (BE); the three big moves (11/10 07:15 Best 31.1, 11/11 12:25 Best 44.8, 11/12 10:50 Best 51.7) kept 21.6 / 37.6 / 33.5.

## History

| Run | Current net | 80/2.5 Δ / z / thirds / L4W Δ | 50/3.5 Δ / z / thirds / L4W Δ | Weeks robust 80/2.5, 50/3.5 | Verdict |
|---|---|---|---|---|---|
| 2026-11-14 | -489 (1194 tr) | +111 / 1.0 / +27 +53 +7 / -2.1 promising | +158 / 1.0 / +1 +109 -60 / -16.4 noise | 0, 0 | no change yet |
| 2026-11-12 (wk 0) | -486 (1190 tr) | +112 / 1.0 / +27 +53 +8 / -3 promising | +162 / 1.0 / +1 +109 -56 / -18 noise | 0, 0 | baseline |
