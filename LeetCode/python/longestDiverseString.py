import heapq
def longestDiverseString(a: int, b: int, c: int) -> str:
    heap = []
    for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
        if count != 0:
            heap.append((-count, char))
            
    heapq.heapify(heap)
    res = ''
    # put the most count char
    # if cur char and prev char is equal
    # put this char aside
    
    aside = None
    while len(heap):
        count, char = heapq.heappop(heap)
        # after pop heap, consider to put aside into heap because later on this will be replaced
        print('count', count)
        print('char', char)
        print('ch=======')
        if aside:
            heapq.heappush(heap, aside)
            aside = None
        
        res += char
        if len(res) > 1 and res[-1] == res[-2]:
            if count + 1 != 0:
                aside = (count + 1, char)
        else:
            if count + 1 != 0:
                heapq.heappush(heap, (count+1, char))   



    print(res)
        
    return res
            
    
    	
# a = 1
# b = 1
# c = 7

a = 2
b = 4
c = 1
longestDiverseString(a, b, c)