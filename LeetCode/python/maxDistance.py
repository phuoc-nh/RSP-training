def maxDistance(position, m):
    def canPlace(mid):
        pre = position[0]
        count = 1
        for i in range(1, len(position)):
            if position[i] - pre >= mid:
                count += 1
                pre = position[i]
            
            if count == m:
                return True
        
        return False                

    position.sort()
    l = 1
    r = position[-1]
    res = -1
    while l <= r:
        mid = (l + r) // 2
        
        if canPlace(mid):
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    print(res)
    return res

position = [5,4,3,2,1,1000000000]
m = 2

maxDistance(position, m)