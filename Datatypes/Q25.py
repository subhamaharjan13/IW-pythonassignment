# Write a python program to check whether all dictionaries in a list or empty or not.

data_list = [{},{},{}]

print(all( len(d) == 0 for d in data_list))
