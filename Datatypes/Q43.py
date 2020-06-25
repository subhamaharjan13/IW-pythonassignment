# Write a Python program to remove an item from a tuple.

tuple_data = ('a','b','c','d')

tuple_to_list = list(tuple_data)

removed_data = tuple_to_list.pop(1)

result_data = tuple(tuple_to_list)

print(result_data)