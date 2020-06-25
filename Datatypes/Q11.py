# Write a Python program to count the occurrences of each word in a given sentence.

sentence = 'Python program to count the occurrences of each word in a given sentence'
occurences = {}

for i in sentence:
    if i in occurences:
        occurences[i] +=1
    else:
        occurences[i] = 1

print("occurences of '%s' is " %sentence + str(occurences))