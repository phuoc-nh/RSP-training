def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    dp = [1 for i in range(len(nums))]
    nums.sort()
    curMax = 1
    for i in range(len(nums)):
        tempI = i - 1
        while tempI >= 0:
            # print(nums[tempI])
            if nums[i] % nums[tempI] == 0:
                dp[i] = max(dp[tempI]+1,dp[i]) 
                curMax = max(dp[i] ,curMax)
            tempI -= 1
    
    print(dp)
    print(curMax)
    res = []
    prev = None
    for i in range(len(nums)-1, -1, -1):
        if (not prev and dp[i] == curMax) or (dp[i] == curMax and prev % nums[i] == 0):
            prev = nums[i]
            res.append(nums[i])
            curMax -= 1
    print(res)
    return res
nums = [4,8,10,240]
largestDivisibleSubset(nums)