# geometry.py

import math

# Function to calculate area and perimeter of a rectangle
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function to calculate area and perimeter of a circle
def circle_area(radius):
    return math.pi * (radius ** 2)

def circle_perimeter(radius):
    return 2 * math.pi * radius

