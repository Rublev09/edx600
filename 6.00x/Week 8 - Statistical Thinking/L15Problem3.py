def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    totlen = 0
    for i in L:
        totlen+= len(i)
    mean = totlen / float(len(L))
    tot = 0.0
    for x in L:
        tot += (len(x) - mean)**2
    return (tot/len(L))**0.5
