# Write a Python program to sort a list of tuples using Lambda.

data = [(3,5),(0,6),(2,1),(1,2),(8,4)]

result = sorted(data, key=lambda tup: tup[0])

print(result)