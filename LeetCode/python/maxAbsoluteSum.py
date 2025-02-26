def maxAbsoluteSum(nums) -> int:
    
    cur = 0
    res = 0
    
    
    for i in range(len(nums)):
        newCur = cur + nums[i]
        
        print('cur', cur)
        print('newCur', newCur)
        print('nums[i]', nums[i])
        
        if newCur < nums[i]:
            res = max(abs(newCur), res)
            cur = newCur
        else:
            res = max(abs(nums[i]), res)
            cur = nums[i]
            
        print('res', res)
        print('=+==+++++++')
        
    cur = 0
    for i in range(len(nums)):
        newCur = cur + nums[i]
        
        # print('cur', cur)
        # print('newCur', newCur)
        # print('nums[i]', nums[i])
        
        if newCur > nums[i]:
            res = max(abs(newCur), res)
            cur = newCur
        else:
            res = max(abs(nums[i]), res)
            cur = nums[i]
            
        # print('res', res)
        # print('=+==+++++++')

    print(res)
    
    return res
    
    
nums = [-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]



maxAbsoluteSum(nums)            
    
        