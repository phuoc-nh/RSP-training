def minDays(bloomDay, m, k):
    
    def countBlooms(day):
        countK = 0
        res = 0
        for b in bloomDay:
            if day >= b:
                countK += 1
            else:
                countK = 0
            
            if countK >= k:
                res += 1
                countK = 0
                
        return res
        
    
    l = 0
    r = max(bloomDay)
    
    res = -1
    while l <= r:
        mid = (l + r) // 2
        count = countBlooms(mid)
        if count >= m:
            res = count
            r = mid - 1
        else:
            l = mid + 1
    
    print(res)  
    return res

bloomDay = [1,10,3,10,2]
m = 3
k = 1

minDays(bloomDay, m, k)