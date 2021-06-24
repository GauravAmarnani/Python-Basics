# WAP to display Method Overriding.

class Parent:
    def __init__(self):
        self.value = "Parent's Value inside displayValue()."

    def displayValue(self):
        print(self.value)


class Child(Parent):
    def __init__(self):
        self.value = "Child's Value inside displayValue()."

    def displayValue(self):
        print(self.value)


parent = Parent()
child = Child()

parent.displayValue()
child.displayValue()

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
