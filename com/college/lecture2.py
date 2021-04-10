""" Data Types in Python :
        1. Number : int, long, float, complex.
        2. String.
        3. List.
        4. Tuple.
        5. List.
        6. Dictionary.
"""


# Number Data Type :

# If we want to find out the Data Type of a variable then :

a = 10
print(type(a))

a = 10.5
print(type(a))

a = "Gaurav"
print(type(a))

# If we want to delete a variable (Like null in Java) :

del a

# If we delete a variable using 'del' and then try to print it, it will give an error
# saying that 'Variable Not Defined'.

# print(a)



# String Data Type :
string1 = "Hello"
string2 = "World "

# '+' for concatenation :
string3 = string1 + string2
print(string3)

# '*' for repetitive printing :
string4 = string3 * 4
print(string4)

print(string1 * 2 + string2 * 3)


# List Data Type : [obj1, obj2, obj3] (It is mutable).

list1 = [1, "Gaurav", True, 10.5]
print(type(list1))

list2 = [2, "Amarnani", False, 20.5]

# '+' for concatenation :
print(list1 + list2)

# '*' for repetitive printing :
print(list1 * 3)

# : for slicing :
# The following code will print the list from 1st index till the end.
print(list1[2:])

# The following code will print the list from start till 3rd index.
print("", list1[:3])


# Tuple Data Type : Almost same to List but is Immutable and has round brackets.

tuple1 = (1, 2, 3, "String", True, 10.5)
print("Type of tuple1 is : ", type(tuple1))

# TypeError: 'tuple' object does not support item assignment
# tuple1[1] = "Gaurav"


# Dictionary Data Type : Just like (java.util.Map).

map1 = {1: "Gaurav"}
map2 = {2: "Archita"}
map3 = {3: "Neha"}
map4 = {4: "Komal"}
print(map1)

list5 = [{1: "Gaurav"}, {2: "Archita"}, {3: "Neha"}, {4: "Komal"}]
print(list5)



# Type Conversion:
a = "123"
print(int(a))



# input() to take user input:
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
print("Welcome to our Python tutorial Mr. ", name, " your age after 10 years will be : ", age+10)



# Square Root:
number = int(input("Enter the Number to get it's square root : "))
print("The Square root is : ", number**(1/2))

