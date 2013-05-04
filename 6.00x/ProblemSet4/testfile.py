def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print


displayHand({'a':1, 'x':2, 'l':8, 'e':1, 'b':4})


user_or_comp = ''
    def user_or_compfunc():
        user_or_comp = str(raw_input('Enter u to have yourself play, c to have the computer play: '))
        if user_or_comp == 'c' or user_or_comp == 'u':
            break
        else:
            user_or_compfunc()
