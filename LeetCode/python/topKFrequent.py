import heapq
from collections import Counter

def topKFrequent(nums, k):
    counter = Counter(nums)
    
    listCounter = []
    heapq.heapify(listCounter)    
    
    for num in counter:
        heapq.heappush(listCounter, (counter[num], num)) # value, key
        if len(listCounter) > k:
            heapq.heappop(listCounter)
    
    res = []
    for i in range(k):
        res.append(heapq.heappop(listCounter)[1])
    print(res)
    print(listCounter)
    return res
    

nums = [1,1,1,2,2,3]
k = 2
topKFrequent(nums, k)
