"""
OOP In Python:

Syntax to create class: class className:

Syntax to create object of class: objectName = className()
                                  objectName1, objectName2 = className()

Syntax to call variables/methods of Class through Object: objectName.variableName

self: It represents Object (classObject) inside that method.
      It means that we can access methods and variables inside method using self.

Syntax to delete attribute: del className.variableName

Overloading:    Method Overloading not possible in Python.
                If we try then the last method will be executed inside the class.
                It's just stupid, don't even try.
"""


# Creating Class:
class MyFirstPythonClass:
    rollNumber = 21
    name = "VESP"

    # Use of self inside method:
    def show(self):
        print("Inside Class Method.", self.rollNumber)


# Creating Object:
classObject = MyFirstPythonClass()

# Calling Variable of Class through Object:
print("Name: ", classObject.name)
print("Roll Number: ", classObject.rollNumber)

# Calling Method of Class through Method:
print("Method: ", classObject.show())
print("---------------------------------------")


# How to Accept and Display Variables through Methods in Class using Object:
class TestClass:

    def acceptValue(self):
        self.rollNumber = int(input("Enter Roll Number: "))
        self.name = input("Enter Name: ")

    def displayValue(self):
        print("Name: ", self.name)
        print("Roll Number: ", self.rollNumber)
        print("---------------------------------------")


testObject = TestClass()
testObject.acceptValue()
testObject.displayValue()


class AnotherTestClass:

    def acceptValue(self):
        self.rollNumber = int(input("Enter Roll Number: "))
        self.name = input("Enter Name: ")

    def parameterizedFunction(self, address):
        print("Name: ", self.name)
        print("Roll Number: ", self.rollNumber)
        print("Address: ", address)
        print("---------------------------------------")


anotherClassObject = AnotherTestClass()
anotherClassObject.acceptValue()
anotherClassObject.parameterizedFunction("Munich")
