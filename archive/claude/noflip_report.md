HTF-flip close ON (current) vs OFF -- CBC EMA Slope current 3m settings (v1.19 logic = v1.22 / v1.23) -- MES / MGC / MNQ / M2K 3m -- 11/16/2026.
Engine = project claude/all_eng.py (TCase gen + MCase3 exits) with the claude/blk_watch.py v1.19 3m bases:
 MES 3m slope 0.42 / 12 bars, LTF ER 0.15, range gate 5, hour block 13-15, no new setups 16:00-19:00, End 16:00 OFF, flip setups ride
        (no TP, closed by the HTF flip back / SL1 / next setup); SL1 3 ATR min 5, TP1 1.75, 100 % at TP1.
 MGC 3m slope 0.165 / 5 bars, range gate 5, stretch 4, late-away 1 pt; SL1 1.7 ATR min 5 cap 7, TP1 1.7 cap 6, 0 % at TP1 + BE (FLIP 0 %).
 MNQ 3m slope 0.75, LTF ER 0.15, NY OR forming block OFF; SL1 1.7 ATR min 25 cap 60, TP1 1.7 cap 40, 0 % at TP1 + BE.
 M2K 3m slope 0.48, LTF ER 0.23, stretch 4; SL1 3.5 ATR min 3 cap 8, TP1 1.7 cap 3, 0 % at TP1 + BE, trail 1.7 (after TP1).
Variants (exits only; entries unchanged except that a longer-running trade can block a later same-direction setup):
 A = no close on the HTF CBC flip against, for every trade (flip-ride trades then end only at SL1 / 16:00 if on / next opposite setup)
 B = no close on the HTF flip for normal trades; MES flip-ride trades keep their flip-back exit
 C = (0 % at TP1 charts) close on the HTF flip only before TP1; after TP1 (stop at BE) the runner ignores the flip
Net after costs (MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35). z = Δ / (SD x sqrt(trades changed)); robust = z >= 2, all thirds better,
last 4 wk >= 0; promising = z >= 1 and all thirds.

## MGC 3m (bars to 11/16)

Current: thirds +1042 / +145 / +578, last 4 wk +187

| Exit | Trades | Net | Avg | Win % | vs current | z | Change by third | Last 4 wk | Max DD | Worst | Median hold | Exits | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Current: close on HTF flip | 618 | +1766 | +2.86 | 27 % | +0 | +0.0 | +0 / +0 / +0 | +0 | 114 | -7.2 | 24 min | flip 231, trail 226, SL1 148, 16:00 13 |  |
| A. No close on HTF flip (all trades) | 582 | +1724 | +2.96 | 12 % | -42 | -0.1 | -88 / +103 / -57 | +27 | 109 | -7.2 | 30 min | trail 310, SL1 195, 16:00 54, new 23 | worse |
| C. Flip close only before TP1 (runner ignores flip) | 591 | +1977 | +3.35 | 13 % | +211 | +0.9 | -79 / +154 / +137 | +63 | 114 | -7.2 | 27 min | trail 294, SL1 141, flip 83, 16:00 51, new 22 | noise |
