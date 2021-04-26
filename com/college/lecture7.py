"""
4. index(): Returns Index Number of element in parameters.
            list.index(element), list.index(element, sIndex), list.index(element, sIndex, eIndex).
            sIndex (startIndex) is inclusive.
            eIndex (endIndex) is exclusive.
5. pop(): Remove the element. Returns the element that got deleted.
          list.pop() => Removes last element.
          list.pop(index) => Removes index number element.
6. remove(): Removes the element passed in the argument.
             list.remove(element) => Removes the first occurance of the element found.
             Will return error if element not found.
             list.remove() is not available. Have to pass the argument.
7. reverse(): To reverse the list.
8. insert(): list.insert(index, element).
             If there is an element present at the index already then it will be pushed to index+1.
             We can also pass sequence, list.insert(index, anotherList).
             But that whole list will be added at that index number.
9. sort(): sorts by default in ascending order.
           For descending pass the argument (reverse=true).
           Eg : list.sort(reverse=True).
10. clear(): It's like truncate of Python.
             Will delete all the elements. But not the list.
11. copy(): Will copy all the elements from one list to another.
"""

list3 = [1, 2, 3, 4, 5, 2, 4, 6, 2]
print("Index : ", list3.index(2)) # -> First occurance of 2.
print("Index : ", list3.index(2, 3)) # -> First occurance of 2 from 3rd index.
# print("Index : ", list3.index(2, 6, 7)) # -> First occurance of 2 from 6th to 7th index.


print(list3)
print("Popped Element when no argument is passed : ", list3.pop())
print("Popped Element when argument is 3 : ", list3.pop(3))


print("List before removing : ", list3)
print(list3.remove(2))
print("List after removing : ", list3)


list3.reverse()
print("Reversed List : ", list3)


list4 = [1, 2, 3, 4]
list4.insert(3, "vesp")
print(list4)
list4.insert(2, ["co", "cm"])
print(list4)


list3.sort()
print("Ascending Sort : ", list3)
list3.sort(reverse=True)
print("Descending Sort : ", list3)


list3.clear()
print(list3)


list5 = list4.copy()
print(list5)




# Tuple : Immutable.

print("\n \n \n TUPLE DATA TYPE INFORMATION : \n \n \n")
tuple1 = (1, True, 1.5, "Gaurav")
print(tuple1[-4:4])

tuple2 = (10)
print("Type : ", type(tuple2))
print("Tuple : ", tuple2)

tuple3 = (10, )
print("Type : ", type(tuple3))
print("Tuple : ", tuple3)


"""
Tuple Operators:

1. Repetition.
2. Concatenation.
3. Membership.
4. Iteration.


Functions:

1. cmp(): 0 - Equal. 1 - If 1st tuple is greater. -1 - If 1st tuple is smaller.
         String > Integer > Boolean (True > False).
         Compares the first element in the tuple with other tuple's first element.
2. length(): Total number of elements present inside the tuple.
3. max(): Returns the element with the maximum length. (String > Integer/Float > Boolean).
4. min(): Returns the element with the minimum length. (String > Integer/Float > Boolean).
5. tuple(): Converts other data type into the tuple.


Methods:

1. count(): Number of times element has occur inside the list.
            tuple.count(element).
2. index(): Returns Index Number of Element in parameters.
            tuple.index(element), tuple.index(element, sIndex), tuple.index(element, sIndex, eIndex).
            sIndex (startIndex) is inclusive.
            eIndex (endIndex) is exclusive.
"""

tuple1 = (1, 2, 3, 4, 5, 6)
print("Tuple1 : ", tuple1)
tuple2 = (5, 6, 7, 8)
print("Tuple2 : ", tuple2)

print("Repetition of Tuple1 : ", tuple1*2)

print("Concatenation of Tuple1 and Tuple2 : ", tuple1 + tuple2)

print("Is 3 In Tuple1 : ", 3 in tuple1)
print("Is 10 in Tuple2: ", 10 in tuple2)

print("Iteration of Tuple1 : ")
for i in tuple1:
    print(i)


print("Length of Tuple1 : ", len(tuple1))

print("Maximum Tuple1 Element: ", max(tuple1))

print("Minimum Tuple1 Element: ", min(tuple1))



# Set Data Type: Unordered List & Unique Elements.

print("\n \n \n SET DATA TYPE INFORMATION : \n \n \n")

set1 = {10, 20, 30, 15, 15}
print("Set1 Type : ", type(set1))
print("Set1 : ", set1)

set2 = {}
print("Set2 Type : ", type(set2))
print("Set2 : ", set2)

print("Is 3 In Set1 : ", 3 in set1)
print("Is 10 in Set1: ", 10 in set1)

print("Length of Set1 : ", len(set1))


"""
Set Methods: 

1. add(element): To add a SINGLE Element.
2. update(element1,.., elementN): To add Single or MULTIPLE Elements.

"""


set1.add(40)
print("Set1 : ", set1)

set1.update([1, 2, 4])
print("Set1 : ", set1)

set1 = {}
print("Type of set1 = {} = ", type(set1))

set2 = set({})
print("Type of set2 = set({}) = ", type(set2))
