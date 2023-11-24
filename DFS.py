MAX = 10
graph = [[] for i in range(MAX)]
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]

def DFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    
    stack = []
    stack.append(s)
    visited[s] = True
    
    while len(stack):
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                stack.append(v)

def recursiveDFS(s):
    for v in graph[s]:
        if not visited[v]:
            visited[s] = True
            path[v] = s
            recursiveDFS(v)

def recursiveDFS(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            path[v] = s
            recursiveDFS(v)

V, E = map(int, input().split())
for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
# recursiveDFS(0)
DFS(0)
print('path',path)
print(graph)
# print