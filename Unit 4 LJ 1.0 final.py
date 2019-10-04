'''
Unit 4 Learning Journal 1.0 - Part 1
hypotenuse function
Anthony Tanjoco
'''
import math  # importing the math module

def hypotenuse(a, b):  # function for hypotenuse of a right triangle
    c_sum = a**2 + b**2  
    c_sqrt = math.sqrt(c_sum)
    return round(c_sqrt, 1)  # rounding because I don't like the display

# printing outputs
print('The hypotenuse of a 3:4 triangle is: ', hypotenuse(3, 4))
print('The hypotenuse of a 5:7 triangle is: ', hypotenuse(5, 7))
print('The hypotenuse of a 10:12 triangle is: ', hypotenuse(10, 12))
