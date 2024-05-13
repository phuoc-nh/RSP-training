def matrixScore(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    for i in range(ROWS):
        if grid[i][0] == 0:
            for j in range(COLS):
                grid[i][j] = 1 - grid[i][j]
    
    # for g in grid:
    #     print(g)           
    # print()
    for i in range(1, COLS):
        countOne = 0
        for j in range(ROWS):
            if grid[j][i] == 1:
                countOne += 1
        
        if countOne < ROWS - countOne:
            for k in range(ROWS):
                grid[k][i] = 1 - grid[k][i]
        
    res = 0
    for row in grid:
        binary = ''.join(map(str, row))
        res += int(binary, 2)
    # for g in grid:
    #     print(g)
    print(res)
    return res
grid = [
    [0,1,1],
    [1,1,1],
    [0,1,0]]
matrixScore(grid)
            
    