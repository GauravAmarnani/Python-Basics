# WAP to add values of common keys in 2 dictionaries.

dictName1 = {1: 100, 2: 200, 3: 300}
dictName2 = {1: 200, 2: 300, 4: 800}
dictName3 = {}

for i in dictName1.keys():
    if i in dictName2.keys():
        dictName3[i] = (dictName1.get(i) + dictName2.get(i))

print("Dictionary 1: ", dictName1, " and Dictionary 2: ", dictName2)
print("After adding values of common keys: ", dictName3)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
