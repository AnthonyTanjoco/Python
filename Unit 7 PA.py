'''
Programming Fundamentals
Unit 7 Programming Assignment
'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):       # histogram function from the assignment
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
    
def has_duplicates(s):  # implementation of the has_duplicates function taking a string parameter
    d = histogram(s)    # calling the histogram function
    flag = False
    for t in d:         # looping through keys in dictionary object
        flag = flag or (d[t] > 1)  # flag test for dictionary values greater than 1
    return flag         # returning a boolean
        
print("Part 1")
print()
for dups in test_dups:  # looping over the strings in test_dups
    if has_duplicates(dups) == True:    # test for boolean return
        print(dups, "has duplicates")
    else:
        print(dups, "has no duplicates")

def missing_letters(s):  # missing_letters function taking a string parameter
    d = histogram(s)     # calling the histogram function
    global alphabet      # using the alphabet global variable directly
    missabet = list(alphabet)  # turning the alphabet string into a list and assigning to variable
    for letter in d:     # looping through keys in dictionary object
        if letter in alphabet:  # test for letter in alphabet string
            missabet.remove(letter)  # removing letter from missabet list
            delimiter = ''          # setting delimiter to join list back to string
            remaining = delimiter.join(missabet) # joining missabet list into string and assigning
    return remaining                            # to remaining variable

print()
print("Part 2")
print()
for miss in test_miss:      # looping over test_miss strings
    if missing_letters(miss) == "":     # calling missing_letters for test of all letters used
        print(miss, "uses all the letters")
    else:
        print(miss, "is missing letters", missing_letters(miss))

            

