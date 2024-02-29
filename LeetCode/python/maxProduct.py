def maxProduct(nums):
    res = max(nums)
    curMax = 1
    curMin = 1
    
    for n in nums:
        if n == 0:
            curMax = 1
            curMin = 1
            continue
        tmp = curMax * n
        curMax = max(n, curMax * n, curMin * n)
        curMin = min(n, curMin * n, tmp)
        res = max(curMax, res)
        
    return res

nums = [2,3,-2,4]
maxProduct(nums)
        
        