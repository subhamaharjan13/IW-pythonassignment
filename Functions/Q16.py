# Write a Python program to square and cube every number in a given list of integers using Lambda.

data = [5, 12, 17, 18, 24, 32]

print("square:", list(map(lambda x: x ** 2, data)))
print("cube:", list(map(lambda x: x ** 3, data)))