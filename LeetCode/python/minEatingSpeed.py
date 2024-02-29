import math
def minEatingSpeed(piles, h):
    l = 1
    r = max(piles)
    res = r
    while l <= r:
        mid = (l + r) // 2
        totalTime = 0
        print('mid', mid)
        for i in piles:
            totalTime += math.ceil(i / mid)
        print('totalTime', totalTime)
        if totalTime <= h:
            res = min(res, mid)
            r = mid - 1
        else:
            l = mid + 1
    return res
    
            
            
piles = [30,11,23,4,20]
h = 5

print(minEatingSpeed(piles, h))
            