from collections import defaultdict

def findAnagrams(s: str, p: str) :
    lenP = len(p)
    lenS = len(s)
    
    if lenP > lenS:
        return []
    
    res = []
    countP = {}
    
    for c in p:
        countP[c] = countP.get(c, 0) + 1
    
    
    countS = {}
    for c in s[0:lenP]:
        countS[c] = countS.get(c, 0) + 1
    
    if countP == countS:
        res.append(0)
    
    for i in range(1, lenS - lenP + 1):
        countS[s[i-1]] -= 1
        if countS[s[i-1]] == 0:
            del countS[s[i-1]]
            
        countS[s[i + lenP - 1]] = countS.get(s[i + lenP - 1], 0) + 1
        
        if countP == countS:
            res.append(i)
            
    print(res)
    
    
    return res

# s = "abab"
# p = "ab"

s = "cbaebabacd"
p = "abc"
findAnagrams(s, p)
    
    
    
    