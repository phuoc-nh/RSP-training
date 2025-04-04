def maximumTripletValue(nums):
    
    
    prefixMax = nums.copy()
    suffixMax = nums.copy()

    curMax = 0
    for i in range(len(prefixMax)):
        
        if nums[i] > curMax:
            curMax = nums[i]
        else:
            prefixMax[i] = curMax
    
    curMax = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > curMax:
            curMax = nums[i]
        else:
            suffixMax[i] = curMax
    

    # print(prefixMax)    
    # print(suffixMax)    
    res = 0        
    for i in range(1, len(nums) -1):
        res = max(res, (prefixMax[i-1] - nums[i]) * suffixMax[i+1])
    
    
    print(res)
            
    return res
    
nums = [12,6,1,2,7]
maximumTripletValue(nums)

# The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.