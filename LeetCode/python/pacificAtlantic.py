def pacificAtlantic(heights) :
	# pacific condition row < 0 or col < 0
	# atlantic condition  row >= ROWS or col >= COLS
    ROWS = len(heights)
    COLS = len(heights[0])

    adjacent = 1
    
    def dfs(i, j, visited, prevHei):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or heights[i][j] < prevHei:
            return
        
        visited.add((i, j))
        dfs(i+1, j, visited, heights[i][j])
        dfs(i-1, j, visited, heights[i][j])
        dfs(i, j+1, visited, heights[i][j])
        dfs(i, j-1, visited, heights[i][j])
       
    # get all pacific cells
    # run bfs/dfs on them and store as pacific cells
    pacific = set()
    atlantic = set()
    for i in range(ROWS):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, COLS - 1, atlantic, heights[i][COLS-1])
        
    for j in range(COLS):
        dfs(0, j, pacific, heights[0][j])
        dfs(ROWS - 1, j, atlantic, heights[ROWS-1][j])
        
    # print(pacific)
    # print(atlantic)
    res = []
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) in pacific and (i, j) in atlantic:
                res.append([i, j])
    
    print(res)
    return res    
    
    # if 

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
pacificAtlantic(heights)