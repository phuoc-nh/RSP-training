import heapq
def carPooling(trips, capacity: int) -> bool:
    reordered = [(start, end, cap) for cap, start, end in trips]
    reordered.sort()
    heap = [] # end, cap
    heapq.heapify(heap)    
    cur = 0
    for trip in reordered:
        start, end, cap = trip
        while len(heap) and heap[0][0] <= start:
            prevEnd, prevCap = heapq.heappop(heap)
            # print('prevEnd, prevCap', prevEnd, prevCap, start)
            cur -= prevCap
        cur += cap
        # print(cur)
        if cur > capacity:
            return False
        
        heapq.heappush(heap, (end, cap))
        
    return True
    
    
    
# trips = [[2,1,5],[3,3,7]]
# capacity = 4

trips = [[2,1,5],[3,3,7]]
capacity = 5

res = carPooling(trips, capacity)

print('res', res)
    