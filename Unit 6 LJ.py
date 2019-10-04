'''
Unit 6 Learning Journal - Part 1
Anthony Tanjoco
'''

lyric = "All I want for Christmas is my two front teeth"
print(lyric)
lyric_list = lyric.split()      # spliting the string
del lyric_list[1]               # deleting "I"
lyric_list.remove("Christmas")  # removing "Christmas"
lyric_list.pop(7)               # popping "teeth"
lyric_list.sort()               # sorting list
lyric_list.append("I")          # appending "I"
lyric_list += ["Christmas"]     # adding "Chistmas"
lyric_list.insert(0, "teeth")   # inserting "teeth"
delimiter = " "                 
lyric2 = delimiter.join(lyric_list)  # joining list to string
print(lyric2)
lyric_list.insert(2, lyric_list)  # nested list example
lyric3 = lyric * 2              # example "*" operator
print(lyric3)
print(lyric_list[:1])           # list slice examples
print(lyric_list[5:6])          

def f_words(s):                 # filter for words beginning with "f"
    for w in s:
        if w[0] == "f":
            print(w)
                   
def t_words(s):                 
    t_list = []
    for w in s:
        if w[0] == "t":
            t_list.append(0)    # example of legal list operation doing the wrong thing
            print(t_list)

f_words(lyric_list)
t_words(lyric_list)

    
