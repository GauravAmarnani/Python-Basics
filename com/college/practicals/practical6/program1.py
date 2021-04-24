# Q. Sum of all the items in a List.

list1 = []
numberOfItems = int(input("Enter Number of Items you want to add : "))
addition = 0


while numberOfItems > 0:
    listItem = int(input("Item : "))
    list1.append(listItem)
    numberOfItems -= 1

for i in list1:
    addition += i

print("Addition : ", addition)
