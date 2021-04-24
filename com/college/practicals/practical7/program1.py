# Minimum and Maximum from Tuple.

list1 = []
numberOfItems = int(input("Enter Number of Items you want to add : "))

while numberOfItems > 0:
    listItem = int(input("Item : "))
    list1.append(listItem)
    numberOfItems -= 1

tuple1 = tuple(list1)

print("Maximum : ", max(tuple1))
print("Minimum : ", min(tuple1))
