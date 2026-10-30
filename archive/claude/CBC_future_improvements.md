# CBC — Possible Future Improvements

Started 09/27/2026 at v8.00 (current: v8.01). A running list of ideas that came up but haven't been built. Add to it whenever a new idea gets offered and deferred. Remove an item (or move it to "Done") once it ships.

## Auto Trade Setup

1. **Live mode for the Trade Levels box / setup levels.** Today TP1/TP2/SL1/SL2 are locked in when the setup triggers; only Price and Pts update live. Option: a toggle that re-picks the levels every bar from the current price, so the box always shows the next levels ahead of and behind price. Trade-off: the stop and targets drift mid-trade, so it becomes more of a "nearby levels" map than a trade plan. Would likely be a separate mode, not a replacement.
2. **"ATS Steps" helper indicator.** A tiny separate indicator whose Settings has only the 4 step fields (TP1/SL1/TP2/SL2). The main script reads them via `input.source()` (one-time linking per chart layout), and changing a value auto-recalculates the main script. Only step counts would pass through, not typed prices.
3. **Decide what negative steps (-1/-2) should do.** In Automatic mode they almost never move anything, because Automatic already picks the nearest level (-N only counts same-price duplicates). Options: (a) drop negative numbers entirely, keeping 0 = Automatic and +N = farther; (b) add closer levels to the candidate pool (for example recent chart-timeframe swing highs/lows or EMA20; BRSG stays excluded) so -1 has somewhere to step to, with Automatic still choosing what it chooses today.
4. **Mirror the Pivot Points table's R2/R3/S2/S3 auto-escalation in the candidate pool.** v7.99 made the "(table only)" toggles feed the pool, but the table's own "show R2 once price is past R1" auto-escalation isn't mirrored. Only matters if the table-only toggles are turned off.
5. **Optional Entry row in the Trade Levels box.** Entry was added without being asked for; could become a toggle if it's unwanted.
6. **Stop-loss fallback rule (from v7.44) is a literal reading of an ambiguous answer.** When no candidate level exists, the stop falls back to the HTF flip candle's low/high. Worth confirming that's what's wanted.

## Headroom / maintenance (CE10295 "main body too long")

7. **Next blocks to move into the library if CE10295 comes back** (re-measure line counts first; offsets have shifted since v7.85):
   - `if not na(YDH)` (~91 code lines) + its paired `if new_day` (~41), which draws/resets the YDH/YDL/PMH/PML/session H-L lines. Move them together as one function.
   - `if show_lvl_lbl` (~71 code lines), the chart-level label overlap-merge pass from v7.72.
8. **Status table `status_tbl_collapsed` for-loop gotcha.** Known, unfixed, low priority.
9. **BRSG zone `else: line.set_x2(...)` extend branch may be dead code.** Flagged, not investigated.

## Signals / markers (open design questions)

10. **Should VWAP Bounce also lose shared-bar priority to the HTF CBC Flip dot?** Left open.
11. **Move the confirmed HTF CBC Flip dot earlier?** It would show sooner but risk repainting. Never decided.

## Parked by the user — do NOT re-offer unless they bring it up

- ORB Retest markers use a hardcoded session classifier, separate from the configurable Alerts-group session windows ("ignore for now").
- VWAP Bounce redesign (halted mid-clarification 09/23/2026).
- Real draggable handles (`input.price` with `confirm=true`). The user doesn't want dragging; steps replaced it.

## Done (moved from this list)
- *(nothing yet)*
