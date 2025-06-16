import heapq
from collections import Counter
def reorganizeString( s: str) -> str:
    counter = Counter(s)
    
    print(counter)
    
    
    # have to put char with bigger counter first
    # after that minus counter and put that char outside of heap queue
    # check until heap is empty
    heap = []
    for k in counter:
        heap.append((-counter[k], k)) # count, char
    heapq.heapify(heap)
    
    res = ''
    temp = None
    while len(heap):
        count, char = heapq.heappop(heap)
        print('tempt', temp)
        if temp:
            heapq.heappush(heap, temp)
            temp = None
            
        if len(res) and res[-1] == char:
            return ''
        
        res += char
        print(count, char)
        print('========')
        count += 1
        if count != 0:
            temp = (count, char)
    # print(res)
    if len(res) != len(s): return ''
    return res
 
    
s = "aaab"
res = reorganizeString(s)
print('res', res)