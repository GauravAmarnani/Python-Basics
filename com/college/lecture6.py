# Continuation on Data Types in Python.

# Operators & Functions of List:

"""
Operators:

1. Repetition.
2. Concatenation.
3. Membership.
4. Iteration.

Functions:

1. cmp(): 0 - Equal. 1 - If 1st list is greater. -1 - If 1st list is smaller.
         String > Integer > Boolean (True > False).
         Compares the first element in the list with other list's first element.
2. length(): Total number of elements present inside the list.
3. max(): Returns the element with the maximum length. (String > Integer/Float > Boolean).
4. min(): Returns the element with the minimum length. (String > Integer/Float > Boolean).
5. list(): Converts other data type into the list.

Methods:

1. append(): To add another List to the end of the List.
             * Works like an array if you add (list or tuple or dictionary)
2. count(): Number of times element has occur inside the list.
            list.count(element).
3. extend(): To add another Data Type to the end of the List. But not as an array.
"""

listName = [1, 1, 1, 2, 3, 4]
print("Repetition: ", listName*2)

listName2 = [5, 6, 7, 8]
print("Concatenation: ", listName+listName2)

print("Is 3 In list : ", 3 in listName)
print("Is 10 in list: ", 10 in listName)

print("Iteration: ")
for i in listName:
    print(i)

print("Length : ", len(listName))

print("Maximum length Element: ", max(listName))

print("Minimum length Element: ", min(listName))

tupleName = (1, 2, 3, 4, 5)

print("List: ", list(tupleName))

list1 = [1, 2, 3]
list2 = (1, 2, 3)
list1.append(list2)
print(list1)

print("Number of appearance of 1: ", listName.count(1))

list1 = [1, 2, 3]
list2 = (1, 2, 3)
list1.extend(list2)
print(list1)


print(listName.pop(4))
print(listName)
