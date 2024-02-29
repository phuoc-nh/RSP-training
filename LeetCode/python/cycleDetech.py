from queue import Queue
t = int(input())
for i in range(t):
    n, a, b = map(int, input().split()) # M, V

    graph = [[] for i in range(n+1)]
    
    for i in range(n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    cyclePoint = None
    def dfs(u, visited, parent):
        global cyclePoint
        visited.add(u)
        # print('u', u)
        for v in graph[u]:
            if v not in visited:
                if dfs(v, visited, u):
                    return True
            elif parent != v:
                # print('cycle', parent, v)
                cyclePoint = v
                return True
    
    dfs(b, visited, -1)
    # print('cyclePoint', cyclePoint)

    def bfs(src, des):
        if src == des:
            return 0
        visited = set()
        visited.add(src)
        distance = 1
        q = Queue()
        q.put(src)
        
        while not q.empty():
            for _ in range(q.qsize()):
                u = q.get()
                for v in graph[u]:
                    if v == des:
                        return distance
                    if v not in visited:
                        visited.add(v)
                        q.put(v)
            distance += 1
            
    # calculate distance from cyclePoint to a 
    aDistance = bfs(a, cyclePoint)
    bDistance = bfs(b, cyclePoint)
    if bDistance < aDistance:
        print('Yes')
    else:
        print('No')

    # calculate distance from cyclePoint to b 
    
    
    
                
        


    