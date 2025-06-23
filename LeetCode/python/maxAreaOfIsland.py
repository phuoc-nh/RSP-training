def maxAreaOfIsland(grid):
    
    ROWS = len(grid)
    COLS = len(grid[0])
    
    def dfs(i, j):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or grid[i][j] == 0:
            return 0
        visited.add((i, j))
        return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i, j + 1) + dfs(i, j - 1)
    
    
    
    visited = set()
    res = 0
    # t = dfs(0, 2)
    # print('t', t)
    
    for i in range(ROWS):
        for j in range(COLS):
            # if grid[i][j] == 0:
            #     continue
            t = dfs(i, j)
            res = max(res, t)
    
    print(res)
    return res

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
maxAreaOfIsland(grid)
            
            
