#!/usr/bin/env python3

# Python 3.9.5

# weight_converter.py

# Purpose: Convert metric to imperial weight and vice versa

class Weight:
    def __init__(self, weight):
        self.weight = weight

    def convert_kg_to_lbs(self):
        return self.weight * 2.2046226

    def convert_lbs_to_kg(self):
        return self.weight / 2.2046226
    
    def convert_lbs_to_oz(self):
        return self.weight * 16

    def convert_oz_to_lbs(self):
        return self.weight / 16

    def convert_oz_to_gramm(self):
        return self.weight * 28.3495

    def convert_gramm_to_oz(self):
        return self.weight / 28.3495

weight = 1
oWeight = Weight(weight)

oWeight.convert_kg_to_lbs() # Convert kg to lbs
oWeight.convert_lbs_to_kg() # Convert lbs to kg

oWeight.convert_lbs_to_oz() # Convert lbs to oz
oWeight.convert_oz_to_lbs() # Convert oz to lbs

oWeight.convert_oz_to_gramm() # Convert oz to gramm
oWeight.convert_gramm_to_oz() # Convert gramm to oz
