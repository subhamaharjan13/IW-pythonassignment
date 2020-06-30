# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.

x = lambda x : x + 15

y = lambda i, j : i * j

print(x(5))
print(y(5,5))