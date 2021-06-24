# WAP to get sum of digits of a given number.

number = int(input("Enter the number: "))
sum = 0
temp = number

while temp > 0:
    rem = temp % 10
    temp = int(temp / 10)
    sum += rem

print("The Sum of Number ", number, " is ", sum)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
