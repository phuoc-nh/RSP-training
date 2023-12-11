# def recursiveDfs(u):
#     visited[u] = True
#     for v in graph[u]:
#         if not visited[v]:
#             recursiveDfs[v]
#     resTopo.append(u)

# def topoSort():
#     visited = [False] * V
#     for i in range(V):
#         if not visited[i]:
#             recursiveDFS(i)
            
#     resTopo.reverse()
    
def main():
    
    V, E = map(int, input().split())
    graph = [[] for i in range(V)]
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
    # print(graph)
    # print(v)
    visited = [False] * V
    topoSort = []
    # print(visited)
    def recursiveDfs(u):
        visited[u] = True
        print(u)
        for v in graph[u]:
            if not visited[v]:
                recursiveDfs(v)
        topoSort.append(u)
    
    for i in range(V):
        if not visited[i]:
            recursiveDfs(i)
            
    topoSort.reverse()
    print('topo sort', topoSort)
main()