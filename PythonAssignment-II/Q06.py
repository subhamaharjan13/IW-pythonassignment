# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

nameList = ["Joey","Chandler","Paul","Monica","Ross","Phoebe","Rachel","John"]

# search for name "John" in the list nameList
for name in range(len(nameList)):
    if "john" in nameList[name].lower():
        print("John exists")
        break
    elif "john" not in nameList[name].lower() and name == len(nameList) - 1:
        print("Not found")
