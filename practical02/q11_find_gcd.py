#11 Computing the greatest common divisor:

number1 = int(input("Please input the first integer: "))
number2 = int(input("Please input the second integer: "))

minfactor = 1
factor = 2
              
while minfactor <= number1 and minfactor <= number2:
    if number1%minfactor == 0 and number2%minfactor == 0:
        minfactor = factor
    minfactor = minfactor + 1

print("The greatest common divisor of {0} and {1} is {2}.".format(number1, number2, factor))
