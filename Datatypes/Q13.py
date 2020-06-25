# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

inputvalue = input("Enter comma separated values: ")            #get value from user

split_list = inputvalue.split (",")                             # split the values and put it into list

sorted_list = sorted(set(split_list))                           # sort the list into ascending order removing duplicates

final_string = ','.join(sorted_list)                            # transform the list into comma separated strings

print(final_string)