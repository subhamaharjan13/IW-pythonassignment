# Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.

def palindrome(string):
    string = string.lower()
    string = string.replace(" ","")
    if string == string[::-1]:
        print("The supplied word is Palindrome")
    else:
        print("The supplied word is Not Palindrome")


palindrome("stressed desserts")
palindrome("stop pots")