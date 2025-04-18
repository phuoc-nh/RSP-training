def findNumberOfLIS(nums) -> int:
    
    LIS = 0
    res = 0
    
    def dfs(i, length):
        nonlocal LIS, res
        if length > LIS:
            LIS = length
            res = 1
        elif length == LIS:
            res += 1
        
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dfs(j, length + 1)
                
    
    for i in range(len(nums)):
        dfs(i, 1)
    
    print('res', res)
    return res
    
    # res = 0
    # maxCurLen = 1
    # for i in range(len(nums)):
    #     curLen = dfs(i)
    #     print(curLen, i)
    #     if curLen > maxCurLen:
    #         res = 1
    #         maxCurLen = curLen
    #     elif curLen == maxCurLen:
    #         res += 1
    
    # print(res)
    
nums = [1,3,5,4,7]

findNumberOfLIS(nums)