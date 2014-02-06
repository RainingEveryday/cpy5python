#12 Finding the smallest factors of an integer:

number = int(input("Please input an integer that you wish to find the smallest factors for: "))
factor = 2
factors = []

while factor <= number:
    while number%factor == 0:
        number = number/factor
        factors.append(factor)
    factor = factor + 1

print(factors)
