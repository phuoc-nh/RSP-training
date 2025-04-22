def maxProduct(nums):
    curMax = 1
    curMin = 1
    res = max(nums)
    
    for i in range(len(nums)):
        n = nums[i]
        if n == 0:
            curMax = 1
            curMin = 1
            continue
        
        tempMax = curMax * n
        tempMin = curMin * n
        
        print('tempMax', tempMax)
        print('tempMin', tempMin)
        
        
        curMax = max(tempMax, tempMin, n)
        curMin = min(tempMax, tempMin, n)
        
        print('curMax', curMax)
        print('curMin', curMin)
        print('-------')
        
        res = max(res, curMax)
        
    print(res)
    
    return res
nums = [2,3,-2,4, 5]
maxProduct(nums)
        
