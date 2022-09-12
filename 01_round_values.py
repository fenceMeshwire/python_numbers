#!/usr/bin/env python3

# Python 3.9.5

# 01_round_values.py

# Rounding two decimals to one decimal after the floating point (e.g. 2.34)
values = [2.34, 2.33, 2.38, -2.35, -2.34]

for value in values:
    print(round(value, 1))
    
# The breaking point is at .5 where to round up.
round(4.4) == 4 # True
round(4.5) == 5 # False
round(4.6) == 5 # True
round(5.4) == 5 # True
round(5.6) == 6 # True
round(6.5) == 6 # True

# Alternatively, another method can be applied:
value = 1.23456
format(value, '0.2f') 
# value = '1.23' and returns as type string.
