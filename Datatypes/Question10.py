# Write a Python program to remove the characters which have odd index values of a given string.

word = "Sentimental"

result = ""
for w in range(len(word)):
    if w % 2 ==0:
        result = result + word[w]

print(result)