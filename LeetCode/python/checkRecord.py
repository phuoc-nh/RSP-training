def checkRecord(n):
    # cache = {}
    
    MOD = 1000000007
    cache1 = [[[-1] * 3 for i in range(3)] for j in range(n+1)]
    
    

    # print(cache1)
    def backtrack(n, absence, late):
        if absence >= 2 or late >= 3:
            return 0
        
        # if (n, absence, late) in cache:
        #     return cache[(n, absence, late)]
        
        if cache1[n][absence][late] != -1:
            return cache1[n][absence][late]
        
        if n == 0:
            return 1
        
        count = backtrack(n - 1, absence, 0)
        count = (count + backtrack(n- 1, absence + 1, 0)) % MOD
        count = (count+ backtrack(n-1, absence, late+1)) % MOD
        
        cache1[n][absence][late]= count
        
        return count
    
    res = backtrack(n, 0, 0)
    print(res)
    return res
n = 2
checkRecord(n)