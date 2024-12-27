def makeGood(s: str) -> str:
    
    res = []
    
    for i in range(len(s)):
        if not len(res):
            res.append(s[i])
            continue
        
        if abs(ord(s[i]) - ord(res[-1])) == 32:
            res.pop()
        else:
            res.append(s[i])


    
    return "".join(res)
    
    
s = "leEeetcode"
res = makeGood(s)
print(res)