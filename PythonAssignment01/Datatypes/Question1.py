# 1. Write a Python program to count the number of characters
# (character frequency) in a string
# String: google.com

word = 'google.com'
char_frequency = {}

for i in word:
    if i in char_frequency:
        char_frequency[i] +=1
    else:
        char_frequency[i] = 1

print("Character frequency of '%s' is " %word + str(char_frequency))