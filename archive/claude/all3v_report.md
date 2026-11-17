# ①②③ full sweep -- MES / MGC 3m on v1.17 settings -- 11/15/2026

Replay Jan 5 -> Nov 13, one change at a time, net after costs. MGC 3m now modelled with the live toward late-away 1 pt (earlier MGC replays used strict away): base 800 / +1182 / DD 166 (strict: 627 / +1164 / DD 117). Script all3v_study.py + mgc3_nb.py (engine all_eng117.py: v1.17 bases, deep-merge). MTF (60m) gate row inert in this engine (tested earlier: MES -203).

## Verdict
- MES 3m: nothing promising or better. Current v1.17 MES 3m set confirmed (13-15 block, window to 19:00, End OFF each worse when undone; slope 0.42 / 36-min lookback best).
- MGC 3m: candidates, all promising only (z 1.1-1.8, last 4 wk mostly negative): 15-min slope lookback (5 bars) 0.15-0.18 (+416..+601, DD 166 -> 99-130); range gate OFF (+263, = gate 3 ATR); late-away 2-3 pts (+70..+107, only 3rd third); combos range OFF + 15-min lookback 0.15 +656 (z 1.6, last 4 wk -92). Not robust -> not implemented yet.

# ①②③ inputs check -- MES / MGC 3m on v1.17 settings -- 11/15/2026

Replay Jan 5 -> Nov 13, one change at a time on each chart's v1.17 settings (MES 3m: slope 0.42, LTF ER 0.15, range gate 5, flip ride, SL1 3 ATR no cap, TP1 1.75 ATR, 100 % at TP1, BE, strict away, 13-15 block, no setups 16:00-19:00, End 16:00 OFF; MGC 3m: slope 0.30, range gate 5, stretch 4, FLIP 0 %, SL1 1.7 cap 7, TP1 1.7 cap 6, toward late-away 1 pt), net after costs (MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35). 
## Candidates (promising or better)

- none


## MES 3m (v1.17)

