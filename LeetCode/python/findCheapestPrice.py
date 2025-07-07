import heapq
def findCheapestPrice(n: int, flights, src: int, dst: int, k: int):
    adj = [[] for i in range(n)]
    for u, v, w in flights:
        adj[u].append((v, w))
    
    dist = [float('inf') for i in range(n)]
    dist[src] = 0
    
    queue = []
    queue.append((0, src)) # distance, node
    stops = 0
    
    while stops <= k and len(queue):
        
        
        # traverse all the node in the queue to fight possible next destination within 'stops' stops
        l = len(queue)
        
        for i in range(l):
            d, node = heapq.heappop(queue)
            
            for v, w in adj[node]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(queue, (dist[v], v))
        
        stops += 1
        
        
    return -1 if dist[dst] == float('inf') else dist[dst]
    
    
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

res = findCheapestPrice(n, flights, src, dst, k)
print('res', res)