# Write a Python function to multiply all the numbers in a list.

sample_list = [8, 2, 3, -1, 7]

def multiply(list):
    multiple = 1
    for x in list: 
        multiple = multiple * x  
    return multiple  

print(multiply(sample_list))