Base: 739 trades, net +809, avg +1.09, thirds +354 / -8 / +462, last 4 wk +217, max DD 142

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 686 | +760 | -49 | -0.6 | -31 / -6 / -12 | -7 | 140 | worse |
| ③ CHOP > 58 block | 625 | +755 | -54 | -0.5 | -12 / -18 / -24 | -21 | 140 | worse |
| ③ ADX < 20 block | 537 | +565 | -244 | -1.8 | -104 / +9 / -148 | -109 | 136 | worse |
| ③ ADX < 15 block | 687 | +795 | -13 | -0.2 | +6 / +28 / -47 | -15 | 139 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 680 | +684 | -125 | -1.5 | -59 / +34 / -100 | -56 | 131 | worse |
| ③ crosses >= 6 block | 730 | +774 | -35 | -0.9 | +5 / -8 / -31 | +0 | 142 | worse |
| ③ N-bar range < 2 ATR block | 725 | +763 | -45 | -1.1 | -31 / -11 / -4 | +0 | 148 | worse |
| ③ N-bar range < 3 ATR block | 536 | +626 | -183 | -1.3 | -50 / -20 / -112 | -85 | 134 | worse |
| ③ HTF flips >= 2 in 8 block | 313 | +59 | -749 | -3.8 | -300 / -40 / -410 | -151 | 82 | robustly worse |
| ③ HTF flips >= 3 in 8 block | 643 | +766 | -43 | -0.4 | -29 / +45 / -59 | -28 | 108 | worse |
| ③ HTF flips >= 4 in 8 block | 722 | +733 | -76 | -1.7 | -26 / -16 / -34 | -17 | 142 | worse |
| ③ Skip non-flip setups from 6 HTF candles after flip | 534 | +850 | +42 | +0.3 | +41 / +28 / -28 | -65 | 133 | noise |
| ③ ... from 9 | 637 | +769 | -40 | -0.4 | -4 / -29 / -7 | -25 | 148 | worse |
| ③ ... from 12 | 690 | +860 | +51 | +0.7 | +9 / +26 / +17 | -4 | 129 | noise |
| ③ Block if VWAP -3 / +2 pts | 686 | +768 | -41 | -0.6 | -55 / +18 / -4 | -11 | 107 | worse |
| ③ Block if EMA200 -3 / +2 pts | 715 | +789 | -20 | -0.4 | -20 / +7 / -7 | -4 | 137 | worse |
| ③ Environment EMA200 vs VWAP | 325 | +352 | -456 | -2.3 | -180 / -8 / -268 | -78 | 77 | robustly worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 709 | +671 | -137 | -2.6 | -71 / +11 / -78 | -74 | 142 | worse |
| ③ Skip if SL1 cap < 1.5 ATR | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ③ ER 0.18 | 792 | +804 | -4 | -0.1 | +47 / -50 / -1 | -0 | 151 | worse |
| ③ ER 0.20 | 769 | +812 | +4 | +0.1 | +2 / -2 / +4 | -2 | 138 | noise |
| ③ ER 0.26 | 703 | +788 | -21 | -0.3 | -10 / +0 / -11 | +12 | 143 | worse |
| ③ ER 0.30 | 663 | +680 | -129 | -1.3 | -48 / -19 / -61 | -58 | 139 | worse |
| ③ ER filter OFF | 841 | +843 | +34 | +0.3 | +77 / -53 / +9 | +11 | 159 | noise |
| ③ ER breakout exception OFF | 561 | +748 | -61 | -0.4 | -139 / -0 / +79 | +37 | 145 | worse |
| ③ Range gate 4 ATR | 819 | +732 | -77 | -0.8 | -20 / -96 / +38 | +20 | 161 | worse |
| ③ Range gate 6 ATR | 698 | +602 | -207 | -2.8 | -65 / -62 / -80 | +9 | 188 | robustly worse |
| ③ Range gate zone 30 % | 645 | +715 | -94 | -0.9 | -30 / +25 / -89 | -64 | 147 | worse |
| ③ Range gate OFF | 898 | +822 | +13 | +0.1 | +58 / -75 / +30 | +13 | 155 | noise |
| ③ VWAP stretch 3 ATR | 310 | +290 | -518 | -2.6 | -190 / +7 / -335 | -164 | 96 | worse |
| ③ VWAP stretch 6 ATR | 586 | +609 | -200 | -1.6 | -68 / -103 / -29 | -84 | 196 | worse |
| ③ VWAP stretch ON 4 ATR | 419 | +510 | -299 | -1.7 | -59 / -25 / -216 | -105 | 126 | worse |
| ① Flip min ER 0.15 | 757 | +765 | -44 | -0.8 | -21 / -4 / -18 | -6 | 138 | worse |
| ① Flip min ER 0.30 | 724 | +653 | -155 | -3.0 | +1 / +17 / -174 | -44 | 141 | worse |
| ① Toward late-away 1 pt (instead of strict) | 867 | +853 | +44 | +0.4 | +8 / +73 / -36 | -6 | 116 | noise |
| ① SL1 x 1.5 ATR | 743 | +529 | -280 | -2.3 | -51 / -107 / -122 | -61 | 178 | robustly worse |
| ① SL1 x 2.0 | 743 | +682 | -127 | -1.2 | -19 / -27 / -81 | -38 | 172 | worse |
| ① SL1 x 2.5 | 742 | +788 | -21 | -0.2 | -27 / -5 / +11 | +16 | 159 | worse |
| ① SL1 x 3.0 | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① SL1 x 3.5 | 738 | +790 | -19 | -0.3 | -8 / +11 / -22 | -16 | 142 | worse |
| ① TP1 x 1.25 ATR | 754 | +729 | -80 | -0.4 | -117 / +75 / -38 | -13 | 67 | worse |
| ① TP1 x 1.5 | 745 | +777 | -31 | -0.2 | -82 / +51 / -0 | -14 | 86 | worse |
| ① TP1 x 1.75 | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① TP1 x 2.0 | 728 | +816 | +7 | +0.0 | +69 / -75 / +14 | -1 | 187 | noise |
| ① TP1 x 2.5 | 711 | +780 | -28 | -0.2 | +14 / -21 / -21 | -6 | 172 | worse |
| ① Close at TP1 0 % | 700 | +727 | -82 | -0.5 | +72 / -104 / -50 | +12 | 207 | worse |
| ① Close at TP1 50 % | 700 | +732 | -77 | -0.4 | +14 / -61 / -29 | +2 | 162 | worse |
| ① Close at TP1 80 % | 700 | +735 | -73 | -0.4 | -21 / -36 / -17 | -4 | 144 | worse |
| ① Close at TP1 100 % | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Breakeven at TP1 OFF | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Trail 1.3 ATR | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Trail 1.7 ATR | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Trail 2.5 ATR | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Trail 3.5 ATR | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① No trail | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Min SL x 0.6 | 739 | +812 | +3 | +0.1 | -1 / +1 / +3 | +0 | 142 | noise |
| ① Min SL x 1.4 | 739 | +803 | -6 | -0.1 | -1 / +5 / -9 | +0 | 142 | worse |
| ① Max SL1 cap OFF | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Max TP1 cap OFF | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Time stop 10 candles (< 0.5 ATR progress) | 743 | +765 | -44 | -0.9 | -25 / +8 / -28 | -8 | 133 | worse |
| ① Time stop 20 candles | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Flip ride OFF (flip setups use TP1) | 739 | +381 | -428 | -5.9 | -38 / -80 / -310 | -92 | 208 | robustly worse |
| ① 13:00-15:00 block OFF | 815 | +636 | -173 | -2.0 | -19 / -101 / -53 | -36 | 196 | worse |
| ① Block 13:00-14:00 only | 782 | +748 | -61 | -0.9 | -7 / -40 / -14 | -4 | 155 | worse |
| ① No new setups to 18:45 (window as v10.97) | 749 | +764 | -45 | -1.5 | -7 / -34 / -4 | +0 | 150 | worse |
| ① End setups at 16:00 ON | 739 | +736 | -73 | -1.9 | -21 / -32 / -21 | -8 | 135 | worse |
| ① Toward late-away 1 pt | 867 | +853 | +44 | +0.4 | +8 / +73 / -36 | -6 | 116 | noise |
| ① Skip setups against MTF (60m) CBC | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ③ Slope 0.34 | 885 | +617 | -191 | -1.5 | +22 / -169 / -44 | +7 | 231 | worse |
| ③ Slope 0.38 | 812 | +729 | -80 | -0.9 | +29 / -91 / -18 | +1 | 176 | worse |
| ③ Slope 0.46 | 687 | +742 | -67 | -0.8 | -42 / +36 / -62 | -56 | 122 | worse |
| ③ Slope 0.50 | 642 | +668 | -140 | -1.3 | -120 / +47 / -68 | -41 | 109 | worse |
| ③ Slope lookback 5 bars (15 min), slope 0.158 | 810 | +720 | -89 | -0.5 | -147 / +85 / -27 | -51 | 165 | worse |
| ③ Slope lookback 5 bars (15 min), slope 0.175 | 740 | +726 | -83 | -0.5 | -87 / +63 / -59 | -71 | 140 | worse |
| ③ Slope lookback 5 bars (15 min), slope 0.193 | 668 | +759 | -50 | -0.3 | -126 / +81 / -5 | -75 | 130 | worse |
| ③ Slope lookback 10 bars (30 min), slope 0.315 | 842 | +624 | -185 | -1.3 | -63 / -109 / -13 | +3 | 186 | worse |
| ③ Slope lookback 10 bars (30 min), slope 0.350 | 764 | +617 | -192 | -1.5 | -62 / -83 / -47 | -5 | 164 | worse |
| ③ Slope lookback 10 bars (30 min), slope 0.385 | 679 | +692 | -117 | -1.0 | -106 / +13 / -24 | -13 | 147 | worse |
| ③ Slope lookback 15 bars (45 min), slope 0.473 | 806 | +618 | -190 | -1.6 | -50 / -93 / -48 | -35 | 192 | worse |
| ③ Slope lookback 15 bars (45 min), slope 0.525 | 756 | +600 | -209 | -1.8 | -125 / -43 / -41 | -21 | 156 | worse |
| ③ Slope lookback 15 bars (45 min), slope 0.578 | 696 | +649 | -159 | -1.3 | -113 / +1 / -47 | -3 | 149 | worse |
| ② LTF pierce late window 0 | 694 | +803 | -6 | -0.1 | -21 / -3 / +18 | +10 | 147 | worse |
| ② LTF pierce late window 2 | 752 | +850 | +41 | +1.0 | +16 / -7 / +33 | +11 | 142 | noise |
| ② HTF pierce late window 0 | 723 | +815 | +7 | +0.1 | +3 / +16 / -13 | -18 | 140 | noise |
| ② HTF pierce late window 2 | 744 | +803 | -6 | -0.2 | +0 / -11 / +5 | +5 | 146 | worse |
| ② HTF late trade-colour OFF | 742 | +810 | +2 | +0.1 | +0 / +1 / +0 | +0 | 142 | noise |
| ② HTF pierce replaces current setup | 743 | +833 | +24 | +1.3 | -3 / -6 / +32 | +26 | 142 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ② Flip: require pullback first (wait 10) | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ② Trigger HTF CBC Flip OFF | 677 | +349 | -460 | -4.1 | +7 / -86 / -382 | -112 | 230 | worse |
| ② Trigger LTF EMA20 Pierce OFF | 400 | +640 | -169 | -0.8 | -103 / -33 / -33 | -51 | 100 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 590 | +844 | +35 | +0.3 | -63 / +151 / -52 | -17 | 98 | noise |
| ② Trigger HTF EMA20 Pierce OFF | 719 | +735 | -74 | -1.6 | -43 / -10 / -21 | -19 | 151 | worse |
| ① Flip distance 1.5 ATR | 736 | +758 | -51 | -3.1 | -11 / +6 / -46 | +0 | 142 | worse |
| ① Flip distance 3 ATR | 749 | +739 | -69 | -2.1 | -58 / -16 / +4 | +5 | 142 | worse |
| ① Flip side gate OFF | 740 | +806 | -3 | -0.3 | -3 / +0 / +0 | +0 | 142 | worse |
| ① Flip side gate 2 pts | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① Flip VWAP slope OFF | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① HTF pierce min ER 0 | 919 | +789 | -20 | -0.1 | -25 / +67 / -61 | -20 | 129 | worse |
| ① HTF pierce min ER 0.23 | 676 | +753 | -55 | -0.6 | -75 / +29 / -9 | +2 | 140 | worse |
| ① LTF pierce min ER 0.12 | 801 | +758 | -50 | -0.6 | +19 / -40 / -29 | -31 | 158 | worse |
| ① LTF pierce min ER 0.15 | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① LTF pierce min ER 0.23 | 649 | +845 | +36 | +0.3 | -47 / -22 / +105 | +48 | 146 | noise |
| ① VWAP reclaim block OFF | 764 | +813 | +4 | +0.1 | +6 / -13 / +10 | +2 | 131 | noise |
| ① VWAP reclaim block 8 | 738 | +803 | -6 | -0.6 | +0 / +0 / -6 | +0 | 142 | worse |
| ① Min candles between setups 5 | 750 | +830 | +21 | +0.5 | +5 / -16 / +33 | +26 | 147 | noise |
| ① Min candles 15 | 715 | +774 | -35 | -0.7 | -45 / +5 / +5 | -8 | 135 | worse |
| ① ATR length 10 | 741 | +725 | -84 | -0.4 | -44 / -1 / -39 | -24 | 112 | worse |
| ① ATR length 20 | 747 | +702 | -107 | -0.6 | -7 / -50 / -50 | -4 | 172 | worse |
| ① No new setups 16:00-19:00 | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |
| ① No-new-setup window OFF | 810 | +750 | -59 | -0.7 | -17 / -53 / +12 | +20 | 166 | worse |
| ① OR forming blocks all OFF | 808 | +768 | -41 | -0.5 | -8 / -73 / +40 | +15 | 170 | worse |
| ① End setups at 16:00 OFF | 739 | +809 | +0 | +0.0 | +0 / +0 / +0 | +0 | 142 | noise |


