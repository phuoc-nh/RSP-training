
def findPaths(m, n, maxMove, startRow, startColumn):
    MOD = 1_000_000_007
    dp = {}
    def dfs(r, c, moves):
        if (r, c, moves) in dp:
            return dp[(r,c,moves)]
        if moves < 0:
            return 0    
        if r < 0 or r >= m or c < 0 or c >= n: # outbound here
            return 1
        print(r,c,moves)
        dp[(r,c,moves)] = dfs(r+1, c, moves-1) + dfs(r-1, c, moves-1) + dfs(r, c+1, moves-1) + dfs(r, c-1, moves-1)
        return dp[(r,c,moves)]
    res = dfs(startRow, startColumn, maxMove)
    print(dp)
    print(res)
    return res % MOD
m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
findPaths(m, n, maxMove, startRow, startColumn)
    