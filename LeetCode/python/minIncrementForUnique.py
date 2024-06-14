from collections import Counter
def minIncrementForUnique(nums):
    nums.sort()
    print(nums)
    res = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            nums[i] += 1
            res += + 1
        elif nums[i-1] > nums[i]:
            temp = nums[i-1] - nums[i] + 1
            nums[i] += temp
            res += temp
    print(nums)
    print(res)
    return res
nums = [3,2,1,2,1,7]
minIncrementForUnique(nums)