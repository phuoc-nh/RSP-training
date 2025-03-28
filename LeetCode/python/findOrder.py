def findOrder(numCourses, prerequisites):
    # graph = [[] for i in range(numCourses)]
    
    
    # for p in prerequisites:
    #     graph[p[1]].append(p[0])
        
    # res = []
    # visited = set()
    # path = set()
    
    # def dfs(i):
    #     if i in path:
    #         return False
    #     if i in visited:
    #         return True
        
    #     path.add(i)
    #     for k in graph[i]:
    #         if dfs(k) == False:
    #             return False
            
    #     visited.add(i)
    #     path.remove(i)
    #     res.append(i)
    #     return True
    
    # for i in range(numCourses):
    #     if dfs(i) == False:
    #         return []

    # print(res)
    # return res
    
    
    
    
    
    
    
    
    
    
    adj = {}
    
    for i in range(numCourses):
        adj[i] = []
    
    for cour, pre in prerequisites:
        adj[cour].append(pre)
        
    print('adj', adj)
        
    visited = set()
    res = []
    path = set()
        
    def dfs(cour):
        if cour in path:
            # cycle here
            return False
        
        if cour in visited:
            return True
        
        path.add(cour)
        visited.add(cour)

        for pre in adj[cour]:
            if not dfs(pre): return False
        
        path.remove(cour)
        res.append(cour)
        
        return True
    
    
    for i in range(numCourses):
        if not dfs(i): return []
    
    # print(res)
    
    
    
        
    return res

    
    
# numCourses = 2
# prerequisites = [[0,1]]
numCourses = 2
prerequisites = [[1,0]]
# [0,2,1,3]
print(findOrder(numCourses, prerequisites))