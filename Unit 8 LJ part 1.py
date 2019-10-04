'''
Unit 8 Learning Journal - Part 1
Anthony Tanjoco
'''
import os
in_file = "a few favorite things.txt"
out_file = "favorite things.txt"
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

with open(path + in_file, 'a') as f:    # appending 3 more items to input file
    f.write('4) warm wollen mittens\n')
    f.write('5) brown paper packages tied up with strings\n')
    f.write('6) cream colored ponies\n')

with open(path + in_file, 'r') as rf:   # reading input file
    for line in rf:
        n_line = line.strip()           # stripping the line to get clean text
        s_line = n_line.split(' ')      # splitting the line into list of strings
        key = s_line[0]                 # getting first list string 
        s_val = s_line[1:]              # getting rest of list strings
        val = ' '.join(s_val)           # joing rest of list back to string
        orig_dic.update({key: val})     # creating dictionary
        invert_dic(orig_dic)            # inverting dictionary

with open(path + out_file, 'w') as w:   # writing dictionary to file
    inverted = invert_dic(orig_dic)
    for key in inverted:
        w.write(key + ' ' + inverted[key] + '\n')
        

