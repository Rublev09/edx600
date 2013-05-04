class hashSet(object):
    def __init__(self, numBuckets): 
        '''
        numBuckets: int. The number of buckets this hash set will have. 
        Raises ValueError if this value is not an integer, or if it is not greater than zero.

        Sets up an empty hash set with numBuckets number of buckets.
        '''
        if type(numBuckets) != int or numBuckets <= 0:
            raise ValueError()
        self.numbuckets = numBuckets
        self.hashSet = []
        for i in range(numBuckets):
            self.hashSet.append([])

    def getNumBuckets(self):
        return self.numbuckets

    def hashValue(self, e):
        '''
        e: an integer

        returns: a hash value for e, which is simply e modulo the number of 
         buckets in this hash set. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError()
        return e % self.numbuckets
    
    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError()
        count = 0
        for i in self.hashSet:
            if e in i:
                count +=1
        if count  == 0:
            return False
        else:
            return True

    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        ''' 
        if type(e) != int:
            raise ValueError()
        if not self.member(e):
            self.hashSet[self.hashValue(e)].append(e)

    def remove(self, e):
        '''
        e: is an integer 
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError()
        if not self.member(e):
            raise ValueError()
        self.hashSet[self.hashValue(e)].remove(e)

    def __str__(self):
        output = '['
        for b in range(self.getNumBuckets()):
            vals = self.hashSet[b]
            vals.sort()
            output += '{' + ','.join([str(e) for e in vals]) + '},\n'
        return output[:-2] + ']'
        
