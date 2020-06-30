#Write a Python function to insert a string in the middle of a string.

def insert_sting_middle(string, word):
    return string[0:2] + word + string[2:]

print(insert_sting_middle('[[]]<<>>', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))