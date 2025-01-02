def shipWithinDays(weights, days: int) -> int:
    res = float('inf')
    
    
    l = 1
    r = 500
    
    maxWeight = max(weights)
    
    while l <= r:
        weight = (l + r) // 2
        # print(l, r)
        # print('weight', weight)
        day = 1
        i = 0
        curWeights = 0
        
        if weight < maxWeight:
            l = weight + 1
            continue
        
        while i < len(weights):
            curWeights += weights[i]
            if curWeights > weight:
                day += 1
                curWeights = 0
            else:
                i += 1
        # print(day)
        # if day == days:
        #     res = min(res, weight)
        #     r = weight - 1
        #     # break
        if day > days:
            l = weight + 1
        else:
            res = min(res, weight)
            r = weight - 1
            
        # if day == days:
        #     res = min(res, weight)
            
        #     break
        # if day > days:
        #     l = weight + 1
        # else:
        #     r = weight - 1
            
    # print(res)
    return res

weights = [3,2,2,4,1,4]
days = 3

shipWithinDays(weights, days)
    
    