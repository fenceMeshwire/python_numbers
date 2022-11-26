#!/usr/bin/env python

# Python 3.9.5

# 08_unit_registry.py

# Purpose: Connect units to values and calculate with them, using UnitRegistry from the module pint.

# Dependencies:
from pint import UnitRegistry

units = UnitRegistry
meter = units.meter
foot = units.foot

distance = 20 * meter + 30 * foot
print(distance)
