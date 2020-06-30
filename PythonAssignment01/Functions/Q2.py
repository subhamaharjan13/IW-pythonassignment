# Write a Python function to sum all the numbers in a list.

Sample_List = [8, 2, 3, 0, 7]

def sum(list, size): 
   if (size == 0): 
     return 0
   else: 
     return list[size - 1] + sum(list, size - 1)


print(sum(Sample_List,len(Sample_List)))