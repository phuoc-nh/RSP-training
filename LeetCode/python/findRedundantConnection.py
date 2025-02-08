def findRedundantConnection(edges):
    n = len(edges)
    path = [-1] * (n + 1)
    
    
    path[edges[0][0]] = edges[0][0] # set root
    path[edges[0][1]] = edges[0][0] # set root
    
    print(path)
    
    for i in range(1, len(edges)):
        u, v = edges[i]
        if path[v] != -1:
            return edges[i]
        path[v] = u
        
    
        
        
    
    
    
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

res = findRedundantConnection(edges)
print('res', res)