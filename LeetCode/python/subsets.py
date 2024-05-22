def subsets(nums):
    res = [[]]
    
    def recursion(i, cur):
        cur.append(nums[i])
        c = cur.copy()
        res.append(c)
        
        if i == len(nums):
            return
        
        for j in range(i+1, len(nums)):
            recursion(j, cur)
            cur.pop()
            
    for i in range(len(nums)):
        recursion(i, [])
    print(res)
    return res
nums = [1]
subsets(nums)