# ①②③ inputs check -- MES / MGC 3m on v1.17 settings -- 11/15/2026

Replay Jan 5 -> Nov 13, one change at a time on each chart's v1.17 settings (MES 3m: slope 0.42, LTF ER 0.15, range gate 5, flip ride, SL1 3 ATR no cap, TP1 1.75 ATR, 100 % at TP1, BE, strict away, 13-15 block, no setups 16:00-19:00, End 16:00 OFF; MGC 3m: slope 0.30, range gate 5, stretch 4, FLIP 0 %, SL1 1.7 cap 7, TP1 1.7 cap 6, toward late-away 1 pt), net after costs (MES 0.50, MGC 0.22, MNQ 0.87, M2K 0.35). 
## Candidates (promising or better)

- MGC 3m: ③ Range gate 4 ATR -> +180, z +1.2, thirds +17 / +142 / +21, last 4 wk -13, max DD 173 vs 166 (promising)
- MGC 3m: ③ Range gate OFF -> +263, z +1.3, thirds +104 / +125 / +34, last 4 wk -24, max DD 138 vs 166 (promising)
- MGC 3m: ① Toward late-away 2 pts -> +70, z +1.2, thirds +1 / +3 / +66, last 4 wk +41, max DD 163 vs 166 (promising)
- MGC 3m: ③ Slope lookback 5 bars (15 min), slope 0.138 -> +382, z +1.1, thirds +223 / +106 / +53, last 4 wk -21, max DD 123 vs 166 (promising)


