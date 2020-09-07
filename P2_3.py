# CIS40 : Summer 2020: Chapter 2.3 Exercise: Nandhini Pandurangan

# P2.3: Write a program that reads a number and displays the square, cube, and fourth power
# Use the ** operator only for the fourth power


flag = True  # counter for input validation
while flag:
    try:
        num = int(input("Please enter a number: "))
        flag = False
    except:
        print('----Please enter a valid numeric input----')

square = num * num
cube = num * num * num
fourth = square ** 2

print("The square, cube and the fourth power of the number {0} is {1}, {2}, {3} respectively".format(num, square, cube, fourth))

''' 
Output: 

Please enter a number: 2
The square, cube and the fourth power of the number 2 is 4 8 16 respectively 

Please enter a number: hello
----Please enter a valid numeric input----
Please enter a number: 234j 
----Please enter a valid numeric input----
Please enter a number: 10
The square, cube and the fourth power of the number 10 is 100, 1000, 10000 respectively
'''