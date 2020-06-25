# Write a Python program to multiply all the items in a dictionary.

item = {'a': 20, 'b': 30, 'c':70}

multiple = 1
for i in item.values():
    multiple = multiple * i

print(multiple)