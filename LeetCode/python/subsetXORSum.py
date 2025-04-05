def subsetXORSum(nums):
    res = [0]
    
    def dfs(i, cur):
        res[0] += cur
        # print(cur)
        if i == len(nums):
            return
        
        for j in range(i+1, len(nums)):
            # print("cur", cur)
            # print("nums[j]", nums[j])
            # next = cur ^ nums[j]
            # print('j', j)
            # next = cur.copy()
            # next.append(nums[j])
            dfs(j, cur ^ nums[j])        
        
    # dfs(0, [5])
    for i in range(len(nums)):
        dfs(i, nums[i])
        
    print(res)
    
    return res[0]
    
    
nums = [3,4,5,6,7,8]
subsetXORSum(nums)