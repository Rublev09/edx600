def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '' or (len(aStr) == 1 and aStr != char):
        return False
    elif (len(aStr) == 1 and aStr == char) or aStr[len(aStr)/2] == char:
        return True
    elif char < aStr[len(aStr)/2]:
        return isIn(char, aStr[:len(aStr)/2])
    elif char > aStr[len(aStr)/2]:
        return isIn(char, aStr[len(aStr)/2:])
    
