"""
Q.  Write a Python program to create a class to print the area of a square and a
    rectangle. The class has two methods with the same name but different number of
    parameters. The method for printing area of rectangle has two parameters which
    are length and breadth respectively while the other method for printing area of
    square has one parameter which is side of square.
"""


class A:
    def area(self, length):
        print("Area of Square is: ", length*length)

    def area(self, length, breadth=1):
        print("Area of Rectangle is: ", length*breadth)


a = A()
a.area(10)
