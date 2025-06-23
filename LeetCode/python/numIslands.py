
def numIslands(grid):
    
    # go through all cell in grid
    # if cell is not visited increase res by 1
    # and run dfs/bfs on it to mark all adjacent visited cells
    
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()
    def dfs(i, j):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or grid[i][j] == '0':
            return
        
        visited.add((i, j))
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
        
    res = 0
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == '0':
                continue
            
            if (i, j) not in visited:
                res += 1
                dfs(i, j)
    
    print(res)
    return res
    
    

    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","0","1"],
  ["1","1","0","0","0"],
  ["0","1","0","1","1"]
]

numIslands(grid)