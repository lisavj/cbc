#!/usr/bin/env python3
"""MGC 3m range gate watch -- candidate gate 4.0 ATR + zone 30 % (vs live gate 5 + zone 20 %), with neighbours.
Replay Jan 5 -> now, live MGC 3m settings (VWAP stretch 4, ER 0.23 + breakout), base exits. Needs CBC v10.52 (per-symbol zone) to apply.
Usage: python3 rgate_watch.py
"""
src = open(__file__.replace('rgate_watch.py', 'rgate4_mgc.py')).read().split("P4=dict(base,r5=4)")[0]
exec(src)
for x, z_ in ((4.0, .30), (4.0, .25), (4.0, .35), (4.0, .40), (3.5, .30), (4.5, .30), (4.0, .20), (5.0, .30)):
    row('Gate %.1f, zone %d %%%s' % (x, z_ * 100, ' (candidate)' if (x, z_) == (4.0, .30) else ''), run(dict(base, r5=x, r5z=z_)))
