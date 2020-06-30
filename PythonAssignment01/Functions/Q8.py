# Write a Python function that takes a list and returns a new list with unique elements of the first list.

sample_list = [1,2,3,3,3,3,4,5]

def unique(list):
    return set(list)

unique_list = list(unique(sample_list))
print(unique_list)