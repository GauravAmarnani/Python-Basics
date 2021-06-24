# WAP to implement Multiple Inheritance.

class A:
    def timepassFunction(self):
        print("These are examples of Multiple Inheritance.")


class B(A):
    def __init__(self):
        super().timepassFunction()


class C(A):
    def __init__(self):
        super().timepassFunction()


b = B()
c = C()

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
