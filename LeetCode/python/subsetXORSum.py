def subsetXORSum(nums):
    total = [0]
    def dfs(j, prev):
        total[0] += prev
        if j == len(nums):
            return
        
        for i in range(j+1, len(nums)):
            dfs(i, prev ^ nums[i])
    
    for i in range(len(nums)):
        dfs(i, nums[i])
    
    # print(total)
    return total[0]
    
nums = [3,4,5,6,7,8]
subsetXORSum(nums)