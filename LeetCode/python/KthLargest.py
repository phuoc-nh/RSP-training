from queue import PriorityQueue

class KthLargest(object):

    def __init__(self, k, nums):
        self.pq = PriorityQueue()
        for num in nums:
            self.pq.put(num)
            if self.pq.qsize() > k:
                self.pq.put()

    def add(self, val):
        self.pq.put(val)
        if self.pq.qsize() > k:
            self.pq.put()
            
        return self.pq.queue[0]
        