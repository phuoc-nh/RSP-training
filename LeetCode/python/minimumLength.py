
from collections import Counter
def minimumLength(s: str) -> int:
    count = {}
    
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]].append(i)
        else:
            count[s[i]] = [i]    
    print(count)
    
    res = 0
    
    for k in count:
        if len(count[k]) % 2 == 1:
            res += 1
        else:
            res += 2
            
    print(res)
    
    return res

s = "abaacbcbb"
minimumLength(s)