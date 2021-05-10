""" String Methods:
1. capitalize(): Upper Cases first character.
2. count(character, sIndex, eIndex): Total Count of character within specified length.
3. center(number, character): Weird method.
4. endswith(character, sIndex, eIndex): Easy dubs.
5. find(character, sIndex, eIndex): If Character found then will return first occurrence of it.
                                    If not found then will return -1.
6. index(character, sIndex, eIndex): If Character found then will return first occurrence of it.
                                     If not found then will raise error.
7. isalpha(): Will return true if only the alphabets are present (a-z/ A-Z) inside the string.
              Will return false if anything other than an alphabet is present inside the string.
8. isdecimal(): Same to same but with only numbers (0-9).
9. isdigit(): Same to same but with any digit (!@#$%^&*()).
10. islower(): Returns true if all the alphabets are in lower case and false even if one character
               is in upper case.
11. isupper(): Returns true if all the alphabets are in upper case and false even if one character
               is in lower case.
12. isspace(): Returns true if only white spaces are present in the string.
13. len(): Easy dubs again.
14. replace(oldCharacter, newCharacter, numberOfTimes): Replaces newCharacter with oldCharacter for
                                                        numberOfTime times.
15. lower(): To Lower Case.
16. upper(): To Upper Case.
17. lstrip(): Removes white space from start.
18. rstrip(): Removes white space from end.
19. strip(): Removes white space from start and end. (Not from between).
20. min(): Returns minimum alphabetical character.
21. max(): Returns maximum alphabetical character.
22. split(): Will split all the characters into a LIST on the basis of white spaces.
23. title(): Will Upper Case the first character of all the words on the basis of white spaces.
             (If number is present on first index of a word then it will capitalize the first string
             occurrence after that).
24. zfill(size): Will fill the string with zero's (0) in the start to fulfill the size provided.
"""

string = "gaurav"
print(string)
print(string.capitalize())

print(string.count("a"))

print(string.center(20, "*"))

print("Does Gaurav Ends With 'a'? - ", string.endswith("a"))
print("Does Gaurav Ends With 'v'? - ", string.endswith("v"))

print("First Occurrence of a in Gaurav is at Index: ", string.find("a"))

print("Does string contain only alphabets? - ", string.isalpha())

decimalString = "12345"
print("Does decimalString contain only Decimal Numbers (All)? - ", decimalString.isdecimal())
print("Does decimalString contain only Digits (0-9)? - ", decimalString.isdigit())

digitString = "124*%$^#"
print("Does digitString contain only Digits (0-9)? - ", digitString.isdigit())

lowerString = "gaurav"
upperString = "GAURAV"
print("Does lowerString contains only lower case alphabets? - ", lowerString.islower())
print("Does upperString contains only upper case alphabets? - ", lowerString.isupper())

spaceString = "       "
notSoScapeString = "    v    "

print("Does spaceString ONLY have space? - ", spaceString.isspace())
print("Does notSoSpaceString ONLY have space? - ", notSoScapeString.isspace())

replaceString = "one one one one"
print("Replace 'one' with 'two' for 1 time: ", replaceString.replace("one", "two", 1))
print("Replace 'one' with 'two' for 2 time: ", replaceString.replace("one", "two", 2))
print("Replace 'one' with 'two' for 3 time: ", replaceString.replace("one", "two", 3))

lowerToUpperString = "gaurav"
upperToLowerString = "GAURAV"
print(lowerToUpperString, " to Upper Case is : ", lowerToUpperString.upper())
print(upperToLowerString, " to Lower Case is : ", upperToLowerString.lower())

startSpaceString = "   My Name is Gaurav."
print("After removing spaces from start: ", startSpaceString.lstrip())

endSpaceString = "My Name is Gaurav.     "
print("After removing spaces from end: ", endSpaceString.rstrip())

removeSpaceString = "   My   Name    is    Gaurav.    "
print("After removing all spaces: ", removeSpaceString.strip())

alphabetString = "abcdefghijklmnopqrstuvwxyz"
print("Smallest Alphabet in alphabetString is ", min(alphabetString))
print("Largest Alphabet in alphabetString is ", max(alphabetString))

splitString = "My Name Is Gaurav Amarnani"
listOfSplitString = splitString.split()
print(listOfSplitString)

titleString = "my undercover name is '6g 9a'."
print("Upper Casing first alphabet of each word: ", titleString.title())

zFillString = "Gaurav"
print("Filling zFillString with 4 Zero's (0): ", zFillString.zfill(10))
