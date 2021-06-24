# Q. Find Factorial of a Number using Function.

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)


userInput = int(input("Enter a Number: "))

if userInput < 0:
    print("Negative Numbers Not Allowed.")
elif userInput == 0:
    print("Factorial is 1")
else:
    print("Factorial is ", factorial(userInput))
