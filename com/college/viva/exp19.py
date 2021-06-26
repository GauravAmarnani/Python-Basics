# WAP to perform following operations on Set: Intersection(&), Symmetric Difference(^)
# and Difference Update(Can't find it.).

setName1 = {1, 2, 3, 4, 5}
setName2 = {4, 5, 6, 7, 8}
print("Intersection of set ", setName1, " and ", setName2, " is:\n", setName1.intersection(setName2))
print("\nSymmetric Difference of set", setName1, " and ", setName2, " is:\n", setName1.symmetric_difference(setName2))
setName1.difference_update(setName2)
print("\nAfter Difference Updated set:\n", setName1)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
