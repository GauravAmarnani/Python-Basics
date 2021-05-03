# Find Factorial of a given Number.

number = int(input("Enter Number : "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(factorial)
