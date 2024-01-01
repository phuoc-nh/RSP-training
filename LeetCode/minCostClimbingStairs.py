def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0 for i in range(n + 1)]
    # dp[0] = cost[0]
    # dp[1] = cost[1]
    
    for i in range(2,n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
        
    # print(dp)
    
    return dp[n]

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))