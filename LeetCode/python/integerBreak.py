def integerBreak(n: int) -> int:
    memo = {}
    def dfs(cur):
        if cur <= 3:
            return cur
        
        if cur in memo:
            return memo[cur]
        
        res = 0
        # print(cur)
        for i in range(1, cur):
            val = dfs(i) * dfs(cur - i)
            
            res = max(res, val)
        
        memo[cur] = res 
        return res
    res = dfs(n)
    print('res', res)
    
    if n == 2: return 1
    if n == 3: return 2
    
    return dfs(n)
    
    
res = integerBreak(2)
