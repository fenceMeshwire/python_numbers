#!/usr/bin/env python3

# Python 3.9.5

# 02_math_functions.py

# Dependency
import numpy as np
import matplotlib.pyplot as plt

# =============================================================
# Parabolic function
def f(x):
  y = x**2 - 5*x + 1
  return y

x = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7])
# Rearranging x for a smooth representation of the line 
# in order to get the impression of a continous function.
x = np.arange(-2, 7.01, 0.01, dtype=float)

y = f(x)

plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.plot(x, f(x))
plt.show()

# =============================================================
# Root function
x = np.arange(0, 7.01, 0.01, dtype=float)
def g(x):
  return np.sqrt(x)

y = g(x)

plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.plot(x, g(x))
plt.show()

# =============================================================
# Sine function
x = np.arange(-4, 4.01, 0.01, dtype=float)
def h(x):
  return np.sin(x)

y = h(x)

plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.plot(x, h(x))
plt.show()
