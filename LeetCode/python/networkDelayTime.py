import heapq

def networkDelayTime(times, n: int, k: int):
    adj = [[] for i in range(n+1)]

    for u, v, w in times:
        adj[u].append((v, w))
    
    heap = []
    heap.append((0, k))
    res = 0
    heapq.heapify(heap) 
    visited = set()    

    while len(heap):
        weight, node = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        
        res = max(res, weight)
        visited.add(node)
        
        for v, w in adj[node]:
            if v in visited:
                continue
            
            heapq.heappush(heap, (weight + w, v))
    
    return res if len(visited) == n else -1
        
        
# ui, vi, wi
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2


print('>>>',networkDelayTime(times, n, k))