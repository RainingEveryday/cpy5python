#1 Checking if a number is even:

number = int(input("Please input the integer you wish to check as to whether it is even or not: "))

if number % 2 == 0:
    print("{0} is even.".format(number))
else:
    print("{0} is odd.".format(number))
