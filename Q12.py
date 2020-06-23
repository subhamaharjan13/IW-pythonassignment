# Write a Python script that takes input from the user and displays that input back in upper and lower cases.

text = input("Enter a word you would like to translate in upper/lower case:")

uppercase = text.upper()
lowercase = text.lower()

print("The word in uppercase is %s " %uppercase)
print("The word in lowercase is %s " %lowercase)