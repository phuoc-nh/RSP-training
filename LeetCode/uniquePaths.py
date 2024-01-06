def uniquePaths(m, n):
    dp = [[0 for i in range(n)] for j in range(m)]
    

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    for d in dp:
        print(d)            
    return dp[m-1][n-1]
    

m = 3
n = 7
print(uniquePaths(m, n))