def countBadPairs(nums) -> int:
    res = 0
    count = {}
    n = len(nums)
    for i in range(len(nums)):
        key = nums[i] - i
        
        if key in count:
            res += count[key]
            count[key] += 1
        else:
            count[key] = 1
        
    
                
    print(int(n*(n-1)/2 - res))
    
    return int(n*(n-1)/2 - res)
    
    
nums = [4,1,3,3]
countBadPairs(nums)