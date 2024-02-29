def largestPerimeter(nums):
    lenNums = len(nums)
    nums.sort()
    prefixSum = [n for n in nums]
    res = -1
    for i in range(1, lenNums):
        prefixSum[i] += prefixSum[i-1]

    # print(prefixSum)

    for i in range(1, lenNums-1):
        if prefixSum[i] > nums[i+1]:
            res = max(res, prefixSum[i] + nums[i+1])

    print(res)
    return res
nums = [5,5,50]
largestPerimeter(nums)