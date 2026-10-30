# CBC Session Handoff

Written 09/15/2026, updated 09/18/2026 (v7.15), updated 09/19-21/2026 (v7.16 through v7.32 — see the sections at the very bottom), updated 09/23/2026 (v7.33 through v7.60 — see the sections at the very bottom), updated 09/24-26/2026 (v7.61-v7.92). Read this first before touching the .pine files — it's the fastest way to pick up the standing conventions without re-reading the whole file history.

## Housekeeping note (09/16/2026)
This project hit its 2M-token knowledge cap because every version bump was saving a full duplicate copy of the ~680KB main script. Cleared out all superseded pine snapshots — **only the current authoritative main script stays saved in the project going forward.** Nothing is lost: each file's own internal changelog (the comment block before `//@version=6`) already preserves the full version history. **Going forward: do NOT keep old version-numbered .pine docs around in the project once a new version supersedes them — delete the prior version's doc in the same turn you write the new one**, or this will fill up again.

## IMPORTANT — this doc was accidentally overwritten once (09/23/2026)
A `project_write` call meant to ADD a short v7.57 addendum instead REPLACED the entire doc, briefly wiping everything below. It was reconstructed from conversation context immediately after and should be complete again as of this write — but if anything below looks thin or missing compared to what you'd expect, flag it to the user rather than assuming it's accurate. **Standing lesson: `project_write` always replaces the WHOLE doc — there is no in-place append. Always `project_read` the current full doc first, edit that full content, and write the full result back — never draft a short standalone update and write() it directly.**

