# def largestPathValue(colors, edges):
#     graph = [[] for i in range(len(colors))]

#     for edge in edges:
#         graph[edge[0]].append(edge[1])
        
#     visited = set()
#     counter = {}
#     res = [0]
    
#     def dfs(i):
        
#         if i in visited:
#             res[0] = -1
#             return
        
#         visited.add(i)
#         counter[colors[i]] = counter.get(colors[i], 0) + 1
#         if counter[colors[i]] > res[0]:
#             res[0]= counter[colors[i]]

#         for u in graph[i]:
#             dfs(u)
            
#         visited.remove(i)
#         counter[colors[i]] = counter.get(colors[i], 0) - 1
#         if counter[colors[i]] == 0:
#             del counter[colors[i]]
    
#     for i in range(len(colors)):
#         dfs(i)
#     print(res[0])
#     return res[0]

def largestPathValue(colors, edges):
    adj = [[] for i in range(len(colors))]
    for edge in edges:
        adj[edge[0]].append(edge[1])
    print('adj', adj)
    def dfs(i):
        if i in path:
            return float('inf')
        
        if i in visited:
            return 0

        visited.add(i)
        path.add(i)
        colorIndex = ord(colors[i]) - ord('a')
        # print('colorIndex', colorIndex)
        dp[i][colorIndex] += 1

        for u in adj[i]:
            ret = dfs(u)
            if ret == float('inf'):
                return float('inf')

            for j in range(25):
                dp[i][j] = max(
                    dp[u][j],
                    (1 if colorIndex == j else 0) + dp[u][j],
                    dp[i][j]
                )

        path.remove(i)
        return max(dp[i])
    visited = set()
    path = set()
    dp = [[0 for i in range(25)] for j in range(len(colors))]
    res = 0

    for i in range(len(colors)):
        res = max(res, dfs(i))
    print(res if res != float('inf') else -1)
    return res if res != float('inf') else -1

colors = "hhqhuqhqff"
edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]

largestPathValue(colors, edges)

