def lengthOfLIS(nums):
    dp = [1 for i in range(len(nums))]
    res = 0
    for i in range(1, len(nums)):
        for j in range(i, -1, -1):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j]) 
        res = max(res, dp[i])
    print(dp)
    print(res)

    return res
nums = [10,9,2,5,3,7,101,18]
lengthOfLIS(nums)