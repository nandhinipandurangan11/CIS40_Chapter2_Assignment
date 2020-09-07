# CIS40 : Summer 2020: Chapter 2.6 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.6

# P2.6: Write a program that prompts the user for a measurement
# in meters and then converts it to miles, feet, and inches

# constants.py contains constant defined values
import constants


def convert():
    flag = True

    while flag:
        try:
            meters = float(input("Please enter a measurement in meters: "))
            flag = False
        except:
            print("  -----Please enter valid numeric input-----  ")

    miles = meters * constants.METERS_TO_MILES
    feet = meters * constants.METERS_TO_FEET
    inches = feet * constants.FEET_TO_INCHES

    print("\n%.2f meters is %.2f miles, %.2f feet, %.2f inches" % (meters, miles, feet, inches))

# calling the function to solve the problem
convert()

''' 
Output: 

Please enter a measurement in meters: hello
  -----Please enter valid numeric input-----  
Please enter a measurement in meters: 2323efadsjfl
  -----Please enter valid numeric input-----  
Please enter a measurement in meters: 20

20.00 meters is 0.01 miles, 65.62 feet, 787.40 inches


--------------------------------------------------
Please enter a measurement in meters: 1

1.00 meters is 0.00 miles, 3.28 feet, 39.37 inches

'''