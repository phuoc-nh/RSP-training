def majorityElement(nums):
    maxCount = 0
    res = 0
    
    m = {}
    
    for n in nums:
        m[n] = m.get(n, 0) + 1
        if m[n] > maxCount:
            res = n
            maxCount = m[n]

    print(res)

    return res

nums = [2,2,1,1,1,2,2]
majorityElement(nums)