#Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

sentence1 = 'The lyrics is not that poor!'
sentence2 = 'The lyrics is poor!'

def substring(string):
    not_index = string.find('not')
    poor_index = string.find('poor')

    if not_index >0:
        if poor_index > not_index:
            result = string.replace(string[not_index: poor_index + 4],'good')
        else:
            result = string
    else:
        result = string

    return result

print(substring(sentence1))
print(substring(sentence2))