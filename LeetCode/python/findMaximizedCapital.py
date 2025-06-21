import heapq
def findMaximizedCapital(k, w, profits, capital):
    # need to process projects  within current capacity to find the highest return value project
    # finish the project and increase the current capacity,
    # continue until geg k projects
    cap_pro = []
    max_pro = []
    
    
    for i in range(len(profits)):
        cap_pro.append((capital[i], profits[i]))
    heapq.heapify(max_pro)
    heapq.heapify(cap_pro)
    for _ in range(k):
        
        while len(cap_pro) and cap_pro[0][0] <= w:
            cap, pro = heapq.heappop(cap_pro)
            heapq.heappush(max_pro, -pro)
        
        w += -heapq.heappop(max_pro) if len(max_pro) else 0
    #     count += 1
    #     if count == k:
    #         return w
        # find project within capital and maximise profit
        # at the top of heap, can only get project with min capital, there may be some project with w yield more profits

    return w
    
    

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]
res = findMaximizedCapital(k, w, profits, capital)
print('res', res)