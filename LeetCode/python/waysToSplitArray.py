def waysToSplitArray( nums) -> int:
    
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
        
    res = 0
    
    for i in range(len(nums) - 1):
        if nums[i] >= nums[-1] - nums[i]:
            res += 1
    print(res)
    return res
    
    
    
nums = [2,3,1,0]

waysToSplitArray(nums)