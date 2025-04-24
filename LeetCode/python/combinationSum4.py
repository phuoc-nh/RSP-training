def combinationSum4(nums, target: int) -> int:
    
    nums.sort()
    
    memo = {0: 1}
    
    def dfs(cur):
        # if cur == 0:
        #     return 1
        
        if cur in memo:
            return memo[cur]
        
        res = 0
        for num in nums:
            if num > cur:
                break
            
            res += dfs(cur - num)
            
        memo[cur] = res
            
        return res
    
    res = dfs(target)
    
    print(res)
    
    return res
    
nums = [1,2,3]
target = 4

combinationSum4(nums, target)