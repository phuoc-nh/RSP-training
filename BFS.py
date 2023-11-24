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
    visited[s] = True
    q.put(s)
    
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                q.put(v)
                visited[v] = True
                path[v] = u

V, E = map(int, input().split())
for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
   
BFS(0) 

print(path)
print(graph)
