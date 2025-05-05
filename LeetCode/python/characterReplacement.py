from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    
    def isValid(m):
        values = m.values()
        maxOcc = max(values)
        sumOcc = sum(values)
        
        if sumOcc - maxOcc > k:
            return False
        
        return True
    
    m = defaultdict(int)
    
    l = 0
    res = 0
    for r in range(len(s)):
        # add el in map
        m[s[r]] += 1
        
        if len(m) > 1:
            while not isValid(m):
                m[s[l]] -= 1
                l += 1
        
        res = max(res, r - l + 1)
        # check if map is valid
        # if valid, continue
        
        # if not valid move l cursor until the map is valid again
        
        
        # m.add(s[r])
        # while len(m) - 1 > k:
        #     m.remove(s[l])
        #     l += 1
            
        
    print(m)
    print(res)
    return res
            
    


s = "ABAB"
k = 2

characterReplacement(s, k)