def countSubarrays(nums, k):
    maxNumb = max(nums)
    n = len(nums)
    
    l = 0
    res = 0
    
    maxCount = 0
    
    
    for r in range(n):
        if nums[r] == maxNumb:
            maxCount += 1
            
        while maxCount == k:
            if nums[l] == maxNumb:
                maxCount -= 1
            l += 1
        
        res += l
    print(res)
    return res    
    
      
  
  
nums = [1,4,2,1]

k = 3
countSubarrays(nums, k)