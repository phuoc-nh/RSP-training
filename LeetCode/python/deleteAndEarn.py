from collections import Counter

def deleteAndEarn(nums) -> int:
    
    counter = Counter(nums)
    
    unique = list(counter.keys())
    unique.sort()
    if len(unique) <= 2:
        return max(n * counter[n] for n in unique)
    
    dp = unique.copy()
    dp[0] = unique[0] * counter[unique[0]]
    dp[1] = unique[1] * counter[unique[1]]
    dp[2] = max(unique[2] * counter[unique[2]] + dp[0], dp[1])
    print(dp.copy())
    for i in range(3, len(unique)):
        cur = unique[i] * counter[unique[i]]
        dp[i] = max(cur + dp[i-2], cur + dp[i - 3], dp[i-2])
        
    
    print(unique)
    print(counter)
    print(dp)
    
    print(max(dp))
    return max(dp)

nums = [3,4,2]
deleteAndEarn(nums)
    