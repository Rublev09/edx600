def square(x):
    return x*x

def fourthpower(x):
    return square(x)*square(x)

def fourthpower2(x):
    return square(square(x))


print fourthpower2(2)

print fourthpower(2)
