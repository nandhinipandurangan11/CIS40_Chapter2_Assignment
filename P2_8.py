# CIS40 : Summer 2020: Chapter 2.8 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.8

# P2.8: Write a program that asks the user for the lengths of the sides of the rectangle
# then print a) the area and perimeter of the rectangle
# and b) the length of the diagonal

import math

def calculate_rectangle():
    flag = True

    # input validation
    while flag:
        try:
            length, width = input("Please enter the length and the width of a rectangle: ").split()
            length = float(length)
            width =  float(width)
            flag = False
        except:
            print("\n  -----Please enter valid numeric input separated by a space-----  ")

    # calculating the area, perimeter, and the diagonal
    area = length * width
    perimeter = (length * 2) + (width * 2)
    diagonal = math.sqrt(math.pow(length,2) + math.pow(width,2))

    # printing the output:
    print("\nArea of rectangle: %.2f units^2" % area)
    print("Perimeter of the rectangle: %.2f units" % perimeter)
    print("Diagonal of the rectangle: %.2f units" % diagonal )

# calling the function to solve the problem
calculate_rectangle()

''' 
Output: 

Please enter the length and the width of a rectangle: 1 2

Area of rectangle: 2.00 units^2
Perimeter of the rectangle: 6.00 units
Diagonal of the rectangle: 2.24 units

--------------------------------------------------------------

Please enter the length and the width of a rectangle: hello

  -----Please enter valid numeric input separated by a space-----  
Please enter the length and the width of a rectangle: 200

  -----Please enter valid numeric input separated by a space-----  
Please enter the length and the width of a rectangle: 12 13

Area of rectangle: 156.00 units^2
Perimeter of the rectangle: 50.00 units
Diagonal of the rectangle: 17.69 units

'''