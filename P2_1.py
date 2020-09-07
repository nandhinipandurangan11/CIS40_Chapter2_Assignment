# CIS40 : Summer 2020: Chapter 2.1 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.1

# constants.py contains constant defined values
import constants


# P2.1: Write a program that displays the dimensions of a letter size
# (8.5 x 11 inch) sheet of paper in millimeters. There are 25.4
# millimeters per inch. Use constants and comments in your program

def convert_into_millimeters(in_length, in_width):
    # calculating the unit conversion
    mm_length = round(in_length * constants.INCHES_TO_MILLIMETERS, 2)
    mm_width = round(in_width * constants.INCHES_TO_MILLIMETERS, 2)

    # printing the result
    print(
        "The dimensions in millimeters of a paper of {0} inches by {1} inches is {2} millimeters by {3} millimeters.".format(
            in_length, in_width, mm_length, mm_width))


# calling the function to solve the problem
convert_into_millimeters(8.5, 11)

''' 
Output: 

The dimensions in millimeters of a paper of 8.5 inches by 11 inches is 215.9 millimeters by 279.4 millimeters.
'''
