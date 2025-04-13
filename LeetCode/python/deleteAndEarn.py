from collections import Counter

def deleteAndEarn(nums) -> int:
    
    counter = Counter(nums)
    
    unique = list(counter.keys())
    unique.sort()
    
    dp = [0] * len(unique)
    
    dp[0] = unique[0] * counter[unique[0]]
    
    for i in range(1, len(unique)):
        if unique[i] - unique[i-1] > 1:
            dp[i] = dp[i-1] + unique[i] * counter[unique[i]]
        else:
            dp[i] = max(dp[i-1], unique[i] * counter[unique[i]] + dp[i-2])
            
    print(unique)
    print(counter)
   
    print(dp)
    
    return max(dp)
    # return max(dp)

nums = [3,4,2]
deleteAndEarn(nums)
    