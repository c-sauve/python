#!/usr/bin/python 3
import math
# To find the circumference of a circle it is 2*pi*r
def circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return math.ceil(circumference * 100) / 100


# To find the are of a circle it is pi*r^2
def circle_area(radius):
    area = math.pi * radius ** 2
    return math.ceil(area * 100) / 100