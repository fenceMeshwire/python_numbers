#!/usr/bin/env python3

# Python 3.9.5

# 05_imperial_measurement_converter.py

class Imperial:

    def __init__(self, distance):
        self.distance = distance
    
    def convert_mile_to_yard(self):
        return self.distance * 880

    def convert_mile_to_feet(self):
        return self.distance * 2640

    def convert_mile_to_inches(self):
        return self.distance * 63360

distance = 1

oImperial = Imperial(distance)
oImperial.convert_mile_to_yard()
oImperial.convert_mile_to_feet()
oImperial.convert_mile_to_inches()
