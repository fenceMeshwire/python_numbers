#!/usr/bin/env python3

# Python 3.9.5

# Dependencies
import pandas as pd
import matplotlib.pyplot as plt

hours = [h for h in range(24)]
minutes = [m for m in range(60)]
results:dict = {}
upper:dict = {}
lower:dict = {}
lower_rate = 0
upper_rate = 0

for hour in hours:
    for minute in minutes:
        if minute != 0:

            if hour < 10 and minute < 10:
                key = "0" + str(hour) + ":0" + str(minute)

            if hour < 10 and minute >= 10:
                key = "0" + str(hour) + ":" + str(minute)

            if hour >= 10 and minute >= 10:
                key = str(hour) + ":" + str(minute)

            if hour >= 10 and minute < 10:
                key = str(hour) + ":0" + str(minute)

            value = hour / minute
            lower_rate += 0.0002872711 # Growth rate for lowest values
            upper_rate += 0.016949     # Upper value growth rate per minute += 1/59

            results[key] = round(value, 3)
            lower[key] = lower_rate
            upper[key] = upper_rate

result = pd.Series(results)
lower = pd.Series(lower)
upper = pd.Series(upper)

result.plot()
lower.plot(linestyle='dotted')
upper.plot(linestyle='dotted')

plt.xlabel('Stunde:Minute')
plt.ylabel('Ergebnis')
plt.show()

# Write the output to a TXT file alternatively:
import os

path = '/Users/user'
os.chdir(path)

# Output:
with open('hour_by_minute.txt', 'wt', encoding='utf-8') as fout:
    for key in results:
        line = str(key) + " = "  + str(results[key]) + "\n"
        fout.write(line)
