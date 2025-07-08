def uniquePathsWithObstacles(obstacleGrid):
    # if obstacleGrid[0][0] == 1:
    #     return 0
    
    # ROWS = len(obstacleGrid)
    # COLS = len(obstacleGrid[0])
    
    # for i in range(ROWS):
    #     for j in range(COLS):
    #         if obstacleGrid[i][j] == 1:
    #             obstacleGrid[i][j] = 'X'
            
    
    
    # obstacleGrid[0][0] = 1
    
    # for i in range(ROWS):
    #     for j in range(COLS):
    #         if  obstacleGrid[i][j] == 'X':
    #             continue
    #         if i == 0 and j == 0: # row == 0
    #             continue
            
    #         if i == 0:
    #             obstacleGrid[i][j] = obstacleGrid[i][j-1]
    #             continue
            
    #         if j == 0:
    #             obstacleGrid[i][j] = obstacleGrid[i-1][j]
    #             continue
            
    #         # i > 0 and j > 0
    #         preCol = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != 'X' else 0
    #         preRow = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != 'X' else 0
            
    #         obstacleGrid[i][j] = preCol + preRow
            
                
    # # for o in obstacleGrid:
    # #     print(o)
            
    # return obstacleGrid[ROWS-1][COLS-1] if 
    if obstacleGrid[0][0] == 1:
        return 0
    
    ROWS = len(obstacleGrid)
    COLS = len(obstacleGrid[0])

    if obstacleGrid[ROWS-1][COLS-1] == 1:
        return 0
    
    
    obstacleGrid[0][0] = 1
    
    for i in range(ROWS):
        for j in range(COLS):
            if i == 0 and j == 0:
                continue
            if  obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
                continue
            
            top = obstacleGrid[i-1][j] if i > 0 else 0
            left = obstacleGrid[i][j - 1] if j > 0 else 0
            
            obstacleGrid[i][j] += top + left
            
    
    # for o in obstacleGrid:
    #     print(o)
                

    return obstacleGrid[ROWS-1][COLS-1] 
                
    
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

res =uniquePathsWithObstacles(obstacleGrid)
print(res)