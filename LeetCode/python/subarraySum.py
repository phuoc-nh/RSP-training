def subarraySum(nums, k):
    m = {0:1}
    total = 0
    res = 0
    for n in nums:
        total += n 
        m[total] = m.get(total, 0) + 1
        
        diff = total - k
        res += m.get(diff, 0)
    print(res)
    return res
nums = [1,1,1]
k = 2
subarraySum(nums, k)