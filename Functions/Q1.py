# Write a Python function to find the Max of three numbers.

def max(a,b,c):
    if a>b and a>c:
        maximum_value = a
    elif b>a and b>c:
        maximum_value = b
    else:
        maximum_value = c
    return maximum_value

print(max(5,10,3))