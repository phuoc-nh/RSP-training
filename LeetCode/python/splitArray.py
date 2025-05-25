def splitArray(nums, k: int) -> int:
    
    def canSplit(maximum):
        cur = 0
        subArrays = 0
        
        for n in nums:
            cur += n
            if cur > maximum:
                subArrays += 1
                cur = n
        
        return subArrays + 1 <= k    
        
    
    l = max(nums)
    r = sum(nums)
    res = r
    
    while l <= r:
        mid = (l + r) // 2
        
        print('mid', mid)
        
        if canSplit(mid):
            print('can mid', mid)
            
            r = mid - 1
            res = mid
        else:
            l = mid + 1
    print(res)
    return res
    
nums = [7,2,5,10,8]
k = 2

splitArray(nums, k)