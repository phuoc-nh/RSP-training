def containsNearbyDuplicate(nums, k: int) -> bool:
    
    numberIndex = {}
    
    for i in range(len(nums)):
        if nums[i] in numberIndex:
            if abs(i - numberIndex[nums[i]]) <= k:
                return True
            else:
                numberIndex[nums[i]] = i
        else:
            numberIndex[nums[i]] = i
            
    return False
    
nums = [1,2,3,1,2,3]
k = 2

res = containsNearbyDuplicate(nums, k)

print(res)