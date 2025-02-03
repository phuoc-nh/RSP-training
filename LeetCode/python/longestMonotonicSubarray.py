def longestMonotonicSubarray(nums) -> int:
    res = 1
    temp = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            temp += 1
            res = max(temp, res)
        else:
            temp = 1
    
    # decrease
    temp = 1
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            temp += 1
            res = max(temp, res)
        else:
            temp = 1
            
    print(res)
    return res
    
    
nums = [3,2,1]

longestMonotonicSubarray(nums)