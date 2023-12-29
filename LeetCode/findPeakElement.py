def findPeakElement(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l+r) // 2
        if mid<len(nums) -1 and nums[mid] < nums[mid+1]:
            l = mid+1
        elif mid > 0 and nums[mid] < nums[mid-1]:
            r = mid-1
        else:
            return mid
        
    return 0
    
nums = [1,2]
print(findPeakElement(nums))