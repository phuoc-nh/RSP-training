from queue import PriorityQueue

def mostBooked(n, meetings):
    meetings.sort()
    
    availableRooms = PriorityQueue()
    for i in range(n):
        availableRooms.put(i)

    usedRooms = PriorityQueue()
    count = [0 for i in range(n)]

    for start, end in meetings:
        while not usedRooms.empty() and start >= usedRooms.queue[0][0]:
            top = usedRooms.get()
            availableRooms.put(top[1])
        
        if availableRooms.empty():
            endTime, room = usedRooms.get()
            end = endTime + (end - start)
            
            availableRooms.put(room)

        room = availableRooms.get()
        usedRooms.put((end, room))
        count[room] += 1
        
    return count.index(max(count))
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
mostBooked(n, meetings)



