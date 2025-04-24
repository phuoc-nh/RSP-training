import math
def numSquares(n):
    squares = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        squares.append(i * i)
        
    memo = {}
    def dfs(cur):
        if cur == 0: 
            return 0
        
        if cur in memo:
            return memo[cur]
        
        res = math.inf
        
        for square in squares:
            if square <= cur:
                res = min(res, 1 + dfs(cur - square))
        memo[cur] = res
        return res
    
    res = dfs(n)
    print('>>>>', res)
    
    return res
    
    
print(numSquares(12))