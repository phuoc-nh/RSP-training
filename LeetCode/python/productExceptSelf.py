def productExceptSelf(nums):
    prefix = nums.copy()
    suffix = nums.copy()
    
    for i in range(1, len(nums)):
        prefix[i] *= prefix[i-1]
        
    for i in range(len(nums) - 2, -1, -1):
        suffix[i] *= suffix[i+1]
        
    res = []
    for i in range(len(nums)):
        if i == 0:
            res.append(suffix[i+1])
        elif i == len(nums) - 1:
            res.append(prefix[i-1])
        else:
            res.append(suffix[i+1] * prefix[i-1])
            
    
    
        
    
    return res
    
nums = [-1,1,0,-3,3]

productExceptSelf(nums)