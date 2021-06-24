# Operators and Statements:

""" Types of Operators :

1. Arithmetic Operator.
2. Assignment Operator.
3. Comparison Operator.
4. Logical Operator.
5. Bitwise Operator.
6. Membership Operator.
7. Identity Operator.

"""

# Arithmetic Operator:

a = 10
b = 2

print("Add : ", a+b)
print("Subtract : ", a-b)
print("Multiply : ", a*b)
print("Divide : ", a/b)
print("Percentage : ", a%b)
print("Exponential : ", a**b)
print("Divide Round Up (Floor) : ", a//b)


# Assignment Operator:

a += b
print("Add : ", a)

a -= b
print("Subtract : ", a)

a *= b
print("Mulitply : ", a)

a /= b
print("Divide : ", a)

a %= b
print("Percentage : ", a)

a //= b
print("Floor : ", a)


# Comparison Operator:

print("Equal to : ", a == b)
print("Not Equal to : ", a != b)
print("a greater than b : ", a < b)
print("a less than b : ", a > b)
print("a less than equal b : ", a <= b)
print("a greater than equal b : ", a >= b)


# Logical Operator :

print("Is 1 > 5 and 5 < 10 : ", 1 > 5 and 5 < 10)
print("Is 10 > 5 and 5 < 30 : ", 10 > 5 and 5 < 30)

print("Is 1 > 5 or 5 < 10 : ", 1 > 5 or 5 < 10)
print("Is 10 < 5 or 5 > 30 : ", 10 < 5 or 5 > 30)

print("Is not(1 > 5 and 5 < 10) : ", (not(1 > 5 and 5 < 10)))
print("Is not(1 > 5 or 5 < 10) : ", (not(1 > 5 or 5 < 10)))


# Bitwise Operator:

# & - Both bits have to be 1 to get 1.

# | - At least one should be 1 to get 1.

# ^ - If both are same then it is 0.

# ~ - [-(Number+1)]

# << - Number shifts to left.

# >> - Number shifts to right.


# Identity Operator: Memory Location Comparison (only works for objects like link, tuple,dictionary).

c = 10
d = 10

print("Value Equals : ", c == d)
print("Location Equals : ", c is d)
print("", c is not d)


# Membership Operator : Checking in sequence.

list1 = [1, "Gaurav", True, 10.5]
string1 = "Gaurav Amarnani."

print("IS 'Gaurav' in list1 : ", "Gaurav" in list1)
print("IS 10 in list1 : ", 10 in list1)

print("IS 'Gaurav' in string1 : ", "Gaurav" in string1)
print("IS 'ABCD' in string1 : ", "ABCD" in string1)

