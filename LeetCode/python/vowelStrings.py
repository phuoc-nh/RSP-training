def vowelStrings(words, queries):
    prefix = [0] * len(words)
    setVowels = {'a', 'e', 'i', 'o', 'u'}
    
    for i in range(len(words)):
        valid = False
        w = words[i]
        
        if len(w) == 1:
            if w in setVowels:
                valid = True
        
        else:
            if w[0] in setVowels and w[len(w) - 1] in setVowels:
                valid = True
                
        
        if i == 0:
            prefix[i] = 1 if valid else 0
            
        else:
            prefix[i] += prefix[i-1] + (1 if valid else 0)
            
    res = []
    
    
    # print(prefix)
    
    for q1, q2 in queries:
        print(q1, q2)
        
        left = prefix[q1 - 1] if q1 > 0 else 0
        
        res.append(prefix[q2] - left)
        
    print(res)
    return res
    
    
    
    
# words = ["aba","bcb","ece","aa","e"]
# queries = [[0,2],[1,4],[1,1]]

words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]

vowelStrings(words, queries)