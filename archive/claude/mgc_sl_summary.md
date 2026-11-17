# MGC 3m SL1 size + cap under FLIP 0 % -- baseline 2026-11-13 (run 1)

Scripts: claude/mgc_sl_study.py (SL1 x ATR 1.0-3.5 x cap 7 / 10 / none, FLIP 0 % and old TRAIL 50 %) and claude/mgc_sl_dist.py
(win %, max profit / loss, percentiles, deciles, result bands for 1.7 cap 7 / 1.5, 1.7, 2.0 no cap). Needs combo_study.py, chop_sim.py,
late_study.py, mes3_ema_grid.py. Replay Jan 5 -> 11/13, after 0.22 cost.

| SL1 (FLIP 0 %) | Net | Δ vs live | z | Δ by third | Δ last 4 wk | Win % | Max loss | Max DD |
|---|---|---|---|---|---|---|---|---|
| 1.7 ATR, cap 7 (live) | +557 | 0 | 0 | 0 / 0 / 0 | 0 | 18 % | -7.2 | 294 |
| 1.5 ATR, no cap | +703 | +146 | +0.5 | +71 / +74 / +1 | +11 | 19 % | -43.3 | 252 |
| 1.7 ATR, no cap | +728 | +171 | +0.8 | +104 / +55 / +12 | +11 | 19 % | -38.1 | 256 |
| 2.0 ATR, no cap | +825 | +268 | +0.9 | +219 / +26 / +23 | -12 | 20 % | -44.8 | 261 |
| any x ATR, cap 7 | +513..+603 | -44..+46 | | mixed | -20..-3 | | | |

- The 7-pt cap binds on about half the setups (median ATR 4.0), so the multiplier barely matters while it stays.
- Old exit (TRAIL 50 %) shows the same pattern: 1.7 ATR no cap +152 (z 1.1), better in all thirds.
- Risk: no cap = avg stop 8.5 vs 6.3 pts; worst trades -38..-45 pts vs -7.2; 4-5 % of trades lose > 10 pts.
- Concentration: live net +565 -> +305 without the best trade (03/19 02:00, +259.9) and -188 without the top 5.
- Decision 11/13: keep SL1 1.7 ATR and the MGC 7-pt cap. To remove the cap for MGC 3m only: Max ATR SL1 list "MGC 3m 0, MES 3m 0, MGC 7, MES 8, ...".
