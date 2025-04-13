def validPartition(nums) -> bool:
    
    def dfs(i):
        if i >= len(nums):
            return True
        res = False
        if i < len(nums) - 1 and nums[i] == nums[i+1]:
            res = dfs(i+2)
        
        if i < len(nums) - 2:
            if nums[i] == nums[i+1] == nums[i+2]:
                res = res or dfs(i+3)
            
            if nums[i] + 1== nums[i+1] == nums[i+2] + 1:
                res = res or dfs(i+3)
            
        return res
        
    return dfs(0)

nums = [1,1,1,2]
res = validPartition(nums)

print(res)