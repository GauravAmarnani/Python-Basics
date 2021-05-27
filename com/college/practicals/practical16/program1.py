# Q. Python program to check for ZeroDivisionError exception.

try:
    number1 = 10
    number2 = 0
    answer = number1/number2
except ZeroDivisionError:
    print("Can't divide with 0.")
else:
    print("Answer is: ", answer)
finally:
    print("Have a good day!")
