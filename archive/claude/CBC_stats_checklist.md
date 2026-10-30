# CBC Stats checklist: features since v9.00

What to check on the Alert Feed **Stats** page (button "Stats", then click **Total** or a trigger row for the detail view) for each feature added since CBC v9.00. Use the **Symbol** and **TF** pickers (MGC / MES, 15-3 / 10-2) to check each symbol and timeframe separately. Filters stack: MTF · OB · Vol · OR · Pat · Ext · Rng.

**Rule: every decision is per symbol AND per chart timeframe** (MGC 3m, MGC 2m, MES 3m, MES 2m are four separate cases). Pick Symbol + TF on the Stats page before reading any box, and set gates with the timeframe syntax (CBC v10.23+): `MGC 3m 5, MGC 2m 0, MES 3m 5, MES 2m 0`.

**Rule of thumb before changing a default:** at least 20 setups for that symbol + timeframe. Recreate alerts after every CBC update, otherwise old snapshots mix into the data.

### Snapshot by symbol + timeframe (10/12-10/19, 94 setups)

| Case | Setups | Net | Range gate 24/20/<5 | VWAP stretch cap 4 | Candle pattern WITH vs none |
|---|---|---|---|---|---|
| MGC 3m | 42 | −49.8 | **+68.1** (18 blocked, 17 % win) | **+35.6** | WITH −6.8 vs none −43.0 |
| MGC 2m | 11 | −2.4 | −6.8 (2 blocked, both won) | −6.0 | n/a (1 WITH) |
| MES 3m | 30 | +33.5 | +19.6 (7 blocked, 29 % win) | +3.1 | WITH +19.7 vs none +13.8 |
| MES 2m | 11 | −6.4 | −6.5 (1 blocked, won) | −0.6 | WITH −14.7 (3) vs none +8.2 |

2m chart-CSV check (10/19, MGC 2m 11 setups / MES 2m 16 setups with results): range gate 24/5 blocks only winners on MGC 2m (+6.8) and is neutral on MES 2m; 6-7 ATR and VWAP stretch also hurt. Only hint: MES 2m long against bearish 1H CBC (3 losers, −19.2; 5 trades total −8.3) and an MES 2m afternoon cluster on 10/19 (6 of 9 losers 10:32-14:38). Watch Stats with MES + 2m: MTF box + Time-of-day box. Keep 2m gates off. 2m range-gate sweep (10/19: N 24–42 bars = 48–84 min, zone 20/25 %, under 4–8 ATR, momentum exempt): no combination helps -- best is +5.9 from blocking ONE MGC 2m trade (N 39–42, 20 %, < 6 ATR); most combinations block winners (MES 2m −5 to −16). Keep `MGC 2m 0, MES 2m 0` and re-run at 20+ setups per 2m case. 2m cases: too few setups (11 each) to set anything; range gate / stretch cap so far HURT on 2m. 3m-only candidates: `MGC 3m 5, MES 3m 5` (range gate), `MGC 3m 4` (stretch).

**10/20 2m + 5m check (chart CSVs to 10/20):**
- **BarFeed caveat:** BarFeed's "HTF timeframe" input is fixed at 15, so 2m/5m bar data (hc/h9/h20) carried 15m flips, not 10m/25m. Set it to 10 on the 2m BarFeed and 25 on the 5m one. Replays now rebuild the 10m/25m CBC from the chart bars (matches BarFeed 15m 100 %; 2m replay agreement 34/34 MES, 14/14 MGC).
- **MES 2m (34 setups, actual −37.6, mostly 10/19–10/20):** MTF (1H) against blocks 16, net −21.9, helps in both halves (−8.1 / −13.8). Flips ≥ 4 blocks 12, net −21.8, but almost all of it is in the 2nd half (−0.5 / −21.3). Exits: SL 1.3 no min + TP1 2.0 100 % −30.5 → −5.2 (better in both halves). NY session 17 setups −43.5. Candidate: MTF gate for MES 2m only; re-check exits at 40+ setups.
- **MGC 2m (14 setups, −3.0):** nothing clear; keep as is.
- **MES 5m/25m:** 1 setup so far. Flip-only proxy 9/30–10/19 (side gate, current exits): 3m/15m +0.70 per trade, 5m/15m +0.67, 5m/25m 0.00 (57 trades, halves −22 / +22). 25m flips looked weaker than 15m so far.

