def findRedundantConnection(edges):
    n = len(edges)
    
    par = [i for i in range(n+1)]
    rank = [1 for i in range(n+1)]
    
    def find(u): # return representative node 

        while par[u] != u:
            u = par[u]
            
        return u
    
    def union(u, v): # union 2 nodes
        pu = find(u)
        pv = find(v)
        
        if pu != pv: # 2 representatives are diff then we can union them
            # compare ranks of 2 nodes
            if rank[pu] > rank[pv]:
                par[pv] = pu
                rank[pu] += 1
            else:
                par[pu] = pv
                rank[pv] += 1
                
            return True
            
        else: #otherwise those belongs to the same component
            return False
  
        
    
        
        
    for u, v in edges:
        success = union(u, v)
        if not success:
            return [u, v]


    
    
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

res = findRedundantConnection(edges)
print('res', res)