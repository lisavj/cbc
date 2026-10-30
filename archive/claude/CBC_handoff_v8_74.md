# CBC handoff — pick up here (10/03/2026)

## Current live files (project docs)
| File | Version | Notes |
|---|---|---|
| `pine/CBC_v8_74.pine` | **CBC v8.74** | imports `samuelsuss8/ESLib/18` — the version the user runs |
| `pine/ESLib.pine` | **ESLib v99 rev6** | = published **/18** |
| `web/index_v80.html` | **Alert Feed v80** | deployed at tv-webhook-dashboard.onrender.com (footer shows version) |
| `claude/CBC_START_HERE.md` | running notes | long changelog per version + rules |
| `pine/HTF_v1_01.pine` | added by the user | not touched in this thread |

## Library version numbers (TradingView assigns them on publish)
- /18 = v99 rev6 (current, used by v8.74)
- /19 = v100 (REJECTED range-mode build — do not import)
- /20 = v101 (REJECTED chart-TF build — only if the user published it)
- **Next republish = /20 or /21 — ASK the user before setting the import.**
- After any Pine change the user must: publish ESLib (if changed) → load CBC → **recreate the alert** (alerts snapshot the script version).

## Hard limits (the main pain points)
- **CE10117 token limit (~100,256).** Estimate with `scratchpad/tok.py` (lexical × ~3.07). v8.74 ≈ **32,574 lexical = at the edge**; anything new needs trimming or moving into ESLib.
- **CE10295 "main body too long"** = too many top-level statements (inputs count). v8.72 fixed it by wrapping the trigger section in local `f_ats_trig()` and the cloud rule in `f_clr()` (local functions CAN return tuples; library exports cannot). Put new logic inside functions/library, not top level.
- Trims already done: f_n/f_s/f_d helpers, s_tfm, removed many `maxval=` caps, removed 30 `any_confirmed := true` lines.
- Ready-made relief if needed (in the rejected v100/v101 libs, file `ESLib_v100_reverted.pine` locally): `f_piv_pts_txt` (pivot alert lines) and `f_orb_info` (ORB info block) — saves ~300 tokens + 6 top-level statements.

## What changed this thread (v8.57 → v8.74, all kept)
**Stops/targets**
- SL method checkbox: 3m ATR (SL1 1.0×, SL2 1.5×) vs pivots; TP method checkbox: ATR (TP1 1.5×, TP2 3.0×). Both default OFF.
- The other method's levels shown as darker info rows ("SL1 ATR", "TP1 Piv"…) in price order; pivot cell "1.5×ATR (2.9)"; min-SL pushed stops show "Min 4 (VWAP)" and "+4 (+1.53)".
- Alert level lines built in ESLib (`f_ats_lv_lines`).

**Triggers**
- HTF pierce late window input (default **1**) + trade-colour candle box (ON).
- LTF pierce late window default **1**; late confirm only needs close back beyond the LTF EMA20.
- Momentum break trigger (close beyond last LTF swing, trade colour, HTF aligned) — default ON.
- HTF CBC Flip: "require a pullback first" checkbox, default **OFF** (enters at the flip).
- LTF EMA20 pierce no longer needs close beyond LTF EMA9; alert shows "(closed beyond EMA9: yes/no)".
- HTF half of the cloud rule split into two boxes ("...also close beyond the HTF EMA9 / EMA20"), both **OFF**.
- HTF pierce: "also require close beyond LTF EMA9/20" box, **OFF**.

**Filters (group "Trade Setup Filters", all OFF)**: Choppiness > 61.8, VWAP stretch > 3×ATR, ≥2 HTF flips in 8 HTF candles. Alert line "Filters: CHOP | VWAP ext | HTF flips n/8".

**Other**
- 15m flip-candle info: range vs avg20 / avg4, Prev1–Prev4 H/L/R (info only).
- ORB Retest Pass tooltip rewritten (names the session OR HIGH/LOW + price, WITH/AGAINST HTF CBC).
- Alert Feed v76–v80: no "(15m)" label, wrapped HTF flip-candle cell, ATR/Piv rows, active TP1/TP2/SL1/SL2 rows get an **orange outline**.

## Rejected — do NOT rebuild without a clear new spec
- **v8.75** Range mode (CHOP/pinched-EMA detection + strict/edge/one-per-side/whip rules) and "Suspicious: HTF crossed S1…" labels.
- **v8.76** Chart-TF mode (chart > 5m: setups only from chart CBC flip + chart EMA9/20 pierce).
- User feedback: "did not do what I wanted" / "too confusing". **Before building, restate the exact behaviour in 2–3 lines and get a yes.**

## Open questions / ideas the user raised
- Suspicious labelling when a 15m candle crosses R1/S1/etc. after a flip — wanted, but the v8.75 form was wrong; ask what it should look like (chart label? block? which levels? wick vs close).
- Better behaviour in ranges (quiet vs whippy ranges) — analysis done, nothing kept.
- "Why no setup" debug labels — offered several times, never built.
- HTF EMA values come from the forming 15m candle (lookahead_on, no [1]); history can look cleaner than live — offered fix, not done.
- 15m vs 3m price mismatch the user saw was a chart-data/timezone difference (B-ADJ / different symbol), not an indicator bug.

## Working style that works with this user
- Short answers; tables for comparisons; read screenshots carefully and say when a read is approximate.
- One small change per version; keep defaults safe (new features OFF unless asked).
- Always deliver the files, update the project docs (one CBC .pine + one ESLib + one index html), delete the superseded doc, and update START_HERE.
- Test HTML with Playwright mocks (`/home/claude/srv` s*.py servers, t*.js scripts) before shipping.
