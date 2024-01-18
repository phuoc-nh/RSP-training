def zeroFilledSubarray(nums):
    i = 0
    countZero = 0
    res = 0
    while i < len(nums):
        if nums[i] != 0:
            i += 1
            for j in range(1,countZero+1):
                res += j
            countZero = 0 
        else:
            countZero += 1
            i += 1

    if countZero:
        for j in range(1,countZero+1):
            res += j
    
    print(res)
    return res
nums = [1,3,0,0,2,0,0,4]
zeroFilledSubarray(nums)