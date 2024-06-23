import heapq

def longestSubarray(nums ,limit):
    maxHeap = []
    minHeap = []
    res = 0
    l = 0
    
    for r in range(len(nums)):
        heapq.heappush(minHeap, (nums[r], r))
        heapq.heappush(maxHeap, (-nums[r], r))
        
        if -maxHeap[0][0] - minHeap[0][0] > limit:
            l = min(maxHeap[0][1], minHeap[0][1]) + 1
            
            while maxHeap[0][1] < l:
                heapq.heappop(maxHeap)
                
            while minHeap[0][1] < l:
                heapq.heappop(minHeap)
        
        res = max(res, r - l + 1)
    print(res)
    return res
        
nums = [4,2,2,2,4,4,2,2]
limit = 0

longestSubarray(nums, limit)