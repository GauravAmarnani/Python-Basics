# WAP to check if given integer is multiple of both 5 and 7.

number = int(input("Enter Number: "))

if number % 5 == 0:
    if number % 7 == 0:
        print(number, " is a multiple of both 5 and 7.")
    else:
        print(number, " is not a multiple of 7.")
else:
    print(number, " is not the multiple of 5.")

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
