# WAP where a function checks whether the number is prime or not.

def primeOrNot(number):
    for i in range(2, number):
        if number % i == 0:
            print(number, " is not a prime number.")
            print("It is divisible by ", i)
            break
        else:
            print(number, " is a prime number.")
            break


userInput = int(input("Enter a Number: "))
if userInput < 1:
    print("Negative Numbers can not be Prime.")
else:
    primeOrNot(userInput)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