## MGC 3m (v1.17)

Base: 800 trades, net +1182, avg +1.48, thirds +669 / +7 / +505, last 4 wk +255, max DD 166

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| ③ CHOP > 61.8 block | 739 | +1101 | -80 | -0.5 | -7 / +43 / -115 | -49 | 146 | worse |
| ③ CHOP > 58 block | 665 | +904 | -278 | -1.3 | -144 / +42 / -176 | -41 | 146 | worse |
| ③ ADX < 20 block | 618 | +828 | -353 | -1.6 | -88 / -120 / -145 | -114 | 279 | worse |
| ③ ADX < 15 block | 770 | +1110 | -71 | -0.8 | -86 / -4 / +19 | +7 | 171 | worse |
| ③ EMA20/VWAP crosses >= 4 block | 716 | +1248 | +66 | +0.4 | +112 / -57 / +11 | -44 | 220 | noise |
| ③ crosses >= 6 block | 791 | +1193 | +12 | +0.2 | -8 / +31 / -11 | +0 | 147 | noise |
| ③ N-bar range < 2 ATR block | 790 | +1125 | -56 | -1.0 | -11 / +6 / -51 | -48 | 167 | worse |
| ③ N-bar range < 3 ATR block | 570 | +798 | -383 | -1.5 | -181 / +17 / -219 | -47 | 154 | worse |
| ③ HTF flips >= 2 in 8 block | 397 | +82 | -1100 | -3.3 | -636 / -0 / -463 | -239 | 95 | robustly worse |
| ③ HTF flips >= 3 in 8 block | 700 | +771 | -411 | -2.2 | -259 / -34 / -118 | -137 | 159 | robustly worse |
| ③ HTF flips >= 4 in 8 block | 779 | +1188 | +6 | +0.1 | -9 / +21 / -5 | -21 | 143 | noise |
| ③ Skip non-flip setups from 6 HTF candles after flip | 588 | +1203 | +22 | +0.1 | +49 / +14 / -42 | -24 | 169 | noise |
| ③ ... from 9 | 702 | +1203 | +22 | +0.1 | +46 / +1 / -26 | -35 | 155 | noise |
| ③ ... from 12 | 762 | +1231 | +50 | +0.5 | +7 / +30 / +13 | -6 | 146 | noise |
| ③ Block if VWAP -3 / +2 pts | 728 | +1134 | -47 | -0.3 | -17 / +2 / -33 | +6 | 159 | worse |
| ③ Block if EMA200 -3 / +2 pts | 741 | +1176 | -5 | -0.0 | -12 / +21 / -14 | +0 | 157 | worse |
| ③ Environment EMA200 vs VWAP | 300 | +407 | -775 | -2.2 | -455 / +67 / -386 | -271 | 55 | worse |
| ③ Skip while ATR > 1.8 x ATR(100) | 770 | +1056 | -125 | -1.3 | -153 / -5 / +32 | +5 | 153 | worse |
| ③ Skip if SL1 cap < 1.5 ATR | 493 | +493 | -689 | -2.4 | -632 / -13 / -44 | -122 | 74 | robustly worse |
| ③ ER 0.18 | 856 | +1119 | -62 | -0.4 | -19 / -12 / -32 | -34 | 193 | worse |
| ③ ER 0.20 | 840 | +1169 | -13 | -0.1 | -4 / -7 / -2 | -3 | 192 | worse |
| ③ ER 0.26 | 782 | +1189 | +7 | +0.1 | +27 / +19 / -39 | +3 | 154 | noise |
| ③ ER 0.30 | 759 | +1208 | +26 | +0.2 | +50 / -8 / -16 | -0 | 175 | noise |
| ③ ER filter OFF | 936 | +1191 | +9 | +0.0 | -27 / +61 / -24 | -31 | 191 | noise |
| ③ ER breakout exception OFF | 506 | +712 | -470 | -1.5 | -335 / -54 / -81 | -69 | 212 | worse |
| ③ Range gate 4 ATR | 851 | +1361 | +180 | +1.2 | +17 / +142 / +21 | -13 | 173 | promising |
| ③ Range gate 6 ATR | 769 | +1068 | -114 | -0.9 | +14 / +10 / -138 | -65 | 156 | worse |
| ③ Range gate zone 30 % | 724 | +1178 | -4 | -0.0 | -11 / +22 / -15 | -46 | 155 | worse |
| ③ Range gate OFF | 883 | +1444 | +263 | +1.3 | +104 / +125 / +34 | -24 | 138 | promising |
| ③ VWAP stretch 3 ATR | 626 | +903 | -279 | -1.3 | -94 / -128 / -56 | -3 | 252 | worse |
| ③ VWAP stretch 6 ATR | 1014 | +1029 | -152 | -0.6 | -123 / -47 / +18 | +37 | 203 | worse |
| ③ VWAP stretch OFF | 1268 | +1226 | +45 | +0.1 | -33 / -32 / +110 | +49 | 181 | noise |
| ① Flip min ER 0.15 | 806 | +1203 | +21 | +0.3 | -0 / +32 / -10 | +1 | 151 | noise |
| ① Flip min ER 0.30 | 794 | +1221 | +39 | +0.5 | +18 / +7 / +14 | +7 | 165 | noise |
| ① Toward late-away 1 pt (instead of strict) | 800 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ① SL1 x 1.5 ATR | 800 | +1142 | -39 | -0.3 | +5 / +3 / -47 | +2 | 175 | worse |
| ① SL1 x 2.0 | 797 | +1161 | -21 | -0.2 | -5 / -8 / -7 | -2 | 176 | worse |
| ① SL1 x 2.5 | 797 | +1150 | -31 | -0.2 | -13 / -4 / -15 | -8 | 181 | worse |
| ① SL1 x 3.0 | 797 | +1155 | -26 | -0.2 | -16 / -4 / -6 | -9 | 182 | worse |
| ① SL1 x 3.5 | 797 | +1153 | -28 | -0.2 | -16 / -5 / -7 | -9 | 183 | worse |
| ① TP1 x 1.25 ATR | 804 | +1188 | +7 | +0.1 | +8 / +16 / -17 | -25 | 152 | noise |
| ① TP1 x 1.5 | 800 | +1200 | +18 | +0.3 | +6 / +21 / -9 | -7 | 146 | noise |
| ① TP1 x 1.75 | 800 | +1176 | -6 | -0.2 | +0 / +0 / -5 | +0 | 166 | worse |
| ① TP1 x 2.0 | 799 | +1183 | +2 | +0.0 | -5 / +24 / -17 | +2 | 181 | noise |
| ① TP1 x 2.5 | 797 | +1185 | +3 | +0.0 | -10 / +36 / -23 | +2 | 175 | noise |
| ① Close at TP1 0 % | 800 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ① Close at TP1 50 % | 800 | +825 | -357 | -1.1 | -239 / +63 / -181 | -87 | 97 | worse |
| ① Close at TP1 80 % | 800 | +611 | -571 | -1.8 | -383 / +102 / -289 | -139 | 57 | worse |
| ① Close at TP1 100 % | 861 | +438 | -744 | -2.2 | -457 / +116 / -403 | -182 | 66 | worse |
| ① Breakeven at TP1 OFF | 760 | +1027 | -155 | -0.6 | -152 / +64 / -67 | -22 | 211 | worse |
| ① Trail 1.3 ATR | 848 | +685 | -496 | -1.7 | -132 / +27 / -391 | -114 | 125 | worse |
| ① Trail 1.7 ATR | 835 | +951 | -231 | -0.9 | -93 / +18 / -157 | -31 | 150 | worse |
| ① Trail 2.5 ATR | 815 | +950 | -231 | -1.2 | -191 / +7 / -47 | -11 | 175 | worse |
| ① Trail 3.5 ATR | 804 | +1160 | -21 | -0.2 | -27 / +8 / -2 | +18 | 149 | worse |
| ① No trail | 800 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ① Min SL x 0.6 | 800 | +1069 | -113 | -1.2 | +4 / +0 / -117 | +2 | 165 | worse |
| ① Min SL x 1.4 | 797 | +1158 | -23 | -0.2 | -16 / -5 / -1 | -9 | 183 | worse |
| ① Max SL1 cap OFF | 799 | +1231 | +50 | +0.3 | +19 / +13 / +18 | +2 | 155 | noise |
| ① Max TP1 cap OFF | 791 | +1116 | -65 | -0.5 | -95 / +18 / +12 | +14 | 189 | worse |
| ① Time stop 10 candles (< 0.5 ATR progress) | 800 | +1176 | -6 | -0.1 | -3 / -18 / +16 | +5 | 194 | worse |
| ① Time stop 20 candles | 800 | +1186 | +4 | +0.2 | +0 / +4 / +0 | +0 | 165 | noise |
| ① Flip ride ON | 800 | +1188 | +7 | +0.1 | -55 / +75 / -13 | -4 | 168 | noise |
| ① Flip distance floor 10 pts | 801 | +1185 | +4 | +0.1 | +0 / +4 / +0 | +0 | 162 | noise |
| ① Toward late-away strict (0) | 627 | +1164 | -18 | -0.1 | -105 / +75 / +12 | +23 | 117 | worse |
| ① Toward late-away 2 pts | 790 | +1252 | +70 | +1.2 | +1 / +3 / +66 | +41 | 163 | promising |
| ③ Slope 0.24 | 930 | +992 | -190 | -0.9 | -115 / -24 / -51 | -12 | 209 | worse |
| ③ Slope 0.27 | 867 | +1047 | -134 | -0.9 | -59 / -32 / -43 | -2 | 202 | worse |
| ③ Slope 0.33 | 734 | +1248 | +66 | +0.5 | +29 / -15 / +53 | +10 | 165 | noise |
| ③ Slope 0.36 | 657 | +1072 | -109 | -0.5 | -33 / -85 / +10 | -35 | 207 | worse |
| ③ Slope lookback 5 bars (15 min), slope 0.113 | 910 | +1514 | +332 | +0.9 | +185 / +113 / +34 | +22 | 141 | noise |
| ③ Slope lookback 5 bars (15 min), slope 0.125 | 846 | +1480 | +299 | +0.9 | +193 / +101 / +5 | -11 | 127 | noise |
| ③ Slope lookback 5 bars (15 min), slope 0.138 | 766 | +1564 | +382 | +1.1 | +223 / +106 / +53 | -21 | 123 | promising |
| ③ Slope lookback 10 bars (30 min), slope 0.225 | 887 | +1251 | +69 | +0.3 | +111 / -12 / -30 | -0 | 145 | noise |
| ③ Slope lookback 10 bars (30 min), slope 0.250 | 822 | +1292 | +111 | +0.5 | +103 / +18 / -10 | -5 | 122 | noise |
| ③ Slope lookback 10 bars (30 min), slope 0.275 | 743 | +1389 | +208 | +1.0 | +173 / +29 / +6 | +6 | 112 | noise |
| ③ Slope lookback 15 bars (45 min), slope 0.338 | 847 | +987 | -195 | -0.9 | -84 / -130 / +18 | -53 | 299 | worse |
| ③ Slope lookback 15 bars (45 min), slope 0.375 | 769 | +1038 | -144 | -0.6 | -62 / -85 / +3 | -26 | 247 | worse |
| ③ Slope lookback 15 bars (45 min), slope 0.413 | 717 | +1109 | -73 | -0.3 | -82 / -27 / +36 | -31 | 197 | worse |
| ② LTF pierce late window 0 | 748 | +1275 | +94 | +0.7 | +3 / +46 / +44 | +30 | 142 | noise |
| ② LTF pierce late window 2 | 814 | +1227 | +45 | +0.5 | +25 / +12 / +8 | -15 | 167 | noise |
| ② HTF pierce late window 0 | 776 | +1167 | -15 | -0.2 | -24 / +5 / +4 | +2 | 162 | worse |
| ② HTF pierce late window 2 | 809 | +1217 | +36 | +0.7 | +12 / +10 / +13 | -10 | 168 | noise |
| ② HTF late trade-colour OFF | 800 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ② HTF pierce replaces current setup | 814 | +1225 | +43 | +0.7 | +2 / -7 / +49 | +0 | 180 | noise |
| ② HTF pierce requires close beyond LTF EMA9/20 | 800 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ② Flip: require pullback first (wait 10) | 800 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ② Trigger HTF CBC Flip OFF | 760 | +1161 | -20 | -0.1 | +56 / +33 / -109 | +9 | 160 | worse |
| ② Trigger LTF EMA20 Pierce OFF | 406 | +972 | -210 | -0.6 | -160 / -3 / -47 | -150 | 100 | worse |
| ② Trigger HTF EMA9 Pierce OFF | 693 | +1108 | -74 | -0.4 | +13 / -7 / -80 | -66 | 170 | worse |
| ② Trigger HTF EMA20 Pierce OFF | 751 | +998 | -183 | -1.4 | -42 / -6 / -135 | -53 | 216 | worse |
| ① Flip distance 1.5 ATR | 797 | +1203 | +22 | +0.8 | +22 / +0 / +0 | +0 | 159 | noise |
| ① Flip distance 3 ATR | 808 | +881 | -301 | -4.1 | -282 / -11 / -8 | -7 | 178 | robustly worse |
| ① Flip side gate OFF | 803 | +1202 | +21 | +0.6 | -0 / +9 / +12 | +0 | 157 | noise |
| ① Flip side gate 2 pts | 799 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ① Flip VWAP slope OFF | 800 | +1182 | +0 | +0.0 | +0 / +0 / +0 | +0 | 166 | noise |
| ① HTF pierce min ER 0 | 943 | +1316 | +135 | +0.5 | +20 / +70 / +45 | -4 | 182 | noise |
| ① HTF pierce min ER 0.23 | 751 | +994 | -188 | -1.4 | -124 / -8 / -56 | +0 | 168 | worse |
| ① LTF pierce min ER 0.12 | 742 | +1139 | -43 | -0.3 | -42 / -9 / +8 | -3 | 193 | worse |
| ① LTF pierce min ER 0.15 | 696 | +1134 | -47 | -0.2 | -36 / -46 / +35 | +22 | 216 | worse |
| ① LTF pierce min ER 0.23 | 592 | +831 | -351 | -1.3 | -249 / -66 / -35 | -66 | 245 | worse |
| ① VWAP reclaim block OFF | 854 | +1273 | +92 | +0.7 | +34 / +69 / -12 | -0 | 161 | noise |
| ① VWAP reclaim block 8 | 793 | +1159 | -22 | -0.4 | -29 / +10 / -3 | +0 | 159 | worse |
| ① Min candles between setups 5 | 819 | +1230 | +48 | +0.7 | -6 / +15 / +39 | +0 | 172 | noise |
| ① Min candles 15 | 790 | +1111 | -70 | -1.1 | -61 / +0 / -10 | +0 | 172 | worse |
| ① ATR length 10 | 791 | +1168 | -13 | -0.1 | +10 / +29 / -52 | -67 | 140 | worse |
| ① ATR length 20 | 796 | +1080 | -101 | -0.6 | -46 / -22 / -34 | +2 | 195 | worse |
| ① No new setups 16:00-19:00 | 785 | +1233 | +51 | +0.6 | +28 / +16 / +7 | +2 | 162 | noise |
| ① No-new-setup window OFF | 876 | +1150 | -31 | -0.2 | +22 / -13 / -41 | -9 | 193 | worse |
| ① OR forming blocks all OFF | 875 | +1170 | -11 | -0.1 | -79 / +54 / +14 | +40 | 214 | worse |
| ① End setups at 16:00 OFF | 799 | +1154 | -27 | -0.4 | -7 / -7 / -13 | -4 | 171 | worse |


