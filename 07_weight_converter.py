#!/usr/bin/env python3

# Python 3.9.5

# 07_weight_converter.py

# Purpose: Convert metric to imperial weight and vice versa

class Weight:
    def __init__(self, weight):
        self.weight = weight

    def convert_kg_to_lbs(self):
        return self.weight * 2.2046226

    def convert_lbs_to_kg(self):
        return self.weight / 2.2046226

weight = 100
oWeight = Weight(weight)

oWeight.convert_kg_to_lbs() # Convert kg to lbs
oWeight.convert_lbs_to_kg() # Convert lbs to kg
