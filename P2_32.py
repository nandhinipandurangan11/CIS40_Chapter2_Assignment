# CIS40 : Summer 2020: Chapter 2.32 Exercise: Nandhini Pandurangan
# This program uses a function to solve P2.32

# P2.32 Translate the following pseudocode into a Python program
# Read the total book price and number of books
# Compute the tax (7.5 percent of the total book price)
# Compute the shipping charge ($2 per book)
# The price of the order is the sum of the total book price, the tax, and the shipping charge
# Print the price of the order

# constants.py contains constant defined values
import constants


def calculate_book_price():
    flag = True

    # input validation
    while flag:
        try:
            total_book_price = float(input("Please enter the total book price: "))
            num_books = int(input("Please enter the number of books being purchased: "))
            flag = False
        except:
            print("  -----  Please enter valid numeric input  -----")

    # calculating the price of the order
    tax = total_book_price * constants.TAX_ON_TOTAL_BOOK_PRICE
    shipping_charge = num_books * constants.SHIPPING_CHARGE_PER_BOOK
    order_price = total_book_price + tax + shipping_charge

    # printing the output
    print("\nThe price of your order is $%.2f" % order_price)


# calling the function to solve the problem
calculate_book_price()

''' 
Output: 

Please enter the total book price: 100
Please enter the number of books being purchased: 10

The price of your order is $127.50 

-----------------------------------------------------

Please enter the total book price: bye
  -----  Please enter valid numeric input  -----
Please enter the total book price: 32sdkjfsd
  -----  Please enter valid numeric input  -----
Please enter the total book price: 50
Please enter the number of books being purchased: 2

The price of your order is $57.75
'''
