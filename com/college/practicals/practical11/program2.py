# Q. Number of Upper and Lower case alphabets in an Input String from User using Function.


def findNumberOfUpperAndLowerLetters(name):
    upperCaseLetters = 0
    lowerCaseLetters = 0
    for n in name:
        if n.isupper():
            upperCaseLetters += 1
        else:
            lowerCaseLetters += 1
    print("Number of UpperCase Letters: ", upperCaseLetters, " and LowerCase Letters: ", lowerCaseLetters)


userInput = input("Enter a Name: ")
findNumberOfUpperAndLowerLetters(userInput)
