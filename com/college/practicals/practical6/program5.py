# Q. Reverse List.

list1 = []
numberOfItems = int(input("Enter Number of Items you want to add : "))

while numberOfItems > 0:
    listItem = int(input("Item : "))
    list1.append(listItem)
    numberOfItems -= 1

list1.reverse()
print("Reversed : ", list1)
