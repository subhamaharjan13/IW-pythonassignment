# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def char(string):
    uppercase = 0
    lowercase = 0

    for i in string:
        if (i.isupper()):
            uppercase = uppercase + 1
        elif (i.islower()):
            lowercase = lowercase + 1
        else:
            pass

    return uppercase,lowercase

print(char('The quick Brow Fox'))
