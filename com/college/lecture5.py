# Nested For Loop:

"""print("\n\n\n\nFOR NESTED LOOP :")
num = int(input("Enter Number :"))
i, j = 0, 0
for i in range(0, num):
    print()
    for j in range(0, i+1):
        print("*",end="")
"""
# Break Statement:

print("\n\n\n\nFOR BREAK STATEMENT :")
for i in range(0,10):
    print(i)
    if i == 5:
        break;

# Continue Statement:

print("\n\n\n\nFOR CONTINUE STATEMENT :")
for i in range(0,10):
    if i == 5:
        continue
    else:
        print(i)


for i in "python":
    if i == "h":
        pass
    else:
        print(i)



# Data Structures (In Detail, Chapter 3):

"""
List:   It is a collection of values or items of different types.
        [].
        Example : L1 = ["ABC", 1, True].
        Mutable.
        Indexing starts from 0.
        
Q. How to access elements of List?

A.  listName[0]. (0 being the index).
    listName[2:4]. (2 will be starting index and (4-1) will be ending index).
    listName[:4]. (When starting value is not mentioned it by default picks up 0).
    listName[2:]. (When end value is not mentioned it by defaults picks up n, n being end).
    listName[-1]. (When considering in negative numbers, it basically means -1 is the last element 
    and -2 is second last element, -3 third last element and so on.
    
Q. How to update List?

A.  listName[index] = newValue.
    listName[indexStart:indexEnd] = {newValue1, newValue2, newValueN).
    
Q. How to delete values in List?

A.  del listName[index].
    del listName.
    
"""

list1 = [0, 1, 2, 3, 4, 5, 6]
# Doubt.
print("Test : ", list1[0:4:1])
