#9 Finding the smallest number such that number^2 > 12000

n = 1
test = False
while test == False:
    if n**2 > 12000:
        print(n)
        test = True
    else:
        n = n + 1
