def longestIncreasingPath(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    dp = {}
    def dfs(i,j, preVal):
        if i < 0 or i >= ROWS or j < 0 or j >= COLS or matrix[i][j] <= preVal:
            return 0
        
        if (i, j) in dp:
            return dp[(i,j)]
        
        res = 1
        res = max(res, 1 + dfs(i+1,j,matrix[i][j]))
        res = max(res, 1 + dfs(i-1,j,matrix[i][j]))
        res = max(res, 1 + dfs(i,j+1,matrix[i][j]))
        res = max(res, 1 + dfs(i,j-1,matrix[i][j]))

        dp[(i,j)] = res
        return res
    for i in range(ROWS):
        for j in range(COLS):
            dfs(i,j,-1)
    
    return max(dp.values)
matrix = [[9,9,4],[6,6,8],[2,1,1]]
longestIncreasingPath(matrix)