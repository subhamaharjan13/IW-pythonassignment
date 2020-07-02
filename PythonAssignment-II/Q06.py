# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

nameList = ["Joey","Chandler","Paul","Monica","Ross","Phoebe","Rachel"]

for x in range(len(nameList)):
    if "John" in nameList[x]:
        print("John exists")
    if "John" not in nameList[x] and x == len(nameList) - 1:
        print("Not found")

    