Last updated: 10/20/2026 (CBC v10.31, Alert Feed v138).

**Stop-loss defaults (v10.28):** SL1 = 1.3 ATR with no fixed minimum on `MGC 3m` and `MES 3m` (others 1.7 ATR + per-symbol minimum 5); time stop `MGC 3m 10` (exit before TP1 if not +0.5 ATR within 10 candles). Replay 10/12-10/19: MGC 3m −28.0 → −3.5, MES 3m +53.0 → +63.5. Watch: SL1-hit share and "Time stop" exits on Stats (MGC + 3m, MES + 3m); if net per setup drops below the 1.7-ATR baseline over 20+ new setups, revert.

**TP1 defaults (v10.31):** TP1 = 2.0 ATR on `MGC 3m` and `MES 3m` (others keep the base TP1 1.7 ATR); partial at TP1 `MGC 3m 50, MES 3m 80`; breakeven at TP1 OFF on both 3m cases (trail 1.7 ATR from the close still moves the stop). Max TP1 cap 6 pts still applies. Replay with the 1.3 SL: MGC 3m −9.7 → +10.3, MES 3m +63.5 → +82.6; 2m unchanged. Watch on Stats (MGC + 3m, MES + 3m): TP1-hit share and "How it ended"; revert if net per setup over 20+ new setups falls below the v10.28 baseline.

**Defaults set in v10.26/v10.27:** range gate `MGC 3m 5, MES 3m 5`, VWAP stretch `MGC 3m 4` (MGC 3m only); flip counter off. Watch MGC + 3m on Stats: "Gate hit" rows (Rng / Ext) should stay negative; if they turn positive over 20+ setups, remove the default.

---

## Open decisions (data still building)

