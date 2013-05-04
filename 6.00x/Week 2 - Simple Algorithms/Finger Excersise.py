print 'Please think of a number between 0 and 100!'
upper_bound = 100
lower_bound = 0
ans = ''
while ans != 'c':
    guess = (upper_bound + lower_bound)/2
    print 'Is your secret number ' + str(guess) + '?'
    ans = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if ans == "h":
        upper_bound = guess
    elif ans == 'l':
        lower_bound = guess
    elif ans == 'c':
        print 'Game over. Your secret number was: '+  str(guess)
        
    else:
        print "Please enter h, l, or c."
