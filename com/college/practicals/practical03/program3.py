# Q. Calculate Surface Area and Volume of a cylinder.

PI = 3.14

radius = float(input("Please Enter the Radius of a Cylinder: "))
height = float(input("Please Enter the Height of a Cylinder: "))

surfaceArea = 2 * PI * radius * (radius + height)
volume = PI * radius * radius * height

print("The Surface Area of a Cylinder = ", surfaceArea)
print("The Volume of a Cylinder = ", volume)
