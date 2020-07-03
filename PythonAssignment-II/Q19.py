# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

class Parentheses:
   def is_valid(self, string):
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for symbol in string:
            if symbol in brackets:
                stack.append(symbol)
            elif len(stack) == 0 or brackets[stack.pop()] != symbol:
                return False
        return len(stack) == 0


print(Parentheses().is_valid("(){}[]"))