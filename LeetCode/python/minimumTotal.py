def minimumTotal(triangle) -> int:
    
    cache = {} # key is (row, col)
    
    def dfs(row, col):
        if row >= len(triangle):
            return 0
        
        if (row, col) in cache:
            return cache[(row, col)]
        
        res = 1e9
        
        res = min(res, triangle[row][col] + dfs(row+1,col), triangle[row][col] + dfs(row+1,col+1))
        cache[(row, col)] = res
        return res
    
    res = dfs(0,0)
    print(res)
    
    return res
    
    
    
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

minimumTotal(triangle)