# Write a python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

first_string = 'abc'
second_string = 'xyz'

char1 = first_string.replace(first_string[0:2],second_string[0:2])
char2 = second_string.replace(second_string[0:2],first_string[0:2])

print("final string:", char1 + " " + char2)