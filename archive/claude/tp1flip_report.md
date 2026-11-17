TP1 % vs HTF CBC flip exits, and combos -- MES 3m / MGC 3m -- replay Jan 5 -> now (CBC engine setups, live gates). Weekly (Sat).
CBC v10.95 inputs: "...close at TP1 (%) per symbol/timeframe" (any %) and "...trail x ATR per symbol/timeframe" (0 = FLIP: BE then HTF flip only).
Each setup keeps its live SL1 / TP1 distances (MES SL1 3 ATR min 5, TP1 1.75 ATR; MGC SL1 1.7 ATR min 5 cap 7, TP1 1.7 ATR cap 6).
A setup also always ends at 16:00 or when CBC draws the next setup. Runner = the part not closed at TP1. Exit families:
  TRAIL   x % at TP1, runner: BE + ATR trail (MES 1.7 / MGC 3.5) or the HTF CBC flip against   (= live CBC exits)
  FLIP    x % at TP1, runner: BE, then ONLY the HTF CBC flip against (no trail)
  FLIP-noBE  same without moving the stop to breakeven
  FLIP+SL  no TP at all: SL1 or the HTF CBC flip against (the bot's flip-only exit)
Net after costs (MES 0.50, MGC 0.22). z vs live = Δ / (SD x sqrt(setups changed)).

## MES 3m -- 1738 setups; live = TRAIL 100 % at TP1 (CBC v10.96 defaults: MES 3m TRAIL 100 %, MGC 3m FLIP 0 % = 0 % at TP1 + trail 0)

| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |
|---|---|---|---|---|---|---|---|---|
| TRAIL | 0 % | -1124 | -314 | -1.6 | -116 / -896 / -113 | +129 | 36 % | 1381 |
| TRAIL | 25 % | -1046 | -235 | -1.2 | -89 / -853 / -103 | +125 | 48 % | 1283 |
| TRAIL | 50 % | -967 | -157 | -0.8 | -63 / -810 / -94 | +121 | 48 % | 1213 |
| TRAIL | 75 % | -889 | -78 | -0.4 | -37 / -766 / -85 | +118 | 48 % | 1142 |
| **TRAIL (live)** | 100 % | -811 | +0 | +0.0 | -11 / -723 / -76 | +114 | 48 % | 1072 |
| FLIP | 0 % | -912 | -102 | -0.5 | -80 / -875 / +43 | +191 | 25 % | 1274 |
| FLIP | 25 % | -887 | -76 | -0.4 | -63 / -837 / +13 | +172 | 48 % | 1218 |
| FLIP | 50 % | -861 | -51 | -0.3 | -46 / -799 / -17 | +152 | 48 % | 1169 |
| FLIP | 75 % | -836 | -25 | -0.1 | -29 / -761 / -47 | +133 | 48 % | 1120 |
| FLIP-noBE | 0 % | -958 | -148 | -0.7 | -149 / -894 / +85 | +206 | 34 % | 1393 |
| FLIP-noBE | 25 % | -921 | -111 | -0.6 | -115 / -851 / +44 | +183 | 37 % | 1302 |
| FLIP-noBE | 50 % | -885 | -74 | -0.4 | -80 / -808 / +4 | +160 | 43 % | 1223 |
| FLIP-noBE | 75 % | -848 | -37 | -0.2 | -46 / -766 / -36 | +137 | 48 % | 1147 |
| FLIP+SL | - | -958 | -148 | -0.7 | -149 / -894 / +85 | +206 | 34 % | 1393 |

Largest: TRAIL 100 % = -811. Better than live in all three thirds: none

## MGC 3m -- 1142 setups; live = FLIP 0 % at TP1 (CBC v10.96 defaults: MES 3m TRAIL 100 %, MGC 3m FLIP 0 % = 0 % at TP1 + trail 0)

| Exit | Close at TP1 | Net | Δ vs live | z | Thirds | Last 4 wk | Win % | Max DD |
|---|---|---|---|---|---|---|---|---|
| TRAIL | 0 % | +600 | -42 | -0.4 | +290 / +1 / +310 | +288 | 20 % | 257 |
| TRAIL | 25 % | +449 | -192 | -0.6 | +204 / +5 / +240 | +227 | 50 % | 223 |
| TRAIL | 50 % | +299 | -343 | -1.0 | +118 / +10 / +171 | +166 | 50 % | 190 |
| TRAIL | 75 % | +148 | -494 | -1.5 | +32 / +14 / +102 | +105 | 50 % | 159 |
| TRAIL | 100 % | -2 | -644 | -1.9 | -54 / +19 / +33 | +44 | 50 % | 176 |
| **FLIP (live)** | 0 % | +642 | +0 | +0.0 | +356 / -10 / +297 | +262 | 18 % | 246 |
| FLIP | 25 % | +481 | -161 | -0.5 | +253 / -3 / +231 | +208 | 50 % | 214 |
| FLIP | 50 % | +320 | -322 | -1.0 | +151 / +4 / +165 | +153 | 50 % | 184 |
| FLIP | 75 % | +159 | -483 | -1.5 | +49 / +11 / +99 | +99 | 50 % | 157 |
| FLIP-noBE | 0 % | +409 | -233 | -0.9 | +198 / +69 / +142 | +221 | 28 % | 329 |
| FLIP-noBE | 25 % | +306 | -336 | -1.0 | +135 / +57 / +114 | +177 | 32 % | 269 |
| FLIP-noBE | 50 % | +203 | -439 | -1.4 | +72 / +44 / +87 | +133 | 37 % | 215 |
| FLIP-noBE | 75 % | +100 | -542 | -1.6 | +9 / +31 / +60 | +89 | 50 % | 169 |
| FLIP+SL | - | +409 | -233 | -0.9 | +198 / +69 / +142 | +221 | 28 % | 329 |

Largest: FLIP 0 % = +642. Better than live in all three thirds: none
