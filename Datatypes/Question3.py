# Write a python program to get a string from a given string where all occurences of its first char have been changed to '$',
# except the first char itself.

string = 'restart'

result_string = string[0]+ string[1:].replace(string[0], "$")

print(result_string)