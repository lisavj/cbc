# CBC daily report -- 2026-11-16 17:27 ET

**STUDY SETTINGS STALE:** settings sync (11/13 16:47 ET) still lists 3 MISMATCHES vs CBC v10.96: `mes3_ema_grid.py LIVE` part 'tod' (live MES 3m is 100 % at TP1 all day since v10.95), `chop_sim.py EXIT[('MES',3)]` part 'tod', and `chop_sim.py EXIT[('MGC',3)]` 50 % / trail 3.5 (live MGC 3m is FLIP 0 % since v10.96). This report reads live alert results only, so its numbers are not affected; the replay studies are. Fixes: claude/settings_sync_report.md, section C.

**Checklist step 4 is out of date** (it describes v10.87). Live is v10.96: MES 3m 100 % at TP1 all day (v10.95); MGC 3m FLIP 0 % (v10.96: nothing closed at TP1, BE, no trail, exit on HTF flip / BE / 16:00 / next setup); bot = three triggers (v10.88) + news blackout (off). The MGC 3m "50 % / trail 3.5" revert flag is superseded.

## Data problems today (check TradingView)

1. **MES 2m alerts stopped Sun 11/15 19:22 ET** -- no MES 2m alert of any kind for ~22 h (normal is 200-300/day). BarFeed MES 2m is current, so the chart is live but the CBC alert is not firing. MES 2m has 0 setups today.
2. **MES 3m alerts stopped after 14:30 ET** (last: 14:27 Trade Setup SHORT). The 14:57 HTF flip and later events sent nothing.
3. **MES 3m TP1 closes send no "Setup Ended" (likely v10.95 side effect).** The 12:30 short (7476, TP1 7463.95) hit TP1 at 13:03 by the bars while the alert was still firing (14:03/14:09 alerts arrived) -- no result alert. The 14:27 short (7441.75, TP1 7429.72) hit TP1 at 14:39 -- no result alert. With 100 % at TP1 every TP1 winner may now be missing from the stored results, so **MES 3m live stats since v10.95 are biased toward losers**. Today recorded −16.8 (3 losers); with the two TP1 closes (~+12.0 each by the bars) MES 3m was about **+7.3**. No MES 3m alert ever ended with a "TP1" reason, so check whether CBC emits Setup Ended when 100 % closes at TP1.
4. **MGC 3m alerts silent Sun 22:21 ET -> Mon 14:39 ET** (~16 h) while MGC 2m / 5m fired normally. It is firing again since 14:39 (alert recreated?).
5. Store still not de-duplicated (`lastDedupe` null); the script de-dupes 11/08-11/12 copies itself. 48,917 alerts after dedupe (10/19 -> 11/16).

## Verdicts

- **MGC 3m (FLIP 0 %, from 11/13 11:00):** 4 setups · +2.1 (11/13 12:57 −1.8 may be on the old exit; 11/15 20:33 BE 0.0 after TP1; today 15:30 flip short +6.9 at 16:00). Earlier: 10/29-11/07 (80 % / 1.7) 29 · −0.84/setup; 11/09-11/12 (50 % / 3.5, partly old exits) 9 · +4.18/setup. Judge FLIP 0 % at 20+.
- **MES 3m (SL1 3 / TP1 1.75, from 11/03, excl. 11/06 TP1 2.0):** 23 recorded · −25.7 (−1.12/setup), halves +10.2 / −36.0; SL1 hit 5 (22 %), TP1 reached 7 (30 %). Earlier exits 88 · −0.22/setup. Since v10.95 the two unrecorded TP1 winners today would make it 25 · ≈ −1.7 (−0.07/setup). Halves disagree + recording bias -> no verdict.
- **MGC 2m (since v10.77, 11/08 18:00):** 68 · −35.5 (−0.52/setup), halves +0.9 / −36.3. Today 4 · −7.7 (3 longs lost; all flagged L5 + OB).
- **MES 2m:** 146 · −99.7 all stored; 0 today (alert dead, see above).
- **MES 3m bot set** (windows; Flip + LTF EMA20 Pierce beyond / not beyond EMA9; 5-day short filter; 100 % at TP1, 0.5 pt cost; TP1 closes estimated from bars): today 05:36 L −7.0, 08:30 Flip S −10.0, 12:30 Flip S ≈ +11.6 (unrecorded TP1) -> ≈ −5.4. Since 10/19 ≈ 44 · +33.6; since 11/09 ≈ 6 · −37.1. 14:27 short was outside the windows; 5-day EMA (~7579) was above price, so shorts were allowed. "LTF not beyond EMA9": none today (23 · +6.4 unchanged).

