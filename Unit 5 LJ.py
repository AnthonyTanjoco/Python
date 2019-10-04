'''
Unit 5 Learning Journal
Anthony Tanjoco
'''
# part 1 - loop from Section 8.3 of textbook
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

# part 2 - three examples of string slices
duck = "Howard The Duck"

print()
print(duck[:7])     # slicing from 0 to the 7th postion 
print(duck[7:10])   # slicing from 7th to the 10th position
print(duck[11:])    # slicing from the 11th postion to the end
print(duck[:7] + duck[-4:])  # adding slices together
