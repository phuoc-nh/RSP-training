def lengthOfLongestSubstring( s: str) -> int:
    if not s: return 0
    res = 1
    l = 0
    dupMap = {}
    for r in range(len(s)):
        if s[r] in dupMap:
            while s[r] in dupMap:
                del dupMap[s[l]]
                l += 1
        else:
            res = max(r - l + 1, res)
        dupMap[s[r]] = r
            
        
    print(res)
    return res
    
    
s = "dvdf"
lengthOfLongestSubstring(s)