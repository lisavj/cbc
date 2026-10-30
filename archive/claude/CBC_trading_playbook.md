# CBC 3-Option Trading Playbook

Captured from the annotated chart screenshot (session-open range, HTF EMA9/20 cloud in red, CBC flip long at (1), 20EMA test at (2), CBC flip short at (3)).

When price is chopping around the HTF EMA9/20 zone after a CBC flip, there are 3 ways to trade it:

## Option 1 — Trade CBC long (BRSG)

**Setup:** A CBC flip fires (confirmed, HTF closed) while price action is pushing into the HTF EMA9/20 zone — not fully cleared through it, sitting between the two EMAs at the moment of the flip.

**Status:** this is the existing "partial confirmation" case (`a_htf_flip_between`) in `CBC_v6_00_with_OrderBlocks.pine` — it already fires alongside the regular confirmed HTF CBC Flip alert, with the BRSG Entry Zone High/Low lines appended automatically. A follow-up relabeled its suffix/note text to explicit "Option 1 Setup" wording, then that relabel was undone per request — the alert still fires on the same condition, just back to its original "partial confirmation" wording rather than named "Option 1" language.

## Option 2 — Short the 20EMA (smaller size)

**Setup:** *(from the screenshot: "20EMA test for short (2)")* — price rallies back up to test the 20 EMA from below/inside the zone before the CBC has confirmed a new direction; take a smaller-size short against that test rather than waiting for full confirmation.

**Status:** not yet implemented — needs the precise entry trigger (e.g. a rejection wick off the 20 EMA, a specific touch-and-reverse condition) defined before it can be coded as an alert.

## Option 3 — Wait for CBC confirmation short, then SGCR

**Setup:** *(from the screenshot: "CBC flip short (3)")* — instead of anticipating, wait for the CBC to actually flip short (confirmed, bar/HTF closed), then execute SGCR (entry method still to be defined/confirmed).

**Status:** not yet implemented — needs SGCR's exact meaning/trigger defined before it can be coded.

---
*Options 2 and 3 are noted here as placeholders from the original screenshot. Option 1's condition already exists in the indicator (unchanged logic); only its alert wording was tried and reverted.*
