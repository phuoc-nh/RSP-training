import math

def jump(nums):
    dp = [math.inf for i in range(len(nums))]
    
    dp[0] = 0
    
    for i in range(len(nums)):
        print(i+1, nums[i]+1)
        for j in range(i+1, nums[i]+1+i):
            if j >= len(nums):
                continue
            if dp[j] != math.inf:
                continue
            dp[j] = min(dp[j], 1 + dp[i])

    print(dp)

    return dp[len(nums)-1]

nums = [2,3,1,1,4]
jump(nums)