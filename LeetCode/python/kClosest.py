import heapq

def kClosest(points, k: int):
    def distance(point):
        return point[0] ** 2 + point[1] ** 2
    heap = []
    heapq.heapify(heap)
    
    for point in points:
        heapq.heappush(heap, (distance(point), point))
        
    res = []
    print(heap)
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])
        
    print(res)
    return res

points = [[1,3],[-2,2]]
k = 1
kClosest(points, k)