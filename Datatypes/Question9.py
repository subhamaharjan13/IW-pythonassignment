# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

word = 'python'

def exchange(text, first_char,last_char):
    text = list(text)
    text[first_char], text[last_char] = text[last_char], text[first_char]
    return "".join(text)

print(exchange(word,0,-1))