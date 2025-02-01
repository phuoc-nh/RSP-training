def countServers(grid) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    rowCount = [0] * ROWS
    colCount = [0] * COLS

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                rowCount[i] += 1
                colCount[j] += 1

    res = 0

    print(rowCount)
    print(colCount)
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1 and (rowCount[i] > 1 or colCount[j] > 1):
                res += 1
                
    print(res)
    return res
    
    
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

countServers(grid)