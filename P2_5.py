# CIS40 : Summer 2020: Chapter 2.5 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.5

# P2.5: Enhance the output of P2.4 so that the numbers are properly aligned


def do_math():
    flag = True

    # input validation
    while flag:
        try:
            print()
            num1, num2 = input("Please enter 2 integers: ").split()
            num1 = int(num1)
            num2 = int(num2)
            flag = False
        except:
            print("-----Please enter 2 integers separated by a space-----")

    # computing the needed calculations
    sum_add = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    average = sum_add / 2
    distance = abs(difference)  # distance is the absolute value of the difference
    max_num = max(num1, num2)
    min_num = min(num1, num2)

    # formatting the output so that the numbers are aligned
    print("Sum:%15d" % sum_add)
    print("Difference:%8d" % difference)
    print("Product:%11d" % product)
    print("Average:%14.2f" % average)
    print("Distance:%10d" % distance)
    print("Maximum:%11d" % max_num)
    print("Minimum:%11d" % min_num)


# calling the function to solve the problem
do_math()

''' 
Output: 

Please enter 2 integers: 1 2
Sum:              3
Difference:      -1
Product:          2
Average:          1.50
Distance:         1
Maximum:          2
Minimum:          1 

-------------------------------
Please enter 2 integers: 10 40
Sum:             50
Difference:     -30
Product:        400
Average:         25.00
Distance:        30
Maximum:         40
Minimum:         10
'''
