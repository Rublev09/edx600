def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    i = start
    totalexposed = 0
    while i<stop:
        totalexposed += (f(i)*step)
        i+=step

    return float(totalexposed)

print radiationExposure(40, 100, 1.5)