**Gate checks:** MES 2m: 0 setups since 10/28 with flips ≥ 4 or 1H against -> gates live. MGC 3m / MES 3m range gate: 0 bar-based violations since 10/28. **MGC 2m range gate:** 12 bar-based violations since v10.77, all 11/09 05:22 -> 11/12 11:40 (the duplicate old alert); none since 11/12 -> looks live now (the 11/13 11:26 alert-text case not flagged by bars). MGC 2m non-flip "Flip flop" setups: last 11/12 05:32 -> flop gate looks live. MES 3m flip timing: today's 05:36 LTF pierce came 1 HTF bar after the flip -> nothing late.

## Gate table (all stored 10/19 -> 11/16: blocked · win % · net of blocked (halves h1 / h2); negative = gate would have helped)

| Gate | MGC 3m (82) | MGC 2m (212) | MES 3m (111) | MES 2m (146) |
|---|---|---|---|---|
| Range 24/20 %/<5 ATR (live 3m + MGC 2m) | 3 · 33 % · −8.1 | 39 · 49 % · −34.6 (−37.2 / +2.6) | 2 · 0 % · −14.0 | 27 · 52 % · −6.5 (−19.8 / +13.3) |
| Range <6 ATR | 6 · 33 % · −6.8 | 57 · 46 % · −49.7 (−46.9 / −2.8) | 9 · 44 % · +3.1 | 39 · 51 % · −10.5 (−18.1 / +7.6) |
| VWAP stretch >4 ATR (live MGC 3m) | 2 · 50 % · −3.0 | 80 · 51 % · +3.7 | 24 · 38 % · −34.2 (+1.4 / −35.6) | 67 · 46 % · −18.7 (−13.7 / −5.0) |
| VWAP stretch >6 ATR | 1 · +2.0 | 51 · 55 % · +15.8 | 12 · 42 % · −36.6 (+10.4 / −47.0) | 41 · 44 % · −16.5 (−16.2 / −0.4) |
| Flips ≥ 4/8 | 7 · 86 % · +54.2 (hurts) | **35 · 29 % · −54.6 (−16.6 / −38.0)** | 22 · 50 % · −6.5 (+18.1 / −24.7) | 18 · −49.3 -> live `MES 2m 4` |
| 1H MTF against | 37 · 38 % · +6.0 | 80 · 48 % · −24.6 (−8.9 / −15.7) | 38 · 45 % · 0.0 | 16 · −21.9 (gated) |
| Side gate | 0 | 0 | 0 | 0 |
| Opposing OB before TP1 | 27 · 41 % · −11.8 (−18.8 / +7.0) | 92 · 47 % · −49.1 (−13.9 / −35.2) | 38 · 50 % · −5.9 | 43 · +5.9 |
| Level/OB < 0.5× TP1 | 58 · −4.0 | 153 · 46 % · −64.3 (−30.8 / −33.5) | **74 · 43 % · −64.0 (−37.3 / −26.8)** | 80 · −35.2 (−76.8 / +41.5) |
| Flip flop warning | 48 · +26.6 (hurts) | 76 · −67.8 (−67.1 / −0.7) -> v10.77 | 69 · +39.8 (hurts) | 67 · −66.5 (−67.8 / +1.3) |
| 15m EMA cloud against | **31 · 35 % · −40.7 (−17.4 / −23.3)** | 60 · −37.6 (−20.5 / −17.1) | 26 · +22.7 (hurts) | 17 · −26.4 |

Pattern WITH vs none: MGC 3m 21 · −12.3 vs 61 · +27.0 · MGC 2m 71 · −28.8 vs 141 · −67.9 · MES 3m 40 · −60.8 vs 71 · +16.1 · MES 2m 56 · −32.8 vs 90 · −66.9.

**MGC 2m flips ≥ 4 (closest to a suggestion):** since v10.77 still 13 · −38.0 (−12.7 / −25.3); non-FL part 11 · −26.4 (−12.1 / −14.3). No new ones today. Becomes a suggestion (`MGC 2m 4` in the flip counter) at 20+ since v10.77 with both halves negative.

