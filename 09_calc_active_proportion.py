#!/usr/bin/env python3

# Python 3.9.5

# 09_calc_active_proportion.py

# Dependency
from pint import UnitRegistry

units = UnitRegistry()
liter = units.liter


def active_proportion(a, b, c, d):
    return d * c * (b / (a + b))

if __name__ == '__main__':

    a = 2 * liter       # Composite A
    b = 1 * liter       # Composite B
    c = 0.125 * liter   # Portion of Composite A and B
    d = 0.12            # Active agent in b

    result = active_proportion(a, b, c, d)
    print(round(result, 6)) # 0.005 liter equals 5 ml
