def longestConsecutive(nums):
    numSet = set(nums)

    res = 1
    for n in nums:
        if (n - 1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            
            res = max(length, res)
    print(res)
    return res

nums = [0,3,7,2,5,8,4,6,0,1]
longestConsecutive(nums)