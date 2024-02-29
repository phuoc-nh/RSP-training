import math

def coinChange(coins, amount):
    dp = [math.inf for i in range(amount+1)]
    dp[0] = 0
    
    for i in range(1, amount+1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])
                
    # print(dp)

    return dp[-1] if dp[-1] != math.inf else -1

coins = [2]
amount = 3
print(coinChange(coins, amount))