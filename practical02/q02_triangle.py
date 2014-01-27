#2 Validating triangles and computing perimeter:

side1 = float(input("Please input the length of the first side of the shape you wish to ascertain as a triangle(units): "))
side2 = float(input("Please input the length of the second side of the shape you wish to ascertain as a triangle(units): "))
side3 = float(input("Please input the length of the third side of the shape you wish to ascertain as a triangle(units): "))
perimeter = side1 + side2 + side3

if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("Your shape is a triangle with an external perimeter of {0:.2f}.".format(perimeter))
else:
    print("Your shape is not a valid triangle.")
