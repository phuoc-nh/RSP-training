def threeSum(nums):
    nums.sort()
    res = []
    print(nums)
    for i in range(len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                print(j)
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
                
    
        
    print(res)
    return res

    # for i in range(4, 1, -1):
    #     print(i)

nums = [-1,0,1,2,-1,-4]
# [[-2,0,2],[-2,1,1]]
threeSum(nums)