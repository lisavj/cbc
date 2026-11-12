# MES 3m close-at-TP1 % by time of day (CBC v10.56 box) -- 11/03/2026

Stop 3.0 ATR (min 5), TP1 1.75 ATR, no caps; windows by setup candle open time (ET) 06:00-16:00 and 18:00-22:30 = 80 %, else 100 %. Replay of real MES 3m setups (BarFeed bars, mes_sltp_grid.load).

```
MES 3m: 102 setups (10/19-11/03), 76 inside 06-16/18-22:30, 26 outside
variant (stop 3.0 / TP1 1.75 ATR, min 5)          | net | halves | thirds | | since 10/27
100% all day                                          +139.2 |  +57.3 /  +81.9 |  +26.3  +32.9  +79.9 | ✱T |  +88.1
80% all day, trail 1.7 + BE                           +146.4 |  +40.8 / +105.7 |  +14.6  +29.8 +102.0 | ✱T | +112.8
80% all day, trail 1.7 no BE                          +140.5 |  +39.0 / +101.6 |  +13.2  +28.5  +98.8 | ✱T | +108.7
80% all day, trail 1.3 + BE                           +149.1 |  +46.8 / +102.4 |  +18.4  +33.5  +97.3 | ✱T | +109.3
TIME MIX (box): 80% in windows (tr1.7+BE), else 100%  +153.7 |  +43.3 / +110.5 |  +16.7  +32.6 +104.5 | ✱T | +117.6
time mix, 80% trail 1.3 + BE                          +153.3 |  +48.0 / +105.2 |  +19.5  +35.4  +98.3 | ✱T | +112.2
reverse mix: 100% in windows, 80% outside             +131.8 |  +54.8 /  +77.0 |  +24.2  +30.1  +77.4 | ✱T |  +83.3

inside windows   n=76  100%: +109.6   80% tr1.7+BE: +124.2   80% tr1.3+BE: +123.7
outside windows  n=26  100%:  +29.6   80% tr1.7+BE:  +22.2   80% tr1.3+BE:  +25.4
00-06     n=26  100%:  +29.6  80%:  +22.2  diff  -7.3
06-09:30  n=18  100%:  -38.8  80%:  -42.1  diff  -3.2
09:30-12  n=12  100%:  +45.7  80%:  +52.9  diff  +7.2
12-16     n=28  100%:  +71.0  80%:  +80.6  diff  +9.7
18-22:30  n=18  100%:  +31.7  80%:  +32.7  diff  +1.0
```

Takeaway: time mix +153.7 vs 100 % all day +139.2 (+14.5); gain comes from 09:30-16:00 (+16.9); 06:00-09:30 80 % slightly worse (-3.2), 00:00-06:00 100 % better (+7.3). First half favours 100 % (+57.3 vs +43.3), second half the mix (+110.5 vs +81.9). Small sample -- re-check at 150+ setups.
