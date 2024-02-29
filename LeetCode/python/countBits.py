def countBits(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
        
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    recent = 2
    
    if n <= 2:
        return dp

    for i in range(1,n):
        if 2 ** i > n:
            break
        dp[2**i] = 1
    print(dp)
    for i in range(3,n+1):
        if dp[i] == 1:
            recent = i
            continue
        dp[i] = dp[recent] + dp[i-recent]
        
    print(dp)
    return dp
countBits(0)