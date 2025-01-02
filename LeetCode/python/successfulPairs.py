def successfulPairs(spells, potions, success):
    copy = spells.copy()
    spells.sort()   
    potions.sort()
    res = []
    lenPotions = len(potions)
    
    def helper():
        l = 0
        r = lenPotions - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if potions[m] * s < success:
                l = m + 1
            else:
                if m == 0:
                    return m
                
                if potions[m-1] * s >= success:
                    r = m - 1
                else:
                    return m
                
        return lenPotions
    
    m = {}
    for s in spells:
        temp = lenPotions - helper()
        m[s] = temp
        
    
    for c in copy:
        res.append(m[c])
    
    
    return res
    
    
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

# spells = [3,1,2]
# potions = [8,5,8]
# success = 16

successfulPairs(spells, potions, success)