def isPrime(n):
    if type(n) != int:
        raise TypeError()
    if n <= 0:
        raise ValueError()


    if n <2:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            return False
    return True
