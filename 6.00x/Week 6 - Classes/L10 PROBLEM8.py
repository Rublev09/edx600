class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        self.vals.insert(0,e)
    def remove(self):
        try:
            return self.vals.pop()
        except:
            raise ValueError()
    
