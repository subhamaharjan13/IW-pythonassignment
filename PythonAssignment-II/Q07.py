# Create a list of tuples of first name, last name, and age for your friends and colleagues. 
# If you don't know the age, put in None. Calculate the average age, skipping over any None values. 
# Print out each name, followed by old or young if they are above or below the average age.

personalInfo = [('subha','maharjan',22),('ram','tuladhar',None),
                    ('hari','shrestha',18),('rohan','shakya',None)]

# list without None values
personalInfoWithoutNone = [i for i in personalInfo if i[2] != None]

# list with only age values
age_list = [i[2] for i in personalInfoWithoutNone if i[2]] 

# calculate average of age
averageAge = sum(age_list)/len(age_list)

# print the name below and above average age
for age in personalInfoWithoutNone:
    if age[2] > averageAge:
        print("Older:",age)
    else:
        print("Younger",age)
