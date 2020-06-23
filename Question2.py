# Write a python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

list_of_words = ['This', 'is', 'an', 'example','to','check']

result_list = []

for word in list_of_words:
    count = len(word)
    if count < 2:
        result = "Empty String"
    elif count == 2:
        result = word + word
    else:
        result = word[0:2]+word[-2:]

    result_list.append(result)

print(result_list)