# WAP where a function calculate Number of Lower and Upper Case letters in a String.

def calculateLowerAndUpper(stringName):
    listName = [0, 0]
    for i in stringName:
        if i.isupper():
            listName[0] += 1
        else:
            listName[1] += 1
    return listName


listName1 = calculateLowerAndUpper("Gaurav Amarnani")
print("String Value = Gaurav Amarnani.\nNumber of Lower Case ", listName1[1], " and Number of Upper Case ", listName1[0])

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
