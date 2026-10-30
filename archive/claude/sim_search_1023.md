# Filter + exit search rerun — Fri 10/23/2026 17:15 ET (scheduled)

Same method as claude/sim_search_1022.md (sim2.py / search.py / robust.py), bars through 10/23, plus a check of each candidate on REAL setups (alerts 10/19–10/23 matched with Setup Ended; MGC 2m alerts only through 10/22).

Real setups with results: MGC 3m 22 (+8.4) · MES 3m 41 (−41.6) · MGC 2m 34 (−5.6) · MES 2m 50 (−91.1).

| Candidate (10/22) | Replay 10/23 (all 3 thirds better?) | Real setups | Verdict |
|---|---|---|---|
| MGC 3m: setup candle body ≥ 0.2 ATR (0.3 stronger) | 0.2: 42 / +4.4 vs base −47.8, yes · 0.3: 29 / +45.1, yes | **Contradicts:** kept 9 / −6.7, blocked 13 / +15.1 (≥ 0.3: kept 8 / −9.2) | Not confirmed — do not adopt |
| MGC 3m: 100 % at TP1 1.5 ATR, SL 1.7 | +18.8 vs −47.8, but last third −4.2 (weakened) | On the 22 real entries: +14.3 vs +15.1 current | Drop |
| MGC 3m: skip when 15m pullback side broken | — | Broken 17 / +2.6 (h1 −4.4, h2 +7.0), intact 5 / +5.8 | Not supported |
| MES 2m: ER minimum 0.20 (all triggers) | 186 / +3.0 vs −103.9, yes (0.15–0.26 all better) | Consistent: blocked 10 / −14.4, negative in both halves; kept 40 still −76.6 | Holds, but small effect on real data |
| MGC 2m: skip flips when ATR > 100-bar average | 304 / +120.2 vs +70.9, yes | Consistent: blocked 4 / −12.2, kept flips 7 / +15.1 | Holds, tiny real N |

New ideas from the search: nothing new robust. MES 2m candle-size / close-position filters show big replay gains but keep only ~1/3 of setups (likely overfit). MES 3m: still nothing beats current settings in the replay (real MES 3m −41.6 handled by the separate claude/mes_sltp_grid_report.md work). MES 2m real setups are clearly negative (50 / −91.1) — biggest open problem.

Next: keep MES 2m ER 0.20 and MGC 2m high-ATR flip skip as watch items until 20+ real blocked setups each; drop the MGC 3m body / exit / structure candidates unless real data turns.
