"""
Default Constructor in Python: __init__(self).
Destructor in Python: __del__(self).
Parameterized Constructor in Python: __init__(self, param1, param2, .. paramN).
"""


class Student:
    def __init__(self, i):
        print("Student Object Created.")

    def __del__(self):
        print("Student Object Destroyed.")


s1 = Student(1)  # Default Constructor will be called while object creation.
s1.__init__(1)  # Calling Default Constructor manually.
s1.__del__()  # Calling Destructor manually.
print("END.")
# Destructor will be called while program ends.

"""
Inheritance in Python:
Syntax:     class A:                --> Parent.
                blah blah blah.
            
            class B(A):             --> Child.
                blah blah blah.
"""


class A:
    def show(self):
        print("Inside show method of A.")


class B(A):
    def show(self):
        print("Inside show method of B.")


b = B()
b.show()
