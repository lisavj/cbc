# 3m weekly watch: MGC 3m slope lookback + MES 3m + MNQ / M2K 3m (Tuesdays 5:09 pm ET)

CBC EMA Slope v1.18 (11/15/2026) put MGC 3m on HTF EMA20 slope lookback 5 bars (15 min) / threshold 0.165 (v1.17: 12 bars / 0.30): replay Jan 5 - Nov 13 800 / +1182 / DD 166 -> 615 / +1782 / DD 114 (+601, z 1.8, PROMISING). v1.19 (11/15/2026) adopted MNQ 3m Max SL1 cap 60 + NY opening-range forming block OFF (443 / +3944 / DD 285 -> 448 / +6455 / DD 278, +2511, z 3.9, robust) and M2K 3m SL1 3.5 ATR + 0 % at TP1 (365 / +110 / DD 25 -> 362 / +221 / DD 47, +111, z 2.6, robust) -- both adopted by the user before the planned 3-week check, so they are revert-watched here. MES 3m unchanged (36-min, 0.42).

Each Tuesday run: `python3 mgc3_lk_watch.py` (project claude/mgc3_lk_watch.py; needs all_eng.py, ats_inputs_study.py, chop_sim.py, ema716_eng.py, mes3_ema_grid.py from claude/), newest run below the rules. "Since go-live" = bars from 11/16.

Rules:
- MGC 3m: REVERT CANDIDATE (back to "MGC 3m 0.3", remove "MGC 3m 5" from ats_slk_sym) if v1.18 - v1.17 since go-live is negative on 3 consecutive runs, or the full-period z drops below 1. CONFIRMED when z >= 2 with all thirds and the last 4 weeks positive.
- MNQ 3m / M2K 3m: the "v1.18" row = old settings vs v1.19 (negative = v1.19 better). REVERT CANDIDATE if that row is positive since go-live on 3 consecutive runs, or its full-period z rises above -1 (v1.19 edge gone). Revert inputs: MNQ -> remove "MNQ 3m 60" from ats_cap_txt and "MNQ 3m 0" from ats_orbf_sym; M2K -> remove "M2K 3m 3.5" from ats_slx_sym and "M2K 3m 0" from ats_part_sym.
- MES 3m: note any row that turns promising or better.

Tallies (runs in a row): MGC since-go-live negative 0 · MNQ v1.18-row positive since go-live 0 · M2K v1.18-row positive since go-live 0

## Run Sun 11/15/2026 (setup check, data to 11/13)

MGC 3m: v1.18 vs v1.17 full period +601 (z +1.8, thirds +361 / +160 / +79, last 4 wk -51) -> promising; since go-live: no bars yet. Neighbours all below v1.18 (5 bars 0.15 -185, 0.18 -37). Range gate OFF +261 (noise), late-away 2 pts +49 (noise). MES 3m: 15 / 30 / 45-min lookbacks and slope 0.38 / 0.46 all worse -> keep.

MNQ 3m (v1.19 base 448 / +6455 / DD 278): v1.18 -2511 (z -3.3, every third worse); cap 30 only -1268; NY block ON only -1452; cap 45 -777; cap OFF +0 (same as 60); + all OR blocks OFF -122.

M2K 3m (v1.19 base 362 / +221 / DD 47): v1.18 -111 (z -1.4, every third worse, but DD 25 vs 47); SL 1.7 + 0 % -71; 80 % with SL 3.5 -81; SL 3.0 -61; SL 4.0 +0 (same); 25 % at TP1 -25.
