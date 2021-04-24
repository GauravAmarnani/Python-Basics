# Q. Largest item in a List.

list1 = []
numberOfItems = int(input("Enter Number of Items you want to add : "))

while numberOfItems > 0:
    listItem = int(input("Item : "))
    list1.append(listItem)
    numberOfItems -= 1

print("Largest : ", max(list1))
