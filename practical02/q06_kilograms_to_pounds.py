#6 Converting kilograms to pounds:

print("Kilograms", "Pounds")
for i in range(0, 10):
    kilograms = i + 1
    pounds = kilograms * 2.2
    spaces = " " * (8 - len(str(kilograms)))
    print("{0} {1} {2:.1f}".format(kilograms, spaces, pounds))
