# ㉒ Opening Range session toggles (NY / London / Asian) -- MES 3m, MGC 3m (v1.08 settings), MNQ 3m (v1.08 settings) -- 11/14/2026

OR length (㉒, live 30 min) sets the OR-forming no-setup windows (NY 09:30, London 03:00, Asia 20:00) and the session OR highs / lows used by the ③ ER breakout exception. LTF pivot N (⑥ LTF Signals "N", live 2) sets the swing highs / lows used by the breakout exception and the Momentum break trigger (Momentum not replayed). ⑩ Price Action Structure lengths (internal 5 / swing 50) only draw HH/HL markers -- not used by setups. Breakout window = "...breakout exception" bars (live 3). OR levels recomputed from bars for every row (base included). One change at a time.
## Candidates (promising or better)

- none


## MES 3m

Base: 749 trades, net +691, thirds +326 / -73 / +438, last 4 wk +210, max DD 169

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| OR session New York OFF (no NY OR levels) | 744 | +679 | -12 | -0.6 | -10 / -2 / +0 | +0 | 164 | worse |
| OR session London OFF | 742 | +670 | -21 | -0.9 | -18 / +0 / -3 | +0 | 167 | worse |
| OR session Asian OFF | 739 | +680 | -10 | -0.4 | +2 / -7 / -5 | +0 | 175 | worse |
| All three OR sessions OFF | 722 | +621 | -70 | -1.5 | -47 / -17 / -6 | +3 | 178 | worse |

## MGC 3m

Base: 627 trades, net +1164, thirds +564 / +82 / +517, last 4 wk +279, max DD 117

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| OR session New York OFF (no NY OR levels) | 616 | +1136 | -27 | -0.4 | +8 / -2 / -33 | -46 | 117 | worse |
| OR session London OFF | 612 | +1201 | +37 | +0.5 | +25 / +9 / +4 | +4 | 109 | noise |
| OR session Asian OFF | 610 | +1200 | +36 | +0.4 | +32 / +11 / -7 | +0 | 103 | noise |
| All three OR sessions OFF | 580 | +1184 | +20 | +0.2 | +37 / +18 / -34 | -42 | 94 | noise |

## MNQ 3m

Base: 443 trades, net +3944, thirds +1208 / +929 / +1807, last 4 wk +800, max DD 285

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| OR session New York OFF (no NY OR levels) | 441 | +3870 | -74 | -0.8 | -14 / +0 / -60 | +0 | 319 | worse |
| OR session London OFF | 442 | +3827 | -116 | -1.0 | +0 / -47 / -69 | -69 | 285 | worse |
| OR session Asian OFF | 440 | +3924 | -20 | -0.2 | -68 / +48 / +0 | +0 | 285 | worse |
| All three OR sessions OFF | 437 | +3280 | -664 | -3.2 | -82 / +0 / -583 | -523 | 319 | worse |

## Verdict (11/14/2026)

The ㉒ session boxes (New York / London / Asian) decide whether that session's OR high / low exists, which feeds the ③ ER breakout exception (and inside-OR-after-set blocks, off; OR levels in the level pool / ORB alerts). The OR-forming no-setup windows are time-based and do NOT depend on these boxes. Keep all three ON: MES all OFF -70, MNQ all OFF -664 (z -3.2); single sessions noise or worse; MGC London / Asian OFF +37 / +36 noise. OR length 30 min: see orpa_report (keep). The other 14 inputs (colours, lines, widths, shading, label text) are display only.
