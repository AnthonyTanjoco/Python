'''
Unit 5 Programming Assignment
'''

import math                   # importing the math module for later use

def my_sqrt(a):               # my_sqrt function that takes on single argument from Section 7.5 
    x = 3                     # initilizing x
    while True:               # while loop from instructions
        y = (x + a/x) / 2.0   
        if y == x:
            break
        x = y
    return x                  # returning x final value

def test_sqrt(a):             # test_sqrt function that takes on single argument
    # printing table header
    print("a" + (" " * 9) + "mysqrt(a)" + (" " * 25) + "math.sqrt(a)" + (" " * 24) + ("diff"))
    print("-" + (" " * 9) + ("-" * 9) + (" " * 25) + ("-" * 12) + (" " * 24) + ("-" * 4))
    while a < 26:             # while loop to go up to 25
        # printing the values of a, my_sqrt(a), and math.sqrt(a)
        # I hate offset tables!
        # str(a).zfill(s) deals with the offset single digits
        # '{0:.16f}'.format() adds 16 decimal places
        # The final diff shows the formated absolute difference between my_sqrt(a) and math.sqrt(a) less than 1e-14
        print("a = ", str(a).zfill(2), "| my_sqrt(a) = {0:.16f}".format(my_sqrt(a)), "| math.sqrt(a) = {0:.16f}".format(math.sqrt(a)), "| diff = {0:.16f}".format(abs(my_sqrt(a) - math.sqrt(a))))
        a = a + 1             # increasing a by 1 each loop
    

test_sqrt(1)
    
    
