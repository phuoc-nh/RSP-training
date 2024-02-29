def cherryPickup(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    cache = {}
    def dfs(r, c1, c2):
        if (r, c1, c2) in cache:
            return cache[(r, c1, c2)]        

        if c1 == c2 or min(c1, c2) < 0 or max(c1,c2) >= COLS:
            return 0
        
        if r == ROWS - 1:
            return grid[r][c1] + grid[r][c2]
        
        res = 0
        for dc1 in [-1,0,1]:
            for dc2 in [-1,0,1]:
                res = max(
                    res,
                    dfs(r+1, c1+dc1, c2+dc2)
                )
                
        cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2] 
        return cache[(r, c1, c2)]
    
    return dfs(0, 0, COLS - 1)
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(cherryPickup(grid))