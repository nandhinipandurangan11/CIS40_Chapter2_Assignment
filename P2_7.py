# CIS40 : Summer 2020: Chapter 2.7 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.7

# P2.7: Write a program that prompts the user for a radius and then prints
# a) the area and circumference of a circle with that radius
# b) the volume and surface area of a sphere with that radius

import math


def calculateCircle():
    flag = True

    while flag:
        try:
            radius = float(input("Please enter the radius of a circle: "))
            flag = False

        except:
            print("  -----Please enter valid numeric input-----  ")

    # calculating the area and circumference
    area = math.pi * math.pow(radius, 2)
    circumference = 2 * math.pi * radius

    # calculating the volume and surface area (volume = (4/3) * pi * r^3) (surface area = 4 * pi * r^2)
    volume = (4 / 3) * math.pi * math.pow(radius, 3)
    s_area = 4 * math.pi * math.pow(radius, 2)

    # printing the output:
    print("\nArea:%8.2f units^2 \tCircumference:%7.2f units" % (area, circumference))
    print("Volume:%6.2f units^3 \tSurface Area:%8.2f units^2 " % (volume, s_area))


# calling the function to solve the problem
calculateCircle()

''' 
Output: 

Please enter the radius of a circle: 1

Area:    3.14 units^2 	Circumference:   6.28 units
Volume:  4.19 units^3 	Surface Area:   12.57 units^2 


------------------------------------------------

Please enter the radius of a circle: hello
  -----Please enter valid numeric input-----  
Please enter the radius of a circle: 10

Area:  314.16 units^2 	Circumference:  62.83 units
Volume:4188.79 units^3 	Surface Area: 1256.64 units^2 
'''
