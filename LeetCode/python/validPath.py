from queue import Queue
def validPath(n, edges, source, destination):
    adj = [[] for i in range(n)]
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    q = Queue()
    q.put(source)
    visited = set()
    set.add(source)

    while not q.empty():
        u = q.get()
        
        if u == destination:
            return True
        
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.put(v)

    return False