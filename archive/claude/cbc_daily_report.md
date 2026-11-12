# CBC daily report -- 2026-11-12 09:57 ET

Run note: this run fired Thursday morning, so "today" = the 11/12 session so far (from Wed 18:00 ET); 11/10–11/11 are folded into "since last report" (the last written report was 11/09).
Settings sync (11/12 09:45 ET): live CBC v10.87; 0 MISMATCH, 1 known item (late_study MGCX runner base). No stale-settings warning.
Data: 44,309 alerts stored, 42,805 after removing duplicates (claude/DATA_NOTES.md: server dedupe not applied yet, `lastDedupe` null; server v14 is running). 504 setups with results (MGC 3m 74 · MGC 2m 186 · MES 3m 106 · MES 2m 138). Every setup matched to bars (no BarFeed-gap skips).
Today (session 11/12 so far): MGC 3m 0 · MGC 2m 6 · +1.9 · MES 3m 1 · −18.7 · MES 2m 3 · −14.8.

**Gate checks:**

- MES 2m flip counter + 1H MTF gate are live: 0 MES 2m setups with "HTF flips 4/8"+ or 1H against since 10/28.
- 3m range gates are live: 0 MGC 3m / MES 3m setups whose alert shows "≥ 80 % of 24-bar range, < 5 ATR" (non-momentum).
- MES 3m flip-timing gate: no late pierce setups since 11/06 (latest pierce setups came 1–5 bars after the HTF flip).
- **MGC 2m gates (v10.77) still NOT confirmed live.** There's one more range-gate violation: 11/10 19:00 LONG, LTF EMA20 Pierce (late), alert "Range: 99 % of 24-bar range · 4.1 ATR", result +2.8. That makes 2 since 11/06.
  - Non-flip setups with a "Flip flop" line kept coming: 9 since 11/06 08:46, 6 of them since 11/10 (net +7.4).
  - Together with the duplicate MGC 2m alert in DATA_NOTES, this suggests one MGC 2m alert is still running an older CBC version or older settings.
  - Action: confirm the MGC 2m chart has v10.87 loaded and only ONE CBC alert, then recreate it.

## Verdicts

- **MGC 3m (50 % at TP1 / trail 3.5 from 11/09):** 7 setups · +32.5 (+4.64/setup) vs the 10/29–11/07 baseline (80 % / 1.7) 29 · −24.3 (−0.84/setup; halves −30.1 / +5.8).
  - The runner made +29.3 of the +32.5, almost all from the 11/08 19:24 long (+24.9 on the runner).
  - Caveat (DATA_NOTES): a second, old-exit MGC 3m alert ran from 11/08 to 11/12. Where two results existed, the "0.5×(TP1)" one was used. The 3 setups without a TP1 breakdown (2 SL1 hits, 1 flip) are the same either way.
  - **Revert flag: not checkable.** The count starts 11/13 per DATA_NOTES (0/20).
- **MES 3m (SL1 3 ATR / TP1 1.75 ATR, from 11/03, excluding the 11/06 TP1 2.0 day):** 18 setups · +2.1 (+0.12/setup), halves +10.7 / −8.6. SL1-hit 22 % (4), TP1-hit 39 % (7).
  - Today's 09:30 short flip lost −18.7 (SL1). It took the per-setup net from +1.22 to +0.12.
  - TP1 2.0 day (11/06): 3 · −22.2.
  - Base 1.7/1.7 (10/28–10/30): 5 · −0.8.
  - Under 20 setups on these exits, so no judgment.
- **MGC 2m:** 186 · −51.9 all stored. Since v10.77 (11/06 08:46): 42 · +9.3 (+0.22/setup), and 11/11–11/12 sessions 19 · +26.5. That's better than the −0.40 watch baseline, but the gates don't look fully live (see above).
- **MES 2m:** 138 · −66.5 all stored. 11/11–11/12 sessions 11 · +5.1. Today's 3 setups: 2 losing shorts on flips (−13.1) and 1 small loss on a pierce.
- **MES 3m bot set** (bot windows, Flip or LTF EMA20 Pierce closed beyond EMA9, 5-day-EMA short filter):
  - Since 10/19: 19 setups · official +64.0 · bot replay (100 % at TP1) +60.9 (+3.20/setup), halves +8.6 / +52.3.
  - Since 11/09: 0 setups.
  - **Today the 5-day short filter skipped the 09:30 Flip short, which lost −18.7 on the chart.** The filter has now skipped 2 shorts (−23.7 in total).

