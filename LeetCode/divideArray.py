def divideArray(nums, k):
    nums.sort()
    # print(nums)
    res = []
    for i in range(0, len(nums), 3):
        print(nums[i])
        res.append(nums[i:i+3])
    # print(res)

    for r in res:
        if r[2] - r[0] > k:
            return []

    return res

nums = [1,3,4,8,7,9,3,5,1]
k = 2

print(divideArray(nums, k))

