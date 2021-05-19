# Q. Use numpy module to generate 6 random numbers between 10 and 30.

import numpy.random as Ram

randomNumbers = Ram.randint(low=10, high=30, size=6)

print("Random Numbers: ", randomNumbers)
