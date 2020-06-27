# Write a Python program to count the occurrences of each word in a given sentence.

sentence = 'Write a Python program to count the occurrences of each word in a given sentence'
sentence = sentence.lower()
sentence_list = sentence.split(" ")
occurences = {}

for i in sentence_list:
    if i in occurences:
        occurences[i] +=1
    else:
        occurences[i] = 1

print("occurences of '%s' is " %sentence + str(occurences))
