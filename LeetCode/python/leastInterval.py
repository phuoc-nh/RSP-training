import heapq
from queue import Queue
from collections import Counter
def leastInterval(tasks, n):
	counter = Counter(tasks)
	maxHeap = [-i for i in counter.values()]
	heapq.heapify(maxHeap)
	
	q = Queue()
	time = 0
	while not q.empty() or maxHeap:
		time +=1 
		if maxHeap:
			top = heapq.heappop(maxHeap)+1
			if top != 0:
				q.put((top, time + n))
	
		if not q.empty() and time >= q.queue[0][1]:
			top = q.get()
			heapq.heappush(maxHeap, top[0])
	return time
		
tasks = ["A","A","A", "B","B","B"]
n = 3
print(leastInterval(tasks, n))
  
