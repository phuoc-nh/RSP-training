def uniquePaths(m, n):
    dp = [[0] * n for i in range(m)]
    
    # the first row always one
    for i in range(n):
        dp[0][i] = 1
    
    # same with the first col
    for i in range(m):
        dp[i][0] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] += dp[i-1][j] + dp[i][j-1]
        
    
    
    # for d in dp:
    #     print(d)
        
    return dp[m-1][n-1]
    

m = 3
n = 7
print(uniquePaths(m, n))