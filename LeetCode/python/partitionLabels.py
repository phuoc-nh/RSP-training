def partitionLabels(s: str):
    lastIndex = {}
    
    for i in range(len(s)):
        lastIndex[s[i]] = i
        
    res = []
    cur = 0
    curLastIndex = 0
    
    for i in range(len(s)):
        cur += 1
        
        if lastIndex[s[i]] > curLastIndex:
            curLastIndex = lastIndex[s[i]]
            
        if i == curLastIndex:
            res.append(cur)
            cur = 0
            
    
    print(res)
    return res
    

            
        

s = "ababcbacadefegdehijhklij"

partitionLabels(s)
    