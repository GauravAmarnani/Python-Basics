""" Q. Concatenate the following Dictionaries:
        a. dic1 = {1: 10, 2: 20}
        b. dic2 = {3: 30, 4: 40}
        c. dic3 = {5: 50, 6: 60}
"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)
