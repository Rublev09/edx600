x, y, z = 3, 5, 7

if x % 2 != 0:
    if y % 2 != 0:
        if z % 2 != 0:
            if x > y and x > z:
                print 'x is the greatest odd'
            elif y > z:
                print 'y is the greatest odd'
            else:
                print 'z is the greatest odd'
        else:
            if x > y:
                print 'x is the greatest odd'
            else:
                print 'y is the greatest odd'
    elif z % 2 != 0:
        if x > z:
                print 'x is the greatest odd'
        else:   
            print 'z is the greatest odd'
    else:
        print 'x is the greatest odd'   
elif y % 2 != 0:
    if z % 2 != 0:
        if y > z:
            print 'y is the greatest odd'
        else:
            print 'z is the greatest odd'
    else:
        print 'y is the greatest odd'
elif z % 2 != 0:
    print 'z is the greatest odd'
else:
    print 'none of them are odd numbers'    
