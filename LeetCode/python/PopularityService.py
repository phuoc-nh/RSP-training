class PopularityService:
    def __init__(self):
        self.keyToPopular = {}
        self.popularCountToKey = {}
        self.maxCount = 0
    def increase(self, id):
        if id not in self.keyToPopular:
            self.keyToPopular[id] = 0
        self.keyToPopular[id] += 1

        count = self.keyToPopular[id]
        if count > self.maxCount:
            self.maxCount = count
        if count not in self.popularCountToKey:
            self.popularCountToKey[count] = []
        
        self.popularCountToKey[count].append(id)
        
    def decrease(self, id):
        prev = self.keyToPopular[id]
        self.popularCountToKey[prev].pop(id)
        if len(self.popularCountToKey[prev]) == 0 and prev == self.maxCount:
            self.maxCount -= 1
        
        
        self.keyToPopular[id] -= 1
        
        
    def mostPopular(self):
        