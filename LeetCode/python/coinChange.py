
# def coinChange(coins, amount):
    
#     cache = {}
#     def dfs(amount):
#         if amount == 0:
#             return 0
        
#         if amount in cache:
#             return cache[amount]
        
#         res = 1e9
        
#         for num in coins:
#             if amount - num >= 0:
#                 res = min(res, 1 + dfs(amount - num))
                
#         cache[amount] = res
                
#         return res
    
#     res = dfs(amount)
#     return res if res != 1e9 else -1
        
        
def coinChange(coins, amount):
    dp = [1e9] * (amount + 1)
    dp[0] = 0
    
    for curAmount in range(1, amount + 1):
        for coin in coins:
            if curAmount - coin >= 0:
                dp[curAmount] = min(dp[curAmount], 1 + dp[curAmount - coin])
                
    return dp[amount] if dp[amount] != 1e9 else -1
            
        
            
    
coins = [1,3,4,5]
amount = 7
print(coinChange(coins, amount))