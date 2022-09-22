#!/usr/bin/env python3

# Python 3.9.5

# measurement_converter.py

# Converting imperial to metric measurements and vice versa.

def convert_yard_to_meter(measurement):
    measurement = measurement * 0.9144
    return float("%.3f" % measurement)

def convert_meter_to_yard(measurement):
    measurement = measurement / 0.9144
    return float("%.3f" % measurement)

def convert_meter_to_foot_inch(dist_meter=None):
    if dist_meter == None: return
    length = dist_meter / 0.3048 # 1 foot = 0.3048 m
    foot = int(dist_meter // 0.3048)
    diff = length - foot
    inch = round(12 * diff) # 1 foot = 12 inch, 1 inch = 0.0254 m
    if inch == 12: 
        foot += 1
        inch = 0
    return (foot, inch)

def convert_foot_inch_to_meter(measurement):
    # 1 foot = 0.3048 m, 1 inch = 0.0254 m
    if measurement[1] > 11:
        print('Check input value, max. 11" allowed.')
        return
    dist_meter = measurement[0] * 0.3048 + measurement[1] * 0.0254
    return dist_meter

if __name__ == '__main__':
    # Convert foot, inch to meter and vice versa
    dist_meter = convert_foot_inch_to_meter((5, 9)) # measurement = (5, 9) # foot, inch
    print('Result in meters', dist_meter, 'm')
    # Convert meter to foot, inch
    dist_imperial = convert_meter_to_foot_inch(dist_meter) 
    print('Result in foot, inch: ' + str(dist_imperial[0]) + "'" + str(dist_imperial[1]) + '"')
    # Proof of concept
    print(dist_meter == convert_foot_inch_to_meter(dist_imperial)) 

    # Convert meter to yard and vice versa:
    dist_meter = convert_yard_to_meter(100)
    print('Result in meters:', dist_meter, 'm')
    dist_imperial = convert_meter_to_yard(dist_meter)
    print('Result in yards:', dist_imperial, 'yd')
    # Proof of concept
    print(dist_imperial == convert_meter_to_yard(dist_meter))
