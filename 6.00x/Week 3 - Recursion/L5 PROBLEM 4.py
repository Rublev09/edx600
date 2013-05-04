def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    val = min(a,b)
    while val >0:
        if a % val == 0 and b% val == 0:
            return val
            break
        else:
            val -=1

    return val

def gcdIterAns(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue


print gcdIter(7, 12)
