from queue import PriorityQueue
INF = 1e9
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    
    def __lt__(self, other):
        return self.dist <= other.dist 

def main():
    V, E = map(int, input().split())
    graph = [[] for i in range(V)]    
    dist = [INF for i in range(V)]
    path = [-1 for i in range(V)]
    for i in range(E):
        u, v, w =  map(int, input().split())
        graph[u].append(Node(v, w))
        
    src = 0 
    pq = PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0

    # for el in graph:
    #     for u in el:
    #         print(u.id, u.dist)

    while not pq.empty():
        u = pq.get()
        for v in graph[u.id]:
            if u.dist + v.dist < dist[v.id]:
                path[v.id] = u.id 
                dist[v.id] = u.dist + v.dist
                pq.put(Node(v.id, dist[v.id]))
    
    print(dist)
    print(path)         
main()