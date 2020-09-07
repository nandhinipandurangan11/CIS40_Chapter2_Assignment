# CIS40 : Summer 2020: Chapter 2.4 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.4

# P2.4: Write a program that prompts the users for two integers and then
# prints a) the sum b) the difference c) the product d) the average
# e) the distance (absolute value of the difference) f) the maximum
# g) the minimum


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

    # printing the output
    print("\tsum: {0} \n\tdifference: {1} \n\tproduct: {2}".format(sum_add, difference, product))
    print("\taverage: {0} \n\tdistance = {1} \n\tmaximum number: {2} \n\tminimum number: {3}".format(average, distance,
                                                                                                     max_num,
                                                                                                     min_num))


# calling the function to solve the problem
do_math()

'''
Output: 

Please enter 2 integers: hello world
-----Please enter 2 integers separated by a space-----

Please enter 2 integers: 1 2 
	sum: 3 
	difference: -1 
	product: 2
	average: 1.5 
	distance = 1 
	maximum number: 2 
	minimum number: 1

--------------------------------------------------------------

Please enter 2 integers: 40 25
	sum: 65 
	difference: 15 
	product: 1000
	average: 32.5 
	distance = 15 
	maximum number: 40 
	minimum number: 25


'''
