def largestPathValue(colors: str, edges):
    n = len(colors)
    adj = [[] for i in range(n)]
    for u, v in edges:
        adj[u].append(v)
        
    # print('adj', adj)
    
    visited = set()
    path = set()
    
    dp = [[0] * 3 for i in range(n)]
    
    def dfs(node):
        if node in path:
            return -1 
        
        if node in visited:
            return 0

        path.add(node)
        visited.add(node)

        colorIndex = ord(colors[node]) - ord('a')
        dp[node][colorIndex] = 1
        
        for nei in adj[node]:
            if dfs(nei) == -1:
                return -1
            for c in range(3):
                dp[node][c] = max(
                    dp[node][c],
                    (1 if colorIndex == c else 0) + dp[nei][c]
                )
        
        path.remove(node)
        return 0
        
    res = 0
    for i in range(n):
        if dfs(i) == -1:
            return -1
        res = max(res, max(dp[i]))
    # for d in dp:
    #     print(d)
        
    print('re', res)
    return res
            
    
    
    
colors = "a"
edges = [[0,0]]

x = largestPathValue(colors, edges)
print('x', x)