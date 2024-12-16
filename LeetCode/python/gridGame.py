def gridGame(grid):
    n = len(grid[0])
    
    row1 = grid[0].copy()
    row2 = grid[1].copy()
    
    
    
    for i in range(1, n):
        row1[i] += row1[i-1]
        row2[i] += row2[i-1]
    print(row1)
    print(row2)
    pos = 0
    maxRobot1 = 0 
    res = float('inf')
    for i in range(n):
        
        top = row1[-1] - row1[i]
        bot = row2[i-1] if i > 0 else 0
        
        second = max(top, bot)
        res = min(res, second)
    print(res)
    return res
    
    
grid = [[20,3,20,17,2,12,15,17,4,15],
        [20,10,13,14,15,5,2,3,14,3]]


gridGame(grid)