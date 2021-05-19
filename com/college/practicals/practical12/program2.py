# Q. Finding Area and Circumference of a Circle using Python Inbuilt Math Module.

import math

radius = float(input("Enter Radius of Circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('Area = ', area, " and Circumference = ", circumference)
