"""
author: Judy El Shentnawy
date: 2026-02-20
This program sorts three numbers from least to greatest using only if statements.
"""
import math

#Input 

radius = int(input("Radius:"))
length = int(input("Length:"))
width = int(input("Width:"))
side_length = int(input("Side length:"))

#Processing 
area_circle = math.pi *radius**2
per_circle = 2*math.pi*radius



area_rect = length * width
per_rect = 2*(length+width)


oct_area = 2*(1+math.sqrt(2))*side_length**2
per_oct = 8*side_length 

#Output
print(f"The circle has an area of {area_circle} and a perimeter of {per_circle}")
print(f"The rectangle has an area of {area_rect} and a perimeter of {per_rect}")
print(f"The octagon has an area of {oct_area} and a perimeter of {per_oct}")