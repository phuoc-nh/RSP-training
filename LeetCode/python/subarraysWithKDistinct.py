def subarraysWithKDistinct(nums, k: int) -> int:
    l_near = 0 
    l_far = 0
    
    count = {}
    
    res = 0
    for r in range(len(nums)):
        count[nums[r]] = 1 + count.get(nums[r], 0)
        
        while len(count.keys()) > k:
            count[nums[l_near]] -= 1
            if count[nums[l_near]] == 0:
                del count[nums[l_near]]
                
            l_near += 1
            l_far = l_near
            
            
        
        while count[nums[l_near]] > 1:
            count[nums[l_near]] -= 1
            l_near += 1
            
        if len(count.keys()) == k:
            res += l_near - l_far + 1
    
    
    print(res)
    return res
    
    
    
nums = [2,2,1,2,2,2,1,1]

k = 2
subarraysWithKDistinct(nums, k)