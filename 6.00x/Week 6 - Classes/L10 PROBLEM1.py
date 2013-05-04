def thisRaisesAZeroDivisionError():
    x = 1/0

def thisRaisesAValueError():
    y = int('Five')

def thisDoesNotRaiseAnyErrors():
    z = 'just a string'

def tryExercise():
    print 'A',
    try:
        return
        print 'B',
    except ZeroDivisionError as e:
        print 'C',
    else:
        print 'D',
    finally:
        print 'E',
    print 'F'

try:
    a = 1.0 / 0.0
except ArithmeticError:
    print "caught ArithmeticError, don't know what kind"

try:
    a = 1.0 / 0.0
except ArithmeticError as e:
    print "caught ArithmeticError:", e
