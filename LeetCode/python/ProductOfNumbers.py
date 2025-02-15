class ProductOfNumbers:

    def __init__(self):
        self.store = [] # {num, product up to here}

    def add(self, num: int) -> None:
        
        if num == 0:
            self.store = []
            
            return
        
        if len(self.store):
            self.store.append((num, num * self.store[-1][1]))
        else:
            self.store.append((num, num))
        

	# 1 2 3 4 5
	# k = 3

    def getProduct(self, k: int) -> int:
        if k > len(self.store):
            return 0
        
        if k == len(self.store):
            return self.store[-1][1]
        
        return int(self.store[-1][1] / self.store[len(self.store) - k -1 ][1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(2)
print(param_2)

# 3 0 2 4 3 2 3 4 8 2
# 3 0 0 0 0 0 0 0 0 0

# 3 1 2 4 3 2 3 4 8 2
# 3 3 6 24 