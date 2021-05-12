# Q. Number of Upper and Lower case alphabets in an Input String from User.

userInput = input("Enter a Name: ")
upperCaseLetters = 0
lowerCaseLetters = 0

for n in userInput:
    if n.isupper():
        upperCaseLetters += 1
    else:
        lowerCaseLetters += 1

print("Number of UpperCase Letters: ", upperCaseLetters, " and LowerCase Letters: ", lowerCaseLetters)
