def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2) 
    
    dp = [[0] * (n + 1) for i in range(m + 1)]
    print(dp)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(text1[j-1])
            print(text2[i-1])
            if text1[j-1] == text2[i-1]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
            print('---')
    # print(dp)
    for d in dp:
        print(d)
        
    return dp[m][n]

text1 = "bsbininm"

text2 = "jmjkbkjkv" 

longestCommonSubsequence(text1, text2)
    