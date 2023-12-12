from random import randrange

class RandomizedSet:
    def __init__(self):
        # easy to get ramdom element bigO(1)
        # remove takes bigO(n), delete last element just takes bigO(1)
        # insert bigO(1) but not sure unique
        self.stack = []
        
        # remove takes bigO(1)
        # insert takes bigO(1) and makes sure unique
        # Can not handle get random
        self.dit = {}

    def insert(self, val):
        if val in self.dit:
            return False
        
        self.stack.append(val)
        # get index of new ele
        lenStack = len(self.stack)
        self.dit[val] = lenStack - 1
        # print('stack insert', self.stack)
        # print('dict insert', self.dit)
        # print('=============')
        return True
    def remove(self, val):
        if val in self.dit:
            lenStack = len(self.stack)
            removeIndex = self.dit[val]
            lastEl = self.stack[-1]
            # Swap in dit and delete
            self.dit[lastEl] = self.dit[val]
            del self.dit[val]
            # swap in stack, remove last el
            self.stack[removeIndex], self.stack[lenStack - 1] = self.stack[lenStack-1], self.stack[removeIndex]
            self.stack.pop()
            # print('stack remove', val, self.stack)
            # print('dict remove', val, self.dit)
            # print('=============')
            return True
        return False
    def getRandom(self):
        lenStack = len(self.stack)
        randomIndex = randrange(lenStack)
        return self.stack[randomIndex]
    
rs = RandomizedSet()

rs.insert(1)
rs.insert(5)
rs.insert(2)
rs.insert(17)
print('random', rs.getRandom())

rs.remove(3)
rs.remove(5)
rs.remove(17)
print('random', rs.getRandom())