from queue import PriorityQueue

def findMaximizedCapital(k, w, profits, capital):
    pq = PriorityQueue()
    maxPq = PriorityQueue()
    for i in range(len(profits)):
        pq.put((capital[i], profits[i]))
    for _ in range(k):
        while not pq.empty() and w >= pq.queue[0][0]:
            top = pq.get()
            maxPq.put(-top[1])
        maxProfit = maxPq.get() * -1 if not maxPq.empty() else 0
        w += maxProfit
    print('w', w)
    return w
    
    
    

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]
findMaximizedCapital(k, w, profits, capital)