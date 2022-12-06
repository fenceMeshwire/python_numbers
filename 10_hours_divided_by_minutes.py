#!/usr/bin/env python3

# Python 3.9.5

# Dependencies
import pandas as pd
import matplotlib.pyplot as plt

hours = [h for h in range(24)]
minutes = [m for m in range(60)]
results:dict = {}

for hour in hours:
    for minute in minutes:
        if minute != 0: # Avoid division by Zero

            if hour < 10 and minute < 10:
                key = "0" + str(hour) + ":0" + str(minute)

            if hour < 10 and minute >= 10:
                key = "0" + str(hour) + ":" + str(minute)

            if hour >= 10 and minute >= 10:
                key = str(hour) + ":" + str(minute)

            if hour >= 10 and minute < 10:
                key = str(hour) + ":0" + str(minute)

            value = hour / minute
            results[key] = round(value, 3)

result = pd.Series(results)
result.plot()

plt.xlabel('Hour:Minute')
plt.ylabel('Result')
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
