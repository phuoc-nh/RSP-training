def canPartition(nums) -> bool:
    
    total = sum(nums)
    
    if total % 2 == 1:
        return False

    memo = {}
        
    # target = total // 2
    # n = len(nums)
    # memo = [[-1] * (target + 1) for _ in range(n + 1)]


    def dfs(i, target):
        if i >= len(nums) or target < 0:
            return False
        if (i, target) in memo:
            return memo[(i, target)]
        
        if target == 0:
            return True
        
        memo[(i, target)] = dfs(i+1, target) or dfs(i+1, target - nums[i])
        print(memo)
        return memo[(i, target)]      
    
    res = dfs(0, total // 2)
        
    return res
nums = [1,5,11,5]
res = canPartition(nums)

print('res', res)