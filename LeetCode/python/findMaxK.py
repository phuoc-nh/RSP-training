def findMaxK(nums):
    negativeSet = set()
    positiveSet = set()
    
    for n in nums:
        if n < 0:
            negativeSet.add(n)
        else:
            positiveSet.add(n)

    res = -1
    
    for p in positiveSet:
        if p * -1 in negativeSet:
            res = max(res, p)
            
    print(res)
    return res

nums = [-10,8,6,7,-2,-3]
findMaxK(nums)

      