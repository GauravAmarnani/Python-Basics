"""
Q.  Python program to read and print students information using two classes using
    simple inheritance.
"""


class Parent:
    def setValue(self):
        self.name = input("Enter Name: ")
        self.rollNumber = int(input("Enter Roll Number: "))


class Child(Parent):
    def printValue(self):
        super().setValue()
        print("----------------------\nStudent Information: ")
        print("Name: ", super().name)
        print("Roll Number: ", super().rollNumber)


child = Child()
child.printValue()
