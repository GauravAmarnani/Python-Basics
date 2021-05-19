"""
Design Pattern : *
                 **
                 ***
                 ****
"""

number = int(input("Enter number of rows : "))

i, j = 0, 0

for i in range(0, number):
    print()
    for j in range(0, i+1):
        print("*", end="")
