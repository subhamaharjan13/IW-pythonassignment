# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

num = int(input("Enter a number:"))

def mul(number):
    multiple = number * num
    return multiple

print(mul(5))