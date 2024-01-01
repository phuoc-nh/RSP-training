from collections import Counter

def minWindow(s, t):
    counter_t = Counter(t)
    map_s = {}
    i = 0
    j = 0
    res = []
    
    def checkMatch(m_s, m_t):
        for key in m_t.keys():
            if key not in m_s:
                return False
            
            if m_t[key] > m_s[key]:
                return False
        
        return True

    while i < len(s) and j < len(s):
        map_s[s[j]] = map_s.get(s[j], 0) + 1
        # print(i,j, map_s)
        while checkMatch(map_s, counter_t):
            res.append(s[i:j+1])
            map_s[s[i]] = map_s.get(s[i], 0) - 1
            if map_s[s[i]] == 0:
                del map_s[s[i]]
            # print(map_s)
            i += 1
        
        j += 1
    
    # print(res)
    # print(min(res, key=len))
    if len(min) == 0:
        return ""
    
    return min(res, key=len)


    #0123456789 10 11 12
# s = "ADOBECODEB A  N  C"
s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))