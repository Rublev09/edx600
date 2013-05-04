import string


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    lowerlist = []
    upperlist = []
    shiftedlowerlist = []
    shiftedupperlist = []

    for i in range(len(lower_case)):
        if i+shift <= 25:
            lowerlist.append(lower_case[i])
            upperlist.append(upper_case[i])
            shiftedlowerlist.append(lower_case[i +shift])
            shiftedupperlist.append(upper_case[i +shift])
        else:
            lowerlist.append(lower_case[i])
            upperlist.append(upper_case[i])
            shiftedlowerlist.append(lower_case[i +shift -26])
            shiftedupperlist.append(upper_case[i +shift -26])

    dictencrypt = {}
    for i in range(len(lower_case)):
        dictencrypt[upperlist[i]] = shiftedupperlist[i]
        dictencrypt[lowerlist[i]] = shiftedlowerlist[i]
    
    return dictencrypt



def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encryptedword = ''
    for i in text:
        if i in coder:
            encryptedword += coder[i]
        else:
            encryptedword += i

    return encryptedword

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))


def findBestShift(text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    maxreal = 0
    bestshift = 0
    newtext = None
    textlist = []
    for i in range(26):
        count = 0
        newtext = applyShift(text,i)
        textlist = newtext.split(' ')
        for word in textlist:
            if isWord(wordList, word):
                count +=1

        
