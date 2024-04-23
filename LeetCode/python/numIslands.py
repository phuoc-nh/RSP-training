from queue import Queue

def numIslands(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    
    res = 0
    
    def bfs(i, j):
        q = Queue()
        q.put((i, j))
        grid[i][j] = 0
        while not q.empty():
            r, c = q.get()   
            for dr, dc in [(1,0), (0,1), (-1, 0), (0,-1)]:
                row = dr + r
                col = dc + c
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == '1':
                    q.put((row, col))
                    grid[row][col] = 0
                    
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == '1':
                bfs(i, j)
                res += 1
                
    print(res)
    return res

    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

numIslands(grid)