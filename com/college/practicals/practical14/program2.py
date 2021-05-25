"""
Q.  Write a Python program to create a class 'Degree' having a method 'getDegree' that
    prints "I got a degree". It has two subclasses namely 'Undergraduate' and
    'Postgraduate' each having a method with the same name that prints "I am an
    Undergraduate" and "I am a Postgraduate" respectively. Call the method by
    creating an object of each of the three classes.
"""


class Parent:
    def getDegree(self):
        print("I got a Degree.")


class FirstChild(Parent):
    def getDegree(self):
        print("I am Under Graduate.")


class SecondChild(Parent):
    def getDegree(self):
        print("I am Post Graduate.")


parent = Parent()
parent.getDegree()
firstChild = FirstChild()
firstChild.getDegree()
secondChild = SecondChild()
secondChild.getDegree()
