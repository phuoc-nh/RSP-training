def gridGame(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    
    
    for i in range(1, COLS):
        grid[0][i] += grid[0][i-1]
        grid[1][i] += grid[1][i-1]
        
        
    res = float('inf')
    for i in  range(COLS):
        
        firstRobotR1 = grid[0][i]
        firstRobotR2 = (grid[1][-1] - (grid[1][i-1] if i > 0 else 0))
        
        totalRobot1 = firstRobotR1 + firstRobotR2
        
        secondRobotR1 = grid[0][-1] - firstRobotR1
        secondRobotR2 = grid[1][i-1] if i > 0 else 0
        
        
        
        # print('Robot1', totalRobot1)   
        # print('Robot2', secondRobotR1 + secondRobotR2)   
        res = min(max(secondRobotR2, secondRobotR1), res)
        
    # print(grid)
    
    # print(res)
    return res
    


grid = [[1,3,1,15],[1,3,3,1]]

gridGame(grid)