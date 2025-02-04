def checkIfPrerequisite(numCourses, prerequisites, queries):
    adj = {}
    
    for i in range(numCourses):
        adj[i] = []
    
    for u, v in prerequisites:
        adj[u].append(v)
            
    res = []
    prereqMap = {}
    # print(adj)
    def dfs(u):
        
        if u not in prereqMap:
            prereqMap[u] = set()
            
            for v in adj[u]:
                prereqMap[u] |= dfs(v)
                
            prereqMap[u].add(u)
        
        return prereqMap[u]
        
            
    for i in range(numCourses):
        dfs(i)
        
    print(adj)
    print(prereqMap)
    
    for u, v in queries:
        res.append(v in prereqMap[u])
        
    print(res)
        
    return res
    
    
	
numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]] 
    
# numCourses = 2
# prerequisites = [[1,0]]
# queries = [[0,1],[1,0]]

# numCourses = 4
# prerequisites = [[2,3],[2,1],[0,3],[0,1]]
# queries = [[0,1]]



checkIfPrerequisite(numCourses, prerequisites, queries)