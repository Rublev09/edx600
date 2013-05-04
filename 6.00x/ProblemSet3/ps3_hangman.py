# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    newword = []
    for letter in secretWord:
        for char in lettersGuessed:
            if letter == char:
                 newword.append(letter)
                 break

    a = len(secretWord)
    b = len(newword)
    if a == b:
        return True
    else:
        return False
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    newword = []
    dong = ''
    for letter in secretWord:
        for char in lettersGuessed:
            if letter == char:
                 newword.append(letter)
                 break
        if len(newword) == 0:
            dong += "_ "
        else:
            dong += letter
        newword = []
    return dong
            

    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    newword = []
    dong = ''
    for letter in alphabet:
        for char in lettersGuessed:
            if letter == char:
                 newword.append(letter)
                 break
        if len(newword) == 0:
            dong += letter
        else:
            dong += ''
        newword = []
    return dong

            

def hangman(secretWord):
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    print '-----------'

    numguess = 8
    lettersGuessed = []

    def checkGuess():
            availableLetters = getAvailableLetters(lettersGuessed)
            newword = []
            print 'You have ' + str(numguess) + ' guesses left.'
            print 'Available letters: ' + str(getAvailableLetters(lettersGuessed))
            guess = raw_input('Please guess a letter: ').lower()
            for letter in availableLetters:
                if guess == letter:
                    lettersGuessed.append(guess)
                    return guess
            else:
                print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
                print '-----------'
                checkGuess()
                    

        
    while numguess > 0:
        initialword = getGuessedWord(secretWord, lettersGuessed)
        checkGuess()
        newguessedword = getGuessedWord(secretWord, lettersGuessed)
        
        if initialword == newguessedword:
            print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed))
            numguess -= 1
        else:
            print 'Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
        

        print '-----------'

        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            break
        
    else:
        print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
        
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'sea'
hangman(secretWord)