## Gate table (all stored 10/19 → 11/12, after dedupe · blocked · win % · net of blocked · halves h1 / h2; negative = gate would have helped)

| Gate | MGC 3m (74) | MGC 2m (186) | MES 3m (106) | MES 2m (138) |
|---|---|---|---|---|
| Range 24/20 %/<5 ATR (live 3m; MGC 2m v10.77) | 3 · 33 % · −8.1 | **38 · 50 % · −28.2 (−20.1 / −8.2)** (gate should be live) | 2 · 0 % · −14.0 | 27 · 52 % · −6.5 (−19.8 / +13.3) |
| Range <6 ATR | 6 · 33 % · −6.8 | 51 · 47 % · −37.9 (−29.8 / −8.1) | 9 · 44 % · +3.1 | 37 · 51 % · −7.8 (−18.1 / +10.3) |
| VWAP stretch >4 ATR (live MGC 3m) | 2 · 50 % · −3.0 | 70 · 53 % · +17.6 (hurts) | 22 · 41 % · −8.4 (+1.4 / −9.8) | 64 · 48 % · +5.3 |
| VWAP stretch >6 ATR | 1 · +2.0 | 44 · 57 % · +25.8 (hurts) | 10 · 50 % · −10.8 (+10.4 / −21.2) | 40 · 45 % · −8.5 (−16.2 / +7.6) |
| Flips ≥ 4/8 | 7 · 86 % · +54.2 (hurts) | 30 · 30 % · −40.9 (−16.6 / −24.2) | 21 · 48 % · −11.8 (+18.1 / −29.9) | 18 · −49.3 → live `MES 2m 4` |
| 1H MTF against | 34 · 38 % · +0.9 | 73 · 48 % · −22.1 (+6.8 / −28.9) | 37 · 43 % · −5.2 (−10.2 / +5.0) | 16 · −21.9 (gated) |
| Side gate | 0 | 0 | 0 | 0 |
| Opposing OB before TP1 | **25 · 36 % · −21.0 (−18.8 / −2.3)** | 78 · −16.8 (−3.5 / −13.4) | 37 · +0.6 | 42 · +2.0 (−49.1 / +51.1) |
| Level/OB < 0.5× TP1 | 55 · −1.3 (−0.6 / −0.6) | 130 · −29.2 (−13.2 / −15.9) | **71 · 44 % · −62.0 (−35.2 / −26.8)** | 78 · −32.5 (−77.9 / +45.4) |
| Flip flop warning | 44 · 48 % · +20.3 (hurts) | **75 · 40 % · −70.7 (−52.2 / −18.5)** → v10.77 | 67 · 51 % · +35.3 (hurts) | 63 · 41 % · −62.6 (−66.3 / +3.7) |
| 15m EMA cloud against | **29 · 34 % · −41.3 (−18.8 / −22.5)** | 53 · −24.1 (−10.4 / −13.7) | 25 · +17.4 (hurts) | 16 · −21.1 (−35.1 / +14.0) |

Pattern WITH vs none: MGC 3m 20 · −15.0 vs 54 · +13.3; MES 3m 39 · −44.5 vs 67 · +27.6; MGC 2m −17.7 vs −34.2; MES 2m −26.0 vs −40.5.

Note: some MGC 2m / MGC 3m setups on 11/10 show VWAP extensions of ±18–29 ATR. That looks like a BarFeed VWAP glitch that day, which inflates the 11/10 rows in the stretch gates.

### Watch items

**Pullback, LTF EMA20 Pierce (< 0.75 ATR vs ≥ 0.75 ATR):**

