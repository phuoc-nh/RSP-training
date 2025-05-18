def search(nums, target: int) -> int:
    
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        
        if nums[m] == target:
            return m
        
        if nums[l] < nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
                
        else:
            if target > nums[r] or target < nums[m]:
                r = m -1
            else:
                l = m + 1
            
        
        
    
    
    return -1 

nums = [4,5,6,7,8,0,1,2,3]
target = 8

res = search(nums, target)
print('res', res)