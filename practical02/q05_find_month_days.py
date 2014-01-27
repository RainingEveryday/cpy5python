#5 Finding the number of days in a month:

month = int(input("Please enter the month(numeral) that to find out how many days it contains: "))
year = int(input("Please enter the year that your desired month is in: "))

if  month == 1: 
    print("January contains 31 days in the year {0}.".format(year))
elif  month == 3: 
    print("March contains 31 days in the year {0}.".format(year))
elif  month == 5: 
    print("May contains 31 days in the year {0}.".format(year))
elif  month == 7: 
    print("July contains 31 days in the year {0}.".format(year))
elif  month == 8: 
    print("August contains 31 days in the year {0}.".format(year))
elif  month == 10: 
    print("October contains 31 days in the year {0}.".format(year))
elif  month == 12: 
    print("December contains 31 days in the year {0}.".format(year)) 
elif year % 400 == 0 and month == 2 or year % 4 == 0 and year % 100 != 0 and month == 2:
    print("February contains 29 days in the year {0}.".format(year))
elif month == 2:
    print("February contains 28 days in the year {0}.".format(year))
elif  month == 4: 
    print("April contains 30 days in the year {0}.".format(year))
elif  month == 6: 
    print("June contains 30 days in the year {0}.".format(year))
elif  month == 9: 
    print("September contains 30 days in the year {0}.".format(year))
elif  month == 11: 
    print("November contains 30 days in the year {0}.".format(year))
else:
    print("You did not enter a valid month or year.")
