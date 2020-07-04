# Write a function to write a CSV file. It should accept a filename and a list of tuples as parameters. 
# The tuples should have a name, address, and age. The file should create a header row followed by a row for each tuple.
# If the following list of tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv

data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

# write the list of tuples in a csv file
with open('assignment.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name','Address','Age'])
    for i in data:
        csv_writer.writerow(i)