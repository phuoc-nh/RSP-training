def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    memo = {}
    def dfs(length):
        if length > high:
            return 0
        
        if length in memo:
            return memo[length]
        
        
        res = 1 if length >= low else 0
        
        res += dfs(length + zero) + dfs(length + one)
        memo[length] = res
        return res
        
    
    res = dfs(0)    
    print(res)
    
    return res
low = 3
high = 3
zero = 1
one = 1

countGoodStrings(low, high, zero, one)