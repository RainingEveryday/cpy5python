#4 Determining a leap year:

year = int(input("Please enter a year that you wish to check as a leap year or otherwise: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("The year {0} is a leap year.".format(year))
else:
    print("The year {0} is not a leap year.".format(year))
