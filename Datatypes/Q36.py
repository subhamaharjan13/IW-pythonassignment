# Write a Python program to sum all the items in a dictionary.

item = {'a': 20, 'b': 30, 'c':70}

sum = 0
for i in item.values():
    sum = sum + i

print(sum)