def canPartition(nums) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)
    memo = [[-1] * (target + 1) for _ in range(n + 1)]

    def dfs(i, target):
        if target == 0:
            return True
        if i >= n or target < 0:
            return False
        if memo[i][target] != -1:
            print('i',i)
            print('target',target)
            return memo[i][target]
        
        memo[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))
        # print(memo[i][target])
        return memo[i][target]
    res = dfs(0, target)
    for m in memo:
        print(m)

    return res
    
    # for i in range(len(nums)):
    #     res = recursion(i, nums[i])
    #     # print('res', res)
        
    #     if res:
    #         return True
        
    # return False
        

nums = [1,5,11,5]
res = canPartition(nums)

print('res', res)