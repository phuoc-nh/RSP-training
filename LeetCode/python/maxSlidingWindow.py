import heapq

def maxSlidingWindow(nums, k: int):
    
    heap = []
    for i in range(k):
        heap.append((-nums[i], i)) # store max heap and index
    heapq.heapify(heap)
    # print(-heap[0][0])
    
    res = []
    res.append(-heap[0][0])
    # l = 0
    
    for r in range(k, len(nums)):
        # check most recent removed value in windows
        print('>>>.',nums[r-k])
        heapq.heappush(heap, (-nums[r], r))
        if nums[r-k] == -heap[0][0]:
            # remove top and all the number before the index
            curMax, maxIndex = heapq.heappop(heap)
            while heap and maxIndex > heap[0][1]:
                print(heap)
                heapq.heappop(heap)
            
        
        print('heap', heap)
        res.append(-heap[0][0])
        
    print(res)
    
    return res
            
    

nums = [1]
k = 1
maxSlidingWindow(nums, k)