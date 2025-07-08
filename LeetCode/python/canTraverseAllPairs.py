import math
def canTraverseAllPairs(nums) -> bool:
    # build adj list
    adj = {}
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if math.gcd(nums[i], nums[j]) > 1:
                if i not in adj:
                    adj[i] = []
                adj[i].append(j)
                
                if j not in adj:
                    adj[j] = []
                adj[j].append(i)
    print(adj)    
    visited = set() 
    def dfs(cur):
        visited.add(cur)
        for v in adj[cur]:
            if v in visited:
                continue
            
            dfs(v)
    dfs(0)
    
    print(visited)
    
    if len(visited) == n:
        return True
    
    return False

    
    # traverse from 0
    
    # if visit all nodes
    # return true
    
    
    
    
nums = [2,3,6]

canTraverseAllPairs(nums)