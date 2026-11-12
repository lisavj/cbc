Time + progress profit lock -- MES 3m and MGC 3m -- 11/08/2026.
Rule (before TP1): from the first candle close at least T min after entry, once the best price since entry has reached R x TP1 distance,
move SL1 to Entry + L (locked profit). L = fixed share of the TP1 distance, or 'mv' = 25 % of the best move so far (re-checked each candle,
the stop only ratchets up). If the close is already past the new stop, exit at that close. After TP1 the normal BE / trail take over
(the lock stays if it is higher). User example: T 8 min (= 9 min on 3m), R 30 %, L 25 % of TP1.
Exits: MES 3m live (SL1 3 ATR, TP1 1.75 ATR, 80/100 % by time of day); MES 3m BOT (100 % at TP1, v10.87 windows + short filter);
MGC 3m live since v10.84 (50 % at TP1, trail 3.5). Net after costs (MES 0.50 / MGC 0.22 per trade, rule exits are stop orders = no extra).

## MES 3m (chart exits) — current: 1700 trades, net -831 after costs (thirds -23 / -714 / -94, last 4 wk +176)

**Your example (after 8 min = 9 min on 3m, at 30 % of TP1, lock 25 % of TP1):** Δ -46 (thirds -38 / +113 / -121, last 4 wk -186, 970 lock exits) 

| Time | Reach | lock 10 % of TP1 | lock 15 % of TP1 | lock 25 % of TP1 | lock 25 % of the move |
|---|---|---|---|---|---|
| 6 min | 20 % | +22 | -53 | -63 | -57 |
| 6 min | 30 % | -47 | -136 | -98 | -118 |
| 6 min | 40 % | -11 | -73 | +3 | -61 |
| 6 min | 50 % | +27 | -53 | -10 | -48 |
| 9 min | 20 % | +92 | +30 | +2 | +48 |
| 9 min | 30 % | -9 | -76 | -46 | -53 |
| 9 min | 40 % | +13 | -24 | +28 | -13 |
| 9 min | 50 % | +12 | -59 | -16 | -43 |
| 12 min | 20 % | +6 | -33 | +15 | -16 |
| 12 min | 30 % | -22 | -77 | -2 | -48 |
| 12 min | 40 % | -13 | -35 | +31 | -28 |
| 12 min | 50 % | +20 | -33 | -0 | -20 |
| 15 min | 20 % | -27 | -59 | -11 | -26 |
| 15 min | 30 % | -85 | -126 | -62 | -91 |
| 15 min | 40 % | -45 | -64 | -9 | -43 |
| 15 min | 50 % | -9 | -63 | -31 | -39 |

Better in all three thirds: 0 of 64. Top 3: none
Walk-forward: picked on thirds 1-2 = 12 min / 40 % / 25 % of TP1 -> third 3 Δ -122 (rank 46 of 64).

## MES 3m BOT (100 % at TP1, bot windows + short filter) — current: 902 trades, net -189 after costs (thirds +77 / -293 / +27, last 4 wk +172)

**Your example (after 8 min = 9 min on 3m, at 30 % of TP1, lock 25 % of TP1):** Δ -159 (thirds -71 / +10 / -99, last 4 wk -127, 480 lock exits) 

| Time | Reach | lock 10 % of TP1 | lock 15 % of TP1 | lock 25 % of TP1 | lock 25 % of the move |
|---|---|---|---|---|---|
| 6 min | 20 % | -131 | -229 | -249 | -243 |
| 6 min | 30 % | -132 | -225 | -218 | -239 |
| 6 min | 40 % | -96 | -182 | -145 | -178 |
| 6 min | 50 % | -75 | -148 | -142 | -169 |
| 9 min | 20 % | -68 | -143 | -189 | -135 |
| 9 min | 30 % | -84 | -152 | -159 | -152 |
| 9 min | 40 % | -54 | -108 | -89 | -103 |
| 9 min | 50 % | -79 | -129 | -126 | -144 |
| 12 min | 20 % | -81 | -123 | -126 | -129 |
| 12 min | 30 % | -86 | -130 | -117 | -139 |
| 12 min | 40 % | -78 | -108 | -92 | -115 |
| 12 min | 50 % | -76 | -104 | -119 | -121 |
| 15 min | 20 % | -131 | -170 | -199 | -176 |
| 15 min | 30 % | -149 | -195 | -215 | -201 |
| 15 min | 40 % | -107 | -140 | -158 | -144 |
| 15 min | 50 % | -108 | -141 | -166 | -156 |

Better in all three thirds: 0 of 64. Top 3: none
Walk-forward: picked on thirds 1-2 = 6 min / 50 % / 25 % of TP1 -> third 3 Δ -138 (rank 63 of 64).

## MGC 3m (live 50 % / trail 3.5) — current: 1591 trades, net +133 after costs (thirds +74 / -1 / +60, last 4 wk +106)

**Your example (after 8 min = 9 min on 3m, at 30 % of TP1, lock 25 % of TP1):** Δ +20 (thirds +166 / -27 / -120, last 4 wk -76, 657 lock exits) 

| Time | Reach | lock 10 % of TP1 | lock 15 % of TP1 | lock 25 % of TP1 | lock 25 % of the move |
|---|---|---|---|---|---|
| 6 min | 20 % | -211 | -186 | -227 | -228 |
| 6 min | 30 % | -191 | -157 | -177 | -179 |
| 6 min | 40 % | -198 | -174 | -196 | -193 |
| 6 min | 50 % | -39 | -40 | -36 | -33 4 |
| 9 min | 20 % | -55 | +1 | +18 | -8 |
| 9 min | 30 % | -57 | +1 | +20 | -1 |
| 9 min | 40 % | -46 | -10 | +34 | -2 |
| 9 min | 50 % | +24 | +47 4 | +80 | +70 4 |
| 12 min | 20 % | -85 | -37 | -36 | -31 |
| 12 min | 30 % | -67 | -20 | -15 | -11 |
| 12 min | 40 % | -48 | -29 | -6 | -12 |
| 12 min | 50 % | -30 | -22 4 | -6 | +8 4 |
| 15 min | 20 % | -51 | -8 | +15 | +1 |
| 15 min | 30 % | -70 | -29 | -8 | -16 |
| 15 min | 40 % | -59 | -44 | -4 | -26 |
| 15 min | 50 % | -16 | -11 | +25 4 | +15 4 |

Better in all three thirds: 0 of 64. Top 3: none
Walk-forward: picked on thirds 1-2 = 9 min / 50 % / 25 % of TP1 -> third 3 Δ -80 (rank 22 of 64).
