import math
def maxSubArray(nums):
    res = nums[0]
    curMax = nums[0]
    for i in range(1, len(nums)):
        curMax = max(nums[i], curMax + nums[i])
        res = max(res, curMax)
    print(res)
    return res
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)