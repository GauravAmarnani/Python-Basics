# Q. Even Number from List.

list1 = []
numberOfItems = int(input("Enter Number of Items you want to add : "))
even = []

while numberOfItems > 0:
    listItem = int(input("Item : "))
    list1.append(listItem)
    numberOfItems -= 1

for i in list1:
    if i % 2 == 0:
        even.append(i)

print("Even Numbers : ", even)
