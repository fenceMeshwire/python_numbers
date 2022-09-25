#!/usr/bin/env python3

# Python 3.9.5

# 06_meter_converter.py

class Metric:
    def __init__(self, distance):
        self.distance = distance

    def convert_meter_decimeter(self):
        return self.distance * 10

    def convert_meter_centimeter(self):
        return self.distance * 10**2

    def convert_meter_millimeter(self):
        return self.distance * 10**3

    def convert_meter_micrometer(self):
        return self.distance * 10**6

    def convert_meter_nanometer(self):
        return self.distance * 10**9

distance = 1 # meter

oMetric = Metric(distance)
oMetric.convert_meter_decimeter()   # Decimeter
oMetric.convert_meter_centimeter()  # Centimeter
oMetric.convert_meter_millimeter()  # Millimeter
oMetric.convert_meter_micrometer()  # Micrometer
oMetric.convert_meter_nanometer()   # Nanometer
