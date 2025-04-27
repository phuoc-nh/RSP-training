import math
def firstMissingPositive(nums) -> int:
    n = len(nums)
    # set neg numbers to 0
    for i in range(n):
        if nums[i] < 0:
            nums[i] = 0
            
    # 
    for i in range(n):
        # if nums[i] == 0:
        #     nums[i] = (n + 1) * -1
        index = abs(nums[i]) - 1
        if index < n and index >= 0:
            if nums[index] == 0:
                nums[index] = (n+1) * -1
            else:
                nums[index] = abs(nums[index]) * -1
            
    print(nums)
    
    for i in range(1, n+1):
        if nums[i-1] >= 0:
            print(i)
            return i
        
    return n + 1
    
# nums = [1,2,0]
# nums = [3,4,-1,1]
nums = [0,1,2]


firstMissingPositive(nums)