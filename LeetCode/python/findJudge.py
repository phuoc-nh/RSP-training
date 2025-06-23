from collections import defaultdict
def findJudge(n: int, trust):
    outgoing = defaultdict(int)
    incoming = defaultdict(int)
    
    for u, v in trust:
        outgoing[u] += 1
        incoming[v] += 1
    
    for i in range(1, n+1):
        if outgoing[i] == 0 and incoming[i] == n-1:
            return i
        
    return -1
    
    # this is my solution
    # adj = {}
    # rev_adj = {}
    # for u, v in trust:
    #     if v not in adj:
    #         adj[v] = []
    #     adj[v].append(u)
        
    #     if u not in rev_adj:
    #         rev_adj[u] = []
    #     rev_adj[u].append(v)
        
        
    # print(adj)
    # print(rev_adj)
    
    # for i in range(1, n+1):
    #     if i not in adj: continue
    #     if len(adj[i]) == (n-1):
    #         foundJudge = True
    #         for u in adj[i]:
    #             if i not in rev_adj[u]:
    #                 foundJudge = False
    #         if i in rev_adj:
    #             foundJudge = False
            
    #         if foundJudge: return i
            
    # return -1
    
    
n = 2
trust = [[1,2]]

# n = 3
# trust = [[1,3],[2,3]]

# n = 3
# trust = [[1,3],[2,3],[3,1]]

res = findJudge(n, trust)
print('res', res)