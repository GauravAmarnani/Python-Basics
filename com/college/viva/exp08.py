# WAP to reverse a given number.

number = int(input("Enter the number: "))
rev = 0
temp = number

while temp > 0:
    rem = temp % 10
    temp = int(temp / 10)
    rev = (rev * 10) + rem

print("The reverse of number ", number, " is ", rev)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
