# Write an if statement to determine whether a variable holding a year is a leap year.

year = 2020

# check whether the variable year is leap year or not
if (year % 4) == 0:
    if (year % 100 ) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))