# Fibonacci Series.

num = int(input("How many Numbers do you want in Fibonacci Series (More than 2) : "))
x = 0
y = 1
c = 2
print("Fibonacci Series: ")
print(x)
print(y)
while c < num:
    c = x+y
    print(c)
    x = y
    y = c
    c += 1
