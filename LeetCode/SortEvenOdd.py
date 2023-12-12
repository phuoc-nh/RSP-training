def sortEvenOdd(nums):
    # sort desending order at odd index
    oddIndexArray = []
    evenIndexArray = []
    
    for i in range(len(nums)):
        if i % 2 == 0:
            evenIndexArray.append(nums[i])
        else:
            oddIndexArray.append(nums[i])
    
    evenIndexArray.sort()
    oddIndexArray.sort(reverse=True)
    
    res = [None] * len(nums)
    for i in range(len(evenIndexArray)):
        res[i * 2] = evenIndexArray[i]
    
    for i in range(len(oddIndexArray)):
        res[i * 2 + 1] = oddIndexArray[i]       
    
    # print(evenIndexArray)
    # print(oddIndexArray)
    
    return res
nums = [2,1]

print(sortEvenOdd(nums))