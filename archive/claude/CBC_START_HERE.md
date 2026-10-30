# CBC — START HERE (v9.06 baseline)

Fresh summary as of **10/14/2026**. Baseline: **CBC v9.86 + ESLib v99 rev29 (published **/48**; rev28 = /45; rev27 never published; rev26 = /42; rev25b = /40) + **ESLib2 v3** (published **/5**; v2 = /4; v1 = /1; older: rev23 = /37; rev21 → /35 placeholder; rev20 → /34 placeholder (never confirmed); v9.24 on /33 = rev19; v9.22 ran on /32 = rev18; rev17 = /31; v9.18 on /29 = rev15 confirmed working; v9.17 ran on /28 = rev14 presumably; /27 = rev11 or rev12 unconfirmed; rev11 = /26) + Alert Feed web v119 + server.js v6 + BarFeed v1.02 + CHT v1.01 + HTF v1.01**. Read this first in any new thread. Older detail: the changelog block at the top of `CBC_v9_06.pine` (one line per version), `CBC_handoff_v8_74.md`, `CBC_session_handoff.md` (v6.97–v7.92 + conventions), `CBC_future_improvements.md` ("Parked, do NOT re-offer"), `CBC_trading_playbook.md` (the user's trading rules).

---

## 1. What this is
- **CBC**: large TradingView **Pine v6 indicator** (~5,700 lines) for MES/MGC futures, traded live on **3m (LTF) with 15m (HTF)**. The user reports issues with screenshots.
- **ESLib**: companion Pine **library** (imported as `obLib`) holding helpers moved out of CBC to stay under TradingView's size limits.
- **Alert Feed** (`index_v82.html`): the user's TradingView webhook dashboard (deployed at tv-webhook-dashboard.onrender.com; their server.js: `/alerts`, `/stream` SSE). Parses CBC `alert()` text — **don't change existing alert line formats**.
- **CHT**: separate chart-timeframe indicator (15m signals on the chart TF, works on 10m etc.), alerts prefixed "• CH15 …".
- **HTF**: small standalone 15m indicator the user added (fixed TP/SL setups). Not touched by Claude.

## 2. Files (authoritative copies in the Claude Project)
| File | Version | Notes |
|---|---|---|
| `pine/CBC_v9_06.pine` | **v9.06** | `indicator("v9.06", …)`; `import samuelsuss8/ESLib/24 as obLib` |
| `pine/ESLib.pine` | **v99 rev11 = /26** (user confirmed 10/08; BarFeed still imports /23) | 90 exports; rev11 = flop label "⚠ 200 V" (V = VWAP) + trailing SL1 (`f_ats_draw_setup` +trail, `f_ats_track(new, c[], tp3, tp4, …, trail)`) — signatures changed, so CBC v9.07 needs rev11. Lib lexical 25,003 (rev10 24,866). |
| `web/index_v118.html` | **Alert Feed v118** (Chart tab + inline chart + full size / pop out + price zoom, any feed TF) | keep top version comment + `<footer>` in sync |
| `pine/CHT_v1_01.pine` | **CHT v1.01** | imports ESLib/18 (fine; rev7/rev8 only ADDED exports) |
| `web/server.js` | **server v4** (10/07; v3 = store key per symbol+TF: `MES` = 3m, `MES_2` = 2m; v4 = newest candle appended, no rewrite) | bar store `/data/bars/<SYM>.ndjson`, `GET /bars`, `POST /bars/import`, SSE `event: bar` |
| `pine/BarFeed_v1_02.pine` | **BarFeed v1.02** | imports ESLib/23; one JSON alert per closed candle + (v1.01) the forming candle once per new minute (`"live":1`, freq_all, input `live_on` ON) |
| `pine/HTF_v1_01.pine` | **HTF 1.01** | user's file, no library |

**Library numbers:** /18 = v99 rev6 · /19, /20 = rejected builds (never import) · rev7 never confirmed separately · /22 = rev8 · /23 = rev9 · **/24 = rev10 (imported by CBC v9.06)** · **/26 = rev11 (current, CBC v9.11)**. /25 never confirmed (do not import). 10/06 the user uploaded the library as "ESLib_28.pine" (content = rev8) — asked whether it is published as /28; unanswered, import left at /22. Next republish: **ask the user for the real number** before setting the import (never guess).

## 3. Workflow (every round)
1. **One small change per version.** New features default **OFF** unless the user asks otherwise. Restate behaviour in 2–3 lines before multi-option features. Short answers.
2. Bump filename + `indicator("vX.YZ")`; one changelog line under the previous one (before `//@version=6`).
3. Verify (no Pine compiler here — tools rebuilt each session in the scratchpad):
   - paren/bracket balance (comment/string-stripped) = 0/0;
   - arg count of EVERY `obLib.` call vs EVERY export;
   - **code-token count** (`tok2.py`: lexical tokens excluding `x = input.*` lines);
   - **naive top-level statement count** (non-indented, non-comment lines).
4. HTML changes: test with Playwright mocks (python mock server for `/alerts` + `/stream`, node script checks).
5. Deliver (SendUserFile), save to project, **delete the superseded file**, update this doc. Only ONE CBC .pine, ONE ESLib, ONE index html in the project.
6. After a Pine update the user: publishes ESLib (if changed) → pastes CBC over the existing copy (keeps settings) → **recreates the TradingView alert**. New inputs on an existing copy start at their default; a newly added copy uses all defaults (common source of "it didn't work").

## 4. Size limits & Pine lessons
- **CE10117 (tokens):** `input.*` lines do NOT count. Code-token ceiling ≈ **23,750** (v8.78 23,750 compiled; v8.79 23,813 failed = 100,419 real). **v9.00 ≈ 23,741 (9 left!)** (this session's tok2 reads 66 lower: 23,675). Any new feature needs relief first. Relief: move pure helpers / alert text builders to ESLib, inline single-use vars, merge mutually-exclusive long/short alert branches (only if truly exclusive — ORB pairs are NOT), reuse `htf_dir_bull_now` etc.
- **CE10295 (main body too long):** counts top-level statements incl. inputs. **v8.94 failed at ~1,387 naive; v9.00 = 1,373.** Wrap new globals in a local function returning a tuple (e.g. `f_ats_hdir()`), fold top-level `if` alerts into existing functions.
- Library exports can't return tuples; libraries can't `alert()`. Local functions can return tuples.
- No array literals outside `options=[...]` (CE10156). `var bool x = na` → `bool(na)`. `na != x` is false → guard with `na()`.
- `varip` survives realtime tick rollback; intrabar drawings are rolled back each tick unless latched (see `f_tch`).
- Known: `htf_ema9/20` use `lookahead_on` without `[1]` (history repaints). Confirmed HTF CBC (`htf_cbc_labels_f`, `[1]` + lookahead_off) registers **~one HTF candle late on history** (8:30–8:45 flip shows ~8:57); live it's on time. The anticipatory red dot on history uses lookahead (sits early) — setups never use it.

## 5. Key variables
- `cbc` = LTF live. `htf_cbc` = live HTF CBC (lookahead_on). `htf_cbc_labels_f` = confirmed HTF (1/0). `htf_dir_bull_now/bear_now` = confirmed direction (defined right after `htf_cbc_labels_f`).
- **Setup engine copies (v8.94+, from `f_ats_hdir()`):** `ats_hb/ats_hs` (dir), `ats_fb/ats_fs` (flip event), `ats_aw` (flip away from HTF EMA20), `ats_fch/ats_fcl` (flip candle H/L), `ats_flip_ok`, `ats_eod`, `ats_tol`. With `ats_hc_on` OFF they equal the confirmed versions.
- `ats_call` = [entry, SL1, TP1, SL2, TP2]; `ats_state` = [entry, TP1, SL1, TP2, SL2, long, live]; `ats_last_draw_bar`; `ats_llg` = last setup was long.

## 6. Auto Trade Setup — current behaviour (v9.00)
**Triggers** (`f_ats_trig()`; "Setup Triggers" group lets the user pick which are on): LTF EMA20 Pierce (+late), HTF EMA9 / EMA20 Pierce (+late), HTF CBC Flip (optional pullback wait), HTF Pullback Structure, Momentum break, **LTF EMA20 Touch** (draws mid-candle and stays, latched via `f_tch`).
**Gates:** closed candle (except touch), `ats_flip_ok`, not 17:00 ET bar, **no new setups 16:00–18:00 ET** (`ats_q_on`), Trade Setup Filters, VWAP reclaim block (5 bars) + Pivot R1–R3/S1–S3 reclaim block, cloud rule (`ats_req_clear`, default **OFF**).
**Spacing:** "Min candles between setups" **10** (`ats_cd_bars`). Exceptions: HTF CBC Flip setups; once the HTF flips against the last setup, the new direction may draw immediately; optional "HTF EMA9/EMA20 Pierce replaces the current setup" (`ats_hs_on`, OFF). During the wait a same-direction trigger sends **"• Setup Confirmed: LONG/SHORT / By: … / Setup Entry: x"** (no box).
**HTF flip timing:** "Setups: act on HTF flip at the HTF candle close" (`ats_hc_on`, **default ON since v9.00**) — on the chart candle that closes the HTF candle (8:42–8:45), the engine takes the HTF CBC as it closes → old setup ends + flip setup draws at 8:45 on history and live. Needs chart TF to divide the HTF evenly (3m/15m, 2m/10m). Verified on the user's 10/6 MGC chart when ON. User asked whether the setup should end at the red dot → answered: with ON it ends on the candle right before the dot candle; offered to make it default ON (unanswered).
**Filters (Trade Setup Filters, all OFF):** chop (CI > 61.8), VWAP stretch (> 3 ATR), frequent HTF flips, **Block if VWAP from -X / +Y**, **Block if EMA200 from -X / +Y** (v9.00, separate, defaults 3 / 2, OFF): signed in the HTF CBC direction (`ats_hb`, local fn `f_nz`) — LONG blocks while close is 3 below to 2 above the level; SHORT mirrored (3 above to 2 below). Inputs `ats_nv/ats_nv2`, `ats_ne/ats_ne2`.
**Levels:** pivot pool (R/S, YDH/L, PMH/L, HTF/LTF pivots, EQH/EQL, EMA200, VWAP, OR H/L), Min SL distance **6** pts, **ATR methods ON by default (v8.98): SL1 2× / SL2 3×, TP1 2× / TP2 3×, ATR 14**. "Show TP2" (OFF since v9.04) / "Show SL2" (OFF since v9.03) checkboxes hide TP2/SL2.
**On chart:** setup boxes; "Keep previous setup" ON; freezes on TP2/SL2 breach, HTF flip against it, 17:00 ET. **ⓘ label** left of each new setup's Entry (`ats_info_on`, ON) — tooltip: LONG/SHORT @ entry, Trigger(s), **Candle: H:MM-H:MM ET**, CBC 3m / CBC 15m, Flip side TOWARD/AWAY, flop, Fib zone.
**Alerts:** Trade Setup (text built in lib `f_ats_msg`; adds "Fib zone: IN 15m top / bot" when Entry is in the HTF Fib golden pocket), Setup Confirmed (`f_ats_conf_msg`), Setup Ended (`f_ats_track`).

## 7. Alert Feed web v82
v81: CHT support (Chart-TF Setups / Chart-TF Alerts types, "TICKER CHnn" symbol key, separate "Chart-TF setups (CHT)" section). v82: purple **FIB** badge on Trade Setup box + card when the alert has "Fib zone: IN …". **Pending (next web version):** handle "• Setup Confirmed" alerts (Alert Type, default ON) and show the confirmation count / "Confirmed by" on the matching setup (same symbol + Setup Entry).

## 7c. Chart tab (web v84 + server v2 + BarFeed v1.00, 10/07)
- **BarFeed** (3m chart, alert "Any alert() function call", same webhook URL): `{"type":"bar","sym":"MES","tf":3,"t":<open ms>,o,h,l,c,v,e9,e20,h9,h20 (15m EMAs, lookahead_on like CBC),e200,vw,pp,r1,s1,ydh,ydl,nyh,nyl,lnh,lnl,ash,asl,hc (15m CBC 1/0 taken on the 3m candle that closes the 15m one),hf (+1/-1 flip),fl (flop text via lib f_flop)}`. Same values plotted Data-Window-only (titles = keys) for CSV export.
- **server.js v2**: `type:"bar"` webhooks skip the alert list/Discord; stored per symbol (sorted, dedup by t, appended NDJSON, compacted at start, trimmed hourly to `BAR_KEEP_DAYS`=60). `GET /bars` (list) / `GET /bars?sym=MES&days=5`; `POST /bars/import?token=&sym=` (TradingView CSV: time/open/high/low/close/Volume + key columns, or JSON array; existing candles kept). SSE named event `bar` (old pages ignore it). `/health` lists bar files.
- **web v84** Chart tab (next to Alerts): Lightweight Charts 4.2 from unpkg, NY-time shift, 3m/15m (15m aggregated from 3m), 2–60 days, layer checkboxes (localStorage): 3m + 15m EMA 9/20 clouds (custom primitive), EMA200, VWAP, R1/PP/S1, YDH/YDL, NY/LN/AS OR, flop tint, 15m flip arrows, setup boxes (Entry→TP1/SL1 from Trade Setup alerts, end = Setup Ended / next setup). Tested with mock server + Playwright.
- **web v85**: `chDerive()` fills missing per-bar values from OHLC (3m EMA9/20/200, VWAP reset 18:00 ET, forming 15m EMA9/20) and ALWAYS recomputes the 15m CBC flip (hf/hc/fl) with the CBC rule at the 15m close, so CSV history without BarFeed columns still gets EMAs and flips. Flip candles drawn lime/red + "15m LONG/SHORT" arrow (+ "⚠ FLOP").
- **web v86**: blue CHART button (`chGotoBtn`, `.ch-goto`) on Trade Setup alerts (setup box header after ENDED + feed card) -> `chGoTo(id)`: Chart tab, symbol root, enough days, centred on the setup candle (`chState.focusMs`).
- **web v87**: on the Alerts page the CHART button opens the same chart INLINE above the feed (`#chartView` moved right after `#symbolTabs`, class `ch-inline`, 460px, `chInlineOpen` var, "✕ Close chart"); alerts shift down. From other pages it opens the Chart tab.
- **web v88**: EMA axis labels "3m 9 / 3m 20 / 15m 9 / 15m 20"; both clouds light green (EMA9 > EMA20) / light red.
- **web v89**: "⤢ Full size" (class `ch-full`, fixed fullscreen overlay, Esc exits) and "↗ Pop out" (`window.open("/?view=chart&popout=1&sym&tf&days")`; body class `ch-popout` hides header/footer/setup box; `chDeepLink()` handles `?view=chart`).
- **web v90**: EMA colours = CBC v9.05 defaults: 3m EMA9 #808080 1px / EMA20 #C8C8C8 2px, cloud color.green/color.red @50% transp; 15m EMA9/20 #2962FF, cloud #007A8A / #B34700 @75% transp.
- **web v91**: cloud colours follow the VIEWED TF like CBC (viewed TF = green/red 50% + grey lines; other TF = teal/orange 75% + blue lines). Vertical price zoom: `chState.vScale` via autoscaleInfoProvider (buttons ↕− / ↕+ / Fit), level lines excluded from autoscale unless "Levels in scale" (`chState.fitLevels`); mouse drag on the price axis also works.
- **web v92**: price zoom no longer calls chRender (only `chRefitPrice()` toggles autoScale) so bar spacing / scroll never change; "Range __ pts" box (`chState.vSpan`, compensates the 20%/10% scale margins); Shift + wheel = vertical zoom.
- **web v93**: 3m view outlines each 15m flip candle (box over its five 3m candles, high-low of the 15m candle, lime/red, "15m LONG/SHORT ⚠ FLOP" label; primitive `chDrawFlipBoxes`); 3m-view arrow markers lose their text.
- **server v3 + web v94**: feeds keyed `SYM` (3m, existing files untouched) or `SYM_<tf>` (e.g. `MES_2`); `/bars` list has `tf`. Web: helpers `chKeyRoot/chKeyTf/chB()/chH()` (HTF = 5 x feed TF); feed picker "MES 2m/10m", TF picker rebuilt per feed (`chTfOptions`), layer labels `{B}m/{H}m`, chDerive/flip boxes/setup snapping use chB/chH. For 2m: BarFeed on a 2m chart with "HTF timeframe" = 10. Verified 10m flips = reference (54).
- **web v95**: flop flips get an "F" marker text (below the up arrow / above the down arrow, arrow colour, size 1.4) on both views; on the HTF view it replaces the "15m LONG/SHORT" text for flop flips.
- **web v96**: setup box label = entry price only, below the entry line (direction colour).
- **web v97**: a setup starting on / one row after a same-direction flip puts its entry price on that flip arrow's marker text ("F 4146" / "4146"), box label skipped (`b.atArrow`, map `arrowPrice`).
- **web v98**: that price is a second stacked marker (shape circle size 0) so it sits on its own line under the F (long: arrow/F/price; short: F/price/arrow).
- **web v99**: chart theme White (default) / Dark (`chState.theme`, localStorage `chTheme`, button `chThemeBtn`, `chApplyTheme()`); long flip markers darker green #08A000 on white.
- **web v100**: last-price box `#chLast` top-left inside `#chHost` (`chUpdateLast()` in chRender): last close, change vs previous feed candle close (pts + %), green/red/grey, update time ET (`chState.lastRecv` = SSE receipt time, else bar close time). Real bid/ask not possible (Pine bid/ask only on 1T charts; webhooks too slow).
- **web v113**: Stats row click → `renderStatsDetail` (statsRecords): summary (win %, avg win/loss, PF, avg best/worst, duration), end reasons, result buckets, furthest TP, trade list (newest 50); window buttons.
- **web v114**: Stats detail adds What-if table (simFlipExit): exit at close of 3m bar completing opposite 15m CBC flip (pierceHc rebuilt from /bars), optional 17:00 ET (#statsEod); Actual vs What-if for All / Clean flips / Flops (alert has "Flip flop: crossed"); trade list gets Flop + What-if cols. Only setups inside BarFeed bar history. pierceRoot strips contract month codes (MGCZ2026 → MGC).
- **web v115**: What-if exit-rule selector #statsRule (statsSel.rule): flip / pl3 = flip or 3m close past prior completed 15m low (long) / high (short) / pc15 = flip or 15m close past prior 15m close. pierceHc now also returns side arrays ph/pl/pc/gc/cl.
- **server v6**: MAX_ALERTS 5000 (env MAX_ALERTS). **web v112**: Stats button → modal (renderStats): per first trigger, windows last 100 / 500 / all stored alerts, setups (L/S), win % (W/L from Setup Ended via setupOutcome), avg pts; symbol filter. Restore slice 5000.
- **CBC v9.30**: default OR shading NY/LN/AS 5% opacity (transparency 95).
- **CBC v9.29**: import ESLib/37 = rev23 (user confirmed 10/09).
- **CBC v9.28 + ESLib rev23**: input `ats_done_op` (10) → f_ats_draw_setup(+done_op); finished fill = reward_col/risk_col at (100−op)% transparency; trail steps split sub_boxes (green) / sub_boxes_r (red). top-level 1,384.
- **CBC v9.27 + ESLib rev22**: finished setup → `f_ats_hollow` sets bgcolor transparent on reward/risk/2 boxes + `sub_boxes` (run/trail steps) at the 3 freeze points (flip/eod, keep-on-new-setup, breach/SL).
- **web v111**: "Setup HH:mm" cell left-aligned, nowrap.
- **CBC v9.26 + ESLib rev21 + web v110**: TP1 partial. Inputs `ats_part_pct` (50), `ats_be_on` (ON), `ats_part_alert` (ON). f_ats_track(+part, be, part_alert): t_tp1/t_part, BE at TP1, "• TP1 Partial:" alert, blended "Result: +5.2 = 0.5×6.1(TP1) + 0.5×4.3(Trail)" (remainder label Trail/BE/SL1/Flip/17:00/New), why "Breakeven hit". f_ats_draw_setup(+part, be): "50% @ TP1" label, BE step even with trail off. Web: split shown in brackets. tok2 23,665, top-level 1,383 (CE10295 risk ~1,387).
- **web v109**: Beep for ▾ → Symbols checkboxes (localStorage `beepOffSyms` = unticked symbols; list rebuilt when the panel opens).
- **CBC v9.25** (10/09) + **ESLib rev20** + **web v108**: flip row "HTF Long 11:15-11:30 - 4" (was "HTF Flip Long"); Trade Levels row 11 merge 0..2, col 3 = "Setup HH:mm" (lib `active_t`); web setup table same (colspan 3 + "Setup HH:mm" from st.time).
- **CBC v9.24** (10/08): default flop background tint OFF.
- **CBC v9.23** (10/08) + **ESLib rev19**: trailing → reward box ends at TP1, `run_box` Entry..best close steps at each new best confirmed close; end-freezes guard reward_box with `if not tp1_hit` and freeze run_box; trail steps solid 2 px #D50000.
- **CBC v9.22** (10/08) + **ESLib rev18**: FIX — f_ats_min_sl (abs distance < min → Entry−min) pulled a trailed SL1 back down whenever the trail block was skipped (forming candle, rev17). Now `if tp1_hit: new_stop := active_stop` before the trail block.
- **CBC v9.21** (10/08): import ESLib/31 = rev17 (user confirmed). Next lib publish: ask for the number.
- **CBC v9.20** (10/08) + **ESLib rev17**: close-mode trail (trail > 0) only updates when `barstate.isconfirmed`; high/low mode live.
- **CBC v9.19** (10/08) + **ESLib rev16**: `trail_box` per trail step, Entry..trailed SL1, reward_col when SL1 past Entry else risk_col; frozen with the setup.
- **CBC v9.18** (10/08) + **ESLib rev15**: trailing on → risk box (and risk box 2) end at the TP1 candle; later freezes guarded with `if not tp1_hit`.
- **CBC v9.17** (10/08) + **ESLib rev14**: f_ats_draw_setup ends (freezes) the drawn setup when low/high crosses active_stop (pre-update) — `sl1_hit` → breach; trail not moved on that candle. Matches f_ats_track.
- **CBC v9.16** (10/08) + **ESLib rev13**: `ats_trail_hl` (OFF) — trail from high/low (live) instead of close; encoded as negative trail value (no lib signature change). tok2 ≈ 23,649.
- **CBC v9.15** (10/08): default trail ON x 1.5. File `pine/CBC_v9_15.pine` replaces v9.14.
- **CBC v9.14** (10/08) + **ESLib rev12**: trailing SL1 drawn as steps (old SL1 segment ends at the trail bar, vertical joint, new segment extend.right; risk box / SL2 box no longer move when trailing). 2 lines per trail move (max_lines 500). Placeholder import /27.
- **CBC v9.13** (10/08): `shorttitle = "9.13"` (zero-width short name hid the name in the alert dialog). **Convention: on every version bump update BOTH `indicator("v9.xx"` and `shorttitle = "9.xx"`.**
- **CBC v9.12** (10/08): touch-dot plots + OR Active H/L plots `display=display.all - display.price_scale` (no price-scale tag). Relief: local `f_tdot(on, lv)`, default plot args dropped. tok2 23,637, top-level 1,379. v9.10 shorttitle zero-width space works (labels show ":VWAP"; TradingView always adds the colon).
- **CBC v9.11** (10/08): import ESLib/26 (rev11). File `pine/CBC_v9_11.pine`; v9.06 / v9.10 removed from the project.
- **CBC v9.10** (10/08): `shorttitle = "\u200b"` (zero-width space) so scale labels drop the "v9.xx:" prefix; legend name is blank (title still v9.10). If TradingView rejects/ignores it, fall back to shorttitle "C". File `pine/CBC_v9_10.pine` replaces v9.09.
- **CBC v9.09** (10/08): plot titles renamed to web names (3m 9/20, 15m 9/20, EMA200, NY/LN/AS OR-H/L) for TradingView price-scale name labels (Chart settings → Scales → Indicators: Name). Pivots / YDH / YDL are line.new → no scale label; adding them needs plots (≈60 tokens + 5 statements) → relief first. File `pine/CBC_v9_09.pine` replaces v9.08.
- **CBC v9.08** (10/08): default cap text MGC 7 (was 8). File `pine/CBC_v9_08.pine` replaces v9.07; same placeholder import /25.
- **CBC v9.07** (10/08): "Trail SL1 after TP1 hit: x ATR" (OFF, 1.5): after TP1, SL1 = max(SL1, close − m×ATR) (long; mirrored short), chart label "SL1 trail", table Pivot "Trail", Setup Ended "Trail SL hit". trail = `ats_trail_on ? ats_trail_m * ats_atr : na` inline in both calls. Also "Max ATR SL1 (pts) per symbol" (default ON, user request) + text `ats_cap_txt` "MGC 8, MES 8, MNQ 30, M2K 5, MCL 0.3, BTC 500" → lib `f_sl_cap(on, txt)` (root map GC→MGC etc., BTC=MBT/BTC*) → `f_ats_atr_lv(…, cap)` lowers the SL1 multiplier to cap/ATR. Text input chosen over 6 number inputs to stay under CE10295. Relief: f_ats_track takes `ats_call`; "no re-pick in ATR mode" moved into lib. tok2 23,659, top-level 1,379.
- **BarFeed v1.02**: fix — live per-minute candle never fired (`varip int last_min = na`; `cur_min != na` never true). Now `= 0`.
- **server v5**: Render log names each alert ("alert MES1! | LTF EMA20 Pierce - Entry: LONG") and logs every BarFeed candle ("bar MGC 3m 10:51 ET LIVE|CLOSE c=…"). 10/08 user reports live candles only every 3 min — check log for LIVE lines.
- **web v107**: fix — failed `/bars` load (Render restart returns HTML 502) left the old symbol's candles under the new name. Now checks r.ok + JSON content-type, clears the chart and retries every 5 s up to 12 (`chRetry`, reset on symbol change / CHART click).
- **web v106**: "Beep: On/Off" + "Beep for ▾" (BEEP_KEYS: triggers flip/ltfp/ltft/h9/h20/pb/mo/other matched on parseTradeSetup().trigger, long/short, optional Setup Ended tone); WebAudio tones (long rising, short falling); localStorage beepOn/beepSel; hooked in es.onmessage → beepAlert.
- **web v105**: `chResync` — quiet `chLoadBars(true)` (keeps view) on visibilitychange and every 60 s with no SSE bar while the chart is open (iPhone pauses SSE). If live candles still only come every 3 min: the TradingView alert must be re-created on BarFeed v1.02 (alerts keep the script version they were made with).
- **web v104**: fix: symbol switch kept the old price axis when auto-scale was off (touch drag on iPhone); first fit after a load now calls `chRefitPrice()`.
- **web v103**: `chDerive` fills pp/r1/s1 from the prior CME day (18:00 ET) H/L/C when the bar has none (imported/older bars), so pivots draw every day; pivot lines 2px. Derived pivots also count in the chart flop check.
- **web v102**: pierce cards (LTF EMA20 / HTF EMA9 / HTF EMA20) get a setup-style outcome line (`pierceOutcome`), computed from `/bars` 3m: entry = alert Price, dir = Entry or Option 2 arrow side; ends at first 15m CBC flip against the trade, 17:00 ET, or 2h (`PIERCE_MAX_MS`); LIVE while running. Live bars update it (re-render ≤ every 20 s).
- **web v101**: `chGotoBtn` shows CHART on every alert card with a real ticker (not only Trade Setups).
- **BarFeed v1.02 + server v4**: forming candle re-sent at the first tick of each new minute (skips the first minute) -> server replaces it in place (append; startup reload keeps the last line per t) -> web redraws (existing same-t replace). Max 3 alerts per 3m candle per symbol.

## 8. Open items
- (done v9.00) `ats_hc_on` default ON. Existing chart copies may keep the saved OFF -- tick it by hand.
- Web: Setup Confirmed count (still pending).
- CHT has none of the v8.81+ features (16–18 window, touch trigger, 10-candle wait, flip exception, ⓘ, filters) — port only if asked.
- Offered earlier, unanswered: Fib zone touch alert / Fib as a trigger / Fib levels as TP/SL; red-dot (anticipatory) setup option (advised against); flip dot default "Both"; flop checkbox also hiding alert lines.
- Rejected: v8.77 lookahead fix for flip labels; v8.86 one-setup-per-HTF-candle; range mode; chart-TF mode in CBC.

## 9. Changelog v8.74 → v9.06 (one line each)
- v8.75 HTF CBC Flip setups bypass the cooldown · v8.76 cloud rule OFF · v8.77 "Setup Triggers" group · v8.78 VWAP reclaim block · v8.79 pivot reclaim block · v8.80 CE10117 fix (needs_brsg removed, pairs merged)
- v8.81 no setups 16–18 ET · v8.82 LTF EMA20 Touch draws mid-candle + intrabar alert · v8.83 touch setup latched · v8.84 ORB pairs split back · v8.85 cooldown 5 · v8.86 rejected · v8.87 flip-direction exception
- v8.88 Setup Confirmed alert · v8.89 cooldown 10 + ag_l fix · v8.90 HTF pierce may replace setup (OFF) · v8.91 Fib zone line in alert (+web v82 FIB badge)
- v8.92 ⓘ label + alert text to lib (rev7) · v8.93 Min SL 6 · v8.94 act at HTF candle close (OFF) + f_ats_why to lib (rev8) · v8.95 CE10295 fix (f_ats_hdir) · v8.96 import /22
- v8.97 ⓘ "Candle:" time · v8.98 ATR SL/TP defaults ON (2/3, 2/3) · v8.99 VWAP / EMA200 proximity filters · v9.00 those filters become a signed -3/+2 band in the HTF CBC direction + `ats_hc_on` default ON · v9.01 YDH/YDL color #CE93D8, PMH/PML #BA68C8 (defaults) · v9.02 London H/L #FF9800, Asia H/L #2962FF, EMA200 #FBC02D (defaults) · v9.03 Show SL2 default OFF · v9.04 Show TP2 default OFF · v9.05 flop: bigger "⚠ FLOP" label (lib rev9) + background tint `show_flop_bg` (ON) from a flop flip to the next HTF flip; web v83 FLOP badge · v9.06 import /24 (flop label "⚠ 200 / ⚠ VWAP")
- **v9.31 / ESLib rev24**: inputs "Erase older setups, keep this many back" (ats_kn_on, default OFF) + int ats_kn (0) -> keep_n (-1 = off) trailing param on f_ats_draw_setup and f_ats_info_lbl. Rolling erase by setup number (sid): every drawing pushed with its sid; on a new setup, drawings with sid <= sid-1-keep_n deleted. keep_n > 0 forces the previous setup to be kept (frozen/hollow). CBC now 23,681 tokens / 1,386 top-level -- essentially AT the ceiling; any further CBC feature needs token relief first.
- **v9.32**: Key Level Alert (alert_on_pivot_cross) default OFF (alert + R1/S1 marker). Inputs only.
- **v9.33**: defaults: keep-N erase ON with 5 back; Key Level Alert back ON. Inputs only.
- **v9.34**: Target Structure Checklist position default Bottom center. Inputs only.
- **v9.35 / ESLib rev25**: 6 chop filters in Trade Setup Filters (all default OFF; shared lookback = renamed "Chop filters length (bars)" ats_f_chop_len): ADX below (ats_c_adx), Efficiency Ratio below (ats_c_er), EMA20/VWAP crosses >= (ats_c_x), HTF EMA20 slope below x ATR (ats_c_sl), N-bar range below x ATR (ats_c_rg), mixed LTF structure LH+HL / HH+LL (ats_c_st_on). Top-level `ats_chop2 = obLib.f_ats_chop2(...)` just above f_ats_trig, passed as new last param c2 to f_ats_filters (ats_flt now 12 values; alert Filters line appends ADX/ER/X/Slope/Range/Struct). Room made: 11 eff_show_* inlined into the status-table call, EMA cloud plot handles inlined into fill(), grp_trade_setup / grp_ats_flt / grp_ob2 replaced by literals. CBC now 23,669 tokens / 1,380 top-level.
- **v9.36 / ESLib rev25b / ESLib2 v1**: ESLib publish failed CE10117 **104,111** tokens (rev25 = tok2 27,448; rev23 26,576 published OK -> ESLib ceiling ≈ tok2 ~26.6k, ratio ~3.79). Lux-style OB cluster (f_ob2_detect, f_ob2_manage, f_ob2_side, f_ob2_clear, f_ob2_fmt_vol; ~1,950 tok2) moved verbatim to new library `pine/ESLib2.pine`; CBC `import samuelsuss8/ESLib2/1 as ob2Lib` + the two calls use ob2Lib. ESLib now tok2 25,503. Next ESLib relief candidates (self-contained): f_render_flip_brsg_fvg_piv_lines (~1,160), f_render_pivot_table (~1,890, shares f_status_pos).
- **v9.37**: imports ESLib/40 (rev25b, user confirmed) + ESLib2/1. No code change.
- **v9.38 / ESLib2 v2**: v9.37 failed CE10117 **100,407 / limit 100,256** (tok2 23,677 -> ratio 4.241; **CBC tok2 ceiling now ≈ 23,640**). Local f_ob2_detect_c moved to ESLib2 as export f_ob2_detect_t (tuple). CBC tok2 23,577 (~64 left). Note: unused functions cost nothing, so deleting dead code does not help.
- **v9.39**: all 31 input group headings prefixed "▌<circled n> " in Inputs-tab order (① Auto Trade Setup … ㉛ Historical Bar Panel); the 4 const grp_* strings too. New inputs must use the numbered group string. Tokens unchanged.
- **v9.40**: Efficiency Ratio chop filter default ON, 0.25. Inputs only.
- **v9.41**: Close at TP1 default 80%. Inputs only.
- **v9.42**: Trail SL1 x ATR default 1.7. Inputs only.
- **v9.43**: ATR SL1 x and TP1 x defaults 1.7. Inputs only.
- **web v116**: iPad fix -- #setupBox .sb-main no longer fixed 300px (width auto, min 300) + children flex-shrink 0 + box overflow-x auto; the levels table (wider than 300px with ATR pivot text) was being overlapped by the status table.
- **web v117**: iPad still overlapped (user re-sent the pre-v116 screenshot, so unverified) -> made WebKit-proof: #setupBox .sb-body = grid (max-content max-content), .sb-main .sb-table / .st-table width max-content. Do NOT set #setupBox width max-content (collapsed heads stretch it to ~1300px).
- **v9.44**: MTF EMA 9/20 cloud (show_mtf_ema_cloud default OFF, col_mtf_cloud_bull/bear with opacity in the colour) = one fill() of two display.none plots of the existing mtf_ema9/20 request (no new security call). CBC tok2 23,623 (~17 left of ≈23,640) -- next feature needs relief first.
- **v9.45 / ESLib2 v2**: v9.44 failed CE10117 **100,354** (tok2 23,625 -> ratio 4.248; ceiling ≈ 23,600 tok2). Moved f_field_render_order (self-contained) and f_clr (now export f_clr(req, r9, r20, htf_ema9, htf_ema20, ema9, ema20)) to ESLib2 v2 (still unpublished, placeholder /2; v2 also has f_ob2_detect_t). CBC tok2 23,418 (~180 left).
- **v9.46**: Include 'toward' HTF flips (ats_allow_toward) default OFF. Inputs only.
- **web v118**: Chart 3m view -- chDrawFlipBoxes draws a normal-size CBC flip triangle per 15m flip box (green ▲ below LONG box label, red ▼ above SHORT box label; hw 5, th 8).
- **v9.47**: VWAP Break alert (alert_on_vwap_break) default OFF. Inputs only.
- **v9.48**: "Block if VWAP from -pts/+pts" (ats_nv_on, still default OFF) gets exception input ats_nv_w (1.0): f_nz(l,a,b,w) not blocked when (long) low - VWAP >= w / (short) VWAP - high >= w. EMA200 call passes na (no exception).
- **v9.49**: no-new-setups window default 1600-1815. Inputs only.
- **v9.50**: import ESLib2/4 (current published ESLib2, user confirmed) + ESLib/40. No placeholders left.
- **v9.51**: no-new-setups window default 1600-1845. Inputs only.
- **v9.52**: keep-N erase default 15 back. Inputs only.
- **v9.53**: min SL per symbol -- ats_min_sl now input.string "MGC 6, MES 6, MNQ 6, M2K 6, MCL 6, BTC 6"; ats_msl = nz(obLib.f_sl_cap(ats_min_sl_on, ats_min_sl)) (unlisted symbol = 0 = no minimum). No lib change.
- **v9.54**: min SL per symbol default "MGC 5, MES 5, MNQ 25, M2K 3, MCL 0.3, BTC 300". Inputs only.
- **v9.55**: ats_tw_late (default OFF, only when ats_allow_toward OFF): in f_ats_hdir, bool lt = first confirmed close on the away side of htf_ema20 after a toward flip -> aw := true and returned fb/fs include lt (so the HTF CBC Flip trigger fires on that candle; also counted by the frequent-flips filter).
- **v9.56**: ats_orb_f (no setups while ny_or_active) + ats_orb_in (no setups while ny_done and ORLow_NY <= close <= ORHigh_NY), both default OFF, in the ats_new_setup gate. Consts grp_orb_retest / grp_bill_breaker inlined to literals to keep top-level at 1384.
- **v9.57**: ats_tw_pts (inline with ats_tw_late, default 0): late-away close must be >= htf_ema20 + pts (long) / <= htf_ema20 - pts (short).
- **v9.58**: ORB blocks per session: ats_orb_f / ats_orb_f_ln / ats_orb_f_as (ny/ln/as_or_active) and ats_orb_in / ats_orb_in_ln / ats_orb_in_as (ny/ln/as_done + close inside that OR), all default OFF. Room: col_ltf_flip_line, col_htf_flip_line, a_vwap_diff, a_ema200_diff inlined.
- **v9.59 / ESLib2 v3**: v9.58 failed CE10117 **100,261** (tok2 23,508 -> ratio 4.265; ceiling ≈ 23,505 tok2!). Moved f_htf_prev, f_htf_last4 (now 10 params) and f_ats_hm to ESLib2 v3 (+ private f_n copy). CBC tok2 23,327 (~180 left). Import ESLib2/5 placeholder until user confirms.
- **v9.60**: defaults ats_orb_f / _ln / _as ON (forming), keep-N 50. Inputs only.
- **v9.61**: ats_one_on (default ON) -- in the ats_new_setup gate, long cond gets `and not (ats_one_on and ats_state[6] == 1 and ats_llg)`, short mirrored; `var float[] ats_state` moved above the gate (next to ats_llg).
- **v9.62**: ats_tw_late default ON, ats_tw_pts 1. Inputs only.
- **v9.63**: ats_kn maxval 500. Inputs only.
- **v9.64**: chop length default 12, ER default 0.23. Inputs only.
- **v9.65 / ESLib rev26**: ats_sl_lbl (default ON) -> new last param bool sl_lbl on f_ats_draw_setup: on sl1_hit a label at active_stop "SL1 x" / "BE x" / "Trail x" (x = runner pts), green if > 0 else red, pushed into all_lb (erased with the setup).
- **v9.66 / ESLib rev26 (same unpublished rev)**: ats_ex_tiny (default ON) -> new last param bool ex_tiny on f_ats_draw_setup: TP1-partial + SL-exit labels become size.tiny label.style_diamond (green) / style_xcross (red, loss/BE) with empty text, full text in tooltip.
- **v9.67**: imports confirmed ESLib/42 (rev26) + ESLib2/5 (v3). No placeholders. No code change.
- **v9.68 / ESLib rev27**: ex_tiny markers = label.style_label_center, transparent bg, text "Ⓣ" (green, TP1 partial) / "Ⓢ" (green if runner > 0 else red), size.small; tooltip unchanged.
- **v9.69 / ESLib rev28**: Ⓣ/Ⓢ label y = beyond the candle on its own side (long TP: max(high,TP)+1.5*range; SL: min(low,stop)-1.5*range; short mirrored) + dotted line.new connector from exit price (pushed to all_l, erased with the setup). Checkbox OFF = text bubbles at price.
- **v9.70 / ESLib rev28 (same unpublished rev)**: ats_ex_tr (int, default 25, inline with ats_ex_tiny) -> new last param int ex_tr = text-label bg transparency. mtf_tf_disp_val inlined into the status-table call to keep top-level at 1385.
- **v9.71**: HTF CBC flip distance gate — ats_fd_mode (Off / pts or x ATR from 3m or 15m EMA20, default Off) + ats_fd_x (2.0), inline in ▌①. Local fd_ok in f_ats_trig ANDed into ats_t_flip_l/s (covers late-away + pullback-wait). Room: ats_chop2 and aplus_pivot_suffix inlined. 23,405 tok2, 1385 top-level. Imports ESLib /45 (rev28).
- **v9.72**: ats_fva_on (default OFF) + ats_fva_x (1.0 pts), inline in ▌① under the EMA20 distance gate: flip long needs close > max(VWAP, EMA200) + X, short close < min(VWAP, EMA200) - X; ANDed into ats_t_flip_l/s. Room: htf_diverge_note and ob2_tf_res inlined. 23,433 tok2, 1385 top-level.
- **v9.73**: ats_h20s_on (default OFF) in ▌①: local h20d = htf_ema20 - htf_ema20[HTF/chart bars] in f_ats_trig; long blocked if h20d < 0, short if > 0 (ANDed into ats_trigger_long / ats_short_cond = all triggers). Room: ats_flip_box_txt inlined. 23,472 tok2, 1385 top-level. NOTE: v9.73 hit CE10117 at 100,458 real (ratio ~4.28 at 23,472 tok2).
- **v9.74**: token fix, no behavior change: removed unused cf_f12_ltf_structure, ats_sl3, htf_fvg_filled block, legacy input confluence_use_ltf_structure_break; plotORNYH unassigned; vwap_bounce_dist -> one variadic math.min; a_time_s via str.format_time (a_hh/a_mi/a_hh_close/a_mi_close removed). 23,268 tok2 (~99.6k real), 1375 top-level.
- **v9.75**: ats_h20s_on is now input.string Off / HTF EMA9 / HTF EMA20 (default Off); local hx picks htf_ema9 or htf_ema20, h20d = hx - hx[HTF/chart bars].
- **v9.76**: slope gate options Off / HTF EMA9 / HTF EMA20 / Both EMA9 + EMA20 + ats_hsl_min (pts per HTF candle, default 0, inline). Locals hk, d9, d20, b9, b20 in f_ats_trig; long blocked if chosen slope (Both = min) < min, short if (Both = max) > -min. NOTE: v9.76 hit CE10117 at 100,308 real with 23,328 tok2 (ratio now ~4.30; keep tok2 <= ~23,250).
- **v9.77**: token fix, no behavior change: a_head / a_mid shared by a_status_msg and the A+ alert body; a_st2 shared structure lines (a_structure_line + a_marker_snapshot); size=htf_label_size (string = size.*); ln_or_open = ny_or_open - 23400000. 23,129 tok2 (~99.5k), 1379 top-level.
- **v9.78**: default ats_fd_mode = "x ATR from 3m EMA20" (ats_fd_x 2.0).
- **v9.79**: max_labels_count 500; mk_n input (default 200, 0 = all) in ▌①; global var label[] mk_q + f_mk(label) after ny_tz; 10 marker label.new calls wrapped (LTF flip/reversal triangles, ORB X, HTF flip dot, HTF LONG/SHORT, alert dot + letter). Not wrapped: HTF trail SL label, setup ⓘ / exit labels (ESLib).
- **v9.80**: mk_l_on / mk_c_on (default OFF, inline in ▌⑤ under show_chart_markers): marker_ltfpierce gated by mk_l_on; C letter + draw condition gated by mk_c_on. Alerts and triggers untouched.
- **v9.81**: ats_er_bg (default ON, ▌③ under ER filter): bgcolor gray 85 where array.get(ats_flt, 7) (ER from f_ats_chop2 via f_ats_filters concat: [ok_l, ok_s, chop, ext, flips, blk, adx, er, xs, slp, rg, mix]) < ats_c_er. Room: a_chart_line, a_mtf_cloud_part inlined.
- **v9.82**: a_htf_flip_ema_dist (HTF CBC Flip dot tooltip, confirmed + anticipatory) gets a line "3m EMA20 x pts / y ATR | HTF slope EMA9 a EMA20 b | ER c". hk/d9/d20 now globals before f_ats_trig; int ext_t (after extend_levels_bars input) replaces 4 copies; a_time_s / a_prev_candle_line / a_stop_line inlined. 23,243 tok2 (~99.9k at 4.30), 1385 top-level. Token headroom now ~300 real: next feature likely needs a library move.
- **v9.83**: global string a_ex (3m EMA20 dist = close - ema20 pts / ATR, HTF slope d9/d20, ER) appended to the flip-dot tooltip AND to the ⓘ why text in f_ats_setup_alert (after the Candle line). a_flip_level_line inlined.
- **v9.84 / ESLib rev29**: f_ats_xm helper (non-exported) in ESLib; f_ats_draw_setup draws an exit marker (gated by sl_lbl) on every end: HTF flip / 17:00 (dir_flipped_against_active; both dirs true = EOD), replaced (kept branch on new_setup, id sid-1), TP2 / SL2 breach without sl1_hit. No signature change. ESLib 26,309 tok2. CBC: import /46 placeholder + ats_sl_lbl title/tooltip only.
- **v9.85 / ESLib rev29 (same unpublished rev)**: ex_tiny markers = filled bubble (transp 0) + white text T1/T2/S/F/E/R, size.normal; connectors dashed width 2 full colour. CBC: mk_h_on (default OFF) gates marker_ltf20 (H letter only). Now imports /48. Later same rev29: marker offset xo = nz(min(1.5 x candle range, ta.atr(14)), range), computed at the top of f_ats_draw_setup every call; f_ats_xm takes xo.
- **v9.86**: ORB High/Low Cross X tooltip + "\nFired: MM/dd HH:mm ET" (time_close).

- **web v119**: Stats detail (click a trigger row / Total) gets an ATR grid: setups replayed from BarFeed 3m bars, SL 1/1.5/1.7/2/2.5/3 x ATR(14) x TP 1/1.5/1.7/2/2.5/3/4 x ATR, full exit at first hit (both in one candle = SL), else opposite 15m flip / 17:00; total pts per cell (hover: win %, PF, best / worst trade, max DD), best cell outlined, 1.7/1.7 shaded; MFE / MAE medians in pts + ATR; "apply min SL per symbol" checkbox (MIN_SL map = CBC defaults). Needs a single symbol selected.
