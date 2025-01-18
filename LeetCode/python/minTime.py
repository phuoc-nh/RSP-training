def minTime(n: int, edges, hasApple) -> int:
    
    graph = [[] for i in range(n)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = set()
    
    def dfs(u):
        time = 0
        visited.add(u)
        # print(u)
        for v in graph[u]:
            if v in visited:
                continue
            # print('>>>>', v, hasApple[v])
            timeChild = dfs(v)
            print(timeChild, v)
            print(hasApple[v], v)
            if hasApple[v] or timeChild:
                time += 2 + timeChild
                
        return time
    print(graph)
    return dfs(0)

            
    
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]

res = minTime(n, edges, hasApple)
print('===')
print(res)