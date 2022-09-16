#!/usr/bin/env python3

# Python 3.9.5

# 03_sigmoid_function.py

import math
import numpy as np
import matplotlib.pyplot as plt

# =============================================================
# Sigmoid function
def f(x):
    return  1 / (1 + math.exp(-x))

# Rearranging x for a smooth representation of the line 
# in order to get the impression of a continous function.
x = np.arange(-7, 7, 0.01, dtype=float)

y = [f(x) for x in x]
a = np.array([0.5 for _ in range(len(x))])

plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.plot(x, y)
plt.plot(x, a)
plt.show()
