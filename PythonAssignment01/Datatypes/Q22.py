# Write a python program to remove duplicates from a list.

data = ['red','blue','pink','red',2,5,7,5,2,5,7]

datawithoutduplicates = list(dict.fromkeys(data))

print(datawithoutduplicates)