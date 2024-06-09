def subarraysDivByK(nums, k):
    m = {0: 1}
    total = 0
    res = 0
    for n in nums:
        total += n
        r = total % k
        if r in m:
            res += m[r]
            m[r] = m.get(r, 0) + 1
        else:
            m[r] = m.get(r, 0) + 1
    print(res)
    
    return res

nums = [4,5,0,-2,-3,1]
k = 5
subarraysDivByK(nums, k)
        