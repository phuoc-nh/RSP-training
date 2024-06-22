def numberOfSubarrays(nums, k):
    l = 0
    m = 0
    odds = 0
    res = 0
    for r in range(len(nums)):
        if nums[r] % 2 == 1:
            odds += 1

        while odds > k:
            if nums[l] % 2 == 1:
                odds -= 1
                
            l += 1
            m = l
            
        if odds == k:
            while nums[m] % 2 == 0:
                m += 1
            
            res += m - l + 1
    
    print(res)
    return res    
        
nums = [1,1,2,1,1]
k = 3

numberOfSubarrays(nums, k)