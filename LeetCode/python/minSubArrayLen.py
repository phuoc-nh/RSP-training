def minSubArrayLen(target: int, nums) -> int:
    res = 1e9
    l = 0
    cur = 0
    for r in range(len(nums)):
        cur += nums[r]
        # if cur >= target:
        while cur >= target:
            res = min(res, r - l + 1)
            cur -= nums[l]
            l += 1
                
        else:
            continue
        
    
    return res if res != 1e9 else 0
    
    
target = 11
nums = [1,1,1,1,1,1,1,1]

res = minSubArrayLen(target, nums)
print(res)