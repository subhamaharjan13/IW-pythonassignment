# Write a python program to insert a given string at the beginning of all items in a list

sample_list = [1,2,3,4]

character = 'emp'

result_list = []

for i in sample_list:
    i = character + str(i)
    result_list.append(i)

print(result_list)