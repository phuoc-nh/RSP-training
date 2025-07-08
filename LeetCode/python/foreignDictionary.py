def foreignDictionary(words):
    # build adjacency list
    adj = {}
    for word in words:
        for c in word:
            adj[c] = set()
            
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        
        minL = min(len(w1), len(w2))
        
        if w1[:minL] == w2[:minL] and len(w1) > len(w2):
            return ""
        
        for j in range(minL):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    print(adj)
    
    # run topo sort and return reversed order
    visited = set() # track word added in result 
    path = set() # track cycle
    
    res = []
        
    def dfs(c):
        if c in path:
            return False
        
        if c in visited:
            return True 

        visited.add(c)
        path.add(c)
        for v in adj[c]:
            if not dfs(v):
                return False
        
        # add word
        res.append(c)
        # backtrack
        path.remove(c)
        # no need to remove visited
        return True
    
    for word in words:
        for c in word:
            
            if c in visited:
                continue
            
            if not dfs(c):
                return ''
    # print(''.join(reversed(res)))
    
    return ''.join(reversed(res))

words=["wrtkj","wrt"]
res = foreignDictionary(words)

print('res', res)