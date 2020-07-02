# Create a list of tuples of first name, last name, and age for your friends and colleagues. 
# If you don't know the age, put in None. Calculate the average age, skipping over any None values. 
# Print out each name, followed by old or young if they are above or below the average age.

personalInfo = [('subha','maharjan',22),('ram','tuladhar',None),
                    ('hari','shrestha',18),('rohan','shakya',None)]

personalInfoWithoutNone = [i for i in personalInfo if i[2] != None]

age_list = [i[2] for i in personalInfoWithoutNone if i[2]] 
# age_list = [i[2] for i in personalInfo if i[2] is not None]                       #this can be done as well

averageAge = sum(age_list)/len(age_list)

for i in personalInfoWithoutNone:
    if i[2] > averageAge:
        print("Older:",i)
    else:
        print("Younger",i)
