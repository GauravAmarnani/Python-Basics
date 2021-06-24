"""
For removing element from Set :
1. discard(element): Does not give error even if element is not present.
2. remove(element): Gives error if the element is not present.
3. pop(): Removes the first element from the set and gives error if set is empty
          Removes the last element from the list and gives error if list is empty.
4. clear(): Removes all the elements and returns set([]).
5. del(): Deletes the set itself.
"""

set1 = {1, 2, 3, 4, 5, 6}
set1.remove(1)
set1.discard(2)
set1.pop()
print(set1)

list1 = [1]
list1.pop()

del set1


"""
Other Methods:
1. set1.union(set2): Combines both the sets.
                     Can also be done with the help of OR Operator (|).
2. set1.intersection(set2): Gives elements present in both.
                            Can also be done with help of AND Operator (&).
3. set1.difference(set2): Gives elements present only in set1 and not in set2.
                          Can also be done with help fo SUBTRACT Operator (-).
4. set1.symmetric_difference(set2): Combination of (s1 - s2) & (s2 - s1).
                                    Basically gives all the uncommon elements in both sets. (^)
"""

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
print("Set 3 : ", set3)
print("set 4 : ", set4)

print("Union with help of | : ", set3 | set4)
print("Union with help of union() : ", set3.union(set4))

print("Intersection with help of & : ", set3 & set4)
print("Intersection with help of intersection() : ", set3.intersection(set4))

print("Difference with help of - : for Set 3 ", set3 - set4)
print("Difference with help of - : for Set 4 ", set4 - set3)
print("Difference with help of difference() for Set 3 : ", set3.difference(set4))
print("Difference with help of difference() for Set 4 : ", set4.difference(set3))
