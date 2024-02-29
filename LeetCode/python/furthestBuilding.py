from queue import PriorityQueue

def furthestBuilding(heights, bricks, ladders):
    pq = PriorityQueue()
    for i in range(len(heights)-1):
        diff = heights[i+1] - heights[i]
        if diff <= 0:
            continue

        bricks -= diff
        pq.put(-diff)

        if bricks < 0:
            if ladders <= 0:
                return i

            ladders -= 1
            bricks += -pq.get()
        
    return len(heights) -1 
    
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

print(furthestBuilding(heights, bricks, ladders))