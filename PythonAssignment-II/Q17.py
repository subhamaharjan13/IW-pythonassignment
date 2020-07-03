# Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator.
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.

num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
op = input("Enter the operator:")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == '/':
    try:
        print(num1 / num2)
    except ZeroDivisionError as e:
        print(e)
else:
    print("Invalid Operator")