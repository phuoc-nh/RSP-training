def findMin(nums) -> int:
    l = 0
    r = len(nums) - 1
    res = 5001
    
    while l <= r:
        m = (l + r) // 2
        
        if nums[m] > nums[r]:
            l = m + 1
        else:
            res = min(res, nums[m])
            r = m -1
            
    
    print(res)
    
    return res
            

            
            
            
        
        
        
        
    
nums = [5,6,7,8,9,0,1,2,3,4]
nums = [3,4,5,1,2]
nums = [11,13,15,17]
findMin(nums)