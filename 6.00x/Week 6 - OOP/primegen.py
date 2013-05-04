def genPrimes():
    primes = []
    test = 1
    while True:
        test += 1
        for i in primes:
            if test % i == 0:
                break
        else:
            primes.append(test)
            yield test
            
                


def genFib():
    fibn_1 = 1  # fib(n-1)
    fibn_2 = 0  # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

def generator1():
    if True:
        yield 1 

def generator2():
    if False:   
        yield 1

g1 = generator1()
g2 = generator2()

print type(g1)
print type(g2)
print g1.next()
print g2.next()