| Case | Shallow < 0.75 ATR | Shallow halves | Deep ≥ 0.75 ATR |
|---|---|---|---|
| MGC 3m | 10 · −28.4 (−2.84/setup) | −7.7 / −20.7 | 33 · +32.4 |
| **MGC 2m (candidate)** | 18 · −20.8 (−1.15/setup) | −21.3 / +0.5 | 79 · +4.8 |
| MES 3m | 5 · −7.9 | −11.6 / +3.7 | 61 · −22.6 |
| MES 2m | 18 · −23.8 | −28.1 / +4.3 | 61 · −19.5 |

The MGC 2m candidate has 18 setups (under 20), and its 2nd half is now slightly positive. No change.

**MES 3m HTF EMA9 Pierce pullback:** > 2.5 ATR is 4 · −4.8 vs ≤ 2.5 ATR 33 · −38.8. No signal.

**MES 3m HTF EMA slope (both 15m EMA slopes ≥ 0.5 pt vs < 0.5):**

- ≥ 0.5 pt: 52 · +52.8 (+1.01/setup), halves −11.8 / +64.6.
- < 0.5: 54 · −69.7 (−1.29/setup), halves −27.1 / −42.5.
- On the current exits only: ≥ 0.5 is 12 · +28.3, < 0.5 is 6 · −26.2.
- The < 0.5 group is negative in both halves, but this mixes exit versions. The gate stays Off per the checklist; it's worth a fresh slope study once the current exits reach 20+ setups.

**Room/context:** MGC 3m opposing OB and 15m cloud, and MES 3m L5, are negative in both halves. Room gates stay watch-only unless the daily room task or the Friday room study recommends one.

## Losers today (session 11/12 so far)

| Case | Time | Dir | Trigger | Result | Ended | Gates |
|---|---|---|---|---|---|---|
| MGC 2m | 11/11 21:28 | L | LTF EMA20 Pierce | −5.70 | SL1 hit | F,FL,L5,M |
| MGC 2m | 11/11 21:40 | S | HTF CBC Flip | −5.85 | SL1 hit | F,FL,**R5**,R6 |
| MES 3m | 11/12 09:30 | S | HTF CBC Flip | −18.70 | SL1 hit | – (bot: skipped by 5-day short filter) |
| MES 2m | 11/11 19:00 | S | HTF CBC Flip | −7.72 | SL1 hit | FL,R5,R6 |
| MES 2m | 11/11 19:50 | S | HTF CBC Flip | −5.38 | SL1 hit | FL |
| MES 2m | 11/11 22:08 | L | LTF EMA20 Pierce | −1.75 | CBC flip | CL,FL,L5 |

## Suggested changes

None meet the rule this run (20+ setups for the case, evidence holds in both halves).

**Withdrawn: MES 2m non-flip flop gate** (standing since 11/06: add `MES 2m 1` to "...also skip NON-flip setups while the HTF flip is a flop"). The 11/10–11/11 sessions reversed it.

- Non-flip FL setups: 44 · −73.9 (−1.68/setup) vs no FL 57 · +13.6.
- Gate halves: −77.8 / **+3.9**, so the recent half no longer supports it.
- Since 11/10: FL 10 · +29.6. Since 10/28: FL 22 · −1.4 vs no FL 27 · +34.8.
- Kept as a watch item.

Not a settings change, but needed:

- **MGC 2m: confirm v10.87 is loaded, delete any duplicate CBC alert, and recreate the alert.** The range gate and the non-flip flop gate are still letting setups through (11/10 19:00 at 99 % / 4.1 ATR; 6 non-flip "Flip flop" setups since 11/10).

Done (not suggestions):

- MGC 3m 50 % / trail 3.5 (v10.84)
- MES 3m exits (SL1 3 / TP1 1.75)
- MGC 2m range + flop gate (v10.77; see the check above)
- MES 3m flip-timing gate
- Bot windows and the 5-day short filter
- MES 2m flip counter and MTF gate
