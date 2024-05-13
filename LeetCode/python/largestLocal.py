def largestLocal(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    res = []
    for i in range(ROWS - 3 + 1):
        res.append([])
        for j in range(COLS - 3 + 1):
            maximum = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    maximum = max(maximum, grid[k][l])
            
            res[i].append(maximum)
            
    print(res)
    return res
grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
largestLocal(grid)
    