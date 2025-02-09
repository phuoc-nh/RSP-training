import heapq

from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.indexNumberMap = {}
        self.numberToIndices = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:
        self.indexNumberMap[index] = number
        heapq.heappush(self.numberToIndices[number], index)
            
    def find(self, number: int) -> int:
        
        print('numberToIndices',  self.numberToIndices)
        print('indexNumberMap',  self.indexNumberMap)
        
        if not self.numberToIndices.get(number):
            return -1
        
        while len(self.numberToIndices[number]):
            topId = heapq.heappop(self.numberToIndices[number])
            
            if self.indexNumberMap.get(topId) == number:
                return topId
            
        return -1


# Your NumberContainers object will be instantiated and called as such:
obj = NumberContainers()
# param_2 = obj.find(10)

obj.change(2,10)
obj.change(1,10)
obj.change(3,10)
obj.change(5,10)


print('>>>>>', obj.find(10))

obj.change(1,20)
print('>>>>>', obj.find(10))
# param_2 = obj.find(10)
# obj.change(1,20)
# param_2 = obj.find(10)
# print(param_2)

