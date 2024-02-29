from queue import PriorityQueue
INF = 1e9
class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
    
    def __lt__(self, other):
        return self.weight <= other.weight 

def main():
    V, E = map(int, input().split())
    graph = [[] for i in range(V)]    
    visited = [False for i in range(V)]
    dist = [INF for i in range(V)]
    path = [-1 for i in range(V)]
    for i in range(E):
        u, v, w =  map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    
    # print(graph)
    src = 0
    q = PriorityQueue()
    q.put(Node(src, 0))
    dist[src] = 0
    
    while not q.empty():
        top = q.get()
        id = top.id
        visited[id] = True
        for v in graph[id]:
            idv = v.id
            weightv = v.weight
            if not visited[idv] and weightv < dist[idv]:
                q.put(Node(idv, weightv))
                path[idv] = id 
                dist[idv] = weightv

    print(path)
    print(dist)
main()