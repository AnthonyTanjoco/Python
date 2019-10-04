# Anthony Tanjoco
# Unit 2 Program Assignment

def new_line():                     # Creation of the new_line function.
    print('.')                      # The print command inside new_line to 
                                    # print a dot (.) at the beginning of the line.
def three_lines(new_line):          # Creation of three_lines with nested function calls.
    new_line()
    new_line()
    new_line()

def nine_lines():                   # Creation of nine_lines function.
    three_lines(new_line)
    three_lines(new_line)
    three_lines(new_line)

def clear_screen():                 # Creation of clear_screen function.
    nine_lines()                    # Using combination of three prior functions.
    nine_lines()
    three_lines(new_line)
    three_lines(new_line)
    new_line()

print('Printing 9 Lines!')          # Pinting placeholder for 9 Lines.
print()                             # Print command for line space.
nine_lines()                        # nine_lines function call.
print()
print('Now Printing 25 Lines!')     # Printing placeholder for 25 Lines.
print()
clear_screen()                      # Calling clear_screen function for last line.

                
