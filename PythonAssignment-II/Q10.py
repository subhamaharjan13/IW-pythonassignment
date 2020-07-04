# Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case 
# (i.e.this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

import re

# convert the camel cased string to snake case
def camel_cased_to_snake(string):
    string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    return string

# convert the camel cased string to kebab string
def camel_cased_to_kebab(string):
    string = re.sub(r'(?<!^)(?=[A-Z])', '-', string).lower()
    return string

print(camel_cased_to_snake("ThisIsCamelCased"))
print(camel_cased_to_kebab("ThisIsCamelCased"))