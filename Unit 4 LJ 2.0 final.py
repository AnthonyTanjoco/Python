'''
Unit 4 Learning Journal 2.0 - Part 1
Calculating the slope of a line
Anthony Tanjoco
'''
def slope(x1, y1, x2, y2):    # function for finding slope of a line
    m = (y2 - y1) / (x2 - x1)   # slope formula
    return m

# asking for points for calcuation
x1 = float(input("Please enter the x1 point: "))
y1 = float(input("please enter the y1 point: "))
x2 = float(input("Please enter the x2 point: "))
y2 = float(input("please enter the y2 point: "))

# printing the slope of the line
print("The slope of your line is: ", slope(x1, y1, x2, y2))
