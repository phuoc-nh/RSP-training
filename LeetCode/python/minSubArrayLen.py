def minSubArrayLen(target, nums):
    l = 0
    r = 0
    res = 1_000_000_000
    curSum = 0
    while l < len(nums) and r < len(nums):
        curSum += nums[r]
        
        while curSum >= target:
            res = min(res, r - l + 1)
            # print('left', l)
            # print('curSum', curSum)
            curSum -= nums[l]
            l += 1
        
        r += 1
        
    # print(res)
    if res == 1_000_000_000:
        return 0
    return res

target = 4
nums = [1,4,4]
print(minSubArrayLen(target, nums))
            