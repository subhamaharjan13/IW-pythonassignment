# Write a Python script to merge two Python dictionaries.

dict1 = {'a':1,'b':2,'c':3}

dict2 = {'1':'a','2':'b','3':'c'}

merged_dict = {**dict1,**dict2}

print(merged_dict)