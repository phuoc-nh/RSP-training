def pacificAtlantic(heights) :
    ROWS = len(heights)
    COLS = len(heights[0])
    
    
    
    
    # put pacific points
    # run dfs to collect cells that pacific water could reach to
        
    def dfs(i, j, visited, prev):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or heights[i][j] < prev:
            return
        
        visited.add((i, j))
        for dr, dc in [[1,0], [-1,0], [0,-1],[0,1]]:
            row = i + dr
            col = j + dc
            dfs(row, col, visited, heights[i][j])
    
    pacific = []
    for i in range(COLS):
        pacific.append((0, i))
    
    for i in range(ROWS):
        pacific.append((i, 0))
    visitedPacific = set()
    for i, j in pacific:
        dfs(i, j, visitedPacific, -1)
        
    atlantic = []
    for i in range(COLS):
        atlantic.append((ROWS-1, i))
    
    for i in range(ROWS):
        atlantic.append((i, COLS-1))
    
    
    visitedAtl = set()
    for i, j in atlantic:
        dfs(i, j, visitedAtl, -1)
        
    res = []
    
    for i, j in visitedPacific:
        if (i, j) in visitedAtl:
            res.append([i, j])
    # print(res)
    # print(visitedPacific)
    # print(visitedAtl)
    return res
 
    # do the same with atlantic
    
    # compare 2 visited list, get common cells 
    # return them
        


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

pacificAtlantic(heights)