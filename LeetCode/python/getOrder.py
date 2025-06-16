import heapq
def getOrder(tasks):
    tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
    tasks.sort()
    print(tasks)
    heap = []
    i = 0
    current = tasks[0][0]
    
    while i < len(tasks) and tasks[i][0] == current:
        heap.append((tasks[i][1], tasks[i][2]))
        i += 1
    
    # print(heap)
    # print(current)
    # print(i)
    
    heapq.heapify(heap)
    
    res = []
    while len(heap):
        time, index = heapq.heappop(heap)
        res.append(index)
        current += time

        if i < len(tasks) and current < tasks[i][0] and not len(heap):
            current = tasks[i][0]
        
        while i < len(tasks) and tasks[i][0] <= current:
            heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
            i += 1
            
    print(res)
    
    
    return res
    
    
tasks = [[1,2],[2,4],[3,2],[4,1]]
# tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# tasks = [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]

getOrder(tasks)

