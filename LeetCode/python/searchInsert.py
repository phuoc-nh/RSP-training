def searchInsert(nums, target: int) -> int:
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
            
    print(l, r)
        
    return l

nums = [1,3,5,6]
target = 7

# nums = [1,3,5,6]
# target = 0

res = searchInsert(nums, target)
print('res', res)