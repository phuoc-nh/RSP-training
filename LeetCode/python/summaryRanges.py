def summaryRanges(nums):
    res = []
    temp = []
    for i in range(len(nums)):
        if not temp:
            temp.append(nums[i])
        else:
            if nums[i] - temp[-1] <= 1:
                if len(temp) == 1:
                    temp.append(nums[i])
                else:
                    temp.pop()
                    temp.append(nums[i])

            else:
                if len(temp) == 1:
                    res.append(f'{temp[0]}')
                else:
                    res.append(f"{temp[0]}->{temp[1]}")
                temp = [nums[i]]
    if temp:
        if len(temp) == 1:
            res.append(f'{temp[0]}')
        else:
            print('.>', temp)
            res.append(f"{temp[0]}->{temp[1]}")
    return res
                
    
nums = [0,2,3,4,6,8,9]
summaryRanges(nums)
# ["0->2","4->5","7"]