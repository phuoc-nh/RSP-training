def rob(nums):
    dp = [0] * (len(nums) + 1)
    # print('dp', dp)
    dp[0] = 0
    dp[1] = nums[0]
    dp[2] = nums[1]
    for i in range(3,len(nums)+1):
        dp[i] = max(nums[i - 1] + dp[i - 2], nums[i - 1] + dp[i - 3])
        
    # print(dp)
    return max(dp)

nums =[2,7,9,3,1]
print(rob(nums))