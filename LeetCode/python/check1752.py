def check(nums) -> bool:
    
    index = nums.index(min(nums))
    print(index)
    lastIndex = len(nums) - 1
    while nums[index] == nums[lastIndex] and lastIndex >= 0:
        index = lastIndex
        lastIndex -= 1
    
    rotatedArray = nums[index:len(nums)] + nums[0:index]
    
    print(rotatedArray)
    
    for i in range(1, len(rotatedArray)):
        if rotatedArray[i] < rotatedArray[i-1]:
            return False
        
        
    return True    
    
nums = [2,1,3,4]

res = check(nums)
print(res)