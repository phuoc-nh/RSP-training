from queue import Queue

def shortestPathBinaryMatrix(grid):
    if grid[0][0] == 1:
        return -1

    n = len(grid)
    DIRECTIONS = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1),
        (1,1),
        (-1,1),
        (1,-1),
        (-1,-1)
    ]
    
    visited = [[False for i in range(n)] for i in range(n)]
    
    q = Queue()
    q.put((0,0, 1))

    visited[0][0] = True
    
    while not q.empty():
        r, c, p = q.get()
        for dr, dc in DIRECTIONS:
            row = r + dr
            col = c + dc
            
            
            if 0 <= row < n and 0 <= col < n and not visited[row][col] and grid[row][col] == 0:
                print(row, col)
                visited[row][col] = True
                q.put((row,col,p+1))  
            if row == n and col == n:
                return p
    
    return -1
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))