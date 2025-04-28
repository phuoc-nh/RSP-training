def sortColors(nums):
    l = 0
    r = len(nums) - 1
    
    # if num = 2, nums[r] = 2, r -= 1, nums[cur] = nums[r] decrease r by 1
    # we still need to consider nums[cur] because it could be either 0 or 1

    # if nums = 0, nums[l] = 0, nums[cur] = nums[l] -> increase l by 1
    
    # if nums = 1 no need to swap number increase pointer mid by 1
    
    m = 0
    while m <= r:
        print(nums[m])
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            m += 1
            l += 1
            continue
        
        if nums[m] == 2:
            nums[r], nums[m] = nums[m], nums[r]
            r -= 1
            # no need to increase m be cause m now could be 1 or 0 so need to consider it in the next loop
            continue
        
        if nums[m] == 1:
            m += 1
            
    print(nums)
        
    
nums = [2,0,2,1,1,0]
# nums = [2,0,1]
# Output: [0,0,1,1,2,2]
sortColors(nums)