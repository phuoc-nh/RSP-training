def largestIsland(grid):
    
    ROWS = len(grid)
    COLS = len(grid[0])
    islandsLabel = {}
    
    def dfs(i, j, label):
        
        stack = []
        # print('label', label)
        stack.append((i, j))
        visited = set()
        area = 1
        visited.add((i, j))
        
        
        while len(stack):
            r, c = stack.pop()
            
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                row = dr + r
                col = dc + c
                
                if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited:
                    continue
                # print(row, col)
                if grid[row][col] == 1:
                    area += 1
                    stack.append((row, col))
                    visited.add((row, col))
        
        
        # print('area', area)
        # print(visited)
        
        for r, c in visited:
            grid[r][c] = label
        islandsLabel[label] = area
            
        
    
    label = 2 # use to tag islands
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                dfs(i, j, label)
                label += 1
    res = 0
    
        
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 0:
                temp = 1 # try to flip it
                visited = set()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    row = dr + i
                    col = dc + j
                    
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited:
                        continue
                    
                    # if gri
                    if grid[row][col] in islandsLabel and grid[row][col] not in visited:
                        temp += islandsLabel[grid[row][col]]
                        visited.add(grid[row][col])
                    res = max(temp, res)
            else:
                res = max(res, islandsLabel[grid[i][j]])
                
                        
                        
    
    # print(grid)
    for g in grid:
        print(g)
    
    print(islandsLabel)
    
    print('res', res)
    
    return res
    
    
grid = [[1,1],[1,1]]
largestIsland(grid)