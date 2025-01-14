from collections import Counter

def canConstruct(s: str, k: int) -> bool:
    
    if k > len(s):
        return False
    
    count = Counter(s)
    odd = 0
    for key in count:
        if count[key] % 2 == 1:
            odd += 1
            
    return odd <= k
    
    
s = "leetcode"
k = 2

res = canConstruct(s, k)
print(res)

