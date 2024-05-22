def subsetsWithDup(nums):
    res = [[]]
    
    def recursion(i, cur):
        cur.append(nums[i])
        c = cur.copy()
        res.append(c)
        
        if i == len(nums):
            return
        
        for j in range(i+1, len(nums)):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            recursion(j, cur)
            cur.pop()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        recursion(i, [])
    print(res)
    return res
nums = [1,2,2]
subsetsWithDup(nums)