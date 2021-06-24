# WAP to multiply all the items in a list.

import math as m

listName1 = [1, 2, 3, 4, 5, 6]
listName2 = [1, 2, 3, 4, 5, 6]
multiplicationOfListName1 = 1

for i in listName1:
    multiplicationOfListName1 *= i

multiplicationOfListName2 = m.prod(listName2)

print("Multiplication of Elements of List ", listName1, " is ", multiplicationOfListName1)
print("Multiplication of Elements of List ", listName2, " is ", multiplicationOfListName2)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
