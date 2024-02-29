from collections import Counter

def minWindow(s, t):
    counterT = Counter(t)
    window = {}
    l = 0
    need = len(counterT.keys())
    have = 0
    res, resLen = [-1,-1] , float('infinity')

    for r in range(len(s)):
        window[s[r]] = window.get(s[r], 0) + 1
        if s[r] in counterT and window[s[r]] == counterT[s[r]]:
            have += 1
            
        while have == need:
            if (r - l + 1) < resLen:
                res = [l,r]
                resLen = (r-l+1)
            window[s[l]] -= 1
            if s[l] in counterT and window[s[l]] < counterT[s[l]]:
                have -= 1
            l += 1
            
    # print(res)
    l, r = res
    return s[l:r+1] if resLen != float('infinity') else ""

    #0123456789 10 11 12
# s = "ADOBECODEB A  N  C"
s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))