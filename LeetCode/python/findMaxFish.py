def findMaxFish(grid) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    
    res = 0
    visited = set()
    def dfs(row, col):
        if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or grid[row][col] == 0:
            
            return 0
        
        
        fishes = grid[row][col]
        
        visited.add((row, col))
        
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            fishes += dfs(row+dr, col + dc)
        
        
        return fishes
        
        
        # visited = set()
        # visited.add((i, j))
        # fishes = grid[i][j]
        
        # s = [(i, j)]
        
        # while len(s):
        #     r, c = s.pop()
            
        #     for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        #         row = dr + r
        #         col = dc + c   
                
        #         if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or grid[row][col] == 0:
        #             continue
                
                
        #         fishes += grid[row][col]
        #         s.append((row, col))
        #         visited.add((row, col))
        
        # print(fishes)
                
        # return fishes
        
                
                
        
    
    
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] != 0:
                res = max(dfs(i, j), res)
    print('res', res)
    return res
    
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
findMaxFish(grid)