## Library-version reconciliation — RECONCILED at v7.82 (`/57`), after the longest gap yet
This doc and the .pine files' own changelogs have been labeling the library "v44", "v45", ... most recently "v66" (as of the v7.90 round) as a SESSION-LOCAL bookkeeping counter, assuming it moves in exact lockstep with the version number TradingView itself assigns each time the library is actually published. That assumption has been wrong every time it's been checked: `/48` (v7.62), `/49` (v7.66), `/51` (v7.73), `/52` (v7.75), and now **`/57`** (v7.82, per the user's direct report mid-turn: "librabry pulished version is 57"). **CONFIRMED (v7.89): the library WAS republished with v7.86's fix live** (the user's own screenshot showed the cyan "◆ TP1 HANDLE" label rendering correctly, which only happens with the v64+ sanity-gated code) — but the import line still hasn't been updated to whatever the new real number is, because the user hasn't reported it yet. **The import line is still `/57` through v7.92 — v7.84, v7.85, v7.86, v7.89, v7.90, AND v7.92 all added/changed library content since that number was last confirmed (v7.91 did NOT touch the library — pure main-script input reordering), so the import line stays put until the user reports a new real number covering all six library-affecting rounds at once.** Session-local library counter is now **v67** (was v66 at v7.90). **Standing lesson going forward: this session's own internal library-revision counter tracks content changes, NOT TradingView's real published number — always use the number the USER reports back after an actual publish, never assume it equals the internal counter.** See convention #38 and the dedicated version-history sections below.

## CE10295 "main body too long" — RESOLVED, now with STRONG DIRECT confirmation as of the v7.89 round
Previously this was inferred only from indirect screenshot evidence (Settings panel showing the right UI). **This round adds a much stronger signal: the user's own screenshot showed the cyan "◆ TP1 HANDLE" label actually rendering on their live chart** — that specific behavior only exists in the POST-v7.86 library code (the pre-fix version would have rendered a plain, uncolored, undifferentiated line only, or in the old buggy case, distorted the chart). This confirms the library the user is running is not just "some recent version" but specifically has v7.86's changes live, meaning CE10295 is cleared, v7.84+v7.85+v7.86 are all compiled and running. Still worth getting the explicit "it compiles" words and the real published library number per convention #47.

## CE10173 "cannot assign 'simple na' to a 'const bool' variable" — FIXED (v7.90)
The v7.89 round's new `var bool active_long = na` declaration (inside `f_ats_draw_setup()`) does not compile — Pine requires an explicit type cast when initializing a `var` of an explicit type directly to a bare `na` literal; `var float`/`var int`/`var label`/etc. auto-convert `na` fine, but `var bool` (and similarly `var color`/`var string` in general) does not. **Fix: `var bool active_long = bool(na)`.** This was caught by the user's own VS Code Pine linter (screenshot showing the exact CE10173 error on that line) before any TradingView compile attempt — a new, earlier-catching signal worth remembering. No other code changed this round. Library bumped to session-local **v66**, main script to **v7.90**. **New standing lesson (convention #66) — see below.**

## Auto Trade Setup's whole input group moved to the very top of Settings (v7.91)
Per direct request ("move auto trade setup inputs to the top - put auto setup where the blue arrow points", with a screenshot showing the arrow pointing at the "LTF Signals" group header — the first group in the whole Settings panel at the time). The ENTIRE `grp_trade_setup = "Auto Trade Setup"` group (all 17 inputs: the 4 drag handles, the enable toggle, both triggers, both zone colors, the Stop/Target/SL2/TP2 level pickers, and Show TP2/Show SL2) was cut from its old spot deep in the file (right before the candidate-pool builder, around the old line ~3607) and moved to just above the "LTF Signals" group's first input — now the literal first input group shown when Settings opens, ahead of everything else in the script. **Pine's Settings panel orders groups by the source-code position of each group's FIRST `input.*()` call, not by where the group variable/string is defined or by any manual priority setting** — this is the mechanism convention #64 already leaned on for in-group ordering, now confirmed to also govern *between*-group ordering. Pure declaration-order move, zero behavior change: none of the moved inputs reads another input's value at declaration time, and the drawing/trigger logic that consumes them (still sitting in its original spot in the file) resolves each variable by name, not by proximity — Pine doesn't care where in the file an input is declared relative to where it's used, only that it's declared somewhere at the top level. No library change needed. Balance check re-run clean (paren/bracket balance unchanged at the established (7,0) baseline). **New standing lesson (convention #67) — see below.**

## "Auto-fill the drag handles when the setup draws" — asked again, still NOT possible (09/26/2026, no version bump)
The user re-asked essentially the v7.89 request in different words: "modify so the tp1 drag ,, sl2 drag values are auto filled in when this box initially draws and the draggable element would be there." Investigated again to be sure nothing changed: **still impossible.** Two independent Pine limitations both block it: (1) no script can write into ANY `input.*()` value at runtime — confirmed at v7.89, still true, this is the same "one-directional input" wall; and (2) even a script-computed *default* is out — `input.price(defval, ...)`'s `defval` must be a compile-time constant literal, it cannot be a variable or a bar-derived value, so there's no way to make the handle "start" at a live target/stop price either. No code change made this round.
- **Practical mitigation, not a fix**: traced through `f_ats_compute_trigger()` (the trigger-time code path) to check whether the user actually needs to retype a handle for every new setup. They don't, in practice — `f_ats_handle_sane(handle, current)` there checks the handle against `current = ` the FRESH auto-computed target/stop of the *new* setup (not a fixed reference), using a very wide 0.2x–5x multiplicative band. For an instrument trading anywhere near where the handle was last set, that band spans roughly a fifth to five times the price — enormous in absolute terms — so a handle typed in ONCE for a given instrument stays "sane" (and keeps snapping/live-following) across essentially all future setups on that instrument, without needing to be retyped each time. The friction the user is hitting is a ONE-TIME setup cost per handle per instrument, not a per-trade one. Told the user this directly rather than attempting a workaround that can't exist.
- **Standing lesson (convention #68)** — see below.

## Drag handles now accept a STEP COUNT (+1/-1/etc.) as an alternative to a price (v7.92)
Direct follow-up after the "why can't it just use the pivots it already has" exchange: the user asked "why can't the script capture the drawing object for tp1 and tp2 and s1 and s2 and use these - it has the pivots" (answered: it already does, in Automatic/handle=0 mode — the handles exist only to OVERRIDE that automatic pick), then made the genuinely new, implementable ask: **"can we have the script be able to take in +1 or -1 to move target away from target(+), etc."**
- **Two design forks resolved via `AskUserQuestion` before implementing** (per convention #7):
  1. **"What should +1/-1 be measured from?"** → user picked **"From today's automatic pick."** So +N chains forward N pivots beyond whatever Automatic already selected for that level, not from entry.
  2. **"Should typing a real price still work, or does this replace that entirely?"** → user picked **"Both, auto-detected (Recommended)."** So absolute-price mode (pre-existing) and step-count mode coexist in the same 4 handle inputs, auto-detected by value shape.
- **New library exports (session-local v67)**:
  - `f_ats_handle_is_step(float handle) => handle != 0.0 and handle == math.round(handle) and math.abs(handle) <= 20` — any nonzero whole number with magnitude ≤ 20 is read as a step count, not a price. (An absolute price this small would fail the existing `f_ats_handle_sane` 0.2x–5x band anyway on any realistically-priced instrument, so the two modes don't collide in practice.)
  - `f_ats_handle_step(float base_ref, float current, float[] cand, bool want_above, int n)` — chains `f_ats_nearest_above`/`f_ats_nearest_below` forward `n` times from `current` (the level's own live automatic pick). `+n` walks further out (away from entry); `-n` walks back toward `base_ref` (the level's own anchor — entry for TP1/SL1, TP1's resolved price for TP2, SL1's resolved price for SL2), refusing to cross that anchor.
  - `f_ats_handle_snap()` signature grew **5→6 params**, gaining `base_ref`: now checks `f_ats_handle_is_step()` first and routes to `f_ats_handle_step()` when true, otherwise falls through to the original absolute-price snap logic unchanged.
  - All 8 real call sites (4 in `f_ats_draw_setup()`'s live-follow branch, 4 in `f_ats_compute_trigger()`) updated to pass `base_ref`: `entry`/`active_entry` for TP1/SL1, `target`/`active_target` (TP1's own resolved value) for TP2, `stop`/`active_stop` (SL1's own resolved value) for SL2.
  - No change needed in `f_ats_draw_handles()` (the on-chart identifier-label drawer) — its existing `f_ats_handle_sane()` gate already naturally excludes small step-mode integers from getting a label (correct/safe: avoids reproducing the v7.86 autoscale-crush bug by trying to plot a coordinate at price=1 or price=-3).
- Updated all 4 handle tooltips to document the new step-count behavior (TP1/SL1 phrased relative to "entry"; TP2/SL2 phrased relative to "TP1"/"SL1").
- **Verification**: balance check clean at the established (7,0)/(3,0) baseline; paren-depth-aware argument matcher confirmed `f_ats_handle_snap()`'s 6 declared params match all 8 call sites' 6 args, in order (one old changelog-comment "5 args" abbreviated example correctly ignored per convention #27).
- **REQUIRES the library republished again** — import line stays at `/57`, now needs to cover six library-affecting rounds (v7.84, v7.85, v7.86, v7.89, v7.90, v7.92) in one go.
- **New standing lesson (convention #69)** — see below.

## Current state
- **v7.92 is the current delivered round — the 4 Auto Trade Setup drag handles (TP1/SL1/TP2/SL2) now accept a small whole-number STEP COUNT (±1 to ±20) as an alternative to an absolute price**, auto-detected, coexisting with the pre-existing absolute-price mode. See the dedicated section above. **REQUIRES the library republished** — import line stays at `/57`.
- **v7.91 — the entire "Auto Trade Setup" input group relocated to the very top of the Settings panel**, ahead of "LTF Signals" (previously first). See the dedicated section above. No library change — import line stays at `/57`.
- **v7.90 — a single-line compile fix (CE10173) for a bug the v7.89 round introduced**, caught via the user's own VS Code Pine linter rather than a TradingView compile attempt or a runtime report. See the dedicated CE10173 section above. **REQUIRES the library republished** (one changed variable initializer inside `f_ats_draw_setup()`) — import line stays at `/57`.
- **v7.89 — two related feature additions**, both per direct follow-up once the user could finally see the handle label render:
  1. **"i moved it but it did not snap"**: until then, a drag handle only ever fed into the math for the NEXT new trigger (`f_ats_compute_trigger()`) — it had zero effect on a setup already drawn on the chart. Per direct confirmation ("Live-update the active setup"), `f_ats_draw_setup()` now re-applies `f_ats_handle_snap()` every bar (not just at `new_setup`) against whichever handle is active, and moves that level's line/label and reshapes the matching reward/risk zone box live when the result differs from what's currently drawn. This also satisfies the separate ask ("I would like the darker green to shade as the tp is moved") — the reward zone box's top/bottom now literally are the live target, so it visually stretches/shrinks as TP1 moves.
  2. **"can we feed the values into the inputs for tp1 tp2 sl1 and sl2"**: confirmed NOT possible — Pine Script has no API for a script to write a value back into its own `input.price()` field, inputs are strictly one-directional (user → script). Closest workable substitute: every TP1/SL1/TP2/SL2 on-chart label AND each handle's own identifier label now show their live numeric price directly in the label text (e.g. "TP1 7810.25", "◆ TP1 HANDLE 7810.25"), so the exact value is readable straight off the chart to type into a handle field. **Re-confirmed impossible again 09/26/2026 when asked a second way — see the dedicated section above.**
  - `f_ats_draw_setup()`'s signature grew 11→17 params (added `tp1_handle`/`sl1_handle`/`tp2_handle`/`sl2_handle`, a shared `tol`, and the candidate pool `cand`). `f_ats_draw_handles()`'s signature is unchanged (label text only). Library bumped to session-local v65 (superseded by v66 at v7.90).
  - New local in the main script: `ats_tol = obLib.f_aplus_pivot_dist(0.0)`, reused so both the trigger's own handle-snap logic and the live-follow logic use the identical tolerance rather than two independently-computed values that could drift.
  - Verification: balance check clean on both files; paren-depth-aware argument matcher confirmed 17 signature params == 17 call-site args, in matching order. **This round's own new `var bool active_long = na` line was itself a compile error (CE10173), caught by the user's linter — see v7.90 above.**
  - **NOT yet confirmed live-in-practice by the user** — pending v7.90's fix, watch the user's next report closely: does dragging TP1/SL1 now visibly move the box/line/label of the CURRENT setup, does TP2/SL2 do the same, and do the labels show the right live numbers.
- **v7.88 — a SECOND reordering pass on the same 4 drag handles**, moving them to the literal first 4 items in the "Auto Trade Setup" group (ahead of the enable toggle), per the user's own follow-up screenshot on v7.87.
- **v7.87 — pure input reordering**, moved the 4 handles from the bottom of the group to right after the enable toggle. Superseded in ordering by v7.88.
- **v7.86 — a real bug fix, per a direct 3-part report on v7.85.** "Where is TP2" investigated and confirmed NOT a bug (expected when no candidate exists beyond TP1). The drag-handle report WAS real: no handle had any upper/lower sanity bound, so a stray value like `1` corrupted both the snap math and the chart's own autoscale. Fix: new shared library export `f_ats_handle_sane(handle, current)`, wired into both `f_ats_handle_snap()` and `f_ats_draw_handles()`. **CONFIRMED WORKING** — see the CE10295 section above.
- **v7.85 — proactive CE10295 headroom.** Moved the `if barstate.islast` CBC Flip/BRSG/FVG/pivot-line block into `obLib.f_render_flip_brsg_fvg_piv_lines(...)`. **See the "Next CE10295 headroom candidates" section below.**
- **v7.84 — the real CE10295 fix.** The Auto Trade Setup trigger `if` block is now `obLib.f_ats_compute_trigger(...)`.
- **v7.83 — comment-only trim.** CONFIRMED INSUFFICIENT by itself.
- **v7.82 — a SECOND CE10295 fix (statement-count only), plus the import line reconciled to `/57`.** Did NOT clear the error alone.
- **v7.81 — the 4 Auto Trade Setup drag handles now each get a small, uniquely-colored on-chart identifier label whenever active.** New library export `f_ats_draw_handles()`, given a sanity gate at v7.86, live-numeric-price text at v7.89, its inputs reordered twice within-group (v7.87, v7.88), then the whole group relocated between-group (v7.91).
- **v7.80 — the setup box/lines now stop extending right once price touches/crosses TP2 or SL2.**
- **v7.79 — "TP1"/"SL1"/"TP2"/"SL2" tags drawn directly on those lines.**
- **v7.78 — removed `confirm=true` from the 4 v7.76 drag handles.**
- **v7.77 — fixes CE10295 (round 1).** New library export `f_ats_handle_snap()`.
- **v7.76 — Auto Trade Setup TP1/SL1/TP2/SL2 each get a draggable "drag-to-snap" handle, plus Show TP2/Show SL2 are now independent toggles.**
- **v7.75 — import-version reconciliation, `/51` → `/52`.**
- **v7.74 — Auto Trade Setup can optionally draw a SECOND TP/SL level (TP2/SL2).**
- **v7.73 — import-version reconciliation, `/49` → `/51`.**
- **v7.72 — chart-level labels landing at the same/near price now merge into ONE combined label.**
- **v7.71 — Pivot Points table Price row shows a compact OPEN-CLOSE time RANGE.**
- **v7.70 — Pivot Points table Price row shows direction + the confirming HTF candle's own OPEN time.**
- **v7.69 — marker tooltips show a "Confirmed Long turning Short HTF" divergence note.**
- **v7.68 — pure cosmetic: `indicator()` title dropped the `-wCBC ` suffix.**
- **v7.67 — Auto Trade Setup's automatic candidate pool now includes NY/London/Asia session Opening Range High/Low.**
- **v7.66 — import-version reconciliation, `/48` → `/49`.**
- **v7.65 — Auto Trade Setup cooldown 5→3 LTF bars, mid-candle draws restored.**
- **v7.64 — CE10237 fix (unused argument 'ltf_bull').**
- **v7.63 — Pivot Points table PRICE row now follows confirmed HTF CBC direction instead of the LTF/chart timeframe's own.**
- **v7.62 — import-version reconciliation, `/50`(internal) → `/48`(real).**
- **v7.61 — Auto Trade Setup box only drew once the triggering bar had closed.** **Explicitly REVERSED at v7.65.**
- **v7.60 — RE10039 runtime fix in the Pivot Points table renderer.**
- **v7.59 — Order Blocks turned OFF by default.**
- **v7.58/v7.57 — two separate CE10237 fixes (unused arguments 'is_long'/'txt_size').**
- **v7.56 — Auto Trade Setup visual restyle + 5-LTF-bar rate limit (since shortened to 3 at v7.65).**
- **v7.55 — pure republish-force bump, no logic change from v7.54.**
- **v7.54 — the final, corrected version of the Auto Trade Setup LTF pierce gate.**
- **v7.51 — manual Stop/Target level picker for Auto Trade Setup.**
- **CE10117 "too many tokens" appears RESOLVED as of v7.49.**
- Main script: **`pine/CBC_v7_15_with_OrderBlocks.pine`** — this is the authoritative version in the project as of this writing (project doc, not the same as the session's latest delivered file). Always `project_read` it (not an old cached copy) before editing.
- **NOT yet promoted to the project as the authoritative doc: v7.16 through v7.92** — all exist only as delivered files (`/mnt/user-data/outputs/`), not project docs, because none has been confirmed compile-clean by the user via an explicit "it compiles" statement yet.
- Library: **`pine/CBC_OrderBlocksLib.pine`** — the STALE project doc copy still reads an old import number. **The main script's import line still reads `/57`** — **v7.84, v7.85, v7.86, v7.89, v7.90, AND v7.92 all need the library republished before that number moves again; v7.87, v7.88, and v7.91 added no library content.**
- **v7.09-v7.14 were each reported over budget (CE10117) or made things worse, and superseded within the same session** — not safe to hand out or reference as "current."
- **v7.15 has NOT yet been confirmed clean by the user.**

## Next CE10295 headroom candidates — located and measured, ready to move whenever this comes up again
v7.85 fixed the single largest remaining top-level block. A full structural scan of the main script (line offsets as of **v7.85**) found these as the next largest top-level blocks, ranked by ACTUAL code-line count (comments/blanks excluded). **Re-run the line-offset measurement before acting on these** — several small rounds since v7.85 (v7.86 through v7.92) have shifted offsets somewhat, and v7.91 in particular moved a ~26-line block from deep in the file to near the top, shifting everything else's line numbers.
1. **`if not na(YDH)` (~91 code lines), tightly paired with `if new_day` (~41 code lines).** Draws/resets the YDH/YDL/PMH/PML/session H-L reference lines and fills. Move together as one function.
2. **`if show_lvl_lbl` (~71 code lines).** The chart-level label overlap-merge pass from v7.72. Takes labels as a `label[]` parameter rather than owning `var` state.

**Suggested order if/when this is picked up again**: combine #1 + its `if new_day` pair first, then #2 if more headroom is still needed. Same verification suite as every prior round.

## RE10140 "too many plots" — RESOLVED (v6.96)
## "The size of the script compilation request is too large" — a THIRD, distinct limit (first hit at v7.44, RESOLVED)
## CE10117 "too many tokens" — the v7.44 Auto Trade Setup chain, likely RESOLVED as of v7.49
## RE10056 "Invalid value of the 'size' argument" — RESOLVED (v7.50)
## Manual Stop/Target level picker for Auto Trade Setup — DELIVERED, unconfirmed (v7.51)
## Auto Trade Setup LTF Pierce gate — the full 3-round story, landed correctly at v7.54
- **Net result, still true as of v7.92**: trigger = `fire_ltf_ema20_pierce_long`/`short` (HTF CBC direction + flip-away-from-ema20) **PLUS** price closed on the favorable side of the LTF's own `ema20` on the pierce bar.

## CE10017 "missing enclosing character" — republish-force bump (v7.55)
## f_fire_alerts() cannot be moved to the library — Pine libraries cannot call `alert()`
## Auto Trade Setup visual restyle + 5-bar rate limit (v7.56)
## CE10237 "unused argument 'txt_size'"/"'is_long'" — FIXED (v7.57/v7.58)
## Order Blocks default OFF (v7.59)
## RE10039 "Column N is out of table bounds" — FIXED (v7.60)
## Auto Trade Setup: draw at bar close only (v7.61) — REVERSED at v7.65
## Import version reconciliation round 1 (v7.62)
## Pivot Points table PRICE direction follows confirmed HTF CBC (v7.63)
## CE10237 "unused argument 'ltf_bull'" — FIXED (v7.64)
## Auto Trade Setup timing changes: cooldown 5→3, bar-close gate removed (v7.65)
## Import version reconciliation round 2, /48 → /49 (v7.66)
## Auto Trade Setup: OR High/Low added to candidate pool (v7.67)
## Indicator title format change (v7.68)
## Marker tooltips: HTF divergence note (v7.69)
## Pivot Points table Price row: direction + confirming-candle time (v7.70)
## Pivot Points table Price row: open-close time range (v7.71)
## Chart-level label overlap handling: merge into one combined label (v7.72)
## Import version reconciliation round 3, CE10271 (v7.73)
## Auto Trade Setup: optional second TP2/SL2 level (v7.74)
- Automatic-mode TP2/SL2 = nearest-above/below fed TP1/SL1 (not entry) as reference. No fallback if nothing qualifies.

## Import version reconciliation round 4, /51 → /52 (v7.75)
## Auto Trade Setup: draggable drag-to-snap handles + independent Show TP2/SL2 (v7.76)
- 4 new inputs — `ats_tp1_handle`/`ats_sl1_handle`/`ats_tp2_handle`/`ats_sl2_handle`. **These are what v7.86 gave a sanity-range check to, v7.87/v7.88 moved (twice) within-group, v7.89 finally made live-update the currently-drawn setup, v7.90 fixed a compile error in, v7.91 relocated (along with the rest of the group) to the very top of the whole Settings panel, and v7.92 gave a coexisting step-count input mode.**

## CE10295 "The main body of the script is too long" — a FOURTH distinct limit, first hit at v7.76 (fixed v7.77), hit AGAIN at v7.81
- Round 1 (v7.77): `f_ats_handle_snap()`. Round 2 (v7.82, not sufficient). Round 3 (v7.83, comment trim, insufficient). Round 4 (v7.84, real fix). Round 5/headroom (v7.85). **Now with strong direct confirmation as of v7.89 — see the dedicated section above.**

## Draggable input.price() handles: confirm=true blocks the chart (v7.78)
## Auto Trade Setup: line labels tied to draw event (v7.79)
## Auto Trade Setup: freeze extension once TP2/SL2 breached (v7.80)
## Auto Trade Setup drag handles: on-chart identifier labels (v7.81)
## CE10295 round 2 (v7.82) — NOT confirmed sufficient
## CE10295 round 3, comment trim (v7.83) — CONFIRMED INSUFFICIENT
## CE10295 round 4, the real fix (v7.84)
## CE10295 headroom round (v7.85)
- **New standing lesson (convention #60)**: measure actual top-level code-line counts per top-level `if` block across the WHOLE file.
- **New standing lesson (convention #61)**: grep every relocated `var` name file-wide first.
- **New standing lesson (convention #62)**: record leftover oversized-block candidates with exact line ranges.

## Auto Trade Setup drag handles: out-of-range value broke both the snap logic AND the chart's own autoscale — FIXED (v7.86)
- **Fix**: new shared library export `f_ats_handle_sane(float handle, float current) => not na(current) and current > 0 and handle > current * 0.2 and handle < current * 5.0`, wired into both `f_ats_handle_snap()` and `f_ats_draw_handles()`. **CONFIRMED WORKING as of the v7.89 round** — the user's screenshot showed the cyan handle label rendering correctly once the handle value (7806) was within the sane band.

## Auto Trade Setup drag handles moved to top of the input group — TWO rounds (v7.87, v7.88)
- **New standing lesson (convention #64)**: when a user reports difficulty finding/selecting a specific `input.*()` field, consider whether it's simply buried deep in a long group before assuming a code/UI bug. **"Near the top" and "the literal first item" are distinct asks** — get the exact position intended, or expect a follow-up round.

## Auto Trade Setup drag handles now live-update the ALREADY-drawn setup, and labels show live prices (v7.89)
- Context: once v7.86's fix let the cyan handle label finally render, the user set TP1's handle to the current price (7806, later moved to 7810) and reported *"i moved it but it did not snap"* — plus a separate ask, *"can we feed the values into the inputs for tp1 tp2 sl1 and sl2."*
- **Root cause of "did not snap"**: not a bug — a deliberate original design limitation nobody had hit before. Every handle's `f_ats_handle_snap()` call only ever ran inside `f_ats_compute_trigger()`, which itself only runs when a NEW setup fires. Dragging a handle had always been documented/intended as "changes where the NEXT trigger places its TP/SL," never as "moves the setup already on screen." Confirmed via `AskUserQuestion` that the user wants the live-update behavior instead.
- **Fix**: `f_ats_draw_setup()` gained 6 new parameters (`tp1_handle`/`sl1_handle`/`tp2_handle`/`sl2_handle`/`tol`/`cand`, signature 11→17) and, in its per-bar (non-`new_setup`) branch, now calls `f_ats_handle_snap()` for each active level against that level's OWN currently-active price (not entry) — `f_ats_handle_snap()` already returns its `current` argument unchanged whenever a handle is inactive/insane, so this is a natural no-op until a handle is both active and meaningfully different. When a level DOES move, its line/label reposition and the matching zone box's top/bottom are reset to match (satisfying the separate "darker green should shade as TP moves" ask automatically, since the box's own boundary now literally IS the live level). New persistent state: `active_target`/`active_stop`/`active_long`/`active_bar` (previously only `active_entry`/`active_target2`/`active_stop2` existed).
- **"Feed the values into the inputs" — confirmed NOT possible.** Pine has no script-to-input write path. Substitute: every TP1/SL1/TP2/SL2 label and every handle identifier label now include the live numeric price in their text (`str.tostring(price, "#.##")`), updated every bar via `label.set_text()`. **Re-asked in different words on 09/26/2026 ("auto filled in when this box initially draws") — re-confirmed still impossible, see the dedicated section above and convention #68.**
- Library bumped to session-local **v65** (superseded by v66 at v7.90). New main-script local `ats_tol = obLib.f_aplus_pivot_dist(0.0)`, shared so the trigger's own snap math and the live-follow logic use one identical tolerance value.
- **REQUIRES the library republished again** — import line stays at `/57`.
- **This round's own new code had a compile error** (`var bool active_long = na`, CE10173) — caught by the user's VS Code Pine linter and fixed at v7.90. See the dedicated section above and convention #66.
- **New standing lesson (convention #65)**: a "drag handle" that only affects the NEXT event (not anything already on screen) is a legitimate, common design choice — but when a user reports a handle "didn't do anything" after they'd already have expected it to move something visible, check whether that's the actual documented scope of the feature before assuming a bug, and ask (via `AskUserQuestion` if available) whether they want the scope widened to affect the live/current instance too, since that's a real behavior change, not a bug fix, and deserves an explicit choice. Once confirmed, the reusable technique is: have the "does this move" function re-run its own snap/compute logic every bar against its OWN currently-active value (not the original trigger-time inputs) — the snap helper's existing "return unchanged if inactive" behavior then makes this a free no-op except when something has actually changed.
- **NOT yet confirmed by the user** (pending v7.90's compile fix).

## CE10173 "cannot assign 'simple na' to a 'const bool' variable" — FIXED (v7.90)
- Introduced by v7.89's new `var bool active_long = na` declaration. Pine requires an explicit cast when a `var` with an explicit non-numeric/non-drawing type (bool, color, string) is initialized directly to a bare `na` literal — `var float`/`var int`/`var line`/`var label`/`var box` all accept bare `na` fine, but `var bool` does not.
- **Fix**: `var bool active_long = bool(na)`.
- **Caught via the user's own VS Code Pine linter** (a red-squiggle screenshot showing the exact CE10173 message on that line), BEFORE any TradingView compile attempt — a new, even-earlier-catching signal than the usual "user reports it after publishing." Worth remembering as a source of fast, precise compile-error reports going forward.
- **New standing lesson (convention #66)**: `var <explicit-type> x = na` is only safe for types Pine implicitly converts `na` into (float, int, and the drawing-object types line/label/box/table/array/etc.). For `bool`, `color`, and `string`, cast explicitly: `bool(na)`, `color(na)`, `string(na)`. When introducing a NEW `var bool`/`var color`/`var string` initialized to "nothing yet," always write the explicit cast form from the start rather than the bare `na` (which works for other types and is easy to copy by habit).

## Standing conventions (apply to every future change)
1. **Every code change requires**: a version bump in both the filename and the `indicator()` title string, plus a changelog comment block immediately before `//@version=6`. Keep this changelog terse — full narrative lives in this handoff doc.
2. **No real Pine compiler is available.** Verification is: (a) a Python comment-stripped paren/bracket balance check; (b) a top-level duplicate-declaration grep; (c) a programmatic argument-count matcher when a library export's parameter list changes. **This suite cannot catch a runtime type/value mismatch, a runtime bound that grows over time, an unused parameter, a main-body-size limit, a var-type/na-cast mismatch (CE10173 — v7.90 precedent), or a runtime LOGIC bug that only shows up as a visual/behavioral symptom** — those require either the user's own report (or their own linter, per v7.90), or careful direct code-reading.
3. **CE10117 "too many tokens" fixes**: (a) move pure-parameter, no-CBC-state helpers to the library, (b) collapse near-identical repeated statements, (c) inline single-use named variables.
4. **RE10140 "too many plots" fixes**: convert plot()-family calls that do NOT feed a fill() call into manually-managed `line.new()` objects.
5. **Declaration-order gotcha for `htf_cbc_labels_f`**: declared relatively late — no forward reference.
6. **Shared-bar marker priority chain**: aplus > vwap > zone > confluence > pierce > pivot.
7. **Ask before implementing when there's a genuine design fork.**
8. **When the user asks to resize/change or "draw" something vague** without naming which type, ask which one(s) before touching code.
9. **Resizing a single marker type**: use a targeted ternary keyed on that type's own boolean.
10. **HTF CBC Flip dot mechanics**: anticipatory dot near still-forming HTF bar's scheduled close; confirmed dot once the HTF bar closes.
11. **Project storage discipline**: only ever keep ONE main-script .pine doc in the project. Same for this handoff doc: full read → edit → full write back, never partial.
12. **LTF CBC Reversal vs. HTF Reversal — two distinct concepts, neither is "engulfing."**
13. **Two time-formatting library helpers exist — pick the right one.**
14. **A single feature addition can trigger a multi-round CE10117 chain.**
15. **Before re-implementing something that sounds like a previously-reverted feature, check the changelog for that revert.**
16. **An array/pass-by-reference restructure is NOT automatically a CE10117 (tokens) win, but CAN be a CE10295 (main-body statement count) win.**
17. **The Pre-Trade Checklist ↔ Status table mapping is an explicit, load-bearing concept as of v7.16/v7.17.**
18. **CE10116 "too many external elements" is a DIFFERENT limit than CE10117 "too many tokens."**
19. **An exported library function CANNOT return a tuple.** Pick one return value; derive anything else at the call site.
20. **CBC direction sources — several distinct variables serve distinct purposes.** `cbc` = LTF live. `cf_f2_htf_bull` = HTF raw/blended. `htf_dir_bull_now` = confirmed last-closed-HTF-bar direction.
21. **CE10095 "already defined" — a duplicate top-level declaration.**
22. **A live screenshot of a feature rendering is strong evidence a round compiled — and a screenshot showing a specific POST-FIX visual detail (not just any rendering) is strong evidence that SPECIFIC fix is live (v7.89 precedent: the cyan handle label appearing at all confirmed the v7.86 sanity gate is running).**
23. **The Pivot Points table's row layout, current as of v7.71.**
24. **The Key Level Alert marker's tooltip includes the crossed level's own price.**
25. **Pine `indicator()` scripts cannot place real trades.**
26. **The changelog-trim size fix is an established, repeatable maintenance move.**
27. **The argument matcher can false-positive on a changelog comment showing an abbreviated example call.**
28. **The matcher can ALSO false-positive on a real call site if any argument is a string literal or function call containing a comma.**
29. **File-wide single-use-variable audit for CE10117 technique (c).** CONFIRMED EXHAUSTED as of v7.48/v7.49.
30. **Large-function-to-library-move method for CE10117 technique (a) at real scale.**
31. **A verification suite built entirely from static/structural checks cannot catch a runtime type-mismatch bug, nor a logic bug that only manifests as a visual/behavioral symptom — those need direct code reading, not guesswork (v7.86 precedent).**
32. **Native TradingView drawing-tool object types have NO Pine Script API for programmatic creation.**
33. **When a parameter becomes unused mid-round, remove the parameter itself in the SAME round.**
34. **CE10237 unused-argument check reports ONE parameter per compile attempt, not all offenders at once.**
35. **An `input.bool` default-value change alone does NOT change what's showing on a chart that already has the indicator added.**
36. **A `var table`/`var box`/`var line`/etc. created exactly once and sized off a value computed at creation time is only as safe as that value's TRUE lifetime maximum.**
37. **When a user asks for something to happen "at bar close" and the block has no `barstate.isconfirmed` gate, add one as its own outer `if`.**
38. **This session's own internal library-revision counter is a LOCAL bookkeeping device — NOT guaranteed to equal TradingView's real published number.** Reconciled 6 times so far (v7.62: 48, v7.66: 49, v7.73: 51, v7.75: 52, v7.82: 57).
39. **When a request says "HTF CBC direction" without further qualification, reach for `htf_dir_bull_now`.**
40. **The Auto Trade Setup cooldown and the bar-close-only gate are two SEPARATE, independently-adjustable knobs.**
41. **The Auto Trade Setup automatic stop/target candidate pool is a deliberately curated subset of the Pivot Points table's own level set. BRSG is explicitly and permanently excluded.**
42. **The `indicator()` title format changed at v7.68**: bare version number, no `-wCBC ` suffix.
43. **The Confluence Score's HTF-related factors are agreement checks between the chart's own live `cbc` and the HTF-derived reading, NOT plain "is HTF bullish/bearish" checks.**
44. **Two separate "last HTF flip timestamp" vars exist**: `htf_last_flip_t` (close time) and `htf_last_flip_t_open` (open time).
45. **Three NY-time formatters exist in the library.**
46. **Chart-level label overlap handling (v7.72) is a post-pass, NOT a change to per-level drawing logic.**
47. **A round that adds new library function CALLS is only usable once the user has published the new library content AND the import line points at that new real version number.**
48. **Auto Trade Setup's optional TP2/SL2 reuses the SAME candidate pool and nearest-distance math as TP1/SL1**, chained off TP1/SL1 not entry. No fallback if nothing qualifies.
49. **The ORB Retest markers/session-tracking use a DIFFERENT, hardcoded session classifier than the user's own configurable Alerts-group session windows.** User said "ignore for now" — do not re-offer.
50. **Pine Script has NO click-event/drag-start API for drawings.** The only genuinely draggable object is `input.price()`/`input.time()`.
51. **CE10295 is a FOURTH distinct compiler/upload limit.** Real fix: relocate top-level code into a genuine function body (comments do NOT count).
52. **`input.price()`/`input.time()`'s `confirm` should default to `false` unless the user genuinely needs a forced one-time placement.**
53. **Pine Script has NO runtime signal for "just added/settings changed" distinct from ordinary historical bar processing.**
54. **A "stop extending / freeze when price does X" request for `extend.right` needs the drawing's function evaluated EVERY bar.**
55. **When a user reports drag confusion between multiple similarly-configured handles, check for on-chart visual distinction first.**
56. **A CE10295 fix is per-instance, not a permanent inoculation.**
57. **A delivered fix is not confirmed by "it makes logical sense" — wait for the user's own next report, and don't assume the SAME fix category works twice.**
58. **CE10295's "main body" size does NOT count comments.** It counts actual top-level code, including code nested inside a top-level `if`/`for`; only a genuine function body is exempt.
59. **When a library export needs many caller-local values, cross-check every one against the ORIGINAL inline code's own call order to any internal helpers it used.**
60. **After any CE10295 fix, measure actual top-level code-line counts (comments/blanks excluded) across the WHOLE file for headroom, not just the section that most recently tripped.**
61. **Before moving a block with `var` object-drawing declarations into a library export, grep every one of those variable names file-wide first.**
62. **When a structural scan turns up more oversized blocks than get moved, record the leftovers with exact line ranges/descriptions.**
63. **Any `input.price()`/`input.time()` "drag handle" whose raw value is used as a plot/label coordinate OR a search anchor needs a sanity-range check against the current price, not just non-zero/non-na.** Reusable pattern: a shared `f_ats_handle_sane(handle, current)`-style helper wired into both the value-consuming and value-plotting logic.
64. **When a user reports difficulty finding/selecting a specific `input.*()` field, consider whether it's simply buried deep in a long group before assuming a code/UI bug.** "Near the top" and "the literal first item" are distinct asks.
65. **A "drag handle" or similar control that only affects the NEXT future event, not anything already on screen, is a legitimate design choice, not automatically a bug** — but when a user's report implies they expected it to move something already visible, ask (via `AskUserQuestion` when available) whether they want the scope widened to also live-update the current/active instance, since that's a real behavior change deserving an explicit choice, not a silent reinterpretation. Once confirmed, the reusable technique is: have the "does this move" function re-run its own snap/compute logic every bar against its OWN currently-active value (not the original trigger-time inputs) — the snap helper's existing "return unchanged if inactive" behavior then makes this a free no-op except when something has actually changed.
66. **`var <explicit-type> x = na` only compiles for types Pine implicitly converts `na` into** (float, int, and drawing-object types like line/label/box/table/array). **For `bool`/`color`/`string`, `na` must be explicitly cast**: `var bool x = bool(na)`, `var color x = color(na)`, `var string x = string(na)`. When introducing a brand-new `var bool`/`var color`/`var string` meant to start as "nothing yet," write the cast form from the start — the bare-`na` form compiles for so many OTHER var types that it's an easy habit to carry over by mistake (v7.89/v7.90 precedent, CE10173). A user's own editor/linter (e.g. VS Code's Pine extension) can catch this class of error even before a TradingView compile attempt — treat that as a valid, often faster source of precise error reports.
67. **Pine's Settings panel orders input GROUPS (not just inputs within a group) by the source-code position of each group's FIRST `input.*()` call** — the group string variable's own declaration point doesn't matter, only where it's first actually used inside an `input.*()` call. To move a whole group to the front of Settings, physically relocate ALL of that group's `input.*()` declarations to before every other group's first `input.*()` call in the file (v7.91 precedent: the entire 17-input "Auto Trade Setup" group was cut from deep in the file and pasted just above the "LTF Signals" group, which had been the de facto first group). This is a pure textual move — check first that none of the relocated inputs reads another input's value at declaration time (rare, but would create a forward-reference problem); the code that CONSUMES the inputs never needs to move, since Pine resolves top-level names by declaration existence, not by proximity to point of use.
68. **"Auto-fill a drag handle input with a computed value" is impossible for TWO independent reasons, not one** — worth checking both before answering: (a) no script can write into any `input.*()` value at runtime (the general one-directional-input wall, established v7.89), AND (b) even a script-computed DEFAULT is impossible separately — `input.price()`'s `defval` parameter must be a compile-time constant literal, never a variable or bar-derived expression, so a handle can't even be given a smart starting default tied to live price. When a user re-asks a variant of an already-declined "write into an input" request, re-verify both angles quickly (it's cheap) but expect the answer to still be no — and look for a PRACTICAL mitigation instead of a code fix: e.g. checking whether the existing sanity-check band (convention #63's `f_ats_handle_sane`) is wide enough that the user only needs to set a handle ONCE per instrument rather than once per trade (true here — a 0.2x-5x band re-evaluated against each new setup's own live target/stop is enormously forgiving in absolute price terms, so a single realistic entry keeps working indefinitely). Explaining that kind of amortized-cost reality can resolve a repeat "make this less tedious" request even when the literal ask can't be implemented.
69. **When a user pushes back with "the script already has X, why can't it just use X automatically" after a feature is declined, check whether the automatic/default case ALREADY does what they're describing** before re-explaining the limitation or reaching for a workaround. If it does, say so plainly and point at exactly where in the code it already happens (v7.92 precedent: "why can't it use the pivots it already has" was answered by pointing out Automatic/handle=0 mode already does exactly that — the drag handles exist only to override that pick). If the user's real want turns out to be adjacent but genuinely new once you dig past the pushback (here: "let me nudge the automatic pick by a step count" is NOT the same ask as "auto-fill the handle," and IS implementable), that's a legitimate, separate feature — distinguish clarifying-what-already-exists from building-something-new, and only reach for `AskUserQuestion` once you're sure it's the latter.

## Open items / things not yet resolved
- **THE #1 OPEN ITEM: get the user's explicit confirmation that CE10295 is actually cleared, plus the real published library version number**, now covering v7.84+v7.85+v7.86+v7.89+v7.90's combined new/changed content in one go (per convention #47; v7.91 added no library content so it doesn't add to this list). Confidence is now HIGH (not just inferred) given the v7.89 round's direct confirmation the v7.86 fix is live, but the exact number and the words "it compiles" still haven't come from the user.
- **The "auto-fill drag handles" request has now been asked twice (v7.89 round, and again 09/26/2026) and confirmed impossible both times for two independent Pine platform reasons.** Treat any further variant of this ask (e.g. "can it remember the last value", "can it start at the current price") the same way — check convention #68's two reasons, then reach for the practical mitigation (set once per instrument) rather than re-investigating from scratch.
- **v7.92's step-count handle mode (+1/-1/etc.) is unconfirmed** — watch for the user's next report on whether a small integer in a handle field resolves to the expected pivot (N steps beyond/back-toward from today's automatic pick), for both the TP1/SL1 (anchored to entry) and TP2/SL2 (anchored to TP1/SL1) cases.
- **v7.91's group reorder is unconfirmed** — watch for the user's next Settings screenshot to confirm "Auto Trade Setup" now renders as the literal first group, ahead of "LTF Signals."
- **v7.90's CE10173 fix is unconfirmed** — watch for the user's next report/linter screenshot to confirm the `active_long` line now compiles clean.
- **v7.89's live-handle-follow and numeric-price-labels are unconfirmed** — this is the biggest behavior change in several rounds; watch closely for the user's next report on whether dragging TP1/SL1/TP2/SL2 now visibly moves the CURRENT setup's box/line/label, and whether the label text shows correct live prices. (Was blocked on the v7.90 compile fix landing first.)
- **v7.87/v7.88's input reordering (two rounds) is unconfirmed** for whether it actually resolved "I can't seem to select it" — may have been a UI quirk unrelated to input order; no further report on this specific complaint yet, though the user has clearly been able to type into the fields successfully in later screenshots (7806, 7810), suggesting selection is no longer an issue.
- **v7.86's TP2 explanation is unconfirmed** — a missing TP2 with Show TP2 checked is expected whenever there's no candidate level beyond TP1 at trigger time, not a bug.
- **v7.84's and v7.85's function-relocation fixes are both now strongly (though not explicitly-worded) confirmed live** — if CE10295 somehow still fires after this, the next candidates are the blocks in the "Next CE10295 headroom candidates" section above.
- **v7.81's handle-identifier labels, v7.80's TP2/SL2 breach-freeze, v7.79's line labels, v7.78's confirm=false fix, v7.77's CE10295 round-1 fix, and v7.76's drag-to-snap handles are all still not EXPLICITLY confirmed by the user as working**, though the v7.86-through-v7.89 screenshots are now strong evidence this whole feature area is live and rendering.
- **ORB Retest markers/session-tracking use a hardcoded classifier unrelated to the user's own configurable Alerts-group session windows — explicitly left unresolved, user said "ignore for now."** Do not implement this or re-offer.
- **v7.74's TP2/SL2 feature is now partially confirmed working (SL2 draws; TP2 confirmed working-as-designed) but not yet explicitly confirmed end-to-end by the user's own words.**
- **Whether VWAP Bounce should also lose priority to the HTF CBC Flip dot** was explicitly left open.
- **A VWAP Bounce redesign discussion was started, then explicitly halted by the user mid-clarification (09/23/2026).** Do not resume or re-offer.
- **Whether to move the confirmed HTF CBC Flip dot earlier (repaint risk tradeoff) was never resolved.**
- **v7.56/v7.57/v7.58's visual restyle and CE10237 fixes, v7.59's Order Blocks default-off, v7.60's RE10039 fix, v7.63's PRICE-direction fix, v7.65's cooldown/mid-candle changes, v7.67's OR-H/OR-L addition, v7.68's title format, v7.69's HTF divergence note, v7.70/v7.71's Price row time display, and v7.72/v7.73's overlap-merge feature are all still not explicitly confirmed by the user as working.**
- **v7.16 through v7.92 have NOT been explicitly compile-confirmed by the user with the word "compiled."** Ask for an explicit "it compiles" confirmation and promote a version to the project per convention #11 once things settle.
- **The Status table's own `status_tbl_collapsed` for-loop gotcha remains unfixed** — low priority.
- **v7.44's Auto Trade Setup stop-loss fallback rule is a literal reading of a somewhat ambiguous answer** — untouched since.
- **The BRSG zone's `else: line.set_x2(...)` extend branch is possibly dead code** — flagged but not yet investigated, low priority.
- **A stale duplicate chart layer (`v4.36-wCBC`) was found loaded alongside a current version on the user's chart** and caused visual confusion that looked like a code bug. Standing lesson: if the user reports a visual discrepancy that doesn't match the code, ask whether an old indicator version might still be loaded on the chart before assuming a code bug.
- **The user is actively using the live chart** (order-entry panel visible in bug-report screenshots, real-time price action, a concurrently-active third-party LuxAlgo overlay) — treat future reports as likely to keep surfacing from real trading sessions, not synthetic testing.

## Version history archive
Full per-version changelog detail for v6.97 through v7.92 lives in this doc's own prior revisions and in each delivered .pine file's own internal changelog comment block (immediately before `//@version=6` in every file under `/mnt/user-data/outputs/`). Consult those directly for full historical detail beyond the summarized conventions/open-items above. **As of v7.83, the delivered main script's own inline changelog header is deliberately terse — this handoff doc is the primary place full per-round narrative detail lives going forward.**
