# Write a Python program to sort a list of dictionaries using Lambda.

data = [{'a': 5, 'b': 3, 'c': 7},{'a':4,'b':2,'c':6},{'a':3,'b':7,'c':1}]

result = sorted(data, key=lambda dict: dict['b'])

print(result)