def sortColors(nums):
    i = 0
    j = 0
    k = len(nums) - 1
    
    while j <= k:
        if nums[j] == 2:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        elif nums[j] == 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
            j += 1
        else:
            j += 1
    print(nums)
    return nums          

nums = [2,0,1]
sortColors(nums)