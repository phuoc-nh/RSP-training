import heapq

def maxSlidingWindow(nums, k):
    heap = [] # max heap
    res = []

    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        
        if i >= k - 1:
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
            
    print(res)
    
    return res
    
    
    
nums = [1]
k = 1

maxSlidingWindow(nums, k)