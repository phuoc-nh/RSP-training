from collections import deque

def shortestBridge(grid) -> int:
    n = len(grid)
    directions = [[1,0], [-1,0],[0,1],[0,-1]]
    def dfs(i, j):
        s = deque()
        visited = set()
        visited.add((i, j))     
        
        s.append((i, j)) 
        
        # collect island
        while len(s):
            r, c = s.pop()
            
            for dr, dc in directions:
                row = dr + r
                col  = dc + c
                
                if row < 0 or row >= n or col < 0 or col >= n or (row, col) in visited:
                    continue
                
                
                if grid[row][col] == 1:
                    s.append((row, col))
                    visited.add((row, col))
                    # grid[row][col] = 0
                

        span = 0
        
        print(s)
        
        # starting point 
        for x in visited:
            s.append(x)
        
        while len(s):
            lenS = len(s)
            
            for _ in range(lenS):
                r, c = s.popleft()
                # if grid[r][c] == 1 and ():
                #     return span
                
                for dr, dc in directions:
                    row = dr + r
                    col  = dc + c
                    
                    if row < 0 or row >= n or col < 0 or col >= n or (row, col) in visited:
                        continue
                    
                    if grid[row][col] == 1:
                        return span
                
                    s.append((row, col))
                    visited.add((row, col))
            span += 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                return dfs(i, j)
    
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
res = shortestBridge(grid)

print(res)