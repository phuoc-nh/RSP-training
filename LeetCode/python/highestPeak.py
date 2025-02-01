from collections import deque

def highestPeak(isWater):
    ROWS = len(isWater)
    COLS = len(isWater[0])
    
    # for w in isWater:
    #     print(w)
        
        
    queue = deque()
    
    visited = set()
    
        
    for i in range(ROWS):
        for j in range(COLS):
            if isWater[i][j] == 1:
                isWater[i][j] == 0
                queue.append((i, j))
                visited.add((i, j))
                
    cur = 0
    while len(queue):
        
        curLen = len(queue)
        for i in range(curLen):
            r, c = queue.popleft()
            print(r, c)
            isWater[r][c] = cur
            for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                row = r + dr 
                col = c + dc 
                
                
                if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited:
                    continue
                
                    
                visited.add((row, col))
                queue.append((row, col))
                
                
        cur += 1                
                
                
    print(isWater)
    return isWater
    
                

            
        
        

isWater = [[0,0,1],[1,0,0],[0,0,0]]

highestPeak(isWater)