import heapq
def swimInWater(grid):
    n = len(grid)
    visited = set()
    queue = [(grid[0][0], 0, 0)] # time, i, j
    
    res = 0
    
    while len(queue):
        time, i, j = heapq.heappop(queue)
        if (i, j) in visited:
            continue
        
        res = time
        if i == n - 1 and j == n - 1:
            return res
        visited.add((i, j))
        
        for dr, dc in [[1, 0], [-1, 0], [0,1], [0,-1]]:
            row = dr + i
            col = dc + j
            
            if row >= n or col >= n or row < 0 or col < 0 or (row, col) in visited:
                continue
            
            heapq.heappush(queue, (max(grid[row][col], time), row, col))
            
    return res
    
    
grid = [[0,2],[1,3]]
res = swimInWater(grid)
print('res', res)