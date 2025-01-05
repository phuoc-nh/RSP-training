from collections import Counter
def countPalindromicSubsequence(s: str) -> int:
    
    res = set()
    
    left = set()
    
    right = Counter(s)
    
    for m in s:
        right[m] -= 1
        if right[m] == 0:
            del right[m]
            
        for c in left:
            if c in right:
                
                res.add((c, m))
            
        left.add(m)
        
    print(len(res))
    return len(res)
    


s = "aabca"

countPalindromicSubsequence(s)