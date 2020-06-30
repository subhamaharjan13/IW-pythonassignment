# Write a Python program to multiplies all the items in a list.

from functools import reduce

def mul(x, y):
    return x * y

data = [2, 4, 7, 3]
print(reduce(mul, data))