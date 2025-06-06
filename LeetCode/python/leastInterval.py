import heapq
from collections import Counter, deque
def leastInterval(tasks, n):
    counter = Counter(tasks)
    heap = [-v for v in counter.values()]
    heapq.heapify(heap)
    
    queue = deque()
    time = 0
    
    while len(heap) or len(queue):
        time += 1
        print(heap, queue)
        if not len(heap):
            cnt, time = queue.popleft() # count, time
            heapq.heappush(heap, cnt)
            continue
        
        count = heapq.heappop(heap)
        # -3
        count += 1
        if count != 0:
            queue.append((count, time + n ))
        
        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.popleft()[0])
        
			
        
    print('time', time)
    return time
    
	
		
tasks = ["A","A","A","B","B","B"]
n = 2

tasks = ["A","C","A","B","D","B"]
n = 1

tasks = ["A","A","A", "B","B","B"]
n = 3
print(leastInterval(tasks, n))
  
