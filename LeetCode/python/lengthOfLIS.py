def lengthOfLIS(nums):
    # bottom up
    # dp = [1] * len(nums)
    
    # for i in range(1, len(nums)):
    #     for j in range(i-1, -1, -1):
    #         if nums[i] > nums[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
                
                
    # print(dp)
    
    # return max(dp)
    
    # dfs approach
    LIS = 0
    memo = {}
    def dfs(i):
        # nonlocal LIS
        # if length > LIS:
        #     LIS = length
        if i in memo:
            return memo[i]
        res = 1
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                res = max(res, 1 + dfs(j))
        memo[i] = res
        return res
        
        
    # dfs(0, 1)
    res = 1
    for i in range(len(nums)):
        res = max(res, dfs(i))
        # print(res)
    print(res)
    return res
    # return LIS
    
   
nums = [0,1,0,3,2,3]
lengthOfLIS(nums)