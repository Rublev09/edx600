def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowels = ['a','e','i','o','u']
    letter = str(char).lower()
    i = 0
    while i < len(vowels):
        if vowels[i] == letter:
            return True
            break
        i +=1

    else:
        return False

print isVowel('a')
