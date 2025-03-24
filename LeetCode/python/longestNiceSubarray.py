def longestNiceSubarray(nums) -> int:
    
    l = 0

    res = 1
    
    def isValid(l, r):
        print(l, r)
        for i in range(l, r):
            if nums[r] & nums[i] != 0:
                return False
            
        return True
    r = 1
    # for r in range(1, len(nums)):
    while r < len(nums):
        if isValid(l, r):
            # print(l, nums[l])
            # print(r, nums[r])
            # print(">>.")
            res = max(res, r - l + 1)
            r += 1
        else:
            l += 1
            
    print(res)
    
    return res
    
# nums = [806734874,280746028,64,256,33554432]

nums = [1,3,8,48,10]




longestNiceSubarray(nums)

    