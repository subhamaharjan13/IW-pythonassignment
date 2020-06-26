# Write a Python program to filter a list of integers using Lambda.

data = [5, 12, 17, 18, 24, 32]

result = list(filter(lambda x:x>15, data))

print(result)
