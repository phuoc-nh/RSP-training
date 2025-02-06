def tupleSameProduct(nums) -> int:
    s = {}
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            prod = nums[i] * nums[j]
            if prod in s:
                res += 8 * s[prod]
                s[prod] += 1
            else:    
                s[prod] = 1
            
    print(s)
    print(res)
    
    return res
    
    
nums = [2,3,4,6,8,12]



tupleSameProduct(nums)


# [6, 8, 12, 16, 24, 12, 18, 24, 36, 24, 32, 48, 48, 72, 96]
