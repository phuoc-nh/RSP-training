def shipWithinDays(weights, days: int) -> int:
    
    def canFinish(weight):
        
        if weight < max(weights):
            return False
        
        totalDays  = 1
        cur = weight
        i = 0
        
        while i < len(weights):
            cur -= weights[i]
            
            if cur < 0:
                cur = weight
                totalDays += 1
            else:
                i += 1
                
        print('totalDay', totalDays)
        if totalDays > days:
            return False
        
        return True
    
    # canFinish(21)
    
    l = 1
    r = 500
    res = 0
    while l <= r:
        m = (l + r ) // 2
        print('m', m)
        if canFinish(m):
            res = m
            r = m - 1
        else:
            l = m + 1
        # if m can carry all weight within days
        # decrease cur weight
        # else increase weight to reduce day taken
    print('res', res)
    
    return res

weights = [1,2,3,4,5,6,7,8,9,10]

days = 5
shipWithinDays(weights, days)
# 15
