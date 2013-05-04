def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans = 1
    while exp > 0:
        ans *= base
        exp -=1

    return ans

print iterPower(3,3)
