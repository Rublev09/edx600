def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n % 5 == 0 or n % 8 == 0:
        return True
    countfive = n / 5
    counteight = n / 8
    for i in range(countfive +1):
        for p in range(counteight+1):
            if (i * 5) + (p * 8) == n:
                return True
    else:
        return False
    
    
    
    
