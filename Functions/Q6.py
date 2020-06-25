# Write a Python function to check whether a number is in a given range.

def number(n):
    if n in range(0,10):
        print("%s exists in the range" %str(n))
    else:
        print("%s doesn't exist in the range" %str(n))


number(8)