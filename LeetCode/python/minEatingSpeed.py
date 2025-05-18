import math

def minEatingSpeed(piles, h: int) -> int:
    def canFinish(banana):
        totalHours = 0
        for p in piles:
            totalHours += math.ceil(p / banana)
        return totalHours
    # res = canFinish(3)
    
    # print(res)
    l = 1
    r = max(piles)
    res = 0
    while l <= r:
        m = (l + r) // 2
        hours = canFinish(m)
        
        if hours > h:
            l = m + 1
        else:
            res = m
            r = m - 1
    
    print('res', res)
    return res
    
    
            
        
    
piles = [3,6,7,11]
h = 8
# output 4

piles = [30,11,23,4,20]
h = 5

piles = [30,11,23,4,20]
h = 6

minEatingSpeed(piles, h)