# VWAP stretch filter study — run 7 -- 2026-11-12 09:58 ET

Since last run: MGC 3m cap 4 net +312 (was +278); still nothing robust or promising (stretch OFF -83, best = ER >= 0.3 exemption +23 z +0.2, Jan-Mar -10; ER >= 0.6 +13 z +0.5, Jul-now +1 = noise); live shadows: 16 MGC 3m, 10/16 wins, net +13.8 (8 new 11/09-11/11: net +12.4, mostly the 11/10 down-trend shorts). Keep "MGC 3m 4".

# VWAP stretch filter study — full output -- 2026-11-12 09:58 ET

VWAP stretch filter study (MGC 3m "...stretch x ATR per symbol" = MGC 3m 4) -- 10/30/2026.

Question: the X4 filter (no short when close > 4 ATR below VWAP, no long > 4 ATR above) blocked every MGC 3m setup on the
10/30 trend day (06:15 flip -> 09:42, ~60 pts down). Would it be better to lift it on strong-trend candles (ER(12) >= x,
HTF ER >= x, flip trigger), raise the cap, or turn it off?
Simulator: chop_sim.py (CBC-style setup engine, ER/breakout rule, R5 range gate ON), BASE exits (SL1 1.7 ATR + min 5,
TP1 1.7 ATR capped 6, 80 % at TP1, BE, trail 1.7 ATR -- live since CBC v10.45). No momentum-break trigger in the sim
(momentum breaks are already exempt live). ~50 % exact match with live setups: compare variants, not totals.
z = change / (per-trade SD x sqrt(setups changed)); robust = z >= 2 and better in all three thirds; promising = z >= 1 and
better in all three thirds. Usage: python3 stretch_study.py [SYM TF]  (needs chop_sim.py next to it).

## MGC 3m — 01/05 to 11/12 · current (X4 = stretch cap 4 ATR): 1192 setups, net +312 (thirds +161 / +2 / +149), SD 5.7

Setups the 4-ATR cap removes (stretch-off run): 608, net -88, avg -0.15, win 48%

| Stretched setups by ER(12) | N | Win % | Net | Avg |
|---|---|---|---|---|
| 0.0–0.3 | 347 | 44% | -146 | -0.42 |
| 0.3–0.4 | 133 | 54% | +27 | +0.20 |
| 0.4–0.5 | 85 | 52% | +10 | +0.12 |
| 0.5–1 | 43 | 56% | +21 | +0.48 |

| Variant | Setups | Net | Δ vs current | z | Δ by third (Jan–Mar / Apr–Jun / Jul–now) | Verdict |
|---|---|---|---|---|---|---|
| Stretch filter OFF | 1774 | +229 | -83 | -0.6 | -67 / +62 / -78 | worse |
| Cap 5 ATR | 1357 | +292 | -19 | -0.2 | -57 / +92 / -54 | worse |
| Cap 6 ATR | 1475 | +194 | -117 | -1.1 | -103 / +54 / -68 | worse |
| Cap 8 ATR | 1620 | +242 | -70 | -0.6 | -60 / +47 / -57 | worse |
| Cap 4 + exempt when ER(12) >= 0.3 | 1475 | +335 | +23 | +0.2 | -10 / +27 / +7 | noise |
| Cap 4 + exempt when ER(12) >= 0.4 | 1331 | +307 | -4 | -0.1 | -7 / +7 / -4 | worse |
| Cap 4 + exempt when ER(12) >= 0.5 | 1242 | +312 | +1 | +0.0 | +11 / +2 / -12 | noise |
| Cap 4 + exempt when ER(12) >= 0.6 | 1213 | +324 | +13 | +0.5 | +7 / +5 / +1 | noise |
| Cap 4 + exempt when HTF ER >= 0.4 | 1436 | +204 | -108 | -1.1 | -92 / +31 / -47 | worse |
| Cap 4 + exempt when HTF ER >= 0.5 | 1367 | +206 | -105 | -1.3 | -56 / -43 / -7 | worse |
| Cap 4 + exempt when HTF ER >= 0.6 | 1310 | +211 | -101 | -1.5 | -36 / -45 / -20 | worse |
| Cap 4 + exempt HTF CBC Flip setups | 1354 | +242 | -70 | -0.9 | -31 / +20 / -59 | worse |

**Today (11/12), stretch OFF run:** 00:06 S h9 2.2 ATR ER 0.20 -> +4.1 (trail); 01:00 L ltf20 -0.9 ATR ER 0.32 -> -6.4 (SL1); 02:03 S ltf20 2.4 ATR ER 0.22 -> +6.6 (trail); 06:30 S ltf20 9.5 ATR ER 0.33 -> +3.1 (trail); 07:03 S ltf20 8.4 ATR ER 0.12 -> +5.2 (trail)

## Candidates (robust / promising)

- none

## Follow-up 10/30: other ways to let stretched setups through (MGC 3m, Jan-Oct, base exits, vs current +228)

None robust or promising -- all worse or noise. Rows: added stretched setups (their net) | Δ net | z | Δ by third.

| Idea | Added (net) | Δ | z | Thirds | Today |
|---|---|---|---|---|---|
| Pullback: close within 0.5 / 1.0 / 1.5 ATR of 3m EMA20 | 339 (-112) / 481 (-112) / 531 (-58) | -120 / -110 / -49 | -1.1 / -0.9 / -0.4 | worse | 07:00 +5.0, 07:33 +6.7 |
| Pullback to 3m EMA20 (0.5 / 1.0 ATR) + ER >= 0.3 | 93 (-57) / 183 (-68) | -79 / -84 | -1.4 / -1.1 | worse | none |
| Exempt LTF EMA20 Pierce / HTF EMA9 Pierce / HTF EMA20 Pierce | 378 (-49) / 199 (+31) / 60 (+4) | -59 / +23 / +4 | -0.5 / +0.3 / +0.1 | worse / noise (Jul-now -34) / noise | LTF20 catches both |
| Measure stretch from 15m EMA20 instead of VWAP (<= 2 / 3 / 4 ATR) | 209 (-22) / 372 (+8) / 502 (+31) | -13 / +8 / +30 | -0.2 / +0.1 / +0.2 | Jul-now -42 / -90 / -63 | 3-4 ATR catch both |
| Trend persistence: stretched > 4 ATR for 10/12, 20/24, 30/36 bars | 467 (-85) / 401 (-108) / 352 (-19) | -105 / -132 / -46 | | worse | |
| 15m EMA20 within 3 ATR + 3m EMA20 within 1 ATR | 329 (+15) | +14 | +0.1 | +26 / +54 / -66 noise | both |
| Different exits for stretched setups (SL 1.0-1.7 x TP1 1.0-1.7 ATR, 80 / 100 % at TP1, 18 combos) | | best -20 (SL 1.0 / TP1 1.7 / 100 %) | | all worse, Jan-Mar and Jul-now negative | |

Conclusion: stretched MGC 3m setups lose on average whatever the entry context or exits; days like 10/30 are the exception.
Suggested instead (not built): info-only "Setup blocked: VWAP stretch x ATR" alert (no box) so a trend day can be taken by
hand, and logged in the Alert Feed as shadow setups so live stats on blocked setups build up.
