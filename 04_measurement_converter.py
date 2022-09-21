#!/usr/bin/env python3

# Python 3.9.5

# measurement_converter.py

def convert_foot_inch_to_meters(measurement):
    # 1 foot = 0.3048 m, 1 inch = 0.0254 m
    if measurement[1] > 11:
        print('Check input value, max. 11" allowed.')
        return
    meters = measurement[0] * 0.3048 + measurement[1] * 0.0254
    return meters

def convert_meters_to_foot_inch(meters=None):
    if meters == None: return
    length = meters / 0.3048 # 1 foot = 0.3048 m
    foot = int(meters // 0.3048)
    diff = length - foot
    inch = round(12 * diff) # 1 foot = 12 inch, 1 inch = 0.0254 m
    if inch == 12: 
        foot += 1
        inch = 0
    measurement = (foot, inch)
    return measurement

if __name__ == '__main__':
    measurement = (5, 9) # foot, inch
    meters = convert_foot_inch_to_meters(measurement)
    print('Result in meters', meters, 'm')
    length = convert_meters_to_foot_inch(meters)
    print('Result in foot, inch: ' + str(length[0]) + "'" + str(length[1]) + '"')
    print(measurement == length)
