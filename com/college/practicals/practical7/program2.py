# Repeated Elements from Tuple.

tuple1 = (1, 2, 3, 4, 5, 1, 4, 7, 8)

for i in tuple1:
    if tuple1.count(i) > 1:
        print(i, " is repeated.")
