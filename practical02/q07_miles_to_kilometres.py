#7 Converting Miles to Kilometres and back again:

print("Miles",">", "Kilometres", "|", "Kilometres", ">", "Miles")

miles = 1
kilometres = 20

while miles <= 10 and kilometres <= 65:
    print("{0:7s} {1:<12.3f} {2:12s} {3:<6.3f}".format(str(miles), float(miles*1.609), str(kilometres), float(kilometres/1.609)))   
    miles = miles + 1
    kilometres = kilometres + 5
