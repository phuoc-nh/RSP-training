def canFinish(numCourses, prerequisites):
    graph = [[] for i in range(numCourses)]
    visited = set()
    path = set()

    for p in prerequisites:
        graph[p[1]].append(p[1])
    print(graph)
    res = [True]
    retPath = []
    def dfs(i):
        if i in visited and i in path:
            res[0] = False
            return
        if i in visited:
            return
        print(i)
        visited.add(i)
        path.add(i)
        retPath.append(i)
        for u in graph[i]:
            dfs(u)
            
        path.remove(i)
    
    for i in range(numCourses):
        if i not in visited:
            dfs(i)
    print(res)
    print(retPath)
    return retPath
    
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
res = canFinish(numCourses, prerequisites)
