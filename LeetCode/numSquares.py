import math

def numSquares(n):
    squares = [i ** 2 for i in range(math.floor(n ** 0.5) + 1)]
    
    dp = [math.inf for i in range(n+1)]
    dp[0]=0
    for i in range(n+1):
        for square in squares:
            if i - square < 0:
                continue
            else:
                dp[i] = min(1 + dp[i - square], dp[i])
    print(dp[n])
    return dp[n]
print(numSquares(12))