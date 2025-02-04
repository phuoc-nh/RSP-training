def maxAscendingSum(nums) -> int:
    
    res = nums[0]
    cur = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            cur += nums[i]
            res = max(res, cur)
        else:
            cur = nums[i]
            
    print(res)   
    
    return res 
    
nums = [10,20,30,5,10,50]
maxAscendingSum(nums)