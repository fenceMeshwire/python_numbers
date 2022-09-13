#!/usr/bin/env python3

# Python 3.9.5

# 02_math_function.py

# Dependency
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  y = x**2 - 5*x + 1
  return y

x = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7])
# Rearranging x for a smooth representation of the line 
# in order to get the impression of a continous function.
x = np.arange(-2, 7.01, 0.01, dtype=float)

y = f(x)
print(y)

plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.plot(x, y)
plt.show()
