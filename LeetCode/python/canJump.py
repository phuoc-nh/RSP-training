def canJump(nums):
    # curMax = 0  
    # for i in range(len(nums)):
        
    #     if i > curMax:
    #         return False
    #     curMax = max(curMax, nums[i] + i)
    # return True

    dp = [False for i in range(len(nums))]
    dp[0] = True
    steps = nums[0]
    lastStepIndex = 0
    for i in range(1, len(nums)):
        print(i, lastStepIndex, steps+1)
        if i in range(lastStepIndex, lastStepIndex+steps+1):
            dp[i] = True
            if nums[i] >= steps - 1:
                lastStepIndex = i
                steps = nums[i]
            else:
                lastStepIndex = i
                steps -= 1
    print(dp)
    return dp[len(nums) - 1]
nums = [3,2,1,0,4]
print(canJump(nums))