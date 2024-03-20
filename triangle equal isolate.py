
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("It forms an equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It forms an isosceles triangle.")
    else:
        print("It forms a scalene triangle.")
else:
    print("It doesn't form a valid triangle.")
