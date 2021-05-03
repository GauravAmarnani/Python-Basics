# Q. Perform Intersection of Set, Union of Set, Difference in Set, Symmetric Difference and
# Clear a Set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Intersection:
print("Intersection: ", set1.intersection(set2))

# Union:
print("Union: ", set1.union(set2))

# Difference:
print("Difference for Set 1 : ", set1.difference(set2))
print("Difference for Set 2 : ", set2.difference(set1))

# Symmetric Difference:
print("Symmetric Difference: ", set1.symmetric_difference(set2))

# Clear a Set:
set1.clear()
