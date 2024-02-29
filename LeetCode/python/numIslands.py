def numIslands(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    result = 0
    
    def dfs(i,j):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] != '1':
            return
        
        grid[i][j] = 0
        
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == '1':
                result += 1
                dfs(i, j)

    # print(result)

    return result

    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

numIslands(grid)