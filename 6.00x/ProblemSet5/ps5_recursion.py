# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 1 or len(aStr) == 0:
        return aStr
    newstr = ''
    newstr += aStr[-1]
    return newstr + reverseString(aStr[0:-1])

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    newword = ''
    if len(x) == 0:
        return True
    if not x[0] in word:
        return False
    if len(x) > 1:
        newword = word[word.index(x[0]):]
        if newword.index(x[0]) > newword.index(x[1]):
            return False
        else:
            newword = word[word.index(x[0])+1:]
            return x_ian(x[1:],newword)
    else:
        return x_ian(x[1:],word)
        
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    newtext = ''
    
    
    return textlist.pop(0)
