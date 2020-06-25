# Write a Python program to remove the nth index character from a nonempty string.

string = "character"

n = 1

first_part = string[:n]
last_part = string[n+1:]

removed_string = first_part + last_part

print(removed_string)