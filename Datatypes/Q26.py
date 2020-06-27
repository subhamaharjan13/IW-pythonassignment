# Write a python program to insert a given string at the beginning of all items in a list

sample_list = [1,2,3,4]

character = 'emp'

result_list = list(map(lambda x: character + str(x) , sample_list)) 
print(result_list)