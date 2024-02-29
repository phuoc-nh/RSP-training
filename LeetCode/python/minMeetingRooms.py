from queue import PriorityQueue

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[0])
    pq = PriorityQueue()
    
    for cur in intervals:
        if pq.empty():
            pq.put(cur[1]) # put end time
            continue
        print('>>',pq.queue[0])
        if pq.queue[0] > cur[0]: # end time
            pq.put(cur[1])
        else:
            pq.get()
            pq.put(cur[1])
            
    print(pq.qsize())   
    return pq.qsize()            

intervals = [[0,30],[5,10],[15,20]]
minMeetingRooms(intervals)