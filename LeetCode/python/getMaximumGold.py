def getMaximumGold(grid) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    
    visited = set()
    
    
    def dfs(i, j, visited):
        
        if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited or grid[i][j] == 0:
            return 0
        
        res = grid[i][j]
        visited.add((i, j))
        
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            row = dr + i
            col = dc + j
            res = max(res,  grid[i][j] + dfs(row, col, visited))
            
        # visited.remove((i, j))
        return res
    
    res = 0
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] != 0:
                print(grid[i][j])
                res = max(res, dfs(i, j, set()))
    
    print(res)    
    return res
    
    
    
grid = [[0,6,0],[5,8,7],[0,9,0]]

getMaximumGold(grid)