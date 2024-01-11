def countVowelPermutation(n):
    genMap = {
        'a': {
            'e': 1
        },
        'e': {
            'a': 1,
            'i': 1
        },
        'i': {
            'a': 1,
            'e': 1,
            'o': 1,
            'u': 1,
        },
        'o': {
            'i': 1,
            'u': 1
        },
        'u': {
            'a': 1
        }
    }

    dp = [0 for i in range(n+1)]

    dp[1] = {
        'a': 1,
        'e': 1,
        'i': 1,
        'o': 1,
        'u': 1,
    }
    
    for i in range(2, n+1):
        temp = {}
        for key, value in dp[i-1].items():
            for k,v in genMap[key].items():
                temp[k] = temp.get(k, 0) + v * value
        
        dp[i] = temp
        
    # print(dp[n])
    return sum(dp[n].values()) % (1_000_000_000 + 7)
    
print(countVowelPermutation(5))