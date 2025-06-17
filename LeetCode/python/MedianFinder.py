import heapq
class MedianFinder:
    # 2 heaps, one max heap to store first half, one min heap to store second half
    # if len first half == len second half , append to first half 
    # but we dont want this num is bigger than any value in second half
    # if num less than top of second half -> ok to append to first half
    # else num bigger than top of second half -> pop top from second half put it into first half and put num to second half
    
    # else first half != len second half
    # consider to put to second half
    # if num bigger than top of second half -> ok to put it into second half
    # else if num smaller than top of first half -> num belongs to first half -> pop one value from first half put it into second half and put num into first half

    def __init__(self):
        self.firstHalf = [] # max heap
        self.secondHalf = [] # min heap
        heapq.heapify(self.firstHalf)
        heapq.heapify(self.secondHalf)
        

    def addNum(self, num: int) -> None:
        if not len(self.firstHalf):
            heapq.heappush(self.firstHalf, -num) # max heap
            return

        if len(self.firstHalf) == len(self.secondHalf):
            if num < self.secondHalf[0]:
                heapq.heappush(self.firstHalf, -num)
            else:
                top = heapq.heappop(self.secondHalf)
                heapq.heappush(self.firstHalf, -top)
                
                heapq.heappush(self.secondHalf, num)
        else:
            if len(self.secondHalf) and num > self.secondHalf[0]:
                heapq.heappush(self.secondHalf, num)
            else:
                if num < self.firstHalf[0] * -1: # max heap
                    top = -heapq.heappop(self.firstHalf)
                    heapq.heappush(self.secondHalf, top)
                    
                    heapq.heappush(self.firstHalf, -num)
                else:
                    heapq.heappush(self.secondHalf, num)
                        
            
    def findMedian(self) -> float:
        if len(self.firstHalf) == len(self.secondHalf):
            return (self.firstHalf[0] * -1 + self.secondHalf[0]) / 2
        else:
            return self.firstHalf[0]