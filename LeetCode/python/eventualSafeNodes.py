def eventualSafeNodes(graph):
    
    adjMap = [[] for i in range(len(graph))]
    print(graph)
    for g in graph:
        if g[0] in adjMap:
            adjMap[g[0]].append(g[1])
        else:
            adjMap[g[0]] = [g[1]]
            
    print(adjMap)
    
    
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
eventualSafeNodes(graph)