# Find a package in the Python standard library for dealing with JSON. Import the library module and inspect the attributes
# of the module. Use the help function to learn more about how to use the module. Serialize a dictionary mapping 'name' to 
# your name and 'age' to your age, to a JSON string. Deserialize the JSON back into python.

import json

 # provides the detailed information on how to use the module     
print(help(json))                              

# converts the dictionary to json string
jsondata = json.dumps({'name':'Subha','age':22})

# converts the json string to python dictionary
dictdata = json.loads(jsondata)

print(type(dictdata))