from queue import PriorityQueue

class MedianFinder:
    def __init__(self):
        self.small = PriorityQueue() # max heap
        self.big = PriorityQueue() # min heap

    def addNum(self, num):
        if self.big.queue and num >= self.big.queue[0]:
            self.big.put(num)
            if self.big.qsize() - self.small.qsize() > 1:
                top = self.big.get()
                self.small.put(-top)
        
        else:
            self.small.put(-num)
            if self.small.qsize() - self.big.qsize() > 1:
                top = -self.small.get()
                self.big.put(top)

        # print(list(self.small.queue))
        # print(list(self.big.queue))
        # print(self.big)
        
    def findMedian(self):
        if self.small.qsize() > self.big.qsize():
            return -self.small.queue[0]
        elif self.small.qsize() < self.big.qsize():
            return self.big.queue[0]
        else:
            return (self.big.queue[0] + -self.small.queue[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(4)
obj.addNum(7)
print('>>>>',obj.findMedian())
obj.addNum(2)
obj.addNum(4)
print('>>>>',obj.findMedian())

obj.addNum(3)
