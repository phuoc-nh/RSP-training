def removeElement(nums, val: int) -> int:
    
    p = 0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        
        nums[p] = nums[i]
        p += 1
        
    print(p)
    print(nums)
    
    return p
    
nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)