def maxSubarraySumCircular(nums):
    right_max = nums.copy()
    suffix = nums[-1]
    # calculate right max suffix
    # which means the max suffix value from right to left
    for i in range(len(nums) - 2, -1, -1):
        suffix += nums[i]
        right_max[i] = max(right_max[i+1], suffix)
    
    print(right_max)
    
    res = nums[0]
    cur_max = 0 # accumulate positive value if the value is negative reset to 0
    prefix = 0
    for i in range(len(nums)):
        cur_max = max(0, cur_max) + nums[i]
        res = max(cur_max, res)
        prefix += nums[i]
        
        if i + 1 < len(nums):
            res = max(res, prefix + right_max[i + 1])
            
    
    return res
    
    
nums = [1,-2,3,-2]

maxSubarraySumCircular(nums)