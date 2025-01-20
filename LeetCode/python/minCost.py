import heapq

dir = [[0, 1], [0,-1], [1, 0], [-1, 0]]

def minCost(grid) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    
    minCosts = [[float('inf') for i in range(COLS)] for j in range(ROWS)]
    # print(minCosts)
    
    minCosts[0][0] = 0
    
    queue = [[0, 0, 0]] # cost, r, c
    
    heapq.heapify(queue)
    
    while len(queue):
        cost, r, c = heapq.heappop(queue)
        
        # print(cost, r, c)
        
        for i in range(len(dir)):
            dr, dc = dir[i]
            row = r + dr
            col = c + dc
            
            newCost = minCosts[r][c] + (1 if i != grid[r][c] - 1 else 0)
            
            if row >= ROWS or row < 0 or col >= COLS or col < 0:
                continue
            
            if newCost >= minCosts[row][col]:
                continue
            
            minCosts[row][col] = newCost
            
            heapq.heappush(queue, [newCost, row, col])
            
            
    print(minCosts)
    
    return minCosts[ROWS-1][COLS-1]
    
    
    
    
    
    
grid = [[1,2],[4,3]]
res = minCost(grid)
print(res)