def sortColors(nums):
    p0 = 0
    p1 = 0 # current
    p2 = len(nums) - 1

    while p1 <= p2:
        if nums[p1] == 0:
            nums[p0], nums[p1] = nums[p1], nums[p0]
            p0 += 1
            p1 += 1
        elif nums[p1] == 2:
            nums[p2], nums[p1] = nums[p1], nums[p2]
            p2 -= 1
        else:
            p1 += 1
    print(nums)            

nums = [2,2,0,1,1,0]
sortColors(nums)