def sol(nums, k):
    prefixMap = {
        0: -1
    }
    res = -1
    cur = 0
    for i in range(len(nums)):
        cur += nums[i]
        if cur not in prefixMap:
            prefixMap[cur] = i

        diff = cur - k
        if diff in prefixMap:
            res = max(res, i - prefixMap[diff])
    print(res)
    return res
nums = [1, -1, 5, -2, 3]
k = 3

sol(nums, k)