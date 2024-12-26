def containsNearbyDuplicate(nums, k: int) -> bool:
    count = {}
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]].append(i)
        else:
            count[nums[i]] = [i]
            
    print(count)
    
    for _, v in count.items():
        if len(v) < 2:
            continue
        
        for i in range(1, len(v)):
            # print(abs(v[i] - v[i-1]) <= k)
            if abs(v[i] - v[i-1]) <= k:
                return True
            
            
    return False
            


nums = [1,2,3,1,2,3]
k = 2

res = containsNearbyDuplicate(nums, k)
print(res)