def guess():
        print 'You have ' + str(1) + ' guesses left.'
        print 'Available letters: '
        guess = raw_input('Please guess a letter: ')
        return guess
guess = guess()

print guess

