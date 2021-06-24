# WAP to print Fibonacci series.

num1, num2 = 0, 1
total = 0

choice = int(input("Choose from below: \n1 for entering total numbers in Fibonacci series. "
                   "\n2 for entering till where you want the series to continue.\n"))

if choice == 1:
    totalNumbers = int(input("Enter Number: "))
    if totalNumbers <= 0:
        print("Please enter a value greater than 0.")
    elif totalNumbers == 1 or totalNumbers == 2:
        print("Fibonacci Series of 1 Number: 0, 1.")
    else:
        print("Fibonacci Series of ", totalNumbers, " : \n0 \n1 ")
        while totalNumbers > 2:
            total = num1 + num2
            num1 = num2
            num2 = total
            totalNumbers -= 1
            print(total)


elif choice == 2:
    totalNumbers = int(input("Enter Number: "))
    if totalNumbers <= 0:
        print("Please enter a value greater than 0.")
    elif totalNumbers == 1:
        print("Fibonacci Series of 1 Number: 0, 1.")
    else:
        print("Fibonacci Series of ", totalNumbers, " : \n0 \n1 ")
        while total < totalNumbers:
            total = num1 + num2
            num1 = num2
            num2 = total
            totalNumbers -= 1
            print(total)

else:
    print("Invalid input.")

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
