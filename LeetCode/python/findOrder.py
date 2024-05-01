def findOrder(numCourses, prerequisites):
    graph = [[] for i in range(numCourses)]
    
    
    for p in prerequisites:
        graph[p[1]].append(p[0])
        
    res = []
    visited = set()
    path = set()
    
    def dfs(i):
        if i in path:
            return False
        if i in visited:
            return True
        
        path.add(i)
        for k in graph[i]:
            if dfs(k) == False:
                return False
            
        visited.add(i)
        path.remove(i)
        res.append(i)
        return True
    
    for i in range(numCourses):
        if dfs(i) == False:
            return []

    print(res)
    return res
numCourses = 2
prerequisites = [[0,1]]
print(findOrder(numCourses, prerequisites))