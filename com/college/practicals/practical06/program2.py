# Q. Multiplication of all the items in a List.

list1 = []
numberOfItems = int(input("Enter Number of Items you want to add : "))
multiplication = 1


while numberOfItems > 0:
    listItem = int(input("Item : "))
    list1.append(listItem)
    numberOfItems -= 1

for i in list1:
    multiplication *= i

print("Multiplication : ", multiplication)
