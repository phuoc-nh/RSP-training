from collections import deque
import heapq
def networkDelayTime(times, n: int, k: int):
    adj = [[] for i in range(n+1)]
    for u, v, w in times:
        # if u not in adj:
        #     adj[u] = []
        adj[u].append((v, w))
    queue = []
    queue.append((0, k))    
    visited = set()
    res = 0
    
    while len(queue):
        w1, u = heapq.heappop(queue)
        
        if u in visited:
            continue
        
        res = w1
        visited.add(u)
        
        for v, w2 in adj[u]:
            if v in visited:
                continue
            
            heapq.heappush(queue, (w2 + w1, v))
            
    # print('res', res)
    # print(visited)
    
    return res if len(visited) == n else -1
    
times = [[1,2,1]]

n = 2
k = 1

print(networkDelayTime(times, n, k))