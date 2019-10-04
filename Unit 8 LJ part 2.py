'''
Unit 8 Learning Journal - Part 2
Anthony Tanjoco
'''
import os
in_file = "favorite things.txt"
out_file = "favorite things again.txt"
path = "C:\\Users\\anthony.tanjoco\\OneDrive\\UoPeople\\CS 1101 Programming Fundamentals\\Unit 8\\"
orig_dic = dict()


def invert_dic(d):  # function from College Success, 2015, p. 107
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = str(key)
        else:
            inverse[val].append(key)
    return inverse

with open(path + in_file, 'r') as rf:  # reading input file
    for line in rf:
        n_line = line.strip()       # stripping the line to get clean text
        s_line = n_line.split(' ')  # splitting the line into list of strings
        s_key = s_line[:-1]         # slicing the list up to the last index
        key = ' '.join(s_key)       # joining the prior slice back into string
        val = s_line[-1]            # slicing the last index
        orig_dic.update({key: val}) # creating dictionary from separated string
        invert_dic(orig_dic)        # inverting dictionary

with open(path + out_file, 'w') as w:   # writing inverted dictionary to file
    inverted = invert_dic(orig_dic)
    for key in inverted:
        w.write(key + ' ' + inverted[key] + '\n')
        

