# Q. Python program to create user defined exception that will check whether the password is correct or not?


class PasswordDoesNotMatchError(Exception):
    pass


def checkPassword():
    myPass = "mainahibataunga"
    userPass = input("Enter Password: ")
    try:
        if myPass != userPass:
            raise PasswordDoesNotMatchError("Wrong Password.")
        print("Password is correct.")
    except PasswordDoesNotMatchError as p:
        print(p)


checkPassword()