### Watch items

**Pullback, LTF EMA20 Pierce (< 0.75 ATR shallow vs ≥ 0.75 deep):**

| Case | Shallow · net | Shallow halves | Deep · net |
|---|---|---|---|
| MGC 3m | 11 · −21.2 | −7.7 / −13.5 | 37 · +33.9 |
| **MGC 2m (candidate)** | 21 · −19.2 | −28.3 / +9.0 | 93 · −20.4 |
| MES 3m | 6 · −24.2 | −7.9 / −16.3 | 63 · −23.8 |
| MES 2m | 19 · −31.8 | −28.1 / −3.7 | 67 · −36.7 |

MGC 2m reached 21 shallow setups but the 2nd half is positive (+9.0; since v10.77 6 · +4.6) -> no change.

**MES 3m HTF EMA9 Pierce pullback:** > 2.5 ATR 5 · −5.6 vs ≤ 2.5 ATR 35 · −61.6 (no support for a cap).

**MES 3m 15m EMA slopes:** both ≥ 0.5 pt 54 · +27.0 (−18.2 / +45.2) vs < 0.5 57 · −71.7 (−20.5 / −51.2). On current exits 14 · +2.5 vs 9 · −28.2. Blocked side negative in both halves, but the kept side is not positive in both -> gate stays Off (watch).

**Room/context:** MES 3m L5 and MGC 3m 15m cloud are negative in both halves but stay watch-only. Room daily task (11/13): MES 3m 0.2× TP1 still "candidate, waiting for out-of-sample" -> not a suggestion. Today it would have blocked 10:51 (0.12×, −0.75) and the unrecorded 14:27 TP1 winner (0.10×).

## Losers today (session from Sun 11/15 18:00 ET)

| Case | Time | Dir | Trigger | Result | Ended | Gates |
|---|---|---|---|---|---|---|
| MGC 3m | 11/15 19:12 | L | LTF EMA20 Pierce | −3.00 | CBC flip | FL,L5 |
| MGC 2m | 11/16 04:04 | L | LTF EMA20 Pierce (late) | −5.30 | SL1 hit | L5,M,OB |
| MGC 2m | 11/16 07:30 | L | LTF EMA20 Pierce + HTF EMA9 | −5.00 | SL1 hit | L5,OB |
| MGC 2m | 11/16 14:46 | L | LTF EMA20 Pierce (late) | −1.10 | CBC flip | L5,M,OB |
| MES 3m | 11/16 05:36 | L | LTF EMA20 Pierce (beyond EMA9) + HTF EMA9 | −6.50 | CBC flip | L5,OB (bot ≈ −7.0) |
| MES 3m | 11/16 08:30 | S | HTF CBC Flip | −9.50 | CBC flip | X4,X6 (VWAP +6.7 ATR; bot ≈ −10.0) |
| MES 3m | 11/16 10:51 | S | HTF EMA9 Pierce | −0.75 | CBC flip | FL,L5 |

Winners recorded: MGC 3m 15:30 S Flip +6.9 (16:00), MGC 3m 20:33 S BE 0.0, MGC 2m 05:08 L +3.66. Unrecorded (no Setup Ended): MES 3m 12:30 S Flip ≈ +12.05, 14:27 S Flip ≈ +12.03 (TP1 by bars).

## Suggested changes

None meet the rule this run (20+ setups for the case and evidence in both halves). No standing items from earlier days. MGC 3m revert flag superseded by FLIP 0 %.

Not settings changes, but needed:

- **Recreate / check the MES 2m CBC alert** (silent since Sun 19:22 ET) and the **MES 3m alert** (silent since 14:30 ET). If the ▶ Bot runs on the MES 3m alert, check that it is still sending.
- **Check MES 3m "Setup Ended" on 100 % TP1 closes** (v10.95+): two TP1 closes today sent no result.
- **Study scripts:** apply the 3 MISMATCH fixes in claude/settings_sync_report.md, section C.

Done (not suggestions): MGC 3m exits (FLIP 0 %, v10.96); MES 3m exits (SL1 3 / TP1 1.75, 100 % at TP1, v10.95); MGC 2m range + flop gate (v10.77); MES 3m flip-timing gate; MES 2m flip counter + MTF gate; bot windows, 5-day short filter, three-trigger set (v10.88), news blackout (v10.94).
