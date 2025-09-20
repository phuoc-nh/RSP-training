def closedIsland(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()
    
    def onBorder(r, c):
        if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
            return True
        
        return False
    
        
    
    
    
    def dfs(r, c):
        stack = []
        stack.append((r, c))
        # visited.add((r, c))
        
        isOnBorder = False
        
        while len(stack):
            i, j = stack.pop()
            # print(i, j)
            visited.add((i, j))
            if onBorder(i, j):
                isOnBorder = True
                
            
            
            for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                row = dr + i
                col = dc + j
                
                if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited or grid[row][col] == 1:
                    continue
                # visited.add((row, col))
                stack.append((row, col))
        
        
        return isOnBorder
                
                
    res = 0
    # print(visited)
    
    # x = dfs(1, 1)
    # print('x', x)
    # if not x:
    #     res += 1
    # print(visited)
    
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) not in visited and grid[i][j] == 0:
                # print(visited)
                
                x = dfs(i, j)
                # print('x', x)
                if not x:
                    res += 1
                # print(visited)
                
                    
    # print('res', res)
    return res
    
    
    
# grid = [
#     [1,1,1,1,1,1,1,0],
#     [1,0,0,0,0,1,1,0],
#     [1,0,1,0,1,1,1,0],
#     [1,0,0,0,0,1,0,1],
#     [1,1,1,1,1,1,1,0]]

# grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]

closedIsland(grid)