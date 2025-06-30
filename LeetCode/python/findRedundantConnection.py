def findRedundantConnection(edges):
    # find all elements belong to the cycle
    # loop through edges reservedly and if the pair in the cycle return it
    # how to find the cycle
    # dfs through nodes, if the node is in visited first point of cycle detected
    # backtrack and the node to the cycle 
    # if cycle start point equal to node it means that we already added all the nodes to the cycle 
    # we need to stop adding nodes to the cycle
    
    # adj = {}
    # for u, v in edges:
    #     if u not in adj:
    #         adj[u] = [] 
    #     adj[u].append(v)
        
    #     if v not in adj:
    #         adj[v] = []
    #     adj[v].append(u)
        
    # startCycle = -1
    # cycle = set()
    # visited = set()
    
    # def dfs(cur, par):
    #     nonlocal startCycle
    #     if cur in visited:
    #         # cycle start here
    #         startCycle = cur
    #         return True
        
    #     visited.add(cur)
        
    #     for v in adj[cur]:
    #         if v == par: # False parent detect
    #             continue
            
    #         if dfs(v, cur):
    #             if startCycle != -1:
    #                 cycle.add(v)
                
    #             if cur == startCycle:
    #                 startCycle = -1 # stop adding to cycle when reaching to the start cycle point
                
    #             return True

    #     return False
    
    # dfs(1, -1)
    # print(cycle)
    # for u, v in reversed(edges):
    #     if u in cycle and v in cycle:
    #         return [u, v]
    
    # return []
    
    
    # ===================== UNION FIND ========================= #
    pars = [i for i in range(len(edges) + 1)]
    rank = [1 for i in range(len(edges) + 1)]
    
    def find(u):
        while u != pars[u]:
            u = pars[u]
        return u
    
    def join(u, v):
        pu = find(u)
        pv = find(v)
        
        if pu == pv: # already join
            return False
        
        if rank[pu] > rank[pv]: # join with pu
            pars[pv] = pu
            rank[pu] += rank[pv]
        else: # join with pv
            pars[pu] = pv
            rank[pv] += rank[pu]
        
        return True
    
    for u, v in edges:
        if not join(u, v):
            return [u, v]
    
    return []            
    
                

    
    
edges = [[1,2],[1,3],[2,3]]


res = findRedundantConnection(edges)
print('res', res)