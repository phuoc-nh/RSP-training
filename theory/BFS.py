from queue import Queue

MAX = 10
graph = [[] for i in range(MAX)]
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]

def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    
    q = Queue()
    q.put(s)
    visited[s] = True
    # Set initial color
    
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                # Toggle child's color here
                q.put(v)

def findPath(s, f):
    if path[f] == -1:
        print('No path')
    
    while True:
        print(f)
        f = path[f]
        if s == f:
            print(f)
            break
V, E = map(int, input().split())
for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
BFS(0) 
findPath(0, 5)
print(path)
print(graph)
