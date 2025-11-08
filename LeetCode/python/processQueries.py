import heapq
def processQueries(c: int, connections, queries):
    # create connected group
    # node to group id
    # group id to nodes, these nodes are put in min heap
    # create a set to store offline stations
    # pop out to get a valid station
    adj = [[] for i in range(c + 1)]

    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
    id = 0
    
    groups = {} # map group id to nodes
    
    # traverse to create group, bfs or dfs
    visited = set()
    stack = []
    
    nodeToGroupId = {}
    
    for i in range(1, c+1):
        if i in visited:
            continue
        
        stack.append(i)
        visited.add(i)
        group = []
        group.append(i)
        nodeToGroupId[i] = id
        
        while len(stack):
            node = stack.pop()
            
            for nei in adj[node]:
                if nei in visited:
                    continue
                
                visited.add(nei)
                group.append(nei)
                stack.append(nei)
                nodeToGroupId[nei] = id
        
        # finish 
        heapq.heapify(group)
        groups[id] = group
        id += 1
    
    
    print(groups)
    disables = set()
    res = []
    for type, node in queries:
        if type == 2:
            disables.add(node)
            continue
        
        if node not in disables:
            res.append(node)
            continue
        
        # type is 1 now
        groupId = nodeToGroupId[node]
        group = groups[groupId]
        
        while len(group) and group[0] in disables:
            heapq.heappop(group)
        
        if len(group):
            res.append(group[0])
        else:
            res.append(-1)
    
    print(res)
    return res
    
c = 5
connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
processQueries(c, connections, queries)