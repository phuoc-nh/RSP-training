def minWindow(s: str, t: str) -> str:
    
    if len(t) > len(s):
        return ""
    
    countT = {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
        
    
    
    def match(countS):
        for k in countT:
            if k in countS and countS[k] >= countT[k]:
                continue
            else:
                return False
            
        return True
                
                
    l = 0
    countS = {}
    
    res = ""
    lenRes = float('inf')
    for r in range(len(s)):
        countS[s[r]] = 1 + countS.get(s[r], 0)
        # print(l)
        # print(countS)
        if s[r] in countT:
            while match(countS):
                if r - l + 1 < lenRes:
                    lenRes = r - l + 1
                    res = s[l:r+1]
                    
                countS[s[l]] -= 1
                # if countS[s[l]] == 0:
                #     del countS[s[l]]
                l += 1            
    # print(res)
    
    
    return res
s = "a"
t = "aa"

minWindow(s, t)