## MGC 3m neighbour / combination checks

| Change | Trades | Net | vs base | z | Change by third | Last 4 wk | Max DD | Verdict |
|---|---|---|---|---|---|---|---|---|
| Lookback 5 bars 0.18 | 539 | +1746 | +564 | +1.6 | +280 / +189 / +96 | -43 | 99 | promising |
| Lookback 5 bars 0.20 | 456 | +1536 | +354 | +1.0 | +279 / +171 / -96 | -165 | 79 | noise |
| Lookback 5 bars 0.22 | 391 | +1513 | +332 | +0.9 | +278 / +140 / -86 | -164 | 67 | noise |
| Range gate 3 ATR | 883 | +1442 | +260 | +1.3 | +104 / +125 / +31 | -24 | 138 | promising |
| Range gate 4.5 ATR | 821 | +1243 | +61 | +0.6 | -17 / +100 / -21 | -7 | 176 | noise |
| Late-away 3 pts | 786 | +1289 | +107 | +1.5 | +1 / -2 / +108 | +41 | 166 | noise |
| Late-away 1.5 pts | 796 | +1232 | +50 | +1.3 | +0 / +3 / +47 | +36 | 163 | noise |
| Lookback 4 bars (12 min) 0.11 | 777 | +1470 | +288 | +0.8 | +302 / +34 / -48 | +34 | 120 | noise |
| Lookback 6 bars (18 min) 0.15 | 780 | +1514 | +332 | +1.0 | +281 / +76 / -25 | -85 | 119 | noise |
| Lookback 5 bars 0.15 | 708 | +1598 | +416 | +1.2 | +285 / +92 / +39 | -67 | 130 | promising |
| Lookback 5 bars 0.165 | 615 | +1782 | +601 | +1.8 | +361 / +160 / +79 | -51 | 114 | promising |
| Range gate OFF + lookback 5 bars 0.138 | 924 | +1743 | +562 | +1.4 | +270 / +240 / +51 | -103 | 138 | promising |
| Range gate OFF + lookback 5 bars 0.15 | 854 | +1837 | +656 | +1.6 | +345 / +234 / +77 | -92 | 144 | promising |
| Range gate OFF + late-away 2 | 870 | +1499 | +317 | +1.5 | +111 / +133 / +73 | +18 | 131 | promising |
| Lookback 5 bars 0.138 + late-away 2 | 756 | +1631 | +449 | +1.3 | +223 / +93 / +133 | +28 | 123 | promising |
| Range gate OFF + lookback 5 0.138 + late-away 2 | 912 | +1826 | +644 | +1.6 | +290 / +230 / +124 | -54 | 136 | promising |
