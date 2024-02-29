# def largestDivisibleSubset(nums):
#     if len(nums) == 1:
#         return nums
#     dp = [1 for i in range(len(nums))]
#     nums.sort()
#     curMax = 1
#     for i in range(len(nums)):
#         tempI = i - 1
#         while tempI >= 0:
#             # print(nums[tempI])
#             if nums[i] % nums[tempI] == 0:
#                 dp[i] = max(dp[tempI]+1,dp[i]) 
#                 curMax = max(dp[i] ,curMax)
#             tempI -= 1
    
#     print(dp)
#     print(curMax)
#     res = []
#     prev = None
#     for i in range(len(nums)-1, -1, -1):
#         if (not prev and dp[i] == curMax) or (dp[i] == curMax and prev % nums[i] == 0):
#             prev = nums[i]
#             res.append(nums[i])
#             curMax -= 1
#     print(res)
#     return res
# nums = [4,8,10,240]
# largestDivisibleSubset(nums)

# def largestDivisibleSubset(nums):
#     cache = {}
#     def dfs(i, prev):
#         if (i, prev) in cache:
#             return cache[(i, prev)]
        
#         if i == len(nums):
#             return []
        
#         res = dfs(i+1, prev)
#         if nums[i] % prev == 0:
#             tmp = [nums[i]] + dfs(i+1, nums[i])
#             res = tmp if len(tmp) > len(res) else res

#         cache[(i, prev)] = res
        
#         return res
    
#     r = dfs(0, 1)

#     print(cache)
#     print(r)
#     return r
        
def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[n] for n in nums]
    
    for i in range(1, len(nums)):
        k = i - 1
        curMax = []
        while k >= 0:
            if nums[i] % nums[k] == 0:
                tmp = dp[i] + dp[k]
                # print(tmp)
                curMax = tmp if len(tmp) > len(curMax) else curMax
            k -= 1
        
        dp[i] = curMax if len(curMax) > 0 else dp[i]
    
    print(dp)
    
    res = []
    for el in dp:
        if len(el) > len(res):
            res = el

    print(res)
    return res
    
nums = [3,4,16,8]
largestDivisibleSubset(nums)