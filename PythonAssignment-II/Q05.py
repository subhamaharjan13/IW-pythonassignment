# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

myName = ("Subha","Maharjan",22)
name1 = ("Ram","Tuladhar",24)
name2 = ("Hari","Shrestha",27)
name3 = ("Arjun","Tamrakar",18)

# Append the tuples to a list
people = list((myName,)+(name1,)+(name2,)+(name3,))

# Sort the list by last name field in the tuple
print("Sorted by second field, lastname:",sorted(people, key=lambda tup: tup[1]))