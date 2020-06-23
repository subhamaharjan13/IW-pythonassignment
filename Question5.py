#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

word = "entertain"

suffix = "ing"

def replace(string):
    count = len(string)
    if count >3:
        if string.endswith(suffix):
            result = string + 'ly'
        else:
            result = string + 'ing'

    return result
        
print(replace(word))