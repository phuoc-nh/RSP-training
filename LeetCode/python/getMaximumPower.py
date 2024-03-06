def getMaximumPower(power):
  maxPower = max(power)
  
  dp = [0 for i in range(maxPower+1)]
  
  for p in power:
    dp[p] += p
    
  n1 = dp[1]
  n2 = dp[2]
  
  for i in range(3, len(power)+1):
    dp[i] = max(dp[i] + dp[i-2], dp[i-2])
    
  return dp[len]
power = [1,1,1,2]
  