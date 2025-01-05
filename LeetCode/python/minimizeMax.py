def minimizeMax(nums, p: int) -> int:
    nums.sort()
    
    l = 0
    r = 1_000_000_000
    
    res = float('inf')
    
    def valid(threshold):
        i = 0
        count = 0
        while i < len(nums) - 1:
            
            if nums[i+1] - nums[i] <= threshold:
                count += 1
                if count == p:
                    return True
                
                i += 2
            else:
                i += 1
                
        return False
            
    
    while l <= r:
        m = (l + r) // 2 # assumed result
        
        if valid(m):
            res = min(res, m)
            r = m - 1
        else:
            l = m + 1
    
    print(res)
        
    return res
    
    
    
    
# nums = [10,1,2,7,1,3]
# p = 2

nums = [4,2,1,2]
p = 1

minimizeMax(nums, p)