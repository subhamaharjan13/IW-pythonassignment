# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

nameList = ["Joey","Chandler","Paul","Monica","Ross","Phoebe","Rachel"]

for x in range(len(nameList)):
    if "john" in nameList[x].lower():
        print("John exists")
        break
    elif "john" not in nameList[x].lower() and x == len(nameList) - 1:
        print("Not found")
