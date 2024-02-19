from queue import PriorityQueue

def findMaximizedCapital(k, w, profits, capital):
    pq = PriorityQueue()
    maxPq = PriorityQueue()

    for i in range(len(capital)):
        pq.put((capital[i], profits[i]))
    res = w
    for i in range(k):
        print('>>',pq.queue[0][0])
        while not pq.empty() and w >= pq.queue[0][0]:
            print(w, pq.queue[0][0])
            _, pro = pq.get()
            maxPq.put(-pro)
        
        temp = -maxPq.get() if not maxPq.empty() else 0
        res += temp  
        w += temp
        
    return res

k = 1
w = 2
profits = [1,2,3]
capital = [1,1,2]
findMaximizedCapital(k, w, profits, capital)