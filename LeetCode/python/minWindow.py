from collections import Counter
def minWindow(s: str, t: str) -> str:
    # function to check if counterS could satisfy ct
    def isValid():
        for k in ct:
            if k in counterS and counterS[k] >= ct[k]:
                continue
            else:
                return False
            
        return True
    
    ct = Counter(t)
    minLen = float('inf')
    res = ""
    l = 0
    counterS = {}
    
    for r in range(len(s)):
#       if char in t, add it into counterS 
        counterS[s[r]] = counterS.get(s[r], 0) + 1

        while isValid() and l <= r:  
            
            if r - l + 1 < minLen:
                minLen = r - l + 1
                res = s[l:r+1]
            
            counterS[s[l]] -= 1
            if counterS[s[l]] == 0:
                del counterS[s[l]]
            l += 1   

#       then check if counterS is a valid answer 
#       if no continue 
#       if yes store answer and shrink the window until it does not meet req any more
#       if char not in t, just add it into counterS
    
    print('>>>.',res)
    return res
s = "ADOBECODEBANC"
t = "ABC"

minWindow(s, t)