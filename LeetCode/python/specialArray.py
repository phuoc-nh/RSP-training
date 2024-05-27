def specialArray(nums):
    nums.sort()
    l = 1
    r = len(nums) + 1
    while l < r:
        mid = (l + r) // 2
        
        count = 0
        for j in range(len(nums)):
            if nums[j] >= mid:
                count += 1
        
        if count == mid:
            return mid
        elif count > mid:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1
nums = [0,4,3,0,4]
print(specialArray(nums))