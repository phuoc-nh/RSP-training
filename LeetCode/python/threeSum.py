def threeSum(nums):
    nums.sort()
    
    print(nums)
    res = []
    for l in range(len(nums) - 2):
        m = l + 1
        r = len(nums) - 1
        
        if l > 0 and nums[l] == nums[l-1]:
            continue
        
        while m < r:
            if nums[l] + nums[m] + nums[r] == 0:
                res.append([nums[l], nums[m], nums[r]])
                
                m +=1 
                while nums[m] == nums[m-1] and m < r:
                    m += 1
                    
            elif nums[l] + nums[m] + nums[r] > 0:
                r -= 1
                
            else:
                m += 1
                
    print(res)
    
    return res
                
    
    
    
    
    
nums = [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
# [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]

# [-4, -1, -1, 0, 1, 2]
# [[-2,0,2],[-2,1,1]]
threeSum(nums)