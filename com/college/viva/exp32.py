# WAP to create a User Defined Exception to check if Password is correct or not.

class PasswordException(Exception):
    pass


try:
    userInput = input("Enter Password: ")
    if userInput == "mainahibataunga":
        print("Well Done Boi.")
    else:
        raise PasswordException("Password is incorrect.")

except PasswordException as p:
    print(p)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
