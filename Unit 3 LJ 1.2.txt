# Unit 3 Learning Journal
# 1.2
# Anthony Tanjoco


def countdown(n):                               # countdown recursive function
    if n < 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def countup(n):                                 # countup recursive function
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

number_string = input("Please enter a number? ")  # keyboard input
n = int(number_string)                          # converting string to integer 

if n > 0:                                  # conditional for converted integer
    countdown(n)            
else:
    countup(n)
        


# chose to call countup for 0, because the condition looked cleaner