| # | Feature (CBC version) | Where on Stats | What to look for | Finding so far | Decision pending |
|---|---|---|---|---|---|
| 1a | **Momentum break exempt from range gate + VWAP stretch cap** (v10.21) | Trigger row **Momentum break** + **Rng: Gate hit** filter | Momentum setups inside "Gate hit" stay positive (they are the range breakout) | Replay: 0 of 27 range-gate blocks were momentum breaks; MGC 10/19 09:36 short (4178.5 → 4162) was the case | Keep exempt unless momentum in "Gate hit" turns negative |
| 1 | **Range-position gate** (v10.20, OFF) | "Range position at setup" box + **Rng: Gate hit / Not hit** | "80–100 %, tight (< 5 ATR)" row stays clearly negative; "Gate 24 / 20 % / < 5 ATR" row Gain stays green on MGC **and** MES | 10/12–10/19: 39 blocked, 25 % win, gain +96.7 (HTML); replay 27 blocked, +80.8 (MGC +61, MES +20); < 6 ATR hurt MES | Turn on (24 / 20 / 5), or per symbol |
| 2 | **VWAP stretch cap per symbol** (v10.19, OFF) | "VWAP extension at setup" box + **Ext** filter | Cap rows: MGC 4 ATR gain stays green; MES gain only from 7–8 ATR | MGC cap 4 = +32.6; MES caps ≤ 6 cost winners; 2–4 ATR is the best band on both | Type `MGC 4, MES 8` |
| 3 | **Candle pattern confirmation** (v10.17, logging only) | "LTF pattern at setup" box + **Pat** filter | "WITH pattern" beats "No pattern" on MGC; MES no-pattern stays fine | WITH 58 % / +11.8 vs none 38 % / −25.3 (86 setups); mostly an MGC effect | Per-symbol gate "require WITH pattern" (reminder set for 10/20) |
| 4 | **Flop gate for flip setups** (v10.16, OFF) | Trigger row **HTF CBC Flip** → Flop column in the trade list; flop rule = v10.15 70 % | Flip setups marked flop vs clean: win % and net | MGC blocked 8 net −1.65, MES 4 net −6.58 (small); MGC flop flips actually beat clean ones | Leave OFF unless flops turn clearly negative |
| 5 | **Flip counter per symbol** (v10.12) | "HTF flips x/8" in the Filters line (no box yet) | Setups with flips ≥ 4 on MGC | Block ≥ 4: MGC +23.2, MES −0.9 | Type `MGC 4, MES 0` |
| 6 | **Flip volume** (v10.12) | "Flip volume at setup" box + **Vol** filter | "With ≥ 55 %" vs "Against < 45 %"; RVOL ≥ 1.2 rows | Not enough clean data yet | Possible gate "flip volume against" |
| 7 | **MTF (60m) gate** (v10.01, OFF) | "MTF CBC at setup" box + **MTF** filter | Against-MTF setups negative on both symbols? | Mixed so far | Turn on "Skip setups against the MTF" |
| 8 | **Opening range** (Stats v132) | "Opening range at setup" box (session picker) + **OR** filter | Per session: WITH vs Inside vs AGAINST | WITH −24.2 / Inside 0 / AGAINST −12 (116 setups) | Possible OR gate |
| 9 | **Order blocks** (v10.05 / v10.09) | "Order block at setup" box + **OB** filter (Near = N pts) | In same-side OB vs opposite OB vs none | Small samples | Possible "opposite OB within N pts" gate |
| 10 | **VWAP / EMA200 side gate for flips** (v9.72, ON by default) | Trade list: flip setups whose alert says "VWAP: Against" or "EMA 200: Against" | These should not appear if the box is ticked | MES 10/19 #2 / #3 and MGC 19:24 broke it, so saved settings likely have it OFF | Tick it in ▌① and check |

## Settled (keep an eye on)

| Feature (CBC version) | Where on Stats | Current setting | Re-check |
|---|---|---|---|
| ER chop block 0.23 (v9.35 / v9.94) | "Efficiency Ratio at setup" box | ON, 0.23 | 0.15–0.23 band stays worst |
| Breakout exception window 3 bars (v9.94) / skip breakout candle (v10.11) | ER box (setups below 0.23 = exception) | 3 bars, skip OFF | breakout candle itself was PF 0.55 |
| Per-trigger ER minimums (v9.96) | ER box filtered by trigger row | LTF 0.08, HTF EMA9/20 0.15, flip 0.23 | — |
| Flip side TOWARD / AWAY (v8.37 / v9.55) | trigger rows | toward OFF | — |
| SL placement / ATR SL / min SL (v9.07 / v9.53 / v10.01) | What-if box (exit rules) + ATR grid | ATR 1.7, min 5 | ATR grid best cell vs 1.7 / 1.7 |
| Trailing SL after TP1, 80 % partial (v9.07 / v9.26) | "How it ended" + "Furthest target" boxes | trail 1.7 ATR | Trail SL hit share vs TP2 reached |
| End setups 16:00 ET (v10.10) | What-if "also exit at 16:00 ET" | ON | — |
| Time of day (Stats v123) | "Time of day (ET)" box (red / green rows, N ≥ 5) | — | Asia / London hours with N ≥ 5 and negative avg |
| Timeframe pairs 15-3 vs 10-2 (Stats v127) | **TF** picker | both running | compare totals per pair |

---

### How to add to this list

New feature → add a row under **Open decisions** with: version, Stats box or filter, what number decides it, the first finding, and the pending setting. Move it to **Settled** once a default is chosen.
