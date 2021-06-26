# WAP to implement Multiple Inheritance.

class A:
    def __init__(self):
        print("Constructor of A.")


class B:
    def __init__(self):
        print("Constructor of B.")


class C(A, B):
    def __init__(self):
        super().__init__()


c = C()

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
