import heapq
def minCostConnectPoints(points):
    n = len(points)
    # build adjacency list
    adj = [[] for i in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            p1 = points[i]
            p2 = points[j]
            distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            
            adj[i].append((distance, j))
            adj[j].append((distance, i))
            
    # print(adj)
    res = 0
    queue = [(0, 0)] # first index point, current distance
    visited = set()
    
    while len(visited) < n:
        # print(queue)
        # print('visited', visited)
        dist, p = heapq.heappop(queue)
        if p in visited:
            continue
        
        res += dist
        visited.add(p)
        
        for newDist, v in adj[p]:
            heapq.heappush(queue, (newDist, v))
    
    print('res', res)
    
    return res
    

points = [[3,12],[-2,5],[-4,1]]
minCostConnectPoints(points)
