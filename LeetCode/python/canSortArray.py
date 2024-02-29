def canSortArray(nums):
    countOneList = [0 for i in range(len(nums))]

    for i in range(len(nums)):
        count = 0
        temp = nums[i]
        while temp > 0:
            if temp % 2 == 1:
                count += 1
            temp = temp >> 1
        
        countOneList[i] = count
    
    curMax = None
    l = []    
    i = 0
    
    while i < len(nums):
        cur = countOneList[i]
        minCur = float('inf')    
        maxCur = float('-inf')
        while i < len(nums) and cur == countOneList[i]:
            minCur = min(minCur, nums[i])
            maxCur = max(maxCur, nums[i])
            
            i += 1
            
        l.append(minCur)
        l.append(maxCur)
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            return False
    return True
nums = [3,16,8,4,2]
print(canSortArray(nums))