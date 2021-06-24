# WAP to implement Single Inheritance.

class A:
    def timepassFunction(self):
        print("This is an example of Single Inheritance.")


class B(A):
    def __init__(self):
        super().timepassFunction()


b = B()

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
