# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

data = ['bc','abc','bac','aba','1211']

word_list = []
for i in data:
    if len(i)>2:
        word_list.append(i)

count = 0
for i in word_list:
    if i[0] == i[-1]:
        count = count + 1

print(count)