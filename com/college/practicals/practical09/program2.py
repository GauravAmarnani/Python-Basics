# Q. Add Values of Common Keys from two Dictionaries.

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d3 = {}

for value in d1:
    if value in d2:
        d3[value] = d1[value] + d2[value]

print(d3)
