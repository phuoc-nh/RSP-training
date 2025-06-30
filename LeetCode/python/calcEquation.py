from collections import deque
def calcEquation(equations, values, queries):
    adj = {}
    
    for i in range(len(equations)):
        u, v = equations[i]
        if u not in adj:
            adj[u] = []
        adj[u].append((v, values[i]))
        
        if v not in adj:
            adj[v] = []
            
        adj[v].append((u, 1/ values[i]))
        
    
    def bfs(source, target):
        if target not in adj or source not in adj:
            return -1
        
        queue = deque()
        queue.append((source, 1)) # source and init value
        visited = set()
        visited.add(source)
        while len(queue) != 0:
            cur, val = queue.popleft()
            if cur == target:
                return val

            for next in adj[cur]:
                v, nextVal = next
                if v in visited:
                    continue
                visited.add(v)
                queue.append((v, nextVal * val))
        
        return -1    
    # for each query
    # run bfs from source to target
    # if target found return the value 
    res = []
    for source, target  in queries:
        temp = bfs(source, target)
        # print('temp', temp)
        res.append(temp)
    print('res', res)
    return res  

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

calcEquation(equations, values, queries)