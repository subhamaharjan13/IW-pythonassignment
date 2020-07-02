# Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list. What is the first item on the list? What is the second item on the list?

nameList = []

nameList.extend(["Ram","Sita","Gita","Hari","Krishna"])

my_iter = iter(sorted(nameList))
print("First item of list:",my_iter.__next__())
print("Second item of list:",my_iter.__next__())
