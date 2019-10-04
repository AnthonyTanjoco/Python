'''
Unit 4 Programming Assignment
Anthony Tanjoco
'''

def is_divisible(a, b):         # is_divisible function from Section 6.4
    return a % b == 0
        
def is_power(a, b):             # is_power function with two arguments
    # calling is_divisible within is_power
    # followed by base case for arguements being equal and equal to 1,
    # or equal to a
    if (is_divisible(a, b) == True) and ((a / b) == 1) or ((a / b) == a):
        return True
    elif (is_divisible(a, b) == True) and ((a / b) != 1):
        c = a / b
        return is_power(c, b)  # recursive is_power call
    else:
        if (is_divisible(a, b) == False) and ((a / b) != 1):
            return False
        
    # output for the five test cases
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))    
print("is_power(1, 1)  returns: ", is_power(1, 1))     
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3)  returns: ", is_power(3, 3))





