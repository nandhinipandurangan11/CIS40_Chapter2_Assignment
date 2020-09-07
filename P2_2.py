# CIS40 : Summer 2020: Chapter 2.2 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.2

# P2.2: Write a program that computes and displays the perimeter of a letter-size
# (8.5 x 11 inch) sheet of paper and the length of its diagonal

import math


def compute_perimeter_diagonal(length, width):
    perimeter = round((2 * length) + (2 * width), 2)
    diagonal = round(math.sqrt(math.pow(length, 2) + math.pow(width, 2)), 2)

    print(
        'The perimeter and diagonal of a {0} by {1} inch paper is {2} inches and {3} inches respectively'.format(length,
                                                                                                                 width,
                                                                                                                 perimeter,
                                                                                                                 diagonal))


# calling the function to solve the problem
compute_perimeter_diagonal(8.5, 11)

''' 
Output: 

The perimeter and diagonal of a 8.5 by 11 inch paper is 39.0 inches and 13.9 inches respectively

'''
