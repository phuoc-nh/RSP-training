import heapq

def minOperations(nums, k: int) -> int:
    
    res = 0
    heapq.heapify(nums)
    while len(nums) >= 2 and nums[0] < k:
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        
        print('num1', num1)
        print('num2', num2)
        
        heapq.heappush(nums, min(num1, num2) * 2 + max(num1, num2))
        
        res += 1
        
    print(res)
    
    return res
        
    
    
nums = [2,11,10,1,3]
k = 10
minOperations(nums, k)